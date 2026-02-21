# v1/containers/{containerId}/expenses/{expenseId}/items

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-expenses-expenseId-items-GET/

---

Expense Items

GET

# v1/containers/{containerId}/expenses/{expenseId}/items

Retrieves the expense items and subitems of the specified expenses for a given project.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/expenses/:expenseId/items |
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

- containerIdstring: UUID The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](/en/docs/bim360/v1/reference/http/admin-accounts-accountidprojects-GET/).
- expenseIdarray: string A list of the object IDs of the expenses whose items you want to retrieve, separated by commas. You can obtain these IDs from the response to the [POST expenses](/en/docs/bim360/v1/reference/http/cost-expenses-POST/) or [GET expenses](/en/docs/bim360/v1/reference/http/cost-expenses-GET/) endpoint.

### Request

## [Query String Parameters](#query-string-parameters)

| include   array: string | A list of the nested expense resources to include in the response with the expense items. For example, `include=budget` returns the IDs of budgets related to the expense items, `include=attributes` will return custom attributes which represents the âpropertiesâ in the response. <br>Possible values: `budget`, `contract`, `attributes`, `externalRelationship`. |
| --- | --- |
| filter[id]   array: string: uuid | Returns only the items that are identified by the provided list of item IDs. Separate multiple IDs with commas. For example, `filter[id]=id1,id2`. |
| filter[lastModifiedSince]   string | Returns only items that were modified since the specified date and time, in ISO 8601 format. For example, `filter[lastModifiedSince]=2020-03-01T13:00:00Z`. |
| offset   int | The number of records to skip before returning results. Used together with `limit` to paginate through results, where `offset` specifies the starting point and `limit` specifies the number of records to return. |
| limit   int | The maximum number of records returned per page. Default: `100`. A page may contain fewer records than the limit if there are fewer matching items or if it is the last page of results. |
| sort   string | Defines the sort order for the results. Each attribute can be sorted in `asc` (default) or `desc` order. For example, `sort=name desc` sorts the results by name in descending order. |
| filter[externalSystem]   string | The name of the external ERP system. Use this name to identify or search within the integrated system. For example, `filter[externalSystem]=Sage300`. <br>Max length: 255 |
| filter[externalId]   array: string | The ID of the item in the external ERP system. Use this ID to track or look up data in an integrated ERP system. For example, `filter[externalId]=id1,id2`. |

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
| results   array: object |  |
| id   string: UUID | The unique identifier of the expense item. |
| budgetId   string,null | The ID of the budget to which the expense item belongs. |
| contractId   string: UUID | The ID of the contract to which the expense item belongs. |
| number   string | The sequence number for the expense item. |
| name   string | The name of the expense item. <br>Max length: 1024 |
| description   string | The detailed description of the expense item. <br>Max length: 2048 |
| note   string | The note attached to the expense item, if returned. The note consists of Tiptap formatted rich text. For more information, see [https://tiptap.dev](https://tiptap.dev/introduction/). |
| scope   string,null | The applicable scope of the expense item. Possible values: `full`, `partial`. |
| quantity   number | The number of units of the expense item. |
| unitPrice   number,string,null | The price per unit of the expense item. |
| unit   string | The expense itemâs unit of measure. |
| amount   number,string,null | The total price of the expense item. |
| aggregateBy   string,null | The aggregate type of the expense item. Possible values: `workCompleted`, `workCompletedQty`, `materialsOnSite` |
| exchangeRate   number,string,null | The exchange rate that applies to the expense itemâs base currency price. For example, provide the value `0.7455` for a foreign currency thatâs worth `0.7455` of your base currency. Default:`1`. Itâs also `1` if multi-currency is not enabled. |
| originalExchangeRate   number,string,null | The original exchange rate from the expense itemâs associated contract. Default:`1`. Itâs also `1` if multi-currency is not enabled. |
| realizedGainOrLoss   number,string,null | The gain or loss on the expense item, calculated as follows:`amount * exchangeRate / originalExchangeRate - amount` |
| externalId   string | The identifier assigned to an item in its original external ERP system. Use this ID to track and look up data within the integrated system. Note that this value comes from the itemâs ID in the external system. <br>Max length: 255 |
| externalSystem   string | The name of the external ERP system integrated with Cost Management. Use this name to identify and search for data within the integrated system. <br>Max length: 255 |
| externalMessage   string | A message generated by the external ERP system that explains the sync status of the integration. For example, common values include `success` or `fail` to indicate the result of the integration operation. <br>Max length: 255 |
| lastSyncTime   datetime: ISO 8601 | The date and time when the item was last synchronized with the external ERP system. This value is updated by the external system and is in ISO 8601 format. |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |
| integrationState   string,null | The state of the item during the integration with the external ERP system (such as SignNow). An item can be a `budget`, `contract`, `main contract`, `main contract item`, `cost item`, `expense`, `expense item`, `change order`, or `schedule of value`. For more details, see [Integrate with External System](/en/docs/acc/v1/tutorials/cost/integrate-with-external-system/) tutorial. Possible values: <br>`locked`: the item is currently locked within the ERP system, preventing modifications until unlocked. To unlock and modify the item, use the relevant PATCH endpoint to set `integrationState` to `null`. For example, for a budget, call [PATCH budgets](en/docs/bim360/v1/reference/http/cost-budgets-budgetId-PATCH/). For a contract, call [PATCH contracts](en/docs/bim360/v1/reference/http/cost-contracts-contractId-PATCH/). For more details, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Integrated_and_Locked).<br>`integrated`: the item has been successfully added to the ERP system.<br>`failed`: the item encountered an error during the integration process and was not successfully added to the ERP system. For example, if a user tries to integrate `contracts` from an ERP system and the updates fail, the `integrationState` can be set to `failed`. Retry the sync process or analyze the issue if it continues to fail.<br>`null`: The item has not been integrated with the ERP system. This is default value.<br>For more information regarding integrations within the Cost Management system, see [Integrations in Cost Management](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Integrations). |
| integrationStateChangedAt   string,null | The date and time that the itemâs integration status was last changed. |
| integrationStateChangedBy   string,null | The user who last changed the integration status. This is the ID of a user managed by the BIM 360/ACC Admin. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/expenses/:expenseId/items?filter[lastModifiedSince]=2020-03-01T13:00:00Z&limit=100&sort=name,createdAt desc' \
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
      "id": "48934441-e392-49d7-bf58-8dea43d413ae",
      "budgetId": "48934441-e392-49d7-bf58-8dea43d413ae",
      "contractId": "48934441-e392-49d7-bf58-8dea43d413ae",
      "number": 1,
      "name": "Site Management Staff",
      "description": "Site Management Staff",
      "note": "Site Management Staff",
      "scope": "full",
      "quantity": "The quantity of the expense item. For example 1.",
      "unitPrice": "1000.0000",
      "unit": "ls",
      "amount": "1000.0000",
      "aggregateBy": "workCompleted",
      "exchangeRate": "1.0000",
      "originalExchangeRate": "1.0000",
      "realizedGainOrLoss": "1000.0000",
      "externalId": "10010-99-AB",
      "externalSystem": "Sage300",
      "externalMessage": "Success.",
      "lastSyncTime": "2019-09-05T01:00:12.989Z",
      "createdAt": "2019-01-06T01:24:22.678Z",
      "updatedAt": "2019-09-05T01:00:12.989Z",
      "integrationState": "locked",
      "integrationStateChangedAt": "2019-09-05T01:00:12.989Z",
      "integrationStateChangedBy": "CED9LVTLHNXV"
    }
  ]
}

```

Show More
