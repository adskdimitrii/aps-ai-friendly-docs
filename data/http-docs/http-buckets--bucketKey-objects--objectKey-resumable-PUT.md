# buckets/:bucketKey/objects/:objectKey/resumable

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-resumable-PUT/

---

Objects

PUT

# buckets/:bucketKey/objects/:objectKey/resumable

Deprecated

This endpoint allows resumable uploads for large files in chunks.

**We will be deprecating this endpoint.**

We recommend using the [GET buckets/:bucketKey/objects/:objectKey/signeds3upload](http-buckets--bucketKey-objects--objectKey-signeds3upload-GET.md) endpoint. See the [App Managed Bucket Tutorial](../how-to-docs/app-managed-bucket.md) for step by step workflow.

Note that for uploading objects smaller than 100 MB we recommend using the [PUT buckets/:bucketKey/objects/:objectKey](http-buckets--bucketKey-objects--objectKey-PUT.md) endpoint.

To check the upload status, use the [GET buckets/:bucketKey/objects/:objectKey/status/:sessionId](http-buckets--bucketKey-objects--objectKey-status--sessionId-GET.md) endpoint.

If you want to validate the integrity of the chunk’s content, then you can send the `x-ads-chunk-sha1` header.

Note this header must be the SHA-1 checksum of the chunk represented as a hexadecimal string, it is not a mechanism for validating the integrity of the entire file.

## [Resource Information](#resource-information)

| Method and URI | PUT https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects/:objectKey/resumable |
| --- | --- |
| Authentication Context | app-only |
| Required OAuth Scopes | `data:write` or `data:create` (`data:write` allows overwriting existing objects) |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be “Bearer `<token>`”, where `<token>` is obtained via [POST token](../../oauth/http-docs/http-gettoken-POST.md). |
| --- | --- |
| Content-Disposition   string | OSS will record the value of the header and on download, would send the header contents down. |
| Content-Length*   integer | Size in bytes of the data chunk being uploaded.   We recommend uploading 5 MB chunks.   Note that chunks must be larger than 2 MB. |
| Content-Range*   string | Byte range of the chunk being uploaded |
| Content-Type   string | Can be omitted, but we encourage adding it   Accepts any content-type except multipart/form-data. For a missing content-type some applications will add `application/stream` by default. |
| Session-Id*   string | Unique identifier of a session of a file being uploaded |
| x-ads-chunk-sha1   string | A SHA-1 checksum of the chunk represented as a hexadecimal string.   If the SHA-1 hash in the header does not match the SHA-1 hash computed by the server for the uploaded chunk, the request fails (status code `400`).   You can try to upload it again. |

* Required

### Request

## [Body Structure](#body-structure)

<Contents of the file to upload>

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success, with the following caveat: no SHA1 information will be returned in object details until the object has been recombined. |
| --- | --- |
| 202   ACCEPTED | Server acknowledges receiving data chunk. |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. |
| 403   FORBIDDEN | The Authorization was successfully validated but permission is not granted. Don’t try again unless you solve permissions first. |
| 404   NOT FOUND | The specified bucket does not exist. |
| 409   CONFLICT | Unable to persist data. |
| 416   REQUEST RANGE NOT SATISFIABLE | Missing Content-Range header. |
| 500   INTERNAL SERVER ERROR | Internal failure while processing the request, reason depends on error. |

### Response

## [Headers](#id3)

| x-ads-chunk-sha1   string | SHA-1 checksum of the uploaded chunk represented as a hexadecimal string computed by the server.   It will be present in all cases, not only when you provide the `x-ads-chunk-sha1` in the request. |
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

| bucketKey   string | Bucket Key |
| --- | --- |
| objectId   string | Object URN |
| objectKey   string | Object Key |
| size   integer | Object size |
| contentType   string | Object content-type |
| location   string | URL to download the object |

## [Example 1](#example-1)

Range Accepted (202)

This is an example where an object could be uploaded in seven steps. It is not necessary to upload chunks in sequential order.

- Upload 1 byte: 0-0/100, Response 202
- Upload 15 bytes: 46-60/100, Response 202
- …
- Final Update: Response 200

Initial byte is 0, final is 99, total is 100.
“Range=bytes=0-0,1-15,16-30,31-45,46-60,61-90,91-99”;
Each non-final step will return a 202 Accepted.

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets/bucketexamplekey/objects/objectKeyFoo/resumable"
  -X PUT
  -H "Authorization:Bearer p0vNqwggSc4EOJdhR4KkTVyJFIzQ"
  -H "Content-Type:text/plain; charset=UTF-8"
  -H "Content-Range:bytes 1-15/100"
  -H "Session-Id:-811577637"
  --data "five-five-five-"

```

### Response

```
HTTP/1.1 202 Accepted
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
x-ads-chunk-sha1: 58ad9e4625a2abddeb688af44c29a26b9d709709
Date: Tue, 24 May 2016 20:57:40 GMT
Server: Apigee Router
Content-Length: 0
Connection: keep-alive

```

Show More

The final range will return a 200 OK.

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Date: Tue, 24 May 2016 20:57:40 GMT
Server: Apigee Router
Content-Length: 0
Connection: keep-alive
{
 "bucketKey" : "bucketexamplekey",
 "objectId" : "urn:adsk.objects:os.object:bucketexamplekey/objectKeyFoo",
 "objectKey" : "objectKeyFoo",
 "size" : 100,
 "contentType" : "text/plain; charset=UTF-8",
 "location" : "https://developer.api.autodesk.com/oss/v2/buckets/bucketexamplekey/objects/objectKeyFoo"
}

```

Show More

## [Example 2](#example-2)

Invalid Content-Range Header (416)

Body length should be compatible with Content-Range.
“Content-Range=bytes 15-30/100” requires 16 bytes in body, [15,16,17,..,30] but found 15.
“Content-Range=bytes 16-30/100” would be valid for this case.

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets/bucketexamplekey/objects/objectKeyFoo/resumable"
  -X PUT
  -H "Authorization:Bearer bPuChwoniWJFx3hz7ZwutRveDqHJ"
  -H "Content-Type:text/plain; charset=UTF-8"
  -H "Content-Range:bytes 15-30/100"
  -H "Session-Id:-811577637"
  --data "five-five-five-"

```

### Response

```
HTTP/1.1 416 Requested Range Not Satisfiable
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Date: Tue, 24 May 2016 20:57:40 GMT
Server: Apigee Router
Content-Length: 0
Connection: keep-alive
{
   "reason" : "Chunk-Length mismatch (found: 15, required:16)"
}

```

Show More

## [Example 3](#example-3)

Missing Content-Range Header (416)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets/bucketexamplekey/objects/objectKeyFoo/resumable"
  -X PUT
  -H "Authorization:Bearer N0AJ9OavqPXHpbXXnOW5B6SlNZ8R"
  -H "Content-Type:text/plain; charset=UTF-8"
  -H "Session-Id:-811577637"
  --data "five-five-five-"

```

### Response

```
HTTP/1.1 416 Requested Range Not Satisfiable
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Date: Tue, 24 May 2016 20:57:40 GMT
Server: Apigee Router
Content-Length: 0
Connection: keep-alive

Missing Content-Range header

```

Show More

## [Example 4](#example-4)

Missing Session-ID Header (400)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets/bucketexamplekey/objects/objectKeyFoo/resumable"
  -X PUT
  -H "Authorization:Bearer N0AJ9OavqPXHpbXXnOW5B6SlNZ8R"
  -H "Content-Type:text/plain; charset=UTF-8"
  --data "five-five-five-"

```

### Response

```
HTTP/1.1 400 Bad Request
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Date: Tue, 24 May 2016 20:57:40 GMT
Server: Apigee Router
Content-Length: 0
Connection: keep-alive

Session-ID header is missing

```

Show More

## [Example 5](#example-5)

Mismatched checksums(400)

If the value sent for the `x-ads-chunk-sha1` header is not equal to the `sha1` value computed in OSS for this object after the upload, a Bad Request message will be returned.
Based on example above, the header value should be: `58ad9e4625a2abddeb688af44c29a26b9d709709`

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets/bucketexamplekey/objects/objectKeyFoo/resumable"
  -X PUT
  -H "Authorization:Bearer N0AJ9OavqPXHpbXXnOW5B6SlNZ8R"
  -H "Content-Type:text/plain; charset=UTF-8"
  -H "x-ads-chunk-sha1: cc2071e3c3a0e95ec68c599ccac6f8caa012677e"
  --data "five-five-five-"

```

### Response

```
HTTP/1.1 400 Bad Request
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
x-ads-chunk-sha1: 58ad9e4625a2abddeb688af44c29a26b9d709709
Date: Tue, 24 May 2016 20:57:40 GMT
Server: Apigee Router
Content-Length: 0
Connection: keep-alive
{
   "reason" : "Mismatched checksums"
}

```

Show More
