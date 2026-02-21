# activities/:id/versions/:version

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/activities-id-versions-version-DELETE/

---

DELETE

# activities/:id/versions/:version

Deletes the specified version of the Activity.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/da/us-east/v3/activities/:id/versions/:version |
| --- | --- |
| Authentication Context | app only |
| Required OAuth Scopes | `code:all` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](/en/docs/oauth/v2/reference/http/gettoken-POST) |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| id   string | Name of Activity (unqualified). |
| --- | --- |
| version   int | Version to delete (integer). |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | No content. |
| --- | --- |
| 403   Forbidden | Unauthorized |
| 409   Conflict | An item with this name already exists. |
| 500   Internal Server Error | Unknown error. |

## [Example](#example)

No content.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/activities/:id/versions/:version' \
  -X 'DELETE' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
204 No Content

```
