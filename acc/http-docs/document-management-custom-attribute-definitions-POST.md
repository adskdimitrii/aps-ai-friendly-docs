# projects/{project_id}/folders/{folder_id}/custom-attribute-definitions

Source: https://aps.autodesk.com/en/docs/acc/reference/http/document-management-custom-attribute-definitions-POST/

---

# projects/{project_id}/folders/{folder_id}/custom-attribute-definitions

Adds a custom attribute to a folder.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/bim360/docs/v1/projects/:project_id/folders/:folder_id/custom-attribute-definitions Authentication Context user context optional Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. Content-Type * string Must be application/json x-user-id string In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified.

### Request

## URI Parameters

project_id string: UUID The ID of the project. This corresponds to the project ID in the Data Management API . To convert a project ID in the Data Management API to a project ID in the BIM 360 API you need to remove the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. folder_id string The URL-encoded ID (URN) of the folder. For details about how to find the URN, follow the initial steps (1-3) of the Download Files tutorial.

For details about how to find the URN, follow the initial steps (1-3) of the Download Files tutorial.

### Request

## Body Structure

name * string The name of the attribute. It needs to be unique within the folder. type * enum:string The type of attribute. Possible values: string (text field), date , array (drop-list). arrayValues array: string A list of possible values for the attribute. Only relevant for drop-list attributes.

### Response

## HTTP Status Code Summary

201 Created Successfully added a custom attribute. 400 Bad Request The parameters of the requested operation are invalid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The project or folder does not exist. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (201)

id int The ID of the attribute. name string The name of the attribute. type enum:string The type of attribute. Possible values: string (text field), date , array (drop-list). arrayValues array: string A list of possible values for the attribute. Only relevant for drop-list attributes.

## Example

Successfully added a custom attribute.

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/docs/v1/projects/c0337487-5b66-422b-a284-c273b424af54/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.9g7HeA2wRqOxLlgLJ40UGQ/custom-attribute-definitions' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "name": "Drawing Type", "type": "array", "arrayValues": [ "Details", "General", "Plans", "Schedules" ] }'
```

### Response

```
{ "id" : 123 , "name" : "Drawing Type" , "type" : "array" , "arrayValues" : [ "Details" , "General" , "Plans" , "Schedules" ] }
```
