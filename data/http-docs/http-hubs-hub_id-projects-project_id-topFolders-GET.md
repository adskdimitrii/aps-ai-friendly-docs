# hubs/:hub_id/projects/:project_id/topFolders

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/hubs-hub_id-projects-project_id-topFolders-GET/

---

Projects

GET

# hubs/:hub_id/projects/:project_id/topFolders

Returns the details of the highest level folders the user has access to for a given project.
The user must have at least read access to the folders.

If the user is a Project Admin, it returns all top level folders in the project. Otherwise,
it returns all the highest level folders in the folder hierarchy the user has access to.

Note that when users have access to a folder, access is automatically granted to its subfolders.

**New!** Autodesk Construction Cloud platform (ACC). Note that this endpoint is compatible with ACC projects. For more information about the Autodesk Construction Cloud APIs, see the [Autodesk Construction Cloud documentation](https://aps.autodesk.com/en/docs/acc/v1/overview/).

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/project/v1/hubs/:hub_id/projects/:project_id/topFolders |
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

| hub_id   string | The unique identifier of a hub. |
| --- | --- |
| project_id   string | The unique identifier of a project. <br>For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a â**b.**" prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of **b.**c8b0c73d-3ae9. |

### Request

## [Query String Parameters](#query-string-parameters)

| excludeDeleted   boolean | Specify whether to exclude deleted folders in response for BIM 360 Docs projects when user context is provided. <br>`true`: response will exclude deleted folders for BIM 360 Docs projects.<br>`false` (default): response will not exclude deleted folders for BIM 360 Docs projects. |
| --- | --- |
| projectFilesOnly   boolean | Specify whether only Project Files folder or its subfolders will be returned for BIM 360 Docs projects when user context is provided. <br>`true`: response will include only Project Files folder and its subfolders for BIM 360 Docs projects.<br>`false` (default): response will include all available folders. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful retrieval of the top foldersâ details. |
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
| data   array: object | The array of folder objects. |
| attributes   object | The attributes of the folder. |
| extension   object | The extension object of the data. |
| data   object | A collection of properties applied to the folder. |
| isRoot   boolean | Determines if folder is root folder. Note that this feature is only available for BIM 360 and ACC projects. |
| folderType   string | Type of folder. Possible values: `normal`, `plan`, `shared`, `recycle`, `drawing`. <br>Note that `recycle` and `drawing` only exist in old projects.<br>Note that this feature is only available for BIM 360 and ACC projects. |
| folderParents   array: object | Parent folders of the current folder. Note that this feature is only available for BIM 360 and ACC projects. |
| urn   string | The unique identifier of the folder. |
| parentUrn   string | The unique identifier of the parent folder. |
| title   string | The name of the folder. |
| isRoot   boolean | Determines if folder is root folder. |
| namingStandardIds   array: string | A list of file naming standard IDs that have been applied to the folder. <br>Note that we currently support one file naming standard per project.<br>Note that this feature is only available for BIM 360 projects.<br>To get the details of a file naming standard, call [GET naming-standards](../../acc/http-docs/http-document-management-naming-standards-id-GET.md).<br>To learn more about the file naming standard feature, see the [BIM 360 File Naming Standard](https://help.autodesk.com/view/BIM360D/ENU/?guid=Common_Data_Environment) help documentation. |
| type   string | The type of resource. |
| version   string | The version of the folderâs type. |
| schema   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| name   string | The name of the folder. |
| displayName   string | Note that this field is reserved for future releases and should not be used. Use `attributes.name` for the folder name. |
| objectCount   int | The number of objects inside the folder. |
| createTime   datetime: ISO 8601 | The time the folder was created, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| createUserId   string | The unique identifier of the user who created the folder. |
| createUserName   string | The name of the user who created the folder. |
| lastModifiedTime   datetime: ISO 8601 | The last time the folder was modified, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| lastModifiedUserId   string | The unique identifier of the user who last modified the folder. |
| lastModifiedUserName   string | The name of the user who last modified the folder. |
| lastModifiedTimeRollup   datetime: ISO 8601 | The date and time the folder or any of its children were last updated. |
| hidden   boolean | The folderâs current visibility state. |
| type   enum:string | The type of this resource. Will always be: `folders` |
| id   string | The unique identifier of the folder. |
| relationships   object | The relationship links associated with the folder, including `refs`, `links`, `parent`, and `contents.` |
| parent   object | Information on resources that are found above this resource. |
| links   object | The object containing information on links of related resources. |
| related   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| contents   object | Information on resources that are found under this resource. |
| links   object | The object containing information on links of related resources. |
| related   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| refs   object | Information on other resources that shares a custom relationship with this resource. |
| links   object | The object containing information on links of related resources that shares a custom relationship with this resource. |
| self   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| related   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| links   object | Information on the link resources found in this resource. |
| links   object | The object containing information on links to this resource. |
| self   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| links   object | Information on links to this resource. |
| self   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| webView   object | An object containing a link that opens the resource in a browser. |
| href   string | The location (URL) of the resource the link goes to. |

## [Example](#example)

Successful retrieval of the top foldersâ details.

### Request

```
curl -v 'https://developer.api.autodesk.com/project/v1/hubs/:hub_id/projects/:project_id/topFolders' \
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
      "href": "/project/v1/hubs/b.622cb5d1-581b-4a46-a6d9-4ebc68ea4051/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/topFolders"
    }
  },
  "data": [
    {
      "type": "folders",
      "id": "urn:adsk.wipprod:dm.folder:hC6k4hndRWaeIVhIjvHu8w",
      "attributes": {
        "name": "Plans",
        "displayName": "Plans",
        "createTime": "2015-11-27T11:11:23.000Z",
        "createUserId": "BW9RM76WZBGL",
        "createUserName": "John Doe",
        "lastModifiedTime": "2015-11-27T11:11:27.000Z",
        "lastModifiedUserId": "BW9RM76WZBGL",
        "lastModifiedUserName": "John Doe",
        "lastModifiedTimeRollup": "2015-11-27T11:11:27.000Z",
        "objectCount": 4,
        "hidden": false,
        "extension": {
          "type": "folders:autodesk.bim360:Folder",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/folders%3Aautodesk.bim360%3AFolder-1.0"
          },
          "data": {
            "allowedTypes": [
              "folders",
              "items:autodesk.bim360:File",
              "items:autodesk.bim360:Document",
              "items:autodesk.bim360:TitleBlock"
            ],
            "visibleTypes": [
              "folders",
              "items:autodesk.bim360:Document"
            ],
            "isRoot": false,
            "folderType": "normal",
            "folderParents": [
              {
                "urn": "urn:adsk.wipprod:fs.folder:co.R3JhbmRwYXJlbnQK",
                "isRoot": true,
                "title": "Project Files",
                "parentUrn": "urn:adsk.wipprod:fs.folder:co.R3JlYXQgR3JhbmRwYXJlbnQK"
              },
              {
                "urn": "urn:adsk.wipprod:fs.folder:co.5-pCTuRbQI2fosqUJoNJ9w",
                "isRoot": false,
                "title": "ViewOnlySupportTest",
                "parentUrn": "urn:adsk.wipprod:fs.folder:co.UGFyZW50Cg"
              }
            ],
            "namingStandardIds": []
          }
        }
      },
      "links": {
        "self": {
          "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Adm.folder%3AhC6k4hndRWaeIVhIjvHu8w"
        },
        "webView": {
          "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Adm.folder%3AhC6k4hndRWaeIVhIjvHu8w"
        }
      },
      "relationships": {
        "parent": {
          "links": {
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Adm.folder%3AhC6k4hndRWaeIVhIjvHu8w/parent"
            }
          },
          "data": {
            "type": "folders",
            "id": "urn:adsk.wipprod:dm.folder:sdfedf8wefl"
          }
        },
        "refs": {
          "links": {
            "self": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Adm.folder%3AhC6k4hndRWaeIVhIjvHu8w/relationships/refs"
            },
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Adm.folder%3AhC6k4hndRWaeIVhIjvHu8w/refs"
            }
          }
        },
        "links": {
          "links": {
            "self": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Adm.folder%3AhC6k4hndRWaeIVhIjvHu8w/relationships/links"
            }
          }
        },
        "contents": {
          "links": {
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Adm.folder%3AhC6k4hndRWaeIVhIjvHu8w/contents"
            }
          }
        }
      }
    }
  ]
}

```

Show More
