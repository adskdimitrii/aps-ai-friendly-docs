# users/me

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-users-me-GET/

---

Submittals Profile

GET

# users/me

Retrieves the Autodesk ID, assigned roles, and permitted actions for the current user within a specified project.

This endpoint serves two main purposes:

- To retrieve the Autodesk ID and roles of the current user in Submittals.
- To obtain the list of actions the user is permitted to perform in the system, such as `Item::create` and `Spec::create`.

For more information on roles and permissions in Submittals, refer to the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittals_Permissions).

For detailed steps on creating submittal items, refer to the [Create Submittal Item](../how-to-docs/submittals-create-submittal-item.md) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/users/me |
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

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Returns user details. |
| --- | --- |
| 401   Unauthorized | Invalid or missing authorization header. Verify the Bearer token and try again. |
| 403   Forbidden | The user is not authorized to perform this action. |
| 404   Not Found | The specified resource was not found. |
| 500   Internal Server Error | An unexpected error occurred on the server while processing the request. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| id   string | The AutodeskId for the current user. |
| --- | --- |
| roles   array: string | The roles assigned to the user in Submittals. Possible values: `1` - `Manager`, `2` - `User`, `4` - `Admin` |
| permittedActions   array: object | A list of actions that the user is allowed to perform |
| id   string | ID of the action in the format `type_of_object::action`. For example, `item::create`, `Spec::create`. |
| fields   object | A mapping of field names to lists of possible values for each field, specific to the associated action. An empty array indicates that there is no specific set of values for those fields. <br>For example, in the action `Spec::create`, fields might contain mapping for title (`title`) and identifier (`identifier`). |
| mandatoryFields   array: string | A subset of fields (`fields`) that are required to perform specific actions, such as creating or transitioning a submittal item. The required fields depend on the user’s role and the action. <br>For example, creating a submittal item in the `mgr-1` state as a manager or in the `sbc-1` state as a subcontractor requires different fields. For example, [`stateId`, `specId`, `title`, `typeId`, `manager`, `managerType`]. |
| transitions   array: object | list of possible transitions |
| id   string | The ID of the transition in the format `from-state::to-state`. Possible values: `create::mgr-1`, `create::sbc-1`. |
| name   string | The descriptive name of the transition. Possible values: `Create`, `Send to Manager`, `Send to void`. |
| stateFrom   object | The starting state of the transition. |
| id   string | The unique ID of the starting state. Possible values: `create`, `mgr-1`, `sbc-1`. A `rev` (review), refers to the state where a submittal item is undergoing revisions or is being reviewed. |
| name   string | The name of the starting state. Possible values: `Create`, `Manager Review`, `Review`. |
| stateTo   object | The target state of the transition. |
| id   string | The unique ID of the target state. For example, `mgr-1`, `mgr-2`, `void`. |
| name   string | The name of the target state. For example, `Manager Review`, `Manager Final Review`, `Void`. |
| transitionFields   array: string | Fields that are used in the transition. For example, [`subcontractor`, `subcontractorType`, `watchers`, `responseId`]. |
| mandatoryFields   array: string | A list of required fields for the transition. For example, [`responseId`]. |
| actionId   string | Not relevant |

## [Example](#example)

Returns user details.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/users/me' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "GJDGNLSX7B8T",
  "roles": [
    "1",
    "2",
    "4"
  ],
  "permittedActions": [
    {
      "id": "Item::create",
      "fields": {},
      "mandatoryFields": [
        ""
      ],
      "transitions": [
        {
          "id": "create::mgr-1",
          "name": "Create",
          "stateFrom": {
            "id": "create",
            "name": "Create"
          },
          "stateTo": {
            "id": "mgr-1",
            "name": "MGR 1"
          },
          "transitionFields": [
            "manager",
            "managerType",
            "stateId",
            "title",
            "description",
            "priority"
          ],
          "mandatoryFields": [
            [
              "manager",
              "managerType",
              "stateId",
              "title"
            ]
          ],
          "actionId": "ITEM_TRANSITION_CREATE_MGR1"
        }
      ]
    }
  ]
}

```

Show More
