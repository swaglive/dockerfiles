FROM        golang:alpine3.6

RUN         apk add --no-cache --virtual .build-deps \
                git && \
            go get -u github.com/googlecloudplatform/gcsfuse && \
            mkdir -p /rootfs/usr/local/bin/ && \
            mv $GOPATH/bin/gcsfuse /usr/local/bin/gcsfuse && \
            apk del .build-deps && \
            mkdir -p /data

ENTRYPOINT ["gcsfuse"]
CMD        ["--help"]
