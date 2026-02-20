# v1/containers/{containerId}/cost-items:detach

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-cost-itemsdetach-POST/

---

# v1/containers/{containerId}/cost-items:detach

Remove existing cost items from a change order.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/cost/v1/containers/:containerId/cost-items:detach Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

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

Change order and cost ID list.

changeOrderId * string: UUID The ID of the change order to which the cost item is attached. costItemId * string: UUID The ID of the cost item to detach.

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters are invalid. 401 Unauthorized The provided bearer token is invalid. 403 Forbidden Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The resource or endpoint cannot be found. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 429 Too Many Requests Rate limit exceeded. Retry your request after a few minutes. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Service unavailable.

### Response

## Body Structure (200)

changeOrderId string: UUID The ID of the change order to which the cost item is attached. costItemId string: UUID The ID of the cost item to detach.

## Example

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/cost-items:detach' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '[ { "changeOrderId": "20982940-85c3-11e8-b1f7-b981d6e78764", "costItemId": "27ace7c0-85c3-11e8-b1f7-b981d6e78764" } ]'
```

### Response

```
[ { "changeOrderId" : "20982940-85c3-11e8-b1f7-b981d6e78764" , "costItemId" : "27ace7c0-85c3-11e8-b1f7-b981d6e78764" } ]
```
