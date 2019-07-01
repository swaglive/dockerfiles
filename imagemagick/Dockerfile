FROM        alpine:3.9

WORKDIR     /usr/src/app

# ImageMagick need:
# - curl: fetch image from https://
# - msttcorefonts-installer, fontconfig: Even if you don't use it.
RUN         apk add --no-cache curl \
                            imagemagick \
                            msttcorefonts-installer \
                            fontconfig && \
            update-ms-fonts && \
            fc-cache -f

ENTRYPOINT [ "magick" ]