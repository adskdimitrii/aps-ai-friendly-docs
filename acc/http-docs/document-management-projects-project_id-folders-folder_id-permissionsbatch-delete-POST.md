# projects/{project_id}/folders/{folder_id}/permissions:batch-delete

Source: https://aps.autodesk.com/en/docs/acc/reference/http/document-management-projects-project_id-folders-folder_id-permissionsbatch-delete-POST/

---

# projects/{project_id}/folders/{folder_id}/permissions:batch-delete

Deletes all the permissions assigned to specified users, roles, and companies. To remove some of the permissions assigned to users, roles, and companies, use the Update permissions endpoint.

Note that you cannot delete permission for project admins, who are always assigned full permissions.

For more information about folder permissions, see the BIM 360 Help documentation or the ACC Files Help documentation .

In addition to the permissions that were assigned to the user for this folder, the user also inherits permissions from any parent folder. After deleting permissions for the folder, the user will still continue to have permissions that were inherited from any parent folder. In order to completely delete the userâs permissions, you need to also delete the userâs permissions from all parent folders.

Note that in addition to inherited permissions, the user might also have been assigned permissions for the folder if a company or roles were assigned to both the user and the folder. To check which company and roles were assigned to the user, call GET /users/user_id . To check which roles and companies were assigned to the folder, call GET permissions . To remove the copmpany or roles permissions for the user from the folder, either remove the company or roles from the folder by calling this endpoint, or remove the company or roles from the user using PATCH /users/user_id .

If you are calling this endpoint on behalf of a user, the user needs to have CONTROL permissions for the folder.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/bim360/docs/v1/projects/:project_id/folders/:folder_id/permissions:batch-delete Authentication Context user context optional Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. Content-Type * string Must be application/json x-user-id string In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified.

### Request

## URI Parameters

project_id string: UUID The ID of the project. This corresponds to project ID in the Data Management API . To convert a project ID in the Data Management API into a project ID in the BIM 360 API you need to remove the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. folder_id string The ID (URN) of the folder. For details about how to find the URN, follow the initial steps (1-3) in the Download Files tutorial.

For details about how to find the URN, follow the initial steps (1-3) in the Download Files tutorial.

### Request

## Body Structure

A list of permission items to delete in this folder.

subjectId string: UUID The ID of the user, role, or company. To verify the subjectId of the user, role, or company, use GET permissions . autodeskId string The Autodesk ID of the user, role or company. subjectType enum:string The type of subject.
Possible values: USER , COMPANY , ROLE

### Response

## HTTP Status Code Summary

200 OK Successfully deleted permissions 400 Bad Request Operation failed because of bad input 403 Forbidden The user does not have permission to perform this operation. 404 Not Found The project or folder does not exist 429 Too Many Requests The server has received too many requests. 500 Internal Server Error Operation failed because of an internal server error

### Response

## Body Structure (200)

Response for 200 has no body.

## Example

Successfully deleted permissions

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/docs/v1/projects/c0337487-5b66-422b-a284-c273b424af54/folders/urn:adsk.wipprod:fs.folder:co.9g7HeA2wRqOxLlgLJ40UGQ/permissions:batch-delete' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '[ { "subjectId": "684c4e47-7720-4961-b0e9-ff5966d82edb", "autodeskId": "45GPJ4KAX789", "subjectType": "USER" } ]'
```

### Response
