# projects/{projectId}/settings

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-settings-GET/

---

# projects/{projectId}/settings

Retrieves the measurement system settings for a project.

For more information about measurement system settings, see the ACC Configure Takeoff Settings help documentation.

To configure the measurement system settings, call PATCH settings .

Note that settings for Takeoff cannot be changed once takeoff types and items have been created in the project.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/settings Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. region string Specifies the region where the service is located. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

projectId string: UUID The ID of the project. This corresponds to project ID in the Data Management API , and can be specified in the form of âUUIDâ or b.âUUIDâ. To learn how to find the project ID, see the Retrieve ACC Account and project ID tutorial.

This corresponds to project ID in the Data Management API , and can be specified in the form of âUUIDâ or b.âUUIDâ.

To learn how to find the project ID, see the Retrieve ACC Account and project ID tutorial.

### Response

## HTTP Status Code Summary

200 OK Successfully retrieved the measurement system settings. 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The âRetry-Afterâ header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

measurementSystem enum:string The project measurement system. Possible values: IMPERIAL , METRIC .

Possible values: IMPERIAL , METRIC .

## Example

Successfully retrieved the measurement system settings.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/settings' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "measurementSystem" : "IMPERIAL" }
```
