FROM            alpine:3.8

ARG             VERSION=4.9

VOLUME          ["/root/.config"]
ENTRYPOINT      ["gsutil"]
CMD             ["version", "-l"]

RUN             apk add --no-cache --virtual .build-deps \
                    curl && \
                curl -sL https://storage.googleapis.com/pub/gsutil_$VERSION.tar.gz | tar xz && \
                find /gsutil -type f -name "*.pyc" -delete && \
                find /gsutil -type f -name "*.pyo" -delete && \
                find /gsutil -type d -name "__pycache__" -delete && \
                chmod +x gsutil/gsutil && \
                mv gsutil/ /usr/local/bin && \
                apk add --no-cache --virtual .run-deps \
                    python \
                    py-crcmod \
                    ca-certificates && \
                apk del .build-deps
