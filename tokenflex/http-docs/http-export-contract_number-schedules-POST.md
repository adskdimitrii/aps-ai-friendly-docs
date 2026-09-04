# /export/:contract_number/schedules

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/export-contract_number-schedules-POST/

---

Export

POST

# /export/:contract_number/schedules

Create a new schedule.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/tokenflex/v1/export/:contract_number/schedules |
| --- | --- |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

## [Request](#request)

### Headers

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

## [Request](#id1)

### URI Parameters

| contract_number   string | The contract number of the schedule (see [GET contract](http-contract-GET.md)). Please note that this parameter currently has no effect on the data exported. It will always be the current active contract. |
| --- | --- |

## [Request](#id2)

### Body Structure

| dateRangeExpression   string | An expression for the time period to export. Currently only `Previous-1-Month` is supported. |
| --- | --- |
| enableFlag   string | Enabled (will run) if `Y`, otherwise disabled. |
| frequencyExpression   string | A cron-like expression for how often the schedule will run. Fields are seconds, minutes, hours, day of month, month, day of week. |
| scheduleObjects   array | An array of JSON objects that describes the reports to schedule. |
| scheduleObjects.scheduleObjects[i]   object | A report object |
| scheduleObjects.scheduleObjects[i].usageCategory   string | Usage category to export. Must be one of `DESKTOP_PRODUCT` or `CLOUD`. The `CLOUD` category includes both `CLOUD_PRODUCT` and `CLOUD_SERVICE`. Exports of adjustment-related data cannot be scheduled. |
| scheduleObjects.scheduleObjects[i].aggregationLevel   string array | The aggregation levels to include. Must be one of `Transactional`, `Daily`, or `Monthly`. |

## [Response](#response)

### HTTP Status Code Summary

| 200   OK | Request succeeded. |
| --- | --- |
| 400   Bad Request | The request was invalid, or some parameter has values that are not allowed. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Response](#id3)

### Body Structure (200)

A newly created schedule object for the request. See [GET export/:contract_number/schedules/:schedule_id](http-export-contract_number-schedules-schedule_id-GET.md).

## [Example](#example)

Successful creating an export schedule. (200)

### Request

```
curl  -X POST \
      'https://developer.api.autodesk.com/tokenflex/v1/export/110000917988/schedules' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N' \
      -d '{
          "enableFlag": "Y",
          "scheduleObjects": [
              {
                  "usageCategory": "DESKTOP_PRODUCT",
                  "aggregationLevel": [
                      "Transactional",
                      "Daily",
                      "Monthly"
                  ]
              },
              {
                  "usageCategory": "CLOUD",
                  "aggregationLevel": [
                      "Transactional",
                      "Daily",
                      "Monthly"
                  ]
              }
          ],
          "dateRangeExpression": "Previous-1-Month",
          "frequencyExpression": "0 0 11 4 * *"
      }'

```

Show More

### Response

```
{
    "dateRangeExpression": "Previous-1-Month",
    "enableFlag": "Y",
    "frequencyExpression": "0 0 11 4 * *",
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
            "usageCategory": "CLOUD_SERVICE"
        },
        {
            "aggregationLevel": [
                "Daily",
                "Monthly"
            ],
            "usageCategory": "CLOUD_PRODUCT"
        }
    ]
}

```

Show More
