FROM        openresty/openresty:alpine

RUN         mkdir -p /var/cache/nginx/storage /var/cache/nginx/authorization && \
            apk add --no-cache --virtual .run-deps \
              ca-certificates

COPY        conf.d/ /etc/nginx/conf.d/
