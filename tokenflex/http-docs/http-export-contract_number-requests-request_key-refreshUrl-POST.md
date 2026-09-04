# /export/:contract_number/requests/:request_key/refreshUrl

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/export-contract_number-requests-request_key-refreshUrl-POST/

---

Export

POST

# /export/:contract_number/requests/:request_key/refreshUrl

Get a new pre-signed URL to the exported file for an export request.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/tokenflex/v1/export/:contract_number/requests/:request_key/refreshUrl |
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

| 200   OK | Request succeeded. |
| --- | --- |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Response](#id2)

### Body Structure (200)

The entire export request object with an updated donwloadUrl. See [GET export/:contract_number/requests/:request_key](http-export-contract_number-requests-request_key-GET.md).

## [Example](#example)

Successfully getting a new download URL for an export request. (200)

### Request

```
curl  -X POST \
      'https://developer.api.autodesk.com/tokenflex/v1/export/110000917988/requests/2018-10-29T03%3A25%3A31%234d16aed0-9de2-40c1-9e91-22e3e83c6ce3' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N'

```

### Response

```
{
    "requestKey": "2018-10-29T03:25:31#4d16aed0-9de2-40c1-9e91-22e3e83c6ce3",
    "requestStatus": "Download",
    "downloadFileName": "DesktopUsage Oct 2017.csv",
    "downloadUrl": "https://download.autodesk.com/4d16aed0-9de2-40c1-9e91-22e3e83c6ce3_1540783561402.csv?key=LNbpb%2BG7OV9P?signature=BsqMLmmyKo6Wj",
    "downloadUrlExpireDate": "2018-10-29T03:31:25.162832Z",
    "exportRequestDate": "2018-10-29T03:25:31.408219Z",
    "readFlag": "N"
}

```

Show More
