FROM            node:12.12-alpine as builder

ENV             NODE_ENV=production

WORKDIR         /usr/src/app

RUN             apk --no-cache add --virtual .build-deps \
                  build-base

COPY            package.json .
COPY            yarn.lock .
RUN             yarn install

###

FROM            node:12.12-alpine

WORKDIR         /usr/src/app
ENV             PATH=/usr/src/app/node_modules/.bin:$PATH
ENV             NODE_ENV=production

ENTRYPOINT      ["node"]
CMD             ["proxy.js"]

RUN             apk --no-cache add --virtual .run-deps \
                  ca-certificates

COPY            --from=builder /usr/src/app/node_modules node_modules
COPY            proxy.js .
