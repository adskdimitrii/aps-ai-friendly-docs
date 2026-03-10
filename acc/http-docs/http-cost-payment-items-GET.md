# v1/containers/{containerId}/payment-items

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-payment-items-GET/

---

Payment Items

GET

# v1/containers/{containerId}/payment-items

Retrieves payment items in the given project based on `associationId` and `paymentId`.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/payment-items |
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

| filter[associationId]   array: string: uuid | Return only the payment items that are associated with the provided list of contract or main contract IDs. Separate multiple IDs with commas. For example, `filter[associationId]=id1,id2`. |
| --- | --- |
| filter[paymentId]   array: string: uuid | Return only the payment items that are associated with the payments identified by the provided list of payment IDs. Separate multiple IDs with commas. For example, `filter[id]=id1,id2`. |
| filter[associationType]   array: string | Return only the payment items that are associated with the type of original entities specified. For example, `filter[associationType]=SOV,SCO`. Possible values for cost payment: `SOV,SCO,CostItem,MaterialsOnSite`, and budget payments: `MainContractItem,OCO,CostItem,SubCostItem,MaterialsOnSite`. |
| offset   int | The number of records to skip before returning results. Used together with `limit` to paginate through results, where `offset` specifies the starting point and `limit` specifies the number of records to return. |
| limit   int | The maximum number of records returned per page. Default: `100`. A page may contain fewer records than the limit if there are fewer matching items or if it is the last page of results. |
| sort   string | Defines the sort order for the results. Each attribute can be sorted in `asc` (default) or `desc` order. For example, `sort=name desc` sorts the results by name in descending order. |

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
| results   array: object | The detail items in the payment. |
| id   string: UUID | Unique identifier of the payment. |
| paymentId   string: UUID | The ID of the payment the items belong to. |
| parentId   string: UUID | The ID of the parent item for sub items. |
| budgetId   string: UUID | The ID of the Budget to which the payment item belongs. |
| budgetCode   string | The budget code for the payment item (unformatted string). |
| budgetFormattedCode   string | The budget code for the payment item (formatted with separators). |
| associationType   enum:string | The object type of the payment item is generated from. Possible values: `SCO`, `OCO`, `SOV`, `CostItem`, `SubCostItem`, `MaterialsOnSite` |
| associationId   string: UUID | The ID of the object that the payment item is generated from. |
| name   string | The name of the payment item. <br>Max length: 1024 |
| description   string | A description of the payment item. |
| position   int | The position of the payment item in the payment item siblings. |
| exchangeRate   number,string,null | Exchange rate. Default value is `1`. If multi-currency is not enabled, it will also be `1`. |
| originalExchangeRate   number,string,null | If this payment item came from Schedule of Value, the value is equal to Schedule of Value exchange rate; If this payment item came from SCO, the value is equal to SCO exchange rate. Default value is `1`. If multi-currency is not enabled, it will also be `1`. |
| previousExchangeRate   number,string,null | Exchange rate from previous payment application. Default value is `1`, if multi-currency is not enabled, it will also be `1`. |
| originalQuantity   number | The original quantity of the payment item. Derived from the associated SOV or the main contract item. |
| originalUnitPrice   number,string,null | The original unit price of the payment item. Derived from the associated SOV or the main contract item. |
| originalAmount   number,string,null | The original amount of the payment item. Derived from the associated SOV or the main contract item. |
| budgetTransfersQuantity   number | Not relevant |
| budgetTransfersUnitPrice   number,string,null | Not relevant |
| budgetTransfers   number,string,null | Not relevant |
| previousQuantity   number | The quantity of total work completed prior to this period. |
| previousUnitPrice   number,string,null | The unit price of total work completed prior to this period. |
| previousAmount   number,string,null | The amount of total work completed prior to this period. |
| previousAmountForeignCurrency   number,string,null | The amount of total work completed prior to this period, in foreign currency. |
| previousMaterialsOnStore   number,string,null | The amount of total materials stored prior to this period. |
| previousMaterialsBilledQuantity   number | The quantity of total materials billed prior to this period. |
| previousMaterialsBilledUnitPrice   number,string,null | The unit price of total materials billed prior to this period. |
| previousMaterialsBilledUnit   string | The unit of total materials billed prior to this period. |
| previousMaterialsBilled   number,string,null | The amount of total materials billed prior to this period. |
| previousMaterialsBilledForeignCurrency   number,string,null | The amount of total materials billed prior to this period, in foreign currency. |
| previousMaterials   number,string,null | Not relevant |
| quantity   number | The quantity of the work completed in this period. |
| unitPrice   number,string,null | The unit price of the work completed in this period. |
| unit   string | The unit of the work completed in this period. |
| amount   number,string,null | The amount of the work completed in this period. |
| materialsBilledQuantity   number | The quantity of the materials billed in this period. |
| materialsBilledUnitPrice   number,string,null | The unit price of the materials billed in this period. |
| materialsBilledUnit   string | The unit of the materials billed in this period. |
| materialsBilled   number,string,null | The amount of the materials billed in this period. |
| materialsOnStoreQuantity   number | The quantity of the materials stored in this application. |
| materialsOnStoreUnitPrice   number,string,null | The unit price of the materials stored in this application. |
| materialsOnStoreUnit   string | The unit of the materials stored in this application. |
| materialsOnStore   number,string,null | The amount of the materials stored in this application. |
| materials   number,string,null | Not relevant |
| currentCompletedWorkRetentionPercent   number | Not relevant |
| currentCompletedWorkRetention   number,string,null | Not relevant |
| currentCompletedWorkRetentionForeignCurrency   number,string,null | Not relevant |
| previousCompletedWorkRetained   number,string,null | Not relevant |
| previousCompletedWorkRetainedForeignCurrency   number,string,null | Not relevant |
| completedWorkRetainedPercent   number | Not relevant |
| completedWorkRetained   number,string,null | Not relevant |
| completedWorkReleased   number,string,null | The retained amount of total work completed released in this period. |
| completedWorkRetentionPercent   number | The percentage of total work completed retained in this application. |
| completedWorkRetention   number,string,null | The amount of total work completed retained (pre-release) in this application. This parameter will be deprecated. |
| currentMaterialsRetentionPercent   number | Not relevant |
| currentMaterialsRetention   number,string,null | Not relevant |
| currentMaterialsRetentionForeignCurrency   number,string,null | Not relevant |
| previousMaterialsRetained   number,string,null | Not relevant |
| previousMaterialsRetainedForeignCurrency   number,string,null | Not relevant |
| materialsRetainedPercent   number | Not relevant |
| materialsRetained   number,string,null | The amount of the materials (stored or billed) retained in this application. |
| materialsReleased   number,string,null | The retained amount of the materials (stored or billed) released in this period. |
| materialsOnStoreReleased   number,string,null | The retained amount of the materials (stored or billed) released in this period. This parameter is deprecated, use materialsReleased. |
| materialsOnStoreRetentionPercent   number | The percentage of the materials retained. This parameter is deprecated, use materialsRetainedPercent. |
| materialsRetentionPercent   number | The percentage of the materials (stored or billed) retained (pre-release) in this application. This parameter will be deprecated, use materialsRetainedPercent. |
| materialsRetention   number,string,null | The amount of the materials (stored or billed) retained (pre-release) in this application. This parameter will be deprecated, use materialsRetained. |
| previousRetained   number,string,null | Not relevant |
| totalRetainedPercent   number | Not relevant |
| totalRetained   number | Not relevant |
| currentRetention   number,string,null | Not relevant |
| currentReleased   number,string,null | Not relevant |
| totalRetentionPercent   number | The percentage of total work completed and materials retained (pre-release). |
| retainage   number,string,null | Not relevant |
| previousNetAmount   number,string,null | Not relevant |
| netAmount   number,string,null | The net amount to be paid in this period, including work completed, materials stored or billed, retention and release. |
| netAmountForeignCurrency   number,string,null | The net amount to be paid in this period, in foreign currency. |
| realizedGainOrLoss   number,string,null | netAmountForeignCurrency / originalExchangeRate - netAmount |
| previousClaimedQuantity   number | The claimed quantity of total work completed prior to this period. |
| previousClaimedUnitPrice   number,string,null | The claimed unit price of the work completed prior to this period. |
| previousClaimedAmount   number,string,null | The claimed amount of the work completed prior to this period. |
| previousClaimedAmountForeignCurrency   number,string,null | The claimed amount of the work completed prior to this period, in foreign currency. |
| claimedQuantity   number,string,null | The claimed quantity of the work completed in this period. |
| claimedUnitPrice   number,string,null | The claimed unit price of the work completed in this period. |
| claimedAmount   number,string,null | The claimed amount of the work completed in this period. |
| previousAdvanceAmount   number,string,null | The advance amount of total work completed prior to this period. |
| previousAdvanceAmountForeignCurrency   number,string,null | The advance amount of total work completed prior to this period, in foreign currency. |
| advancePercent   number,null | The advance percent of the work completed in this period. |
| advanceAmount   number,string,null | The advance amount of the work completed in this period. |
| previousRecoupmentAmount   number,string,null | The recoupment amount of the work completed prior to this period. |
| previousRecoupmentAmountForeignCurrency   number,string,null | The recoupment amount of the work completed prior to this period, in foreign currency. |
| recoupmentAmount   number,string,null | The recoupment amount of the work completed in this period. |
| recoupmentPercentOfCompletedWork   number,null | The recoupment percentage of the work completed in this period. |
| creatorId   string,null | The user who created the payment item. This is the ID of a user managed by BIM 360 Admin. |
| changedBy   string,null | The user who made the change. |
| status   string,null | The review status the payment item. Possible values: `accepted`, `rejected`, `semi-rejected`, `null` |
| lastReviewedBy   string,null | The last user who made the review. |
| hasComment   boolean | Indicate if this payment item has comment. |
| canDelete   boolean | Indicate if this payment item can be deleted. |
| isPrivate   boolean,null | Indicate if this payment item should be exposed to owner. This is only for budget payment. |
| aggregateBy   string,null | The aggregate type to budget Payment application. Possible values: `workCompleted`, `workCompletedPercentage` |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |
| externalId   string | The identifier assigned to an item in its original external ERP system. Use this ID to track and look up data within the integrated system. Note that this value comes from the item’s ID in the external system. <br>Max length: 255 |
| externalSystem   string | The name of the external ERP system integrated with Cost Management. Use this name to identify and search for data within the integrated system. <br>Max length: 255 |
| externalMessage   string | A message generated by the external ERP system that explains the sync status of the integration. For example, common values include `success` or `fail` to indicate the result of the integration operation. <br>Max length: 255 |
| lastSyncTime   datetime: ISO 8601 | The date and time when the item was last synchronized with the external ERP system. This value is updated by the external system and is in ISO 8601 format. |
| integrationState   string,null | The state of the item during the integration with the external ERP system (such as SignNow). An item can be a `budget`, `contract`, `main contract`, `main contract item`, `cost item`, `expense`, `expense item`, `change order`, or `schedule of value`. For more details, see [Integrate with External System](../how-to-docs/cost-integrate-with-external-system.md) tutorial. Possible values: <br>`locked`: the item is currently locked within the ERP system, preventing modifications until unlocked. To unlock and modify the item, use the relevant PATCH endpoint to set `integrationState` to `null`. For example, for a budget, call [PATCH budgets](en/docs/bim360/v1/reference/http/cost-budgets-budgetId-PATCH/). For a contract, call [PATCH contracts](en/docs/bim360/v1/reference/http/cost-contracts-contractId-PATCH/). For more details, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Integrated_and_Locked).<br>`integrated`: the item has been successfully added to the ERP system.<br>`failed`: the item encountered an error during the integration process and was not successfully added to the ERP system. For example, if a user tries to integrate `contracts` from an ERP system and the updates fail, the `integrationState` can be set to `failed`. Retry the sync process or analyze the issue if it continues to fail.<br>`null`: The item has not been integrated with the ERP system. This is default value.<br>For more information regarding integrations within the Cost Management system, see [Integrations in Cost Management](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Integrations). |
| integrationStateChangedAt   string,null | The date and time that the item’s integration status was last changed. |
| integrationStateChangedBy   string,null | The user who last changed the integration status. This is the ID of a user managed by the BIM 360/ACC Admin. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/payment-items?limit=100&sort=name,createdAt desc' \
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
      "id": "a2e16076-d5bb-44b3-b451-fb1fb390e4fc",
      "paymentId": "18d97ae0-9484-11e8-a7ec-7ddae203e404",
      "parentId": "18d97ae0-9484-11e8-a7ec-7ddae203e404",
      "budgetId": "48934441-e392-49d7-bf58-8dea43d413ae",
      "budgetCode": "847200010330000SUB",
      "budgetFormattedCode": "8472-0001.03.30.00.0.SUB",
      "associationType": "Contract",
      "associationId": "18d97ae0-9484-11e8-a7ec-7ddae203e404",
      "name": "INSURANCE",
      "description": "The description of the payment item.",
      "position": 1,
      "exchangeRate": "1.0000",
      "originalExchangeRate": "1.0000",
      "previousExchangeRate": "1.0000",
      "originalQuantity": 100,
      "originalUnitPrice": "1000.0000",
      "originalAmount": "1000.0000",
      "budgetTransfersQuantity": 100,
      "budgetTransfersUnitPrice": "1000.0000",
      "budgetTransfers": "1000.0000",
      "previousQuantity": 2000,
      "previousUnitPrice": "1000.0000",
      "previousAmount": "1000.0000",
      "previousAmountForeignCurrency": "1000.0000",
      "previousMaterialsOnStore": "1000.0000",
      "previousMaterialsBilledQuantity": 100,
      "previousMaterialsBilledUnitPrice": "1000.0000",
      "previousMaterialsBilledUnit": "LS",
      "previousMaterialsBilled": "1000.0000",
      "previousMaterialsBilledForeignCurrency": "1000.0000",
      "previousMaterials": "1000.0000",
      "quantity": 100,
      "unitPrice": "1000.0000",
      "unit": "LS",
      "amount": "1000.0000",
      "materialsBilledQuantity": 100,
      "materialsBilledUnitPrice": "1000.0000",
      "materialsBilledUnit": "LS",
      "materialsBilled": "1000.0000",
      "materialsOnStoreQuantity": 100,
      "materialsOnStoreUnitPrice": "1000.0000",
      "materialsOnStoreUnit": "LS",
      "materialsOnStore": "1000.0000",
      "materials": "1000.0000",
      "currentCompletedWorkRetentionPercent": 0.3,
      "currentCompletedWorkRetention": "1000.0000",
      "currentCompletedWorkRetentionForeignCurrency": "1000.0000",
      "previousCompletedWorkRetained": "1000.0000",
      "previousCompletedWorkRetainedForeignCurrency": "1000.0000",
      "completedWorkRetainedPercent": 0.3,
      "completedWorkRetained": "1000.0000",
      "completedWorkReleased": "1000.0000",
      "completedWorkRetentionPercent": "0.3",
      "completedWorkRetention": "1000.0000",
      "currentMaterialsRetentionPercent": 0.1,
      "currentMaterialsRetention": "1000.0000",
      "currentMaterialsRetentionForeignCurrency": "1000.0000",
      "previousMaterialsRetained": "1000.0000",
      "previousMaterialsRetainedForeignCurrency": "1000.0000",
      "materialsRetainedPercent": 0.1,
      "materialsRetained": "1000.0000",
      "materialsReleased": "1000.0000",
      "materialsOnStoreReleased": "1000.0000",
      "materialsOnStoreRetentionPercent": "0.1",
      "materialsRetentionPercent": "0.1",
      "materialsRetention": "1000.0000",
      "previousRetained": "1000.0000",
      "totalRetainedPercent": 0.3,
      "totalRetained": "0.1",
      "currentRetention": "1000.0000",
      "currentReleased": "1000.0000",
      "totalRetentionPercent": "0.2",
      "retainage": "1000.0000",
      "previousNetAmount": "1000.0000",
      "netAmount": "1000.0000",
      "netAmountForeignCurrency": "1000.0000",
      "realizedGainOrLoss": "1000.0000",
      "previousClaimedQuantity": 100,
      "previousClaimedUnitPrice": "1000.0000",
      "previousClaimedAmount": "1000.0000",
      "previousClaimedAmountForeignCurrency": "1000.0000",
      "claimedQuantity": "1000.0000",
      "claimedUnitPrice": "1000.0000",
      "claimedAmount": "1000.0000",
      "previousAdvanceAmount": "1000.0000",
      "previousAdvanceAmountForeignCurrency": "1000.0000",
      "advancePercent": "",
      "advanceAmount": "1000.0000",
      "previousRecoupmentAmount": "1000.0000",
      "previousRecoupmentAmountForeignCurrency": "1000.0000",
      "recoupmentAmount": "1000.0000",
      "recoupmentPercentOfCompletedWork": "",
      "creatorId": "CED9LVTLHNXV",
      "changedBy": "CED9LVTLHNXV",
      "status": "rejected",
      "lastReviewedBy": "CED9LVTLHNXV",
      "hasComment": true,
      "canDelete": true,
      "isPrivate": false,
      "aggregateBy": "workCompleted",
      "createdAt": "2019-01-06T01:24:22.678Z",
      "updatedAt": "2019-09-05T01:00:12.989Z",
      "externalId": "10010-99-AB",
      "externalSystem": "Sage300",
      "externalMessage": "Success.",
      "lastSyncTime": "2019-09-05T01:00:12.989Z",
      "integrationState": "locked",
      "integrationStateChangedAt": "2019-09-05T01:00:12.989Z",
      "integrationStateChangedBy": "CED9LVTLHNXV"
    }
  ]
}

```

Show More
