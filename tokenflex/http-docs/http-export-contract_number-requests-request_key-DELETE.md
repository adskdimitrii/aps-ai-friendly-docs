# /export/:contract_number/requests/:request_key

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/export-contract_number-requests-request_key-DELETE/

---

Export

DELETE

# /export/:contract_number/requests/:request_key

Delete the specified export request.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/tokenflex/v1/export/:contract_number/requests/:request_key |
| --- | --- |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

## [Request](#request)

### Headers

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

## [Request](#id1)

### URI Parameters

| contract_number   string | The contract number to retrieve (see [GET contract](http-contract-GET.md)). |
| --- | --- |
| request_key   string | The request key for the export request. Note that this parameter must be URI encoded. |

## [Response](#response)

### HTTP Status Code Summary

| 204   No Content | Delete request succeeded. |
| --- | --- |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Example](#example)

Successful deletion of an export request. (204)

### Request

```
curl  -X DELETE \
      'https://developer.api.autodesk.com/tokenflex/v1/export/110000917988/requests/2018-10-29T03%3A25%3A31%234d16aed0-9de2-40c1-9e91-22e3e83c6ce3' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N'

```

### Response

The response will be empty.
