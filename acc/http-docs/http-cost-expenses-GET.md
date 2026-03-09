# v1/containers/{containerId}/expenses

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-expenses-GET/

---

Expenses

GET

# v1/containers/{containerId}/expenses

Retrieves the requested set of expenses in the specified project.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/expenses |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow.
- regionstring Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [ACC Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.To verify your projectâs region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](https://aps.autodesk.com/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page.

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](http-admin-accounts-accountidprojects-GET.md). |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| include   array: string | A list of the nested expense resources to include in the response with the expenses. For example, `include=expenseItems` returns the expense items related to each expense. `include=attributes` will return custom attributes which represents the âpropertiesâ in the response. <br>Possible values: `expenseItems`, `mainContract`, `attributes`, `externalRelationship`, `paymentReferences`. |
| --- | --- |
| filter[id]   array: string: uuid | Returns only the items that are identified by the provided list of item IDs. Separate multiple IDs with commas. For example, `filter[id]=id1,id2`. |
| filter[number]   array: string | Returns only the items that are identified by the provided list of auto-generated sequence numbers. Separate multiple numbers with commas; for example, `filter[number]=0001,0002`. |
| filter[status]   array: string | Returns only contracts with the specified statuses. Separate multiple values with commas. For example, `filter[status]=draft,pending`. Possible values:`draft`, `pending`, `submitted`, `revise`, `sent`, `signed`, `executed`, `closed`, `inReview`. |
| filter[mainContractId]   array: string: uuid | The Main Contract ID. Separate multiple IDs with commas. For example, `filter[mainContractId]=id1,id2`, or filter these items that are not linked to any main contract `filter[mainContractId]=blank`. |
| filter[budgetPaymentId]   array: string: uuid | Returns only the payments associated with the budget payments (used to query the related cost payments or expenses) that are identified on this list of IDs. Separate multiple IDs with commas; for example, `filter[budgetPaymentId]=id1,id2`. |
| filter[createdAt]   string | Filter data by its create date. This may be an ISO 8601 date string or a range. Ranges can be **lowerValue..upperValue**, **lowerValue..** or **..upperValue**. The range tests are always inclusive of their endpoints. |
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
| id   string | The unique identifier of the expense. |
| supplierId   string,null | The ID of a company managed by a BIM 360 Admin. Detailed company information can be retrieved by calling [GET projects/:project_id/companies](en/docs/bim360/v1/reference/http/projects-:project_id-companies-GET/) and locating the member_group_id in the response. |
| supplierCompanyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](en/docs/bim360/v1/reference/http/companies-:company_id-GET/) in the response. |
| supplierName   string,null | The supplier company name for the expense. Any company can be used regardless the ones added in Account Administration. <br>Max length: 255 |
| mainContractId   string | The ID of the Main Contract to which the expense belongs. |
| budgetPaymentId   string,null | The ID of the Budget Pay App the expense amount will be aggregated to. |
| number   string | The auto-generated sequence number for the expense. <br>Max length: 255 |
| name   string | The name of the expense. <br>Max length: 1024 |
| description   string | The detailed description of the expense. <br>Max length: 2048 |
| note   string | The note attached to the expense, if returned. The note consists of Tiptap formatted rich text. For more information, see [https://tiptap.dev](https://tiptap.dev/introduction/). |
| term   string | The term of the expense. This is customizable by the project administrator. |
| referenceNumber   string | The user-provided reference number of the expense. |
| type   string,null | The type of the expense. This is customizable by the project administrator. <br>Max length: 128 |
| scope   string,null | The applicable scope of the expense. Possible values: `full`, `partial`. |
| creatorId   string,null | The user who created the expense. This is the ID of a user managed by BIM 360 Admin. |
| changedBy   string,null | The user who made the last change to the expense. This is the ID of a user managed by BIM 360 Admin. |
| purchasedBy   string,null | The user who purchased the expense. This is the ID of a user managed by BIM 360 Admin. |
| status   string,null | The status of the expense. Possible values: `draft`, `pending`, `revise`, `rejected`, `approved`, `paid`. |
| amount   number,string,null | The total value of the subitems of the expense. |
| paymentDue   string,null | The payment due date and time of the expense. |
| issuedAt   string,null | The date and time when the expense was issued. |
| receivedAt   string,null | The date and time when the expense was received. |
| approvedAt   string,null | The date and time when the expense was approved. |
| paidAt   string,null | The date and time when the expense was paid. |
| forecastDistributionAt   string,null | The date and time determine which distribution period this expense belongs to, after the status of `status` is set to `approved` or `paid`. |
| aggregateBy   string,null | Not relevant |
| externalId   string | The identifier assigned to an item in its original external ERP system. Use this ID to track and look up data within the integrated system. Note that this value comes from the itemâs ID in the external system. <br>Max length: 255 |
| externalSystem   string | The name of the external ERP system integrated with Cost Management. Use this name to identify and search for data within the integrated system. <br>Max length: 255 |
| externalMessage   string | A message generated by the external ERP system that explains the sync status of the integration. For example, common values include `success` or `fail` to indicate the result of the integration operation. <br>Max length: 255 |
| lastSyncTime   datetime: ISO 8601 | The date and time when the item was last synchronized with the external ERP system. This value is updated by the external system and is in ISO 8601 format. |
| integrationState   string,null | The state of the item during the integration with the external ERP system (such as SignNow). An item can be a `budget`, `contract`, `main contract`, `main contract item`, `cost item`, `expense`, `expense item`, `change order`, or `schedule of value`. For more details, see [Integrate with External System](../how-to-docs/cost-integrate-with-external-system.md) tutorial. Possible values: <br>`locked`: the item is currently locked within the ERP system, preventing modifications until unlocked. To unlock and modify the item, use the relevant PATCH endpoint to set `integrationState` to `null`. For example, for a budget, call [PATCH budgets](en/docs/bim360/v1/reference/http/cost-budgets-budgetId-PATCH/). For a contract, call [PATCH contracts](en/docs/bim360/v1/reference/http/cost-contracts-contractId-PATCH/). For more details, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Integrated_and_Locked).<br>`integrated`: the item has been successfully added to the ERP system.<br>`failed`: the item encountered an error during the integration process and was not successfully added to the ERP system. For example, if a user tries to integrate `contracts` from an ERP system and the updates fail, the `integrationState` can be set to `failed`. Retry the sync process or analyze the issue if it continues to fail.<br>`null`: The item has not been integrated with the ERP system. This is default value.<br>For more information regarding integrations within the Cost Management system, see [Integrations in Cost Management](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Integrations). |
| integrationStateChangedAt   string,null | The date and time that the itemâs integration status was last changed. |
| integrationStateChangedBy   string,null | The user who last changed the integration status. This is the ID of a user managed by the BIM 360/ACC Admin. |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/expenses?filter[status]=open&filter[createdAt]=2020-10-31T14:48:00.000Z..2020-11-01T14:48:00.000Z&filter[lastModifiedSince]=2020-03-01T13:00:00Z&limit=100&sort=name,createdAt desc' \
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
      "id": "efcc4961-6115-4147-84c7-51b37be933c8",
      "supplierId": "GF8XKPKWM38E",
      "supplierCompanyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
      "supplierName": "Supply US",
      "mainContractId": "48934441-e392-49d7-bf58-8dea43d413ae",
      "budgetPaymentId": "ce4af4e1-d14c-4c9b-89fb-0d932306f093",
      "number": 1,
      "name": "Site Management Staff",
      "description": "Site Management Staff",
      "note": "Site Management Staff",
      "term": " Net 30",
      "referenceNumber": 20,
      "type": "expense",
      "scope": "full",
      "creatorId": "CED9LVTLHNXV",
      "changedBy": "CED9LVTLHNXV",
      "purchasedBy": "CED9LVTLHNXV",
      "status": "draft",
      "amount": "1000.0000",
      "paymentDue": "2019-05-05T01:00:12.989Z",
      "issuedAt": "2019-02-05T01:00:12.989Z",
      "receivedAt": "2019-02-05T01:00:12.989Z",
      "approvedAt": "2019-02-05T01:00:12.989Z",
      "paidAt": "2019-02-05T01:00:12.989Z",
      "forecastDistributionAt": "2019-02-05T01:00:12.989Z",
      "aggregateBy": "workCompleted",
      "externalId": "10010-99-AB",
      "externalSystem": "Sage300",
      "externalMessage": "Success.",
      "lastSyncTime": "2019-09-05T01:00:12.989Z",
      "integrationState": "locked",
      "integrationStateChangedAt": "2019-09-05T01:00:12.989Z",
      "integrationStateChangedBy": "CED9LVTLHNXV",
      "createdAt": "2019-01-06T01:24:22.678Z",
      "updatedAt": "2019-09-05T01:00:12.989Z"
    }
  ]
}

```

Show More
