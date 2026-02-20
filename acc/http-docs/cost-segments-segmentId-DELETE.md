# v1/containers/{containerId}/templates/{templateId}/segments/{segmentId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-segments-segmentId-DELETE/

---

# v1/containers/{containerId}/templates/{templateId}/segments/{segmentId}

Deletes a segment by ID.

## Resource Information

Method and URI DELETE https://developer.api.autodesk.com/cost/v1/containers/:containerId/templates/:templateId/segments/:segmentId Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. region string Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead. Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page. To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.

Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page.

To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

### Request

## URI Parameters

containerId string: UUID The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see GET projects . templateId string: UUID The budget code template ID. To obtain a template ID, use GET templates . segmentId string: UUID The segment ID. To obtain a segment ID, use GET templates/:templateId/segments .

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
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/templates/a2a9eb81-052b-4a18-9988-571e8134f98b/segments/87256c07-5c03-42cd-b4dc-e9d06411c0cc' \ -X 'DELETE' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
204 No Content
```
