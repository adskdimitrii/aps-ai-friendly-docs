# engines/:id

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/engines-id-GET/

---

GET

# engines/:id

Gets the details of the specified Engine. Note that the {id} parameter must be a QualifiedId (owner.name+label).

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/da/us-east/v3/engines/:id |
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

| id   string | Full qualified id of the Engine (owner.name+label). |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully get the details of an Engine. |
| --- | --- |
| 400   Bad Request | The request is invalid. |
| 403   Forbidden | Forbidden. |
| 404   Not Found | Resource cannot be found. Note that the server will return this result if a valid but unqualified id is passed. |
| 500   Internal Server Error | Unknown error. |

### Response

## [Body Structure (200)](#body-structure-200)

| productVersion   string | The product version of the Engine. |
| --- | --- |
| description   string | Human readable description of the object. |
| version   int | The version this engine id refers to. |
| id   string | Full qualified id of the Engine. |

## [Example](#example)

Successfully get the details of an Engine.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/engines/:id' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "productVersion": "23.00",
  "description": "Inventor 2019 RTM",
  "version": 31,
  "id": "Autodesk.Inventor+23"
}

```
