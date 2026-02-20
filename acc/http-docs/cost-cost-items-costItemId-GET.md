# v1/containers/{containerId}/cost-items/{costItemId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-cost-items-costItemId-GET/

---

# v1/containers/{containerId}/cost-items/{costItemId}

Gets a cost item specified by ID. The returned item includes details.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/cost-items/:costItemId Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. region string Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead. Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page. To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.

Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page.

To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

### Request

## URI Parameters

containerId string: UUID The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see GET projects . costItemId string The ID of the cost item.

### Request

## Query String Parameters

include array: string A list of resources related to the returned cost items to include in the response. Resources can have a maximum length of 100. For example, include=changeOrders returns the change orders that contain each cost item. include=attributes returns custom attributes, which represent the âpropertiesâ in the response. Possible values: budget , changeOrders , subCostItems , attributes .

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters are invalid. 401 Unauthorized The provided bearer token is invalid. 403 Forbidden Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The resource or endpoint cannot be found. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 429 Too Many Requests Rate limit exceeded. Retry your request after a few minutes. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Service unavailable.

### Response

## Body Structure (200)

id string: UUID The unique identifier of the cost item. number string The system generated sequential number. splitNumber object Not relevant prefix string Not relevant number string Not relevant postfix string Not relevant isFreeModify boolean Not relevant name string The name of the cost item. Max length: 255 description string A detailed description of the cost item. budgetId string,null The ID of the budget to which the cost item is linked. contractId string,null The ID of the contract to which the cost item is linked. budgetStatus string,null The current budget status of the cost item, indicating its lifecycle stage. Possible values: draft , open , submitted , accepted , approved , executed , revising , rejected , void . Note that you can only change the status by updating the associated change order. costStatus string,null The current financial approval status of the cost item. Possible values: draft , open , revising , pricing , proposed , approved , executed , rejected , contracted , accepted , void . Note that the cost status can only be changed by updating the associated change order. scope enum:string Defines the projectâs scope status of the cost item. Possible values: out , in , tbd , budgetOnly , contingency . type string The category or classification of the cost item, which the Project Admin can customize. isMarkup boolean Indicates if the cost item includes a markup. true : the item is a markup cost item. false : (default) the item is not a markup cost item. estimated number,string,null The rough estimate of the cost item without a formal quote. proposed number,string,null The quoted cost of the cost item provided by the supplier. submitted number,string,null The amount submitted to the owner for approval. approved number,string,null The amount approved by the owner. committed number,string,null The amount committed to the supplier. inputQuantity number,null The initial quantity of the proposed cost item as specified in the budget or contract. quantity number The total quantity of the cost item. unit string The unit of measurement for the cost item. scopeOfWork string The scope of work of the cost items, formatted as Tiptap rich text ( https://tiptap.dev/introduction/ ). note string A note associated with the cost item, formatted as Tiptap rich text ( https://tiptap.dev/introduction/ ). proposedExchangeRate number,string,null The exchange rate used for the proposed cost. If multi-currency was not enabled, the value is set to 1 regardless of the specified rate. Default value: 1 . committedExchangeRate number,string,null The exchange rate used for the committed cost. If multi-currency was not enabled, the value is set to 1 regardless of the specified rate. Default value: 1 . budgetTransferId string,null Not relevant budgetTransferItemId string,null Not relevant locations array,null A list of the IDs of the project locations where this item applies. For more information, see the Locations Help documentation help. locationPaths array,null A list of the IDs of the project locations where this item applies, along with the node paths of these locations in the projectâs locations tree. For more information, see the Locations Help documentation help. externalId string The identifier assigned to an item in its original external ERP system. Use this ID to track and look up data within the integrated system. Note that this value comes from the itemâs ID in the external system. Max length: 255 externalSystem string The name of the external ERP system integrated with Cost Management. Use this name to identify and search for data within the integrated system. Max length: 255 externalMessage string A message generated by the external ERP system that explains the sync status of the integration. For example, common values include success or fail to indicate the result of the integration operation. Max length: 255 lastSyncTime datetime: ISO 8601 The date and time when the item was last synchronized with the external ERP system. This value is updated by the external system and is in ISO 8601 format. integrationState string,null The state of the item during the integration with the external ERP system (such as SignNow). An item can be a budget , contract , main contract , main contract item , cost item , expense , expense item , change order , or schedule of value . For more details, see Integrate with External System tutorial.
Possible values: locked : the item is currently locked within the ERP system, preventing modifications until unlocked. To unlock and modify the item, use the relevant PATCH endpoint to set integrationState to null . For example, for a budget, call PATCH budgets . For a contract, call PATCH contracts . For more details, see the Help documentation . integrated : the item has been successfully added to the ERP system. failed : the item encountered an error during the integration process and was not successfully added to the ERP system. For example, if a user tries to integrate contracts from an ERP system and the updates fail, the integrationState can be set to failed . Retry the sync process or analyze the issue if it continues to fail. null : The item has not been integrated with the ERP system. This is default value. For more information regarding integrations within the Cost Management system, see Integrations in Cost Management . integrationStateChangedAt string,null The date and time that the itemâs integration status was last changed. integrationStateChangedBy string,null The user who last changed the integration status. This is the ID of a user managed by the BIM 360/ACC Admin. createdAt datetime: ISO 8601 The date and time that the item was created, in ISO 8601 format. updatedAt datetime: ISO 8601 The date and time that the item was last updated, in ISO 8601 format.

Max length: 255

Possible values: draft , open , submitted , accepted , approved , executed , revising , rejected , void .

Note that you can only change the status by updating the associated change order.

Possible values: draft , open , revising , pricing , proposed , approved , executed , rejected , contracted , accepted , void .

Note that the cost status can only be changed by updating the associated change order.

true : the item is a markup cost item.

false : (default) the item is not a markup cost item.

For more information, see the Locations Help documentation help.

For more information, see the Locations Help documentation help.

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
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/cost-items/f6445638-ca68-4e3c-9160-15864de6b818' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "id" : "02fd1230-7d9c-11e8-9262-abe29bdc14f2" , "number" : 1 , "splitNumber" : { "prefix" : "INT-" , "number" : 1 , "postfix" : "-XYZ" , "isFreeModify" : false }, "name" : "Revised Entry Details per RFI-001" , "description" : "Revised Entry Details per RFI-001" , "budgetId" : "227e1360-9481-11e8-87fb-215990a8aeb3" , "contractId" : "48dba1a0-2a8e-11ee-b1a7-2f4a196105cb" , "budgetStatus" : "open" , "costStatus" : "open" , "scope" : "in" , "type" : "Purchase Order" , "isMarkup" : false , "estimated" : "1000.0000" , "proposed" : "1000.0000" , "submitted" : "1000.0000" , "approved" : "1000.0000" , "committed" : "1000.0000" , "inputQuantity" : 1 , "quantity" : 1 , "unit" : "ls" , "scopeOfWork" : "" , "note" : "" , "proposedExchangeRate" : "1.0000" , "committedExchangeRate" : "1.0000" , "budgetTransferId" : "48dba1a0-2a8e-11ee-b1a7-2f4a196105cb" , "budgetTransferItemId" : "48dba1a0-2a8e-11ee-b1a7-2f4a196105cb" , "locations" : [ "683904a0-47ce-4146-ac2d-a3840f00e0f4" ], "locationPaths" : [ "683904a0-47ce-4146-ac2d-a3840f00e0f4" ], "externalId" : "10010-99-AB" , "externalSystem" : "Sage300" , "externalMessage" : "Success." , "lastSyncTime" : "2019-09-05T01:00:12.989Z" , "integrationState" : "locked" , "integrationStateChangedAt" : "2019-09-05T01:00:12.989Z" , "integrationStateChangedBy" : "CED9LVTLHNXV" , "createdAt" : "2019-01-06T01:24:22.678Z" , "updatedAt" : "2019-09-05T01:00:12.989Z" }
```
