# appbundles/:id/aliases

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/appbundles-id-aliases-GET/

---

GET

# appbundles/:id/aliases

Lists all aliases for the specified AppBundle.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id/aliases |
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

### Request

## [Query String Parameters](#query-string-parameters)

| page   string | Access an additional âpageâ of data when necessary, based on the âpaginationTokenâ returned from a previous invocation. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully list all aliases for an AppBundle. |
| --- | --- |
| 400   Bad Request | The request is invalid. |
| 403   Forbidden | Unauthorized |
| 404   Not Found | Not found. |
| 500   Internal Server Error | Unknown error. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| paginationToken   string |  |
| --- | --- |
| data   array: object |  |
| version   int | The version that this alias refers to. |
| receiver   string or array: string | The user(s) to share the alias with. |
| id   string | The alias id. |

## [Example](#example)

Successfully list all aliases for an AppBundle.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id/aliases' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "paginationToken": "",
  "data": [
    {
      "version": 1,
      "id": "prod"
    },
    {
      "version": 1,
      "id": "$LATEST"
    }
  ]
}

```

Show More
