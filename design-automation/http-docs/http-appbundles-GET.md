# appbundles

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/appbundles-GET/

---

GET

# appbundles

Lists all available AppBundles, including AppBundles shared with this app.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/da/us-east/v3/appbundles |
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

| page   string | Access an additional ‘page’ of data when necessary, based on the ‘paginationToken’ returned from a previous invocation. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully get all AppBundles. |
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

Successfully get all AppBundles.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/appbundles' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "paginationToken": "",
  "data": [
    "AutoCAD.Publish2View22+prod",
    "Revit.RVTIOSandboxTestPackage2018+prod",
    "Inventor.iLogicSampleAppPackage+prod",
    "Inventor.Configuration+Beta",
    "AutoCAD.Publish2View23+prod",
    "Inventor.ChangeParams+prod",
    "3dsMax.bakeToTexture+prod",
    "Revit.RVTIOSketchItPackage2018+prod"
  ]
}

```

Show More
