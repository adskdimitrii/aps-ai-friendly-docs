# v1/containers/{containerId}/segments/{segmentId}/values

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-values-POST/

---

# v1/containers/{containerId}/segments/{segmentId}/values

Creates a segment value in a budget code segment.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/cost/v1/containers/:containerId/segments/:segmentId/values Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json region string Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead. Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page. To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.

Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page.

To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

### Request

## URI Parameters

containerId string: UUID The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see GET projects . segmentId string: UUID The segment ID. To obtain a segment ID, use GET templates/:templateId/segments .

### Request

## Body Structure

The segmentValue.

id string: UUID The ID of the code. parentId string,null The parent ID of this code if it is the sub item of another code. code * string The display code. Max length: 255 originalCode string The original value of the code before the delimiters are removed. Max length: 255 description * string The description of the code. Max length: 2048

Max length: 255

Max length: 255

Max length: 2048

### Response

## HTTP Status Code Summary

201 Created Success 400 Bad Request The parameters are invalid. 401 Unauthorized The provided bearer token is invalid. 403 Forbidden Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The resource or endpoint cannot be found. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 429 Too Many Requests Rate limit exceeded. Retry your request after a few minutes. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Service unavailable.

### Response

## Body Structure (201)

id string: UUID The ID of the code. segmentId string: UUID The ID of the segment this code belongs to. parentId string,null The parent ID of this code if it is the sub item of another code. code string The display code. Max length: 255 originalCode string The original value of the code before the delimiters are removed. Max length: 255 description string The description of the code. Max length: 2048 createdAt datetime: ISO 8601 The date and time that the item was created, in ISO 8601 format. updatedAt datetime: ISO 8601 The date and time that the item was last updated, in ISO 8601 format.

Max length: 255

Max length: 255

Max length: 2048

## Example

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/segments/87256c07-5c03-42cd-b4dc-e9d06411c0cc/values' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "id": "229d3420-9481-11e8-87fb-215990a8aeb3", "parentId": "null", "code": 6656, "originalCode": "01 50 00", "description": "Temporary Facilities and Controls" }'
```

### Response

```
{ "id" : "229d3420-9481-11e8-87fb-215990a8aeb3" , "segmentId" : "87256c07-5c03-42cd-b4dc-e9d06411c0cc" , "parentId" : "null" , "code" : 6656 , "originalCode" : "01 50 00" , "description" : "Temporary Facilities and Controls" , "createdAt" : "2019-01-06T01:24:22.678Z" , "updatedAt" : "2019-09-05T01:00:12.989Z" }
```
