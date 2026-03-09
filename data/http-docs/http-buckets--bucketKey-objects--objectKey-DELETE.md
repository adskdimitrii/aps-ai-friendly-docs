# buckets/:bucketKey/objects/:objectKey

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-DELETE/

---

Objects

DELETE

# buckets/:bucketKey/objects/:objectKey

Deletes an object from the bucket.

Warning:This operation is irreversable and cannot be undone.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects/:objectKey |
| --- | --- |
| Authentication Context | app-only |
| Required OAuth Scopes | `data:write` |

### Request

## [Headers](#headers)

| Authorization*   string | Must be âBearer `<token>`â, where `<token>` is obtained via [POST token](../../oauth/http-docs/http-gettoken-POST.md). |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| bucketKey*   string | URL-encoded bucket where object was uploaded into. |
| --- | --- |
| objectKey*   string | URL-encoded object key to to be deleted. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful operation. |
| --- | --- |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify authentication and try again. |
| 403   FORBIDDEN | The Authorization was successfully validated but permission is not granted. Donât try again unless you solve permissions first. |
| 404   NOT FOUND | The specified bucketKey/objectKey does not exist. |
| 500   INTERNAL SERVER ERROR | Internal failure while processing the request, reason depends on error. |

### Response

## [Body Structure (200)](#body-structure-200)

For a successful delete request, an HTTP 200 will be returned with an empty text in response body:

## [Example](#example)

Delete Object (200)

### Request

```
   curl -v "https://developer.api.autodesk.com/oss/v2/buckets/bucketexamplekey/objects/objectKey"
-X DELETE
-H "Authorization: Bearer kuhodzPEHSCrWH3Pm1WuBMBnxw39"
-H "Content-Type: application/json;charset=UTF-8"

```

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Date: Wed, 25 May 2016 19:39:39 GMT
Server Apigee Router is not blacklisted
Server: Apigee Router
Content-Length: 0
Connection: keep-alive

```

Show More
