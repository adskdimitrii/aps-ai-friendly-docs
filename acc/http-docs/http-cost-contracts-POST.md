# v1/containers/{containerId}/contracts

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-contracts-POST/

---

Contracts

POST

# v1/containers/{containerId}/contracts

Creates a contract in the specific project.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/cost/v1/containers/:containerId/contracts |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| region   string | Specifies the region where the project data resides. <br>By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.<br>Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [ACC Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.<br>To verify your project’s region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](https://aps.autodesk.com/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](http-admin-accounts-accountidprojects-GET.md). |
| --- | --- |

### Request

## [Body Structure](#body-structure)

The contract

Expand all

| code   string | The code of the contract. <br>Max length: 255 |
| --- | --- |
| name*   string | The name of the contract. <br>Max length: 1024 |
| description   string | The detailed description of a contract. <br>Max length: 2048 |
| companyId   string,null | The ID of a company managed by a BIM 360 Admin. Detailed company information can be retrieved by calling [GET projects/:project_id/companies](http-projects--project_id-companies-GET.md) and locating the member_group_id in the response. |
| companyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](http-companies--company_id-GET.md) in the response. |
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
| externalId   string | The identifier assigned to an item in its original external ERP system. Use this ID to track and look up data within the integrated system. Note that this value comes from the item’s ID in the external system. <br>Max length: 255 |
| externalSystem   string | The name of the external ERP system integrated with Cost Management. Use this name to identify and search for data within the integrated system. <br>Max length: 255 |
| externalMessage   string | A message generated by the external ERP system that explains the sync status of the integration. For example, common values include `success` or `fail` to indicate the result of the integration operation. <br>Max length: 255 |
| lastSyncTime   datetime: ISO 8601 | The date and time when the item was last synchronized with the external ERP system. This value is updated by the external system and is in ISO 8601 format. |
| integrationState   string,null | The state of the item during the integration with the external ERP system (such as SignNow). An item can be a `budget`, `contract`, `main contract`, `main contract item`, `cost item`, `expense`, `expense item`, `change order`, or `schedule of value`. For more details, see [Integrate with External System](../how-to-docs/cost-integrate-with-external-system.md) tutorial. Possible values: <br>`locked`: the item is currently locked within the ERP system, preventing modifications until unlocked. To unlock and modify the item, use the relevant PATCH endpoint to set `integrationState` to `null`. For example, for a budget, call [PATCH budgets](http-cost-budgets-budgetId-PATCH.md). For a contract, call [PATCH contracts](http-cost-contracts-contractId-PATCH.md). For more details, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Integrated_and_Locked).<br>`integrated`: the item has been successfully added to the ERP system.<br>`failed`: the item encountered an error during the integration process and was not successfully added to the ERP system. For example, if a user tries to integrate `contracts` from an ERP system and the updates fail, the `integrationState` can be set to `failed`. Retry the sync process or analyze the issue if it continues to fail.<br>`null`: The item has not been integrated with the ERP system. This is default value.<br>For more information regarding integrations within the Cost Management system, see [Integrations in Cost Management](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Integrations). |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Success |
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

## [Body Structure (201)](#body-structure-201)

Expand all

| code   string | The code of the contract. <br>Max length: 255 |
| --- | --- |
| name   string | The name of the contract. <br>Max length: 1024 |
| description   string | The detailed description of a contract. <br>Max length: 2048 |
| companyId   string,null | The ID of a company managed by a BIM 360 Admin. Detailed company information can be retrieved by calling [GET projects/:project_id/companies](http-projects--project_id-companies-GET.md) and locating the member_group_id in the response. |
| companyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](http-companies--company_id-GET.md) in the response. |
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
| companyERPId   string,null | Not relevant |
| companyTaxId   string,null | Not relevant |
| externalId   string | The identifier assigned to an item in its original external ERP system. Use this ID to track and look up data within the integrated system. Note that this value comes from the item’s ID in the external system. <br>Max length: 255 |
| externalSystem   string | The name of the external ERP system integrated with Cost Management. Use this name to identify and search for data within the integrated system. <br>Max length: 255 |
| externalMessage   string | A message generated by the external ERP system that explains the sync status of the integration. For example, common values include `success` or `fail` to indicate the result of the integration operation. <br>Max length: 255 |
| lastSyncTime   datetime: ISO 8601 | The date and time when the item was last synchronized with the external ERP system. This value is updated by the external system and is in ISO 8601 format. |
| integrationState   string,null | The state of the item during the integration with the external ERP system (such as SignNow). An item can be a `budget`, `contract`, `main contract`, `main contract item`, `cost item`, `expense`, `expense item`, `change order`, or `schedule of value`. For more details, see [Integrate with External System](../how-to-docs/cost-integrate-with-external-system.md) tutorial. Possible values: <br>`locked`: the item is currently locked within the ERP system, preventing modifications until unlocked. To unlock and modify the item, use the relevant PATCH endpoint to set `integrationState` to `null`. For example, for a budget, call [PATCH budgets](http-cost-budgets-budgetId-PATCH.md). For a contract, call [PATCH contracts](http-cost-contracts-contractId-PATCH.md). For more details, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Integrated_and_Locked).<br>`integrated`: the item has been successfully added to the ERP system.<br>`failed`: the item encountered an error during the integration process and was not successfully added to the ERP system. For example, if a user tries to integrate `contracts` from an ERP system and the updates fail, the `integrationState` can be set to `failed`. Retry the sync process or analyze the issue if it continues to fail.<br>`null`: The item has not been integrated with the ERP system. This is default value.<br>For more information regarding integrations within the Cost Management system, see [Integrations in Cost Management](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Integrations). |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/contracts' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
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
        "externalId": "10010-99-AB",
        "externalSystem": "Sage300",
        "externalMessage": "Success.",
        "lastSyncTime": "2019-09-05T01:00:12.989Z",
        "integrationState": "locked"
      }'

```

Show More

### Response

```
{
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
  "companyERPId": "GF8XKPKWM38E",
  "companyTaxId": "GF8XKPKWM38E",
  "externalId": "10010-99-AB",
  "externalSystem": "Sage300",
  "externalMessage": "Success.",
  "lastSyncTime": "2019-09-05T01:00:12.989Z",
  "integrationState": "locked"
}

```

Show More
