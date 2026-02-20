# v1/containers/{containerId}/main-contracts/{id}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-main-contracts-id-GET/

---

# v1/containers/{containerId}/main-contracts/{id}

Retrieves a main contract by ID in the given project.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/main-contracts/:id Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. region string Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead. Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page. To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.

Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page.

To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

### Request

## URI Parameters

containerId string: UUID The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see GET projects . id string: UUID The object ID of the main contract. You can obtain this ID from the response to the POST mainContract or GET mainContract endpoint.

### Request

## Query String Parameters

include array: string A list of the types of sub-main contract components to include in the response with the main contracts, separated by commas. For example, include=mainContractItems returns the items that comprise each of the returned main contracts; include=attributes returns custom attributes of the main contracts. Possible values mainContractItems , attributes .

For example, include=mainContractItems returns the items that comprise each of the returned main contracts; include=attributes returns custom attributes of the main contracts.

Possible values mainContractItems , attributes .

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters are invalid. 401 Unauthorized The provided bearer token is invalid. 403 Forbidden Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The resource or endpoint cannot be found. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 429 Too Many Requests Rate limit exceeded. Retry your request after a few minutes. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Service unavailable.

### Response

## Body Structure (200)

id string The unique ID of the main contract. If not present, the system generates one automatically. code string The code of the main contract. Max length: 255 name string The name of the main contract. Max length: 1024 note string A note about the main contract in Tiptap -formatted rich text. scopeOfWork string The scope of work signed by all parties to the main contract, in Tiptap -formatted rich text. description string A detailed description of the main contract. Max length: 2048 type string,null The type of the main contract. For example, Fixed Price or Unit Price . This is customizable for the project administrator. contactId string,null The BIM360/ACC ID of the supplierâs default contact. recipients array: object Not relevant id string Not relevant isDefault boolean Not relevant creatorId string,null The BIM360/ACC ID of the user who created the main contract. signedBy string,null The BIM360/ACC ID of the user who signed the main contract. changedBy string,null The BIM360/ACC ID of the user who made the most recent change to the main contract. ownerCompanyId string,null The ID of a company managed by a BIM 360 Admin. Detailed company information can be retrieved by calling GET projects/:project_id/companies and locating the member_group_id in the response. contractorCompanyId string,null Not relevant ownerCompanyUid string,null The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling GET companies/:company_id in the response. contractorCompanyUid string,null The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling GET companies/:company_id in the response. architectCompanyUid string,null The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling GET companies/:company_id in the response. notaryCompanyUid string,null The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling GET companies/:company_id in the response. notaryContactId string,null The notary contact id. This is the ID of a contact managed by BIM360/ACC Admin. additionalCollaborators array: object The additional collaborator company and contacts. companyId string The BIM360/ACC ID of the firm. companyUid string,null The unique ID (UUID) of the company in this account. Detailed company information can be retrieved using this UUID by calling GET companies/:company_id in the response. contactIds array: string The BIM360/ACC user ID of the contacts in the firm. status string The status of the main contract. Possible values: closed , executed , review , signed . amount number,string,null The total value of the subitems of the main contract. paid number,string,null The total amount of the main contract that has been paid to date. createdAt datetime: ISO 8601 The date and time that the item was created, in ISO 8601 format. updatedAt datetime: ISO 8601 The date and time that the item was last updated, in ISO 8601 format. startDate string,null The start date of the main contract. executedDate string,null The execution date of the main contract. plannedCompletionDate string,null The planned completion date of the main contract. scheduleChange number,null The schedule change of the main contract. revisedCompletionDate string,null The revised completion date of the main contract. actualCompletionDate string,null The actual completion date of the main contract. closeDate string,null The closing date of the main contract. isDefault boolean,null true : This is the default main contract. false : This is not the default main contract. completedWorkRetentionPercent number,null The completed work retention percentage of the main contract amount. materialsRetentionPercent number,null The materials retention percentage of the main contract amount. retentionCap number,null The total retention percentage of the main contract amount. paymentDue int Not relevant paymentDueType string,null Not relevant unReceived integer,null The total value of the main contract amount that was approved but not paid. externalId string The identifier assigned to an item in its original external ERP system. Use this ID to track and look up data within the integrated system. Note that this value comes from the itemâs ID in the external system. Max length: 255 externalSystem string The name of the external ERP system integrated with Cost Management. Use this name to identify and search for data within the integrated system. Max length: 255 externalMessage string A message generated by the external ERP system that explains the sync status of the integration. For example, common values include success or fail to indicate the result of the integration operation. Max length: 255 lastSyncTime datetime: ISO 8601 The date and time when the item was last synchronized with the external ERP system. This value is updated by the external system and is in ISO 8601 format. integrationState string,null The state of the item during the integration with the external ERP system (such as SignNow). An item can be a budget , contract , main contract , main contract item , cost item , expense , expense item , change order , or schedule of value . For more details, see Integrate with External System tutorial.
Possible values: locked : the item is currently locked within the ERP system, preventing modifications until unlocked. To unlock and modify the item, use the relevant PATCH endpoint to set integrationState to null . For example, for a budget, call PATCH budgets . For a contract, call PATCH contracts . For more details, see the Help documentation . integrated : the item has been successfully added to the ERP system. failed : the item encountered an error during the integration process and was not successfully added to the ERP system. For example, if a user tries to integrate contracts from an ERP system and the updates fail, the integrationState can be set to failed . Retry the sync process or analyze the issue if it continues to fail. null : The item has not been integrated with the ERP system. This is default value. For more information regarding integrations within the Cost Management system, see Integrations in Cost Management . integrationStateChangedAt string,null The date and time that the itemâs integration status was last changed. integrationStateChangedBy string,null The user who last changed the integration status. This is the ID of a user managed by the BIM 360/ACC Admin.

Max length: 255

Max length: 1024

Max length: 2048

Max length: 255

Max length: 255

Max length: 255

locked : the item is currently locked within the ERP system, preventing modifications until unlocked. To unlock and modify the item, use the relevant PATCH endpoint to set integrationState to null . For example, for a budget, call PATCH budgets . For a contract, call PATCH contracts . For more details, see the Help documentation .

integrated : the item has been successfully added to the ERP system.

failed : the item encountered an error during the integration process and was not successfully added to the ERP system. For example, if a user tries to integrate contracts from an ERP system and the updates fail, the integrationState can be set to failed . Retry the sync process or analyze the issue if it continues to fail.

null : The item has not been integrated with the ERP system. This is default value.

For more information regarding integrations within the Cost Management system, see Integrations in Cost Management .

## Example

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/main-contracts/1df59db0-9484-11e8-a7ec-7ddae203e404' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "id" : "1df59db0-9484-11e8-a7ec-7ddae203e404" , "code" : 1011 , "name" : "Site Management Staff" , "note" : "Site Management Staff" , "scopeOfWork" : "Site Management Staff" , "description" : "Site Management Staff" , "type" : "Fixed Price" , "contactId" : "CED9LVTLHNXV" , "recipients" : [ { "id" : "ZPYARKZX9ANQ" , "isDefault" : false } ], "creatorId" : "CED9LVTLHNXV" , "signedBy" : "CED9LVTLHNXV" , "changedBy" : "CED9LVTLHNXV" , "ownerCompanyId" : "GF8XKPKWM38E" , "contractorCompanyId" : "GF8XKPKWM38E" , "ownerCompanyUid" : "683904a0-47ce-4146-ac2d-a3840f00e0f4" , "contractorCompanyUid" : "683904a0-47ce-4146-ac2d-a3840f00e0f4" , "architectCompanyUid" : "683904a0-47ce-4146-ac2d-a3840f00e0f4" , "notaryCompanyUid" : "683904a0-47ce-4146-ac2d-a3840f00e0f4" , "notaryContactId" : "716EF53CE6B1" , "additionalCollaborators" : [ { "companyId" : "GF8XKPKWM38E" , "companyUid" : "683904a0-47ce-4146-ac2d-a3840f00e0f4" , "contactIds" : [ "CED9LVTLHNXV" ] } ], "status" : "open" , "amount" : "1000.0000" , "paid" : "1000.0000" , "createdAt" : "2019-01-06T01:24:22.678Z" , "updatedAt" : "2019-09-05T01:00:12.989Z" , "startDate" : "2019-08-22" , "executedDate" : "2019-08-22" , "plannedCompletionDate" : "2019-08-22" , "scheduleChange" : 10 , "revisedCompletionDate" : "2019-08-22" , "actualCompletionDate" : "2019-08-22" , "closeDate" : "2019-08-22" , "isDefault" : true , "completedWorkRetentionPercent" : "50" , "materialsRetentionPercent" : "50" , "retentionCap" : "50" , "paymentDue" : 10 , "paymentDueType" : "afterStart" , "unReceived" : 10 , "externalId" : "10010-99-AB" , "externalSystem" : "Sage300" , "externalMessage" : "Success." , "lastSyncTime" : "2019-09-05T01:00:12.989Z" , "integrationState" : "locked" , "integrationStateChangedAt" : "2019-09-05T01:00:12.989Z" , "integrationStateChangedBy" : "CED9LVTLHNXV" }
```
