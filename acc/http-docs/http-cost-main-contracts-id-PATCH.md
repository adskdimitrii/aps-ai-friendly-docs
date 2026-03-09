# v1/containers/{containerId}/main-contracts/{id}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-main-contracts-id-PATCH/

---

Main Contracts

PATCH

# v1/containers/{containerId}/main-contracts/{id}

Updates a main contract in the given project.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/cost/v1/containers/:containerId/main-contracts/:id |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| region   string | Specifies the region where the project data resides. <br>By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.<br>Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [ACC Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.<br>To verify your projectâs region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](https://aps.autodesk.com/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

- containerIdstring: UUID The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](http-admin-accounts-accountidprojects-GET.md).
- idstring: UUID The object ID of the main contract. You can obtain this ID from the response to the [POST mainContract](http-cost-main-contracts-POST.md) or [GET mainContract](http-cost-main-contracts-GET.md) endpoint.

### Request

## [Body Structure](#body-structure)

The main contract

Expand all

| code   string | The code of the main contract. <br>Max length: 255 |
| --- | --- |
| name   string | The name of the main contract. <br>Max length: 1024 |
| description   string | Detailed description of a main contract. <br>Max length: 2048 |
| note   string | A note about the main contract in [Tiptap](https://tiptap.dev/introduction/)-formatted rich text. |
| scopeOfWork   string | The scope of work signed by all parties to the main contract, in [Tiptap](https://tiptap.dev/introduction/)-formatted rich text. |
| type   string,null | The type of the main contract. For example, `Fixed Price` or `Unit Price`. This is customizable for the project administrator. |
| contactId   string,null | The BIM360/ACC ID of the supplierâs default contact. |
| ownerCompanyId   string,null | The BIM360/ACC ID of the owner company. |
| ownerContactId   string,null | The BIM360/ACC ID of the primary contact at the owner company. |
| architectCompanyId   string,null | The BIM360/ACC ID of the architecture firm. |
| architectContactId   string,null | The BIM360/ACC ID of the primary contact at the architecture firm. |
| additionalCollaborators   array: object | The additional collaborator company and contacts. |
| companyId*   string | The BIM360/ACC ID of the firm. |
| companyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](en/docs/bim360/v1/reference/http/companies-:company_id-GET/) in the response. |
| contactIds   array: string | The BIM360/ACC user ID of the contacts in the firm. |
| ownerCompanyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](en/docs/bim360/v1/reference/http/companies-:company_id-GET/) in the response. |
| contractorCompanyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](en/docs/bim360/v1/reference/http/companies-:company_id-GET/) in the response. |
| architectCompanyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](en/docs/bim360/v1/reference/http/companies-:company_id-GET/) in the response. |
| notaryCompanyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](en/docs/bim360/v1/reference/http/companies-:company_id-GET/) in the response. |
| startDate   string,null | The start date of the main contract. |
| executedDate   string,null | The execution date of the main contract. |
| plannedCompletionDate   string,null | The planned completion date of the main contract. |
| revisedCompletionDate   string,null | The revised completion date of the main contract. |
| actualCompletionDate   string,null | The actual completion date of the main contract. |
| closeDate   string,null | The closing date of the main contract. |
| status   string | The status of the main contract. Possible values: `closed`, `executed`, `review`, `signed`. |
| isDefault   boolean,null | `true`: This is the default main contract. `false`: This is not the default main contract. |
| completedWorkRetentionPercent   number,null | The completed work retention percentage of the main contract amount. |
| materialsRetentionPercent   number,null | The materials retention percentage of the main contract amount. |
| retentionCap   number,null | Total retention percentage of the main contract amount. |
| externalId   string | The identifier assigned to an item in its original external ERP system. Use this ID to track and look up data within the integrated system. Note that this value comes from the itemâs ID in the external system. <br>Max length: 255 |
| externalSystem   string | The name of the external ERP system integrated with Cost Management. Use this name to identify and search for data within the integrated system. <br>Max length: 255 |
| externalMessage   string | A message generated by the external ERP system that explains the sync status of the integration. For example, common values include `success` or `fail` to indicate the result of the integration operation. <br>Max length: 255 |
| lastSyncTime   datetime: ISO 8601 | The date and time when the item was last synchronized with the external ERP system. This value is updated by the external system and is in ISO 8601 format. |
| integrationState   string,null | The state of the item during the integration with the external ERP system (such as SignNow). An item can be a `budget`, `contract`, `main contract`, `main contract item`, `cost item`, `expense`, `expense item`, `change order`, or `schedule of value`. For more details, see [Integrate with External System](../how-to-docs/cost-integrate-with-external-system.md) tutorial. Possible values: <br>`locked`: the item is currently locked within the ERP system, preventing modifications until unlocked. To unlock and modify the item, use the relevant PATCH endpoint to set `integrationState` to `null`. For example, for a budget, call [PATCH budgets](en/docs/bim360/v1/reference/http/cost-budgets-budgetId-PATCH/). For a contract, call [PATCH contracts](en/docs/bim360/v1/reference/http/cost-contracts-contractId-PATCH/). For more details, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Integrated_and_Locked).<br>`integrated`: the item has been successfully added to the ERP system.<br>`failed`: the item encountered an error during the integration process and was not successfully added to the ERP system. For example, if a user tries to integrate `contracts` from an ERP system and the updates fail, the `integrationState` can be set to `failed`. Retry the sync process or analyze the issue if it continues to fail.<br>`null`: The item has not been integrated with the ERP system. This is default value.<br>For more information regarding integrations within the Cost Management system, see [Integrations in Cost Management](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Integrations). |

* Required

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

| id   string | The unique ID of the main contract. If not present, the system generates one automatically. |
| --- | --- |
| code   string | The code of the main contract. <br>Max length: 255 |
| name   string | The name of the main contract. <br>Max length: 1024 |
| note   string | A note about the main contract in [Tiptap](https://tiptap.dev/introduction/)-formatted rich text. |
| scopeOfWork   string | The scope of work signed by all parties to the main contract, in [Tiptap](https://tiptap.dev/introduction/)-formatted rich text. |
| description   string | A detailed description of the main contract. <br>Max length: 2048 |
| type   string,null | The type of the main contract. For example, `Fixed Price` or `Unit Price`. This is customizable for the project administrator. |
| contactId   string,null | The BIM360/ACC ID of the supplierâs default contact. |
| recipients   array: object | Not relevant |
| id   string | Not relevant |
| isDefault   boolean | Not relevant |
| creatorId   string,null | The BIM360/ACC ID of the user who created the main contract. |
| signedBy   string,null | The BIM360/ACC ID of the user who signed the main contract. |
| changedBy   string,null | The BIM360/ACC ID of the user who made the most recent change to the main contract. |
| ownerCompanyId   string,null | The ID of a company managed by a BIM 360 Admin. Detailed company information can be retrieved by calling [GET projects/:project_id/companies](en/docs/bim360/v1/reference/http/projects-:project_id-companies-GET/) and locating the member_group_id in the response. |
| contractorCompanyId   string,null | Not relevant |
| ownerCompanyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](en/docs/bim360/v1/reference/http/companies-:company_id-GET/) in the response. |
| contractorCompanyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](en/docs/bim360/v1/reference/http/companies-:company_id-GET/) in the response. |
| architectCompanyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](en/docs/bim360/v1/reference/http/companies-:company_id-GET/) in the response. |
| notaryCompanyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](en/docs/bim360/v1/reference/http/companies-:company_id-GET/) in the response. |
| notaryContactId   string,null | The notary contact id. This is the ID of a contact managed by BIM360/ACC Admin. |
| additionalCollaborators   array: object | The additional collaborator company and contacts. |
| companyId   string | The BIM360/ACC ID of the firm. |
| companyUid   string,null | The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling [GET companies/:company_id](en/docs/bim360/v1/reference/http/companies-:company_id-GET/) in the response. |
| contactIds   array: string | The BIM360/ACC user ID of the contacts in the firm. |
| status   string | The status of the main contract. Possible values: `closed`, `executed`, `review`, `signed`. |
| amount   number,string,null | The total value of the subitems of the main contract. |
| paid   number,string,null | The total amount of the main contract that has been paid to date. |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |
| startDate   string,null | The start date of the main contract. |
| executedDate   string,null | The execution date of the main contract. |
| plannedCompletionDate   string,null | The planned completion date of the main contract. |
| scheduleChange   number,null | The schedule change of the main contract. |
| revisedCompletionDate   string,null | The revised completion date of the main contract. |
| actualCompletionDate   string,null | The actual completion date of the main contract. |
| closeDate   string,null | The closing date of the main contract. |
| isDefault   boolean,null | `true`: This is the default main contract. `false`: This is not the default main contract. |
| completedWorkRetentionPercent   number,null | The completed work retention percentage of the main contract amount. |
| materialsRetentionPercent   number,null | The materials retention percentage of the main contract amount. |
| retentionCap   number,null | The total retention percentage of the main contract amount. |
| paymentDue   int | Not relevant |
| paymentDueType   string,null | Not relevant |
| unReceived   integer,null | The total value of the main contract amount that was approved but not paid. |
| externalId   string | The identifier assigned to an item in its original external ERP system. Use this ID to track and look up data within the integrated system. Note that this value comes from the itemâs ID in the external system. <br>Max length: 255 |
| externalSystem   string | The name of the external ERP system integrated with Cost Management. Use this name to identify and search for data within the integrated system. <br>Max length: 255 |
| externalMessage   string | A message generated by the external ERP system that explains the sync status of the integration. For example, common values include `success` or `fail` to indicate the result of the integration operation. <br>Max length: 255 |
| lastSyncTime   datetime: ISO 8601 | The date and time when the item was last synchronized with the external ERP system. This value is updated by the external system and is in ISO 8601 format. |
| integrationState   string,null | The state of the item during the integration with the external ERP system (such as SignNow). An item can be a `budget`, `contract`, `main contract`, `main contract item`, `cost item`, `expense`, `expense item`, `change order`, or `schedule of value`. For more details, see [Integrate with External System](../how-to-docs/cost-integrate-with-external-system.md) tutorial. Possible values: <br>`locked`: the item is currently locked within the ERP system, preventing modifications until unlocked. To unlock and modify the item, use the relevant PATCH endpoint to set `integrationState` to `null`. For example, for a budget, call [PATCH budgets](en/docs/bim360/v1/reference/http/cost-budgets-budgetId-PATCH/). For a contract, call [PATCH contracts](en/docs/bim360/v1/reference/http/cost-contracts-contractId-PATCH/). For more details, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Integrated_and_Locked).<br>`integrated`: the item has been successfully added to the ERP system.<br>`failed`: the item encountered an error during the integration process and was not successfully added to the ERP system. For example, if a user tries to integrate `contracts` from an ERP system and the updates fail, the `integrationState` can be set to `failed`. Retry the sync process or analyze the issue if it continues to fail.<br>`null`: The item has not been integrated with the ERP system. This is default value.<br>For more information regarding integrations within the Cost Management system, see [Integrations in Cost Management](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Integrations). |
| integrationStateChangedAt   string,null | The date and time that the itemâs integration status was last changed. |
| integrationStateChangedBy   string,null | The user who last changed the integration status. This is the ID of a user managed by the BIM 360/ACC Admin. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/main-contracts/1df59db0-9484-11e8-a7ec-7ddae203e404' \
  -X 'PATCH' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "code": 1011,
        "name": "Site Management Staff",
        "description": "Site Management Staff",
        "note": "Site Management Staff",
        "scopeOfWork": "Site Management Staff",
        "type": "Fixed Price",
        "contactId": "CED9LVTLHNXV",
        "ownerCompanyId": "F71EDA97",
        "ownerContactId": "90A2FD749912",
        "architectCompanyId": "6FA508F4",
        "architectContactId": "EF6BDFD0AE4D",
        "additionalCollaborators": [
          {
            "companyId": "GF8XKPKWM38E",
            "companyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
            "contactIds": [
              "CED9LVTLHNXV"
            ]
          }
        ],
        "ownerCompanyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
        "contractorCompanyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
        "architectCompanyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
        "notaryCompanyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
        "startDate": "2019-08-22",
        "executedDate": "2019-08-22",
        "plannedCompletionDate": "2019-08-22",
        "revisedCompletionDate": "2019-08-22",
        "actualCompletionDate": "2019-08-22",
        "closeDate": "2019-08-22",
        "status": "open",
        "isDefault": true,
        "completedWorkRetentionPercent": "50",
        "materialsRetentionPercent": "50",
        "retentionCap": "50",
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
  "id": "1df59db0-9484-11e8-a7ec-7ddae203e404",
  "code": 1011,
  "name": "Site Management Staff",
  "note": "Site Management Staff",
  "scopeOfWork": "Site Management Staff",
  "description": "Site Management Staff",
  "type": "Fixed Price",
  "contactId": "CED9LVTLHNXV",
  "recipients": [
    {
      "id": "ZPYARKZX9ANQ",
      "isDefault": false
    }
  ],
  "creatorId": "CED9LVTLHNXV",
  "signedBy": "CED9LVTLHNXV",
  "changedBy": "CED9LVTLHNXV",
  "ownerCompanyId": "GF8XKPKWM38E",
  "contractorCompanyId": "GF8XKPKWM38E",
  "ownerCompanyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
  "contractorCompanyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
  "architectCompanyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
  "notaryCompanyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
  "notaryContactId": "716EF53CE6B1",
  "additionalCollaborators": [
    {
      "companyId": "GF8XKPKWM38E",
      "companyUid": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
      "contactIds": [
        "CED9LVTLHNXV"
      ]
    }
  ],
  "status": "open",
  "amount": "1000.0000",
  "paid": "1000.0000",
  "createdAt": "2019-01-06T01:24:22.678Z",
  "updatedAt": "2019-09-05T01:00:12.989Z",
  "startDate": "2019-08-22",
  "executedDate": "2019-08-22",
  "plannedCompletionDate": "2019-08-22",
  "scheduleChange": 10,
  "revisedCompletionDate": "2019-08-22",
  "actualCompletionDate": "2019-08-22",
  "closeDate": "2019-08-22",
  "isDefault": true,
  "completedWorkRetentionPercent": "50",
  "materialsRetentionPercent": "50",
  "retentionCap": "50",
  "paymentDue": 10,
  "paymentDueType": "afterStart",
  "unReceived": 10,
  "externalId": "10010-99-AB",
  "externalSystem": "Sage300",
  "externalMessage": "Success.",
  "lastSyncTime": "2019-09-05T01:00:12.989Z",
  "integrationState": "locked",
  "integrationStateChangedAt": "2019-09-05T01:00:12.989Z",
  "integrationStateChangedBy": "CED9LVTLHNXV"
}

```

Show More
