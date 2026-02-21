# appbundles/:id

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/appbundles-id-DELETE/

---

DELETE

# appbundles/:id

Deletes the specified AppBundle, including all versions and aliases.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id |
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

| id   string | Name of AppBundle (unqualified). |
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
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id' \
  -X 'DELETE' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
204 No Content

```
