# projects/:project_id/folders/:folder_id

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-PATCH/

---

Folders

PATCH

# projects/:project_id/folders/:folder_id

Modifies folder names. You can also use this endpoint to delete and restore BIM 360 Docs folders by using the `hidden` attribute, or move BIM 360 Docs folders by using `parent` relationships.

Note that you cannot permanently delete BIM 360 Docs folders.
They are tagged as `hidden` folders and are removed from the BIM 360 Docs UI and from regular Data Management API responses until you restore them.
You can use the `hidden` filter (`filter[hidden]=true`) to get a list of deleted folders with
the [GET projects/:project_id/folders/:folder_id/contents](http-projects-project_id-folders-folder_id-contents-GET.md) endpoint.

Note that to access BIM 360 Docs folders using the Data Management API you need to provision your app in the BIM 360
Account Administrator portal. For more details, see the [Manage Access to Docs](https://aps.autodesk.com/en/docs/bim360/v1/tutorials/manage-access-to-docs/) tutorial.

**New!** Autodesk Construction Cloud platform (ACC). Note that this endpoint is compatible with ACC projects. For more information about the Autodesk Construction Cloud APIs, see the [Autodesk Construction Cloud documentation](https://aps.autodesk.com/en/docs/acc/v1/overview/).

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/data/v1/projects/:project_id/folders/:folder_id |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:write` |
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
| folder_id   string | The unique identifier of a folder. |

### Request

## [Body Structure](#body-structure)

describe the folder to be patched.

Expand all

| jsonapi*   object | The JSON API object. |
| --- | --- |
| version*   enum:string | The version of JSON API. Will always be: `1.0` |
| data*   object | The data object. |
| type*   enum:string | The type of this resource. Will always be: `folders` |
| id*   string | The URN of the folder. <br>For details about how to find the URN, follow the initial steps in the [Download a File](../how-to-docs/download-file.md) tutorial.<br>Note that this should NOT be URL-encoded.<br>Note that you also need to specify the URN of the folder in the URI (`folder_id`). |
| attributes   object | The attributes of the data object |
| hidden   boolean | `true` if you want to delete a BIM 360 Docs folder. <br>`false` if you want to restore a BIM 360 Docs folder. |
| name   string | The new folder name (1-255 characters). <br>Reserved characters: `<`, `>`, `:`, `"`, `/`, `\`, `|`, `?`, `*`, `` ` ``, `\n`, `\r`, `\t`, `\0`, `\f`, `¢`, `™`, `$`, `®`.<br>Restored folders are assigned the original folder name by default, unless you specify a different name.<br>Note that if you assign a deleted folder name to a different folder, you will need to assign a new name to the deleted folder when you restore it. |
| relationships   object | The resources that share a relationship with this resource. |
| parent   object | Information on the parent resource of this resource. |
| data*   object | The data object. |
| type*   enum:string | The type of this resource. Will always be: `folders` |
| id*   string | The URN of the parent folder in which you want to move a folder to. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Folder successfully renamed. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 403   Forbidden | The request was successfully validated but permission is not granted or the application has not been white-listed. Do not try again unless you solve permissions first. |
| 404   Not Found | The specified resource was not found. |
| 423   Locked | The source or destination resource is locked or being modifed. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| jsonapi   object | The JSON API object. |
| --- | --- |
| version   enum:string | The version of JSON API. Will always be: `1.0` |
| links   object | Information on links to this resource. |
| self   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | The object containing information on the folder. |
| type   enum:string | The type of this resource. Will always be: `folders` |
| id   string | The unique identifier of the folder. |
| attributes   object | The attributes of the folder. |
| name   string | The new name of the folder. <br>When you delete a folder a unique identifier is generated for the folder name until it is restored.<br>Note that if you assign a deleted folder name to a different folder, you will need to assign a new name to the deleted folder when you restore it. |
| displayName   string | Note that this field is reserved for future releases and should not be used. Use `attributes.name` for the new name of the folder. |
| objectCount   int | The number of objects inside the folder. |
| createTime   datetime: ISO 8601 | The time the folder was created, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| createUserId   string | The unique identifier of the user who created the folder. |
| createUserName   string | The name of the user who created the folder. |
| lastModifiedTime   datetime: ISO 8601 | The last time the folder was modified, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| lastModifiedUserId   string | The unique identifier of the user who last modified the folder. |
| lastModifiedUserName   string | The name of the user who last modified the folder. |
| lastModifiedTimeRollup   datetime: ISO 8601 | The date and time the folder or any of its children were last updated. |
| hidden   boolean | The folder’s current visibility state. |
| extension   object | The extension object of the data. |
| type   string | The type of the schema that the resource’s data object adheres to. |
| version   string | The version of the schema that the data is adhering to. |
| schema   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | Additional properties that the resource’s data possesses. |
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

Folder successfully renamed.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/folders/:folder_id' \
  -X 'PATCH' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/vnd.api+json' \
  -d '{
        "jsonapi": {
          "version": "1.0"
        },
        "data": {
          "type": "folders",
          "id": "urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA",
          "attributes": {
            "name": "Drawings"
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
      "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Adm.folder%3AhC6k4hndRWaeIVhIjvHu8w"
    }
  },
  "data": {
    "type": "folders",
    "id": "urn:adsk.wipprod:dm.folder:hC6k4hndRWaeIVhIjvHu8w",
    "attributes": {
      "name": "Drawings",
      "displayName": "Drawings",
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
}

```

Show More
