# buckets/:bucketKey/objects/:objectKey/status/:sessionId

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-status-:sessionId-GET/

---

Objects

GET

# buckets/:bucketKey/objects/:objectKey/status/:sessionId

This endpoint returns status information about a resumable upload.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects/:objectKey/status/:sessionId |
| --- | --- |
| Authentication Context | app-only |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be âBearer `<token>`â, where `<token>` is obtained via [POST token](/en/docs/oauth/v2/reference/http/gettoken-POST). |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| bucketKey*   string | URL-encoded bucket key where object was uploaded into |
| --- | --- |
| objectKey*   string | URL-encoded object key to give status for |
| sessionId*   string | Session identifier |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 202   ACCEPTED | Server acknowledges reception of segment |
| --- | --- |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. |
| 403   FORBIDDEN | The Authorization was successfully validated but permission is not granted. Donât try again permission is resolved first. |
| 404   NOT FOUND | The specified bucket does not exist. |
| 416   REQUEST RANGE NOT SATISFIABLE | Missing Content-Range header |
| 500   INTERNAL SERVER ERROR | Internal failure while processing the request, reason depends on error. |

## [Example](#example)

Get Resumable Upload Status (202)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/resumabletest.txt/status/679a7ef0-7b26-4a36-a4d8-968e518a864d"
  -X GET
  -H "Authorization: Bearer ShiAeQ67rdNSfmyEmtGW8Lnrcqto"

```

### Response

```
HTTP/1.1 202 Accepted
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Date: Sat, 21 May 2016 00:29:07 GMT
Range: bytes=0-43,44-83
Server: Apigee Router
Content-Length: 0
Connection: keep-alive

```

Show More
