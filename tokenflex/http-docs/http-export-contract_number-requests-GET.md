# /export/:contract_number/requests

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/export-contract_number-requests-GET/

---

Export

GET

# /export/:contract_number/requests

List export requests for a specified contract.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/tokenflex/v1/export/:contract_number/requests |
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

| contract_number   string | The contract number to retrieve (see [GET contract](http-contract-GET.md)). Use the string null for exports made through the UI and scheduled exports. |
| --- | --- |

## [Request](#id2)

### Query String Parameters

| fromDate*   datetime | The earliest export request date inclusive. For example, `fromDate=2018-08-20T22:43:13.132559Z`. |
| --- | --- |
| toDate*   datetime | The latest export request date exclusive. For example, `toDate=2018-09-21T00:00:00Z`. |

* Required

## [Response](#response)

### HTTP Status Code Summary

| 200   OK | Request succeeded. |
| --- | --- |
| 400   Bad Request | The requested item does not exist or is invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Response](#id3)

### Body Structure (200)

An array of export request JSON objects. See [GET export/:contract_number/requests/:request_key](http-export-contract_number-requests-request_key-GET.md).

## [Example](#example)

Successful listing of all export requests between 2018-10-16T21:22:43Z inclusive and 2018-10-16T22:19:50Z exclusive (200)

### Request

```
curl  -X GET \
      'https://developer.api.autodesk.com/tokenflex/v1/export/110000917988/requests?fromDate=2018-10-16T21:22:43Z&toDate=2018-10-16T22:19:50Z' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N'

```

### Response

```
[
    {
        "requestKey": "2018-10-16T21:22:43#8ab025dc-aa44-4695-b9dd-a0c1694d4917",
        "requestStatus": "Download",
        "downloadFileName": "API_Custom_Export.csv",
        "downloadUrl": "https://download.autodesk.com/8ab025dc-aa44-4695-b9dd-a0c1694d4917_1539725110999.csv?key=LNbpb%2BG7OV9P?signature=BsqMLmmyKo6Wj",
        "downloadUrlExpireDate": "2018-10-16T21:27:11.343Z",
        "exportRequestDate": "2018-10-16T21:22:43.554552Z",
        "readFlag": "N"
    },
    {
        "requestKey": "2018-10-16T22:19:49#94307b1f-363d-46ce-984c-ce97307d1b26",
        "requestStatus": "Download",
        "downloadFileName": "API_Custom_Export.csv",
        "downloadUrl": "https://download.autodesk.com/94307b1f-363d-46ce-984c-ce97307d1b26_1539728457012.csv?key=ASIATSV5SR47M?signature=O8n%2BAe0ZH%2F",
        "downloadUrlExpireDate": "2018-10-16T22:23:08.631439",
        "exportRequestDate": "2018-10-16T22:19:49.76836Z",
        "readFlag": "Y"
    }
]

```

Show More
