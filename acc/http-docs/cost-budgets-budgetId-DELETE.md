# v1/containers/{containerId}/budgets/{budgetId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-budgets-budgetId-DELETE/

---

# v1/containers/{containerId}/budgets/{budgetId}

Deletes a budget.

## Resource Information

Method and URI DELETE https://developer.api.autodesk.com/cost/v1/containers/:containerId/budgets/:budgetId Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. region string Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead. Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page. To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.

Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page.

To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

### Request

## URI Parameters

containerId string: UUID The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see GET projects . budgetId array: string: uuid The budget ID.

### Request

## Query String Parameters

force boolean true : This request forces an override of locked budgeting so the request can succeed. The ability to create, update, or delete budgets can be locked at the project level, and force enables administrators to override the lock. A locked budget. Only a project administrator is allowed to update, create, or delete budgets when locked. false : This request does not override locked budgeting.

false : This request does not override locked budgeting.

### Response

## HTTP Status Code Summary

204 No Content The resource has been deleted successfully. 400 Bad Request The parameters are invalid. 401 Unauthorized The provided bearer token is invalid. 403 Forbidden Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The resource or endpoint cannot be found. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 429 Too Many Requests Rate limit exceeded. Retry your request after a few minutes. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Service unavailable.

### Response

## Body Structure (204)

Response for 204 has no body.

## Example

The resource has been deleted successfully.

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/budgets/226449d0-9481-11e8-87fb-215990a8aeb3' \ -X 'DELETE' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
204 No Content
```
