FROM        python:3.6.9-alpine3.10

ARG         SIMD_LEVEL=sse4

ENV         PYTHONPATH=/usr/src/app/lib
ENV         PYTHONOPTIMIZE=2

WORKDIR     /usr/src/app
EXPOSE      8888/tcp
ENTRYPOINT  ["dockerize", "-no-overwrite", "-template", "thumbor.conf.py.tmpl:thumbor.conf.py", "thumbor"]
CMD         ["-l", "debug", "-c", "thumbor.conf.py"]

COPY        --from=swaglive/dockerize:0.6.1 /usr/local/bin/dockerize /usr/local/bin/dockerize

RUN         apk add --no-cache --virtual .build-deps \
                build-base \
                curl-dev \
                libjpeg-turbo-dev \
                zlib-dev \
                tiff-dev \
                freetype-dev \
                lcms2-dev \
                libwebp-dev \
                openjpeg-dev \
                libpng-dev \
                libmemcached-dev && \
            # apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/testing --virtual .build-deps \
            #     libimagequant-dev
            pip install \
                thumbor==6.6.0 \
                pycurl==7.43.0.3 \
                tornado==5.1.1 \
                greenlet==0.4.15 \
                python-rapidjson==0.6.3 \
                tc-core==0.4.0 \
                # Memcached Storage
                thumbor-memcached==5.1.0 \
                pylibmc==1.6.0 \
                # Redis Storage
                tc-redis==1.0.1 \
                redis==2.10.6 \
                hiredis==0.2.0 \
                # Mongo Storage
                tc_mongodb==5.1.0 \
                pymongo==3.7.2 \
                # Thumbor-video
                https://github.com/swaglive/thumbor-video/archive/5f9ce7a88af66b4ed10bf0f75bff9805d2f92945.zip && \
            apk add --no-cache --virtual .run-deps \
                openjpeg \
                libjpeg-turbo \
                libjpeg-turbo-utils \
                libpng \
                freetype \
                libwebp \
                zlib \
                gifsicle \
                tiff \
                ffmpeg && \
#             apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/testing --virtual .run-deps \
#                 libimagequant && \
            pip uninstall -y pillow && \
            CC="cc -m$SIMD_LEVEL" pip -v install --force-reinstall --no-binary pillow-simd pillow-simd==5.3.0.post0 \
                --global-option="build_ext" --global-option="--debug" && \
            apk del --no-cache .build-deps

            # HACK - Python 3 support
RUN         sed -i 's/basestring = str/basestring = bytes/g' /usr/local/lib/python3.6/site-packages/thumbor/server.py && \
            sed -i "s/return encode_url(unquote(url).decode('utf-8'))/return encode_url(unquote(url))/g" /usr/local/lib/python3.6/site-packages/thumbor/loaders/http_loader.py && \
            sed -i "s/buffer.startswith('/buffer.startswith(b'/g" /usr/local/lib/python3.6/site-packages/thumbor/engines/__init__.py && \
            sed -i "s/.replace(b'\\\0', '')/.replace(b'\\\0', b'').decode('utf-8')/g" /usr/local/lib/python3.6/site-packages/thumbor/engines/__init__.py && \
            sed -i "s/' in e.message:/' in str(e):/g" /usr/local/lib/python3.6/site-packages/thumbor/handlers/__init__.py

            # HACK - rapidjson replacement for json
COPY        json.py lib/json.py

COPY        thumbor.conf.py thumbor.conf.py.tmpl
