# v1/containers/{containerId}/schedule-of-values/{id}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-schedule-of-values-id-DELETE/

---

Schedule Of Values

DELETE

# v1/containers/{containerId}/schedule-of-values/{id}

Deletes a specified schedule of values (SOV) item in the given project.

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/cost/v1/containers/:containerId/schedule-of-values/:id |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context.
- regionstring Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [Forma Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.To verify your project’s region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](https://aps.autodesk.com/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page.

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](http-admin-accounts-accountidprojects-GET.md). |
| --- | --- |
| id   array: string | The ID of the SOV items to delete, separated by commas. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | The resource has been deleted successfully. |
| --- | --- |
| 400   Bad Request | The parameters are invalid. |
| 401   Unauthorized | The provided bearer token is invalid. |
| 403   Forbidden | Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The resource or endpoint cannot be found. |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the resource. |
| 429   Too Many Requests | Rate limit exceeded. Retry your request after a few minutes. |
| 500   Internal Server Error | An unexpected error occurred on the server. |
| 503   Service Unavailable | Service unavailable. |

### Response

## [Body Structure (204)](#body-structure-204)

Response for 204 has no body.

## [Example](#example)

The resource has been deleted successfully.

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/schedule-of-values/226449d0-9481-11e8-87fb-215990a8aeb3' \
  -X 'DELETE' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
204 No Content

```
