# status-step-sets

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-status-step-sets-POST/

---

Status-Sets

POST

# status-step-sets

Creates a new status set.

This endpoint defines a new status set by specifying a display name, an optional description, and a set of one
or more new statuses. The endpoint uses the status specifications to create new statuses for the status set.
Each status set has its own unique set of statuses, and statuses are not shared among status sets.

To understand the basics of status sets, and the Assets settings that define them, see the [Assets Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/assets/).

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/assets/v1/projects/{projectId}/status-step-sets |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` `data:create` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The Forma project ID. Must be a UUID or a project ID of the form “b.{UUID}”. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| renameConflicting   boolean | Specifies that any inactive (deleted) entity with a conflicting name should be automatically renamed to avoid a conflict. Only supported by specific APIs. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

Expand all

| name*   string | The display name for the status set. This name appears in the Assets UI when viewing status sets. <br>Max length: 100 |
| --- | --- |
| description   string | A description of the status set. <br>Max length: 500 |
| values*   array: object | An array of asset statuses to populate the new status set. This array defines new statuses. |
| label*   string | The display label of the status. This label appears in the Assets UI when viewing statuses. The label must be unique within this status set, but does not need to be unique within the project (in other words, the same label can be used in multiple status sets in the same project). “Uniqueness” in this context means case-insensitive. |
| description   string | A description of the status. |
| color   string | The color of the status as the status appears in the Assets UI. <br>This field is not restricted as it is primarily a tool for the Assets UI to use.<br>However, there are only certain colors that the Forma Assets UI knows how to operate with. Understood color values are: `adsk-black`, `adsk-white`, `adsk-charcoal-900`, `adsk-charcoal-800`, `adsk-charcoal-700`, `adsk-charcoal-600`, `adsk-charcoal-500`, `adsk-charcoal-400`, `adsk-charcoal-300`, `adsk-charcoal-200`, `adsk-charcoal-100`, `adsk-charcoal-050`, `adsk-blue-700`, `adsk-blue-500`, `adsk-blue-300`, `adsk-blue-100`, `adsk-red-700`, `adsk-red-500`, `adsk-red-300`, `adsk-green-700`, `adsk-green-500`, `adsk-green-300`, `adsk-yellow-orange-700`, `adsk-yellow-orange-500`, `adsk-yellow-orange-300`, `adsk-dark-blue-700`, `adsk-dark-blue-500`, `adsk-dark-blue-300`, `adsk-pink-700`, `adsk-pink-500`, `adsk-pink-300`, `adsk-turquoise-700`, `adsk-turquoise-500`, `adsk-turquoise-300`, `adsk-purple-700`, `adsk-purple-500`, `adsk-purple-300`, `adsk-salmon-700`, `adsk-salmon-500`, `adsk-salmon-300`, `adsk-brown-700`, `adsk-brown-500`, `adsk-brown-300`.<br>Using colors other than those specified here is not disallowed, but may result in unexpected behavior in<br>the Assets UI. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Successfully created a new status set. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the target resource |
| 429   Too Many Requests | The request was not accepted because the rate limit was exceeded due to too many requests being made. |
| 500   Internal Server Error | An unexpected error occurred on the server |

### Response

## [Body Structure (201)](#body-structure-201)

Expand all

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
| projectId   string: UUID | The Forma project ID. Must be a UUID or a project ID of the form “b.{UUID}”. |
| name   string | The display name for the status set. This name appears in the Assets UI when viewing status sets. <br>Max length: 100 |
| description   string | A description of the status set. <br>Max length: 500 |
| isDefault   boolean | Specifies if this is the status set that is assigned to categories by default - that is, this is the status set that will be assigned to categories if no other status set has been assigned, either explicitly or through inheritance. If `true`, it’s the default status set. If `false`, it’s not. |
| values   array: object | An array of statuses that belong to this status set. |
| label   string | The display label of the status. This label appears in the Assets UI when viewing statuses. The label must be unique within this status set, but does not need to be unique within the project (in other words, the same label can be used in multiple status sets in the same project). “Uniqueness” in this context means case-insensitive. |
| description   string | A description of the status. |
| color   string | The color of the status as the status appears in the Assets UI. <br>This field is not restricted as it is primarily a tool for the Assets UI to use.<br>However, there are only certain colors that the Forma Assets UI knows how to operate with. Understood color values are: `adsk-black`, `adsk-white`, `adsk-charcoal-900`, `adsk-charcoal-800`, `adsk-charcoal-700`, `adsk-charcoal-600`, `adsk-charcoal-500`, `adsk-charcoal-400`, `adsk-charcoal-300`, `adsk-charcoal-200`, `adsk-charcoal-100`, `adsk-charcoal-050`, `adsk-blue-700`, `adsk-blue-500`, `adsk-blue-300`, `adsk-blue-100`, `adsk-red-700`, `adsk-red-500`, `adsk-red-300`, `adsk-green-700`, `adsk-green-500`, `adsk-green-300`, `adsk-yellow-orange-700`, `adsk-yellow-orange-500`, `adsk-yellow-orange-300`, `adsk-dark-blue-700`, `adsk-dark-blue-500`, `adsk-dark-blue-300`, `adsk-pink-700`, `adsk-pink-500`, `adsk-pink-300`, `adsk-turquoise-700`, `adsk-turquoise-500`, `adsk-turquoise-300`, `adsk-purple-700`, `adsk-purple-500`, `adsk-purple-300`, `adsk-salmon-700`, `adsk-salmon-500`, `adsk-salmon-300`, `adsk-brown-700`, `adsk-brown-500`, `adsk-brown-300`.<br>Using colors other than those specified here is not disallowed, but may result in unexpected behavior in<br>the Assets UI. |
| statusStepSetId   string: UUID | The ID of the status set to which the new status belongs. |
| id   string | The ID of the component. |
| createdAt   string | The time when the component was created (ISO8601 Date time format in UTC). |
| createdBy   string | The actor that created the component. This is an Autodesk / Oxygen ID. |
| updatedAt   string | The time when the component was last updated (ISO8601 Date time format in UTC). |
| updatedBy   string | The actor that last updated the component. This is an Autodesk / Oxygen ID. |
| deletedAt   string | The time when the component was deleted at (ISO8601 Date time format in UTC). |
| deletedBy   string | The actor that deleted the component. This is an Autodesk / Oxygen ID. |
| isActive   boolean | A flag indicating whether the component is active or inactive (`isActive` is `true` if-and-only-if `deletedAt` is empty). |
| version   int | A global sequence number that is incremented any time a component of this type is created, updated, or deleted. If you cache components, you can use the version value to compare the cached component to the same component online to see if the component has been updated. If the online component has a higher version value, it has been updated. |
| projectId   string: UUID | The Forma project ID. Must be a UUID or a project ID of the form “b.{UUID}”. |
| bucket   string | An immutable string assigned to a status on its creation, typically created by incorporating the status’s label into a larger string that is guaranteed to be unique within a project. The bucket name remains the same for the life of the status, and doesn’t change even if the label does. The bucket value is a useful tool for semantic identification. |
| sortOrder   int | A value that indicates the order of a status within its status set. Each status in the set has a sort order value that indicates its order relative to other statuses in the set. A status set’s sort order values don’t necessarily start at 1, and may not be sequential. The only way to know a status’s order within a set is to compare its sort order value with the sort order values of other statuses. |

## [Example](#example)

Successfully created a new status set.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v1/projects/:projectId/status-step-sets?renameConflicting=true' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "Spatiotemporal Status Set",
        "description": "My really cool status step set",
        "values": [
          {
            "label": "Functional-Testing",
            "description": "Custom Functional Testing Status",
            "color": "green"
          }
        ]
      }'

```

Show More

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
  "name": "Spatiotemporal Status Set",
  "description": "My really cool status step set",
  "isDefault": false,
  "values": [
    {
      "label": "Functional-Testing",
      "description": "Custom Functional Testing Status",
      "color": "green",
      "statusStepSetId": "6eb35939-e5fb-453a-98ed-e2e11f326e73",
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
      "bucket": "custom_functional_testing_status_1582935184385",
      "sortOrder": 1
    }
  ]
}

```

Show More
