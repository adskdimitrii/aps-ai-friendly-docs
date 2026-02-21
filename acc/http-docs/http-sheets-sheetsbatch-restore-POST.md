# projects/{projectId}/sheets:batch-restore

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-sheetsbatch-restore-POST/

---

Sheets

POST

# projects/{projectId}/sheets:batch-restore

Restores deleted sheets. The sheet is restored to the version set it was associated with when it was deleted.

Note that sheet numbers need to be unique within a version set.
If you try to restore a sheet to a version set that includes an existing sheet with the same number, it will not restore the sheet.
The `errors` object in the response gives information about unrestored sheets.

To delete sheets, call [POST sheets:batch-delete](/en/docs/acc/v1/reference/http/sheets-sheetsbatch-delete-POST/).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/sheets:batch-restore |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| x-user-id   string | The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. <br>When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.<br>You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId). |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. Use the [Data Management API](/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/). You can use a project ID either with a âb.â prefix or without a âb.â prefix. For instance, a project ID of âb.a4be0c34a-4ab7â can also be referred to as âa4be0c34a-4ab7â. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

| ids*   array: string | The IDs of the sheets to restore. To find the IDs of deleted sheets you want to restore, call [GET sheets](/en/docs/acc/v1/reference/http/sheets-sheets-GET/) using the `isDeleted=true` filter. <br>The max number of items is 200. |
| --- | --- |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully restored sheets. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 403   Forbidden | The user or client represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource cannot be found. |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the target resource. |
| 429   Too Many Requests | The server has received too many requests. |
| 500   Internal Server Error | An unexpected error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of sheets that were successfully restored. |
| --- | --- |
| id   string: UUID | The ID of the sheet. |
| errors   array: object | The list of sheets that were not restored. Sheets are usually not restored because a sheet with the same number exists in the version set. |
| sheetId   string: UUID | The ID of the sheet that was not restored. |
| code   string | The code of the error. |
| title   string | The title of the error. |
| detail   string | Details about the error. |

## [Example](#example)

Successfully restored sheets.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/sheets:batch-restore' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "ids": [
          "0d7a5883-1694-3078-a06d-ad24413f8b06"
        ]
      }'

```

Show More

### Response

```
{
  "results": [
    {
      "id": "0d7a5883-1694-3078-a06d-ad24413f8b06"
    }
  ],
  "errors": [
    {
      "sheetId": "",
      "code": "",
      "title": "",
      "detail": ""
    }
  ]
}

```

Show More
