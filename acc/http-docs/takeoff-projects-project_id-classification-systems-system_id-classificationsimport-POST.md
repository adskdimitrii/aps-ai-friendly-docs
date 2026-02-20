# projects/{projectId}/classification-systems/{systemId}/classifications:import

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-classification-systems-system_id-classificationsimport-POST/

---

# projects/{projectId}/classification-systems/{systemId}/classifications:import

Updates a classification system.

A classification system categorizes and organizes construction information in a hierarchical structure, and is used to label items in a takeoff project.

For more information about the classification system, see the ACC Configure Takeoff Settings help documentation.

Note that this endpoint updates a classification system with a new name and/or classifications configured as a JSON object in the payload, created from a spreadsheet file.

Note that a classification system must first be created, before it can be updated. To create a classification system, call POST classification-systems .

Note that this action overwrites the name and/or all classifications that currently exist in the classification system you are updating.

Note that classifications cannot be updated once the classification system is in use. To check if a classification system is in use, call GET packages and use the package IDs ( results[i].id ) to call GET takeoff-types . Iterate through the takeoff types and check if classificationCodeOne and classificationCodeTwo have a value for both primaryQuantityDefinition and secondaryQuantityDefinition .

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/classification-systems/{systemId}/classifications:import Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. region string Specifies the region where the service is located. Possible values: US , EMEA . For the full list of supported regions, see the Regions page. Content-Type * string Must be application/json

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

projectId string: UUID The ID of the project. This corresponds to project ID in the Data Management API , and can be specified in the form of âUUIDâ or b.âUUIDâ. To learn how to find the project ID, see the Retrieve ACC Account and project ID tutorial. systemId string: UUID The classification system ID. To find the ID, call GET classification-systems .

This corresponds to project ID in the Data Management API , and can be specified in the form of âUUIDâ or b.âUUIDâ.

To learn how to find the project ID, see the Retrieve ACC Account and project ID tutorial.

To find the ID, call GET classification-systems .

### Request

## Body Structure

classificationSystemName string The classification system name. Max length: 200 classifications * array: object The classification hierarchy. The classification hierarchy is configured as a JSON array in the payload, created from a spreadsheet file. Max size: 30000 . For more details, see the ACC Configure Takeoff Settings help documentation. code * string The classification code. Max length: 256 parentCode * string The classification parent code. Its value may be null , indicating that this classification is at the top level of the hierarchy. Max length: 256 description * string A description of the classification. Max length: 256 measurementType enum:string Deprecated. Will be removed on September 15, 2025. The type of measurement. Possible values: AREA , COUNT , DISTANCE , VOLUME .

Max length: 200

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

200 OK Successfully imported the list of classifications. 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The âRetry-Afterâ header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

classificationChanges object added int The number of classifications added by the import. deleted int The number of classifications deleted by the import. modified int The number of classifications modified by the import. classificationSystemName string The classification system name. Max length: 200

Max length: 200

## Example

Successfully imported the list of classifications.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/classification-systems/:systemId/classifications:import' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "classificationSystemName": "Smith Construction Classification", "classifications": [ { "code": "A1010", "parentCode": null, "description": "Concrete", "measurementType": "AREA" }, { "code": "A1010.10", "parentCode": "A1010", "description": "Sprayed concrete", "measurementType": "AREA" }, { "code": "A1010.20", "parentCode": "A1010", "description": "Foamed concrete", "measurementType": "AREA" } ] }'
```

### Response

```
{ "classificationChanges" : { "added" : 1 , "deleted" : 3 , "modified" : 2 }, "classificationSystemName" : "Smith Construction Classification" }
```
