# buckets/:bucketKey

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-DELETE/

---

Buckets

DELETE

# buckets/:bucketKey

Deletes a bucket. The bucket must be owned by the application.

Warning:This operation is irreversable and cannot be undone.

We recommend only deleting small buckets used for acceptance testing or prototyping, since it can take a long time for a bucket to be deleted.

Note that the bucket name will not be immediately available for reuse.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey |
| --- | --- |
| Authentication Context | app-only |
| Required OAuth Scopes | `bucket:delete` |

### Request

## [Headers](#headers)

| Authorization*   string | Must be âBearer `<token>`â, where `<token>` is obtained via [POST token](/en/docs/oauth/v2/reference/http/gettoken-POST). |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| bucketKey*   string | URL-encoded bucket name |
| --- | --- |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful operation. |
| --- | --- |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify authentication and try again. |
| 403   FORBIDDEN | The Authorization was successfully validated but permission is not granted. Donât try again unless you solve permissions first. |
| 404   NOT FOUND | The specified bucketKey does not exist. |
| 409   CONFLICT | The bucket is currently marked for deletion |
| 500   INTERNAL SERVER ERROR | Internal failure while processing the request, reason depends on error. |

### Response

## [Body Structure (200)](#body-structure-200)

For a successful delete request, an HTTP 200 will be returned with no text in the response body.

## [Example](#example)

Delete Bucket (200)

### Request

```
   curl -v "https://developer.api.autodesk.com/oss/v2/buckets/bucketexamplekey"
-X DELETE
-H "Authorization: Bearer kuhodzPEHSCrWH3Pm1WuBMBnxw39"

```

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Date: Wed, 25 May 2016 19:39:39 GMT
Server: Apigee Router
Content-Length: 0
Connection: keep-alive

```

Show More
