# projects/:project_id/folders

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-folders-POST/

---

Folders

POST

# projects/:project_id/folders

Creates a new folder. To delete and restore folders,
use the [PATCH projects/:project_id/folders/:folder_id](http-projects-project_id-folders-folder_id-PATCH.md) endpoint.

**BIM 360 and ACC**

1. To access Docs folders using the Data Management API you need to provision your app in the Account Administrator portal. For more details, see the [Manage Access to Docs](https://aps.autodesk.com/en/docs/bim360/v1/tutorials/manage-access-to-docs/) tutorial.
2. The number of subfolder levels is limited to 25.

**New!** Autodesk Construction Cloud platform (ACC). Note that this endpoint is compatible with ACC projects. For more information about the Autodesk Construction Cloud APIs, see the [Autodesk Construction Cloud documentation](https://aps.autodesk.com/en/docs/acc/v1/overview/).

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/data/v1/projects/:project_id/folders |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:create` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/vnd.api+json` |
| x-user-id   string | In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified. <br>Note that for a three-legged OAuth flow or for a two-legged OAuth flow with user impersonation (`x-user-id`), the user must have permission to create a subfolder in the specified parent folder (`data.attributes.relationships.parent.data.id`).<br>For information about managing and verifying folder permissions for BIM 360 Docs, see the section on [Managing Folder Permissions](http://help.autodesk.com/view/BIM360D/ENU/?guid=GUID-2643FEEF-B48A-45A1-B354-797DAD628C37). |

* Required

### Request

## [URI Parameters](#uri-parameters)

| project_id   string | The unique identifier of a project. <br>For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a â**b.**" prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of **b.**c8b0c73d-3ae9. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

describe the folder to be created.

Expand all

| jsonapi*   object | The JSON API object. |
| --- | --- |
| version*   enum:string | The version of JSON API. Will always be: `1.0` |
| data*   object | The data object. |
| type*   enum:string | The type of this resource. Will always be: `folders` |
| attributes*   object | The attributes of the data object. |
| name*   string | The name of new folder (1-255 characters). <br>Reserved characters: `<`, `>`, `:`, `"`, `/`, `\`, `|`, `?`, `*`, `` ` ``, `\n`, `\r`, `\t`, `\0`, `\f`, `Â¢`, `â¢`, `$`, `Â®`. |
| extension*   object | The object containing information on the base attributes of the extension of an object. |
| type*   string | The type of folder extension. <br>For BIM 360 Docs folders, use `folders:autodesk.bim360:Folder`.<br>For all other services, use `folders:autodesk.core:Folder`. |
| version*   string | The version of the folder extension type. The current version is `1.0.` |
| data   object | The data object. |
| relationships*   object | The resources that share a relationship with this resource. |
| parent*   object | Information on the parent resource of this resource. |
| data*   object | The data object. |
| type*   enum:string | The parent folder resource. Will always be: `folders` |
| id*   string | The URN of parent folder. For details about how to find the URN, follow the initial steps in the [Download a File](../how-to-docs/download-file.md) tutorial. <br>Note that for BIM 360 Docs, new folders must be created within an existing folder (e.g., the Plans or Project Files folders), but not directly within the root folder. Permissions, visibility (e.g., items:autodesk.bim360:Document or items:autodesk.bim360:File), and actions (e.g., OCR) are inherited from the existing parent folder. New folders also inherit subscriptions, i.e., notifications that are sent when files are added to a folder. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Successful creation of a folder. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 403   Forbidden | The request was successfully validated but permission is not granted or the application has not been white-listed. Do not try again unless you solve permissions first. |
| 404   Not Found | The specified resource was not found. |
| 409   Conflict | The specified resource already exists or has been modified. |
| 423   Locked | The source or destination resource is locked or being modifed. |

### Response

## [Body Structure (201)](#body-structure-201)

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
| extension   object | The extension object of the data. |
| type   string | The type of resource. |
| version   string | The version of the folderâs type. |
| schema   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | A collection of properties applied to the folder. |
| namingStandardIds   array: string | A list of file naming standard IDs that have been applied to the folder. <br>Note that we currently support one file naming standard per project.<br>Note that this feature is only available for BIM 360 projects.<br>To get the details of a file naming standard, call [GET naming-standards](../../acc/http-docs/http-document-management-naming-standards-id-GET.md).<br>To learn more about the file naming standard feature, see the [BIM 360 File Naming Standard](https://help.autodesk.com/view/BIM360D/ENU/?guid=Common_Data_Environment) help documentation. |
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

Successful creation of a folder.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/folders' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/vnd.api+json' \
  -d '{
        "jsonapi": {
          "version": "1.0"
        },
        "data": {
          "type": "folders",
          "attributes": {
            "name": "Plans",
            "extension": {
              "type": "folders:autodesk.core:Folder",
              "version": "1.0"
            }
          },
          "relationships": {
            "parent": {
              "data": {
                "type": "folders",
                "id": "urn:adsk.wipprod:dm.folder:sdfedf8wefl"
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
      "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Adm.folder%3AhC6k4hndRWaeIVhIjvHu8w"
    }
  },
  "data": {
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
      "lastModifiedTimeRollup": "2015-11-27T11:11:23.000Z",
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
