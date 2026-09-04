# /export/:contract_number/requests/:request_key

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/export-contract_number-requests-request_key-GET/

---

Export

GET

# /export/:contract_number/requests/:request_key

Retrieve details for an export request.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/tokenflex/v1/export/:contract_number/requests/:request_key |
| --- | --- |
| Required OAuth Scopes | `data:read` |
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

| requestKey   string | ID of the export request |
| --- | --- |
| requestStatus   string | Current state of the request (`Requested`, `Download`, `Error`) |
| downloadFileName   string | Friendly name of exported file |
| downloadUrl   string | A pre-signed URL where the file can be downloaded. Note this URL allows anyone to download through it, so take caution not to share it. |
| downloadUrlExpireDate   datetime | An ISO8601 timestamp for the expiration of the pre-signed downloadUrl |
| exportRequestDate   datetime | An ISO8601 timestamp for when the request was originally made |
| scheduleId   string | Optional ID of the schedule this was triggered from. |
| readFlag   string | Read if `Y`, not read otherwise. (Corresponds to UI indicator) |

## [Example](#example)

Successful polling for an export request. (200)

### Request

```
curl  -X GET \
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
