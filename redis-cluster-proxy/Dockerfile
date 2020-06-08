FROM        alpine:3.11 as builder
ENV         VERSION=1.0-beta2

RUN         apk add \
              build-base \
              linux-headers \
              git \
              curl

RUN         curl -L https://github.com/RedisLabs/redis-cluster-proxy/archive/$VERSION.tar.gz | tar xvz

WORKDIR     /redis-cluster-proxy-$VERSION

RUN         make
RUN         make install

###

FROM        alpine:3.11
ENTRYPOINT  ["redis-cluster-proxy"]

COPY        --from=builder /usr/local/bin/redis-cluster-proxy /usr/local/bin/redis-cluster-proxy
