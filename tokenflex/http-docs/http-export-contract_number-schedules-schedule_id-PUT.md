# /export/:contract_number/schedules/:schedule_id

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/export-contract_number-schedules-schedule_id-PUT/

---

Export

PUT

# /export/:contract_number/schedules/:schedule_id

Update an existing schedule.

## [Resource Information](#resource-information)

| Method and URI | PUT https://developer.api.autodesk.com/tokenflex/v1/export/:contract_number/schedules/:schedule_id |
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

| contract_number   string | The contract number to retrieve (see [GET contract](http-contract-GET.md)). |
| --- | --- |
| schedule_id   string | ID of schedule. Note that this parameter must be URI encoded. |

## [Response](#response)

### HTTP Status Code Summary

| 200   OK | Request succeeded. |
| --- | --- |
| 400   Bad Request | The request was invalid, or some parameter has values that are not allowed. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Request](#id2)

### Body Structure (200)

The updated schedule object. See [GET export/:contract_number/schedules/:schedule_id](http-export-contract_number-schedules-schedule_id-GET.md).

## [Example](#example)

Successful updating an export schedule and setting the enableFlag to disabled. (200)

### Request

```
curl  -X PUT \
      'https://developer.api.autodesk.com/tokenflex/v1/export/110000917988/schedules/423744f5-0c21-40c9-a8d9-73bb234ef7bb' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N' \
      -d '{
          "enableFlag": "N",
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
    "enableFlag": "N",
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
            "usageCategory": "CLOUD"
        }
    ]
}

```

Show More
