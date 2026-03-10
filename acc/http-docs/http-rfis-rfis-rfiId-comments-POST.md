# v3/projects/{projectId}/rfis/{rfiId}/comments

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-rfis-rfiId-comments-POST/

---

Comments

POST

# v3/projects/{projectId}/rfis/{rfiId}/comments

Adds a comment to an RFI.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfis/:rfiId/comments |
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

- projectIdstring The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- rfiIdstring The ID of the RFI. To find the ID, call [POST search:rfis](http-rfis-rfi-search-POST.md).

### Request

## [Body Structure](#body-structure)

| id   string: UUID | The comment ID. Leave empty if you want to let the system generate one. |
| --- | --- |
| body   string | The content of the comment. <br>Max length: 10000 |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Created |
| --- | --- |
| 400   Bad Request | The parameters are invalid |
| 401   Unauthorized | The provided bearer token is not valid |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation |
| 500   Internal Server Error | An unknown error occurred on the server |

### Response

## [Body Structure (201)](#body-structure-201)

| id   string | The unique identifier of the comment. |
| --- | --- |
| body   string | The content of the comment. |
| createdBy   string | The Autodesk ID of the user who created the comment. <br>To check the name of the user, call [GET users](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-v1-projects-projectId-users-GET/). |
| createdAt   datetime: ISO 8601 | The timestamp of the date and time the comment was created, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| updatedAt   datetime: ISO 8601 | The timestamp of the date and time the comment was updated, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| source   enum:string | The source of the comment. Indicates how the comment was created. Possible values:  > `web` – The comment was created through the web interface or API.`email` – The comment was created by replying via email. |
| rfiId   string | The ID of the RFI associated with this comment. |

## [Example](#example)

Created

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfis/:rfiId/comments' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "id": "",
        "body": "This needs more attention."
      }'

```

Show More

### Response

```
{
  "id": "94ce6921-e8f9-4bc5-bf5a-1a8f543a2564",
  "body": "This needs more attention.",
  "createdBy": "PER8KQPK2JRT",
  "createdAt": "2018-08-01T08:56:48.699Z",
  "updatedAt": "2019-08-01T08:56:48.699Z",
  "source": "web",
  "rfiId": "f73e4dd9-cd44-4b3e-8651-901ba2e8bc8d"
}

```

Show More
