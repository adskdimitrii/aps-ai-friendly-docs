# v1/containers/{containerId}/time-sheets/{id}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-time-sheets-id-PATCH/

---

Timesheet

PATCH

# v1/containers/{containerId}/time-sheets/{id}

Updates the specified timesheet in the given project.

Note that Cost API timesheets endpoints are designed only for use with a third party tracking app that youâve synchronized with Cost Management. For more information, see [Performance Tracking](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Performance_Tracking).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/cost/v1/containers/:containerId/time-sheets/:id |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| region   string | Specifies the region where the project data resides. <br>By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.<br>Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [ACC Regions](/en/docs/acc/v1/overview/acc-regions) page.<br>To verify your projectâs region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](/en/docs/bim360/v1/reference/http/admin-accounts-accountidprojects-GET/). |
| --- | --- |
| id   string | The timesheet ID. To find the timesheet ID, call [GET time-sheets](/en/docs/bim360/v1/reference/http/cost-time-sheets-GET/) and inspect `results.id` in the response. |

### Request

## [Body Structure](#body-structure)

The timesheet

| trackingItemInstanceId   string,null | The ID of the tracking item instance to which the timesheet will belong. Required if both `trackingItemInstanceNumber` and `budgetCode` are omitted from this request. To find the instance ID, call [GET performance-tracking-item-instances](/en/docs/bim360/v1/reference/http/cost-performance-tracking-item-instances-GET/) and inspect `results.id` in the response. |
| --- | --- |
| trackingItemInstanceNumber   string,null | The user-provided code that represents the tracking item instance to which the timesheet will belong. Required if both `trackingItemInstanceId` and `budgetCode` are omitted from this request. To find the instance number, call [GET performance-tracking-item-instances](/en/docs/bim360/v1/reference/http/cost-performance-tracking-item-instances-GET/) and inspect `results.number` in the response. |
| budgetCode   string,null | The code that identifies the budget to which the timesheet belongs. Required if both `trackingItemInstanceId` and `trackingItemInstanceNumber` are omitted from this request. To find the budget code, call [GET budgets](/en/docs/bim360/v1/reference/http/cost-budgets-GET/) and inspect `results.code` in the response. |
| startDate   string | The first date of the time period covered by the timesheet. |
| endDate   string | The last date of the time period covered by the timesheet. This is also the date that the tracked `inputQuantity` and `outputQuantity` values are considered to have been reported. |
| inputQuantity   number | The hours worked during the time period covered by the timesheet. |
| outputQuantity   number | The quantity of material used during time period covered by the timesheet. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success |
| --- | --- |
| 400   Bad Request | The parameters are invalid. |
| 401   Unauthorized | The provided bearer token is invalid. |
| 403   Forbidden | Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The resource or endpoint cannot be found. |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the resource. |
| 429   Too Many Requests | Rate limit exceeded. Retry your request after a few minutes. |
| 500   Internal Server Error | An unexpected error occurred on the server. |
| 503   Service Unavailable | Service unavailable. |

### Response

## [Body Structure (200)](#body-structure-200)

| id   string: UUID | The ID of the timesheet. |
| --- | --- |
| containerId   string: UUID | The ID of the cost container for the project to which the timesheet belongs. |
| trackingItemInstanceId   string: UUID | The ID of the tracking item instance to which the timesheet belongs. |
| startDate   string | The first date of the time period covered by the timesheet. |
| endDate   string | The last date of the time period covered by the timesheet. This is also the date that the tracked `inputQuantity` and `outputQuantity` values are considered to have been reported. |
| inputQuantity   number | The hours worked during the time period covered by the timesheet. |
| inputUnit   string | The input unit of measurement of the timesheet. Currently this value should always be `hr`. |
| outputQuantity   number | The quantity of material used during time period covered by the timesheet. |
| outputUnit   string | The output unit of measurement of the timesheet. |
| creatorId   string,null | The BIM 360/ACC ID of the user who created the timesheet. |
| changedBy   string,null | The BIM 360/ACC ID of the user who made the last change to the timesheet. |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/time-sheets/9e027d30-9483-11e8-a7ec-7ddae203e404' \
  -X 'PATCH' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "trackingItemInstanceId": "1df59db0-9484-11e8-a7ec-7ddae203e404",
        "trackingItemInstanceNumber": "84720010121001FEE-01",
        "budgetCode": "84720010121001FEE",
        "startDate": "2020-01-06",
        "endDate": "2020-01-06",
        "inputQuantity": "100",
        "outputQuantity": "100"
      }'

```

Show More

### Response

```
{
  "id": "1df59db0-9484-11e8-a7ec-7ddae203e404",
  "containerId": "1df59db0-9484-11e8-a7ec-7ddae203e404",
  "trackingItemInstanceId": "1df59db0-9484-11e8-a7ec-7ddae203e404",
  "startDate": "2020-01-06",
  "endDate": "2020-01-06",
  "inputQuantity": "100",
  "inputUnit": "hr",
  "outputQuantity": "100",
  "outputUnit": "cy",
  "creatorId": "CED9LVTLHNXV",
  "changedBy": "CED9LVTLHNXV",
  "createdAt": "2019-01-06T01:24:22.678Z",
  "updatedAt": "2019-09-05T01:00:12.989Z"
}

```

Show More
