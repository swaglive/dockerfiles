FROM            alpine:edge

ARG             version="0.10.14-r0"
LABEL           caddy_version="$version"
ENV             ACME_AGREE="true"
ENV             ENABLE_TELEMETRY="false"

EXPOSE          80/tcp 443/tcp 2015/tcp
VOLUME          /root/.caddy /srv
WORKDIR         /srv

ENTRYPOINT      ["caddy"]
CMD             ["--conf", "/etc/Caddyfile", "--log", "stdout", "--agree"]
COPY            Caddyfile /etc/Caddyfile

RUN             apk add --no-cache \
                    caddy=$version
