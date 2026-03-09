# activities/:id/aliases/:aliasId

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/activities-id-aliases-aliasId-GET/

---

GET

# activities/:id/aliases/:aliasId

Gets alias details.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/da/us-east/v3/activities/:id/aliases/:aliasId |
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
| aliasId   string | Name of alias. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully get the details of an Activityâs alias. |
| --- | --- |
| 403   Forbidden | Unauthorized |
| 404   Not Found | Not found. |
| 500   Internal Server Error | Unknown error. |

### Response

## [Body Structure (200)](#body-structure-200)

| version   int | The version that this alias refers to. |
| --- | --- |
| receiver   string or array: string | The user(s) to share the alias with. |
| id   string | The alias id. |

## [Example](#example)

Successfully get the details of an Activityâs alias.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/activities/:id/aliases/:aliasId' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "version": 1,
  "id": "prod"
}

```
