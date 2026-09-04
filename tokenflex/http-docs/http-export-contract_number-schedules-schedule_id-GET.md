# /export/:contract_number/schedules/:schedule_id

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/export-contract_number-schedules-schedule_id-GET/

---

Export

GET

# /export/:contract_number/schedules/:schedule_id

Get details on the specified schedule.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/tokenflex/v1/export/:contract_number/schedules/:schedule_id |
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
| schedule_id   string | ID of schedule. Note that this parameter must be URI encoded. |

## [Response](#response)

### HTTP Status Code Summary

| 200   OK | Request succeeded. |
| --- | --- |
| 400   Bad Request | The specified schedule does not exist or is otherwise invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Response](#id2)

### Body Structure (200)

| scheduleID   string | Unique ID of the schedule. |
| --- | --- |
| dateRangeExpression   string | An expression for the time period to export. Currently only `Previous-1-Month` is supported. |
| enableFlag   string | Enabled (will run) if `Y`, otherwise disabled. |
| frequencyExpression   string | A cron-like expression for how often the schedule will run. Fields are seconds, minutes, hours, day of month, month, day of week. |
| lastRanDate   datetime | The last time this schedule ran or `null` if not yet run. |
| nextRunDate   datetime | Optional if enabled. The next time this schedule will run from the current datetime. |
| scheduleObjects   object | An object that describes the reports that have been scheduled. |

## [Example](#example)

Successful getting an export schedule. (200)

### Request

```
curl  -X GET \
      'https://developer.api.autodesk.com/tokenflex/v1/export/110000917988/schedules/423744f5-0c21-40c9-a8d9-73bb234ef7bb' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N'

```

### Response

```
{
    "dateRangeExpression": "Previous-1-Month",
    "enableFlag": "Y",
    "frequencyExpression": "0 0 11 4 * *",
    "lastRanDate": null,
    "nextRunDate": "2018-11-04T11:00:00Z",
    "scheduleID": "423744f5-0c21-40c9-a8d9-73bb234ef7bb",
    "scheduleObjects": [
        {
            "aggregationLevel": [
                "Transactional",
                "Daily",
                "Monthly"
            ],
            "usageCategory": "DESKTOP_PRODUCT"
        },
        {
            "aggregationLevel": [
                "Transactional",
                "Daily",
                "Monthly"
            ],
            "usageCategory": "CLOUD"
        }
    ]
}

```

Show More
