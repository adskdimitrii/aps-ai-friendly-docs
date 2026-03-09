# buckets/:bucketKey/objects/:objectKey/signeds3download

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3download-GET/

---

Objects

GET

# buckets/:bucketKey/objects/:objectKey/signeds3download

Gets a short-lived signed URL at which you can download an object directly from S3, bypassing OSS servers.

The signed URL returned by this endpoint will expire after 2 minutes as default (** longer expiration times can be set using the minutesExpiration param up to 60 minutes). This is the time at which S3 receives the request, not the time at which the data transfer completes.

As long as S3 receives the request before 2 minutes expires, the subsequent download stream can take much longer.

If your download request to S3 fails after 2 minutes elapses, you can call this endpoint again to request a new S3 signed URL.

A successful call to this endpoint requires object read access.

Note that resumable uploads store each chunk individually. After upload completes, an async process merges all the chunks and creates the definitive OSS file. This async process can take time. If you request an S3 download URL before the async process completes, the response returns a map of S3 URLs, one per chunk where the key is the corresponding range bytes. In case you donât want multiple URLs in the response, you can use [OSS signed URL functionality](http-buckets--bucketKey-objects--objectKey-signed-POST.md) , with the `public-resource-fallback` query parameter set to `true`.

**Note:** While this endpoint does not support range headers, the returned URL(s) can be used for ranged downloads. This way, downloads can be parallelized using multiple ranges for maximum speed.

** DISCLAIMER When generating signed URLs, itâs important to use the smallest possible expiration time, in order to avoid longer access in case of exposure of the URL.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects/:objectKey/signeds3download |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be âBearer `<token>`â, where `<token>` is obtained via [POST token](../../oauth/http-docs/http-gettoken-POST.md). |
| --- | --- |
| If-None-Match   string | If the value of this header matches the ETag of the object, an entity will not be returned from the server; instead a `304` (not modified) response will be returned without any message-body. |
| If-Modified-Since   HTTP date | If the requested object has not been modified since the time specified in this field, an entity will not be returned from the server; instead, a `304` (not modified) response will be returned without any message-body. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| bucketKey*   string | URL-encoded bucket key |
| --- | --- |
| objectKey*   string | URL-encoded object key to create signed URL for |

* Required

### Request

## [Query String Parameters](#query-string-parameters)

| response-content-type   string | Value of the Content-Type header that the client expects to receive. If this attribute is not provided, it defaults to the value corresponding to the object. |
| --- | --- |
| response-content-disposition   string | Value of the Content Disposition header the client expects to receive. If this attribute is not provided, it defaults to the value corresponding to the object. |
| response-cache-control   string | Value of the Cache-Control header that the client expects to receive. If this attribute is not provided, it defaults to the value corresponding to the object. |
| public-resource-fallback   boolean | Allows fallback to [OSS signed URLs](http-buckets--bucketKey-objects--objectKey-signed-POST.md) in case of unmerged resumable uploads. |
| useCdn   boolean | Will generate a CloudFront URL for the S3 object. |
| minutesExpiration   integer | The custom expiration time within the 1 to 60 minutes range, if not specified, default is 2 minutes. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK |  |
| --- | --- |
| 304   NOT MODIFIED | If the `If-None-Match` header was specified in the request, and it matches the objectâs ETAG, no content will be sent. Or, if the `If-Modified-Since` header was specified and the object has not been modified since the time specified, no content will be sent. |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. |
| 403   FORBIDDEN | The Authorization was successfully validated but permission is not granted. Donât try again unless you solve permissions first. |
| 404   NOT FOUND | Object or bucket does not exist |
| 500   INTERNAL SERVER ERROR | Internal failure while processing the request, reason depends on error |

### Response

## [Body Structure (200)](#body-structure-200)

| status   enum:string | Indicates the status of the object. Possible values are:   - `complete` - raw uploads or merged resumable uploads   - `chunked` - unmerged resumable uploads and `public-resource-fallback` = `false`   - `fallback` - unmerged resumable uploads and `public-resource-fallback` = `true` |
| --- | --- |
| url   string | The S3 signed URL to download from. This attribute is returned when the value of the `status` attribute is `complete` or `fallback` (in which case the URL will be an OSS Signed URL instead of an S3 signed URL). |
| urls   object | A map of S3 signed URLs where each key correspond to a specific byte range chunk. This attribute is returned when the value of the `status` attribute is `chunked`. |
| params   object | The values for the updatable params that were used in the creation of the returned S3 signed URL (`Content-Type`, `Content-Disposition` & `Cache-Control`). |
| size   integer | The object size in bytes. |
| sha1   string | The calculated sha1 of the object if available. |

## [Example 1](#example-1)

Demonstrates the obtaining of an S3 signed URL for an object (raw uploads or merged resumable uploads) (200).

### Request

```
curl
  -X GET
  -H "Authorization=Bearer eYeL5gYxAT2j3u9TEerxoJoToNbi"
  https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/objectKeyFoo/signeds3download

```

### Response

```
{
  "status": "complete"
  "url": "https://oss-bucket-name.s3.amazonaws.com/4F/2D/df/a9f898eda7edee1ab9827cfeb57f2ec647/apptestbucket?response-content-disposition=attachment%3B%20filename%3D%22objectKeyFoo%22&response-content-type=application%2Foctet-stream&X-Amz-Security-Token=AWS_TOKEN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210120T152914Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=6c1abf52e7849asignature"
  "params" : {
    "content-type": "application/octet-stream",
    "content-disposition": "attachment; filename=\"objectKeyFoo\""
  },
  "size" : 221983,
  "sha1" : 4F2Ddfa9f898eda7edee1ab9827cfeb57f2ec647
}

```

Show More

## [Example 2](#example-2)

Demonstrates the obtaining an OSS signed URL for an unmerged object because `public-resource-fallback` equals to `true` (200).

### Request

```
curl
  -X GET
  -H "Authorization=Bearer eYeL5gYxAT2j3u9TEerxoJoToNbi"
  https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/unmerged.json/signeds3download?public-resource-fallback=true

```

### Response

```
{
  "status": "fallback"
  "url": "http://developer.api.autodesk.com/oss/v2/signedresources/6969f2ed-2931-498f-bad8-b9d300ad1c7e?region=US"
  "params" : {
    "content-type": "application/json",
    "content-disposition": "attachment; filename=\"unmerged.json\""
  },
  "size" : 19715187
}

```

Show More

## [Example 3](#example-3)

Demonstrates the obtaining of multiple S3 signed URLs for an unmerged object, one per chunk (200).

### Request

```
curl
  -X GET
  -H "Authorization=Bearer eYeL5gYxAT2j3u9TEerxoJoToNbi"
  https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/unmerged.json/signeds3download

```

### Response

```
{
  "status": "chunked"
  "urls": {
    "0-10747471": "https://oss-bucket.s3.amazonaws.com/ead4b508f5a502b9251d16b640128ad83af7e4ba/bucket/apptestbucket/chunk-uuid/uuid-fcdf6275-8789-472f-b811-5472c9262ffc?response-content-disposition=attachment%3B%20filename%3D%22unmerged.json%22&response-content-type=application%2Fjson&X-Amz-Security-Token=AWS_TOKEN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210120T152914Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=6c1abf52e7849asignature",
    "10747472-19715186": "https://oss-bucket.s3.amazonaws.com/ead4b508f5a502b9251d16b640128ad83af7e4ba/bucket/apptestbucket/chunk-uuid/uuid-cc685997-7afa-4dd3-ada3-71390a973bc5?response-content-disposition=attachment%3B%20filename%3D%22unmerged.json%22&response-content-type=application%2Fjson&X-Amz-Security-Token=AWS_TOKEN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210120T152914Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=6c1abf52e7849asignature"
  },
  "params" : {
    "content-type": "application/json",
    "content-disposition": "attachment; filename=\"unmerged.json\""
  },
  "size" : 19715187
}

```

Show More

## [Example 4](#example-4)

Demonstrates the obtaining of an S3 signed URL for an object using the minutesExpiration parameter (200).

### Request

```
curl
  -X GET
  -H "Authorization=Bearer eYeL5gYxAT2j3u9TEerxoJoToNbi"
  https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/objectKeyFoo/signeds3download?minutesExpiration=30

```

### Response

```
{
  "status": "complete"
  "url": "https://oss-bucket-name.s3.amazonaws.com/4F/2D/df/a9f898eda7edee1ab9827cfeb57f2ec647/apptestbucket?response-content-disposition=attachment%3B%20filename%3D%22objectKeyFoo%22&response-content-type=application%2Foctet-stream&X-Amz-Security-Token=AWS_TOKEN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210120T152914Z&X-Amz-SignedHeaders=host&X-Amz-Expires=1800&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=6c1abf52e7849asignature"
  "params" : {
    "content-type": "application/octet-stream",
    "content-disposition": "attachment; filename=\"objectKeyFoo\""
  },
  "size" : 221983,
  "sha1" : 4F2Ddfa9f898eda7edee1ab9827cfeb57f2ec647
}

```

Show More
