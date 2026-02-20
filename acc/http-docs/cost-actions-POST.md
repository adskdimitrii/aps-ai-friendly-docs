# v1/containers/{containerId}/workflows/actions

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-actions-POST/

---

# v1/containers/{containerId}/workflows/actions

Perform a specified action on an item.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/cost/v1/containers/:containerId/workflows/actions Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json region string Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead. Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page. To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.

Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page.

To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

### Request

## URI Parameters

containerId string: UUID The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see GET projects .

### Request

## Body Structure

The actions to perform.

action * string Name of the action to perform. The possible actions are from GET /actions . Max length: 255 associationId * string The ID of the item on which to perform the action. For example, change order ID. associationType * enum:string The type of the item on which to perform the action. Possible values: FormInstance , OCO , PCO , RCO , RFQ , SCO , Expense , Contract , CostPayment , BudgetPayment , BudgetTransfer , MainContract , DistributionItem . options object Extra data required by the action.

Max length: 255

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters are invalid. 401 Unauthorized The provided bearer token is invalid. 403 Forbidden Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The resource or endpoint cannot be found. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 429 Too Many Requests Rate limit exceeded. Retry your request after a few minutes. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Service unavailable.

### Response

## Body Structure (200)

action string The name of the action performed on the specified item. For example, budgetOpen on a PCO. Max length: 255 associationId string The object ID of the item on which the action was performed - a change order (PCO, RCO, OCO, RFQ or SCO) for example. associationType string The type of the item on which the action was performed. Possible values: FormInstance , OCO , PCO , RCO , RFQ , SCO , Expense , Contract , CostPayment , BudgetPayment , BudgetTransfer , MainContract . errors array: object An array of errors that occurred during action execution. status int BIM 360 Cost Management defined error code for the error. title string Title of the error. detail string Detailed description of the error. errors array: object List of field validation errors. code string BIM 360 Cost Management defined error code for the error. field string Name of the field associated to the error. title string Title of the error. detail string The detailed description of the error.

Max length: 255

## Example

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/workflows/actions' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '[ { "action": "open", "associationId": "48934441-e392-49d7-bf58-8dea43d413ae", "associationType": "FormInstance", "options": {} } ]'
```

### Response

```
[ { "action" : "open" , "associationId" : "48934441-e392-49d7-bf58-8dea43d413ae" , "associationType" : "FormInstance" , "errors" : [ { "status" : 400 , "title" : "Authentication required" , "detail" : "Missing authentication credentials for the Greeting resource." , "errors" : [ { "code" : 400010 , "field" : "color" , "title" : "Invalid Parameter" , "detail" : "color must be ``green``, ``red`` or ``blue``" } ] } ] } ]
```
