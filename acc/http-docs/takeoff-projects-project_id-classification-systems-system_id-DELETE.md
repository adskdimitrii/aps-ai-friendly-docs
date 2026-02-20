# projects/{projectId}/classification-systems/{systemId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-classification-systems-system_id-DELETE/

---

# projects/{projectId}/classification-systems/{systemId}

Deletes a classification system from a project.

Note that this action will only succeed if there are no takeoff types and items associated with the classification system. The Takeoff API currently does not support dissociating types and items from a classification system. You dissociate takeoff types and items from a classification system in the UI.

To check if a classification system is associated with takeoff types and items, call GET packages and use the package IDs ( results[i].id ) to call GET takeoff-types . Iterate through the takeoff types and check if classificationCodeOne and classificationCodeTwo have a value for both primaryQuantityDefinition and secondaryQuantityDefinition .

## Resource Information

Method and URI DELETE https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/classification-systems/{systemId} Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. region string Specifies the region where the service is located. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

systemId string: UUID The classification system ID. To find the ID, call GET classification-systems . projectId string: UUID The ID of the project. This corresponds to project ID in the Data Management API , and can be specified in the form of âUUIDâ or b.âUUIDâ. To learn how to find the project ID, see the Retrieve ACC Account and project ID tutorial.

To find the ID, call GET classification-systems .

This corresponds to project ID in the Data Management API , and can be specified in the form of âUUIDâ or b.âUUIDâ.

To learn how to find the project ID, see the Retrieve ACC Account and project ID tutorial.

### Response

## HTTP Status Code Summary

204 No Content Successfully deleted the classification system. 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 409 Conflict Canât delete the classification system as some classifications are in use. 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The âRetry-Afterâ header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (204)

Response for 204 has no body.

## Example

Successfully deleted the classification system.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/classification-systems/:systemId' \ -X 'DELETE' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
204 No Content
```
