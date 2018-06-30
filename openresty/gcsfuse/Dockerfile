FROM        golang:1.10-alpine3.7 as gcsfuse

RUN         apk add --no-cache --virtual .build-deps \
                build-base \
                git && \
            go get -u github.com/googlecloudplatform/gcsfuse && \
            mv $GOPATH/bin/gcsfuse /usr/local/bin/gcsfuse && \
            chmod +x /usr/local/bin/gcsfuse

###

FROM        openresty/openresty:alpine

ENV         S6_BEHAVIOUR_IF_STAGE2_FAILS 2
ENV         S6_CMD_WAIT_FOR_SERVICES 1

RUN         mkdir -p /usr/share/nginx/html && \
            rm -rf /etc/nginx/conf.d/*
EXPOSE      80/tcp
ENTRYPOINT  ["/init"]
CMD         ["nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;"]

RUN         apk --no-cache add --virtual .run-deps \
                fuse \
                ca-certificates

            # s6-overlay
RUN         wget -q -O - https://github.com/just-containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz | tar xz -f - -C / && \
            # auth0/nginx-jwt
            mkdir -p /lua && \
            wget -O - https://github.com/auth0/nginx-jwt/releases/download/v1.0.1/nginx-jwt.tar.gz | tar x -f - -C /lua

COPY        --from=gcsfuse /usr/local/bin/gcsfuse /usr/local/bin/gcsfuse
COPY        rootfs /
