FROM        alpine:3.8 as dockerize

ENV         VERSION=0.6.1
RUN         wget -q -O - https://github.com/jwilder/dockerize/releases/download/v$VERSION/dockerize-alpine-linux-amd64-v$VERSION.tar.gz | tar xz -C /usr/local/bin && \
            chmod +x /usr/local/bin/dockerize
