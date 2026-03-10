# workitems/:id

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/workitems-id-DELETE/

---

DELETE

# workitems/:id

Cancels a specific WorkItem.

If the WorkItem is on the queue, it is removed from the queue and not processed.

If the WorkItem is already being processed, then it may or may not be interrupted and cancelled.

If the WorkItem has already finished processing, then it has no effect on the processing or results.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/da/us-east/v3/workitems/:id |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `code:all` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| id   string | The GUID used to identify the WorkItem. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | OK. |
| --- | --- |
| 403   Forbidden | The user is not authorized to modify the WorkItem status. |
| 404   Not Found | The WorkItem doesn’t exist. |
| 409   Conflict | Conflict. |
| 500   Internal Server Error | Unknown error. |

## [Example](#example)

OK.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/workitems/:id' \
  -X 'DELETE' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
204 No Content

```
