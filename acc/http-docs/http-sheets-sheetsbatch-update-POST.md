# projects/{projectId}/sheets:batch-update

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-sheetsbatch-update-POST/

---

Sheets

POST

# projects/{projectId}/sheets:batch-update

Updates a list of sheets.

Note that you can only update a single sheet number and a single title in one call. However, you can update multiple sheets and tags in a version set in a single call.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/sheets:batch-update |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-user-id   string | The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. <br>When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.<br>You can use either the user’s ACC ID (id), or their Autodesk ID (autodeskId). |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](../how-to-docs/getting-started-retrieve-account-and-project-id.md). You can use a project ID either with a “b.” prefix or without a “b.” prefix. For instance, a project ID of “b.a4be0c34a-4ab7” can also be referred to as “a4be0c34a-4ab7”. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

Expand all

| ids*   array: string | To find the IDs of the sheets you want to update, call [GET sheets](http-sheets-sheets-GET.md). <br>The max number of items is 200. |
| --- | --- |
| updates   object | The list of updates. |
| number   string | The new sheet number. <br>Only available for single sheet update.<br>The number should not contain these reserved characters: `<`, `>`, `:`, `"`, `/`, `\`, `|`, `?`, `*`, `\n`, `\r`, `\t`, `\0`, `\f`, `'`.You cannot assign the following reserved names to the number: CON, PRN, AUX, NUL, COM1, COM2, COM3, COM4, COM5, COM6, COM7, COM8, COM9, LPT1, LPT2, LPT3, LPT4, LPT5, LPT6, LPT7, LPT8, and LPT9.You cannot put a period at the end of the number.The number should not be space only.The max length is 255.<br>The API will format the number in the following ways before applying it to the sheet:<br>Remove spaces at the end and beginning of the number.Reduce multiple continuous spaces to a single space.<br>Max length: 255 |
| title   string | The new title of the sheet. <br>Only available for single sheet.<br>The title should not be space only.The max length is 255.<br>The API will format the title in the following ways before applying it to the sheet:<br>Remove spaces at the end and beginning of the title.Reduce multiple continuous spaces to a single space.<br>Max length: 255 |
| versionSetId   string | The ID of the new version set. |
| addTags   array: string | The tags to be attached to the sheets. <br>The max length is 100.The tags should not be space only.After applying addTags and removeTags, the number of remain tags of the sheets should not exceed 100.<br>The API will format the tags in the following ways before applying them to the sheets:<br>Remove spaces at the end and beginning of the tags.Reduce multiple continuous spaces to a single space.The tags are case insensitive. Upper case letters will be transformed to lower case. |
| removeTags   array: string | The tags to be detached from the sheets. <br>The max length is 100.The tags should not be space only.<br>The API will format the tags in the following ways before comparing them to the existing tags:<br>Remove spaces at the end and beginning of the tags.Reduce multiple continuous spaces to a single space.The tags are case insensitive. Upper case letters will be transformed to lower case. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully updated sheets. |
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

| results   array: object | The IDs of the updated sheets. |
| --- | --- |
| id   string | The ID of the sheet. |

## [Example](#example)

Successfully updated sheets.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/sheets:batch-update' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "ids": [
          "0d7a5883-1694-3078-a06d-ad24413f8b06"
        ],
        "updates": {
          "number": "A-01",
          "title": "Floor One",
          "versionSetId": "7c2ecde0-2406-49f9-9199-50176848a0b7",
          "addTags": [
            "floor"
          ],
          "removeTags": [
            "top"
          ]
        }
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
  ]
}

```
