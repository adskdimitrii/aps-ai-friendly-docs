# projects/{projectId}/issues/{issueId}/comments

Source: https://aps.autodesk.com/en/docs/acc/reference/http/issues-comments-GET/

---

Issue Comments

GET

# projects/{projectId}/issues/{issueId}/comments

Get all the comments for a specific issue.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/issues/v1/projects/{projectId}/issues/{issueId}/comments |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context.
- x-ads-regionstring The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: `US`, `EMEA`.For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring: UUID The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- issueIdstring: UUID The unique identifier of the issue. To find the ID, call [GET issues](http-issues-issues-GET.md).

### Request

## [Query String Parameters](#query-string-parameters)

| sortBy   array: string | Sort issue comments by specified fields. Separate multiple values with commas. To sort in descending order add a `-` (minus sign) before the sort criteria. For example: `sortBy=createdAt,-updatedAt`. Possible values: `createdAt`, `updatedAt`, `createdBy`. |
| --- | --- |
| limit   int | Add `limit=20` to limit the results count (together with the offset to support pagination). |
| offset   int | Add `offset=20` to get partial results (together with the limit to support pagination). |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | List of comments of the specific requested issue in combination with pagination details |
| --- | --- |
| 400   Bad Request | Invalid ID supplied |
| 403   Forbidden | The request is valid but lacks the necessary permissions. |
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
| results   array: object | A list of comments for the specified issue. |
| id   string: UUID | The unique identifier for the comment. |
| body   string | The comment content. A ` ` represents a new line. For example, HeynAharon will appear as a two-line comment. <br>Max length: 10000 |
| createdAt   datetime: ISO 8601 | The date and time the comment was created, in the following format: YYYY-MM-DDThh:mm:ss.sz. |
| createdBy   string | The Autodesk ID of the user who created the comment. |
| updatedAt   datetime: ISO 8601 | Not relevant |
| deletedAt   datetime: ISO 8601 | Not relevant |
| clientCreatedAt   string | Not relevant |
| clientUpdatedAt   datetime: ISO 8601 | Not relevant |
| permittedActions   array: string | Not relevant |
| permittedAttributes   array: string | Not relevant |

## [Example](#example)

List of comments of the specific requested issue in combination with pagination details

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/:projectId/issues/:issueId/comments' \
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
      "id": "d26c0adb-bb27-4cec-b3ad-bae5ce5a0b29",
      "body": "Hey Aharon,\nPlease validate that this is even possible before starting work on the issue",
      "createdAt": "2018-07-22T15:05:58.033Z",
      "createdBy": "A3RGM375QTZ7",
      "updatedAt": "",
      "deletedAt": "",
      "clientCreatedAt": "A3RGM375QTZ7",
      "clientUpdatedAt": "2018-07-22T15:05:58.033Z",
      "permittedActions": [
        ""
      ],
      "permittedAttributes": [
        ""
      ]
    }
  ]
}

```

Show More
