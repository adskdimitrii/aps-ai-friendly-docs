# projects/:project_id/versions/:version_id/downloadFormats

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-versions-version_id-downloadFormats-GET/

---

Versions

GET

# projects/:project_id/versions/:version_id/downloadFormats

Returns a collection of file formats this `version` could be converted to and downloaded as.

Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/data/v1/projects/:project_id/versions/:version_id/downloadFormats |
| --- | --- |
| Authentication Context | User context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is a two-legged access token obtained via a [Client Credentials Grant flow](../../oauth/how-to-docs/get-2-legged-token.md), or a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context.
- x-user-idstring In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified.

* Required

### Request

## [URI Parameters](#uri-parameters)

| project_id   string | The unique identifier of a project. <br>To convert BIM 360 or Forma Project IDs to Data Management Project IDs, prefix them with `b.` For example, a Project ID of `c8b0c73d-3ae9` becomes `b.c8b0c73d-3ae9`. |
| --- | --- |
| version_id   string | The unique identifier of a version. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful retrieval of the available download formats for a specific version. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 403   Forbidden | The request was successfully validated but permission is not granted or the application has not been white-listed. Do not try again unless you solve permissions first. |
| 404   Not Found | The specified resource was not found. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| jsonapi   object | The JSON API object. |
| --- | --- |
| version   enum:string | The version of JSON API. Will always be: `1.0` |
| links   object | Information on links to this resource. |
| self   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | The object containing information on the download_formats of the resource. |
| type   enum:string | The type of this resource. Will always be: `downloadFormats` |
| id   string | The id of the resource. |
| attributes   object | The attributes of the download format. |
| formats   array: object | An array of supported download formats for this resource. |
| fileType   string | The file type of the resource. |
| links   object | Information on links to this resource. |
| self   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |

## [Example](#example)

Successful retrieval of the available download formats for a specific version.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/versions/:version_id/downloadFormats' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "/data/v1/projects/{some_project_id}/versions/{some_version_id}/downloadFormats"
    }
  },
  "data": {
    "type": "downloadFormats",
    "id": "96af4f60-53b8-4efe-b890-1eaa9ea5cb08",
    "attributes": {
      "formats": [
        {
          "fileType": "pdf"
        },
        {
          "fileType": "dwg"
        }
      ]
    }
  }
}

```

Show More
