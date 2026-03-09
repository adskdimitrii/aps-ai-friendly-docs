# activities/:id/aliases/:aliasId

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/activities-id-aliases-aliasId-PATCH/

---

PATCH

# activities/:id/aliases/:aliasId

Modifies alias details.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/da/us-east/v3/activities/:id/aliases/:aliasId |
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

| id   string | Name of Activity (unqualified). |
| --- | --- |
| aliasId   string | Name of alias. |

### Request

## [Body Structure](#body-structure)

| receiver   string or array: string | The user(s) to share the alias with. |
| --- | --- |
| version   int | The version that this alias refers to. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully modify an alias details. |
| --- | --- |
| 400   Bad Request | The request is invalid. |
| 403   Forbidden | Maximum number of items exceeded. |
| 404   Not Found | Not found. |
| 409   Conflict | An item with this name already exists. |
| 500   Internal Server Error | Unknown error. |

### Response

## [Body Structure (200)](#body-structure-200)

| version   int | The version that this alias refers to. |
| --- | --- |
| receiver   string or array: string | The user(s) to share the alias with. |
| id   string | The alias id. |

## [Example](#example)

Successfully modify an alias details.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/activities/:id/aliases/:aliasId' \
  -X 'PATCH' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "version": 1
      }'

```

### Response

```
{
  "version": 1,
  "id": "prod"
}

```
