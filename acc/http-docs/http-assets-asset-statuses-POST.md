# asset-statuses

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-asset-statuses-POST/

---

Statuses

POST

# asset-statuses

Creates a new asset status.

This endpoint defines the new status and specifies a status set to which the new status will belong. A status
may only belong to one status set.

To understand the basics of asset statuses, and the Assets settings that define them, see the [Assets Field Guide](/en/docs/acc/v1/overview/field-guide/assets/).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/assets/v1/projects/{projectId}/asset-statuses |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` `data:create` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

| label*   string | The display label of the status. This label appears in the Assets UI when viewing statuses. The label must be unique within this status set, but does not need to be unique within the project (in other words, the same label can be used in multiple status sets in the same project). âUniquenessâ in this context means case-insensitive. |
| --- | --- |
| description   string | A description of the status. |
| color   string | The color of the status as the status appears in the Assets UI. <br>This field is not restricted as it is primarily a tool for the Assets UI to use.<br>However, there are only certain colors that the Autodesk Construction Cloud Assets UI knows how to operate with. Understood color values are: `adsk-black`, `adsk-white`, `adsk-charcoal-900`, `adsk-charcoal-800`, `adsk-charcoal-700`, `adsk-charcoal-600`, `adsk-charcoal-500`, `adsk-charcoal-400`, `adsk-charcoal-300`, `adsk-charcoal-200`, `adsk-charcoal-100`, `adsk-charcoal-050`, `adsk-blue-700`, `adsk-blue-500`, `adsk-blue-300`, `adsk-blue-100`, `adsk-red-700`, `adsk-red-500`, `adsk-red-300`, `adsk-green-700`, `adsk-green-500`, `adsk-green-300`, `adsk-yellow-orange-700`, `adsk-yellow-orange-500`, `adsk-yellow-orange-300`, `adsk-dark-blue-700`, `adsk-dark-blue-500`, `adsk-dark-blue-300`, `adsk-pink-700`, `adsk-pink-500`, `adsk-pink-300`, `adsk-turquoise-700`, `adsk-turquoise-500`, `adsk-turquoise-300`, `adsk-purple-700`, `adsk-purple-500`, `adsk-purple-300`, `adsk-salmon-700`, `adsk-salmon-500`, `adsk-salmon-300`, `adsk-brown-700`, `adsk-brown-500`, `adsk-brown-300`.<br>Using colors other than those specified here is not disallowed, but may result in unexpected behavior in<br>the Assets UI. |
| statusStepSetId*   string: UUID | The ID of the status set to which the new status belongs. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Successfully created a new status. |
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

| label   string | The display label of the status. This label appears in the Assets UI when viewing statuses. The label must be unique within this status set, but does not need to be unique within the project (in other words, the same label can be used in multiple status sets in the same project). âUniquenessâ in this context means case-insensitive. |
| --- | --- |
| description   string | A description of the status. |
| color   string | The color of the status as the status appears in the Assets UI. <br>This field is not restricted as it is primarily a tool for the Assets UI to use.<br>However, there are only certain colors that the Autodesk Construction Cloud Assets UI knows how to operate with. Understood color values are: `adsk-black`, `adsk-white`, `adsk-charcoal-900`, `adsk-charcoal-800`, `adsk-charcoal-700`, `adsk-charcoal-600`, `adsk-charcoal-500`, `adsk-charcoal-400`, `adsk-charcoal-300`, `adsk-charcoal-200`, `adsk-charcoal-100`, `adsk-charcoal-050`, `adsk-blue-700`, `adsk-blue-500`, `adsk-blue-300`, `adsk-blue-100`, `adsk-red-700`, `adsk-red-500`, `adsk-red-300`, `adsk-green-700`, `adsk-green-500`, `adsk-green-300`, `adsk-yellow-orange-700`, `adsk-yellow-orange-500`, `adsk-yellow-orange-300`, `adsk-dark-blue-700`, `adsk-dark-blue-500`, `adsk-dark-blue-300`, `adsk-pink-700`, `adsk-pink-500`, `adsk-pink-300`, `adsk-turquoise-700`, `adsk-turquoise-500`, `adsk-turquoise-300`, `adsk-purple-700`, `adsk-purple-500`, `adsk-purple-300`, `adsk-salmon-700`, `adsk-salmon-500`, `adsk-salmon-300`, `adsk-brown-700`, `adsk-brown-500`, `adsk-brown-300`.<br>Using colors other than those specified here is not disallowed, but may result in unexpected behavior in<br>the Assets UI. |
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
| projectId   string: UUID | The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â. |
| bucket   string | An immutable string assigned to a status on its creation, typically created by incorporating the statusâs label into a larger string that is guaranteed to be unique within a project. The bucket name remains the same for the life of the status, and doesnât change even if the label does. The bucket value is a useful tool for semantic identification. |
| sortOrder   int | A value that indicates the order of a status within its status set. Each status in the set has a sort order value that indicates its order relative to other statuses in the set. A status setâs sort order values donât necessarily start at 1, and may not be sequential. The only way to know a statusâs order within a set is to compare its sort order value with the sort order values of other statuses. |

## [Example](#example)

Successfully created a new status.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v1/projects/:projectId/asset-statuses' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "label": "Functional-Testing",
        "description": "Custom Functional Testing Status",
        "color": "green",
        "statusStepSetId": "6eb35939-e5fb-453a-98ed-e2e11f326e73"
      }'

```

Show More

### Response

```
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

```

Show More
