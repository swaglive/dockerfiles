################################### Logging ####################################

## Logging configuration as json
## Defaults to: None
#THUMBOR_LOG_CONFIG = None

## Log Format to be used by thumbor when writing log messages.
## Defaults to: '%(asctime)s %(name)s:%(levelname)s %(message)s'
#THUMBOR_LOG_FORMAT = '%(asctime)s %(name)s:%(levelname)s %(message)s'

## Date Format to be used by thumbor when writing log messages.
## Defaults to: '%Y-%m-%d %H:%M:%S'
#THUMBOR_LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

################################################################################


################################### Imaging ####################################

## Max width in pixels for images read or generated by thumbor
## Defaults to: 0
#MAX_WIDTH = 0

## Max height in pixels for images read or generated by thumbor
## Defaults to: 0
#MAX_HEIGHT = 0

## Max pixel count for images read by thumbor
## Defaults to: 75000000.0
#MAX_PIXELS = 75000000.0

## Min width in pixels for images read or generated by thumbor
## Defaults to: 1
#MIN_WIDTH = 1

## Min width in pixels for images read or generated by thumbor
## Defaults to: 1
#MIN_HEIGHT = 1

## Allowed domains for the http loader to download. These are regular
## expressions.
## Defaults to: #    [
#    ]

#ALLOWED_SOURCES = #    [
#    ]


## Quality index used for generated JPEG images
## Defaults to: 80
#QUALITY = 80

## Exports JPEG images with the `progressive` flag set.
## Defaults to: True
#PROGRESSIVE_JPEG = True

## Specify subsampling behavior for Pillow (see `subsampling`               in
## http://pillow.readthedocs.org/en/latest/handbook/image-file-
## formats.html#jpeg).Be careful to use int for 0,1,2 and string for "4:4:4"
## notation. Will ignore `quality`. Using `keep` will copy the original file's
## subsampling.
## Defaults to: None
#PILLOW_JPEG_SUBSAMPLING = None

## Specify quantization tables for Pillow (see `qtables`               in
## http://pillow.readthedocs.org/en/latest/handbook/image-file-
## formats.html#jpeg). Will ignore `quality`. Using `keep` will copy the
## original file's qtables.
## Defaults to: None
#PILLOW_JPEG_QTABLES = None

## Specify resampling filter for Pillow resize method.One of LANCZOS, NEAREST,
## BILINEAR, BICUBIC, HAMMING (Pillow>=3.4.0).
## Defaults to: 'LANCZOS'
#PILLOW_RESAMPLING_FILTER = 'LANCZOS'

## Quality index used for generated WebP images. If not set (None) the same level
## of JPEG quality will be used.
## Defaults to: None
#WEBP_QUALITY = None

## Compression level for generated PNG images.
## Defaults to: 6
#PNG_COMPRESSION_LEVEL = 6

## Indicates if final image should preserve indexed mode (P or 1) of original
## image
## Defaults to: True
#PILLOW_PRESERVE_INDEXED_MODE = True

## Specifies whether WebP format should be used automatically if the request
## accepts it (via Accept header)
## Defaults to: False
#AUTO_WEBP = False

## Specifies whether a PNG image should be used automatically if the png image
## has no transparency (via alpha layer). WARNING: Depending on case, this is
## not a good deal. This transformation maybe causes distortions or the size
## of image can increase. Images with texts, for example, the result image
## maybe will be distorced. Dark images, for example, the size of result image
## maybe will be bigger. You have to evaluate the majority of your use cases
## to take a decision about the usage of this conf.
## Defaults to: False
#AUTO_PNG_TO_JPG = False

## Specify the ratio between 1in and 1px for SVG images. This is only used
## whenrasterizing SVG images having their size units in cm or inches.
## Defaults to: 150
#SVG_DPI = 150

## Max AGE sent as a header for the image served by thumbor in seconds
## Defaults to: 86400
#MAX_AGE = 86400

## Indicates the Max AGE header in seconds for temporary images (images with
## failed smart detection)
## Defaults to: 0
#MAX_AGE_TEMP_IMAGE = 0

## Indicates whether thumbor should rotate images that have an Orientation EXIF
## header
## Defaults to: False
#RESPECT_ORIENTATION = False

## Ignore errors during smart detections and return image as a temp image (not
## saved in result storage and with MAX_AGE_TEMP_IMAGE age)
## Defaults to: False
#IGNORE_SMART_ERRORS = False

## Sends If-Modified-Since & Last-Modified headers; requires support from result
## storage
## Defaults to: False
#SEND_IF_MODIFIED_LAST_MODIFIED_HEADERS = False

## Preserves exif information in generated images. Increases image size in
## kbytes, use with caution.
## Defaults to: False
#PRESERVE_EXIF_INFO = False

## Indicates whether thumbor should enable the EXPERIMENTAL support for animated
## gifs.
## Defaults to: True
#ALLOW_ANIMATED_GIFS = True

## Indicates whether thumbor should use gifsicle engine. Please note that smart
## cropping and filters are not supported for gifs using gifsicle (but won't
## give an error).
## Defaults to: False
#USE_GIFSICLE_ENGINE = False

## Indicates whether thumbor should enable blacklist functionality to prevent
## processing certain images.
## Defaults to: False
#USE_BLACKLIST = False

## Size of the thread pool used for image transformations.  The default value is
## 0 (don't use a threadpoool. Increase this if you are seeing your IOLoop
## getting blocked (often indicated by your upstream HTTP requests timing out)
## Defaults to: 0
#ENGINE_THREADPOOL_SIZE = 0

################################################################################


################################ Extensibility #################################

## The metrics backend thumbor should use to measure internal actions. This must
## be the full name of a python module (python must be able to import it)
## Defaults to: 'thumbor.metrics.logger_metrics'
#METRICS = 'thumbor.metrics.logger_metrics'

## The loader thumbor should use to load the original image. This must be the
## full name of a python module (python must be able to import it)
## Defaults to: 'thumbor.loaders.http_loader'
#LOADER = 'thumbor.loaders.http_loader'

## The file storage thumbor should use to store original images. This must be the
## full name of a python module (python must be able to import it)
## Defaults to: 'thumbor.storages.file_storage'
#STORAGE = 'thumbor.storages.file_storage'

## The result storage thumbor should use to store generated images. This must be
## the full name of a python module (python must be able to import it)
## Defaults to: None
#RESULT_STORAGE = None

## The imaging engine thumbor should use to perform image operations. This must
## be the full name of a python module (python must be able to import it)
## Defaults to: 'thumbor.engines.pil'
#ENGINE = 'thumbor.engines.pil'

## The gif engine thumbor should use to perform image operations. This must be
## the full name of a python module (python must be able to import it)
## Defaults to: 'thumbor.engines.gif'
#GIF_ENGINE = 'thumbor.engines.gif'

## The url signer thumbor should use to verify url signatures.This must be the
## full name of a python module (python must be able to import it)
## Defaults to: 'libthumbor.url_signers.base64_hmac_sha1'
#URL_SIGNER = 'libthumbor.url_signers.base64_hmac_sha1'

################################################################################


################################### Security ###################################

## The security key thumbor uses to sign image URLs
## Defaults to: 'MY_SECURE_KEY'
#SECURITY_KEY = 'MY_SECURE_KEY'

## Indicates if the /unsafe URL should be available
## Defaults to: True
#ALLOW_UNSAFE_URL = True

## Indicates if encrypted (old style) URLs should be allowed
## Defaults to: True
#ALLOW_OLD_URLS = True

################################################################################


##################################### HTTP #####################################

## Enables automatically generated etags
## Defaults to: True
#ENABLE_ETAGS = True

################################################################################


################################### Storage ####################################

## Set maximum id length for images when stored
## Defaults to: 32
#MAX_ID_LENGTH = 32

################################################################################


################################# Performance ##################################

## Set garbage collection interval in seconds
## Defaults to: None
#GC_INTERVAL = None

################################################################################


################################### Metrics ####################################

## Host to send statsd instrumentation to
## Defaults to: None
#STATSD_HOST = None

## Port to send statsd instrumentation to
## Defaults to: 8125
#STATSD_PORT = 8125

## Prefix for statsd
## Defaults to: None
#STATSD_PREFIX = None

################################################################################


################################# File Loader ##################################

## The root path where the File Loader will try to find images
## Defaults to: '/root'
#FILE_LOADER_ROOT_PATH = '/root'

################################################################################


################################# HTTP Loader ##################################

## The maximum number of seconds libcurl can take to connect to an image being
## loaded
## Defaults to: 5
#HTTP_LOADER_CONNECT_TIMEOUT = 5

## The maximum number of seconds libcurl can take to download an image
## Defaults to: 20
#HTTP_LOADER_REQUEST_TIMEOUT = 20

## Indicates whether libcurl should follow redirects when downloading an image
## Defaults to: True
#HTTP_LOADER_FOLLOW_REDIRECTS = True

## Indicates the number of redirects libcurl should follow when downloading an
## image
## Defaults to: 5
#HTTP_LOADER_MAX_REDIRECTS = 5

## The maximum number of simultaneous HTTP connections the loader can make before
## queuing
## Defaults to: 10
#HTTP_LOADER_MAX_CLIENTS = 10

## Indicates whether thumbor should forward the user agent of the requesting user
## Defaults to: False
#HTTP_LOADER_FORWARD_USER_AGENT = False

## Indicates whether thumbor should forward the headers of the request
## Defaults to: False
#HTTP_LOADER_FORWARD_ALL_HEADERS = False

## Indicates which headers should be forwarded among all the headers of the
## request
## Defaults to: #    [
#    ]

#HTTP_LOADER_FORWARD_HEADERS_WHITELIST = #    [
#    ]


## Default user agent for thumbor http loader requests
## Defaults to: 'Thumbor/6.6.0'
#HTTP_LOADER_DEFAULT_USER_AGENT = 'Thumbor/6.6.0'

## The proxy host needed to load images through
## Defaults to: None
#HTTP_LOADER_PROXY_HOST = None

## The proxy port for the proxy host
## Defaults to: None
#HTTP_LOADER_PROXY_PORT = None

## The proxy username for the proxy host
## Defaults to: None
#HTTP_LOADER_PROXY_USERNAME = None

## The proxy password for the proxy host
## Defaults to: None
#HTTP_LOADER_PROXY_PASSWORD = None

## The filename of CA certificates in PEM format
## Defaults to: None
#HTTP_LOADER_CA_CERTS = None

## Validate the server’s certificate for HTTPS requests
## Defaults to: None
#HTTP_LOADER_VALIDATE_CERTS = None

## The filename for client SSL key
## Defaults to: None
#HTTP_LOADER_CLIENT_KEY = None

## The filename for client SSL certificate
## Defaults to: None
#HTTP_LOADER_CLIENT_CERT = None

## If the CurlAsyncHTTPClient should be used
## Defaults to: False
#HTTP_LOADER_CURL_ASYNC_HTTP_CLIENT = False

################################################################################


################################### General ####################################

## If HTTP_LOADER_CURL_LOW_SPEED_LIMIT and HTTP_LOADER_CURL_ASYNC_HTTP_CLIENT are
## set, then this is the time in seconds as integer after a download should
## timeout if the speed is below HTTP_LOADER_CURL_LOW_SPEED_LIMIT for that
## long
## Defaults to: 0
#HTTP_LOADER_CURL_LOW_SPEED_TIME = 0

## If HTTP_LOADER_CURL_LOW_SPEED_TIME and HTTP_LOADER_CURL_ASYNC_HTTP_CLIENT are
## set, then this is the limit in bytes per second as integer which should
## timeout if the speed is below that limit for
## HTTP_LOADER_CURL_LOW_SPEED_TIME seconds
## Defaults to: 0
#HTTP_LOADER_CURL_LOW_SPEED_LIMIT = 0

## Custom app class to override ThumborServiceApp. This config value is
## overridden by the -a command-line parameter.
## Defaults to: 'thumbor.app.ThumborServiceApp'
#APP_CLASS = 'thumbor.app.ThumborServiceApp'

################################################################################


################################# File Storage #################################

## Expiration in seconds for the images in the File Storage. Defaults to one
## month
## Defaults to: 2592000
#STORAGE_EXPIRATION_SECONDS = 2592000

## Indicates whether thumbor should store the signing key for each image in the
## file storage. This allows the key to be changed and old images to still be
## properly found
## Defaults to: False
#STORES_CRYPTO_KEY_FOR_EACH_IMAGE = False

## The root path where the File Storage will try to find images
## Defaults to: '/tmp/thumbor/storage'
#FILE_STORAGE_ROOT_PATH = '/tmp/thumbor/storage'

################################################################################


#################################### Upload ####################################

## Max size in Kb for images uploaded to thumbor
## Aliases: MAX_SIZE
## Defaults to: 0
#UPLOAD_MAX_SIZE = 0

## Indicates whether thumbor should enable File uploads
## Aliases: ENABLE_ORIGINAL_PHOTO_UPLOAD
## Defaults to: False
#UPLOAD_ENABLED = False

## The type of storage to store uploaded images with
## Aliases: ORIGINAL_PHOTO_STORAGE
## Defaults to: 'thumbor.storages.file_storage'
#UPLOAD_PHOTO_STORAGE = 'thumbor.storages.file_storage'

## Indicates whether image deletion should be allowed
## Aliases: ALLOW_ORIGINAL_PHOTO_DELETION
## Defaults to: False
#UPLOAD_DELETE_ALLOWED = False

## Indicates whether image overwrite should be allowed
## Aliases: ALLOW_ORIGINAL_PHOTO_PUTTING
## Defaults to: False
#UPLOAD_PUT_ALLOWED = False

## Default filename for image uploaded
## Defaults to: 'image'
#UPLOAD_DEFAULT_FILENAME = 'image'

################################################################################


############################### Memcache Storage ###############################

## List of Memcache storage server hosts
## Defaults to: #    [
#        'localhost:11211',
#    ]

#MEMCACHE_STORAGE_SERVERS = #    [
#        'localhost:11211',
#    ]


################################################################################


################################ Mixed Storage #################################

## Mixed Storage file storage. This must be the full name of a python module
## (python must be able to import it)
## Defaults to: 'thumbor.storages.no_storage'
#MIXED_STORAGE_FILE_STORAGE = 'thumbor.storages.no_storage'

## Mixed Storage signing key storage. This must be the full name of a python
## module (python must be able to import it)
## Defaults to: 'thumbor.storages.no_storage'
#MIXED_STORAGE_CRYPTO_STORAGE = 'thumbor.storages.no_storage'

## Mixed Storage detector information storage. This must be the full name of a
## python module (python must be able to import it)
## Defaults to: 'thumbor.storages.no_storage'
#MIXED_STORAGE_DETECTOR_STORAGE = 'thumbor.storages.no_storage'

################################################################################


##################################### Meta #####################################

## The callback function name that should be used by the META route for JSONP
## access
## Defaults to: None
#META_CALLBACK_NAME = None

################################################################################


################################## Detection ###################################

## List of detectors that thumbor should use to find faces and/or features. All
## of them must be full names of python modules (python must be able to import
## it)
## Defaults to: #    [
#    ]

#DETECTORS = #    [
#    ]


## The cascade file that opencv will use to detect faces.
## Defaults to: 'haarcascade_frontalface_alt.xml'
#FACE_DETECTOR_CASCADE_FILE = 'haarcascade_frontalface_alt.xml'

## The cascade file that opencv will use to detect glasses.
## Defaults to: 'haarcascade_eye_tree_eyeglasses.xml'
#GLASSES_DETECTOR_CASCADE_FILE = 'haarcascade_eye_tree_eyeglasses.xml'

## The cascade file that opencv will use to detect profile faces.
## Defaults to: 'haarcascade_profileface.xml'
#PROFILE_DETECTOR_CASCADE_FILE = 'haarcascade_profileface.xml'

################################################################################


################################## Optimizers ##################################

## List of optimizers that thumbor will use to optimize images
## Defaults to: #    [
#    ]

OPTIMIZERS = ( {{ range $value := (split (default .Env.OPTIMIZERS "") " " ) }}"{{ $value }}",{{ end }} )


## Path for the jpegtran binary
## Defaults to: '/usr/bin/jpegtran'
#JPEGTRAN_PATH = '/usr/bin/jpegtran'

## Path for the progressive scans file to use with jpegtran optimizer. Implies
## progressive jpeg output
## Defaults to: ''
#JPEGTRAN_SCANS_FILE = ''

## Path for the ffmpeg binary used to generate gifv(h.264)
## Defaults to: '/usr/local/bin/ffmpeg'
#FFMPEG_PATH = '/usr/local/bin/ffmpeg'

################################################################################


################################### Filters ####################################

## List of filters that thumbor will allow to be used in generated images. All of
## them must be full names of python modules (python must be able to import
## it)
## Defaults to: #    [
#        'thumbor.filters.brightness',
#        'thumbor.filters.colorize',
#        'thumbor.filters.contrast',
#        'thumbor.filters.rgb',
#        'thumbor.filters.round_corner',
#        'thumbor.filters.quality',
#        'thumbor.filters.noise',
#        'thumbor.filters.watermark',
#        'thumbor.filters.equalize',
#        'thumbor.filters.fill',
#        'thumbor.filters.sharpen',
#        'thumbor.filters.strip_exif',
#        'thumbor.filters.strip_icc',
#        'thumbor.filters.frame',
#        'thumbor.filters.grayscale',
#        'thumbor.filters.rotate',
#        'thumbor.filters.format',
#        'thumbor.filters.max_bytes',
#        'thumbor.filters.convolution',
#        'thumbor.filters.blur',
#        'thumbor.filters.extract_focal',
#        'thumbor.filters.focal',
#        'thumbor.filters.no_upscale',
#        'thumbor.filters.saturation',
#        'thumbor.filters.max_age',
#        'thumbor.filters.curve',
#        'thumbor.filters.background_color',
#        'thumbor.filters.upscale',
#        'thumbor.filters.proportion',
#        'thumbor.filters.stretch',
#    ]

#FILTERS = #    [
#        'thumbor.filters.brightness',
#        'thumbor.filters.colorize',
#        'thumbor.filters.contrast',
#        'thumbor.filters.rgb',
#        'thumbor.filters.round_corner',
#        'thumbor.filters.quality',
#        'thumbor.filters.noise',
#        'thumbor.filters.watermark',
#        'thumbor.filters.equalize',
#        'thumbor.filters.fill',
#        'thumbor.filters.sharpen',
#        'thumbor.filters.strip_exif',
#        'thumbor.filters.strip_icc',
#        'thumbor.filters.frame',
#        'thumbor.filters.grayscale',
#        'thumbor.filters.rotate',
#        'thumbor.filters.format',
#        'thumbor.filters.max_bytes',
#        'thumbor.filters.convolution',
#        'thumbor.filters.blur',
#        'thumbor.filters.extract_focal',
#        'thumbor.filters.focal',
#        'thumbor.filters.no_upscale',
#        'thumbor.filters.saturation',
#        'thumbor.filters.max_age',
#        'thumbor.filters.curve',
#        'thumbor.filters.background_color',
#        'thumbor.filters.upscale',
#        'thumbor.filters.proportion',
#        'thumbor.filters.stretch',
#    ]


################################################################################


################################ Result Storage ################################

## Expiration in seconds of generated images in the result storage
## Defaults to: 0
#RESULT_STORAGE_EXPIRATION_SECONDS = 0

## Path where the Result storage will store generated images
## Defaults to: '/tmp/thumbor/result_storage'
#RESULT_STORAGE_FILE_STORAGE_ROOT_PATH = '/tmp/thumbor/result_storage'

## Indicates whether unsafe requests should also be stored in the Result Storage
## Defaults to: False
#RESULT_STORAGE_STORES_UNSAFE = False

################################################################################


############################ Queued Redis Detector #############################

## Server host for the queued redis detector
## Defaults to: 'localhost'
#REDIS_QUEUE_SERVER_HOST = 'localhost'

## Server port for the queued redis detector
## Defaults to: 6379
#REDIS_QUEUE_SERVER_PORT = 6379

## Server database index for the queued redis detector
## Defaults to: 0
#REDIS_QUEUE_SERVER_DB = 0

## Server password for the queued redis detector
## Defaults to: None
#REDIS_QUEUE_SERVER_PASSWORD = None

################################################################################


############################# Queued SQS Detector ##############################

## AWS key id
## Defaults to: None
#SQS_QUEUE_KEY_ID = None

## AWS key secret
## Defaults to: None
#SQS_QUEUE_KEY_SECRET = None

## AWS SQS region
## Defaults to: 'us-east-1'
#SQS_QUEUE_REGION = 'us-east-1'

################################################################################


#################################### Errors ####################################

## This configuration indicates whether thumbor should use a custom error
## handler.
## Defaults to: False
#USE_CUSTOM_ERROR_HANDLING = False

## Error reporting module. Needs to contain a class called ErrorHandler with a
## handle_error(context, handler, exception) method.
## Defaults to: 'thumbor.error_handlers.sentry'
#ERROR_HANDLER_MODULE = 'thumbor.error_handlers.sentry'

## File of error log as json
## Defaults to: None
#ERROR_FILE_LOGGER = None

## File of error log name is parametrized with context attribute
## Defaults to: False
#ERROR_FILE_NAME_USE_CONTEXT = False

################################################################################


############################### Errors - Sentry ################################

## Sentry thumbor project dsn. i.e.: http://5a63d58ae7b94f1dab3dee740b301d6a:73ee
## a45d3e8649239a973087e8f21f98@localhost:9000/2
## Defaults to: ''
#SENTRY_DSN_URL = ''

################################################################################


#################################### Server ####################################

## The amount of time to wait before shutting down the server, i.e. stop
## accepting requests.
## Defaults to: 0
#MAX_WAIT_SECONDS_BEFORE_SERVER_SHUTDOWN = 0

## The amount of time to waut before shutting down all io, after the server has
## been stopped
## Defaults to: 0
#MAX_WAIT_SECONDS_BEFORE_IO_SHUTDOWN = 0

################################################################################
