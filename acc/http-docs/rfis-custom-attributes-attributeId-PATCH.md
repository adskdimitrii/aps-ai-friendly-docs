# custom-attributes/:attributeId

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-custom-attributes-attributeId-PATCH/

---

# custom-attributes/:attributeId

Updates an existing custom attribute definition for a project.

Use this endpoint to change the attributeâs name, description, status, or possible values.
The attribute can be used when creating or updating RFIs.

For more information on custom attributes, see the Custom RFI Fields help topic.

## Resource Information

Method and URI PATCH https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/attributes/:attributeId Authentication Context user context required Required OAuth Scopes data:write data:create Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json

### Request

## URI Parameters

projectId string The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. attributeId string The ID of the custom attribute.

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Request

## Body Structure

name string The name of the custom attribute as displayed in the UI. Max length: 50 description string The description of the attribute as shown in the UI. Max length: 1000 status enum:string The display status of the attribute in the UI. Possible values: active , inactive , hidden . multipleChoice boolean true : users can select more than one value for this attribute. false : (default) users can select only one value. possibleValues object Updates the list of possible values for the attribute. To overwrite an existing possible value, specify both newAttributes (the new value name) and deletedAttributes (the ID of the value to remove). newAttributes array: string,null Adds new possible values to the attribute. Each item is the name of a new possible value as shown in the UI. updatedAttributes array: object Updates the names of existing possible values. id string: UUID The unique ID of the attribute value. name * string,integer,null The name of the attribute value as shown in the UI. Max length: 100 deletedAttributes array: string Deletes possible values from the attribute. Each item is the ID of a possible value to delete.

Max length: 50

Max length: 1000

false : (default) users can select only one value.

To overwrite an existing possible value, specify both newAttributes (the new value name) and deletedAttributes (the ID of the value to remove).

Each item is the name of a new possible value as shown in the UI.

Max length: 100

### Response

## HTTP Status Code Summary

200 OK Updated 400 Bad Request The parameters are invalid 401 Unauthorized The provided bearer token is not valid 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation 500 Internal Server Error An unknown error occurred on the server

### Response

## Body Structure (200)

id string: UUID The ID of the custom attribute definition. name string The name of the custom attribute as displayed in the UI. Max length: 50 type enum:string The type of the attribute.
Possible values: text , numeric description string The description of the attribute as shown in the UI. Max length: 1000 status enum:string The display status of the attribute in the UI. Possible values: active , inactive , hidden . multipleChoice boolean true : users can select more than one value for this attribute. false : (default) users can select only one value. possibleValues array: object A list of possible values for the attribute. id string: UUID The unique ID of the attribute value. name string,integer,null The name of the attribute value as shown in the UI. Max length: 100

Max length: 50

Max length: 1000

false : (default) users can select only one value.

Max length: 100

## Example

Updated

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/attributes/:attributeId' \ -X 'PATCH' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "name": "Attribute 1", "description": "This is a description of the attribute", "status": "active", "multipleChoice": false, "possibleValues": { "newAttributes": [ "Plaster" ], "updatedAttributes": [ { "id": "c911852d-5957-4145-9c8d-e7cfe9d564df", "name": "Value 1" } ], "deletedAttributes": [ "3ff28f60-33ae-4b90-a55f-53ab305c9591" ] } }'
```

### Response

```
{ "id" : "c911852d-5957-4145-9c8d-e7cfe9d564df" , "name" : "Attribute 1" , "type" : "text" , "description" : "This is a description of the attribute" , "status" : "active" , "multipleChoice" : false , "possibleValues" : [ { "id" : "c911852d-5957-4145-9c8d-e7cfe9d564df" , "name" : "Value 1" } ] }
```
