# projects/{projectId}/exports/{exportId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/v1-files-export-status-and-result-GET/

---

Export Status and Result

GET

# projects/{projectId}/exports/{exportId}

Retrieves the status of an export job. The S3 signed URL (in `result.output.signedUrl`) will be available for downloading the exported file.

The export job ID is obtained from [POST /projects/{projectId}/exports](https://forge.autodesk.com/en/docs/acc/v1/reference/http/files-export-pdf-files-POST/).

Note that only the authenticated user who launched the export job may use this endpoint to retrieve the signed URL. The signed URL will be available for **1 hour**, and will expire thereafter. If you havenât downloaded the file yet, you must create a new export job for the same files.

For more details about exporting files, see the [Export Files](https://help.autodesk.com/view/DOCS/ENU/?guid=Export_Files) tutorial.

**Note that this endpoint is not compatible with BIM 360 projects.** For BIM 360 projects use [GET versions/{version_id}/exports/{export_id}](en/docs/bim360/v1/reference/http/document-management-projects-project_id-versions-version_id-exports-export_id-GET/).

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/files/v1/projects/{projectId}/exports/{exportId} |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-user-id   string | The ID of a user on whose behalf your API request is acting. Required if youâre using a 2-legged authentication context, which must be 2-legged OAuth2 security with user impersonation. <br>The app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified.<br>You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId). |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring: UUID The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](../how-to-docs/getting-started-retrieve-account-and-project-id.md). You can use a project ID either with a âb.â prefix or without a âb.â prefix. For instance, a project ID of âb.a4be0c34a-4ab7â can also be referred to as âa4be0c34a-4ab7â.
- exportIdstring The ID of the export job. The export ID is generated when you initialize an export job using [POST exports](https://aps.autodesk.com/en/docs/acc/v1/reference/http/export-pdf-files-POST/).

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully get the export job status |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. <br>Sample error code with possible messages:<br>ERR_BAD_INPUT: <br>  Failed to parse the token |
| 401   Unauthorized | The provided bearer token is not valid. <br>Sample error code with possible messages:<br>ERR_AUTHENTICATED_ERROR: <br>  Authentication header is not correct |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. <br>Sample error code with possible messages:<br>ERR_NOT_ALLOWED: <br>  Account inactive  Project inactive  User inactive  Api access deny  User {userId} does not have download permission on resource {resource} |
| 404   Not Found | The project, project user or the exporting job is not found <br>Sample error code with possible messages:<br>ERR_RESOURCE_NOT_EXIST: <br>  Project not found  Project user not found  The job does not exist |
| 500   Internal Server Error | An unknown error occurred on the server. <br>Sample error code with possible messages:<br>ERR_INTERNAL_SERVER_ERROR: <br>  Request failed for internal exception xxx  Failed to get account  Failed to get project  Failed to get user ERR_WORKFLOW_TIMEOUT <br>  Workflow Timeout Error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| id   string: UUID | The ID of the PDF export job. |
| --- | --- |
| status   string | The status of the PDF export job. |
| result   object | The result of a completed export job: <br>If the exporting jobâs `status` value is `successful`, the downloadable signed url will be included in the `result.output` objectIf the exporting jobâs `status` value is `failed` (e.g. the files have been deleted), the `result.error` object will be present with details.If the exporting jobâs `status` value is `partialSuccess` (e.g. when some dwg/rvt files do not contain any exportable views or sheets), the `result.output.failedFiles` object will be present with file urn and reason. |
| output   object | The output containing the downloadable signed URL. |
| signedUrl   string | The signed URL to download the PDF or ZIP file. Expires in 1 hour. |
| failedFiles   array: object | Only for dwg/rvt files. |
| id   string | The file version URN. |
| reason   string | The reason for failure. |
| detail   string | The detail message for failure |
| error   object | The error codes could be<br> :   ERR_WORKFLOW_TIMEOUT, when the export job runs more than 30 minutes.<br>ERR_INTERNAL_SERVER_ERROR, when other internal server error happens.<br>ERR_NO_PROCESSABLE_FILES, when all dwg/rvt files do not contain any 2d pdf files.<br>ERR_FILE_TOO_LARGE, when the total size of exported files exceeds the upper limit. |
| code   string | The HTTP code of the error. |
| title   string | The title of the error. |
| detail   string | The detail of the error. |

## [Example](#example)

Successfully retrieved export data

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/files/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/exports/5b4bb914-c123-4f10-87e3-579ef934aaf9' \
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

### Response (200 with partial successful result)

```
{
  "id": "5b4bb914-c123-4f10-87e3-579ef934aaf9",
  "status": "partialSuccess",
  "result": {
    "signedUrl": "https://signedUrl",
    "failedFiles": [{
      "id": "fileUrn",
      "reason": "ERR_NO_PROCESSABLE_FILES",
      "detail": "This file does not contain any 2d pdf files or still under processing."
    }]
  }
}

```

Show More
