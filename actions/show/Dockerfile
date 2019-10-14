
FROM docker:stable

LABEL version="1.0.0"

LABEL "version"="1.0.0"
LABEL "maintainer"="Rammus Xu <rammus.xu@swag.live>"
LABEL "com.github.actions.name"="GCR Login"
LABEL "com.github.actions.description"="use GCLOUD_AUTH"
LABEL "com.github.actions.icon"="terminal"
LABEL "com.github.actions.color"="green"

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]