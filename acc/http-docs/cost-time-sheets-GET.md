# v1/containers/{containerId}/time-sheets

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-time-sheets-GET/

---

Timesheet

GET

# v1/containers/{containerId}/time-sheets

Retrieves one or more timesheets in the given project.

Note that Cost API timesheets endpoints are designed only for use with a third party tracking app that youâve synchronized with Cost Management. For more information, see [Performance Tracking](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Performance_Tracking).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/time-sheets |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow.
- regionstring Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [ACC Regions](/en/docs/acc/v1/overview/acc-regions) page.To verify your projectâs region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page.

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](/en/docs/bim360/v1/reference/http/admin-accounts-accountidprojects-GET/). |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| offset   int | The number of records to skip before returning results. Used together with `limit` to paginate through results, where `offset` specifies the starting point and `limit` specifies the number of records to return. |
| --- | --- |
| limit   int | The maximum number of records returned per page. Default: `100`. A page may contain fewer records than the limit if there are fewer matching items or if it is the last page of results. |
| sort   string | Defines the sort order for the results. Each attribute can be sorted in `asc` (default) or `desc` order. For example, `sort=name desc` sorts the results by name in descending order. |
| filter[budgetCode]   string | Filter data that belong to associated budget code. For example, `filter[budgetCode]=code`. <br>To find budget codes, call [GET budgets](/en/docs/bim360/v1/reference/http/cost-budgets-GET/) and inspect `results.code` in the response. |
| filter[trackingItemInstanceId]   string: UUID | Filter data that belong to associated tracking item instance id. For example, `filter[trackingItemInstanceId]=id`. |
| filter[lastModifiedSince]   string | Returns only items that were modified since the specified date and time, in ISO 8601 format. For example, `filter[lastModifiedSince]=2020-03-01T13:00:00Z`. |
| include   array: string | Include additional resources in the response. For example, `include=meta` will return the meta data. Possible values: `meta`. |
| filter[startDate]   string | Filter data by its start date. This may be an ISO 8601 string or a range. Ranges can be **lowerValue..upperValue**, **lowerValue..** or **..upperValue**. The range tests are always inclusive of their endpoints. |
| filter[endDate]   string | Filter data by its end date. This may be an ISO 8601 string or a range. Ranges can be **lowerValue..upperValue**, **lowerValue..** or **..upperValue**. The range tests are always inclusive of their endpoints. |

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

Expand all

| pagination   object | Contains pagination information when data is returned page by page. |
| --- | --- |
| limit   int | The maximum number of records returned in the response. |
| offset   int | The number of records skipped before returning the page of results. |
| totalResults   int | The total number of records that matched the request criteria. |
| nextUrl   string | The URL for the next request to retrieve the next page of results. Max length: 2000. <br>Max length: 2000 |
| meta   object |  |
| totalPreviousInputQuantity   number,null | Total sum of timesheet logs input quantity before given `trackingItemInstanceId` and `endDate` filter. `null` if not applicable. |
| totalPreviousOutputQuantity   number,null | Total sum of timesheet logs output quantity before given `trackingItemInstanceId` and `endDate` filter. `null` if not applicable. |
| results   array: object | The timesheet list. |
| id   string: UUID | The ID of the timesheet. |
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
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/time-sheets?limit=100&sort=name,createdAt desc&filter[budgetCode]=code&filter[trackingItemInstanceId]=b6445638-ca68-4e3c-9160-15864de6b818&filter[lastModifiedSince]=2020-03-01T13:00:00Z&filter[startDate]=2020-10-31T14:48:00.000Z..2020-11-01T14:48:00.000Z&filter[endDate]=2020-10-31T14:48:00.000Z..2020-11-01T14:48:00.000Z' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 20,
    "offset": 0,
    "totalResults": 1,
    "nextUrl": ""
  },
  "meta": {
    "totalPreviousInputQuantity": "200",
    "totalPreviousOutputQuantity": "200"
  },
  "results": [
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
  ]
}

```

Show More
