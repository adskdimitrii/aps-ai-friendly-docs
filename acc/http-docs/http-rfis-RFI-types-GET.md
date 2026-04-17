# rfi-types

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-RFI-types-GET/

---

Rfi Types

GET

# rfi-types

Retrieves the list of RFI types configured for the specified project.

Each RFI type defines the default values and permitted options used when creating or updating RFIs. This includes the available `discipline`, `category`, and `priority` values, as well as the list of users, companies, or roles who can be assigned to workflow roles such as `manager`, `reviewer`, and `watcher`.

Call this endpoint before creating or updating an RFI to:

- Retrieve the available options for configurable fields such as `discipline`, `category`, `priority`, `costImpact`, and `scheduleImpact`.
- Get the list of potential assignees for workflow roles.
- Determine the default due date offset for an RFI type.

The values returned by this endpoint reflect the configuration set by project admins in Forma Data Management and Project Management.
For more information about creating and updating RFIs, see [POST rfis](http-rfis-rfis-POST.md) and [PATCH rfis/:id](http-rfis-rfis-id-PATCH.md).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfi-types |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The number of RFIs to return in the response. Acceptable values: `1–200`. Default: `10`. For example, to limit the response to two items per page, use `limit=2` |
| --- | --- |
| offset   int | The number of items to skip before starting to return results. <br>For example, to begin the results from the fourth item, use `offset=3`. |
| filter[status]   array: string | Filters the response to only include RFI types with the specified status. Possible values: `active`, `inactive`, `hidden`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success |
| --- | --- |
| 400   Bad Request | The parameters are invalid |
| 401   Unauthorized | The provided bearer token is not valid |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation |
| 500   Internal Server Error | An unknown error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of RFI types configured for the project. |
| --- | --- |
| id   string: UUID | The ID of the default RFI type assigned to the project. This is the unique identifier of the RFI type that will be selected by default when creating a new RFI. |
| name   string | The name of the RFI type, as configured by the project admin. This name is shown in the Forma UI and in the API when selecting an RFI type. <br>Max length: 50 |
| wfType   enum:string | The workflow type used for this RFI type. <br>Possible values:<br>`US`: The US-style workflow, with a Reviewer and optional Manager.`EU`: The EU-style workflow, with a Project Coordinator and Project Reviewer.<br>The workflow type determines the available statuses and workflow roles for RFIs of this type. |
| status   enum:string | The current status of the RFI type. <br>Possible values:<br>`active`: The type is available for use when creating or updating RFIs.`inactive`: The type exists but cannot currently be selected when creating RFIs.`hidden`: The type is hidden from users in the UI but may still appear in the API.<br>Only active types are available by default when creating new RFIs. |
| isDefault   boolean | `true`: This RFI type is the default for the project. <br>`false`: (default) This RFI type is not the default. |
| projectReviewer   array: object | A list of users, companies, or roles that can be assigned to this project role. |
| id   string | The Autodesk ID of the user, company, or role. <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](http-projects--project_id-companies-GET.md).<br>Note that we do not currently support finding details about roles for a project. |
| type   enum:string | The type of assignee. Possible values: `user`, `company`, `role`. |
| projectCoordinator   array: object | A list of users, companies, or roles that can be assigned to this project role. |
| id   string | The Autodesk ID of the user, company, or role. <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](http-projects--project_id-companies-GET.md).<br>Note that we do not currently support finding details about roles for a project. |
| type   enum:string | The type of assignee. Possible values: `user`, `company`, `role`. |
| manager   array: object | A list of users, companies, or roles who can be assigned to this workflow role. |
| id   string | The Autodesk ID of the user, company, or role. <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](http-projects--project_id-companies-GET.md).<br>Note that we do not currently support finding details about roles for a project. |
| type   enum:string | The type of assignee. Possible values: `user`, `company`, `role`. |
| watchers   array: object | A list of users, companies, or roles that can be assigned to this project role. |
| id   string | The Autodesk ID of the user, company, or role. <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](http-projects--project_id-companies-GET.md).<br>Note that we do not currently support finding details about roles for a project. |
| type   enum:string | The type of assignee. Possible values: `user`, `company`, `role`. |
| dueDateOffset   integer,null | The number of calendar days from the RFI creation date to the default due date. Used to automatically calculate the RFI due date when creating a new RFI of this type. |
| locationDescription   string,null | The default text for the **Location** field when creating a new RFI. <br>Note that the API does not auto-populate this value. Clients are responsible for applying the default if desired. |
| costImpact   string,null | The default cost impact value for new RFIs of this type. <br>Possible values: `null`, `Yes`, `No`, `Unknown`. |
| scheduleImpact   string,null | The default schedule impact value for new RFIs of this type. <br>Possible values: `null`, `Yes`, `No`, `Unknown`. |
| priority   string,null | The default priority for new RFIs of this type. <br>The available priority values are configured in Project Admin.<br>If no default is set, this field is `null`.<br>Note that the API does not auto-populate this value when creating an RFI. Clients are responsible for applying the default if desired.<br>Some possible values: `null`, `High`, `Normal`, `Low`. |
| discipline   array: string | The list of available disciplines for RFIs. <br>Each discipline is configured in Project Admin. Some possible values: `Architectural`, `Civil/Site`, `Concrete`, `Electrical`, `Exterior Envelope`, `Fire Protection`, `Interior/Finishes`, `Landscaping`, `Masonry`, `Mechanical`, `Plumbing`, `Structural`, `Other`. |
| category   array: string | A list of predefined categories to assign to the RFI. <br>Categories help group RFIs for filtering and reporting. Each value must match a category configured in the project’s RFI settings. Categories are case-sensitive and project-specific.<br>RFI categories are configured in Project Admin and may differ between projects.<br>Some possible values: `Code Compliance`, `Constructability`, `Design Coordination`, `Documentation Conflict`, `Documentation Incomplete`, `Field condition`, `Other`. |
| reference   string,null | The default value for the Reference field when creating a new RFI. <br>This is typically used when the RFI was created in another system.<br>Note that the API does not auto-populate this value. Clients are responsible for applying the default if desired.<br>Max length: 20 |
| bridgeTargetProjectIds   array,null | Not relevant |
| pagination   object | The pagination object. |
| limit   int | The number of items returned per page. |
| offset   int | The number of items skipped before this page of results. |
| totalResults   int | The total number of items matching the request. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfi-types' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "id": "c911852d-5957-4145-9c8d-e7cfe9d564df",
      "name": "Type 1",
      "wfType": "US",
      "status": "active",
      "isDefault": true,
      "projectReviewer": [
        {
          "id": "PER8KQPK2JRT",
          "type": "user"
        }
      ],
      "projectCoordinator": [
        {
          "id": "PER8KQPK2JRT",
          "type": "user"
        }
      ],
      "manager": [
        {
          "id": "PER8KQPK2JRT",
          "type": "user"
        }
      ],
      "watchers": [
        {
          "id": "PER8KQPK2JRT",
          "type": "user"
        }
      ],
      "dueDateOffset": 7,
      "locationDescription": "In the middle of the room.",
      "costImpact": "Yes",
      "scheduleImpact": "Yes",
      "priority": "High",
      "discipline": [
        "Architectural"
      ],
      "category": [
        "Constructability"
      ],
      "reference": "",
      "bridgeTargetProjectIds": ""
    }
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 97
  }
}

```

Show More
