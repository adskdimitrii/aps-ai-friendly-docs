# projects/{projectId}/classification-systems/{systemId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-classification-systems-system_id-GET/

---

# projects/{projectId}/classification-systems/{systemId}

Retrieves high-level details of a specified classification system.

A classification system categorizes and organizes construction information in a hierarchical structure, and is used to label items in a takeoff project.

For more information about the classification system, see the ACC Configure Takeoff Settings help documentation.

To find the hierarchy of a specific classification system, call GET classifications .

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/classification-systems/{systemId} Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

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

200 OK Successfully retrieved the classification system. 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The âRetry-Afterâ header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

id string: UUID The classification system ID. name string The classification system name. Max length: 200 type enum:string The type of classification system. Possible values: CLASSIFICATION_SYSTEM_1 , CLASSIFICATION_SYSTEM_2 . See the Help documentation for more details about the classification systems.

Max length: 200

Possible values: CLASSIFICATION_SYSTEM_1 , CLASSIFICATION_SYSTEM_2 .

See the Help documentation for more details about the classification systems.

## Example

Successfully retrieved the classification system.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/classification-systems/:systemId' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "id" : "497f6eca-6276-4993-bfeb-53cbbbba6f08" , "name" : "Smith Construction Classification" , "type" : "CLASSIFICATION_SYSTEM_1" }
```
