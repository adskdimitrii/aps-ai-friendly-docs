# projects/{projectId}/items/{itemId}/steps/{stepId}/tasks/{taskId}:close

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-tasks-taskIdclose-POST/

---

# projects/{projectId}/items/{itemId}/steps/{stepId}/tasks/{taskId}:close

Closes a task by adding a required review response, marking it as complete within the submittal review workflow. This action updates the taskâs status and, when the last required task in a review step is closed, transitions the submittal item to the next step in the workflow. Note that the ability to close a task depends on the userâs permitted actions, which can be retrieved by calling GET Item/:id to check available transitions.

The submittal item progresses to the Close and distribute state only after all review steps and required tasks are completed. Note that closing a task corresponds to adding a review in the UI.

For a detailed overview of the submittal workflow, see the Manage Submittal Item Transitions tutorial .

For more information about submittals and their lifecycle, see the Help documentation .

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/items/:itemId/steps/:stepId/tasks/:taskId:close Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. itemId string The ID of the submittal item. To find the item ID, call GET items . stepId string The ID of the review step associated with the submittal item. To find the step ID, call GET steps . taskId string The ID of the task. To get the task ID, call GET tasks .

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Request

## Body Structure

responseId * string The ID of the response associated with the task, linking to the specific feedback or action taken. To retrieve this ID, call GET responses . responseComment string The body of the response comment, containing feedback or instructions related to the task. saveAttachmentDrafts array: string Not relevant duplicateAttachments array: string A list of attachment IDs to duplicate from a submittal itemâs previous stage in the workflow. To retrieve available attachments, call GET items/:itemId/attachments .

### Response

## HTTP Status Code Summary

200 OK Task successfully closed. 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request headers. 401 Unauthorized Invalid or missing authorization header. Verify the Bearer token and try again. 403 Forbidden The user is not authorized to perform this action. 404 Not Found The specified resource was not found. 500 Internal Server Error An unexpected error occurred on the server while processing the request.

### Response

## Body Structure (200)

id string: UUID The internal, globally unique identifier (UUID) for the task. stepId string: UUID The ID of the review step associated with the task. status enum:string The current status of the task. Possible values: not-started , in-progress , completed . assignedTo string The Autodesk ID or member group ID of the user , company , or role assigned to the task. assignedToType enum:string Specifies whether the task is assigned to a user, company, or role.
Possible values: 1 (user), 2 (company), 3 (role). isRequired boolean true : the task is required to complete the step. false : (default) the task is not required to complete the step. stepDueDate string The due date of the related step, formatted as YYYY-MM-DD (ISO 8601) in UTC. For example, 2025-01-20 . responseId string: UUID The ID of the response associated with the task, linking to the specific feedback or action taken. responseComment string The content of the response comment, providing feedback or instructions related to the task. respondedAt datetime: ISO 8601 The date and time when the response was added, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2025-01-20T12:00:00.198466Z . respondedBy string The Autodesk ID of the user who provided the response to the task. createdAt datetime: ISO 8601 The date and time when the task was originally created, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2025-01-20T12:00:00.198466Z . createdBy string The Autodesk ID of the user who created the task. updatedAt datetime: ISO 8601 The date and time when the task was last updated, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2025-01-20T12:00:00.198466Z . updatedBy string The Autodesk ID of the user who last updated the task. startedAt datetime: ISO 8601 The date and time when the related step was marked as started ( In Progress ), formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2025-01-20T12:00:00.198466Z . completedAt datetime: ISO 8601 The date and time when the task was completed, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2025-01-20T12:00:00.198466Z . completedBy string The Autodesk ID of the user who completed the task. permittedActions array: object A list of actions that the user is allowed to perform on the task within the submittal workflow. id string The ID of the action in the format type_of_object::action . For example, partial_update . fields object A mapping of field names to lists of possible values for each field. Note that an empty array indicates that there is no specific set of values for those fields. mandatoryFields array: string Fields required to perform specific actions, such as closing a task. The required fields depend on the userâs role and the action. transitions array: string Not relevant

false : (default) the task is not required to complete the step.

## Example

Task successfully closed.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/items/767b5888-2c6a-413d-8487-613966dd64ce/steps/b79059cc-611b-4769-80b7-f8db9a2dfcdf/tasks/f2bc8b34-7e95-4317-b298-0ed80c3eba6d:close' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "responseId": "2d46d30b-7dc1-4a65-991d-d739a1381eb8", "responseComment": "Approved without changes.", "saveAttachmentDrafts": [ "" ], "duplicateAttachments": [ "f572d479-ede1-4654-a895-f669c2639b26", "06b3d2b0-bd5a-4aa2-b35f-4ae55fe8fd5d" ] }'
```

### Response

```
{ "id" : "4d539b8f-c522-4f1c-9743-d7fdfa9e9c9e" , "stepId" : "d6635799-e973-4c9c-80d8-fb4b3591ef6b" , "status" : "completed" , "assignedTo" : "WD43ZJGKDFLFH" , "assignedToType" : "1" , "isRequired" : true , "stepDueDate" : "2024-02-15" , "responseId" : "2d46d30b-7dc1-4a65-991d-d739a1381eb8" , "responseComment" : "Approved without changes." , "respondedAt" : "2024-02-03T12:09:24.198466Z" , "respondedBy" : "WD43ZJGKDFLFH" , "createdAt" : "2024-03-21T23:04:49.406Z" , "createdBy" : "WD43ZJGKDFLFH" , "updatedAt" : "2024-03-24T23:04:49.406674Z" , "updatedBy" : "WD43ZJGKDFLFH" , "startedAt" : "2024-03-21T23:15:49.406894Z" , "completedAt" : "2024-03-24T23:04:49.4066344Z" , "completedBy" : "WD43ZJGKDFLFH" , "permittedActions" : [ { "id" : "Task::partial_update" , "fields" : { "responseComment" : [], "responseId" : [] }, "mandatoryFields" : [ "responseId" ], "transitions" : [ "" ] } ] }
```
