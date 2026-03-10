# projects/{projectId}/packages/{id}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-packages-id-GET/

---

Packages

GET

# projects/{projectId}/packages/{id}

Retrieve details about a single package. For information about packages, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Packages).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/packages/:id |
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

- projectIdstring: UUID The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- idstring The ID of the submittal item to retrieve revisions for. To obtain this ID, call [GET items](http-submittals-items-GET.md).

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | A successfully retrieved package |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. |
| 401   Unauthorized | Invalid or missing authorization header. Verify the Bearer token and try again. |
| 403   Forbidden | The user is not authorized to perform this action. |
| 404   Not Found | The specified resource was not found. |
| 500   Internal Server Error | An unexpected error occurred on the server while processing the request. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| id   string: UUID | The internal, globally unique identifier (UUID) for the package. |
| --- | --- |
| specId   string: UUID | The internal, globally unique identifier (UUID) of the spec associated with the package. |
| title   string | The title of the package. |
| identifier   int | The unique ID assigned to the package within the UI. |
| description   string | The description of the package. |
| specIdentifier   string | The unique ID of the spec assigned to the package in the UI, specific to each project. |
| permittedActions   array: object | The list of actions the user is allowed to perform on the submittal item. |
| id   string | The ID of the action in the format `type_of_object::action`. For example, `Item::retrieve`. |
| fields   object | A list of field names for which values must be provided when performing the action. An empty array indicates no specific set of values. |
| mandatoryFields   array: string | Lists the fields that are required when updating a submittal item. <br>The required fields depend on the action being performed, the item’s current state, and the user’s role.<br>For example:<br>To transition the state of a submittal item, `stateId` and `responseId` are required. To reassign the manager, `manager` and `managerType` are required. To modify the spec section, `specId` is required. |
| transitions   array: object | The list of possible state transitions for a submittal item within the review workflow. |
| id   string | The ID of the transition in the format `from-state::to-state`. For example, `create::mgr-1`, `mgr-1::mgr-2`, `rev::void`. |
| name   string | The descriptive name of the transition. For example, `Create`, `Send to Manager`, `Send to void`. |
| stateFrom   object | The starting state of the transition, representing the current position of the submittal item in the workflow. |
| id   string | The unique ID of the starting state. For example, `create`, `mgr-1`, `rev`. The `rev` state indicates that the submittal item is currently under review. |
| name   string | The name of the starting state. For example, `Create`, `Manager Review`, `Review`. |
| stateTo   object | The target state of the transition, indicating the next position of the submittal item in the workflow. |
| id   string | The unique ID of the target state. For example, `mgr-1`, `mgr-2`, `void`. |
| name   string | The name of the target state. For example, `Manager Review`, `Manager Final Review`, `Void`. |
| transitionFields   array: string | Fields that are used in the transition. For example, [`subcontractor`, `subcontractorType`, `watchers`, `responseId`]. |
| mandatoryFields   array: string | A list of required fields for the transition. For example, [`responseId`]. |
| actionId   string | Not relevant |

## [Example](#example)

A successfully retrieved package

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/packages/:id' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "e8302552-fc5a-42ac-ba4b-e9de9760c356",
  "specId": "e6111f96-8437-491e-a1ae-16fd53f0cbef",
  "title": "my package1",
  "identifier": 222,
  "description": "Electrical specifications",
  "specIdentifier": "A-500",
  "permittedActions": [
    {
      "id": "Item::update",
      "fields": {
        "subcontractor": [],
        "manager": []
      },
      "mandatoryFields": [
        ""
      ],
      "transitions": [
        {
          "id": "rev::void",
          "name": "Send to void",
          "stateFrom": {
            "id": "rev",
            "name": "Review"
          },
          "stateTo": {
            "id": "void",
            "name": "Void"
          },
          "transitionFields": [
            "subcontractor",
            "subcontractorType",
            "watchers",
            "responseId"
          ],
          "mandatoryFields": [
            "responseId"
          ],
          "actionId": "ITEM_TRANSITION_REV_VOID"
        }
      ]
    }
  ]
}

```

Show More
