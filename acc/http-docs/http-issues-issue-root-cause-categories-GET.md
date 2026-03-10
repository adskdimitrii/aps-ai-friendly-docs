# projects/{projectId}/issue-root-cause-categories

Source: https://aps.autodesk.com/en/docs/acc/reference/http/issues-issue-root-cause-categories-GET/

---

Issue Root Cause Categories

GET

# projects/{projectId}/issue-root-cause-categories

Retrieves a list of supported root cause categories and root causes that you can allocate to an issue. For example, communication and coordination.

Note that by default, this endpoint only returns root cause categories. To include root causes you need to to add the `include` query string parameter (`include=rootcauses`).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/issues/v1/projects/{projectId}/issue-root-cause-categories |
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

| include   string | Add ‘include=rootcauses’ to add the root causes for each category. |
| --- | --- |
| limit   int | Add `limit=20` to limit the results count (together with the offset to support pagination). |
| offset   int | Add `offset=20` to get partial results (together with the limit to support pagination). |
| filter[updatedAt]   string | Retrieves root cause categories updated at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03` or `2022-02-28T22:00:00.000Z..2022-03-28T22:00:00.000Z`Specific day: e.g., `2022-03-02` or `2022-02-28T22:00:00.000Z`Specific start date: e.g., `2022-03-02..` or `2022-02-28T22:00:00.000Z..`Specific end date: e.g., `..2022-03-02` or `..2022-02-28T22:00:00.000Z`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | List of issue root cause categories |
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
| results   array: object | A list of issue root cause categories. |
| id   string: UUID | The ID of the issue root cause category. |
| title   string | The title of the issue root cause category. <br>Max length: 100 |
| isActive   boolean | States whether the root cause category is active. |
| permittedActions   array: string | Not relevant |
| permittedAttributes   array: string | Not relevant |
| rootCauses   array: object | A list of root causes of the specific root cause category. |
| id   string: UUID | The ID of the issue root cause. |
| rootCauseCategoryId   string: UUID | The ID of the parent issue root cause category. |
| title   string | The title of the issue root cause. <br>Max length: 100 |
| isActive   boolean | States whether the root cause is active. |
| permittedActions   array: string | Not relevant |
| permittedAttributes   array: string | Not relevant |
| createdAt   datetime: ISO 8601 | The date and time the issue root cause was created, in the following format: YYYY-MM-DDThh:mm:ss.sz. |
| createdBy   string | The Autodesk ID of the user who created the issue root cause. |
| updatedAt   datetime: ISO 8601 | The last date and time the issue root cause was updated, in the following format: YYYY-MM-DDThh:mm:ss.sz. |
| updatedBy   string | The Autodesk ID of the user who last updated the issue root cause. |
| deletedAt   datetime: ISO 8601 | The date and time the issue root cause was deleted, in the following format: YYYY-MM-DDThh:mm:ss.sz. |
| deletedBy   string | The Autodesk ID of the user who deleted the issue root cause. |
| createdAt   datetime: ISO 8601 | The date and time the issue root cause category was created, in the following format: YYYY-MM-DDThh:mm:ss.sz. |
| createdBy   string | The Autodesk ID of the user who created the issue root cause category. |
| updatedAt   datetime: ISO 8601 | The last date and time the issue root cause category was updated, in the following format: YYYY-MM-DDThh:mm:ss.sz. |
| updatedBy   string | The Autodesk ID of the user who last updated the issue root cause category. |
| deletedAt   datetime: ISO 8601 | The date and time the issue root cause category was deleted, in the following format: YYYY-MM-DDThh:mm:ss.sz. |
| deletedBy   string | The Autodesk ID of the user who deleted the issue root cause category. |

## [Example](#example)

List of issue root cause categories

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/:projectId/issue-root-cause-categories' \
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
      "title": "Coordination",
      "isActive": false,
      "permittedActions": [
        "edit"
      ],
      "permittedAttributes": [
        "title"
      ],
      "rootCauses": [
        {
          "id": "2220f222-6c54-4b01-90e6-d701748f0222",
          "rootCauseCategoryId": "1110f111-6c54-4b01-90e6-d701748f1111",
          "title": "Constructability",
          "isActive": false,
          "permittedActions": [
            "edit"
          ],
          "permittedAttributes": [
            "title"
          ],
          "createdAt": "2018-07-22T15:05:58.033Z",
          "createdBy": "A3RGM375QTZ7",
          "updatedAt": "2018-07-22T15:05:58.033Z",
          "updatedBy": "A3RGM375QTZ7",
          "deletedAt": "2018-07-22T15:05:58.033Z",
          "deletedBy": "A3RGM375QTZ7"
        }
      ],
      "createdAt": "2018-07-22T15:05:58.033Z",
      "createdBy": "A3RGM375QTZ7",
      "updatedAt": "2018-07-22T15:05:58.033Z",
      "updatedBy": "A3RGM375QTZ7",
      "deletedAt": "2018-07-22T15:05:58.033Z",
      "deletedBy": "A3RGM375QTZ7"
    }
  ]
}

```

Show More
