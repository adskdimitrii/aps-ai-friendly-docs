# forgeapps/:id

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/forgeapps-id-DELETE/

---

DELETE

# forgeapps/:id

Delete all data associated with the given app.

All AppBundles and Activities are DELETED.

This may take up to 2 minutes. During this time the app will not be able to make successful requests.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/da/us-east/v3/forgeapps/:id |
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

| id   string | Must be âmeâ for the call to succeed. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | OK. |
| --- | --- |
| 403   Forbidden | Forbidden. |
| 409   Conflict | Conflict. |
| 500   Internal Server Error | Unknown error. |

## [Example](#example)

OK.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/forgeapps/:id' \
  -X 'DELETE' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
204 No Content

```
