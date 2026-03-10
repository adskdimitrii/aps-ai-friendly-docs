# signedresources/:id/resumable

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/signedresources-:id-resumable-PUT/

---

Objects

PUT

# signedresources/:id/resumable

Resumable upload for signed URLs.

Conditions to call this operation:

- Session is available
- Expiration period is valid
- Signed URL should be created with `write` or `readwrite` access.
- If you set the URL to expire after it is used the first time, it will expire when the session is complete.

## [Resource Information](#resource-information)

| Method and URI | PUT https://developer.api.autodesk.com/oss/v2/signedresources/:id/resumable |
| --- | --- |
| Authentication Context | *none* |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Content-Disposition   string | The Content-Disposition header specified here during upload will be echoed back during download. |
| --- | --- |
| Content-Range*   string | Byte range of a segment being uploaded. |
| Content-Type   string | Can be omitted, but we encourage adding it.   Accepts any content-type except `multipart/form-data`. For a missing content-type some applications will add `application/stream` by default. |
| Session-Id*   string | Unique identifier of a session of a file being uploaded. |
| x-ads-region   enum | Route the request to the specified region.   Acceptable values:       - `US` - Data center for the US region.   - `EMEA` - Data center for the Europe, Middle East, and Africa regions.   - `AUS` - (Beta) Data center for the Australia region.   - `CAN` - Data centre for the Canada region.   - `DEU` - Data centre for the Germany region.   - `IND` - Data centre for the India region.   - `JPN` - Data centre for the Japan region.   - `GBR` - Data centre for the United Kingdom region.       **Note**:       - Beta features are subject to change. Please avoid using them in production environments. |

* Required

### Request

## [Body Structure](#body-structure)

<Contents of the file to upload>

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Response immediately after the upload stream is completed   No Synchronous waiting for the merge No SHA information will be returned |
| --- | --- |
| 202   ACCEPTED | Server acknowledges reception of segment |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. |
| 403   FORBIDDEN | The Authorization was successfully validated but permission is not granted. Don’t try again unless you solve permissions first. |
| 404   NOT FOUND | The specified bucket does not exist. |
| 409   CONFLICT | Unable to persist data |
| 416   REQUEST RANGE NOT SATISFIABLE | Missing Content-Range header |
| 500   INTERNAL SERVER ERROR | Internal failure while processing the request, reason depends on error. |

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

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/signedresources/4ff88e65-e7c0-4b10-bac8-750f48b37cf2/resumable"
  -X PUT
  -H "Content-Type:text/plain; charset=UTF-8"
  -H "Content-Range:bytes 0-0/10" -H "Session-Id:1661831201"
  --data '
  X
  '

```

### Response

```
HTTP/1.1 202 Accepted
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Date: Tue, 24 May 2016 20:57:40 GMT
Server: Apigee Router
Content-Length: 0
Connection: keep-alive

```

Show More

## [Example 2](#example-2)

Upload Complete (200)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/signedresources/4ff88e65-e7c0-4b10-bac8-750f48b37cf2/resumable"
  -X PUT
  -H "Content-Type:text/plain; charset=UTF-8"
  -H "Content-Range:bytes 1-9/10"
  -H "Session-Id:1661831201"
  --data '
  bcdefghij
  '

```

Show More

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
 "objectId" : "urn:adsk.objects:os.object:bucketexamplekey/testobject",
 "objectKey" : "testobject",
 "size" : 10,
 "contentType" : "text/plain; charset=UTF-8",
 "location" : "https://developer.api.autodesk.com/oss/v2/buckets/bucketexamplekey/objects/testobject"
}

```

Show More

## [Example 3](#example-3)

Missing Session-ID Header (400)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/signedresources/4ff88e65-e7c0-4b10-bac8-750f48b37cf2/resumable"
  -X PUT
  -H "Content-Type:text/plain; charset=UTF-8"
  -H "Content-Range:bytes 1-9/10"
  --data '
  bcdefghij
  '

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

Session-Id header is missed

```

Show More

#### .

#### Example 4

### Missing Content-Range Header (416)

```
curl -v "https://developer.api.autodesk.com/oss/v2/signedresources/4ff88e65-e7c0-4b10-bac8-750f48b37cf2/resumable"
  -X PUT
  -H "Content-Type:text/plain; charset=UTF-8"
  -H "Session-Id:1661831201"
  --data '
  bcdefghij
  '

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

#### .

#### Example 5

Overlapping Range (416)

Suppose a range of bytes (positions 1-9) was uploaded previously.

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/signedresources/4ff88e65-e7c0-4b10-bac8-750f48b37cf2/resumable"
  -X PUT
  -H "Content-Type:text/plain; charset=UTF-8"
  -H "Content-Range:bytes 1-9/10"
  -H "Session-Id:1661831201"
  --data '
  bcdefghij
  '

```

Show More

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
   "reason" : "Overlapping Ranges"
}

```

Show More
