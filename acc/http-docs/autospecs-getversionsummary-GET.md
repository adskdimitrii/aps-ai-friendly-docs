# projects/{projectId}/version/{versionId}/submittalsSummary

Source: https://aps.autodesk.com/en/docs/acc/reference/http/autospecs-getversionsummary-GET/

---

# projects/{projectId}/version/{versionId}/submittalsSummary

Retrieves the number of submittals for each submittal group and each submittal type.
To retrieve all submittal data from the Smart Register, call GET smartregister

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/autospecs/v1/projects/{projectId}/version/{versionId}/submittalsSummary Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

projectId string The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial . You need to convert the project ID into a project ID for the ACC API by removing the âb.â prefix. For example, a project ID of b.a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. versionId string The AutoSpecs version ID of the project. For information about how to find the version ID, see the first few steps of the Retrieve Submittal Log tutorial.

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial . You need to convert the project ID into a project ID for the ACC API by removing the âb.â prefix. For example, a project ID of b.a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Response

## HTTP Status Code Summary

200 OK OK 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

submittalGroups array: object A list of submittal groups. submittalGroupTypes array: object A list of submittal group types. submittalType enum:string The type of submittal. This corresponds to the Submittal type column in the UI.
Possible values: Test Reports , Shop Drawings , Schedules , Samples , Sample Warranty , Reports , Qualification Data , QUALITY ASSURANCE , Product Data , Performance Data , Mfg. Instructions , Meeting/Conferences , Drawings , Delegated-Design , Certifications , Certificates , Calculations , Attic Stock , Demonstrations , General Warranties , O&M Manuals , Special Warranties , LEED , As-Builts , TESTS AND INSPECTIONS , General , Manufacturers Instructions , Substitutions , Mix Design , Others total int The number of submittals for the submittal type. submittalGroup enum:string The submittal group associated with the submittal. This is equivalent to the Submittal group column in the UI.
Possible values: ACTION AND INFORMATIONAL , CLOSEOUT SUBMITTALS , FIELD QUALITY CONTROL , Mockups , QUALITY ASSURANCE , Tests And Inspections , DIVISION 01 REQUIREMENTS total int The number of submittals in the submittal group.

## Example

Successful retrieval of the number of submittals for each submittal group and each submittal type

### Request

```
curl - v 'https://developer.api.autodesk.com/construction/autospecs/v1/projects/:projectId/version/:versionId/submittalsSummary' \ - H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "submittalGroups" : [ { "submittalGroupTypes" : [ { "submittalType" : "LEED" , "total" : 2 }, { "submittalType" : "Mfg. Instructions" , "total" : 1 }, { "submittalType" : "Others" , "total" : 1 }, { "submittalType" : "Product Data" , "total" : 3 }, { "submittalType" : "Qualification Data" , "total" : 1 }, { "submittalType" : "Reports" , "total" : 1 }, { "submittalType" : "Samples" , "total" : 1 }, { "submittalType" : "Shop Drawings" , "total" : 3 } ], "submittalGroup" : "Action And Informational" , "total" : 13 }, { "submittalGroup" : "Mockups" , "total" : 1 }, { "submittalGroup" : "Quality Assurance" , "total" : 12 }, { "submittalGroup" : "Tests And Inspections" , "total" : 3 } ] }
```
