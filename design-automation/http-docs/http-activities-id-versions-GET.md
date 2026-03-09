# activities/:id/versions

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/activities-id-versions-GET/

---

GET

# activities/:id/versions

Lists all versions of the specified Activity.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/da/us-east/v3/activities/:id/versions |
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

### Request

## [Query String Parameters](#query-string-parameters)

| page   string | Access an additional âpageâ of data when necessary, based on the âpaginationTokenâ returned from a previous invocation. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully list all versions of an Activity. |
| --- | --- |
| 400   Bad Request | The request is invalid. |
| 403   Forbidden | Unauthorized |
| 404   Not Found | Not found. |
| 500   Internal Server Error | Unknown error. |

### Response

## [Body Structure (200)](#body-structure-200)

| paginationToken   string |  |
| --- | --- |
| data   array: integer |  |

## [Example](#example)

Successfully list all versions of an Activity.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/activities/:id/versions' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "paginationToken": "",
  "data": [
    1
  ]
}

```
