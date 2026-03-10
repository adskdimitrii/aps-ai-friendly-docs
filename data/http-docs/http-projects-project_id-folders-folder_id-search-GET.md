# projects/:project_id/folders/:folder_id/search

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-search-GET/

---

Folders

GET

# projects/:project_id/folders/:folder_id/search

Filters the data of a folder and recursively in the subfolders of any project accessible to you,
using the `filter` query string parameter. You can filter the following properties from the `version` payload:
the `type` property, the `id` property, and any of the `attributes` object properties. For example,
you can filter `createTime`, `mimeType`. It returns tip versions (latest versions) of properties where the filter conditions are satisfied.
To verify the properties of the `attributes` object for a specific version,
see the [GET projects/:project_id/versions/:version_id](http-projects-project_id-versions-version_id-GET.md).

To filter a folder's data without recursively filtering its subfolders, see the [GET projects/:project_id/folders/:folder_id/contents](http-projects-project_id-folders-folder_id-contents-GET.md) endpoint.

**New!** Autodesk Construction Cloud platform (ACC). Note that this endpoint is compatible with ACC projects. For more information about the Autodesk Construction Cloud APIs, see the [Autodesk Construction Cloud documentation](https://aps.autodesk.com/en/docs/acc/v1/overview/).

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/data/v1/projects/:project_id/folders/:folder_id/search |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:search` `data:read` |
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
| folder_id   string | The unique identifier of a folder. |

### Request

## [Query String Parameters](#query-string-parameters)

| filter[*]   array: string | Filter the data. See the [Filtering](https://aps.autodesk.com/en/docs/data/v2/overview/filtering/) section for details. |
| --- | --- |
| page[number]   int | Specifies what page to return. Page numbers start at 0, so the first page is page 0. The minimum value to specify is 0 and the maximum is 49. For fewer results to page through, consider searching an inner folder. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful retrieval of the search results. |
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
| links   object | The object containing information on links to this resource. |
| self   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| first   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| prev   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| next   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   array: object | The object containing information on this resource. |
| type   enum:string | The type of this resource. Will always be: `versions` |
| id   string | The id of the resource. |
| attributes   object | The attributes of the resource. |
| name   string | The filename used when synced to local disk. |
| displayName   string | Displayable name of the version. Note that for BIM 360 projects, this field is reserved for future releases and should not be used. Use version’s `attributes.name` for the file name. |
| versionNumber   int | Version number of this versioned file. |
| mimeType   string | Mimetype of the version’s content. |
| fileType   string | File type, only present if this version represents a file. |
| storageSize   int | File size in bytes, only present if this version represents a file. |
| createTime   datetime: ISO 8601 | The time that the resource was created at. |
| createUserId   string | The userId that created the resource. |
| createUserName   string | The username that created the resource. |
| lastModifiedTime   datetime: ISO 8601 | The time that the resource was last modifed. |
| lastModifiedUserId   string | The userId that last modified the resource. |
| lastModifiedUserName   string | The username that last modified the resource. |
| extension   object | The extension object of the data. |
| type   string | The type of the schema that the resource’s data object adheres to. |
| version   string | The version of the schema that the data is adhering to. |
| schema   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | Additional properties that the resource’s data possesses. |
| conformingStatus   enum:string | A status indicating whether or not this version conforms to its parent folder’s file naming standard. <br>Possible values:<br>`NONE`: The conforming status is not applicable for the version.`CONFORMING`: The version conforms to its parent folder’s file naming standard.`NON_CONFORMING`: The version does not conform to its parent folder’s file naming standard.<br>In the event of a `NON_CONFORMING` status, call [GET folders/folder_id](http-projects-project_id-folders-folder_id-GET.md) to get the file naming standards IDs that have been applied to the version’s parent folder, and then use the ID to call [GET naming-standards](../../acc/http-docs/http-document-management-naming-standards-id-GET.md) to get the details of the file naming standard.<br>Note that this feature is only available for BIM 360 projects.<br>To learn more about the file naming standard feature, see the [BIM 360 File Naming Standard](https://help.autodesk.com/view/BIM360D/ENU/?guid=Common_Data_Environment) help documentation. |
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
| included   array: object | Information on the latest versions of the items in this resource. |
| type   enum:string | The type of this resource. Will always be: `items` |
| id   string | The unique identifier of the item. |
| attributes   object | Attributes of the latest version of an item. |
| displayName   string | Displayable name of an item. Note that for BIM 360 projects, this field is reserved for future releases and should not be used. Use version’s `attributes.name` for the file name. |
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
| type   string | The type of the schema that the resource’s data object adheres to. |
| version   string | The version of the schema that the data is adhering to. |
| schema   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | Additional properties that the resource data possesses. <br>Contains extended properties for this resource based on the extension schema type and version. The properties documented under this object may not always be present. |
| description   string | The item’s description property. <br>**Note:**<br>This attribute is available only for items in BIM 360 Docs or ACC projects. |
| reviewState   string | Indicates the current status of items/lineages. <br>This parameter denotes the state of extracted document sheets, showing if they are awaiting publication. It applies to PDFs, IFCs, and DWFs in the [BIM360 Plans folder](https://help.autodesk.com/view/BIM360D/ENU/?guid=GUID-1B49B17A-12C3-47A1-9AAC-EFC46AF9D7AD) It tracks the progression through review and publication stages. Key states are `NEEDS_REVIEW` and `ACCEPTED`.<br>**Note:**<br>This attribute is available only for items in BIM 360 Docs or ACC projects.It does not indicate the status of BIM360 project files or ACC docs in the review process <br>  To check review status of BIM360 project files, use [BIM360 Batch GET](../../acc/http-docs/http-document-management-versionsbatch-get-POST.md) instead  To check the review status of ACC docs, use [ACC Batch GET](../../acc/http-docs/http-document-management-versionsbatch-get-POST.md) instead It does not track ACC Sheets extraction status from Revit/DWG files. Use [Review Sheets](../../acc/http-docs/http-sheets-review-sheets-GET.md) for that purpose. |
| pathInProject   string | The relative path of the item starting from project’s root folder. <br>Note: this attribute is not available in search results. |
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
| meta   object | The object containing metadata about the search results. |
| approximateNumberOfPages   int | The approximate number of pages of search results matching the search criteria. |

## [Example](#example)

Successful retrieval of the search results.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/folders/:folder_id/search' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "data": [
    {
      "type": "versions",
      "id": "urn:adsk.wipprod:fs.file:vf.4cW918j8QsynzG0oZ6_Nbg?version=1",
      "attributes": {
        "name": "sample.txt",
        "displayName": "sample.txt",
        "createTime": "2016-11-09T13:11:27+00:00",
        "createUserId": "BW9RM76WZBGL",
        "createUserName": "John Doe",
        "lastModifiedTime": "2016-11-09T13:11:36+00:00",
        "lastModifiedUserId": "BW9RM76WZBGL",
        "lastModifiedUserName": "John Doe",
        "versionNumber": 1,
        "fileType": "txt",
        "extension": {
          "type": "versions:autodesk.bim360:File",
          "version": "1.0",
          "schema": {
            "href": "/schema/v1/versions/versions%3Aautodesk.bim360%3AFile-1.0"
          },
          "data": {
            "processState": "PROCESSING_COMPLETE",
            "extractionState": "UNSUPPORTED",
            "splittingState": "NOT_SPLIT",
            "conformingStatus": "NONE"
          }
        }
      },
      "links": {
        "self": {
          "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.4cW918j8QsynzG0oZ6_Nbg%3Fversion%3D1"
        },
        "webView": {
          "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.0J4paz_FQgWPX2QRsaBkiw/detail/viewer/items/urn%3Aadsk.wipprod%3Afs.file%3Avf.4cW918j8QsynzG0oZ6_Nbg%3Fversion%3D1"
        }
      },
      "relationships": {
        "item": {
          "data": {
            "type": "items",
            "id": "urn:adsk.wipprod:dm.lineage:4cW918j8QsynzG0oZ6_Nbg"
          },
          "links": {
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.4cW918j8QsynzG0oZ6_Nbg%3Fversion%3D1/item"
            }
          }
        },
        "links": {
          "links": {
            "self": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.4cW918j8QsynzG0oZ6_Nbg%3Fversion%3D1/relationships/links"
            }
          }
        },
        "refs": {
          "links": {
            "self": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.4cW918j8QsynzG0oZ6_Nbg%3Fversion%3D1/relationships/refs"
            },
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.4cW918j8QsynzG0oZ6_Nbg%3Fversion%3D1/refs"
            }
          }
        },
        "downloadFormats": {
          "links": {
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.4cW918j8QsynzG0oZ6_Nbg%3Fversion%3D1/downloadFormats"
            }
          }
        },
        "derivatives": {
          "data": {
            "type": "derivatives",
            "id": "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNGNXOTE4ajhRc3luekcwb1o2X05iZz92ZXJzaW9uPTE"
          },
          "meta": {
            "link": {
              "href": "/modelderivative/v2/designdata/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNGNXOTE4ajhRc3luekcwb1o2X05iZz92ZXJzaW9uPTE/manifest?scopes=b360project.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d,global,O2tenant.tenantId"
            }
          }
        },
        "thumbnails": {
          "data": {
            "type": "thumbnails",
            "id": "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNGNXOTE4ajhRc3luekcwb1o2X05iZz92ZXJzaW9uPTE"
          },
          "meta": {
            "link": {
              "href": "/modelderivative/v2/designdata/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNGNXOTE4ajhRc3luekcwb1o2X05iZz92ZXJzaW9uPTE/thumbnail?scopes=b360project.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d,global,O2tenant.tenantId"
            }
          }
        },
        "storage": {
          "data": {
            "type": "objects",
            "id": "urn:adsk.objects:os.object:wip.dm.prod/095f7c56-2373-4831-9485-e3546dd501ba.txt"
          },
          "meta": {
            "link": {
              "href": "/oss/v2/buckets/wip.dm.prod/objects/095f7c56-2373-4831-9485-e3546dd501ba.txt?scopes=b360project.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d,global,O2tenant.tenantId"
            }
          }
        }
      }
    },
    {
      "type": "versions",
      "id": "urn:adsk.wipprod:fs.file:vf.jts1sOfCS6mdwCV38lKpGQ?version=1",
      "attributes": {
        "name": "sample.pdf",
        "displayName": "sample.pdf",
        "createTime": "2016-11-09T13:13:09+00:00",
        "createUserId": "BW9RM76WZBGL",
        "createUserName": "John Doe",
        "lastModifiedTime": "2016-11-09T13:13:42+00:00",
        "lastModifiedUserId": "BW9RM76WZBGL",
        "lastModifiedUserName": "John Doe",
        "versionNumber": 1,
        "fileType": "pdf",
        "extension": {
          "type": "versions:autodesk.bim360:File",
          "version": "1.0",
          "schema": {
            "href": "/schema/v1/versions/versions%3Aautodesk.bim360%3AFile-1.0"
          },
          "data": {
            "processState": "PROCESSING_COMPLETE",
            "extractionState": "SUCCESS",
            "splittingState": "NOT_SPLIT",
            "reviewState": "NOT_IN_REVIEW",
            "conformingStatus": "NONE"
          }
        }
      },
      "links": {
        "self": {
          "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.jts1sOfCS6mdwCV38lKpGQ%3Fversion%3D1"
        },
        "webView": {
          "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.0J4paz_FQgWPX2QRsaBkiw/detail/viewer/items/urn%3Aadsk.wipprod%3Afs.file%3Avf.jts1sOfCS6mdwCV38lKpGQ%3Fversion%3D1"
        }
      },
      "relationships": {
        "item": {
          "data": {
            "type": "items",
            "id": "urn:adsk.wipprod:dm.lineage:jts1sOfCS6mdwCV38lKpGQ"
          },
          "links": {
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.jts1sOfCS6mdwCV38lKpGQ%3Fversion%3D1/item"
            }
          }
        },
        "links": {
          "links": {
            "self": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.jts1sOfCS6mdwCV38lKpGQ%3Fversion%3D1/relationships/links"
            }
          }
        },
        "refs": {
          "links": {
            "self": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.jts1sOfCS6mdwCV38lKpGQ%3Fversion%3D1/relationships/refs"
            },
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.jts1sOfCS6mdwCV38lKpGQ%3Fversion%3D1/refs"
            }
          }
        },
        "downloadFormats": {
          "links": {
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.jts1sOfCS6mdwCV38lKpGQ%3Fversion%3D1/downloadFormats"
            }
          }
        },
        "derivatives": {
          "data": {
            "type": "derivatives",
            "id": "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuanRzMXNPZkNTNm1kd0NWMzhsS3BHUT92ZXJzaW9uPTE"
          },
          "meta": {
            "link": {
              "href": "/modelderivative/v2/designdata/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuanRzMXNPZkNTNm1kd0NWMzhsS3BHUT92ZXJzaW9uPTE/manifest?scopes=b360project.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d,global,O2tenant.tenantId"
            }
          }
        },
        "thumbnails": {
          "data": {
            "type": "thumbnails",
            "id": "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuanRzMXNPZkNTNm1kd0NWMzhsS3BHUT92ZXJzaW9uPTE"
          },
          "meta": {
            "link": {
              "href": "/modelderivative/v2/designdata/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuanRzMXNPZkNTNm1kd0NWMzhsS3BHUT92ZXJzaW9uPTE/thumbnail?scopes=b360project.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d,global,O2tenant.tenantId"
            }
          }
        },
        "storage": {
          "data": {
            "type": "objects",
            "id": "urn:adsk.objects:os.object:wip.dm.prod/f5a8a8e8-9bbc-46cf-bce9-9cc34508c2d4.pdf"
          },
          "meta": {
            "link": {
              "href": "/oss/v2/buckets/wip.dm.prod/objects/f5a8a8e8-9bbc-46cf-bce9-9cc34508c2d4.pdf?scopes=b360project.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d,global,O2tenant.tenantId"
            }
          }
        }
      }
    }
  ],
  "included": [
    {
      "type": "items",
      "id": "urn:adsk.wipprod:dm.lineage:4cW918j8QsynzG0oZ6_Nbg",
      "attributes": {
        "displayName": "sample",
        "createTime": "2016-11-09T13:11:27+00:00",
        "createUserId": "BW9RM76WZBGL",
        "createUserName": "John Doe",
        "lastModifiedTime": "2016-11-09T13:11:36+00:00",
        "lastModifiedUserId": "BW9RM76WZBGL",
        "lastModifiedUserName": "John Doe",
        "hidden": false,
        "reserved": true,
        "reservedTime": "2016-11-09T13:11:30.000Z",
        "reservedUserId": "BW9RM76WZBGL",
        "reservedUserName": "John Doe",
        "extension": {
          "type": "items:autodesk.bim360:File",
          "version": "1.0",
          "schema": {
            "href": "/schema/v1/versions/items%3Aautodesk.bim360%3AFile-1.0"
          },
          "data": {}
        }
      },
      "links": {
        "self": {
          "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3A4cW918j8QsynzG0oZ6_Nbg"
        },
        "webView": {
          "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.0J4paz_FQgWPX2QRsaBkiw/detail/viewer/items/urn%3Aadsk.wipprod%3Adm.lineage%3A4cW918j8QsynzG0oZ6_Nbg"
        }
      },
      "relationships": {
        "tip": {
          "data": {
            "type": "versions",
            "id": "urn:adsk.wipprod:fs.file:vf.4cW918j8QsynzG0oZ6_Nbg?version=1"
          },
          "links": {
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3A4cW918j8QsynzG0oZ6_Nbg/tip"
            }
          }
        },
        "versions": {
          "links": {
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3A4cW918j8QsynzG0oZ6_Nbg/versions"
            }
          }
        },
        "parent": {
          "data": {
            "type": "folders",
            "id": "urn:adsk.wipprod:fs.folder:co.KJRpLpSXRm66X2HB2Q7AQw"
          },
          "links": {
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3A4cW918j8QsynzG0oZ6_Nbg/parent"
            }
          }
        },
        "refs": {
          "links": {
            "self": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3A4cW918j8QsynzG0oZ6_Nbg/relationships/refs"
            },
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3A4cW918j8QsynzG0oZ6_Nbg/refs"
            }
          }
        },
        "links": {
          "links": {
            "self": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3A4cW918j8QsynzG0oZ6_Nbg/relationships/links"
            }
          }
        }
      }
    },
    {
      "type": "items",
      "id": "urn:adsk.wipprod:dm.lineage:jts1sOfCS6mdwCV38lKpGQ",
      "attributes": {
        "displayName": "sample",
        "createTime": "2016-11-09T13:13:09+00:00",
        "createUserId": "BW9RM76WZBGL",
        "createUserName": "John Doe",
        "lastModifiedTime": "2016-11-09T13:13:41+00:00",
        "lastModifiedUserId": "BW9RM76WZBGL",
        "lastModifiedUserName": "John Doe",
        "hidden": false,
        "reserved": true,
        "reservedTime": "2016-11-09T13:13:24.000Z",
        "reservedUserId": "BW9RM76WZBGL",
        "reservedUserName": "John Doe",
        "extension": {
          "type": "items:autodesk.bim360:File",
          "version": "1.0",
          "schema": {
            "href": "/schema/v1/versions/items%3Aautodesk.bim360%3AFile-1.0"
          },
          "data": {}
        }
      },
      "links": {
        "self": {
          "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3Ajts1sOfCS6mdwCV38lKpGQ"
        },
        "webView": {
          "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.0J4paz_FQgWPX2QRsaBkiw/detail/viewer/items/urn%3Aadsk.wipprod%3Adm.lineage%3Ajts1sOfCS6mdwCV38lKpGQ"
        }
      },
      "relationships": {
        "tip": {
          "data": {
            "type": "versions",
            "id": "urn:adsk.wipprod:fs.file:vf.jts1sOfCS6mdwCV38lKpGQ?version=1"
          },
          "links": {
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3Ajts1sOfCS6mdwCV38lKpGQ/tip"
            }
          }
        },
        "versions": {
          "links": {
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3Ajts1sOfCS6mdwCV38lKpGQ/versions"
            }
          }
        },
        "parent": {
          "data": {
            "type": "folders",
            "id": "urn:adsk.wipprod:fs.folder:co.KJRpLpSXRm66X2HB2Q7AQw"
          },
          "links": {
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3Ajts1sOfCS6mdwCV38lKpGQ/parent"
            }
          }
        },
        "refs": {
          "links": {
            "self": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3Ajts1sOfCS6mdwCV38lKpGQ/relationships/refs"
            },
            "related": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3Ajts1sOfCS6mdwCV38lKpGQ/refs"
            }
          }
        },
        "links": {
          "links": {
            "self": {
              "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3Ajts1sOfCS6mdwCV38lKpGQ/relationships/links"
            }
          }
        }
      }
    }
  ]
}

```

Show More
