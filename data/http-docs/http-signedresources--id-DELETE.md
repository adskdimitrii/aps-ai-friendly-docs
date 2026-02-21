# signedresources/:id

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/signedresources-:id-DELETE/

---

Objects

DELETE

# signedresources/:id

Delete a signed URL. A successful call to this endpoint requires bucket owner access.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/oss/v2/signedresources/:id |
| --- | --- |
| Authentication Context | app-only |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [URI Parameters](#uri-parameters)

| id*   string | Id of signed resource |
| --- | --- |

* Required

### Request

## [Query String Parameters](#query-string-parameters)

| region   enum | The region where the bucket resides   Acceptable values: `US`, `EMEA` Default: `US` |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK |  |
| --- | --- |
| 401   UNAUTHORIZED | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify authentication and try again. |
| 403   FORBIDDEN | The Authorization was successfully validated but permission is not granted. Donât try again unless you solve permissions first. |
| 404   NOT FOUND | Hash does not exist. |
| 500   INTERNAL SERVER ERROR | Internal failure while processing the request, reason depends on error. |

### Response

## [Body Structure (200)](#body-structure-200)

For a successful delete request, an HTTP 200 will be returned with a text response body:

Signed resource deleted successfully: <ID>

## [Example](#example)

Delete Signed Resource - Success (200)

### Request

```
    curl -v "https://developer.api.autodesk.com/oss/v2/signedresources/322cca8f-4cbf-448f-b70b-55df2597b0d2"
-X DELETE
-H "Authorization: Bearer tQrZGiR0L1rYRAtEAsGyvA9ZF9Nj"

```

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: text/plain; charset=utf-8
Date: Mon, 23 May 2016 18:15:15 GMT
Server: Apigee Router
Content-Length: 74
Connection: keep-alive

Signed resource deleted successfully: 7ffc5eef-1407-4c24-b3f3-3cbfe32a9232

```

Show More
