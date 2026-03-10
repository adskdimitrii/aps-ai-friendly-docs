# projects/{projectId}/users/{userId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/admin-projects-project-Id-users-userId-DELETE/

---

projects/:project_id/users/:user_id

DELETE

# projects/{projectId}/users/{userId}

Removes the specified user from a project.

Note that the `Authorization` header token can be obtained either via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow, or via a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) Oauth flow *with user impersonation*, for which the `User-Id` header is required.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/construction/admin/v1/projects/:projectId/users/:userId |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `account:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Region   string | Specifies the region where your request should be routed. If not set, the request is routed automatically, which may result in a slight increase in latency. <br>Possible values: `US`, `EMEA`. For a complete list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |
| User-Id   string | The ID of a user on whose behalf your request is acting. <br>Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.<br>You can use either the user’s ACC ID (`id`), or their Autodesk ID (`autodeskId`).<br>Note that this header is required for Account Admin POST, PATCH, and DELETE endpoints if you want to use a 2-legged authentication context. This header is optional for Account Admin GET endpoints. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. This corresponds to project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). To convert a project ID in the Data Management API into a project ID in the ACC API you need to remove the “**b.**" prefix. For example, a project ID of `b.a4be0c34a-4ab7` translates to a project ID of `a4be0c34a-4ab7`. |
| --- | --- |
| userId   string | The ID of the user. To find the ID call [GET users](http-admin-projectsprojectId-users-GET.md). You can use either the ACC ID (`id`) or the Autodesk ID (`autodeskId`). |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | The request has succeeded, no content returned. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax. |
| 401   Unauthorized | Request has not been applied because it lacks valid authentication credentials for the target resource. |
| 403   Forbidden | The server understood the request but refuses to authorize it. |
| 404   Not Found | The resource could not be found. |
| 410 | Access to the target resource is no longer available. |
| 415 | The server refuses to accept the request because the payload format is in an unsupported format. |
| 429   Too Many Requests | User has sent too many requests in a given amount of time. |
| 500   Internal Server Error | An unexpected error occurred on the server. |
| 503   Service Unavailable | Server is not ready to handle the request. |

### Response

## [Body Structure (204)](#body-structure-204)

Response for 204 has no body.

## [Example](#example)

The request has succeeded, no content returned.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/admin/v1/projects/367d5cc2-9008-462c-96e5-c9491db85d93/users/6cc15635-2fbd-4f73-afbe-abd833408a1d' \
  -X 'DELETE' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
204 No Content

```
