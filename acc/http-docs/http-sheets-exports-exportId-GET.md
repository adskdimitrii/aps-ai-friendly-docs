# projects/{projectId}/exports/{exportId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-exports-exportId-GET/

---

Exports

GET

# projects/{projectId}/exports/{exportId}

Retrieves the status of a PDF sheet export job, as well as the signed URL required to download the exported file once the export process is complete.

To initiate a sheet export, use [POST exports](http-sheets-exports-POST.md). This will return an export ID which should be used with this endpoint.

Note that only the authenticated user who initiated the export job can retrieve the signed URL using this endpoint. This signed URL will be available for one hour. If you need to download the file after this period, you will need to make another call to [POST exports](http-sheets-exports-POST.md).

For more details about exporting sheets, see the [Export Sheets](https://help.autodesk.com/view/BUILD/ENU/?guid=Export_Sheets) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/exports/{exportId} |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-user-id   string | The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. <br>When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.<br>You can use either the user’s ACC ID (id), or their Autodesk ID (autodeskId). |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring: UUID The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](../how-to-docs/getting-started-retrieve-account-and-project-id.md). You can use a project ID either with a “b.” prefix or without a “b.” prefix. For instance, a project ID of “b.a4be0c34a-4ab7” can also be referred to as “a4be0c34a-4ab7”.
- exportIdstring The ID of the export job. The export ID is generated when you initialize an export job using [POST exports](http-sheets-exports-POST.md).

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved export data |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. <br>Sample error code with possible messages:<br>ERR_BAD_INPUT: <br>  Failed to parse the token |
| 401   Unauthorized | The provided bearer token is not valid. <br>Sample error code with possible messages:<br>ERR_AUTHENTICATED_ERROR: <br>  Authentication header is not correct |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. <br>Sample error code with possible messages:<br>ERR_NOT_ALLOWED: <br>  Account inactive  Project inactive  User inactive  API access denied  User {userId} does not have download permission on resource {resource} |
| 404   Not Found | The requested resources, such as the project, account, user, sheet, or job, do not exist. <br>Sample error code with possible messages:<br>ERR_RESOURCE_NOT_EXIST: <br>  Project not found  Project user not found  The job does not exist |
| 500   Internal Server Error | An unknown error occurred on the server. <br>Sample error code with possible messages:<br>ERR_INTERNAL_SERVER_ERROR: <br>  Request failed for internal exception xxx  Failed to get account  Failed to get project  Failed to get user |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| id   string: UUID | The ID of the sheets export job. |
| --- | --- |
| status   enum:string | The status of the sheets export job. Possible values: `successful`, `processing`, `failed` |
| result   object | The result of a completed export job. <br>If the `status` is `successful`, a downloadable signed URL will be included in the `result.output` object.If the `status` value is `failed` (e.g., because some files were deleted), the `result.error` object will include details of the error. |
| output   object | Details about the downloadable signed URL. |
| signedUrl   string | The signed URL that you can use to download the PDF file. Note that it expires in one hour. |
| error   object | Information about the error. |
| code   string | The code of the error. |
| title   string | The title of the error. |
| detail   string | The details of the error. |

## [Example](#example)

Successfully retrieved export data

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/exports/5b4bb914-c123-4f10-87e3-579ef934aaf9' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response (200 with signedUrl)

```
{
  "id": "5b4bb914-c123-4f10-87e3-579ef934aaf9",
  "status": "successful",
  "result": {
    "output": {
      "signedUrl": "https://signedUrl"
    }
  }
}

```

Show More

### Response (200 with failed result)

```
{
  "id": "5b4bb914-c123-4f10-87e3-579ef934aaf9",
  "status": "failed",
  "result": {
    "error": {
      "code": "401",
      "title": "ERR_AUTHORIZATION_ERROR",
      "detail": "Authentication header is not correct"
    }
  }
}

```

Show More
