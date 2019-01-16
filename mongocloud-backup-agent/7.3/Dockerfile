FROM        alpine:3.8 as builder

ARG         VERSION=7.3.0.1023-1

RUN         apk add --no-cache --virtual .build-deps \
                curl ca-certificates && \
            curl -sL -o - https://cloud.mongodb.com/download/agent/automation/mongodb-mms-backup-agent-$VERSION.linux_x86_64.tar.gz | tar xz && \
            mkdir -p /etc/mongodb-mms-backup-agent && \
            mv mongodb-mms-backup-agent-$VERSION.linux_x86_64/mongodb-mms-backup-agent /usr/local/bin/mongodb-mms-backup-agent && \
            mv mongodb-mms-backup-agent-$VERSION.linux_x86_64/local.config /etc/mongodb-mms-backup-agent/backup-agent.config && \
            chmod +x /usr/local/bin/mongodb-mms-backup-agent && \
            sed -i 's/mmsGroupId=/mmsGroupId={{ default .Env.MMS_GROUP_ID "" }}/' /etc/mongodb-mms-backup-agent/backup-agent.config && \
            sed -i 's/mmsApiKey=/mmsApiKey={{ default .Env.MMS_API_KEY "" }}/' /etc/mongodb-mms-backup-agent/backup-agent.config

###

FROM        alpine:3.8 as dockerize

ARG         DOCKERIZE_VERSION=v0.6.1

RUN         wget -q https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
            tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
            rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

###

FROM        debian:9-slim

VOLUME      /var/lib/mongodb-mms-automation
VOLUME      /var/log/mongodb-mms-automation
VOLUME      /data

ENTRYPOINT  ["dockerize", "-template", "/etc/mongodb-mms-backup-agent/backup-agent.config:/etc/mongodb-mms-backup-agent/backup-agent.config", "mongodb-mms-backup-agent"]
CMD         ["-c", "/etc/mongodb-mms-backup-agent/backup-agent.config"]

COPY        --from=dockerize /usr/local/bin/dockerize /usr/local/bin/dockerize

RUN         apt-get update && \
            apt-get install -y libsasl2-2 ca-certificates && \
            rm -rf /var/lib/apt/lists/* && \
            ln -sf /dev/stdout /var/log/mongodb-mms-automation/backup-agent.log

COPY        --from=builder /usr/local/bin/mongodb-mms-backup-agent /usr/local/bin/
COPY        --from=builder /etc/mongodb-mms-backup-agent/backup-agent.config /etc/mongodb-mms-backup-agent/backup-agent.config
