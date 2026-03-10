# v1/containers/{containerId}/payments

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-payments-GET/

---

Payments

GET

# v1/containers/{containerId}/payments

Retrieves payments in the given project based on the specified query criteria.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/payments |
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
| filter[associationType]   enum:string | Returns only the payments that are associated with the type of contract specified. Possible values:`Contract` for cost payments; `MainContract` for budget payments. For example, `filter[associationType]=Contract`. |
| filter[associationId]   array: string: uuid | Returns only the payments that are associated with the provided list of contract or main contract IDs. Separate multiple IDs with commas. For example, `filter[associationId]=id1,id2`. |
| filter[id]   array: string: uuid | Returns only the items that are identified by the provided list of item IDs. Separate multiple IDs with commas. For example, `filter[id]=id1,id2`. |
| filter[number]   array: string | Returns only the items that are identified by the provided list of auto-generated sequence numbers. Separate multiple numbers with commas; for example, `filter[number]=0001,0002`. |
| filter[status]   array: string | Returns only payments that have a status on the provided list of statuses. Separate multiple values with commas. For example, `filter[status]=draft,submitted`. Possible values:`draft`, `pendingInput`, `submitted`, `revise`, `inReview`, `accepted`, `paid`. |
| filter[budgetPaymentId]   array: string: uuid | Returns only the payments associated with the budget payments (used to query the related cost payments or expenses) that are identified on this list of IDs. Separate multiple IDs with commas; for example, `filter[budgetPaymentId]=id1,id2`. |
| filter[lastModifiedSince]   string | Returns only items that were modified since the specified date and time, in ISO 8601 format. For example, `filter[lastModifiedSince]=2020-03-01T13:00:00Z`. |
| filter[externalSystem]   string | The name of the external ERP system. Use this name to identify or search within the integrated system. For example, `filter[externalSystem]=Sage300`. <br>Max length: 255 |
| filter[externalId]   array: string | The ID of the item in the external ERP system. Use this ID to track or look up data in an integrated ERP system. For example, `filter[externalId]=id1,id2`. |
| include   array: string | Include nested resources in the response. For example, `include=paymentReferences` will return payment references to each payment. `include=attributes` will return custom attributes which represents the “properties” in the response. Possible values: `paymentReferences`, `attributes`, `summaryCalculatedFields`, `complianceExpiration`. |

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
| results   array: object | The project cost payments or budget payments. |
| id   string: UUID | The unique identifier of the payment. |
| billingPeriodId   string: UUID | Not relevant |
| previousPaymentId   string: UUID | The unique identifier of the previous payment for this payment. |
| associationType   enum:string | The type of contract associated with this payment. <br>Possible values: `Contract`, `MainContract`. |
| associationId   string: UUID | The ID of the contract or main contract that the payment is associated with. |
| mainContractId   string: UUID | The ID of the main contract associated with this payment. |
| budgetPaymentId   string,null | The ID of the budget payment associated with this cost payment. This field is valid only for cost payments. |
| budgetTransferIds   array: string | Not relevant |
| startDate   string | The start date of this payment. |
| endDate   string | The end date of this payment. |
| dueDate   string | The due date of this payment. |
| number   string | The number of this payment. <br>Max length: 255 |
| name   string | The name of this payment. <br>Max length: 1024 |
| description   string | A detailed description of this payment. |
| note   string | The note attached to the payment, if returned. The note consists of Tiptap formatted rich text. For more information, see [https://tiptap.dev](https://tiptap.dev/introduction/). |
| contactId   string,null | The ID of a contact managed by a BIM 360 Admin. |
| creatorId   string,null | The user who created the payment. This is the ID of a user managed by BIM 360 Admin. |
| status   enum:string | The status of this payment. For details about the possible values of this field, see [Payment Application Statuses](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Payment_Application_Statuses). <br>Possible values: `draft`, `pendingInput`, `submitted`, `revise`, `accepted`, `approved`, `paid`. |
| exchangeRate   number,string,null | Exchange rate. Default value is `1`. If multi-currency is not enabled, it will also be `1`. |
| previousExchangeRate   number,string,null | Exchange rate from previous payment application. Default value is `1`, if multi-currency is not enabled, it will also be `1`. |
| contractAmount   number,string,null | The original contract amount of the payment. |
| contractAmountForeignCurrency   number,string,null | The original contract amount of the payment, in foreign currency. |
| approvedChangeOrders   number,string,null | The amount of total approved change orders in this payment. |
| approvedChangeOrdersForeignCurrency   number,string,null | The amount of total approved change orders in this payment, in foreign currency. |
| approvedBudgetTransfers   number,string,null | Not relevant |
| approvedBudgetTransfersForeignCurrency   number,string,null | Not relevant |
| originalAmount   number,string,null | The original payment amount, including the main contract amount, change orders, and internal budget transfers that affect the schedule of values defined in project settings. |
| originalAmountForeignCurrency   number,string,null | The original payment amount in foreign currency, including the main contract amount, change orders, and internal budget transfers that affect the schedule of values defined in project settings. |
| previousAmount   number,string,null | The amount of total work completed prior to this period. |
| previousAmountForeignCurrency   number,string,null | The amount of total work completed prior to this period, in foreign currency. |
| previousApprovedChangeOrders   number,string,null | The amount of total approved change orders prior to this period. |
| previousApprovedChangeOrdersForeignCurrency   number,string,null | The amount of total approved change orders prior to this period, in foreign currency. |
| previousApprovedBudgetTransfers   number,string,null | Not relevant |
| previousApprovedBudgetTransfersForeignCurrency   number,string,null | Not relevant |
| amount   number,string,null | The amount of the work completed in this period. |
| previousMaterialsOnStore   number,string,null | The amount of total materials stored prior to this period. |
| materialsOnStore   number,string,null | The amount of the materials stored in this application. |
| previousMaterialsBilled   number,string,null | The amount of total materials billed prior to this period. |
| previousMaterialsBilledForeignCurrency   number,string,null | The amount of total materials billed prior to this period, in foreign currency. |
| materialsBilled   number,string,null | The amount of the materials billed in this period. |
| currentCompletedWorkRetentionPercent   number | Not relevant |
| completedWorkRetainedPercent   number | Not relevant |
| completedWorkRetained   number | Not relevant |
| completedWorkRetention   number,string,null | The amount of total work completed retained in this application. |
| completedWorkRetentionForeignCurrency   number,string,null | The amount of total work completed retained (pre-release), in foreign currency. |
| completedWorkGrossRetentionPercent   number | The percentage of the gross retention amount of the payment for work completed. (released value is not removed) |
| currentMaterialsRetentionPercent   number | Not relevant |
| materialsGrossRetentionPercent   number | The percentage of the gross retention of the payment for material (released value is not removed). |
| materialsRetainedPercent   number | Not relevant |
| materialsRetained   number,string,null | The amount of the materials (stored or billed) retained in this application. |
| materialsRetention   number,string,null | The amount of the materials (stored or billed) retained in this application. |
| materialsOnStoreRetention   number,string,null | The amount of the materials stored retained in this application. This parameter is deprecated. |
| materialsRetentionForeignCurrency   number,string,null | The amount of the materials (stored or billed) retained in this application, in foreign currency. |
| totalGrossRetentionPercent   number | The percentage of the gross retention of the payment for work completed and material. (released value is not removed) |
| totalRetainedPercent   number | Not relevant |
| totalRetained   number | Not relevant |
| previousRetention   number,string,null | The retained amount of total work completed and materials (stored or billed) prior to this period. |
| previousRetentionForeignCurrency   number,string,null | The retained amount of total work completed and materials (stored or billed) prior to this period, in foreign currency. |
| netAmount   number,string,null | The net amount that should be paid in this period, including work completed, advance amount, materials stored or billed, retention and release. |
| netAmountForeignCurrency   number,string,null | The net amount that should be paid in this period, including work completed, advance amount, materials stored or billed, retention and release, in foreign currency. |
| netMaterialsOnStore   number,string,null | The net materials stored in this period, which equals to (materialsOnStore - previousMaterialsOnStore). |
| netRetention   number,string,null | The net retention in this period, which equals to (completedWorkRetention + materialsOnStoreRetention - previousRetention). |
| previousClaimedAmount   number,string,null | The claimed amount of total work completed prior to this period. |
| previousClaimedAmountForeignCurrency   number,string,null | The claimed amount of total work completed prior to this period, in foreign currency. |
| claimedAmount   number,string,null | The claimed amount of total work completed in this period. |
| previousAdvanceAmount   number,string,null | The advance amount of total work completed prior to this period. |
| previousAdvanceAmountForeignCurrency   number,string,null | The advance amount of total work completed prior to this period, in foreign currency. |
| previousRecoupmentAmount   number,string,null | The recoupment amount of total work completed prior to this period. |
| previousRecoupmentAmountForeignCurrency   number,string,null | The recoupment amount of total work completed prior to this period, in foreign currency. |
| advancePercent   number,null | The advance percent of the work completed in this period. |
| advanceAmount   number,string,null | The advance amount of the work completed in this period. |
| recoupmentAmount   number,string,null | The recoupment amount of the work completed in this period. |
| recoupmentPercentOfCompletedWork   number,null | The recoupment percentage of the work completed in this period. |
| aggregateBy   string,null | Not relevant |
| canReleaseRetention   boolean | Not relevant |
| hasItemRejected   boolean | Indicate if this payment has item rejected. This parameter is deprecated. |
| hasItemReviewed   boolean | Indicate if this payment has item reviewed. This parameter is deprecated. |
| recipients   array: object | Persons that the generated documents will be sent to. |
| id   string | This is the ID of a user managed by BIM 360 Admin. |
| isDefault   boolean | True if this is the default recipient of a Contract or Change Order. |
| companyId   string,null | The ID of a company managed by a BIM 360 Admin. Detailed company information can be retrieved by calling [GET projects/:project_id/companies](http-projects--project_id-companies-GET.md) and locating the member_group_id in the response. |
| companyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](http-companies--company_id-GET.md) in the response. |
| architectCompanyId   string,null | The BIM360/ACC ID of the architecture firm. The detailed company information can be retrieved from [GET projects/:project_id/companies](http-projects--project_id-companies-GET.md) endpoint by searching the member_group_id in the response. |
| architectCompanyUid   string,null | The unique ID of the architecture firm. The detailed company information can be retrieved by this uuid from GET companies/:company_id <en/docs/bim360/v1/reference/http/companies-:company_id-GET/> in the response |
| architectContactId   string,null | The BIM360/ACC ID of the primary contact at the architecture firm. |
| additionalCollaborators   array: object | The additional collaborator company and contacts. |
| companyId   string | The BIM360/ACC ID of the firm. |
| companyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](http-companies--company_id-GET.md) in the response. |
| contactIds   array: string | The BIM360/ACC user ID of the contacts in the firm. |
| approvedAt   string,null | The date and time that the item was approved, in ISO 8601 format. |
| calculatedAt   string,null | The date and time that the item was calculated, in ISO 8601 format. |
| calculatedBy   string | The ID of the user who calculated the payment. |
| paidAt   string,null | The date and time when the expense is paid. |
| forecastDistributionAt   string,null | The date and time determine which distribution period this payment belongs to, after the status of `status` is set to `approved` or `paid`. |
| submittedAt   string,null | The date and time when the payment is submitted. |
| paymentStage   enum:string | Not relevant |
| internalId   string,null | Not relevant |
| internalSystem   string,null | Not relevant |
| integrationState   string,null | The state of the item during the integration with the external ERP system (such as SignNow). An item can be a `budget`, `contract`, `main contract`, `main contract item`, `cost item`, `expense`, `expense item`, `change order`, or `schedule of value`. For more details, see [Integrate with External System](../how-to-docs/cost-integrate-with-external-system.md) tutorial. Possible values: <br>`locked`: the item is currently locked within the ERP system, preventing modifications until unlocked. To unlock and modify the item, use the relevant PATCH endpoint to set `integrationState` to `null`. For example, for a budget, call [PATCH budgets](http-cost-budgets-budgetId-PATCH.md). For a contract, call [PATCH contracts](http-cost-contracts-contractId-PATCH.md). For more details, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Integrated_and_Locked).<br>`integrated`: the item has been successfully added to the ERP system.<br>`failed`: the item encountered an error during the integration process and was not successfully added to the ERP system. For example, if a user tries to integrate `contracts` from an ERP system and the updates fail, the `integrationState` can be set to `failed`. Retry the sync process or analyze the issue if it continues to fail.<br>`null`: The item has not been integrated with the ERP system. This is default value.<br>For more information regarding integrations within the Cost Management system, see [Integrations in Cost Management](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Integrations). |
| integrationStateChangedAt   string,null | The date and time that the item’s integration status was last changed. |
| integrationStateChangedBy   string,null | The user who last changed the integration status. This is the ID of a user managed by the BIM 360/ACC Admin. |
| externalId   string | The identifier assigned to an item in its original external ERP system. Use this ID to track and look up data within the integrated system. Note that this value comes from the item’s ID in the external system. <br>Max length: 255 |
| externalSystem   string | The name of the external ERP system integrated with Cost Management. Use this name to identify and search for data within the integrated system. <br>Max length: 255 |
| externalMessage   string | A message generated by the external ERP system that explains the sync status of the integration. For example, common values include `success` or `fail` to indicate the result of the integration operation. <br>Max length: 255 |
| lastSyncTime   datetime: ISO 8601 | The date and time when the item was last synchronized with the external ERP system. This value is updated by the external system and is in ISO 8601 format. |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/payments?limit=100&sort=name,createdAt desc&filter[associationType]=Contract&filter[status]=paid&filter[lastModifiedSince]=2020-03-01T13:00:00Z' \
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
      "billingPeriodId": "18d97ae0-9484-11e8-a7ec-7ddae203e404",
      "previousPaymentId": "18d97ae0-9484-11e8-a7ec-7ddae203e404",
      "associationType": "Contract",
      "associationId": "18d97ae0-9484-11e8-a7ec-7ddae203e404",
      "mainContractId": "18d97ae0-9484-11e8-a7ec-7ddae203e404",
      "budgetPaymentId": "18d97ae0-9484-11e8-a7ec-7ddae203e404",
      "budgetTransferIds": [
        "a2e16076-d5bb-44b3-b451-fb1fb390e4fc"
      ],
      "startDate": "2019-02-01",
      "endDate": "2019-02-28",
      "dueDate": "2019-02-28",
      "number": "09871000072000O",
      "name": "INSURANCE",
      "description": "Description of Payment",
      "note": "",
      "contactId": "CED9LVTLHNXV",
      "creatorId": "CED9LVTLHNXV",
      "status": "draft",
      "exchangeRate": "1.0000",
      "previousExchangeRate": "1.0000",
      "contractAmount": "1000.0000",
      "contractAmountForeignCurrency": "1000.0000",
      "approvedChangeOrders": "1000.0000",
      "approvedChangeOrdersForeignCurrency": "1000.0000",
      "approvedBudgetTransfers": "1000.0000",
      "approvedBudgetTransfersForeignCurrency": "1000.0000",
      "originalAmount": "1000.0000",
      "originalAmountForeignCurrency": "1000.0000",
      "previousAmount": "1000.0000",
      "previousAmountForeignCurrency": "1000.0000",
      "previousApprovedChangeOrders": "1000.0000",
      "previousApprovedChangeOrdersForeignCurrency": "1000.0000",
      "previousApprovedBudgetTransfers": "1000.0000",
      "previousApprovedBudgetTransfersForeignCurrency": "1000.0000",
      "amount": "1000.0000",
      "previousMaterialsOnStore": "1000.0000",
      "materialsOnStore": "1000.0000",
      "previousMaterialsBilled": "1000.0000",
      "previousMaterialsBilledForeignCurrency": "1000.0000",
      "materialsBilled": "1000.0000",
      "currentCompletedWorkRetentionPercent": 0.1,
      "completedWorkRetainedPercent": 0.1,
      "completedWorkRetained": "",
      "completedWorkRetention": "1000.0000",
      "completedWorkRetentionForeignCurrency": "1000.0000",
      "completedWorkGrossRetentionPercent": 0.1,
      "currentMaterialsRetentionPercent": 0.1,
      "materialsGrossRetentionPercent": 0.1,
      "materialsRetainedPercent": 0.1,
      "materialsRetained": "1000.0000",
      "materialsRetention": "1000.0000",
      "materialsOnStoreRetention": "1000.0000",
      "materialsRetentionForeignCurrency": "1000.0000",
      "totalGrossRetentionPercent": 0.1,
      "totalRetainedPercent": 0.1,
      "totalRetained": "",
      "previousRetention": "1000.0000",
      "previousRetentionForeignCurrency": "1000.0000",
      "netAmount": "1000.0000",
      "netAmountForeignCurrency": "1000.0000",
      "netMaterialsOnStore": "1000.0000",
      "netRetention": "1000.0000",
      "previousClaimedAmount": "1000.0000",
      "previousClaimedAmountForeignCurrency": "1000.0000",
      "claimedAmount": "1000.0000",
      "previousAdvanceAmount": "1000.0000",
      "previousAdvanceAmountForeignCurrency": "1000.0000",
      "previousRecoupmentAmount": "1000.0000",
      "previousRecoupmentAmountForeignCurrency": "1000.0000",
      "advancePercent": 0.1,
      "advanceAmount": "1000.0000",
      "recoupmentAmount": "1000.0000",
      "recoupmentPercentOfCompletedWork": 0.1,
      "aggregateBy": "workCompleted",
      "canReleaseRetention": false,
      "hasItemRejected": true,
      "hasItemReviewed": true,
      "recipients": [
        {
          "id": "ZPYARKZX9ANQ",
          "isDefault": false
        }
      ],
      "companyId": "GF8XKPKWM38E",
      "companyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
      "architectCompanyId": "GF8XKPKWM38E",
      "architectCompanyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
      "architectContactId": "CED9LVTLHNXV",
      "additionalCollaborators": [
        {
          "companyId": "GF8XKPKWM38E",
          "companyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
          "contactIds": [
            "CED9LVTLHNXV"
          ]
        }
      ],
      "approvedAt": "2019-02-05T01:00:12.989Z",
      "calculatedAt": "2019-02-05T01:00:12.989Z",
      "calculatedBy": "CED9LVTLHNXV",
      "paidAt": "2019-02-05T01:00:12.989Z",
      "forecastDistributionAt": "2019-02-05T01:00:12.989Z",
      "submittedAt": "2019-02-05T01:00:12.989Z",
      "paymentStage": "Progress",
      "internalId": "123",
      "internalSystem": "GCPay",
      "integrationState": "locked",
      "integrationStateChangedAt": "2019-09-05T01:00:12.989Z",
      "integrationStateChangedBy": "CED9LVTLHNXV",
      "externalId": "10010-99-AB",
      "externalSystem": "Sage300",
      "externalMessage": "Success.",
      "lastSyncTime": "2019-09-05T01:00:12.989Z",
      "createdAt": "2019-01-06T01:24:22.678Z",
      "updatedAt": "2019-09-05T01:00:12.989Z"
    }
  ]
}

```

Show More
