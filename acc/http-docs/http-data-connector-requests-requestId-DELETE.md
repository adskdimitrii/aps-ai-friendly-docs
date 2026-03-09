# accounts/{accountId}/requests/{requestId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/data-connector-requests-requestId-DELETE/

---

Requests

DELETE

# accounts/{accountId}/requests/{requestId}

Deletes the specified data request created earlier by the authenticated user. Note that the user must have executive overview or project administrator permissions.

To get request IDs for your requests, use [GET requests](http-data-connector-requests-GET.md).

To understand the basics of requests, the jobs they spawn, and the data extracts returned by the jobs, see the [Data Connector API Field Guide](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/data-connector/).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/requests/:requestId |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| accountId   string: UUID | The account ID. You can derive it from your hub ID if necessary: Use [GET hubs](../../data/http-docs/http-hubs-GET.md) in the Data Management API to retrieve your hub ID. Remove the initial âb.â from the hub ID to get your account ID. |
| --- | --- |
| requestId   string: UUID | The ID of the specified request |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | The specified object is successfully deleted. |
| --- | --- |
| 400   Bad Request | The parameters are invalid. |
| 401   Unauthorized | The provided bearer token is invalid. |
| 403   Forbidden | Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The resource or endpoint cannot be found. |
| 429   Too Many Requests | Rate limited exceeded; wait some time before retrying. |
| 500   Internal Server Error | An unexpected error occurred on the server. |
| 503   Service Unavailable | Service unavailable. |

### Response

## [Body Structure (204)](#body-structure-204)

Response for 204 has no body.

## [Example](#example)

The specified object is successfully deleted.

### Request

```
curl -v 'https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/requests/:requestId' \
  -X 'DELETE' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
204 No Content

```
