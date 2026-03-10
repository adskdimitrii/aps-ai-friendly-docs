# activities

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/activities-GET/

---

GET

# activities

Lists all available Activities, including Activities shared with this app.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/da/us-east/v3/activities |
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

| 200   OK | Successfully get all available Activities. |
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

Successfully get all available Activities.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/activities' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "paginationToken": "",
  "data": [
    "Autodesk.Nop+Latest",
    "AutoCAD.AcSvfPublish+prod",
    "Revit.RvtIOSandboxTestActivity2018+prod",
    "3dsMax.HelloWorld+Latest",
    "Revit.RvtIOSketchItActivity2018+prod",
    "Inventor.BasicPluginTest+prod",
    "3dsMax.bakeToTexture+Latest",
    "Inventor.iLogic_Volume2020+prod",
    "AutoCAD.AcF2dPublish+prod",
    "AutoCAD.AcLMVPublish+prod",
    "AutoCAD.PlotToPDF+prod",
    "Inventor.Configuration+Beta",
    "Inventor.ChangeParams+prod"
  ]
}

```

Show More
