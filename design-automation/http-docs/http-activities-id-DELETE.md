# activities/:id

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/activities-id-DELETE/

---

DELETE

# activities/:id

Deletes the specified Activity, including all versions and aliases.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/da/us-east/v3/activities/:id |
| --- | --- |
| Authentication Context | app only |
| Required OAuth Scopes | `code:all` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](../../oauth/http-docs/http-gettoken-POST.md) |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| id   string | Name of Activity (unqualified). |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | OK. |
| --- | --- |
| 403   Forbidden | Unauthorized |
| 404   Not Found | Not found. |
| 500   Internal Server Error | Unknown error. |

## [Example](#example)

OK.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/activities/:id' \
  -X 'DELETE' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
204 No Content

```
