# projects/:project_id/items/:item_id

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-items-item_id-PATCH/

---

Items

PATCH

# projects/:project_id/items/:item_id

Updates the properties of the given `item_id` object. Note that updating the displayName of an item is not supported for BIM 360 Docs or ACC items. Instead, use the [POST projects/:project_id/versions](/en/docs/data/v2/reference/http/projects-project_id-versions-POST) endpoint.

**New!** Autodesk Construction Cloud platform (ACC). Note that this endpoint is compatible with ACC projects. For more information about the Autodesk Construction Cloud APIs, see the [Autodesk Construction Cloud documentation](/en/docs/acc/v1/overview/).

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/data/v1/projects/:project_id/items/:item_id |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:write` |
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
| item_id   string | The unique identifier of an item. |

### Request

## [Body Structure](#body-structure)

describe the item to be patched.

Expand all

| jsonapi*   object | The JSON API object. |
| --- | --- |
| version*   enum:string | The version of JSON API. Will always be: `1.0` |
| data*   object | The data object. |
| type*   enum:string | The type of this resource. Will always be: `items` |
| id*   string | The id of the resource. |
| attributes   object | Attributes of the item. |
| extension   object | Extended information on the resource. |
| data   object | Additional properties to modify. <br>Contains extended properties for this resource based on the extension schema type and version. The ability to modify these properties depends on whether the schema type and version allow it. |
| description   string | The new description of the item (0-255 characters). This property is only available for items BIM 360 Docs or ACC projects. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful update of a specific itemâs properties. |
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
| data   object | The object containing information on the item. |
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
| included   array: object | The other resources included within this item. |
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

## [Example](#example)

Successful update of a specific itemâs properties.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/items/:item_id' \
  -X 'PATCH' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/vnd.api+json' \
  -d '{
        "jsonapi": {
          "version": "1.0"
        },
        "data": {
          "type": "items",
          "id": "urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ",
          "attributes": {
            "displayName": "new name for drawing.dwg"
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
      "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2swMDEjMjAyNDA0MTEwMTAxMDEw/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ"
    }
  },
  "data": {
    "type": "items",
    "id": "urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ",
    "attributes": {
      "displayName": "new name for drawing.dwg",
      "extension": {
        "data": {},
        "version": "1.0",
        "type": "items:autodesk.core:File",
        "schema": {
          "href": "https://developer.api.autodesk.com/schema/v1/versions/items:autodesk.core:File-1.0"
        }
      },
      "createUserId": "BW9RM76WZBGL",
      "createUserName": "John Doe",
      "lastModifiedUserId": "BW9RM76WZBGL",
      "lastModifiedUserName": "John Doe",
      "lastModifiedTime": "2015-11-27T11:11:27.000Z",
      "createTime": "2015-11-27T11:11:23.000Z",
      "hidden": false,
      "reserved": true,
      "reservedTime": "2015-11-27T11:11:25.000Z",
      "reservedUserId": "BW9RM76WZBGL",
      "reservedUserName": "John Doe"
    },
    "relationships": {
      "tip": {
        "data": {
          "type": "versions",
          "id": "urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ?version=1"
        },
        "links": {
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2swMDEjMjAyNDA0MTEwMTAxMDEw/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ/tip"
          }
        }
      },
      "parent": {
        "data": {
          "type": "folders",
          "id": "urn:adsk.wipprod:fs.folder:co.sdfedf8wefl"
        },
        "links": {
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2swMDEjMjAyNDA0MTEwMTAxMDEw/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ/parent"
          }
        }
      },
      "versions": {
        "links": {
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2swMDEjMjAyNDA0MTEwMTAxMDEw/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ/versions"
          }
        }
      },
      "refs": {
        "links": {
          "self": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2swMDEjMjAyNDA0MTEwMTAxMDEw/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ/relationships/refs"
          },
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2swMDEjMjAyNDA0MTEwMTAxMDEw/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ/refs"
          }
        }
      },
      "links": {
        "links": {
          "self": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2swMDEjMjAyNDA0MTEwMTAxMDEw/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ/relationships/links"
          }
        }
      }
    },
    "links": {
      "self": {
        "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2swMDEjMjAyNDA0MTEwMTAxMDEw/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ"
      }
    }
  },
  "included": [
    {
      "type": "versions",
      "id": "urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ?version=1",
      "attributes": {
        "name": "testFile.dwg",
        "displayName": "testFile.dwg",
        "createTime": "2016-04-01T11:09:03.000Z",
        "createUserId": "BW9RM76WZBGL",
        "createUserName": "John Doe",
        "lastModifiedTime": "2016-04-01T11:11:18.000Z",
        "lastModifiedUserId": "BW9RM76WZBGL",
        "lastModifiedUserName": "John Doe",
        "versionNumber": 1,
        "mimeType": "application/vnd.autodesk.autocad.dwg",
        "storageSize": 35696,
        "fileType": "dwg",
        "extension": {
          "type": "versions:autodesk.core:File",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.core:File-1.0"
          },
          "data": {}
        }
      },
      "links": {
        "self": {
          "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2swMDEjMjAyNDA0MTEwMTAxMDEw/versions/urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion=1"
        }
      },
      "relationships": {
        "item": {
          "links": {
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2swMDEjMjAyNDA0MTEwMTAxMDEw/versions/urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion=1/item"
            }
          },
          "data": {
            "type": "items",
            "id": "urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ"
          }
        },
        "refs": {
          "links": {
            "self": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2swMDEjMjAyNDA0MTEwMTAxMDEw/versions/urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion=1/relationships/refs"
            },
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2swMDEjMjAyNDA0MTEwMTAxMDEw/versions/urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion=1/refs"
            }
          }
        },
        "links": {
          "links": {
            "self": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2swMDEjMjAyNDA0MTEwMTAxMDEw/versions/urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion=1/relationships/links"
            }
          },
          "storage": {
            "meta": {
              "link": {
                "href": "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/44f771a1-3b11-4ff1-b6d7-5b4719481c93.dwg?scopes=global"
              }
            },
            "data": {
              "type": "objects",
              "id": "urn:adsk.objects:os.object:wip.dm.prod/44f771a1-3b11-4ff1-b6d7-5b4719481c93.dwg"
            }
          }
        }
      }
    }
  ]
}

```

Show More
