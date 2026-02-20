# projects/{projectId}/items/{itemId}/steps

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-steps-GET/

---

# projects/{projectId}/items/{itemId}/steps

Retrieves a list of review steps associated with a specific submittal item.

Review steps represent sequential stages in the submittal review process. Each step contains one or more tasks, which assign responsibility for completing specific actions within that step. Tasks are tied to reviewers (represented in the UI as members, roles, or companies) and must be completed to progress to the next review step.

For a detailed overview of the submittal workflow, see the Manage Submittal Item Transitions tutorial .

For more information about submittals and their lifecycle, see the Help documentation .

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/items/:itemId/steps Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. itemId string The ID of the submittal item. To find the item ID, call GET items .

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Request

## Query String Parameters

limit int The maximum number of results per page. Possible values: 1 - 50 . Default value: 20 . For example, to limit the response to two results per page, use limit=2 . offset int The number of results to skip before starting to return data. For example, to skip the first 20 results, include offset=20 in the query string. For more details, see the JSON API Paging Help documentation .

### Response

## HTTP Status Code Summary

200 OK Review steps for the submittal item successfully retrieved. 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request headers. 401 Unauthorized Invalid or missing authorization header. Verify the Bearer token and try again. 403 Forbidden The user is not authorized to perform this action. 404 Not Found The specified resource was not found. 500 Internal Server Error An unexpected error occurred on the server while processing the request.

### Response

## Body Structure (200)

pagination object Describes pagination details for the response, including information about the current page and navigation to other pages. limit int The maximum number of results to be displayed on each page. offset int The number of results skipped before starting the current page. totalResults int The overall count of results available across all pages. previousUrl string The URL to retrieve the preceding page of results, if applicable. Not returned on the first page of results. nextUrl string The URL to retrieve the subsequent page of results, if available. If not included, this is the last page of data. results array: object Review steps associated with the specified submittal item. id string: UUID The internal, globally unique identifier (UUID) for the step. itemId string: UUID The ID of the item associated with the step. status enum:string The current status of the step. Possible values: not-started , in-progress , completed . stepNumber number The number representing the order of the steps, where 1 is the first step. daysToRespond number Specifies a dynamic due date. When the step starts, the due date is calculated based on this field. dueDate string The due date of the step in the format YYYY-MM-DD (ISO 8601) in UTC. For example, 2018-02-15 . tasks array: object The list of tasks associated with the step. id string: UUID The internal, globally unique identifier (UUID) for the task. stepId string: UUID The ID of the review step associated with the task. status enum:string The current status of the task. Possible values: not-started , in-progress , completed . assignedTo string The Autodesk ID or member group ID of the user , company , or role assigned to the task. assignedToType enum:string Specifies whether the task is assigned to a user, company, or role.
Possible values: 1 (user), 2 (company), 3 (role). isRequired boolean true : the task is required to complete the step. false : (default) the task is not required to complete the step. stepDueDate string The due date of the related step, formatted as YYYY-MM-DD (ISO 8601) in UTC. For example, 2025-01-20 . responseId string: UUID The ID of the response associated with the task, linking to the specific feedback or action taken. responseComment string The content of the response comment, providing feedback or instructions related to the task. respondedAt datetime: ISO 8601 The date and time when the response was added, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2025-01-20T12:00:00.198466Z . respondedBy string The Autodesk ID of the user who provided the response to the task. createdAt datetime: ISO 8601 The date and time when the task was originally created, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2025-01-20T12:00:00.198466Z . createdBy string The Autodesk ID of the user who created the task. updatedAt datetime: ISO 8601 The date and time when the task was last updated, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2025-01-20T12:00:00.198466Z . updatedBy string The Autodesk ID of the user who last updated the task. startedAt datetime: ISO 8601 The date and time when the related step was marked as started ( In Progress ), formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2025-01-20T12:00:00.198466Z . completedAt datetime: ISO 8601 The date and time when the task was completed, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2025-01-20T12:00:00.198466Z . completedBy string The Autodesk ID of the user who completed the task. permittedActions array: object A list of actions that the user is allowed to perform on the task within the submittal workflow. id string The ID of the action in the format type_of_object::action . For example, partial_update . fields object A mapping of field names to lists of possible values for each field. Note that an empty array indicates that there is no specific set of values for those fields. mandatoryFields array: string Fields required to perform specific actions, such as closing a task. The required fields depend on the userâs role and the action. transitions array: string Not relevant createdAt datetime: ISO 8601 The date and time when the step was created, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2025-01-20T12:00:00.198466Z . createdBy string The Autodesk ID of the user that created the step. updatedAt datetime: ISO 8601 The date and time when the step was last updated, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2025-01-20T12:00:00.198466Z . updatedBy string The Autodesk ID of the user that updated the step. startedAt datetime: ISO 8601 The date and time when the step transitioned to In Progress in the backend. This corresponds to the step being marked as Started in the UI, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2025-01-20T12:00:00.198466Z . completedAt datetime: ISO 8601 The date and time when the step was completed, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2025-01-20T12:00:00.198466Z . permittedActions array: object A list of actions that the user is allowed to perform on the step. id string The ID of the action in the format type_of_object::action . For example, Step::partial_update . fields object A mapping of field names to lists of possible values for each field. If a field does not require a specific value, it will be returned as an empty array. mandatoryFields array: string A list of fields required to perform specific actions on a step, such as tasks for the Step::partial_update action. The required fields depend on the userâs role and the action. transitions array: string Not relevant

false : (default) the task is not required to complete the step.

## Example

Review steps for the submittal item successfully retrieved.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/items/767b5888-2c6a-413d-8487-613966dd64ce/steps' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "pagination" : { "limit" : 10 , "offset" : 100 , "totalResults" : 25 , "previousUrl" : "https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/items/767b5888-2c6a-413d-8487-613966dd64ce/steps?limit=5&offset=10" , "nextUrl" : null }, "results" : [ { "id" : "84eb33cd-4a42-42b7-95dd-3900035c3407" , "itemId" : "2df3b4cf-16f4-496e-8173-7125f31e3dd1" , "status" : "in-progress" , "stepNumber" : 1 , "daysToRespond" : 10 , "dueDate" : "2024-02-15" , "tasks" : [ { "id" : "4d539b8f-c522-4f1c-9743-d7fdfa9e9c9e" , "stepId" : "d6635799-e973-4c9c-80d8-fb4b3591ef6b" , "status" : "completed" , "assignedTo" : "WD43ZJGKDFLFH" , "assignedToType" : "1" , "isRequired" : true , "stepDueDate" : "2024-02-15" , "responseId" : "2d46d30b-7dc1-4a65-991d-d739a1381eb8" , "responseComment" : "Approved without changes." , "respondedAt" : "2024-02-03T12:09:24.198466Z" , "respondedBy" : "WD43ZJGKDFLFH" , "createdAt" : "2024-03-21T23:04:49.406Z" , "createdBy" : "WD43ZJGKDFLFH" , "updatedAt" : "2024-03-24T23:04:49.406674Z" , "updatedBy" : "WD43ZJGKDFLFH" , "startedAt" : "2024-03-21T23:15:49.406894Z" , "completedAt" : "2024-03-24T23:04:49.4066344Z" , "completedBy" : "WD43ZJGKDFLFH" , "permittedActions" : [ { "id" : "Task::partial_update" , "fields" : { "responseComment" : [], "responseId" : [] }, "mandatoryFields" : [ "responseId" ], "transitions" : [ "" ] } ] } ], "createdAt" : "2024-03-21T23:04:49.406Z" , "createdBy" : "WD43ZJGKDFLFH" , "updatedAt" : "2024-03-24T23:04:49.406Z" , "updatedBy" : "WD43ZJGKDFLFH" , "startedAt" : "2024-03-21T23:15:49.406Z" , "completedAt" : "2024-03-24T23:04:49.406Z" , "permittedActions" : [ { "id" : "Step::overwrite_step" , "fields" : { "tasks" : [] }, "mandatoryFields" : [ "tasks" ], "transitions" : [ "" ] } ] } ] }
```
