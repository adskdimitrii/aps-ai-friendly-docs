# shares

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/shares-GET/

---

GET

# shares

Gets all Shares (AppBundles and Activities) shared by this app (shared to other
:   apps for them to use).

Sharing of AppBundles and Activities is controlled via the use of âaliasesâ.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/da/us-east/v3/shares |
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

## [Query String Parameters](#query-string-parameters)

| page   string | Used to get subsequent âpagesâ of data. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully get all Shares for an app. |
| --- | --- |
| 403   Forbidden | Unauthorized |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| paginationToken   string |  |
| --- | --- |
| data   array: object |  |
| id   string | The name alias id with the owner stripped ex: CoolApp+Prod. |
| receiver   string or array: string | The receiver(s) of the shared alias. |
| type   enum:string | Possible values: `activity`, `app` |

## [Example](#example)

Successfully get all Shares for an app.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/shares' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "paginationToken": null,
  "data": [
      {
          "id": "NetworkTests+Latest",
          "receiver": "everyone",
          "type": "activity"
      },
      {
          "id": "RVTIOSketchItPackage2024+test",
          "receiver": "myNickname",
          "type": "app"
      }
  ]
}

```

Show More
