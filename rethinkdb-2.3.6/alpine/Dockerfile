FROM      alpine:edge

VOLUME    ["/data"]
WORKDIR   /data

          # process cluster webui
EXPOSE    28015 29015 8080

CMD       ["rethinkdb", "--bind", "all"]

RUN       apk add --no-cache rethinkdb
