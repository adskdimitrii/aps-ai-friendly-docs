# projects/{projectId}/classification-systems

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-classification-systems-POST/

---

# projects/{projectId}/classification-systems

Creates a classification system for a project.

A classification system categorizes and organizes construction information in a hierarchical structure, and is used to label items in a takeoff project.

For more information about the classification system, see the ACC Configure Takeoff Settings help documentation.

Note that you can create up to two classification systems for a project.

Note that you can create either an empty, or populated classification system.

To update an existing classification system, call POST classifications:import .

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/classification-systems Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. region string Specifies the region where the service is located. Possible values: US , EMEA . For the full list of supported regions, see the Regions page. Content-Type * string Must be application/json

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

projectId string: UUID The ID of the project. This corresponds to project ID in the Data Management API , and can be specified in the form of âUUIDâ or b.âUUIDâ. To learn how to find the project ID, see the Retrieve ACC Account and project ID tutorial.

This corresponds to project ID in the Data Management API , and can be specified in the form of âUUIDâ or b.âUUIDâ.

To learn how to find the project ID, see the Retrieve ACC Account and project ID tutorial.

### Request

## Body Structure

name * string The classification system name. Max length: 200 type * enum:string The type of classification system. Possible values: CLASSIFICATION_SYSTEM_1 , CLASSIFICATION_SYSTEM_2 . See the Help documentation for more details about the classification systems. classifications array: object The classification hierarchy. The classification hierarchy is configured as a JSON array in the payload, created from a spreadsheet file. Max size: 30000 . For more details, see the ACC Configure Takeoff Settings help documentation. code * string The classification code. Max length: 256 parentCode * string The classification parent code. Its value may be null , indicating that this classification is at the top level of the hierarchy. Max length: 256 description * string A description of the classification. Max length: 256 measurementType enum:string Deprecated. Will be removed on September 15, 2025. The type of measurement. Possible values: AREA , COUNT , DISTANCE , VOLUME .

Max length: 200

Possible values: CLASSIFICATION_SYSTEM_1 , CLASSIFICATION_SYSTEM_2 .

See the Help documentation for more details about the classification systems.

The classification hierarchy is configured as a JSON array in the payload, created from a spreadsheet file.

Max size: 30000 .

For more details, see the ACC Configure Takeoff Settings help documentation.

Max length: 256

Its value may be null , indicating that this classification is at the top level of the hierarchy.

Max length: 256

Max length: 256

The type of measurement.

Possible values: AREA , COUNT , DISTANCE , VOLUME .

### Response

## HTTP Status Code Summary

201 Created Successfully created a classification system. 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 409 Conflict The specified resource already exists. 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The âRetry-Afterâ header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (201)

id string: UUID The classification system ID. name string The classification system name. Max length: 200 type enum:string The type of classification system. Possible values: CLASSIFICATION_SYSTEM_1 , CLASSIFICATION_SYSTEM_2 . See the Help documentation for more details about the classification systems.

Max length: 200

Possible values: CLASSIFICATION_SYSTEM_1 , CLASSIFICATION_SYSTEM_2 .

See the Help documentation for more details about the classification systems.

## Example

Successfully created a classification system.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/classification-systems' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "name": "Smith Construction Classification", "type": "CLASSIFICATION_SYSTEM_1", "classifications": [ { "code": "A1010", "parentCode": null, "description": "Concrete", "measurementType": "AREA" }, { "code": "A1010.10", "parentCode": "A1010", "description": "Sprayed concrete", "measurementType": "AREA" }, { "code": "A1010.20", "parentCode": "A1010", "description": "Foamed concrete", "measurementType": "AREA" } ] }'
```

### Response

```
{ "id" : "497f6eca-6276-4993-bfeb-53cbbbba6f08" , "name" : "Smith Construction Classification" , "type" : "CLASSIFICATION_SYSTEM_1" }
```
