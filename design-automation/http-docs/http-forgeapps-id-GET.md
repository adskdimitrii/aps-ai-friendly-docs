# forgeapps/:id

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/forgeapps-id-GET/

---

GET

# forgeapps/:id

Return the given appâs nickname.

If the app has no nickname, this route will return its id.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/da/us-east/v3/forgeapps/:id |
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

| 200   OK | Successfully get the userâs nickname. |
| --- | --- |
| 403   Forbidden | Forbidden. |
| 500   Internal Server Error | Unknown error. |

## [Example](#example)

Successfully get the userâs nickname.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/forgeapps/:id' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
""

```
