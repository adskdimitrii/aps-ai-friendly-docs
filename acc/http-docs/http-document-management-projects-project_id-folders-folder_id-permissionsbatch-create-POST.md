# projects/{project_id}/folders/{folder_id}/permissions:batch-create

Source: https://aps.autodesk.com/en/docs/acc/reference/http/document-management-projects-project_id-folders-folder_id-permissionsbatch-create-POST/

---

Permissions (beta)

POST

# projects/{project_id}/folders/{folder_id}/permissions:batch-create

Assign permissions to multiple users, roles, and companies for a [BIM 360 Document Management](https://docs.b360.autodesk.com/) folder.

For more information about folder permissions, see the [BIM 360 Help documentation](http://help.autodesk.com/view/BIM360D/ENU/?guid=GUID-2643FEEF-B48A-45A1-B354-797DAD628C37) or the [ACC Files Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Folder_Permissions).

For details about updating a userâs permissions, see the [Update a Userâs Folder Permissions](/en/docs/bim360/v1/tutorials/update-permissions/) tutorial.

If you are calling this endpoint on behalf of a user, the user needs to have `CONTROL` permissions for the folder.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/bim360/docs/v1/projects/:project_id/folders/:folder_id/permissions:batch-create |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| x-user-id   string | In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| project_id   string: UUID | The ID of the project. This corresponds to project ID in the [Data Management API](/en/docs/data/v2/). To convert a project ID in the Data Management API into a project ID in the BIM 360 API you need to remove the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |
| folder_id   string | The ID (URN) of the folder. <br>For details about how to find the URN, follow the initial steps (1-3) in the [Download Files](/en/docs/bim360/v1/tutorials/document-management/download-document-s3/) tutorial. |

### Request

## [Body Structure](#body-structure)

A list of permission items to create in this folder.

| subjectId*   string: UUID | The ID of the user, role, or company. To verify the subjectId: <br>For a user, use [GET users](/en/docs/bim360/v1/reference/http/admin-v1-projects-projectId-users-GET).For a role, use [GET roles](/en/docs/bim360/v1/reference/http/projects-project_id-industry_roles-GET)For a company, use [GET companies](/en/docs/bim360/v1/reference/http/projects-:project_id-companies-GET) |
| --- | --- |
| autodeskId   string | The Autodesk ID of the user, role or company. |
| subjectType*   enum:string | The type of subject. Possible values: `USER`, `COMPANY`, `ROLE` |
| actions*   array: string | Permitted actions for the user, role, or company. The permission action group is different in BIM 360 Document Management and ACC Build Files. <br>The six permission levels in BIM 360 Document Management correspond to one or more actions: <br>  View Only: `VIEW`, `COLLABORATE`  View/Download: `VIEW`, `DOWNLOAD`, `COLLABORATE`  Upload Only: `PUBLISH`  View/Download+Upload: `PUBLISH`, `VIEW`, `DOWNLOAD`, `COLLABORATE`  View/Download+Upload+Edit: `PUBLISH`, `VIEW`, `DOWNLOAD`, `COLLABORATE`, `EDIT`  Full controller: `PUBLISH`, `VIEW`, `DOWNLOAD`, `COLLABORATE`, `EDIT`, `CONTROL` The six permission levels in Autodesk Construction Cloud correspond to one or more actions: <br>  View Only: `VIEW`, `COLLABORATE`  View/Download: `VIEW`, `DOWNLOAD`, `COLLABORATE`  View/Download+PublishMarkups: `VIEW`, `DOWNLOAD`, `COLLABORATE`, `PUBLISH_MARKUP`  View/Download+PublishMarkups+Upload: `PUBLISH`, `VIEW`, `DOWNLOAD`, `COLLABORATE`, `PUBLISH_MARKUP`  View/Download+PublishMarkups+Upload+Edit: `PUBLISH`, `VIEW`, `DOWNLOAD`, `COLLABORATE`, `PUBLISH_MARKUP`, `EDIT`  Full controller: `PUBLISH`, `VIEW`, `DOWNLOAD`, `COLLABORATE`, `PUBLISH_MARKUP`, `EDIT`, `CONTROL` <br>See the [BIM 360 Help documentation](http://help.autodesk.com/view/BIM360D/ENU/?guid=GUID-2643FEEF-B48A-45A1-B354-797DAD628C37) or the [ACC Files Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Folder_Permissions) for more details about each permission level.<br>Note that the full set of permissions assigned to the user, role, or company is a combination of `actions` and `inheritActions`. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully created permissions |
| --- | --- |
| 400   Bad Request | Operation failed because of bad input |
| 403   Forbidden | The user does not have permission to perform this operation. |
| 404   Not Found | The project or folder does not exist |
| 422   Unprocessable Entity | The payload contains unprocessable data |
| 423   Locked | The folder is temporarily inaccessible because it is being used by another operation. |
| 429   Too Many Requests | The server has received too many requests. |
| 500   Internal Server Error | Operation failed because of an internal server error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The results object. |
| --- | --- |
| subjectId   string: UUID | The ID of the user, role, or company. For example, this corresponds to the `id`, `roleId`, or `companyId` in the response for [GET /users/user_id](/en/docs/bim360/v1/reference/http/admin-v1-projects-projectId-users-userId-GET/). |
| subjectType   enum:string | The type of subject. Possible values: `USER`, `COMPANY`, `ROLE` |
| actions   array: string | Permitted actions for the user, role, or company. The permission action group is different in BIM 360 Document Management and ACC Build Files. <br>The six permission levels in BIM 360 Document Management correspond to one or more actions: <br>  View Only: `VIEW`, `COLLABORATE`  View/Download: `VIEW`, `DOWNLOAD`, `COLLABORATE`  Upload Only: `PUBLISH`  View/Download+Upload: `PUBLISH`, `VIEW`, `DOWNLOAD`, `COLLABORATE`  View/Download+Upload+Edit: `PUBLISH`, `VIEW`, `DOWNLOAD`, `COLLABORATE`, `EDIT`  Full controller: `PUBLISH`, `VIEW`, `DOWNLOAD`, `COLLABORATE`, `EDIT`, `CONTROL` The six permission levels in Autodesk Construction Cloud correspond to one or more actions: <br>  View Only: `VIEW`, `COLLABORATE`  View/Download: `VIEW`, `DOWNLOAD`, `COLLABORATE`  View/Download+PublishMarkups: `VIEW`, `DOWNLOAD`, `COLLABORATE`, `PUBLISH_MARKUP`  View/Download+PublishMarkups+Upload: `PUBLISH`, `VIEW`, `DOWNLOAD`, `COLLABORATE`, `PUBLISH_MARKUP`  View/Download+PublishMarkups+Upload+Edit: `PUBLISH`, `VIEW`, `DOWNLOAD`, `COLLABORATE`, `PUBLISH_MARKUP`, `EDIT`  Full controller: `PUBLISH`, `VIEW`, `DOWNLOAD`, `COLLABORATE`, `PUBLISH_MARKUP`, `EDIT`, `CONTROL` <br>See the [BIM 360 Help documentation](http://help.autodesk.com/view/BIM360D/ENU/?guid=GUID-2643FEEF-B48A-45A1-B354-797DAD628C37) or the [ACC Files Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Folder_Permissions) for more details about each permission level.<br>Note that the full set of permissions assigned to the user, role, or company is a combination of `actions` and `inheritActions`. |

## [Example](#example)

Successfully created permissions

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/docs/v1/projects/c0337487-5b66-422b-a284-c273b424af54/folders/urn:adsk.wipprod:fs.folder:co.9g7HeA2wRqOxLlgLJ40UGQ/permissions:batch-create' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '[
        {
          "subjectId": "684c4e47-7720-4961-b0e9-ff5966d82edb",
          "autodeskId": "45GPJ4KAX789",
          "subjectType": "USER",
          "actions": [
            "PUBLISH"
          ]
        }
      ]'

```

Show More

### Response

```
{
  "results": [
    {
      "subjectId": "684c4e47-7720-4961-b0e9-ff5966d82edb",
      "subjectType": "USER",
      "actions": [
        "PUBLISH"
      ]
    }
  ]
}

```

Show More
