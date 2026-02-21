# servicelimits/:owner

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/servicelimits-owner-GET/

---

GET

# servicelimits/:owner

Gets a userâs service limit configuration.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/da/us-east/v3/servicelimits/:owner |
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

| owner   string | The user to fetch the service limit configuration for. It should be âmeâ for the call to succeed. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully get the service limits configuration. |
| --- | --- |
| 403   Forbidden | The access is forbidden (not admin). |
| 500   Internal Server Error | Unknown error. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| frontendLimits   object | Limits enforced by the frontend. |
| --- | --- |
| limitPayloadSizeInKB   int | Max permitted size for App/Activity/Workitem json payload in kilobytes. Default is 64KB. |
| limitVersions   int | Max permitted number of App/Activity versions a client can have at any one time. Default is 100. |
| limitAliases   int | Max permitted number of aliases that a client can have at any one time. Default is 100. |
| limitPublicAliases   int | Max permitted number of public aliases that a client can have at any one time. Default is 0. |
| limitAppUploadSizeInMB   int | Max permitted size of an App upload in megabytes. |
| limitMonthlyProcessingTimeInHours   int | Max commulative engine usage by client in a given calendar month. This limit applies to all engines. For example, if the limit is set to 1 hour then 30 minutes of Revit usage and 30 minutes of Inventor usage will reach limit. |
| backendLimits   object |  |
| *   object | Type: dictionary<string, [*](#id3)> |
| limitProcessingTimeSec   int | Max duration of processing in seconds per workitem (includes download and upload time). |
| limitTotalUncompressedAppsSizeInMB   int | Max permitted size of all Apps referenced by an activity. It is enforced when you post a workitem. Default is 500. |

## [Example](#example)

Successfully get the service limits configuration.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/servicelimits/:owner' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "frontendLimits": {
    "limitPayloadSizeInKB":64,
    "limitVersions": 100,
    "limitAliases": 100,
    "limitPublicAliases": 0,
    "limitAppUploadSizeInMB": 100
  },
  "backendLimits": {
    "Revit": {
      "limitProcessingTimeSec": 150,
      "limitTotalUncompressedAppsSizeInMB": 500
    }
  }
}

```

Show More
