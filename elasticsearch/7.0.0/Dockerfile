FROM gradle:5.4.1 as builder

RUN wget -O- https://github.com/sing1ee/elasticsearch-jieba-plugin/archive/v7.0.0.tar.gz| tar -xzv -C . --strip 1 && \
    gradle pz
    
RUN unzip build/distributions/elasticsearch-jieba-plugin-7.0.0.zip -d /home/gradle/dist

###

FROM elasticsearch:7.0.0

COPY --chown=elasticsearch:root --from=builder /home/gradle/dist  /usr/share/elasticsearch/plugins/jieba

