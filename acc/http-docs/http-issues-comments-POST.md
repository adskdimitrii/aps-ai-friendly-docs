# projects/{projectId}/issues/{issueId}/comments

Source: https://aps.autodesk.com/en/docs/acc/reference/http/issues-comments-POST/

---

Issue Comments

POST

# projects/{projectId}/issues/{issueId}/comments

Creates a new comment under a specific issue.

Creating comments for deleted issues is not allowed.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/issues/v1/projects/{projectId}/issues/{issueId}/comments |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-ads-region   string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`.<br>For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring: UUID The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- issueIdstring: UUID The unique identifier of the issue. To find the ID, call [GET issues](http-issues-issues-GET.md).

### Request

## [Body Structure](#body-structure)

The body content.

| body*   string | The comment content. A `\n` indicates a new line, e.g.: `Hey\nAharon` will be a 2 lines comment. <br>Max length: 10000 |
| --- | --- |
| createdBy   string | Not relevant |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Returns the created comment |
| --- | --- |
| 400   Bad Request | Invalid input |
| 403   Forbidden | The request is valid but lacks the necessary permissions. |
| 404   Not Found | Project not found |
| 409   Conflict | The request contained a data conflict |
| 500   Internal Server Error | Internal server error |

### Response

## [Body Structure (201)](#body-structure-201)

| id   string: UUID | The unique identifier for the comment. |
| --- | --- |
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

Returns the created comment

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/:projectId/issues/:issueId/comments' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "body": "Hey Aharon, please validate that this is even possible before starting to work on the issue.",
        "createdBy": "A3RGM375QTZ7"
      }'

```

Show More

### Response

```
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

```

Show More
