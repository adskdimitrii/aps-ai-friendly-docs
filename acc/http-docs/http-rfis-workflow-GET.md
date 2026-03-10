# workflow

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-workflow-GET/

---

Workflows

GET

# workflow

Retrieves the workflow configuration for a given project, including the workflow type, description, and the mapping between project roles and their permitted assignees.

This endpoint helps clients understand which users, companies, or roles are allowed to participate in specific workflow actions within a project.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/workflow |
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

| projectId   string | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | OK |
| --- | --- |
| 400   Bad Request | The parameters are invalid |
| 401   Unauthorized | The provided bearer token is not valid |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation |
| 500   Internal Server Error | An unknown error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| workflowType   enum:string | The region type of the workflow. Possible values: `US`, `EU`. |
| --- | --- |
| description   string | A description of the workflow |
| projectRolesMapping   array: object | A list of project roles and their corresponding permitted assignees. |
| name   string | The name of the project role |
| permittedAssignees   array: object | A list of users, companies, or roles that can be assigned to this project role. |
| id   string | The Autodesk ID of the user, company, or role. <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](http-projects--project_id-companies-GET.md).<br>Note that we do not currently support finding details about roles for a project. |
| type   enum:string | The type of assignee. Possible values: `user`, `company`, `role`. |

## [Example](#example)

OK

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/workflow' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "workflowType": "US",
  "description": "Support for RFI creation. Review and response with Creator, Manager and Reviewer workflow roles.",
  "projectRolesMapping": [
    {
      "name": "projectGC",
      "permittedAssignees": [
        {
          "id": "PER8KQPK2JRT",
          "type": "user"
        }
      ]
    }
  ]
}

```

Show More
