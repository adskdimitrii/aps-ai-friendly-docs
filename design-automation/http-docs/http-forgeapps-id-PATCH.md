# forgeapps/:id

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/forgeapps-id-PATCH/

---

PATCH

# forgeapps/:id

Creates/updates the nickname for the current app. The nickname is
used as a clearer alternative name when identifying AppBundles and Activities, as
compared to using the Client ID. Once you have defined a nickname,
it MUST be used instead of the Client ID.

The new nickname cannot be in use by any other app.

The app cannot have any data when this endpoint is invoked. Use the ‘DELETE /forgeapps/me’
endpoint (cautiously!!!) to remove all data from this app. ‘DELETE /forgeapps/me’ is
also the only way to remove the nickname.

Note the nickname is supplied in the body, not as a query-parameter.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/da/us-east/v3/forgeapps/:id |
| --- | --- |
| Authentication Context | app only |
| Required OAuth Scopes | `code:all` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](../../oauth/http-docs/http-gettoken-POST.md) |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| id   string | Must be “me” for the call to succeed. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

Expand all

| nickname   string |  |
| --- | --- |
| publicKey   object |  |
| Exponent   string |  |
| Modulus   string |  |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully update the user’s nickname. |
| --- | --- |
| 403   Forbidden | Forbidden. |
| 409   Conflict | Conflict (in use by someone else). |
| 500   Internal Server Error | Unknown error. |

## [Example](#example)

Successfully update the user’s nickname.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/forgeapps/:id' \
  -X 'PATCH' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "nickname": "",
        "publicKey": {
          "Exponent": "",
          "Modulus": ""
        }
      }'

```

Show More

### Response

```

```
