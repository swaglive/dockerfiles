# Usage

```Dockerfile
FROM s6-overlay as s6-overlay

FROM alpine:3.7

COPY --from s6-overlay / /
```
