# assets:batch-delete V2

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-assets-batch-delete-v2-POST/

---

Assets

POST

# assets:batch-delete V2

Deletes one or more assets.

This endpoint accepts an object with an array of one or more asset IDs, then soft deletes each of the specified
assets. When an asset is soft deleted, it becomes inactive but its record remains so it can be retrieved and
examined.

To understand the basics of assets and the Assets settings that define them, see the [Assets Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/assets/).

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/assets/v2/projects/{projectId}/assets:batch-delete |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The Forma project ID. Must be a UUID or a project ID of the form “b.{UUID}”. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

Request payload for deleting a batch of Assets by IDs

| ids   array: string | An array of unique IDs of assets to delete. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | Successfully soft-deleted a batch of assets. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the target resource |
| 429   Too Many Requests | The request was not accepted because the rate limit was exceeded due to too many requests being made. |
| 500   Internal Server Error | An unexpected error occurred on the server |

### Response

## [Body Structure (204)](#body-structure-204)

Response for 204 has no body.

## [Example](#example)

Successfully soft-deleted a batch of assets.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v2/projects/:projectId/assets:batch-delete' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "ids": [
          "6cdd4356-a719-4964-9fd7-0c505e731ac7"
        ]
      }'

```

Show More

### Response

```
204 No Content

```
