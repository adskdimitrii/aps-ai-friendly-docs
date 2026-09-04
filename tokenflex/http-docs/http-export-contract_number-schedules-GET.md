# /export/:contract_number/schedules

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/export-contract_number-schedules-GET/

---

Export

GET

# /export/:contract_number/schedules

List all schedules for the specified contract.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/tokenflex/v1/export/:contract_number/schedules |
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

| contract_number   string | The contract number of the schedule (see [GET contract](http-contract-GET.md)). |
| --- | --- |

## [Response](#response)

### HTTP Status Code Summary

| 200   OK | Request succeeded. |
| --- | --- |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Response](#id2)

### Body Structure (200)

A JSON array of schedule objects. See [GET export/:contract_number/schedules/:schedule_id](http-export-contract_number-schedules-schedule_id-GET.md).

## [Example](#example)

Successful listing of all export requests between 2018-10-16T21:22:43Z inclusive and 2018-10-16T22:19:50Z exclusive (200)

### Request

```
curl  -X GET \
      'https://developer.api.autodesk.com/tokenflex/v1/export/110000917988/schedules' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N'

```

### Response

```
[
    {
        "dateRangeExpression": "Previous-1-Month",
        "enableFlag": "Y",
        "frequencyExpression": "0 0 18 5 * *",
        "lastRanDate": "2018-10-05T18:00:00Z",
        "nextRunDate": "2018-11-05T18:00:00Z",
        "scheduleID": "a5d118df-31ce-4f57-a7d9-73f5564e914a",
        "scheduleObjects": [
            {
                "aggregationLevel": [
                    "Daily"
                ],
                "usageCategory": "DESKTOP_PRODUCT"
            },
            {
                "aggregationLevel": [
                    "Daily"
                ],
                "usageCategory": "CLOUD"
            }
        ]
    }
]

```

Show More
