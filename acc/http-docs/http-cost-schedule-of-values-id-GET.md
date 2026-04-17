# v1/containers/{containerId}/schedule-of-values/{id}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-schedule-of-values-id-GET/

---

Schedule Of Values

GET

# v1/containers/{containerId}/schedule-of-values/{id}

Retrieves one schedule of values (SOV) item in the given project by ID..

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/schedule-of-values/:id |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context.
- regionstring Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [Forma Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.To verify your project’s region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](https://aps.autodesk.com/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page.

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](http-admin-accounts-accountidprojects-GET.md). |
| --- | --- |
| id   string | The unique ID of this SOV item. |

### Request

## [Query String Parameters](#query-string-parameters)

| include   array: string | Return the specified nested resources in the response. For example, `include=subitems` returns the project’s SOV items, `include=attributes` will return custom attributes which represents the “properties” in the response. Note that for a value of `idOnly`, the response includes only a list of SOV item IDs, and other `include` values are ignored. <br>Possible values: `subitems`, `attributes`, `idOnly`. |
| --- | --- |

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

| id   string: UUID | The unique ID of the schedule of values (SOV) item. |
| --- | --- |
| parentId   string,null | The ID of the SOV item’s parent item, the default value is `null`. For root SOV items, this value is `null`. |
| contractId   string | The ID of the contract to which the SOV item belongs. |
| budgetId   string,null | The ID of the budget to which the SOV item belongs. |
| code   string | The code of the SOV item. <br>Max length: 255 |
| name   string | The name of the SOV item. <br>Max length: 1024 |
| quantity   number | The quantity of the SOV item. |
| unitPrice   number | The unit price of the SOV item. |
| unit   string | The unit of measure of the SOV item. <br>Max length: 1024 |
| amount   number,string,null | The total price of the SOV item. |
| allocatedAmount   number,string,null | The amount of budget allocated to this contract. |
| quantityPerBulk   number | The quantity conversion ratio of the SOV item. |
| bulkUnitPrice   number | The unit price of the converted SOV item quantity. |
| bulk   number | The converted quantity of the SOV item. |
| associationId   string,null | The ID of a change order or cost item that this SOV item was originally created from. |
| associationType   string,null | The type of object from which the SOV item was created:a change order or a cost item. |
| exchangeRate   number,string,null | The exchange rate that applies to the SOV item’s base currency price. For example, provide the value `0.7455` for a foreign currency that’s worth `0.7455` of your base currency. |
| position   number | The position of the SOV item in the list of SOV items. |
| hasBudgetLinked   boolean | Not relevant |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |
| externalId   string | The identifier assigned to an item in its original external ERP system. Use this ID to track and look up data within the integrated system. Note that this value comes from the item’s ID in the external system. <br>Max length: 255 |
| externalSystem   string | The name of the external ERP system integrated with Cost Management. Use this name to identify and search for data within the integrated system. <br>Max length: 255 |
| externalMessage   string | A message generated by the external ERP system that explains the sync status of the integration. For example, common values include `success` or `fail` to indicate the result of the integration operation. <br>Max length: 255 |
| lastSyncTime   datetime: ISO 8601 | The date and time when the item was last synchronized with the external ERP system. This value is updated by the external system and is in ISO 8601 format. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/schedule-of-values/88dc0f70-9483-11e8-a7ec-7ddae203e404' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "88dc0f70-9483-11e8-a7ec-7ddae203e404",
  "parentId": "null",
  "contractId": "2256dc50-9481-11e8-87fb-215990a8aeb3",
  "budgetId": "f6445638-ca68-4e3c-9160-15864de6b818",
  "code": "03 30 01.1",
  "name": "Concrete to Pile Caps",
  "quantity": 50,
  "unitPrice": 20,
  "unit": "ea",
  "amount": "1000.0000",
  "allocatedAmount": "1000.0000",
  "quantityPerBulk": 50,
  "bulkUnitPrice": 20,
  "bulk": 50,
  "associationId": "88dc0f70-9483-11e8-a7ec-7ddae203e404",
  "associationType": "SCO",
  "exchangeRate": "1000.0000",
  "position": 1,
  "hasBudgetLinked": false,
  "createdAt": "2019-01-06T01:24:22.678Z",
  "updatedAt": "2019-09-05T01:00:12.989Z",
  "externalId": "10010-99-AB",
  "externalSystem": "Sage300",
  "externalMessage": "Success.",
  "lastSyncTime": "2019-09-05T01:00:12.989Z"
}

```

Show More
