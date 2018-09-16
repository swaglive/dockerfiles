FROM        alpine:3.8

ENTRYPOINT  ["nsenter", "--target", "1", "--mount", "--uts", "--ipc", "--net", "--pid", "--"]

RUN         apk add --no-cache --virtual .run-deps \
                util-linux
