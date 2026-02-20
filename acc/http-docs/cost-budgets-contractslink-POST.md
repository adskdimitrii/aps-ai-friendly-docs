# v1/containers/{containerId}/budgets-contracts:link

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-budgets-contractslink-POST/

---

# v1/containers/{containerId}/budgets-contracts:link

Link or unlink one or multiple budgets with one or multiple contracts. After budgets and contracts are linked, Contract Schedule of Values will be created.
Max 50 pairs are allowed to link or unlink in one request.
Note: Linking the same budget to multiple contracts in a single API call is not yet supported. Youâll need to call this API multiple times to link the same budget to multiple contracts. Ensure that Allocate a Budget to more than one Contract is enabled in your Cost Settings.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/cost/v1/containers/:containerId/budgets-contracts:link Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

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

create array: object contractId string: UUID ID of the Contract to which the budget to link. budgetId string: UUID ID of the Budget to which the contract should be linked. remove array: object contractId string: UUID ID of the Contract to which the budget to link. budgetId string: UUID ID of the Budget to which the contract to link.

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters are invalid. 401 Unauthorized The provided bearer token is invalid. 403 Forbidden Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The resource or endpoint cannot be found. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 429 Too Many Requests Rate limit exceeded. Retry your request after a few minutes. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Service unavailable.

### Response

## Body Structure (200)

Response for 200 has no body.

## Example

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/budgets-contracts:link' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "create": [ { "contractId": "226449d0-9481-11e8-87fb-215990a8aeb3", "budgetId": "f77f7cfa-47a4-41d4-be49-dafc92202903" } ], "remove": [ { "contractId": "d241d341-eb21-4893-b21f-3152d6db4faa", "budgetId": "0d760290-a82b-41ac-9e62-aa70b7217d42" } ] }'
```

### Response
