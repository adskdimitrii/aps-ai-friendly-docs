# engines

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/engines-GET/

---

GET

# engines

Lists all available Engines.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/da/us-east/v3/engines |
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

## [Query String Parameters](#query-string-parameters)

| page   string | Access an additional âpageâ of data when necessary, based on the âpaginationTokenâ returned from a previous invocation. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully list all Engines. |
| --- | --- |
| 400   Bad Request | Bad request. |
| 403   Forbidden | Unauthorized |
| 500   Internal Server Error | Unknown error. |

### Response

## [Body Structure (200)](#body-structure-200)

| paginationToken   string |  |
| --- | --- |
| data   array: string |  |

## [Example](#example)

Successfully list all Engines.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/engines' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "paginationToken": "",
  "data": [
    "Autodesk.3dsMax+2020",
    "Autodesk.AutoCAD+22",
    "Autodesk.Inventor+23",
    "Autodesk.AutoCAD+23",
    "Autodesk.3dsMax+2021",
    "Autodesk.Revit+2018",
    "Autodesk.Test+Latest",
    "Autodesk.Inventor+22",
    "Autodesk.AutoCAD+21",
    "Autodesk.Revit+2019",
    "Autodesk.Revit+2020",
    "Autodesk.Revit+2021",
    "Autodesk.AutoCAD+20_1"
  ]
}

```

Show More
