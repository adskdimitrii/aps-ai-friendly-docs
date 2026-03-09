# categories:batch-get

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-categories-batch-get-POST/

---

Categories

POST

# categories:batch-get

Returns a specified set of categories.

This endpoint accepts an object with an array of one or more category IDs and returns an array of categories
corresponding to each of those IDs. Invalid category IDs will simply be omitted from the response and the client
is responsible for identifying missing results.

To understand the basics of categories, category inheritance, and the Assets settings that define them, see the [Assets Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/assets/).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/assets/v1/projects/{projectId}/categories:batch-get |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| includeUid   boolean | If provided, and set to `true`, the globally-unique category `uid` field will be present in the response. The globally unique category ID is used with the (upcoming) `v3` category APIs. The option to include the globally-unique ID with the `v1` category APIs is to help consumers transition to the new IDs. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

| ids   array: string | Unique IDs of categories to fetch |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully returned a batch of categories. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found |
| 429   Too Many Requests | The request was not accepted because the rate limit was exceeded due to too many requests being made. |
| 500   Internal Server Error | An unexpected error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | Returned categories |
| --- | --- |
| id   string | The ID of the category. This is a numeric string for `v1` category APIs. |
| createdAt   string | The time when the component was created (ISO8601 Date time format in UTC). |
| createdBy   string | The actor that created the component. This is an Autodesk / Oxygen ID. |
| updatedAt   string | The time when the component was last updated (ISO8601 Date time format in UTC). |
| updatedBy   string | The actor that last updated the component. This is an Autodesk / Oxygen ID. |
| deletedAt   string | The time when the component was deleted at (ISO8601 Date time format in UTC). |
| deletedBy   string | The actor that deleted the component. This is an Autodesk / Oxygen ID. |
| isActive   boolean | A flag indicating whether the component is active or inactive (`isActive` is `true` if-and-only-if `deletedAt` is empty). |
| name   string | The name of the category. Must be unique among children of the same parent category. This name is displayed for the category in the Assets user interface where a user chooses categories. |
| description   string | A description of the category. |
| uid   string | The globally-unique ID of a `Category` from the `v3` (upcoming) Category APIs. This is provided for interoperability with other APIs that use the globally-unique category ID. Only included if the `includeUid=true` query param is included. |
| parentId   string | The ID of the categoryâs parent category. |
| isRoot   boolean | Whether or not this category is the root category of the category tree. If `true`, itâs the root; if `false`, itâs not. There will only ever be one (immutable) root category for a project, which is created automatically when the project is created. |
| isLeaf   boolean | Whether or not this category is a leaf category of the category tree. If `true`, itâs a leaf; if `false`, itâs not. <br>Note that this is a derived field and should not be persisted as this field may be updated without updating the category itself. |
| subcategoryIds   array: string | An array of category IDs of this categoryâs child categories. <br>Note that this is a derived field and should not be persisted as this field may be updated without updating the category itself. As such, it is highly recommended to use the `parentId` field to construct the tree locally instead of `subcategoryIds`. |

## [Example](#example)

Successfully returned a batch of categories.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v1/projects/:projectId/categories:batch-get?includeUid=true' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "ids": [
          "123"
        ]
      }'

```

Show More

### Response

```
{
  "results": [
    {
      "id": "123",
      "createdAt": "2020-05-01T06:00:00.000Z",
      "createdBy": "LA7ZL85MU7ML",
      "updatedAt": "2020-05-01T06:00:00.000Z",
      "updatedBy": "LA7ZL85MU7ML",
      "deletedAt": "2020-05-01T06:00:00.000Z",
      "deletedBy": "LA7ZL85MU7ML",
      "isActive": true,
      "name": "Electrical",
      "description": "Electrical Outlets",
      "uid": "b4511bcd-e141-4253-8607-26b194de4ae3",
      "parentId": "122",
      "isRoot": false,
      "isLeaf": false,
      "subcategoryIds": [
        "124",
        "125"
      ]
    }
  ]
}

```

Show More
