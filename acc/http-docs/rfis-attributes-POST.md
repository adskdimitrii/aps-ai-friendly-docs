# custom-attributes

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-attributes-POST/

---

# custom-attributes

Creates a custom attribute definition for a project.

Use this endpoint to add a new attribute that can be included when creating or updating RFIs.

For more information on setting up custom attributes, see the Custom RFI Fields help topic.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/attributes Authentication Context user context required Required OAuth Scopes data:write data:create Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json

### Request

## URI Parameters

projectId string The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Request

## Body Structure

name * string The name of the custom attribute as displayed in the UI. Max length: 50 type * enum:string The type of the attribute.
Possible values: text , numeric description string The description of the attribute as shown in the UI. Max length: 1000 status * enum:string The display status of the attribute in the UI. Possible values: active , inactive , hidden . multipleChoice boolean true : users can select more than one value for this attribute. false : (default) users can select only one value. possibleValues array: object A list of possible values for the attribute. id string: UUID The unique ID of the attribute value. name * string,integer,null The name of the attribute value as shown in the UI. Max length: 100

Max length: 50

Max length: 1000

false : (default) users can select only one value.

Max length: 100

### Response

## HTTP Status Code Summary

201 Created Created 400 Bad Request The parameters are invalid 401 Unauthorized The provided bearer token is not valid 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation 500 Internal Server Error An unknown error occurred on the server

### Response

## Body Structure (201)

id string: UUID The ID of the custom attribute definition. name string The name of the custom attribute as displayed in the UI. Max length: 50 type enum:string The type of the attribute.
Possible values: text , numeric description string The description of the attribute as shown in the UI. Max length: 1000 status enum:string The display status of the attribute in the UI. Possible values: active , inactive , hidden . multipleChoice boolean true : users can select more than one value for this attribute. false : (default) users can select only one value. possibleValues array: object A list of possible values for the attribute. id string: UUID The unique ID of the attribute value. name string,integer,null The name of the attribute value as shown in the UI. Max length: 100

Max length: 50

Max length: 1000

false : (default) users can select only one value.

Max length: 100

## Example

Created

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/attributes' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "name": "Attribute 1", "type": "text", "description": "This is a description of the attribute", "status": "active", "multipleChoice": false, "possibleValues": [ { "id": "c911852d-5957-4145-9c8d-e7cfe9d564df", "name": "Value 1" } ] }'
```

### Response

```
{ "id" : "c911852d-5957-4145-9c8d-e7cfe9d564df" , "name" : "Attribute 1" , "type" : "text" , "description" : "This is a description of the attribute" , "status" : "active" , "multipleChoice" : false , "possibleValues" : [ { "id" : "c911852d-5957-4145-9c8d-e7cfe9d564df" , "name" : "Value 1" } ] }
```
