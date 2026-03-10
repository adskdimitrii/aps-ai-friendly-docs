# projects/:project_id/storage

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-storage-POST/

---

Projects

POST

# projects/:project_id/storage

Creates a storage location in the OSS where data can be uploaded to.

**New!** Autodesk Construction Cloud platform (ACC). Note that this endpoint is compatible with ACC projects. For more information about the Autodesk Construction Cloud APIs, see the [Autodesk Construction Cloud documentation](https://aps.autodesk.com/en/docs/acc/v1/overview/).

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/data/v1/projects/:project_id/storage |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:create` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/vnd.api+json` |
| x-user-id   string | In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| project_id   string | The unique identifier of a project. <br>For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a “**b.**" prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of **b.**c8b0c73d-3ae9. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

describe the file the storage is created for.

Expand all

| jsonapi*   object | The JSON API object. |
| --- | --- |
| version*   enum:string | The version of JSON API. Will always be: `1.0` |
| data*   object | The data object. |
| type*   enum:string | The type of this resource. Will always be: `objects` |
| attributes*   object | The attributes of the data object. |
| name*   string | Displayable name of the resource. |
| relationships*   object | The resources that share a relationship with this resource. |
| target*   object | Information on the target object. |
| data*   object | The data object. |
| type*   enum:string | The type of this resource. Possible values: `folders`, `items` |
| id*   string | The id of the resource. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Successful creation of a storage location. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 403   Forbidden | The request was successfully validated but permission is not granted or the application has not been white-listed. Do not try again unless you solve permissions first. |
| 404   Not Found | The specified resource was not found. |

### Response

## [Body Structure (201)](#body-structure-201)

Expand all

| jsonapi   object | The JSON API object. |
| --- | --- |
| version   enum:string | The version of JSON API. Will always be: `1.0` |
| links   object | Information on links to this resource. |
| self   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | The object containing information on the storage resource. |
| type   enum:string | The type of this resource. Will always be: `objects` |
| id   string | The id of the resource. |
| relationships   object | Information on other resources that shares a relationship with this resource. |
| target   object | Information on the target object. |
| links   object | The object containing information on links of related resources. |
| related   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | The data object of the resource. |
| type   enum:string | The type of this resource. Will always be: `folders` |
| id   string | The id of the resource. |

## [Example](#example)

Successful creation of a storage location.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/storage' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/vnd.api+json' \
  -d '{
        "jsonapi": {
          "version": "1.0"
        },
        "data": {
          "type": "objects",
          "attributes": {
            "name": "drawing.dwg"
          },
          "relationships": {
            "target": {
              "data": {
                "type": "folders",
                "id": "urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA"
              }
            }
          }
        }
      }'

```

Show More

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "/oss/v2/buckets/wipbucket/objects/830b7ac3-dc75-4e36-aa32-7a1cff7599a1.dwg"
    }
  },
  "data": {
    "type": "objects",
    "id": "urn:adsk.objects:os.object:wip.dm.prod.temp/830b7ac3-dc75-4e36-aa32-7a1cff7599a1.dwg",
    "relationships": {
      "target": {
        "links": {
          "related": {
            "href": "/data/v1/projects/b.6f8813fe-31a7-4440-bc63-d8ca97c856b4/folders/urn%3Aadsk.wipprod%3Adm.folder%3Asdfedf8wefl"
          }
        },
        "data": {
          "type": "folders",
          "id": "urn:adsk.wipprod:dm.folder:sdfedf8wefl"
        }
      }
    }
  }
}

```

Show More
