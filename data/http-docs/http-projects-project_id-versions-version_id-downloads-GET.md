# projects/:project_id/versions/:version_id/downloads

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-versions-version_id-downloads-GET/

---

Versions

GET

# projects/:project_id/versions/:version_id/downloads

Returns a set of already available downloads for this `version`.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/data/v1/projects/:project_id/versions/:version_id/downloads |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-user-id   string | In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| project_id   string | The unique identifier of a project. <br>For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a “**b.**" prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of **b.**c8b0c73d-3ae9. |
| --- | --- |
| version_id   string | The unique identifier of a version. |

### Request

## [Query String Parameters](#query-string-parameters)

| filter[format.fileType]   array: string | Filter by the `file type` of the `download` object. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful retrieval of the available downloads collection associated with a specific version. |
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
| data   array: object | The array of download objects. |
| type   enum:string | The type of this resource. Will always be: `downloads` |
| id   string | The id of the resource. |
| attributes   object | The attributes of the download object. |
| format   object | The object containing information on the format of the download. |
| fileType   string | The file type of the resource. |
| relationships   object | Information on other resources that shares a relationship with this resource. |
| storage   object | Information on resources that are indirectly related to this resource. |
| meta   object | Meta-information on links to this resource. |
| link   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| links   object | Information on links to this resource. |
| self   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |

## [Example](#example)

Successful retrieval of the available downloads collection associated with a specific version.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/versions/:version_id/downloads' \
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
      "href": "/data/v1/projects/{project_id}/downloads"
    }
  },
  "data": [
    {
      "type": "downloads",
      "id": "{download_id}",
      "attributes": {
        "format": {
          "fileType": "pdf"
        }
      },
      "relationships": {
        "source": {
          "links": {
            "related": {
              "href": "/data/v1/projects/{project_id}/downloads/{download_id}/source"
            }
          },
          "data": {
            "type": "versions",
            "id": "{version_id}"
          }
        },
        "storage": {
          "data": {
            "type": "objects",
            "id": "urn:adsk.objects:os.object:{wip_bucket}/{guid}.pdf"
          },
          "meta": {
            "link": {
              "href": "/oss/v2/buckets/{wip_bucket}/objects/{guid}.pdf?scopes={list_of_scopes}"
            }
          }
        }
      },
      "links": {
        "self": {
          "href": "/data/v1/projects/{project_id}/downloads/{download_id}"
        }
      }
    }
  ]
}

```

Show More
