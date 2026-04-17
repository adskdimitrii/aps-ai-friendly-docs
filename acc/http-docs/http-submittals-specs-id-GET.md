# projects/{projectId}/specs/{id}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-specs-id-GET/

---

Specs

GET

# projects/{projectId}/specs/{id}

Retrieve the details about a single spec section. For information about spec sections, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Spec_Sections).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/specs/:id |
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

- projectIdstring: UUID The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- idstring The ID of the submittal item to retrieve revisions for. To obtain this ID, call [GET items](http-submittals-items-GET.md).

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful request to create a new spec section. |
| --- | --- |
| 403   Forbidden | Unauthorized |

### Response

## [Body Structure (200)](#body-structure-200)

| id   string: UUID | The internal, globally unique identifier (UUID) for the spec section. |
| --- | --- |
| title   string | The title of the spec section. |
| identifier   string | The unique ID assigned to the spec section within the UI. |
| createdBy   string | The Autodesk ID of the user who created the spec section. |
| createdAt   datetime: ISO 8601 | The time and date when the spec section was created. |
| updatedBy   string | The Autodesk ID of the user who last updated the spec section. |
| updatedAt   datetime: ISO 8601 | The time and date when spec section was last updated. |

## [Example](#example)

Successful request to create a new spec section.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/specs/:id' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "e6111f96-8437-491e-a1ae-16fd53f0cbef",
  "title": "Materials",
  "identifier": "500",
  "createdBy": "WD43ZJGKDFLFH",
  "createdAt": "2018-02-01T12:09:24.198466Z",
  "updatedBy": "WD43ZJGKDFLFH",
  "updatedAt": "2018-02-01T12:09:24.198466Z"
}

```

Show More
