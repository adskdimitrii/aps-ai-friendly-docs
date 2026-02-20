# projects/{projectId}/items:next-custom-identifier

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-itemsnext-custom-identifier-GET/

---

# projects/{projectId}/items:next-custom-identifier

Retrieves the next available custom identifier for a submittal item in a project. The identifier is generated based on specific rules:

- Sequentially increments the last created itemâs number, relative to either the whole project for a global sequence or the specific spec for a spec sequence.

- Skips numbers already in use.

- Reuses deleted or cleared numbers.

- Increments digits appropriately, and manages leading zeros without increasing character count unless necessary.

For information about custom numbering in Submittals, see the Help documentation .

For details on using custom identifiers in the Submittal workflow, see the Create Submittal Item tutorial.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/items:next-custom-identifier Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Request

## Query String Parameters

specId string: UUID The item spec ID. This parameter is only required when the project is in spec sequence type (as opposed to global sequence). To verify the sequence type, call GET metadata , and check customIdentifierSequenceType . To get the spec ID, call GET specs , and select the relevant ID ( id ).

To verify the sequence type, call GET metadata , and check customIdentifierSequenceType .

To get the spec ID, call GET specs , and select the relevant ID ( id ).

### Response

## HTTP Status Code Summary

200 OK Details of the last created and the next available custom identifiers. 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request headers. 401 Unauthorized Invalid or missing authorization header. Verify the Bearer token and try again. 403 Forbidden The user is not authorized to perform this action. 404 Not Found The specified resource was not found. 500 Internal Server Error An unexpected error occurred on the server while processing the request.

### Response

## Body Structure (200)

previousCustomIdentifier string The last created custom identifier. nextCustomIdentifier string The next available custom identifier for the project.

## Example

Details of the last created and the next available custom identifiers.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/items:next-custom-identifier' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "previousCustomIdentifier" : "0001" , "nextCustomIdentifier" : "0002" }
```
