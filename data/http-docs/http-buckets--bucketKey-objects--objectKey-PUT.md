# buckets/:bucketKey/objects/:objectKey

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-PUT/

---

Objects

PUT

# buckets/:bucketKey/objects/:objectKey

Deprecated

Upload an object.

**We will be deprecating this endpoint.**

We recommend using the [GET buckets/:bucketKey/objects/:objectKey/signeds3upload](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-GET) endpoint. See the [App Managed Bucket Tutorial](en/docs/data/v2/tutorials/app-managed-bucket) for step by step workflow.

Upload an object.
If the specified object key already exists in the bucket, the uploaded content will overwrite the existing content for the bucket name/object key combination.

Note that for objects larger than 100 MB we recommend using the [PUT buckets/:bucketKey/objects/:objectKey/resumable](en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-resumable-PUT) endpoint.

## [Resource Information](#resource-information)

| Method and URI | PUT https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects/:objectKey |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:write` or `data:create` (`data:write` allows overwriting existing objects) |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [POST token](/en/docs/oauth/v2/reference/http/gettoken-POST) |
| --- | --- |
| Content-Disposition   string | The suggested default filename when downloading this object to a file after it has been uploaded. |
| Content-Length*   integer | Size in bytes of the request body.       Most clients add this header automatically, so you should only set it explicitly if necessary. |
| Content-Type   string | It is recommended to add this header if the content-type is known. Accepts any content-type except multipart/form-data. |
| If-Match   string | When overwriting an object, use the latest SHA-1 hash to verify that you are overwriting the latest data.   A SHA-1 hash is returned every time you upload or overwrite an object. If the SHA-1 hash in the header does not match the current SHA-1 hash stored for this object in OSS, the request fails (status code `412`). |
| x-ads-content-sha1   string | A SHA-1 checksum of the object represented as a hexadecimal string.   If the SHA-1 hash in the header does not match the SHA-1 hash computed by the server for the uploaded object, the request fails (status code `400`). |

* Required

### Request

## [URI Parameters](#uri-parameters)

| bucketKey*   string | URL-encoded bucket to upload object into |
| --- | --- |
| objectKey*   string | URL-encoded object key being uploaded |

* Required

### Request

## [Body Structure](#body-structure)

Contents of the file to upload

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful operation. |
| --- | --- |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. |
| 403   FORBIDDEN | The Authorization was successfully validated but permission is not granted. Donât try again unless you solve permissions first. |
| 404   NOT FOUND | The specified bucket does not exist. |
| 412   PRECONDITION FAILED | Conditional update failed because the hash value supplied in the header does not match the SHA-1 hash value of the current object in OSS. |
| 500   INTERNAL SERVER ERROR | Internal failure while processing the request, reason depends on error. |

### Response

## [Headers](#id4)

| x-ads-content-sha1   string | SHA-1 checksum of the uploaded chunk represented as a hexadecimal string computed by the server. It will be sent only when the checksum validation fails, to allow you to compare the computed hash by the server with the provided one. |
| --- | --- |

### Response

## [Body Structure (200)](#body-structure-200)

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "bucketKey": {
      "type": "string"
    },
      "objectId": {
        "type": "string"
    },
      "objectKey": {
        "type": "string"
    },
      "sha1": {
        "type": "string"
    },
      "size": {
        "type": "integer"
    },
      "contentType": {
        "type": "string"
    },
      "location": {
        "type": "string"
    }
  }
}

```

Show More

| bucketKey   string | Bucket key |
| --- | --- |
| objectId   string | Object URN |
| objectKey   string | Object Key |
| sha1   string | SHA-1 hash of the object, to be used as the value of the `If-Match` header in subsequent calls to overwrite the object. |
| size   integer | Object size |
| contentType   string | Object content-type |
| location   string | URL to download the object |

## [Example 1](#example-1)

Successful Upload (200)

### Request

```
curl -v 'https://developer.api.autodesk.com/oss/v2/buckets/mybucket/objects/example.txt'
  -X 'PUT'
  -H 'Authorization: Bearer AlmsGlZlqz1JkkzEruUdINMKA6IF'
  -H 'Content-Type: text/plain; charset=UTF-8'
  -T 'example.txt'

```

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Wed, 25 May 2016 15:55:22 GMT
Server Apigee Router is not blacklisted
Server: Apigee Router
Content-Length: 364
Connection: keep-alive
{
  "bucketKey" : "mybucket",
  "objectId" : "urn:adsk.objects:os.object:mybucket/example.txt",
  "objectKey" : "example.txt",
  "sha1" : "cc2071e3c3a0e95ec68c599ccac6f8caa012677e",
  "size" : 525,
  "contentType" : "text/plain; charset=UTF-8",
  "location" : "https://developer.api.autodesk.com/oss/v2/buckets/mybucket/objects/example.txt"
}

```

Show More

## [Example 2](#example-2)

Precondition Failed (412)

If the value sent for the `If-Match` header is not equal to the `sha1` value stored in OSS for this object, a Precondition Failed message will be returned.
Based on example 1 above, the header value should be: `cc2071e3c3a0e95ec68c599ccac6f8caa012677e`

### Request

```
curl -v 'https://developer.api.autodesk.com/oss/v2/buckets/mybucket/objects/example.txt'
  -X 'PUT'
  -H 'If-Match: 86b62d847d5292d2c8a2e66863a593642d7e3d89X'
  -H 'Authorization: Bearer AlmsGlZlqz1JkkzEruUdINMKA6IF'
  -H 'Content-Type: text/plain; charset=UTF-8'
  -T 'example.txt'

```

### Response

```
HTTP/1.1 412 Precondition Failed
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Wed, 25 May 2016 15:58:44 GMT
Server Apigee Router is not blacklisted
Server: Apigee Router
Content-Length: 29
Connection: keep-alive

{
   "reason":"ETag Not Matched"
}

```

Show More

## [Example 3](#example-3)

Mismatched checksums(400)

If the value sent for the `x-ads-content-sha1` header is not equal to the `sha1` value computed in OSS for this object after the upload, a Bad Request message will be returned.
Based on example above, the header value should be: `58ad9e4625a2abddeb688af44c29a26b9d709709`

### Request

```
curl -v 'https://developer.api.autodesk.com/oss/v2/buckets/mybucket/objects/example.txt'
  -X 'PUT'
  -H 'If-Match: 86b62d847d5292d2c8a2e66863a593642d7e3d89X'
  -H 'Authorization: Bearer AlmsGlZlqz1JkkzEruUdINMKA6IF'
  -H "x-ads-content-sha1: cc2071e3c3a0e95ec68c599ccac6f8caa012677e"
  -H 'Content-Type: text/plain; charset=UTF-8'
  -T 'example.txt'

```

### Response

```
HTTP/1.1 400 Precondition Failed
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
x-ads-content-sha1: 58ad9e4625a2abddeb688af44c29a26b9d709709
Content-Type: application/json; charset=utf-8
Date: Wed, 25 May 2016 15:58:44 GMT
Server Apigee Router is not blacklisted
Server: Apigee Router
Content-Length: 29
Connection: keep-alive

{
   "reason":"Mismatched checksums"
}

```

Show More
