FROM        python:3.6-alpine3.7 as poetry

ENV         POETRY_VERSION=0.12.11
ENV         PATH=/root/.poetry/bin:$PATH

RUN         apk add --no-cache --virtual .run-deps \
                ca-certificates \
                curl && \
            curl -q https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
