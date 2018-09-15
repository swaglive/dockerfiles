FROM        alpine:3.8

ARG         VERSION=1.10.8
ENTRYPOINT  ["kubectl"]

RUN         wget -q https://storage.googleapis.com/kubernetes-release/release/v$VERSION/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl && \
            chmod +x /usr/local/bin/kubectl && \
            apk add --no-cache --virtual .run-deps \
                ca-certificates
