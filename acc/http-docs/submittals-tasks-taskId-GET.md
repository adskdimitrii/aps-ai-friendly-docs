# projects/{projectId}/items/{itemId}/steps/{stepId}/tasks/{taskId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-tasks-taskId-GET/

---

Tasks

GET

# projects/{projectId}/items/{itemId}/steps/{stepId}/tasks/{taskId}

Retrieves details of a specific task associated with a review step in a submittal item. A task represents the assignment of responsibility for completing a specific step in the review process. Tasks may correspond to a reviewer, such as an individual user (Member), a role, or a company.

To learn more about using this endpoint within the submittal workflow, see the [Process Submittal Items tutorial](/en/docs/acc/v1/tutorials/submittals/submittal-transitions.rst.rst/).

For more information about submittals and their lifecycle, see the [Process Submittal Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Process_Submittal).

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/items/:itemId/steps/:stepId/tasks/:taskId |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |
| itemId   string | The ID of the submittal item. To find the item ID, call [GET items](/en/docs/acc/v1/reference/http/submittals-items-GET/). |
| stepId   string | The ID of the review step associated with the submittal item. To find the step ID, call [GET steps](/en/docs/acc/v1/reference/http/submittals-steps-GET/). |
| taskId   string | The ID of the task. To get the task ID, call [GET tasks](/en/docs/acc/v1/reference/http/submittals-tasks-GET/). |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Task details successfully retrieved. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. |
| 401   Unauthorized | Invalid or missing authorization header. Verify the Bearer token and try again. |
| 403   Forbidden | The user is not authorized to perform this action. |
| 404   Not Found | The specified resource was not found. |
| 500   Internal Server Error | An unexpected error occurred on the server while processing the request. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| id   string: UUID | The internal, globally unique identifier (UUID) for the task. |
| --- | --- |
| stepId   string: UUID | The ID of the review step associated with the task. |
| status   enum:string | The current status of the task. Possible values: `not-started`, `in-progress`, `completed`. |
| assignedTo   string | The Autodesk ID or member group ID of the `user`, `company`, or `role` assigned to the task. |
| assignedToType   enum:string | Specifies whether the task is assigned to a user, company, or role. Possible values: `1` (user), `2` (company), `3` (role). |
| isRequired   boolean | `true`: the task is required to complete the step. <br>`false`: (default) the task is not required to complete the step. |
| stepDueDate   string | The due date of the related step, formatted as YYYY-MM-DD (ISO 8601) in UTC. For example, `2025-01-20`. |
| responseId   string: UUID | The ID of the response associated with the task, linking to the specific feedback or action taken. |
| responseComment   string | The content of the response comment, providing feedback or instructions related to the task. |
| respondedAt   datetime: ISO 8601 | The date and time when the response was added, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2025-01-20T12:00:00.198466Z`. |
| respondedBy   string | The Autodesk ID of the user who provided the response to the task. |
| createdAt   datetime: ISO 8601 | The date and time when the task was originally created, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2025-01-20T12:00:00.198466Z`. |
| createdBy   string | The Autodesk ID of the user who created the task. |
| updatedAt   datetime: ISO 8601 | The date and time when the task was last updated, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2025-01-20T12:00:00.198466Z`. |
| updatedBy   string | The Autodesk ID of the user who last updated the task. |
| startedAt   datetime: ISO 8601 | The date and time when the related step was marked as started (`In Progress`), formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2025-01-20T12:00:00.198466Z`. |
| completedAt   datetime: ISO 8601 | The date and time when the task was completed, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2025-01-20T12:00:00.198466Z`. |
| completedBy   string | The Autodesk ID of the user who completed the task. |
| permittedActions   array: object | A list of actions that the user is allowed to perform on the task within the submittal workflow. |
| id   string | The ID of the action in the format `type_of_object::action`. For example, `partial_update`. |
| fields   object | A mapping of field names to lists of possible values for each field. Note that an empty array indicates that there is no specific set of values for those fields. |
| mandatoryFields   array: string | Fields required to perform specific actions, such as closing a task. The required fields depend on the userâs role and the action. |
| transitions   array: string | Not relevant |

## [Example](#example)

Task details successfully retrieved.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/items/767b5888-2c6a-413d-8487-613966dd64ce/steps/b79059cc-611b-4769-80b7-f8db9a2dfcdf/tasks/f2bc8b34-7e95-4317-b298-0ed80c3eba6d' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "4d539b8f-c522-4f1c-9743-d7fdfa9e9c9e",
  "stepId": "d6635799-e973-4c9c-80d8-fb4b3591ef6b",
  "status": "completed",
  "assignedTo": "WD43ZJGKDFLFH",
  "assignedToType": "1",
  "isRequired": true,
  "stepDueDate": "2024-02-15",
  "responseId": "2d46d30b-7dc1-4a65-991d-d739a1381eb8",
  "responseComment": "Approved without changes.",
  "respondedAt": "2024-02-03T12:09:24.198466Z",
  "respondedBy": "WD43ZJGKDFLFH",
  "createdAt": "2024-03-21T23:04:49.406Z",
  "createdBy": "WD43ZJGKDFLFH",
  "updatedAt": "2024-03-24T23:04:49.406674Z",
  "updatedBy": "WD43ZJGKDFLFH",
  "startedAt": "2024-03-21T23:15:49.406894Z",
  "completedAt": "2024-03-24T23:04:49.4066344Z",
  "completedBy": "WD43ZJGKDFLFH",
  "permittedActions": [
    {
      "id": "Task::partial_update",
      "fields": {
        "responseComment": [],
        "responseId": []
      },
      "mandatoryFields": [
        "responseId"
      ],
      "transitions": [
        ""
      ]
    }
  ]
}

```

Show More
