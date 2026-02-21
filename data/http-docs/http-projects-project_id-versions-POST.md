# projects/:project_id/versions

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-versions-POST/

---

Versions

POST

# projects/:project_id/versions

Creates new versions of a file (item), except for the first version of the item. To create the first version of the item, use [POST items](/en/docs/data/v2/reference/http/projects-project_id-items-POST).

Before creating each version you need to [create a new storage location](/en/docs/data/v2/reference/http/projects-project_id-storage-POST) for the version, and [upload the file to the storage object](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-PUT). For more details about the workflow, see the tutorial on [uploading a file](/en/docs/data/v2/tutorials/upload-file).

This endpoint also copies versions of items to exisitng items in other folders. The endpoint creates a new version of the existing item in the target folder. You cannot copy versions of items across different projects and accounts.

To copy versions of items to other folders and create a new item and a first version of the item in the target folder, use [POST versions](/en/docs/data/v2/reference/http/projects-project_id-items-POST).

This endpoint can also be used to delete files on BIM360 Document Management. For more information, please refer to the [delete and restore a file turorial](/en/docs/data/v2/tutorials/delete-and-restore-file).

Note that to access BIM 360 Docs files using the Data Management API you need to provision your app in the BIM 360 Account Administrator portal. For more details, see the [Manage Access to Docs](/en/docs/bim360/v1/tutorials/manage-access-to-docs) tutorial.

**New!** Autodesk Construction Cloud platform (ACC). Note that this endpoint is compatible with ACC projects. For more information about the Autodesk Construction Cloud APIs, see the [Autodesk Construction Cloud documentation](/en/docs/acc/v1/overview/).

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/data/v1/projects/:project_id/versions |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:create` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/vnd.api+json` |
| x-user-id   string | In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| project_id   string | The unique identifier of a project. <br>For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a â**b.**" prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of **b.**c8b0c73d-3ae9. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

- copyFromstring Only relevant for copying files to BIM 360 Docs - the version ID (URN) of the file to copy. For details about finding the URN, follow the initial steps in the [Download a File](/en/docs/data/v2/tutorials/download-file/) tutorial.You can only copy files to the Plans folder or to subfolders of the Plans folder with an `item:autodesk.bim360:Document` item extension type, and you can only copy files to the Project Files folder or to subfolders of the Project Files folder with an `item:autodesk.bim360:File` item extension type.To verify an itemâs extension type, use [GET item](/en/docs/data/v2/reference/http/projects-project_id-items-item_id-GET), and check the `attributes.extension.type` attribute.Note that if you copy a file to the Plans folder or to a subfolder of the Plans folder, the copied file inherits the permissions of the source file. For example, if the end user did not have permission to download files in the source folder, but does have permission to download files in the target folder, he/she will not be able to download the copied file.Note that you cannot copy a file if it is in the middle of being uploaded, updated, or copied. To verify the current process state of a file, call [GET item](/en/docs/data/v2/reference/http/projects-project_id-items-item_id-GET), and check the `attributes.extension.data.processState` attribute.

### Request

## [Body Structure](#body-structure)

describe the version to be created.

Expand all

| jsonapi*   object | The JSON API object. |
| --- | --- |
| version*   enum:string | The version of JSON API. Will always be: `1.0` |
| data*   object | The data object. |
| type*   enum:string | The type of this resource. Will always be: `versions` |
| attributes*   object | The attributes of the data object. |
| name*   string | When copying, copied version uses name of source version by default. This is not required for copy but if present, the value will be used for the copied version. |
| extension*   object | The object containing information on the base attributes of the extension of an object. |
| type*   string | The type of this resource. |
| version*   string | The version of the resource. |
| data   object | The data object. |
| displayName   string | Note that this field is reserved for future releases and should not be used. Use `data.attributes.name` for the file name. |
| relationships*   object | The resources that share a relationship with this resource. |
| item*   object | The object containing information on the item. |
| data*   object | The data object. |
| type*   enum:string | The type of this resource. Will always be: `items` |
| id*   string | The id of the resource. |
| storage   object | The object containing information on the storage resource. |
| data*   object | The data object. |
| type*   enum:string | The type of this resource. Will always be: `objects` |
| id*   string | The id of the resource. |
| refs   object | Only relevant for creating files. |
| data*   array: object | The array of ref objects. |
| type*   enum:string | Will always be: `versions` |
| id*   string | The URN of Version. |
| meta*   object | The meta-information of this resource. |
| refType*   enum:string | Will always be: `xrefs` |
| direction*   enum:string | Possible values: `from`, `to` |
| extension*   object | Extended information on the resource. |
| type*   enum:string | The type of the resource. Will always be: `xrefs:autodesk.core:Xref` |
| version*   string | The version of xref type. The current version is 1.1.0. |
| data   object | The data object. |
| nestedType*   enum:string | The type of the resource. Possible values: `attachment`, `overlay` |
| meta   object | Meta-information for the resource creation. |
| workflow*   string | Only relevant for BIM 360 Docs. The workflow id created for a webhook, used to listen to Model Derivative events. It needs to be no more than 36 chars, and only ASCII, decimal and hyphen are accepted. See the [Creating a Webhook and Listening to Events](https://aps.autodesk.com/en/docs/webhooks/v1/tutorials/create-a-hook-model-derivative) tutorial for details. |
| workflowAttribute   object | Only relevant for BIM 360 Docs. A user-defined JSON object, which you can use to set some custom workflow information. It needs to be less than 1KB and will be ignored if meta.workflow parameter is not set. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Successful creation of a version. |
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
| data   object | The object containing information on the version of the resource. |
| type   enum:string | The type of this resource. Will always be: `versions` |
| id   string | The id of the resource. |
| attributes   object | The attributes of the resource. |
| name   string | The filename used when synced to local disk. |
| displayName   string | Displayable name of the version. Note that for BIM 360 projects, this field is reserved for future releases and should not be used. Use versionâs `attributes.name` for the file name. |
| versionNumber   int | Version number of this versioned file. |
| mimeType   string | Mimetype of the versionâs content. |
| fileType   string | File type, only present if this version represents a file. |
| storageSize   int | File size in bytes, only present if this version represents a file. |
| createTime   datetime: ISO 8601 | The time that the resource was created at. |
| createUserId   string | The userId that created the resource. |
| createUserName   string | The username that created the resource. |
| lastModifiedTime   datetime: ISO 8601 | The time that the resource was last modifed. |
| lastModifiedUserId   string | The userId that last modified the resource. |
| lastModifiedUserName   string | The username that last modified the resource. |
| extension   object | The extension object of the data. |
| type   string | The type of the schema that the resourceâs data object adheres to. |
| version   string | The version of the schema that the data is adhering to. |
| schema   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | Additional properties that the resourceâs data possesses. |
| conformingStatus   enum:string | A status indicating whether or not this version conforms to its parent folderâs file naming standard. <br>Possible values:<br>`NONE`: The conforming status is not applicable for the version.`CONFORMING`: The version conforms to its parent folderâs file naming standard.`NON_CONFORMING`: The version does not conform to its parent folderâs file naming standard.<br>In the event of a `NON_CONFORMING` status, call [GET folders/folder_id](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-GET) to get the file naming standards IDs that have been applied to the versionâs parent folder, and then use the ID to call [GET naming-standards](/en/docs/bim360/v1/reference/http/document-management-naming-standards-id-GET/) to get the details of the file naming standard.<br>Note that this feature is only available for BIM 360 projects.<br>To learn more about the file naming standard feature, see the [BIM 360 File Naming Standard](https://help.autodesk.com/view/BIM360D/ENU/?guid=Common_Data_Environment) help documentation. |
| relationships   object | Information on other resources that shares a relationship with this resource. |
| item   object | Information on resources that are found above this resource. |
| links   object | The object containing information on links of related resources. |
| related   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
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
| storage   object | Information on resources that are indirectly related to this resource. |
| meta   object | Meta-information on links to this resource. |
| link   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| derivatives   object | Information on resources that are indirectly related to this resource. |
| meta   object | Meta-information on links to this resource. |
| link   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| thumbnails   object | Information on resources that are indirectly related to this resource. |
| meta   object | Meta-information on links to this resource. |
| link   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| downloadFormats   object | Information on resources that are found under this resource. |
| links   object | The object containing information on links of related resources. |
| related   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| links   object | Information on links to this resource. |
| self   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| webView   object | An object containing a link that opens the resource in a browser. |
| href   string | The location (URL) of the resource the link goes to. |
| included   array: object | The array of resources included within this resource. |
| type   enum:string | The type of this resource. Will always be: `items` |
| id   string | The unique identifier of the item. |
| attributes   object | Attributes of the latest version of an item. |
| displayName   string | Displayable name of an item. Note that for BIM 360 projects, this field is reserved for future releases and should not be used. Use versionâs `attributes.name` for the file name. |
| createTime   datetime: ISO 8601 | The time the item was created, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| createUserId   string | The unique identifier of the user who created the item. |
| createUserName   string | The name of the user who created the item. |
| lastModifiedTime   datetime: ISO 8601 | The last time the item was modified, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| lastModifiedUserId   string | The unique identifier of the user who last modified the item. |
| lastModifiedUserName   string | The name of the user who last modified the item. |
| hidden   boolean | `true` if the file has been deleted. `false` if the file has not been deleted. |
| reserved   boolean | `true` if the file has been locked.``false`` if the file has not been locked. Note that you can lock BIM 360 Project Files folder files and A360 files, but you cannot lock BIM 360 Plans Folder files. |
| reservedTime   datetime: ISO 8601 | The time the item was reserved. |
| reservedUserId   string | The unique identifier of the user who reserved the item. |
| reservedUserName   string | The name of the user who reserved the item. |
| extension   object | The extension object of the item. |
| type   string | The type of the schema that the resourceâs data object adheres to. |
| version   string | The version of the schema that the data is adhering to. |
| schema   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | Additional properties that the resource data possesses. <br>Contains extended properties for this resource based on the extension schema type and version. The properties documented under this object may not always be present. |
| description   string | The itemâs description property. <br>**Note:**<br>This attribute is available only for items in BIM 360 Docs or ACC projects. |
| reviewState   string | Indicates the current status of items/lineages. <br>This parameter denotes the state of extracted document sheets, showing if they are awaiting publication. It applies to PDFs, IFCs, and DWFs in the [BIM360 Plans folder](https://help.autodesk.com/view/BIM360D/ENU/?guid=GUID-1B49B17A-12C3-47A1-9AAC-EFC46AF9D7AD) It tracks the progression through review and publication stages. Key states are `NEEDS_REVIEW` and `ACCEPTED`.<br>**Note:**<br>This attribute is available only for items in BIM 360 Docs or ACC projects.It does not indicate the status of BIM360 project files or ACC docs in the review process <br>  To check review status of BIM360 project files, use [BIM360 Batch GET](/en/docs/bim360/v1/reference/http/document-management-versionsbatch-get-POST/) instead  To check the review status of ACC docs, use [ACC Batch GET](/en/docs/acc/v1/reference/http/document-management-versionsbatch-get-POST/) instead It does not track ACC Sheets extraction status from Revit/DWG files. Use [Review Sheets](/en/docs/acc/v1/reference/http/sheets-review-sheets-GET/) for that purpose. |
| pathInProject   string | The relative path of the item starting from projectâs root folder. <br>Note: this attribute is not available in search results. |
| relationships   object | Information on other resources that shares a relationship with this item. |
| parent   object | Information on resources that are found above this resource. |
| links   object | The object containing information on links of related resources. |
| related   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| tip   object | Information on resources that are found above this resource. |
| links   object | The object containing information on links of related resources. |
| related   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| versions   object | Information on resources that are found under this resource. |
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
| meta   object | The object containing information on the command id of the command processor. |
| bim360DmCommandId   string | The command id of command processor. Can be used to check the status of processing. |

## [Example](#example)

Successful creation of a version.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/versions' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/vnd.api+json' \
  -d '{
        "jsonapi": {
          "version": "1.0"
        },
        "data": {
          "type": "versions",
          "attributes": {
            "name": "drawing.dwg",
            "extension": {
              "type": "versions:autodesk.core:File",
              "version": "1.0"
            }
          },
          "relationships": {
            "item": {
              "data": {
                "type": "items",
                "id": "urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ"
              }
            },
            "storage": {
              "data": {
                "type": "objects",
                "id": "urn:adsk.objects:os.object:wip.dm.prod/980cff2c-f0f8-43d9-a151-4a2d916b91a2.dwg"
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
      "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.d34fdsg3g%3Fversion%3D2"
    }
  },
  "data": {
    "type": "versions",
    "id": "urn:adsk.wipprod:fs.file:vf.d34fdsg3g?version=2",
    "attributes": {
      "extension": {}
    },
    "relationships": {},
    "links": {
      "self": {
        "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn:adsk.wipprod:fs.file:vf.d34fdsg3g%3Fversion=2"
      },
      "webView": {
        "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.akd2j_B3Tsu7v6v7Kxf2oQ/detail/viewer/items/urn:adsk.wipprod:fs.file:vf.d34fdsg3g%3Fversion%3D2"
      }
    }
  },
  "included": [
    {
      "type": "items",
      "id": "urn:adsk.wipprod:dm.lineage:d34fdsg3g",
      "attributes": {
        "extension": {}
      },
      "relationships": {
        "tip": {
          "data": {
            "type": "versions",
            "id": "urn:adsk.wipprod:fs.file:vf.d34fdsg3g?version=2"
          }
        }
      },
      "links": {
        "self": {
          "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn:adsk.wipprod:fs.file:vf.d34fdsg3g%3Fversion=2"
        },
        "webView": {
          "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.akd2j_B3Tsu7v6v7Kxf2oQ/detail/viewer/items/urn:adsk.wipprod:fs.file:vf.d34fdsg3g%3Fversion%3D2"
        }
      }
    }
  ]
}

```

Show More

## [Example 2](#example-2)

Successful creation of a version with workflow.

**Note:** This is only supported for BIM 360 Docs and ACC.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions?copyFrom=urn%3Aadsk%3Awipprod%3Afs.file%3ASOME.SOURCE%3Fversion%3D1' \
  -X POST \
  -H "Authorization: Bearer kEnG562yz5bhE9igXf2YTcZ2bu0z" \
  -H "Content-Type: application/vnd.api+json" \
  -d '{
        "jsonapi": {
          "version": "1.0"
        },
        "data": {
          "type": "versions",
          "attributes": {
            "name": "newname",
            "extension": {
              "version": "1.0"
            }
          },
          "relationships": {
            "item": {
              "data": {
                "type": "items",
                "id": "urn:adsk.wipprod:dm.lineage:2344sdfd"
              }
            },
            "storage": {
              "data": {
                "type": "objects",
                "id": "urn:adsk.objects:os.object:wip.dm.prod/980cff2c-f0f8-43d9-a151-4a2d916b91a2.dwg"
              }
            }
          }
        },
        "meta": {
          "workflow": "my-workflow-id",
          "workflowAttribute": {
            "myfoo": 33,
            "projectId": "someURN",
            "myobject": {
              "nested": true
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
      "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.AABBCCDD%3Fversion%3D2"
    }
  },
  "data": {
    "type": "versions",
    "id": "urn:adsk:wipprod:fs.file:vf.AABBCCDD?version=2",
    "attributes": {
      "name": "newname",
      "displayName": "drawing",
      "createTime": "2018-03-26T09:40:16.0000000Z",
      "createUserId": "CGT5PFDIZMAS",
      "createUserName": "Owen",
      "lastModifiedTime": "2018-03-26T09:41:16.0000000Z",
      "lastModifiedUserId": "CGT5PFDIZMAS",
      "lastModifiedUserName": "Owen",
      "versionNumber": 1,
      "extension": {
        "type": "versions:autodesk.core:File",
        "version": "1.0",
        "data": {
          "processState": "NEEDS_PROCESSING"
        }
      }
    },
    "links": {
      "self": {
        "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.AABBCCDD%3Fversion%3D2"
      },
      "webView": {
        "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.akd2j_B3Tsu7v6v7Kxf2oQ/detail/viewer/items/urn%3Aadsk.wipprod%3Afs.file%3Avf.AABBCCDD%3Fversion%3D2"
      }
    }
  },
  "included": [
    {
      "type": "items",
      "id": "urn:adsk.wipprod:dm.lineage:2344sdfd",
      "attributes": {
        "displayName": "drawing",
        "createTime": "2018-03-26T09:40:16.0000000Z",
        "createUserId": "CGT5PFDIZMAS",
        "createUserName": "Owen",
        "lastModifiedTime": "2018-03-26T09:41:16.0000000Z",
        "lastModifiedUserId": "CGT5PFDIZMAS",
        "lastModifiedUserName": "Owen",
        "hidden": false,
        "reserved": false,
        "extension": {
          "type": "items:autodesk.core:File",
          "version": "1.0"
        }
      },
      "links": {
      "self": {
        "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.AABBCCDD%3Fversion%3D2"
      },
      "webView": {
        "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.akd2j_B3Tsu7v6v7Kxf2oQ/detail/viewer/items/urn%3Aadsk.wipprod%3Afs.file%3Avf.AABBCCDD%3Fversion%3D2"
      }
    }
    }
  ]
}

```

Show More

## [Example 3](#example-3)

Successful Copy of a Version.

**Note:** This is only supported for BIM 360 Docs and ACC.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions?copyFrom=urn%3Aadsk%3Awipprod%3Afs.file%3ASOME.SOURCE%3Fversion%3D1'
  -X POST \
  -H "Authorization: Bearer kEnG562yz5bhE9igXf2YTcZ2bu0z" \
  -H "Content-Type: application/vnd.api+json"
  -d '{
        "jsonapi": {
          "version": "1.0"
        },
        "data": {
          "type": "versions",
          "attributes": {
            "name": "drawing_copy",
            "extension": {
              "version": "1.0"
            }
          },
          "relationships": {
            "item": {
              "data": {
                "type": "items",
                "id": "urn:adsk.wipprod:dm.lineage:2344sdfd"
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
      "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.AABBCCDD%3Fversion%3D2"
    }
  },
  "data": {
    "type": "versions",
    "id": "urn:adsk:wipprod:fs.file:vf.AABBCCDD?version=2",
    "attributes": {
      "name": "drawing_copy",
      "displayName": "drawing_copy",
      "createTime": "2018-03-26T09:40:16.0000000Z",
      "createUserId": "CGT5PFDIZMAS",
      "createUserName": "Owen",
      "lastModifiedTime": "2018-03-26T09:41:16.0000000Z",
      "lastModifiedUserId": "CGT5PFDIZMAS",
      "lastModifiedUserName": "Owen",
      "versionNumber": 1,
      "extension": {
        "type": "versions:autodesk.core:File",
        "version": "1.0",
        "data": {
          "processState": "NEEDS_PROCESSING"
        }
      }
    },
    "links": {
      "self": {
        "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.AABBCCDD%3Fversion%3D2"
      },
      "webView": {
        "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.akd2j_B3Tsu7v6v7Kxf2oQ/detail/viewer/items/urn%3Aadsk.wipprod%3Afs.file%3Avf.AABBCCDD%3Fversion%3D2"
      }
    }
  },
  "included": [
    {
      "type": "items",
      "id": "urn:adsk.wipprod:dm.lineage:2344sdfd",
      "attributes": {
        "displayName": "drawing_copy",
        "createTime": "2018-03-26T09:40:16.0000000Z",
        "createUserId": "CGT5PFDIZMAS",
        "createUserName": "Owen",
        "lastModifiedTime": "2018-03-26T09:41:16.0000000Z",
        "lastModifiedUserId": "CGT5PFDIZMAS",
        "lastModifiedUserName": "Owen",
        "hidden": false,
        "reserved": false,
        "extension": {
          "type": "items:autodesk.core:File",
          "version": "1.0"
        }
      },
      "links": {
      "self": {
        "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.AABBCCDD%3Fversion%3D2"
      },
      "webView": {
        "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.akd2j_B3Tsu7v6v7Kxf2oQ/detail/viewer/items/urn%3Aadsk.wipprod%3Afs.file%3Avf.AABBCCDD%3Fversion%3D2"
      }
    }
    }
  ]
}

```

Show More

## [Example 4](#example-4)

Successfully rename an item by copying the source version.

**Note:** This is only supported for BIM 360 Docs and ACC.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions?copyFrom=urn%3Aadsk%3Awipprod%3Afs.file%3ASOME.SOURCE%3Fversion%3D1'
  -X POST \
  -H "Authorization: Bearer kEnG562yz5bhE9igXf2YTcZ2bu0z" \
  -H "Content-Type: application/vnd.api+json"
  -d '{
        "jsonapi": {
          "version": "1.0"
        },
        "data": {
          "type": "versions",
          "attributes": {
            "name": "newname.dwg"
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
      "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk%3Awipprod%3Afs.file%3ASOME.SOURCE%3Fversion%3D2"
    }
  },
  "data": {
    "type": "versions",
    "id": "urn:adsk:wipprod:fs.file:SOME.SOURCE?version=2",
    "attributes": {
      "name": "newname.dwg",
      "displayName": "newname.dwg",
      "createTime": "2018-03-26T09:40:16.0000000Z",
      "createUserId": "CGT5PFDIZMAS",
      "createUserName": "Owen",
      "lastModifiedTime": "2018-03-26T09:41:16.0000000Z",
      "lastModifiedUserId": "CGT5PFDIZMAS",
      "lastModifiedUserName": "Owen",
      "versionNumber": 2,
      "storageSize": 35696,
      "fileType": "dwg",
      "extension": {
        "type": "versions:autodesk.bim360:File",
        "version": "1.0",
        "schema": {
          "href": "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.bim360:File-1.0"
        },
        "data": {
          "processState": "PROCESSING_PROMOTING",
          "revisionDisplayLabel": "1",
          "sourceFileName": "drawing.dwg",
          "conformingStatus": "NONE"
        }
      }
    },
    "links": {
      "self": {
        "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk%3Awipprod%3Afs.file%3ASOME.SOURCE%3Fversion%3D2"
      },
      "webView": {
        "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.akd2j_B3Tsu7v6v7Kxf2oQ/detail/viewer/items/urn%3Aadsk%3Awipprod%3Afs.file%3ASOME.SOURCE%3Fversion%3D2"
      }
    }
  },
  "included": [
    {
      "type": "items",
      "id": "urn:adsk.wipprod:dm.lineage:2344sdfd",
      "attributes": {
        "name": "newname.dwg",
        "createTime": "2018-03-26T09:40:16.0000000Z",
        "createUserId": "CGT5PFDIZMAS",
        "createUserName": "Owen",
        "lastModifiedTime": "2018-03-26T09:41:16.0000000Z",
        "lastModifiedUserId": "CGT5PFDIZMAS",
        "lastModifiedUserName": "Owen",
        "hidden": false,
        "reserved": false,
        "extension": {
          "type": "items:autodesk.bim360:File",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/items:autodesk.bim360:File-1.0"
          },
          "data": {
            "sourceFileName": "drawing.dwg"
          }
        }
      },
      "links": {
        "self": {
          "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk%3Awipprod%3Afs.file%3ASOME.SOURCE%3Fversion%3D2"
        },
        "webView": {
          "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.akd2j_B3Tsu7v6v7Kxf2oQ/detail/viewer/items/urn%3Aadsk%3Awipprod%3Afs.file%3ASOME.SOURCE%3Fversion%3D2"
        }
      }
    }
  ]
}

```

Show More
