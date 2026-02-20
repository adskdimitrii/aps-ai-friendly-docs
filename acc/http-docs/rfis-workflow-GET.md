# workflow

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-workflow-GET/

---

# workflow

Retrieves the workflow configuration for a given project, including the workflow type, description, and the mapping between project roles and their permitted assignees.

This endpoint helps clients understand which users, companies, or roles are allowed to participate in specific workflow actions within a project.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/workflow Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

projectId string The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Response

## HTTP Status Code Summary

200 OK OK 400 Bad Request The parameters are invalid 401 Unauthorized The provided bearer token is not valid 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation 500 Internal Server Error An unknown error occurred on the server

### Response

## Body Structure (200)

workflowType enum:string The region type of the workflow. Possible values: US , EU . description string A description of the workflow projectRolesMapping array: object A list of project roles and their corresponding permitted assignees. name string The name of the project role permittedAssignees array: object A list of users, companies, or roles that can be assigned to this project role. id string The Autodesk ID of the user, company, or role. To find details about users, call GET users , to find details about companies, call GET companies . Note that we do not currently support finding details about roles for a project. type enum:string The type of assignee. Possible values: user , company , role .

To find details about users, call GET users , to find details about companies, call GET companies .

Note that we do not currently support finding details about roles for a project.

## Example

OK

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/workflow' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "workflowType" : "US" , "description" : "Support for RFI creation. Review and response with Creator, Manager and Reviewer workflow roles." , "projectRolesMapping" : [ { "name" : "projectGC" , "permittedAssignees" : [ { "id" : "PER8KQPK2JRT" , "type" : "user" } ] } ] }
```
