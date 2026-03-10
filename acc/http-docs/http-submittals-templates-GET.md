# projects/{projectId}/templates

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-templates-GET/

---

Templates

GET

# projects/{projectId}/templates

Retrieves a list of review templates available for a project. Each review template contains predefined steps and tasks that streamline the review workflow and can be applied to submittal items during their creation using [POST items](http-submittals-items-POST.md).

Currently, review templates must be created in the UI. For instructions on creating review templates, see the [Submittal Review Templates Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Review_Templates).

For a detailed overview of the submittal workflow, see the [Manage Submittal Item Transitions tutorial](../how-to-docs/submittals-submittal-transitions.rst.md).

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/templates |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The maximum number of results per page. Possible values: `1`- `50`. Default value: `20`. For example, to limit the response to two results per page, use `limit=2`. |
| --- | --- |
| offset   int | The number of results to skip before starting to return data. For example, to skip the first 20 results, include `offset=20` in the query string. For more details, see the [JSON API Paging Help documentation](https://jsonapi.org/format/#fetching-pagination). |
| sort   string | A comma-delimited list of fields to sort by in the format `field asc` or `field desc`. <br>Possible values: `id`, `name`, `createdAt`, `createdBy`, `updatedAt`, `updatedBy`.<br>For example: `sort=id asc`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | A successful request returning review templates with steps and tasks. |
| --- | --- |
| 401   Unauthorized | Invalid or missing authorization header. Verify the Bearer token and try again. |
| 403   Forbidden | The user is not authorized to perform this action. |
| 404   Not Found | The specified resource was not found. |
| 500   Internal Server Error | An unexpected error occurred on the server while processing the request. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| pagination   object | Describes pagination details for the response, including information about the current page and navigation to other pages. |
| --- | --- |
| limit   int | The maximum number of results to be displayed on each page. |
| offset   int | The number of results skipped before starting the current page. |
| totalResults   int | The overall count of results available across all pages. |
| previousUrl   string | The URL to retrieve the preceding page of results, if applicable. Not returned on the first page of results. |
| nextUrl   string | The URL to retrieve the subsequent page of results, if available. If not included, this is the last page of data. |
| results   array: object | The list of templates retrieved in the API response. Each template includes its steps and associated tasks. |
| id   string: UUID | The internal, globally unique identifier (UUID) for the template. Each template in the workflow has a unique ID. |
| name   string | The name of the template. |
| steps   array: object | The list of steps included in the template. Each step defines specific actions and associated tasks. |
| id   string: UUID | The internal, globally unique identifier (UUID) for the step. Each step in the workflow has a unique ID. |
| stepNumber   number | The number representing the order of the steps, where `1` is the first step. |
| daysToRespond   number | Specifies a dynamic due date. When the step starts, the due date is calculated based on this field. |
| tasks   array: object | A list of tasks associated with this template. Each task has its own unique identifier (UUID). |
| id   string: UUID | The internal, globally unique identifier (UUID) for the task. |
| assignedTo   string | The Autodesk ID or member group ID of the `user`, `company`, or `role` assigned to the task. |
| assignedToType   enum:string | Specifies whether the task is assigned to a user, company, or role. Possible values: `1` (user), `2` (company), `3` (role). |
| isRequired   boolean | `true`: the task is required to complete the step.`false`: (default) the task is not required to complete the step. |
| createdAt   datetime: ISO 8601 | The date and time when the template was originally created, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2025-01-20T12:00:00.198466Z`. |
| createdBy   string | The Autodesk ID of the user that created the template. |
| updatedAt   datetime: ISO 8601 | The date and time when the template was last updated, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2025-01-20T12:00:00.198466Z`. |
| updatedBy   string | The Autodesk ID of the user that last updated the template. |
| watchers   array: object | A list of project watchers, who can be individual users, roles, or companies. |
| id   string | The Autodesk ID of the watcher. The watcher can be a user (`autodeskId`), role (`memberGroupId`), or company (`memberGroupId`). <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](en/docs/acc/v1/reference/http/projects-:project_id-companies-GET/). Note that we do not currently support finding details about roles for a project. |
| userType   object | The type of watcher assigned to the submittal item. <br>Possible values:<br>`1` (user)`2` (company)`3` (role) |

## [Example](#example)

A successful request returning review templates with steps and tasks.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/templates' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 10,
    "offset": 100,
    "totalResults": 25,
    "previousUrl": "https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/templates?limit=5&offset=10",
    "nextUrl": null
  },
  "results": [
    {
      "id": "56abeb4a-c450-4c34-a23d-a49e5e47ef2a",
      "name": "Structural Review Template",
      "steps": [
        {
          "id": "54e9ca56-54b8-4492-b140-d6c0454d70fe",
          "stepNumber": 1,
          "daysToRespond": 10,
          "tasks": [
            {
              "id": "63d901e6-e148-4b29-8330-92dfe91e8d07",
              "assignedTo": "WD43ZJGKDFLFH",
              "assignedToType": "1",
              "isRequired": true
            }
          ]
        }
      ],
      "createdAt": "2018-02-21T23:04:49.406673Z",
      "createdBy": "WD43ZJGKDFLFH",
      "updatedAt": "2018-02-21T23:04:49.406Z",
      "updatedBy": "WD43ZJGKDFLFH",
      "watchers": [
        {
          "id": "224356",
          "userType": "2"
        },
        {
          "id": "3522614",
          "userType": "3"
        }
      ]
    }
  ]
}

```

Show More
