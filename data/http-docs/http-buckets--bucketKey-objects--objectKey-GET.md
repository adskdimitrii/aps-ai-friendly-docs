# buckets/:bucketKey/objects/:objectKey

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-GET/

---

Objects

GET

# buckets/:bucketKey/objects/:objectKey

Deprecated

Download an object.

**We will be deprecating this endpoint.**

We recommend using the [GET buckets/:bucketKey/objects/:objectKey/signeds3download](http-buckets--bucketKey-objects--objectKey-signeds3download-GET.md) endpoint. See the [Download a File](../how-to-docs/download-file.md) for step by step workflow.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects/:objectKey |
| --- | --- |
| Authentication Context | app-only |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be âBearer `<token>`â, where `<token>` is obtained via [POST token](../../oauth/http-docs/http-gettoken-POST.md). |
| --- | --- |
| Range   byte range | A range of bytes to download from the specified object. |
| If-None-Match   string | The value of this header is compared to the ETAG of the object. If they match, the body will not be included in the response. Only the object information will be included. |
| If-Modified-Since   HTTP date | If the requested object has not been modified since the time specified in this field, an entity will not be returned from the server; instead, a `304` (not modified) response will be returned without any message-body. |
| Accept-Encoding   string | When gzip is specified, a gzip compressed stream of the objectâs bytes will be returned in the response. Cannot use âAccept-Encoding:gzipâ with Range header containing an end byte range. End byte range will not be honored if âAccept-Encoding: gzipâ header is used. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| bucketKey*   string | URL-encoded bucket key |
| --- | --- |
| objectKey*   string | URL-encoded object key |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   SUCCESS |  |
| --- | --- |
| 206   PARTIAL CONTENT | The server is delivering only part of the resource due to a range header sent by the client. |
| 304   NOT MODIFIED | If using the If-None-Match header on the request and it matches the objectâs ETAG, no content will be sent. Or, if using If-Modified-Since header and the object has not been modified since the time specified, no content will be sent. |
| 401   AUTHORIZATION FAILURE | The OAuth2 token being used is not present or is invalid. |
| 403   ACCESS DENIED | The calling service or client application does not have sufficient privileges to download the object from this bucket. |
| 404   NOT FOUND | The bucket key / object key combination was not found |
| 429   THROTTLE | The server is busy. Please retry. |
| 500   EXCEPTION | A server side error occurred. |

## [Example 1](#example-1)

Download file - Success (200)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/test.txt"
  -X GET
  -H "Authorization: Bearer ShiAeQ67rdNSfmyEmtGW8Lnrcqto"

```

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Disposition: attachment; filename="test.txt"
Content-Type: application/x-www-form-urlencoded
Date: Sat, 21 May 2016 00:24:25 GMT
ETag: "33a16388013ce310564af70b0ef5320d8fd85444"
Server: Apigee Router
Content-Length: 618
Connection: keep-alive

The quick brown fox jumps over the lazy dog
Pack my box with five dozen liquor jugs
Cozy lummox gives smart squid who asks for job pen
Sphinx of black quartz, judge my vow
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

```

Show More

## [Example 2](#example-2)

Download Byte Range - Partial Content (206)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/test.txt"
  -X GET
  -H "Authorization: Bearer ShiAeQ67rdNSfmyEmtGW8Lnrcqto"
  -H "Range: bytes=44-83"

```

### Response

```
HTTP/1.1 206 Partial Content
Accept-Ranges: bytes
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Disposition: attachment; filename="test.txt"
Content-Range: bytes 44-83/618
Content-Type: application/x-www-form-urlencoded
Date: Sat, 21 May 2016 00:26:22 GMT
Server: Apigee Router
Content-Length: 40
Connection: keep-alive

Pack my box with five dozen liquor jugs

```

Show More
