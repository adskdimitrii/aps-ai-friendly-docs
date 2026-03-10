# v1/containers/{containerId}/performance-tracking-items

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-performance-tracking-items-GET/

---

Performance Tracking Item

GET

# v1/containers/{containerId}/performance-tracking-items

Retrieves one or more performance tracking items in the given project. Note that a tracking item contains a subset of the attributes of the budget from which it was created. For more information about performance tracking, see the [Cost Management API Field Guide](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/cost-management/).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/performance-tracking-items |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow.
- regionstring Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [ACC Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.To verify your project’s region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](https://aps.autodesk.com/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page.

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](http-admin-accounts-accountidprojects-GET.md). |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| offset   int | The number of records to skip before returning results. Used together with `limit` to paginate through results, where `offset` specifies the starting point and `limit` specifies the number of records to return. |
| --- | --- |
| limit   int | The maximum number of records returned per page. Default: `100`. A page may contain fewer records than the limit if there are fewer matching items or if it is the last page of results. |
| sort   string | Defines the sort order for the results. Each attribute can be sorted in `asc` (default) or `desc` order. For example, `sort=name desc` sorts the results by name in descending order. |
| filter[id]   array: string: uuid | Returns only the items that are identified by the provided list of item IDs. Separate multiple IDs with commas. For example, `filter[id]=id1,id2`. |
| filter[budgetId]   array: string: uuid | Returns only tracking item instances that belong to the budgets identified by the provided list of budget IDs (separated with commas). For example, `filter[budgetId]=id1,id2`. Note that you can return the instances that are not linked to any budget using `filter[budgetId]=blank`. To find budget IDs, call [GET budgets](http-cost-budgets-GET.md) and inspect `results.id` in the response. |
| filter[budgetCode]   array: string | Filter data that belong to associated budget code. For example, `filter[budgetCode]=code1,code2`. |
| filter[lastModifiedSince]   string | Returns only items that were modified since the specified date and time, in ISO 8601 format. For example, `filter[lastModifiedSince]=2020-03-01T13:00:00Z`. |

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
| results   array: object | The performance tracking item list. |
| id   string: UUID | The ID of the tracking item. |
| containerId   string: UUID | The ID of the cost container for the project to which this tracking item belongs. |
| budgetId   string: UUID | The ID of the tracking item’s underlying budget. |
| name   string | The name of the tracking item’s underlying budget. |
| description   string | The description of the tracking item’s underlying budget. |
| code   string | The code of the tracking item’s underlying budget. |
| quantity   number | The quantity of the performance tracking item’s underlying budget. |
| unit   string | The unit of the performance tracking item’s underlying budget. |
| unitPrice   number,string,null | The unit price of the performance tracking item’s underlying budget. |
| originalAmount   number | Original amount of the budget, equals to `quantity` * `unitPrice` |
| plannedStartDate   datetime: ISO 8601 | The planned start date of the performance tracking item’s underlying budget. |
| plannedEndDate   datetime: ISO 8601 | The planned end date of the performance tracking item’s underlying budget. |
| locations   array,null | A list of the IDs of the project locations where this item applies. <br>For more information, see the Locations [Help documentation](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/locations-nodes-GET/) help. |
| locationPaths   array,null | A list of the IDs of the project locations where this item applies, along with the node paths of these locations in the project’s locations tree. <br>For more information, see the Locations [Help documentation](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/locations-nodes-GET/) help. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/performance-tracking-items?limit=100&sort=name,createdAt desc&filter[lastModifiedSince]=2020-03-01T13:00:00Z' \
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
  "results": [
    {
      "id": "1df59db0-9484-11e8-a7ec-7ddae203e404",
      "containerId": "1df59db0-9484-11e8-a7ec-7ddae203e404",
      "budgetId": "1df59db0-9484-11e8-a7ec-7ddae203e404",
      "name": "Pouring Concrete to Pile Caps",
      "description": "Pouring Concrete to Pile Caps",
      "code": "100.033000.1.LAB",
      "quantity": 2000,
      "unit": "hr",
      "unitPrice": "1000.0000",
      "originalAmount": 1000,
      "plannedStartDate": "2023-01-01T00:00:00.000Z",
      "plannedEndDate": "2025-01-01T00:00:00.000Z",
      "locations": [
        "683904a0-47ce-4146-ac2d-a3840f00e0f4"
      ],
      "locationPaths": [
        "683904a0-47ce-4146-ac2d-a3840f00e0f4"
      ]
    }
  ]
}

```

Show More
