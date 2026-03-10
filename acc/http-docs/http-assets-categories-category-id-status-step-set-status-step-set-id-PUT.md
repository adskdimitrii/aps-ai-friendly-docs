# categories/:categoryId/status-step-set/:statusStepSetId

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-categories-category-id-status-step-set-status-step-set-id-PUT/

---

Status-Sets

PUT

# categories/:categoryId/status-step-set/:statusStepSetId

Assigns a status set to a category.

This endpoint specifies a category and a status set to assign to that category. It returns the details of the
status set category assignment.

Only a single status set can be assigned to a category at any given time. Assigning a status set to a category
will overwrite any existing status set assignments for this category, either explicitly assigned or inherited
from the parent category.

To understand the basics of status sets, inheritance, and the Assets settings that define them, see the [Assets Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/assets/).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | PUT https://developer.api.autodesk.com/construction/assets/v1/projects/{projectId}/categories/{categoryId}/status-step-set/{statusStepSetId} |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form “b.{UUID}”. |
| --- | --- |
| categoryId   string | The category ID |
| statusStepSetId   string: UUID | The status set ID |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully assigned a status set to a category. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the target resource |
| 429   Too Many Requests | The request was not accepted because the rate limit was exceeded due to too many requests being made. |
| 500   Internal Server Error | An unexpected error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

| id   string | The ID of the component. |
| --- | --- |
| createdAt   string | The time when the component was created (ISO8601 Date time format in UTC). |
| createdBy   string | The actor that created the component. This is an Autodesk / Oxygen ID. |
| updatedAt   string | The time when the component was last updated (ISO8601 Date time format in UTC). |
| updatedBy   string | The actor that last updated the component. This is an Autodesk / Oxygen ID. |
| deletedAt   string | The time when the component was deleted at (ISO8601 Date time format in UTC). |
| deletedBy   string | The actor that deleted the component. This is an Autodesk / Oxygen ID. |
| isActive   boolean | A flag indicating whether the component is active or inactive (`isActive` is `true` if-and-only-if `deletedAt` is empty). |
| version   int | A global sequence number that is incremented any time a component of this type is created, updated, or deleted. If you cache components, you can use the version value to compare the cached component to the same component online to see if the component has been updated. If the online component has a higher version value, it has been updated. |
| projectId   string: UUID | The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form “b.{UUID}”. |
| categoryId   string | The ID of the category to which the status set is assigned. |
| statusStepSetId   string: UUID | The ID of the status set assigned to the category. |

## [Example](#example)

Successfully assigned a status set to a category.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v1/projects/:projectId/categories/123/status-step-set/6eb35939-e5fb-453a-98ed-e2e11f326e73' \
  -X 'PUT' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "b302d910-b5e3-46ba-81d8-6b6d30406e14",
  "createdAt": "2020-05-01T06:00:00.000Z",
  "createdBy": "LA7ZL85MU7ML",
  "updatedAt": "2020-05-01T06:00:00.000Z",
  "updatedBy": "LA7ZL85MU7ML",
  "deletedAt": "2020-05-01T06:00:00.000Z",
  "deletedBy": "LA7ZL85MU7ML",
  "isActive": true,
  "version": 1,
  "projectId": "f74a012c-62fd-4988-ac2b-c5b4fd937724",
  "categoryId": "124",
  "statusStepSetId": "6eb35939-e5fb-453a-98ed-e2e11f326e73"
}

```

Show More
