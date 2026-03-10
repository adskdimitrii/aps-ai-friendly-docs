# v1/containers/{containerId}/cost-items/{costItemId}/sub-cost-items

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-sub-cost-items-GET/

---

Sub Cost Items

GET

# v1/containers/{containerId}/cost-items/{costItemId}/sub-cost-items

Retrieves sub cost items associated with a specific cost item in a project.
For more information about cost and sub cost items, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Cost_Items#add-a-cost-item).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/cost-items/:costItemId/sub-cost-items |
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
| costItemId   array: string: uuid | A cost item ID to retrieve sub cost items for one cost item in a single request. The response includes all sub cost items associated with the specified cost item. Cost items do not have parent-child relationships, but sub cost items can be structured under other sub cost items. To find the cost item ID, call [GET cost-items](http-cost-cost-items-GET.md). |

### Request

## [Query String Parameters](#query-string-parameters)

| filter[type]   enum:string | The type of the value to break down. Possible values: `estimated`, `proposed`, `submitted`, `approved`, `committed` |
| --- | --- |
| offset   int | The number of records to skip before returning results. Used together with `limit` to paginate through results, where `offset` specifies the starting point and `limit` specifies the number of records to return. |
| limit   int | The maximum number of records returned per page. Default: `100`. A page may contain fewer records than the limit if there are fewer matching items or if it is the last page of results. |
| sort   string | Defines the sort order for the results. Each attribute can be sorted in `asc` (default) or `desc` order. For example, `sort=name desc` sorts the results by name in descending order. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The request was successful, returning the retrieved sub cost items. |
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
| results   array: object | A list of sub cost items associated with the requested cost items. |
| id   string: UUID | The unique ID of the sub cost item. |
| parentId   string,null | The unique ID of the parent sub cost item. A sub cost item has a parent Id when it is part of a hierarchical cost structure. Root sub cost items do not have a parent ID. |
| type   enum:string | The classification of the sub cost item that indicates its role in cost tracking and approval workflows. Possible values: `estimated`, `proposed`, `submitted`, `approved`, `committed`. <br>Max length: 255 |
| costItemId   string | The ID of the cost item to which the sub cost item belongs. |
| code   string | The identifier for the sub cost item. If copied from another model, for example, a `Contract SOV`, it inherits the code. Otherwise, it is manually assigned. <br>Max length: 255 |
| position   number,null | The position of the sub cost item relative to its sibling sub cost items. If a new sub cost item is assigned a position that already exists, the system shifts existing items downward to maintain order. |
| name   string | The name of the sub cost item. <br>Max length: 1024 |
| quantity   number,string,null | The planned number of units allocated for the sub cost item. |
| inputQuantity   number,string,null | The recorded input quantity, typically used in performance tracking. For example, in labor tracking, `inputQuantity` represents man-hours utilized. |
| unitPrice   number,string,null | The price per individual unit of the sub cost item. |
| unit   string | The unit of measurement for the sub cost item. This value is configured in the `Unit of measure` settings for the project. Common units include `ea` (Each), `gal` (Gallon), and various volume, length, and time measurements. <br>Max length: 1024 |
| value   number,string,null | The total value of the sub cost item, calculated as `quantity` * `unitPrice`. |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |

## [Example](#example)

The request was successful, returning the retrieved sub cost items.

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/cost-items/eb284d80-f026-11e7-98ee-cb31483cc0ac/sub-cost-items?filter[type]=estimated&limit=100&sort=name,createdAt desc' \
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
      "id": "8f127780-96d6-11e8-81a8-cd51c63a9484",
      "parentId": null,
      "type": "estimated",
      "costItemId": "eb284d80-f026-11e7-98ee-cb31483cc0ac",
      "code": "0002",
      "position": 1,
      "name": "concrete flooring",
      "quantity": "1.0000",
      "inputQuantity": "1000.0000",
      "unitPrice": "1000.0000",
      "unit": "ea",
      "value": "1000.0000",
      "createdAt": "2019-01-06T01:24:22.678Z",
      "updatedAt": "2019-09-05T01:00:12.989Z"
    }
  ]
}

```

Show More
