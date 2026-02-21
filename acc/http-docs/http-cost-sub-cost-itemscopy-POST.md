# v1/containers/{containerId}/cost-items/{costItemId}/sub-cost-items:copy

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-sub-cost-itemscopy-POST/

---

Sub Cost Items

POST

# v1/containers/{containerId}/cost-items/{costItemId}/sub-cost-items:copy

Copies sub cost items from a source type to a target type within a cost item, replacing any existing sub cost items of the target type.

When copying from a budget or a contract, the request must include specific IDs that identify the source budget items or contract Schedule of Values (SOV) items. All sub cost items associated with these provided IDs are copied to the specified target type within the cost item.

For example, to copy sub cost items from a `contract SOV` to `estimated` sub cost items, use the endpoint with your specific project IDs.

In the request body, set `from` as `contract`, `to` as `estimated`, and specify the contract SOV IDs in the `source.ids` array. After copying, you can verify the changes by calling [GET sub-cost-items](/en/docs/acc/v1/reference/http/cost-sub-cost-items-GET/).

For more information about cost and sub cost items, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Cost_Items#add-a-cost-item).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/cost/v1/containers/:containerId/cost-items/:costItemId/sub-cost-items:copy |
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
| costItemId   string: UUID | The ID of the cost item to which the sub cost item belongs. To find the cost item ID, call [GET cost-items](/en/docs/bim360/v1/reference/http/cost-cost-items-GET/). |

### Request

## [Body Structure](#body-structure)

The request body.

Expand all

| from*   enum:string | The type of the sub cost items being copied. Note that `contract` and `budget` can only be used as a source type, not a destination. Possible values: `contract`, `budget`, `estimated`, `proposed`, `submitted`, `approved`, `committed`. |
| --- | --- |
| to*   enum:string | The type to which the sub cost items are copied. Note that `contract` and `budget` cannot be used as a destination. Possible values: `estimated`, `proposed`, `submitted`, `approved`, `committed`. |
| source   object | The source object defining where sub-cost items are copied from. When copying from a `budget` or `contract`, this must include one or more source IDs. |
| ids   array: string | A list of budget IDs or Schedule of Value (SOV) IDs from a contract, used as the source for copying sub cost items. To retrieve the relevant IDs, call [GET budgets](/en/docs/bim360/v1/reference/http/cost-budgets-GET/) or [GET contracts](/en/docs/bim360/v1/reference/http/cost-contracts-GET/). |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The sub cost items were successfully copied to the target type. |
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

| id   string: UUID | The unique ID of the sub cost item. |
| --- | --- |
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

The sub cost items were successfully copied to the target type.

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/cost-items/eb284d80-f026-11e7-98ee-cb31483cc0ac/sub-cost-items:copy' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "from": "estimated",
        "to": "proposed",
        "source": {
          "ids": [
            "f2D2ED17-C763-465B-8FAB-251C5A35D42F"
          ]
        }
      }'

```

Show More

### Response

```
[
  {
    "id": "8f127780-96d6-11e8-81a8-cd51c63a9484",
    "parentId": null,
    "type": "proposed",
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

```

Show More
