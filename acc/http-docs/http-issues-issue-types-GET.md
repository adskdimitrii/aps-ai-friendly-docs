# projects/{projectId}/issue-types

Source: https://aps.autodesk.com/en/docs/acc/reference/http/issues-issue-types-GET/

---

Issue Types

GET

# projects/{projectId}/issue-types

Retrieves a project’s categories and types. Note the following differences in terminology between the product and the API:

| Product Name | API Name |
| --- | --- |
| Category | Type |
| Type | Subtype |

Note that by default this endpoint does not return types (subtypes). To return types (subtypes), you need to add the `include=subtypes` query string parameter.

Note that this endpoint does not return deleted items.

This operation is available to everyone.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/issues/v1/projects/{projectId}/issue-types |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-ads-region   string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`.<br>For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| include   string | Use `include=subtypes` to include the types (subtypes) for each category (type). |
| --- | --- |
| limit   int | Add `limit=20` to limit the results count (together with the offset to support pagination). |
| offset   int | Add `offset=20` to get partial results (together with the limit to support pagination). |
| filter[updatedAt]   string | Retrieves types that were last updated at the specified date and time, in in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03` or `2022-02-28T22:00:00.000Z..2022-03-28T22:00:00.000Z`Specific day: e.g., `2022-03-02` or `2022-02-28T22:00:00.000Z`Specific start date: e.g., `2022-03-02..` or `2022-02-28T22:00:00.000Z..`Specific end date: e.g., `..2022-03-02` or `..2022-02-28T22:00:00.000Z`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[isActive]   boolean | Filter types by status e.g. `filter[isActive]=true` will only return active types. Default value: `undefined` (meaning both active & inactive issue type categories will return). |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | List of issue types |
| --- | --- |
| 400   Bad Request | Invalid input |
| 403   Forbidden | Unauthorized |
| 404   Not Found | Project not found |
| 500   Internal Server Error | Internal server error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| pagination   object | The pagination object. |
| --- | --- |
| limit   int | The number of items per page. |
| offset   int | The page number that the results begin from. |
| totalResults   int | The number of items in the response. |
| results   array: object | A list of issue type categories. |
| id   string: UUID | The ID of the issue type. |
| containerId   string: UUID | Not relevant |
| title   string | Max length: 250 |
| isActive   boolean | States whether the issue type is active. |
| orderIndex   int | Not relevant |
| permittedActions   array: string | Not relevant |
| permittedAttributes   array: string | Not relevant |
| subtypes   array: object | A list of subtypes of the specific issue type. |
| id   string: UUID | The ID of the issue subtype. |
| issueTypeId   string: UUID | The ID of the parent issue type. |
| title   string | Max length: 250 |
| code   string | 3 chars pin label. <br>Max length: 3 |
| isActive   boolean | Stated whether the issue subtype is active. |
| orderIndex   int | Not relevant |
| isReadOnly   boolean | Not relevant |
| permittedActions   array: string | Not relevant |
| permittedAttributes   array: string | Not relevant |
| createdBy   string | The unique identifier of the user who created the issue type. |
| createdAt   datetime: ISO 8601 | The date and time the issue was created, in ISO8601 format. |
| updatedBy   string | The unique identifier of the user who updated the issue type. |
| updatedAt   datetime: ISO 8601 | The date and time the issue type was updated, in ISO8601 format. |
| deletedBy   string | The unique identifier of the user who deleted the issue type. |
| deletedAt   datetime: ISO 8601 | The date and time the issue type was deleted, in ISO8601 format. |
| statusSet   string | Not relevant |
| createdBy   string | The unique identifier of the user who created the issue type. |
| createdAt   datetime: ISO 8601 | The date and time the issue was created, in ISO8601 format. |
| updatedBy   string | The unique identifier of the user who updated the issue type. |
| updatedAt   datetime: ISO 8601 | The date and time the issue type was updated, in ISO8601 format. |
| deletedBy   string | The unique identifier of the user who deleted the issue type. |
| deletedAt   datetime: ISO 8601 | The date and time the issue type was deleted, in ISO8601 format. |

## [Example](#example)

List of issue types

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/:projectId/issue-types' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 10,
    "offset": 100,
    "totalResults": 25
  },
  "results": [
    {
      "id": "1110f111-6c54-4b01-90e6-d701748f1111",
      "containerId": "a5f49f04-59bb-477c-97e6-6833cb50bdac",
      "title": "Coordination",
      "isActive": true,
      "orderIndex": 2,
      "permittedActions": [
        "edit"
      ],
      "permittedAttributes": [
        "title"
      ],
      "subtypes": [
        {
          "id": "2220f222-6c54-4b01-90e6-d701748f0222",
          "issueTypeId": "1110f111-6c54-4b01-90e6-d701748f1111",
          "title": "Clash",
          "code": "exo",
          "isActive": true,
          "orderIndex": 5,
          "isReadOnly": false,
          "permittedActions": [
            "edit"
          ],
          "permittedAttributes": [
            "title"
          ],
          "createdBy": "A3RGM375QTZ7",
          "createdAt": "2018-07-22T15:05:58.033Z",
          "updatedBy": "A3RGM375QTZ7",
          "updatedAt": "2018-07-22T15:05:58.033Z",
          "deletedBy": "A3RGM375QTZ7",
          "deletedAt": "2018-07-22T15:05:58.033Z"
        }
      ],
      "statusSet": "gg",
      "createdBy": "A3RGM375QTZ7",
      "createdAt": "2018-07-22T15:05:58.033Z",
      "updatedBy": "A3RGM375QTZ7",
      "updatedAt": "2018-07-22T15:05:58.033Z",
      "deletedBy": "A3RGM375QTZ7",
      "deletedAt": "2018-07-22T15:05:58.033Z"
    }
  ]
}

```

Show More
