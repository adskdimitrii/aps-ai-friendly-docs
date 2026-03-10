# users/me

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-users-me-GET/

---

RFIs

GET

# users/me

Retrieves information about the current user in the context of the specified project. The response includes the user’s assigned RFI workflow roles, whether the user is permitted to create RFIs, the workflow states in which the user can create RFIs, and the attributes required in each state.

**We strongly recommend calling this endpoint before creating an RFI,** to ensure the user has the necessary permissions and the latest configuration for the project.

The RFIs API does not currently support adding users to a project or assigning workflow roles. Only project members can create or edit RFIs.

To add responses or attachments to the RFI, call [POST responses](http-rfis-rfis-POST.md) after the RFI is created.

Users can create RFIs if they are assigned either the creator (`projectSC`) or manager (`projectGC`) workflow role.
These roles must be explicitly configured in the RFI tool settings by going to RFIs → Settings → Permissions in the Autodesk Construction Cloud (ACC) web interface.
There is no default workflow role, so project members will not be able to create RFIs unless one of these roles is assigned.

To check if a user can create RFIs, look for the `createRfi` object inside the `permittedActions` section of the response.

Workflow roles must be assigned manually via the UI. There is currently no API support for modifying workflow roles.

The table below lists the Project Admin workflow role names and their corresponding RFIs API role names:

| Project Admin Module Workflow Role Name | RFIs API Workflow Role Name |
| --- | --- |
| Creator | Subcontractor (`projectSC`) |
| Manager | General Contractor (`projectGC`) |
| Reviewer 1 (EMEA workflow) | Construction Manager (`projectCoordinator`) |
| Reviewer (US workflow) / Reviewer 2 (EMEA workflow) | Architect (`projectReviewer`) |

For more information, see the [RFIs permissions documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=RFI_Permissions).

The table below shows the workflow names used in the Project Admin UI and their corresponding values in the RFIs API:

| Project Admin Module Workflow Type Name | RFIs API Workflow Type Name |
| --- | --- |
| Default Workflow | US |
| Workflow with Additional Reviewer | EMEA |

You can use either workflow type (`US` or `EMEA`) in both the US and EMEA regions. To assign a workflow type to a project, use the Project Admin UI.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/users/me |
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

| 200   OK | Success |
| --- | --- |
| 400   Bad Request | The parameters are invalid |
| 401   Unauthorized | The provided bearer token is not valid |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation |
| 500   Internal Server Error | An unknown error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| user   object | The current user’s details. |
| --- | --- |
| id   string | The Autodesk ID of the user. |
| name   string | The name of the user. |
| role   enum:string | The user’s role in the project. Possible values: `project_user`, `project_admin`. |
| permittedActions   object | The list of actions that are permitted for the user. |
| createRfi   object | The user’s permissions for creating RFIs. <br>Note that if this field is present, the user is permitted to create RFIs in the project. |
| permittedStatuses   object | The list of statuses the user is permitted to transition an RFI to, without differentiating between workflow types (e.g., `us` and `emea`). |
| wfUS   array: object | The list of statuses the user is permitted to transition an RFI to in workflows of type `US`. |
| status   enum:string | The current response status of the RFI for single-reviewer workflows (US):  > Possible values: > `draft`, `submitted`, `open`, `answered`, `rejected`, `closed`, `void`. <br>For more information about workflows, see [About RFI Workflows – Autodesk Help](https://help.autodesk.com/view/BUILD/ENU/?guid=RFI_Types). |
| maxAssignees   int | The maximum number of users that can be assigned to this RFI. |
| requiredAttributes   array: object | The list of attributes that are required when creating or updating an RFI. |
| name   string | The name of the RFI attribute that must be provided when updating or creating an RFI in the specified status. |
| values   array: object | The list of allowed values for the required attribute. |
| value   string | The actual value that must be used for the required attribute when updating or creating the RFI. <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](en/docs/acc/v1/reference/http/projects-:project_id-companies-GET/).<br>Note that we do not currently support finding details about roles for a project. |
| type   string | The type of the required attribute value. Indicates what kind of entity the value represents (e.g., `user`, `role`, or `company`). |
| permittedAttributes   array: object | The list of attributes that the user is optionally allowed to include when updating or creating the RFI in the specified status. |
| name   string | The name of the RFI attribute that must be provided when updating or creating an RFI in the specified status. |
| values   array: object | The list of allowed values for the required attribute. |
| value   string | The actual value that must be used for the required attribute when updating or creating the RFI. <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](en/docs/acc/v1/reference/http/projects-:project_id-companies-GET/).<br>Note that we do not currently support finding details about roles for a project. |
| type   string | The type of the required attribute value. Indicates what kind of entity the value represents (e.g., `user`, `role`, or `company`). |
| wfEU   array: object | The list of statuses the user is permitted to transition an RFI to in workflows of type `emea`. |
| status   enum:string | The current response status of the RFI for a multi-reviewer workflow (EMEA): Possible values: `draft`, `submitted`, `openRev1` (manager), `openRev2` (reviewer), `answeredRev1`, `answeredManager`, `closed`, `void`. <br>For more information about workflows, see [About RFI Workflows – Autodesk Help](https://help.autodesk.com/view/BUILD/ENU/?guid=RFI_Types). |
| maxAssignees   int | The maximum number of users that can be assigned to this RFI. |
| requiredAttributes   array: object | The list of attributes that are required when creating or updating an RFI. |
| name   string | The name of the RFI attribute that must be provided when updating or creating an RFI in the specified status. |
| values   array: object | The list of allowed values for the required attribute. |
| value   string | The actual value that must be used for the required attribute when updating or creating the RFI. <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](en/docs/acc/v1/reference/http/projects-:project_id-companies-GET/).<br>Note that we do not currently support finding details about roles for a project. |
| type   string | The type of the required attribute value. Indicates what kind of entity the value represents (e.g., `user`, `role`, or `company`). |
| permittedAttributes   array: object | The list of attributes that the user is optionally allowed to include when updating or creating the RFI in the specified status. |
| name   string | The name of the RFI attribute that must be provided when updating or creating an RFI in the specified status. |
| values   array: object | The list of allowed values for the required attribute. |
| value   string | The actual value that must be used for the required attribute when updating or creating the RFI. <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](en/docs/acc/v1/reference/http/projects-:project_id-companies-GET/).<br>Note that we do not currently support finding details about roles for a project. |
| type   string | The type of the required attribute value. Indicates what kind of entity the value represents (e.g., `user`, `role`, or `company`). |
| workflow   object | The user’s assigned workflow roles and workflow type for RFIs in the current project. |
| roles   array: string | The list of RFI workflow roles assigned to the user. Possible values: <br>`projectSC` — Creator<br>`projectGC` — Manager<br>`projectCoordinator` — Reviewer 1 (EMEA workflow only)<br>`projectReviewer` — Reviewer 1 (US) or Reviewer 2 (EMEA)<br>For information about workflow roles, see the [RFIs Permission](https://help.autodesk.com/view/BUILD/ENU/?guid=RFI_Statuses) documentation. |
| type   enum:string | The RFI workflow type assigned to the project. <br>Possible values:<br>`US` Single-reviewer workflow `EU` Two-reviewer workflow<br>Note that you cannot set the workflow type via the API. To change it, use the Project Admin UI. |
| defaultRfiType   string: UUID | The ID of the default RFI type assigned to the project. This is the unique identifier of the RFI type that will be selected by default when creating a new RFI. |
| externalUsers   array: object | Not relevant |
| email   string | Not relevant |
| autodeskId   string | Not relevant |
| maintenanceEndDate   string | Not relevant |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/users/me' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "user": {
    "id": "BZPWJWWWMLSV",
    "name": "Jon Doe",
    "role": "project_admin"
  },
  "permittedActions": {
    "createRfi": {
      "permittedStatuses": {
        "wfUS": [
          {
            "status": "open",
            "maxAssignees": "",
            "requiredAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "PER8KQPK2JRT",
                    "type": "user"
                  }
                ]
              }
            ],
            "permittedAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "PER8KQPK2JRT",
                    "type": "user"
                  }
                ]
              }
            ]
          }
        ],
        "wfEU": [
          {
            "status": "open",
            "maxAssignees": "",
            "requiredAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "PER8KQPK2JRT",
                    "type": "user"
                  }
                ]
              }
            ],
            "permittedAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "PER8KQPK2JRT",
                    "type": "user"
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  },
  "workflow": {
    "roles": [
      "projectSC"
    ],
    "type": "US"
  },
  "defaultRfiType": "c911852d-5957-4145-9c8d-e7cfe9d564df",
  "externalUsers": [
    {
      "email": "",
      "autodeskId": ""
    }
  ],
  "maintenanceEndDate": ""
}

```

Show More
