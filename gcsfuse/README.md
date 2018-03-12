# Usage

```Dockerfile
FROM gcsfuse as gcsfuse

FROM alpine

COPY --from gcsfuse /usr/local/bin/gcsfuse /usr/local/bin/gcsfuse
```
