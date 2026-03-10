# signedresources/:id

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/signedresources-:id-GET/

---

Objects

GET

# signedresources/:id

Download an object using a signed URL.
If you set the URL to expire after it is used the first time, it will expire when the download is complete.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/oss/v2/signedresources/:id |
| --- | --- |
| Authentication Context | *none* |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Range   byte range | A range of bytes to download from the specified object. |
| --- | --- |
| If-None-Match   string | The value of this header is compared to the ETAG of the object. If they match, the body will not be included in the response. Only the object information will be included. |
| If-Modified-Since   HTTP date | If the requested object has not been modified since the time specified in this field, an entity will not be returned from the server; instead, a 304 (not modified) response will be returned without any message-body. |
| Accept-Encoding   string | When gzip is specified, a gzip compressed stream of the object’s bytes will be returned in the response. Cannot use “Accept-Encoding:gzip” with Range header containing an end byte range. End byte range will not be honored if “Accept-Encoding: gzip” header is used. |

### Request

## [URI Parameters](#uri-parameters)

| id*   string | ID of signed resource |
| --- | --- |

* Required

### Request

## [Query String Parameters](#query-string-parameters)

| region   enum | The region where the bucket resides   Acceptable values: `US`, `EMEA` Default: `US` |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful operation |
| --- | --- |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied authorization header was not valid or the supplied token scope was not acceptable. Verify authentication and try again. |
| 403   FORBIDDEN | The authorization was successfully validated but permission is not granted. Don’t try again unless permission is resolved first. |
| 404   NOT FOUND | The specified resource does not exist. |
| 412   PRECONDITION FAILED |  |
| 500   INTERNAL SERVER ERROR | Internal failure while processing the request, reason depends on error. |

### Response

## [Body Structure (200)](#body-structure-200)

Raw bytes

## [Example](#example)

Download Using a Signed URL - Success (200)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/signedresources/7ffc5eef-1407-4c24-b3f3-3cbfe32a9232?region=US"
  -X GET

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
Date: Mon, 23 May 2016 18:10:35 GMT
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
