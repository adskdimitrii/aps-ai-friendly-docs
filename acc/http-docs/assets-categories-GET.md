# categories

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-categories-GET/

---

Categories

GET

# categories

Searches for and returns all specified categories.

This endpoint accepts a set of optional category property filters, then uses supplied filters to search for and
return categories within a project that satisfy those filters. If no filters are set, this endpoint returns all
categories within a project.

Note that although the endpoint returns pagination fields for API consistency, the endpoint does not support
pagination in requests.

To understand the basics of categories, category inheritance, and the Assets settings that define them, see the [Assets Field Guide](/en/docs/acc/v1/overview/field-guide/assets/).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/assets/v1/projects/{projectId}/categories |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| filter[isActive]   boolean | Specifies whether or not to return categories that are active. If `true`, return only active categories. If `false`, return only inactive categories. Default is to return both active and inactive categories, to ensure full tree structure is returned (conversely, full tree structure is not guaranteed when filtering active or inactive categories). <br>Note that this behavior is different than that of the `includeDeleted` flag other endpoints use. |
| --- | --- |
| filter[parentId]   string | Specifies the parent category ID of returned categories. The query returns only categories that are direct child categories of the specified category. |
| filter[maxDepth]   number | Specifies the depth of the category tree to return, starting with the root category. Depth `0` means to return only the root category. Depth `4`, for example, means to return only the root category and categories that are four levels of inheritance deep, but not to return categories that are five or more levels deep. <br>Note that this can be used in conjunction with `filter[parentId]`, but that the depth is still computed from the root category, not the parent category specified by the filter. |
| filter[updatedAt]   string | A string that specifies a date and time or a date and time range at which all returned objects mast have been updated. A single date and time takes this format: `YYYY-MM-DDThh:mm:ss.SSSZ`, A date and time range takes this format: `YYYY-MM-DDThh:mm:ss.SSSZ..YYYY-MM-DDThh:mm:ss.SSSZ`. Range queries can be closed or open in either direction: `YYYY-MM-DDThh:mm:ss.SSSZ..` or `..YYYY-MM-DDThh:mm:ss.SSSZ`. |
| includeUid   boolean | If provided, and set to `true`, the globally-unique category `uid` field will be present in the response. The globally unique category ID is used with the (upcoming) `v3` category APIs. The option to include the globally-unique ID with the `v1` category APIs is to help consumers transition to the new IDs. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully returned a page of categories. |
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

| pagination   object | The pagination object. |
| --- | --- |
| limit   int | The maximum number of objects that can be returned in a page. A request might return fewer objects than the limit if the Assets service runs out of specified objects to return - at the end of a set of paged results, for example. The maximum limit is `200`; the default limit is `25`. |
| offset   int | The offset of the first entry in the pagination results. |
| totalResults   int | Total number of results available. |
| results   array: object | Result categories |
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

Successfully returned a page of categories.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v1/projects/:projectId/categories?filter[isActive]=true&filter[parentId]=122&filter[maxDepth]=3&filter[updatedAt]=2020-05-01T06:00:00.000Z..&includeUid=true' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 25,
    "offset": 0,
    "totalResults": 100
  },
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
