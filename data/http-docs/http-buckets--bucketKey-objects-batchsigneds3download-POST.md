# buckets/:bucketKey/objects/batchsigneds3download

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-batchsigneds3download-POST/

---

Objects

POST

# buckets/:bucketKey/objects/batchsigneds3download

Gets one or more short-lived signed URL at which you can download an object directly from S3, bypassing OSS servers.

The signed URL(s) returned by this endpoint will expire after 2 minutes as default (** longer expiration times can be set using the minutesExpiration param up to 60 minutes). This is the time at which S3 receives the request, not the time at which the data transfer completes.

As long as S3 receives the request before 2 minutes expires, the subsequent download stream can take much longer.

If your download request to S3 fails after 2 minutes elapses, you can call this endpoint again to request a new S3 signed URL.

This call will return one or more URLs. Each URL requires object read access for the object.

Note that resumable uploads store each chunk individually. After upload completes, an async process merges all the chunks and creates the definitive OSS file. This async process can take time. If you request an S3 download URL before the async process completes, the response returns a map of S3 URLs, one per chunk where the key is the corresponding range bytes. In case you donât want multiple URLs in the response, you can use [OSS signed URL functionality](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signed-POST) , with the `public-resource-fallback` query parameter set to `true`.

**Note:** While this endpoint does not support range headers, the returned URL(s) can be used for ranged downloads. This way, downloads can be parallelized using multiple ranges for maximum speed.

** DISCLAIMER When generating signed URLs, itâs important to use the smallest possible expiration time, in order to avoid longer access in case of exposure of the URL.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects/batchsigneds3download |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be âBearer `<token>`â, where `<token>` is obtained via [POST token](/en/docs/oauth/v2/reference/http/gettoken-POST). |
| --- | --- |
| Content-Type*   string | Must be `application/json`. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| bucketKey*   string | URL-encoded bucket key |
| --- | --- |

* Required

### Request

## [Query String Parameters](#query-string-parameters)

| public-resource-fallback   boolean | Allows to fallback to [OSS signed URLs](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signed-POST) in case of unmerged resumable uploads. |
| --- | --- |
| useCdn   boolean | Will generate a CloudFront URL for the S3 object. |
| minutesExpiration   integer | The custom expiration time within the 1 to 60 minutes range, if not specified, default is 2 minutes. |

### Request

## [Body Structure](#body-structure)

| requests*   array | An array of objects representing each request to get an S3 URL to download from. |
| --- | --- |
| objectKey*   string | Object key to create a download S3 signed URL for |
| response-content-type   string | Value of the Content-Type header that the client expects to receive. If this attribute is not provided, it defaults to the value corresponding to the object. |
| response-content-disposition   string | Value of the Content Disposition header the client expects to receive. If this attribute is not provided, it defaults to the value corresponding to the object. |
| response-cache-control   string | Value of the Cache-Control header that the client expects to receive. If this attribute is not provided, it defaults to the value corresponding to the object. |
| If-None-Match   string | The value of this attribute is compared to the ETAG of the object. If they match, the response body will show the status of this item as âskippedâ with the reason as âNot modifiedâ. |
| If-Modified-Since   string | If the requested object has not been modified since the time specified in this attribute, the response body will show the status of this item as âskippedâ with the reason as âNot modifiedâ. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK |  |
| --- | --- |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. |
| 403   FORBIDDEN | The Authorization was successfully validated but permission is not granted. Donât try again unless you solve permissions first. |
| 500   INTERNAL SERVER ERROR | Internal failure while processing the request, reason depends on error |

### Response

## [Body Structure (200)](#body-structure-200)

| results   object | Indicates the list of returned results, where each key correspond to the object key. |
| --- | --- |
| status   enum:string | Indicates the status of the object. Possible values are:       - `complete` - raw uploads or merged resumable uploads   - `chunked` - unmerged resumable uploads and `public-resource-fallback = false`   - `fallback` - unmerged resumable uploads and `public-resource-fallback = true`   - `skipped` - whenever the request specifies `If-None-Match` or `If-Modified-Since` parameters and a NOT MODIFIED response is get   - `error` - whenever an error occurs getting the URL due to invalid content-type/content-disposition params or object or bucket not found |
| url   string | The S3 signed URL to download from. This attribute is returned when the value of the `status` attribute is `complete` or `fallback` (in which case the URL is an OSS Signed URL instead of an S3 signed URL). |
| urls   object | A map of S3 signed URLs where each key correspond to a specific byte range chunk. This attribute is returned when the value of the `status` attribute is `chunked`. |
| params   object | The values for the updatable params that were used in the creation of the returned S3 signed URL (`Content-Type`, `Content-Disposition` & `Cache-Control`). |
| size   integer | The object size in bytes. |
| sha1   string | The calculated sha1 of the object if available. |
| reason   string | The reason for not getting the requested signed URL, this attribute returned if the value of the `status` attribute is `skipped` or `error` |

## [Example 1](#example-1)

Demonstrates the obtaining of a mix of successful and unsuccessful signed URLs, without falling back to OSS signed URLs (200).

### Request

```
curl
  -X POST
  -H "Authorization=Bearer eYeL5gYxAT2j3u9TEerxoJoToNbi"
  -H "Content-Type=application/json;charset=UTF-8";
  --data '{
    "requests": [{
      "objectKey": "someObject.dat",
      "If-Modified-Since": "Wed, 15 Jan 2021 00:00:00 GMT"
    },{
      "objectKey": "someOtherObject.pdf",
      "If-None-Match": "5ca0855e5758a92dd9ffdaba5fc974c1ae6a0267"
    },{
      "objectKey": "some-invalid-content-object.html",
      "response-content-type": "text/html",
      "response-content-disposition": "inline"
    },{
      "objectKey": "some-valid-object.text",
      "response-content-type": "text"
    },{
      "objectKey": "unmerged-object.json"
    }]
  }'
  https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/batchsigneds3download

```

Show More

### Response

```
{
    "results": {
        "someObject.dat": {
            "status": "skipped",
            "reason": "Not modified"
        },
        "someOtherObject.pdf": {
            "status": "skipped",
            "reason": "Not modified"
        },
        "some-invalid-content-object.html": {
            "status": "error",
            "reason": "Inline executable content not allowed",
            "params": {
                "content-type": "text/html",
                "content-disposition": "inline"
            }
        },
        "some-valid-object.text": {
            "status": "complete",
            "url": "https://oss-bucket.s3.amazonaws.com/07ce8529-a8e6-4dac-98c3-95e2d10f19cd/bucket/apptestbucket/object/some-valid-object.text?response-content-disposition=attachment%3B%20filename%3D%22some-valid-object.text%22&response-content-type=text&X-Amz-Security-Token=AWS_TOKEN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210120T152914Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=6c1abf52e7849asignature",
            "params": {
                "content-type": "text",
                "content-disposition": "attachment; filename=\"some-valid-object.text\""
            },
            "size": 1024334,
            "sha1": "2ae00660a78c643453fac826f288c774c789de64"
        },
        "unmerged-object.json": {
            "status": "chunked",
            "urls": {
                "0-10747471": "https://oss-bucket.s3.amazonaws.com/ead4b508f5a502b9251d16b640128ad83af7e4ba/bucket/apptestbucket/chunk-uuid/uuid-fcdf6275-8789-472f-b811-5472c9262ffc?response-content-disposition=attachment%3B%20filename%3D%22unmerged-object.json%22&response-content-type=application%2Fjson&X-Amz-Security-Token=AWS_TOKEN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210120T152914Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=6c1abf52e7849asignature",
                "10747472-19715186": "https://oss-bucket.s3.amazonaws.com/ead4b508f5a502b9251d16b640128ad83af7e4ba/bucket/apptestbucket/chunk-uuid/uuid-cc685997-7afa-4dd3-ada3-71390a973bc5?response-content-disposition=attachment%3B%20filename%3D%22unmerged-object.json%22&response-content-type=application%2Fjson&X-Amz-Security-Token=AWS_TOKEN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210120T152914Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=6c1abf52e7849asignature"
            },
            "params": {
                "content-type": "application/json",
                "content-disposition": "attachment; filename=\"unmerged-object.json\""
            },
            "size": 19715187
        }
    }
}

```

Show More

## [Example 2](#example-2)

Demonstrates the obtaining of a batch of successful and unsuccessful signed URLs, falling back to OSS signed URLs (200).

### Request

```
curl
  -X POST
  -H "Authorization=Bearer eYeL5gYxAT2j3u9TEerxoJoToNbi"
  -H "Content-Type=application/json;charset=UTF-8";
  --data '{
    "requests": [{
      "objectKey": "someObject.dat",
      "If-Modified-Since": "Wed, 15 Jan 2021 00:00:00 GMT"
    },{
      "objectKey": "someOtherObject.pdf",
      "If-None-Match": "5ca0855e5758a92dd9ffdaba5fc974c1ae6a0267"
    },{
      "objectKey": "some-invalid-content-object.html",
      "response-content-type": "text/html",
      "response-content-disposition": "inline"
    },{
      "objectKey": "some-valid-object.text",
      "response-content-type": "text"
    },{
      "objectKey": "unmerged-object.json"
    }]
  }'
  https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/batchsigneds3download?public-resource-fallback=true

```

Show More

### Response

```
{
    "results": {
        "someObject.dat": {
            "status": "skipped",
            "reason": "Not modified"
        },
        "someOtherObject.pdf": {
            "status": "skipped",
            "reason": "Not modified"
        },
        "some-invalid-content-object.html": {
            "status": "error",
            "reason": "Inline executable content not allowed",
            "params": {
                "content-type": "text/html",
                "content-disposition": "inline"
            }
        },
        "some-valid-object.text": {
            "status": "complete",
            "url": "https://oss-bucket.s3.amazonaws.com/07ce8529-a8e6-4dac-98c3-95e2d10f19cd/bucket/apptestbucket/object/some-valid-object.text?response-content-disposition=attachment%3B%20filename%3D%22some-valid-object.text%22&response-content-type=text&X-Amz-Security-Token=AWS_TOKEN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210120T152914Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=6c1abf52e7849asignature",
            "params": {
                "content-type": "text",
                "content-disposition": "attachment; filename=\"some-valid-object.text\""
            },
            "size": 1024334,
            "sha1": "2ae00660a78c643453fac826f288c774c789de64"
        },
        "unmerged-object.json": {
            "status": "fallback",
            "url": "http://developer.api.autodesk.com/oss/v2/signedresources/09e24d80-f7ef-4535-8ce7-f08f5c6916f9?region=US",
            "params": {
                "content-type": "application/json",
                "content-disposition": "attachment; filename=\"unmerged-object.json\""
            },
            "size": 19715187
        }
    }
}

```

Show More

## [Example 3](#example-3)

Demonstrates the obtaining of a mix of successful and unsuccessful signed URLs using the minutesExpiration parameter (200).

### Request

```
curl
  -X POST
  -H "Authorization=Bearer eYeL5gYxAT2j3u9TEerxoJoToNbi"
  -H "Content-Type=application/json;charset=UTF-8";
  --data '{
    "requests": [{
      "objectKey": "someObject.dat",
      "If-Modified-Since": "Wed, 15 Jan 2021 00:00:00 GMT"
    },{
      "objectKey": "someOtherObject.pdf",
      "If-None-Match": "5ca0855e5758a92dd9ffdaba5fc974c1ae6a0267"
    },{
      "objectKey": "some-invalid-content-object.html",
      "response-content-type": "text/html",
      "response-content-disposition": "inline"
    },{
      "objectKey": "some-valid-object.text",
      "response-content-type": "text"
    },{
      "objectKey": "unmerged-object.json"
    }]
  }'
  https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/batchsigneds3download?minutesExpiration=60

```

Show More

### Response

```
{
    "results": {
        "someObject.dat": {
            "status": "skipped",
            "reason": "Not modified"
        },
        "someOtherObject.pdf": {
            "status": "skipped",
            "reason": "Not modified"
        },
        "some-invalid-content-object.html": {
            "status": "error",
            "reason": "Inline executable content not allowed",
            "params": {
                "content-type": "text/html",
                "content-disposition": "inline"
            }
        },
        "some-valid-object.text": {
            "status": "complete",
            "url": "https://oss-bucket.s3.amazonaws.com/07ce8529-a8e6-4dac-98c3-95e2d10f19cd/bucket/apptestbucket/object/some-valid-object.text?response-content-disposition=attachment%3B%20filename%3D%22some-valid-object.text%22&response-content-type=text&X-Amz-Security-Token=AWS_TOKEN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210120T152914Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=6c1abf52e7849asignature",
            "params": {
                "content-type": "text",
                "content-disposition": "attachment; filename=\"some-valid-object.text\""
            },
            "size": 1024334,
            "sha1": "2ae00660a78c643453fac826f288c774c789de64"
        },
        "unmerged-object.json": {
            "status": "chunked",
            "urls": {
                "0-10747471": "https://oss-bucket.s3.amazonaws.com/ead4b508f5a502b9251d16b640128ad83af7e4ba/bucket/apptestbucket/chunk-uuid/uuid-fcdf6275-8789-472f-b811-5472c9262ffc?response-content-disposition=attachment%3B%20filename%3D%22unmerged-object.json%22&response-content-type=application%2Fjson&X-Amz-Security-Token=AWS_TOKEN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210120T152914Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=6c1abf52e7849asignature",
                "10747472-19715186": "https://oss-bucket.s3.amazonaws.com/ead4b508f5a502b9251d16b640128ad83af7e4ba/bucket/apptestbucket/chunk-uuid/uuid-cc685997-7afa-4dd3-ada3-71390a973bc5?response-content-disposition=attachment%3B%20filename%3D%22unmerged-object.json%22&response-content-type=application%2Fjson&X-Amz-Security-Token=AWS_TOKEN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210120T152914Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=6c1abf52e7849asignature"
            },
            "params": {
                "content-type": "application/json",
                "content-disposition": "attachment; filename=\"unmerged-object.json\""
            },
            "size": 19715187
        }
    }
}

```

Show More
