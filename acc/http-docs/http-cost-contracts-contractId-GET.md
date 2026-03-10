# v1/containers/{containerId}/contracts/{contractId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-contracts-contractId-GET/

---

Contracts

GET

# v1/containers/{containerId}/contracts/{contractId}

Retrieves the contract specified by contract ID.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/contracts/:contractId |
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
| contractId   string: UUID | The contract ID. |

### Request

## [Query String Parameters](#query-string-parameters)

| include   array: string | A list of resources related to the contract to include in the response. For example, `include=budgets` returns budgets related to the contract. Possible values: `budgets`, `scheduleOfValues`, `compounded`, `companyERPId`, `companyTaxId`. |
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

Expand all

| id   string: UUID | The unique identifier of a contract. |
| --- | --- |
| code   string | The code of the contract. <br>Max length: 255 |
| name   string | The name of the contract. <br>Max length: 1024 |
| description   string | The detailed description of a contract. <br>Max length: 2048 |
| companyId   string,null | The ID of a company managed by a BIM 360 Admin. Detailed company information can be retrieved by calling [GET projects/:project_id/companies](en/docs/bim360/v1/reference/http/projects-:project_id-companies-GET/) and locating the member_group_id in the response. |
| companyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](en/docs/bim360/v1/reference/http/companies-:company_id-GET/) in the response. |
| type   string,null | The type of contract. For example, `consultant` or `purchase order`. The `type` can be customized by the project admin. |
| contactId   string,null | The unique identifier of the default contact for the supplier. This ID is generated and managed by the BIM 360 Admin service. The `contactId` can be used to query user information such as `email` and `company`. |
| recipients   array: object | Not relevant |
| id   string | Not relevant |
| isDefault   boolean | Not relevant |
| source   string,null | The URN of the source entity from which the contract is created. |
| additionalContacts   object | Not relevant |
| sovContactId   string,null | Not relevant |
| signatoryId   string,null | Not relevant |
| rfqRecipientId   string,null,array | Not relevant |
| scoSignatoryId   string,null | Not relevant |
| costPaymentApplicationContactId   string,null | Not relevant |
| signedBy   string,null | The user who signed the contract. This is the ID of a user managed by BIM 360 Admin. |
| ownerId   string,null | The user responsible for the purchase. This is the ID of a user managed by BIM 360 Admin. |
| mainContractId   string,null | The ID of the main contract with which this item is associated. |
| completedWorkRetentionPercent   number,null | The completed work retention percentage of the contract amount. |
| materialsRetentionPercent   number,null | The materials retention percentage of the contract amount. |
| retentionCap   number,null | The maximum percentage of the total contract amount which can be used as the retention amount. |
| status   string,null | The status of this contract. Possible values: `draft`, `pending`, `submitted`, `revise`, `sent`, `signed`, `executed`, `closed`, `inReview` |
| subStatus   string,null | The subStatus is used when the contract is in an `executed` state and may have additional statuses under it. For example, if a contract is “executed” but requires the supplier to provide additional information, the status will be executed and the subStatus will be pending. In other cases, subStatus is always `null`. Possible values: `null`, `pending`, `submitted`, `revise`. Default value: `null`. |
| currency   string | The code of the currency specified for the contract if it’s awarded in a foreign currency. |
| exchangeRate   number,string,null | The final exchange rate for the specified `currency`, applied as a multiplier of the contract’s base currency. For example, 1 base currency = 0.7455 foreign currency. |
| forecastExchangeRate   number,string,null | The forecast exchange rate. Default value: `null`. |
| forecastExchangeRateUpdatedAt   datetime: ISO 8601 | The last time that the forecast exchange rate was updated, in ISO 8601 format. |
| awardedAt   string,null | The date and time of the contract award, in ISO 8601 format. |
| statusChangedAt   datetime: ISO 8601 | The date and time of the last status change, in ISO 8601 format. |
| sentAt   string,null | The date and time of contract transmission to the supplier, in ISO 8601 format. |
| respondedAt   string,null | The date and time of the supplier’s response, in ISO 8601 format. |
| responseDue   string,null | The date and time by which the supplier response is due, in ISO 8601 format. |
| returnedAt   string,null | The date and time of the signed contract return, in ISO 8601 format. |
| onsiteAt   string,null | The date and time of the supplier’s arrival on-site, in ISO 8601 format. |
| offsiteAt   string,null | The date and time of job completion by the supplier, in ISO 8601 format. |
| procuredAt   string,null | The date and time of purchase, in ISO 8601 format. This is designed for Purchase Order contracts. |
| approvedAt   string,null | The date and time of contract approval, in ISO 8601 format. |
| executedAt   string,null | The date and time of contract execution, in ISO 8601 format. |
| internalId   string,null | Not relevant |
| internalSystem   string,null | Not relevant |
| changedBy   string | The user who made the last change to the contract. This is the ID of a user managed by BIM 360 Admin. |
| creatorId   string | The user who created the contract. This is the ID of a user managed by BIM 360 Admin. |
| awarded   number | Amount of the original Contract |
| originalBudget   number | The total amount of original amount of budgets associated to this Contract. |
| internalAdjustment   number | The total amount of internal transfers of budgets associated to this Contract. |
| approvedOwnerChanges   number | The total amount of the changes approved by the owner. |
| pendingOwnerChanges   number | The total amount of the changes pending approval by the owner. |
| approvedChangeOrders   number | The total amount of the changes committed to the supplier. |
| approvedInScopeChangeOrders   number | The total amount of in-scope changes committed to the supplier. |
| pendingChangeOrders   number | The total amount of the changes not committed to the supplier. |
| reserves   number | The total amount of the changes under estimating. |
| actualCost   number | The total amount of actual cost of the contract. |
| uncommitted   number | The amount that has been approved by owner but not committed to the supplier. This is calculated as `approvedOwnerChanges` - (`approvedChangeOrders` - `approvedInScopeChangeOrders`). |
| revised   number | The total amount of the approved budget from the owner, equals to `originalAmount` + `internalAdjustment` + `approvedOwnerChanges`. |
| projectedCost   number | The total amount of the project cost. For a budget, it is equal to `originalCommitment` + `approvedChangeOrders` + `pendingChangeOrders` + `reserves`. For a contract , it is equal to `awarded` + `approvedChangeOrders` + `pendingChangeOrders` + `reserves`. |
| projectedBudget   number | The total amount of the project budget including pending changes, equals to `revised` + `pendingOwnerChanges`. |
| forecastFinalCost   number | The total amount of the project cost including forecast adjustments, equals to `projectedCost` + `adjustmentsTotal`. |
| forecastVariance   number | The total amount of the forecast variance, equals to `projectedBudget` - `forecastFinalCost`. |
| forecastCostComplete   number | The total amount of the forecast cost to complete, equals to `forecastFinalCost` - `actualCost`. |
| varianceTotal   number | The total amount of the variance of a budget, equals to `projectedBudget` - `projectedCost`. |
| documentGeneratedAt   datetime: ISO 8601 | The date and time when the contract document was generated, in ISO 8601 format. |
| scopeOfWork   string | Scope of work agreed upon and signed by all parties of the contract. This is a Tiptap formatted rich text (<https://tiptap.dev/introduction/>). |
| note   string | A note related to the contract. This is a Tiptap formatted rich text (<https://tiptap.dev/introduction/>) |
| compounded   object | The calculated values based on the contract’s customized columns. |
| paymentDue   int | Not relevant |
| paymentDueType   string,null | Not relevant |
| budgetIds   array: string | Not relevant |
| budgets   array: object | Budgets that are linked to this contract. |
| id   string: UUID | The ID of the budget linked to the contract. |
| mainContractId   string: UUID | Not relevant |
| scheduleOfValues   array: object | The schedule of values for the contract. |
| id   string: UUID | The unique ID of the schedule of values (SOV) item. |
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
| companyName   string | Not relevant |
| lockState   string | Not relevant |
| lockedBy   string | Not relevant |
| lockedAt   datetime: ISO 8601 | Not relevant |
| externalId   string | The identifier assigned to an item in its original external ERP system. Use this ID to track and look up data within the integrated system. Note that this value comes from the item’s ID in the external system. <br>Max length: 255 |
| externalSystem   string | The name of the external ERP system integrated with Cost Management. Use this name to identify and search for data within the integrated system. <br>Max length: 255 |
| externalMessage   string | A message generated by the external ERP system that explains the sync status of the integration. For example, common values include `success` or `fail` to indicate the result of the integration operation. <br>Max length: 255 |
| lastSyncTime   datetime: ISO 8601 | The date and time when the item was last synchronized with the external ERP system. This value is updated by the external system and is in ISO 8601 format. |
| integrationState   string,null | The state of the item during the integration with the external ERP system (such as SignNow). An item can be a `budget`, `contract`, `main contract`, `main contract item`, `cost item`, `expense`, `expense item`, `change order`, or `schedule of value`. For more details, see [Integrate with External System](../how-to-docs/cost-integrate-with-external-system.md) tutorial. Possible values: <br>`locked`: the item is currently locked within the ERP system, preventing modifications until unlocked. To unlock and modify the item, use the relevant PATCH endpoint to set `integrationState` to `null`. For example, for a budget, call [PATCH budgets](en/docs/bim360/v1/reference/http/cost-budgets-budgetId-PATCH/). For a contract, call [PATCH contracts](en/docs/bim360/v1/reference/http/cost-contracts-contractId-PATCH/). For more details, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Integrated_and_Locked).<br>`integrated`: the item has been successfully added to the ERP system.<br>`failed`: the item encountered an error during the integration process and was not successfully added to the ERP system. For example, if a user tries to integrate `contracts` from an ERP system and the updates fail, the `integrationState` can be set to `failed`. Retry the sync process or analyze the issue if it continues to fail.<br>`null`: The item has not been integrated with the ERP system. This is default value.<br>For more information regarding integrations within the Cost Management system, see [Integrations in Cost Management](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Integrations). |
| integrationStateChangedAt   string,null | The date and time that the item’s integration status was last changed. |
| integrationStateChangedBy   string,null | The user who last changed the integration status. This is the ID of a user managed by the BIM 360/ACC Admin. |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |
| companyERPId   string,null | Not relevant |
| companyTaxId   string,null | Not relevant |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/contracts/97363960-9483-11e8-a7ec-7ddae203e404' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "97363960-9483-11e8-a7ec-7ddae203e404",
  "code": "GC-01",
  "name": "Site Management Staff",
  "description": "Site Management Staff",
  "companyId": "GF8XKPKWM38E",
  "companyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
  "type": "consultant",
  "contactId": "CED9LVTLHNXV",
  "recipients": [
    {
      "id": "ZPYARKZX9ANQ",
      "isDefault": false
    }
  ],
  "source": "urn:adsk.service-name:us.prd:customer:1234",
  "additionalContacts": {
    "sovContactId": "CED9LVTLHNXV",
    "signatoryId": "CED9LVTLHNXV",
    "rfqRecipientId": "CED9LVTLHNXV",
    "scoSignatoryId": "CED9LVTLHNXV",
    "costPaymentApplicationContactId": "CED9LVTLHNXV"
  },
  "signedBy": "CED9LVTLHNXV",
  "ownerId": "CED9LVTLHNXV",
  "mainContractId": "",
  "completedWorkRetentionPercent": "50",
  "materialsRetentionPercent": "50",
  "retentionCap": "50",
  "status": "open",
  "subStatus": "open",
  "currency": "USD",
  "exchangeRate": "1000.0000",
  "forecastExchangeRate": "1000.0000",
  "forecastExchangeRateUpdatedAt": "2019-09-06T01:24:22.678Z",
  "awardedAt": "2019-09-04T01:45:24.582Z",
  "statusChangedAt": "2019-09-04T01:45:24.582Z",
  "sentAt": "2019-09-04T01:45:24.582Z",
  "respondedAt": "2019-09-04T01:45:24.582Z",
  "responseDue": "2019-09-04T01:45:24.582Z",
  "returnedAt": "2019-09-04T01:45:24.582Z",
  "onsiteAt": "2019-09-04T01:45:24.582Z",
  "offsiteAt": "2019-09-04T01:45:24.582Z",
  "procuredAt": "2019-09-04T01:45:24.582Z",
  "approvedAt": "2019-09-04T01:45:24.582Z",
  "executedAt": "2019-09-04T01:45:24.582Z",
  "internalId": "123",
  "internalSystem": "GCPay",
  "changedBy": "CED9LVTLHNXV",
  "creatorId": "CED9LVTLHNXV",
  "awarded": 1000,
  "originalBudget": 1000,
  "internalAdjustment": 1000,
  "approvedOwnerChanges": 1000,
  "pendingOwnerChanges": 1000,
  "approvedChangeOrders": 1000,
  "approvedInScopeChangeOrders": 1000,
  "pendingChangeOrders": 1000,
  "reserves": 1000,
  "actualCost": 1000,
  "uncommitted": 1000,
  "revised": 1000,
  "projectedCost": 1000,
  "projectedBudget": 1000,
  "forecastFinalCost": 1000,
  "forecastVariance": 1000,
  "forecastCostComplete": 1000,
  "varianceTotal": 1000,
  "documentGeneratedAt": "2019-09-04T01:45:24.582Z",
  "scopeOfWork": "",
  "note": "",
  "compounded": {},
  "paymentDue": 10,
  "paymentDueType": "afterStart",
  "budgetIds": [
    "48934441-e392-49d7-bf58-8dea43d413ae"
  ],
  "budgets": [
    {
      "id": "f6445638-ca68-4e3c-9160-15864de6b818",
      "mainContractId": "f6445638-ca68-4e3c-9160-15864de6b819"
    }
  ],
  "scheduleOfValues": [
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
  ],
  "companyName": "Autodesk",
  "lockState": "LOCKED",
  "lockedBy": "CED9LVTLHNXV",
  "lockedAt": "2019-09-04T01:45:24.582Z",
  "externalId": "10010-99-AB",
  "externalSystem": "Sage300",
  "externalMessage": "Success.",
  "lastSyncTime": "2019-09-05T01:00:12.989Z",
  "integrationState": "locked",
  "integrationStateChangedAt": "2019-09-05T01:00:12.989Z",
  "integrationStateChangedBy": "CED9LVTLHNXV",
  "createdAt": "2019-01-06T01:24:22.678Z",
  "updatedAt": "2019-09-05T01:00:12.989Z",
  "companyERPId": "GF8XKPKWM38E",
  "companyTaxId": "GF8XKPKWM38E"
}

```

Show More
