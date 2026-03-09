# appbundles/:id/aliases

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/appbundles-id-aliases-POST/

---

POST

# appbundles/:id/aliases

Creates a new alias for this AppBundle.

Limit:
1. Number of aliases (LimitAliases).

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id/aliases |
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

| id   string | Name of AppBundle (unqualified). |
| --- | --- |

### Request

## [Body Structure](#body-structure)

| version   int | The version that this alias refers to. |
| --- | --- |
| receiver   string or array: string | The user(s) to share the alias with. |
| id   string | The alias id. Only alphanumeric characters and _ (underscore) are allowed. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully create a new alias for an AppBundle. |
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

Successfully create a new alias for an AppBundle.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id/aliases' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "version": 1,
        "id": "prod"
      }'

```

Show More

### Response

```
{
  "version": 1,
  "id": "prod"
}

```
