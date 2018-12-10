# Google Cloud Storage Proxy

Allows for access to Google Cloud storage with credentials automatically proxied into the request.

## Usage

* Currently uses Instance Metadata permissions for access to Google Cloud Storage
  * This means it inherits the permissions of the Instance when it was created (`scopes`)
  * Requires to be run in Google Cloud (or have access to the Google Instance Metadata API)
* The proxy will have access to any buckets/objects that the account has permission for (if it uses `storage-full` scope, then everything)

```
docker run -it --rm -p 80:80 swaglive/google-cloud-storage:0.1.0

curl http://127.0.0.1/my-bucket/hello/world.mp4
-> 200 OK
```


## TODO

* https://docs.nginx.com/nginx/admin-guide/content-cache/content-caching/#byte-range-caching
