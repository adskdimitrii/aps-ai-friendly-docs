# v3/projects/{projectId}/rfis/{rfiId}/comments

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-rfis-rfiId-comments-GET/

---

Comments

GET

# v3/projects/{projectId}/rfis/{rfiId}/comments

Retrieves a list of comments associated with a specific RFI.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfis/:rfiId/comments |
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

- projectIdstring The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- rfiIdstring The ID of the RFI. To find the ID, call [POST search:rfis](http-rfis-rfi-search-POST.md).

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The number of RFIs to return in the response. Acceptable values: `1–200`. Default: `10`. For example, to limit the response to two items per page, use `limit=2` |
| --- | --- |
| offset   int | The number of items to skip before starting to return results. <br>For example, to begin the results from the fourth item, use `offset=3`. |
| sort   array: string | The fields to sort the list by |
| fields   array: string | Specify which attributes you want to see in the response. Separate multiple values with commas. For example, `fields = title,description`. |
| filter[createdAt]   string | Retrieves comments created after the specified date, in the following format: YYYY-MM-DDThh:mm:ss.sz, or a date range in the following format: YYYY-MM-DDThh:mm:ss.sz..YYYY-MM-DDThh:mm:ss.sz. |
| filter[createdBy]   array: string | Retrieves comments created by the user. For example, `filter[createdBy]=PER8KQPK2JRT` |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success |
| --- | --- |
| 400   Bad Request | The parameters are invalid |
| 401   Unauthorized | The provided bearer token is not valid |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation |
| 404   Not Found | RFI not found |
| 500   Internal Server Error | An unknown error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | A list of comments associated with the RFI. |
| --- | --- |
| id   string | The unique identifier of the comment. |
| body   string | The content of the comment. |
| createdBy   string | The Autodesk ID of the user who created the comment. <br>To check the name of the user, call [GET users](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-v1-projects-projectId-users-GET/). |
| createdAt   datetime: ISO 8601 | The timestamp of the date and time the comment was created, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| updatedAt   datetime: ISO 8601 | The timestamp of the date and time the comment was updated, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| source   enum:string | The source of the comment. Indicates how the comment was created. Possible values:  > `web` – The comment was created through the web interface or API.`email` – The comment was created by replying via email. |
| pagination   object | The pagination object. |
| limit   int | The number of items returned per page. |
| offset   int | The number of items skipped before this page of results. |
| totalResults   int | The total number of items matching the request. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfis/:rfiId/comments' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "id": "94ce6921-e8f9-4bc5-bf5a-1a8f543a2564",
      "body": "This needs more attention.",
      "createdBy": "PER8KQPK2JRT",
      "createdAt": "2018-08-01T08:56:48.699Z",
      "updatedAt": "2019-08-01T08:56:48.699Z",
      "source": "web"
    }
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 97
  }
}

```

Show More
