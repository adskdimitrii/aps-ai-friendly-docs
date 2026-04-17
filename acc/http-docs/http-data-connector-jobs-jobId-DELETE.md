# accounts/{accountId}/jobs/{jobId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/data-connector-jobs-jobId-DELETE/

---

Jobs

DELETE

# accounts/{accountId}/jobs/{jobId}

Cancels the specified running job spawned by a data request created by the authenticated user. The user must have project administrator or executive overview permissions.

Use [GET requests/:requestId/jobs](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/data-connector-requests-requestid-jobs-GET/) to get the jobs spawned by a request along with their job IDs. A cancelled job will still appear as a spawned job with a completion status of `cancelled`.

To understand the basics of requests, the jobs they spawn, and the data extracts returned by the jobs, see the [Data Connector API Field Guide](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/data-connector/).

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/jobs/:jobId |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| accountId   string: UUID | The ID of the hub. To obtain the hub ID, call [GET hubs](../../data/http-docs/http-hubs-GET.md) in the Data Management API and remove the “b.” prefix. |
| --- | --- |
| jobId   string: UUID | The job ID |

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
curl -v 'https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/jobs/:jobId' \
  -X 'DELETE' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
204 No Content

```
