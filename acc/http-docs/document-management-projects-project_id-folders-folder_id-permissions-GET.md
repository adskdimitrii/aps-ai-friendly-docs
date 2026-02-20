# projects/{project_id}/folders/{folder_id}/permissions

Source: https://aps.autodesk.com/en/docs/acc/reference/http/document-management-projects-project_id-folders-folder_id-permissions-GET/

---

# projects/{project_id}/folders/{folder_id}/permissions

Retrieves information about the permissions assigned to users, roles and companies for a BIM 360 Document Management folder, including details about the name and the status.

For information about the different types of permissions you can assign to a user, role or company, see the Help documentation .

For more details about retrieving a userâs permissions, see the Retrieve Permissions tutorial.

If you are calling this endpoint on behalf of a user, the user needs to have VIEW permissions for the folder.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/bim360/docs/v1/projects/:project_id/folders/:folder_id/permissions Authentication Context user context optional Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. x-user-id string In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified.

### Request

## URI Parameters

project_id string: UUID The ID of the project. This corresponds to project ID in the Data Management API . To convert a project ID in the Data Management API into a project ID in the BIM 360 API you need to remove the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. folder_id string The ID (URN) of the folder. For details about how to find the URN, follow the initial steps (1-3) in the Download Files tutorial.

For details about how to find the URN, follow the initial steps (1-3) in the Download Files tutorial.

### Response

## HTTP Status Code Summary

200 OK Successfully retrieved a list of permissions 400 Bad Request Operation failed because of bad input 403 Forbidden The user does not have permission to perform this operation. 404 Not Found The project or folder does not exist 429 Too Many Requests The server has received too many requests. 500 Internal Server Error Operation failed because of an internal server error

### Response

## Body Structure (200)

subjectId string: UUID The ID of the user, role, or company. For example, this corresponds to the id , roleId , or companyId in the response for GET /users/user_id . autodeskId string The Autodesk ID of the user, role or company. name string The name of the user, role, or company. email string The userâs email. Only relevant if the subject is a user. userType enum:string The type of project user. Possible values: PROJECT_ADMIN or PROJECT_MEMBER . Only relevant if the subject is a user. subjectType enum:string The type of subject.
Possible values: USER , COMPANY , ROLE subjectStatus enum:string The status of the user, role, or company.
Possible values: For a user: INACTIVE , ACTIVE , PENDING , DISABLED For a role: INACTIVE , ACTIVE For a company: ACTIVE actions array: string Permitted actions for the user, role, or company.
The permission action group is different in BIM 360 Document Management and ACC Files. The six permission levels in BIM 360 Document Management correspond to one or more actions: View Only: VIEW , COLLABORATE View/Download: VIEW , DOWNLOAD , COLLABORATE Upload Only: PUBLISH View/Download+Upload: PUBLISH , VIEW , DOWNLOAD , COLLABORATE View/Download+Upload+Edit: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , EDIT Full controller: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , EDIT , CONTROL The six permission levels in ACC correspond to one or more actions: View Only: VIEW , COLLABORATE View/Download: VIEW , DOWNLOAD , COLLABORATE View/Download+PublishMarkups: VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP View/Download+PublishMarkups+Upload: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP View/Download+PublishMarkups+Upload+Edit: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP , EDIT Full controller: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP , EDIT , CONTROL See the BIM 360 Help documentation or the ACC Files Help documentation for more details about each permission group. Note that the full set of permissions assigned to the user, role, or company is a combination of actions and inheritActions . inheritActions array: string Permissions inherited by the user, role, or company from a higher level folder.
The permission action group is different in BIM 360 Document Management and ACC Files. The six permission levels in BIM 360 Document Management correspond to one or more actions: View Only: VIEW , COLLABORATE View/Download: VIEW , DOWNLOAD , COLLABORATE Upload Only: PUBLISH View/Download+Upload: PUBLISH , VIEW , DOWNLOAD , COLLABORATE View/Download+Upload+Edit: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , EDIT Full controller: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , EDIT , CONTROL The six permission levels in ACC correspond to one or more actions: View Only: VIEW , COLLABORATE View/Download: VIEW , DOWNLOAD , COLLABORATE View/Download+PublishMarkups: VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP View/Download+PublishMarkups+Upload: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP View/Download+PublishMarkups+Upload+Edit: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP , EDIT Full controller: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP , EDIT , CONTROL See the BIM 360 Help documentation or the ACC Files Help documentation for more details about each permission group. Note that the full set of permissions assigned to the user, role, or company is a combination of actions and inheritActions . Note that project administratorsâ permissions are non-inherited actions for the root folder, and inherited actions for all other folders.

- For a user: INACTIVE , ACTIVE , PENDING , DISABLED

- For a role: INACTIVE , ACTIVE

- For a company: ACTIVE

- The six permission levels in BIM 360 Document Management correspond to one or more actions: View Only: VIEW , COLLABORATE View/Download: VIEW , DOWNLOAD , COLLABORATE Upload Only: PUBLISH View/Download+Upload: PUBLISH , VIEW , DOWNLOAD , COLLABORATE View/Download+Upload+Edit: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , EDIT Full controller: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , EDIT , CONTROL

- View Only: VIEW , COLLABORATE

- View/Download: VIEW , DOWNLOAD , COLLABORATE

- Upload Only: PUBLISH

- View/Download+Upload: PUBLISH , VIEW , DOWNLOAD , COLLABORATE

- View/Download+Upload+Edit: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , EDIT

- Full controller: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , EDIT , CONTROL

- The six permission levels in ACC correspond to one or more actions: View Only: VIEW , COLLABORATE View/Download: VIEW , DOWNLOAD , COLLABORATE View/Download+PublishMarkups: VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP View/Download+PublishMarkups+Upload: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP View/Download+PublishMarkups+Upload+Edit: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP , EDIT Full controller: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP , EDIT , CONTROL

- View Only: VIEW , COLLABORATE

- View/Download: VIEW , DOWNLOAD , COLLABORATE

- View/Download+PublishMarkups: VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP

- View/Download+PublishMarkups+Upload: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP

- View/Download+PublishMarkups+Upload+Edit: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP , EDIT

- Full controller: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP , EDIT , CONTROL

See the BIM 360 Help documentation or the ACC Files Help documentation for more details about each permission group.

Note that the full set of permissions assigned to the user, role, or company is a combination of actions and inheritActions .

- The six permission levels in BIM 360 Document Management correspond to one or more actions: View Only: VIEW , COLLABORATE View/Download: VIEW , DOWNLOAD , COLLABORATE Upload Only: PUBLISH View/Download+Upload: PUBLISH , VIEW , DOWNLOAD , COLLABORATE View/Download+Upload+Edit: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , EDIT Full controller: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , EDIT , CONTROL

- View Only: VIEW , COLLABORATE

- View/Download: VIEW , DOWNLOAD , COLLABORATE

- Upload Only: PUBLISH

- View/Download+Upload: PUBLISH , VIEW , DOWNLOAD , COLLABORATE

- View/Download+Upload+Edit: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , EDIT

- Full controller: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , EDIT , CONTROL

- The six permission levels in ACC correspond to one or more actions: View Only: VIEW , COLLABORATE View/Download: VIEW , DOWNLOAD , COLLABORATE View/Download+PublishMarkups: VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP View/Download+PublishMarkups+Upload: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP View/Download+PublishMarkups+Upload+Edit: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP , EDIT Full controller: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP , EDIT , CONTROL

- View Only: VIEW , COLLABORATE

- View/Download: VIEW , DOWNLOAD , COLLABORATE

- View/Download+PublishMarkups: VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP

- View/Download+PublishMarkups+Upload: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP

- View/Download+PublishMarkups+Upload+Edit: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP , EDIT

- Full controller: PUBLISH , VIEW , DOWNLOAD , COLLABORATE , PUBLISH_MARKUP , EDIT , CONTROL

See the BIM 360 Help documentation or the ACC Files Help documentation for more details about each permission group.

Note that the full set of permissions assigned to the user, role, or company is a combination of actions and inheritActions .

Note that project administratorsâ permissions are non-inherited actions for the root folder, and inherited actions for all other folders.

## Example

Successfully retrieved a list of permissions

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/docs/v1/projects/c0337487-5b66-422b-a284-c273b424af54/folders/urn:adsk.wipprod:fs.folder:co.9g7HeA2wRqOxLlgLJ40UGQ/permissions' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
[ { "subjectId" : "684c4e47-7720-4961-b0e9-ff5966d82edb" , "autodeskId" : "45GPJ4KAX789" , "name" : "John Smith" , "email" : "john.smith@mail.com" , "userType" : "PROJECT_ADMIN" , "subjectType" : "USER" , "subjectStatus" : "ACTIVE" , "actions" : [ "PUBLISH" ], "inheritActions" : [ "PUBLISH" ] } ]
```
