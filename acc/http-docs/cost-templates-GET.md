# v1/containers/{containerId}/templates

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-templates-GET/

---

# v1/containers/{containerId}/templates

Retrieves ID, name, and timestamp information for all budget code templates in a specific project. Currently, a project can have only one template.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/templates Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. region string Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead. Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page. To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.

Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page.

To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

### Request

## URI Parameters

containerId string: UUID The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see GET projects .

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters are invalid. 401 Unauthorized The provided bearer token is invalid. 403 Forbidden Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The resource or endpoint cannot be found. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 429 Too Many Requests Rate limit exceeded. Retry your request after a few minutes. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Service unavailable.

### Response

## Body Structure (200)

id string: UUID The ID of the budget code template. name string The name of the budget code template. Max length: 1024 locked boolean,null The lock status of template. createdAt datetime: ISO 8601 The date and time that the item was created, in ISO 8601 format. updatedAt datetime: ISO 8601 The date and time that the item was last updated, in ISO 8601 format. integrationState string,null The state of the item during the integration with the external ERP system (such as SignNow). An item can be a budget , contract , main contract , main contract item , cost item , expense , expense item , change order , or schedule of value . For more details, see Integrate with External System tutorial.
Possible values: locked : the item is currently locked within the ERP system, preventing modifications until unlocked. To unlock and modify the item, use the relevant PATCH endpoint to set integrationState to null . For example, for a budget, call PATCH budgets . For a contract, call PATCH contracts . For more details, see the Help documentation . integrated : the item has been successfully added to the ERP system. failed : the item encountered an error during the integration process and was not successfully added to the ERP system. For example, if a user tries to integrate contracts from an ERP system and the updates fail, the integrationState can be set to failed . Retry the sync process or analyze the issue if it continues to fail. null : The item has not been integrated with the ERP system. This is default value. For more information regarding integrations within the Cost Management system, see Integrations in Cost Management . integrationStateChangedAt string,null The date and time that the itemâs integration status was last changed. integrationStateChangedBy string,null The user who last changed the integration status. This is the ID of a user managed by the BIM 360/ACC Admin.

Max length: 1024

locked : the item is currently locked within the ERP system, preventing modifications until unlocked. To unlock and modify the item, use the relevant PATCH endpoint to set integrationState to null . For example, for a budget, call PATCH budgets . For a contract, call PATCH contracts . For more details, see the Help documentation .

integrated : the item has been successfully added to the ERP system.

failed : the item encountered an error during the integration process and was not successfully added to the ERP system. For example, if a user tries to integrate contracts from an ERP system and the updates fail, the integrationState can be set to failed . Retry the sync process or analyze the issue if it continues to fail.

null : The item has not been integrated with the ERP system. This is default value.

For more information regarding integrations within the Cost Management system, see Integrations in Cost Management .

## Example

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/templates' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
[ { "id" : "a2a9eb81-052b-4a18-9988-571e8134f98b" , "name" : "Custom Template" , "locked" : false , "createdAt" : "2019-01-06T01:24:22.678Z" , "updatedAt" : "2019-09-05T01:00:12.989Z" , "integrationState" : "locked" , "integrationStateChangedAt" : "2019-09-05T01:00:12.989Z" , "integrationStateChangedBy" : "CED9LVTLHNXV" } ]
```
