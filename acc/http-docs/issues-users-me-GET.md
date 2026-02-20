# users/me

Source: https://aps.autodesk.com/en/docs/acc/reference/http/issues-users-me-GET/

---

# users/me

Returns the current user permissions.

Note that if a user with View and assign issues for their company permissions attempts to assign a user from a another company to the issue, it will return an error.
You can verify a userâs assignment permissions by checking the permittedActions or permissionLevels attributes.

This operation is available to everyone.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/issues/v1/projects/{projectId}/users/me Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. x-ads-region string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA .

For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request Invalid input 403 Forbidden Unauthorized 404 Not Found Project not found 500 Internal Server Error Internal server error

### Response

## Body Structure (200)

id string The userâs Autodesk ID. isProjectAdmin boolean States whether the current logged in user is a system admin. canManageTemplates boolean Not relevant issues object new object If this object appears in the response, it indicates that the user can create and modify issues. permittedActions array: string The list of actions permitted for the user for this issue in its current state. Possible Values: assign_all (can assign another user from another company to the issue), assign_same_company (can only assign another user from the same company to the issue), clear_assignee , delete , add_comment , add_attachment , remove_attachment . The following values are not relevant: add_attachment , remove_attachment . permittedAttributes array: string A list of attributes you are allowed to open a new issue. issueTypeId , linkedDocument , links , ownerId , officialResponse , rootCauseId , snapshotUrn are not applicable. Possible Values: title , description , issueTypeId , issueSubtypeId , status , assignedTo , assignedToType , dueDate , locationId , locationDetails , linkedDocuments , links , ownerId , rootCauseId , officialResponse , customAttributes , snapshotUrn , startDate , published , deleted , watchers . permittedStatuses array: string A list of available statuses for the project. Possible values: draft , open , pending , in_progress , completed , in_review , not_approved , in_dispute , closed . For more information about statuses, see the Help documentation . permitted_actions array: string Not relevant permitted_attributes array: string Not relevant permitted_statuses array: string Not relevant filter object Not relevant permittedStatuses array: string Not relevant permissionLevels array: string The permission level of the user. Each permission level corresponds to a combination of values in the response. For example, a combination of read and create in the response, corresponds to a Full visibility permission level. Note that if a user with View and assign issues for their company permissions attempts to assign a user from a another company to the issue, it will return an error. In addition, the user can both create and view issues for their own company. You can also verify a userâs assignment permissions by checking the permittedActions or permissionLevels attributes. Edit, view, and assign This permission level is split into two sub-levels: View and assign to their company (previously known as Create for my company ) : create and the permittedActions array must include assign-same-company View issues for their company. Assign issues to anyone. : create and the permittedActions array must include assign-all Full visibility (previously known as Create for other companies ): create , read Manage issues : create , read , write Possible values: create , read , write . For more details about the permission levels, see Issues Permissions .

Possible Values: assign_all (can assign another user from another company to the issue), assign_same_company (can only assign another user from the same company to the issue), clear_assignee , delete , add_comment , add_attachment , remove_attachment .

The following values are not relevant: add_attachment , remove_attachment .

Possible Values: title , description , issueTypeId , issueSubtypeId , status , assignedTo , assignedToType , dueDate , locationId , locationDetails , linkedDocuments , links , ownerId , rootCauseId , officialResponse , customAttributes , snapshotUrn , startDate , published , deleted , watchers .

Possible values: draft , open , pending , in_progress , completed , in_review , not_approved , in_dispute , closed .

For more information about statuses, see the Help documentation .

Note that if a user with View and assign issues for their company permissions attempts to assign a user from a another company to the issue, it will return an error. In addition, the user can both create and view issues for their own company. You can also verify a userâs assignment permissions by checking the permittedActions or permissionLevels attributes.

- Edit, view, and assign This permission level is split into two sub-levels: View and assign to their company (previously known as Create for my company ) : create and the permittedActions array must include assign-same-company View issues for their company. Assign issues to anyone. : create and the permittedActions array must include assign-all

- View and assign to their company (previously known as Create for my company ) : create and the permittedActions array must include assign-same-company

- View issues for their company. Assign issues to anyone. : create and the permittedActions array must include assign-all

- Full visibility (previously known as Create for other companies ): create , read

- Manage issues : create , read , write

Possible values: create , read , write .

For more details about the permission levels, see Issues Permissions .

## Example

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/:projectId/users/me' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "id" : "BXQXL7646C2R" , "isProjectAdmin" : true , "canManageTemplates" : "" , "issues" : { "new" : { "permittedActions" : [ "add_comment" ], "permittedAttributes" : [ "title" ], "permittedStatuses" : [ "draft" , "open" , "pending" , "in_progress" , "completed" , "in_review" , "not_approved" , "in_dispute" , "closed" ], "permitted_actions" : [ "add_comment" ], "permitted_attributes" : [ "title" ], "permitted_statuses" : [ "open" ] }, "filter" : { "permittedStatuses" : [ "draft" , "open" , "pending" , "in_progress" , "completed" , "in_review" , "not_approved" , "in_dispute" , "closed" ] } }, "permissionLevels" : [ "read" ] }
```
