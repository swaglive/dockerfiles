const os = require('os');
const bunyan = require('bunyan');
const async = require('async');
const { PubSub } = require('@google-cloud/pubsub');
const fetch = require('node-fetch');
const jwt = require('jsonwebtoken');
const crypto = require('crypto');
const url = require('url');


const config = {
  SECRET_KEY: process.env.SECRET_KEY || 'secret-key',
  NOTIFY_ENDPOINT: process.env.NOTIFY_ENDPOINT,
  JWT_ISSUER: process.env.JWT_ISSUER || os.hostname(),

  PUBSUB_SUBSCRIPTION_NAMES: (process.env.PUBSUB_SUBSCRIPTION_NAMES || '').split(' ').filter(v => v),
  // NOTE: PUBSUB_FLOW_CONTROL_MAX_MESSAGES controls the concurrency of Job submissions
  //       not the concurrency of execution
  PUBSUB_FLOW_CONTROL_MAX_MESSAGES: Number(process.env.PUBSUB_FLOW_CONTROL_MAX_MESSAGES || 1),
  PUBSUB_NACK: Number(process.env.PUBSUB_NACK || 10),

  LOGGER: {
    name: process.LOG_NAME || 'proxy',
    level: process.env.LOG_LEVEL || 'info',
  },

  HTTP_HEADERS: {
    'X-Forwarded-Proto': 'https',
  },
  HTTP_USER_AGENT: process.env.HTTP_USER_AGENT || `pubsub-proxy/${ process.env.VERSION || "latest" } (${ os.hostname() })`,
};
config.JWT_KID = crypto.createHash('sha256').update(config.SECRET_KEY).digest('hex').substring(0, 8);
config.JWT_AUDIENCE = url.parse(config.NOTIFY_ENDPOINT).host;


// Initialize - Logger
const logger = bunyan.createLogger(config.LOGGER);


// Initialize - Google PubSub
const pubsub = new PubSub();
// Create Google Pubsub
const subscriptions = config.PUBSUB_SUBSCRIPTION_NAMES.map((name) => {
  logger.debug(`Subscribed to ${name}`);

  return pubsub.subscription(name, {
    // Note that flow control settings are not persistent across subscribers.
    flowControl: {
      maxMessages: config.PUBSUB_FLOW_CONTROL_MAX_MESSAGES,
      // allowExcessMessages: false,
      // maxExtension: 10,
    },
  }).on('error', (err) => {
    logger.error(err, 'Google PubSub subscription error');
  });
});


// Add shutdown hooks
const shutdown = (signal) => {
  logger.debug(`Received ${ signal }`);
  logger.info('Gracefully Shutting down');

  subscriptions.forEach((subscription) => {
    subscription.close();
  });
};
['SIGTERM', 'SIGINT'].forEach((signal) => {
  process.on(signal, shutdown);
  logger.debug(`Registered shutdown on ${ signal }`);
});

if (!config.NOTIFY_ENDPOINT) {
  logger.error(config, 'NOTIFY_ENDPOINT not set');
  process.exit(1);
}
logger.info(config, 'Initialization complete');


const handler = (message) => async.autoInject({
  body: (next) => {
    let { id, publishTime, attributes, data } = message;

    try {
      data = JSON.parse(data);
    } catch (err) {
      return next(err);
    }

    return jwt.sign({
      iss: config.JWT_ISSUER,
      aud: config.JWT_AUDIENCE,
      sub: message._subscriber._name,

      messageId: id,
      publishTime: publishTime,
      attributes: attributes,
      data: data,
    }, config.SECRET_KEY, {
      header: { kid: config.JWT_KID },
    }, next);
  },
  notify: (body, next) => {
    return fetch(config.NOTIFY_ENDPOINT, {
      method: 'POST',
      headers: {
        'User-Agent': config.USER_AGENT,
        ...config.HTTP_HEADERS,
      },
      body: body,
    })
      .then(
        (res) => next(null, res),
        (err) => next(err)
      );
  },
}, (err, results) => {
  if (err) {
    logger.error(err);
    return message.nack(config.PUBSUB_NACK);
  }

  let { body } = results;
  logger.info({
    endpoint: config.NOTIFY_ENDPOINT,
    body: body,
  }, 'Webhook success');
  return message.ack();
});

subscriptions.forEach((subscription) => subscription.on('message', handler));
