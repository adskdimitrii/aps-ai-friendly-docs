# projects/:project_id/items/:item_id/tip

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-items-item_id-tip-GET/

---

Items

GET

# projects/:project_id/items/:item_id/tip

Returns the “tip” version for the given item. Multiple versions of a resource item can be uploaded in a project. The tip version is the most recent one.

Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/data/v1/projects/:project_id/items/:item_id/tip |
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
| item_id   string | The unique identifier of an item. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful retrieval of a specific version. |
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
| data   object | The object containing information on the version of the resource. |
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

## [Example](#example)

Successful retrieval of a specific version.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/items/:item_id/tip' \
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
      "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.b909RzMKR4mhc3O7UBY_8g%3Fversion%3D2"
    }
  },
  "data": {
    "type": "versions",
    "id": "urn:adsk.wipprod:fs.file:vf.b909RzMKR4mhc3O7UBY_8g?version=2",
    "attributes": {
      "name": "version-test.pdf",
      "displayName": "version-test.pdf",
      "createTime": "2016-04-01T11:12:35.000Z",
      "createUserId": "BW9RM76WZBGL",
      "createUserName": "John Doe",
      "lastModifiedTime": "2016-04-01T11:15:22.000Z",
      "lastModifiedUserId": "BW9RM76WZBGL",
      "lastModifiedUserName": "John Doe",
      "versionNumber": 2,
      "mimeType": "application/pdf",
      "extension": {
        "type": "versions:autodesk.bim360:File",
        "version": "1.0",
        "schema": {
          "href": "https://developer.api.autodesk.com/schema/v1/versions/versions%3Aautodesk.bim360%3AFile-1.0"
        },
        "data": {
          "tempUrn": null,
          "properties": {},
          "storageUrn": "urn:adsk.objects:os.object:wip.dm.prod/9f8bdc3f-e29c-4ada-ab7b-bb8dfa821163.pdf",
          "storageType": "OSS",
          "conformingStatus": "NONE"
        }
      }
    },
    "links": {
      "self": {
        "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.b909RzMKR4mhc3O7UBY_8g%3Fversion%3D2"
      },
      "webView": {
        "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.0J4paz_FQgWPX2QRsaBkiw/detail/viewer/items/urn%3Aadsk.wipprod%3Afs.file%3Avf.b909RzMKR4mhc3O7UBY_8g%3Fversion%3D2"
      }
    },
    "relationships": {
      "item": {
        "links": {
          "related": {
            "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3Ab909RzMKR4mhc3O7UBY_8g"
          }
        },
        "data": {
          "type": "items",
          "id": "urn:adsk.wipprod:dm.lineage:b909RzMKR4mhc3O7UBY_8g"
        }
      },
      "refs": {
        "links": {
          "self": {
            "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.b909RzMKR4mhc3O7UBY_8g%3Fversion%3D2/relationships/refs"
          },
          "related": {
            "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.b909RzMKR4mhc3O7UBY_8g%3Fversion%3D2/refs"
          }
        }
      },
      "links": {
        "links": {
          "self": {
            "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.b909RzMKR4mhc3O7UBY_8g%3Fversion%3D2/relationships/links"
          }
        }
      },
      "storage": {
        "meta": {
          "link": {
            "href": "/oss/v2/buckets/wipbucket/objects/9f8bdc3f-e29c-4ada-ab7b-bb8dfa821163.pdf?scopes=b360project.6f8813fe-31a7-4440-bc63-d8ca97c856b4,global,O2tenant.tenantId"
          }
        },
        "data": {
          "type": "objects",
          "id": "urn:adsk.objects:os.object:wip.dm.prod/9f8bdc3f-e29c-4ada-ab7b-bb8dfa821163.pdf"
        }
      },
      "derivatives": {
        "data": {
          "type": "derivatives",
          "id": "dXJuOmFkc2sud2lwcWE6ZnMuZmlsZTp2Zi50X3hodWwwYVFkbWhhN2FBaVBuXzlnP3ZlcnNpb249MQ"
        },
        "meta": {
          "link": {
            "href": "/modelderivative/v2/designdata/dXJuOmFkc2sud2lwcWE6ZnMuZmlsZTp2Zi50X3hodWwwYVFkbWhhN2FBaVBuXzlnP3ZlcnNpb249MQ/manifest?scopes=b360project.6f8813fe-31a7-4440-bc63-d8ca97c856b4,global,O2tenant.tenantId"
          }
        }
      },
      "thumbnails": {
        "data": {
          "type": "thumbnails",
          "id": "dXJuOmFkc2sud2lwcWE6ZnMuZmlsZTp2Zi50X3hodWwwYVFkbWhhN2FBaVBuXzlnP3ZlcnNpb249MQ"
        },
        "meta": {
          "link": {
            "href": "/modelderivative/v2/designdata/dXJuOmFkc2sud2lwcWE6ZnMuZmlsZTp2Zi50X3hodWwwYVFkbWhhN2FBaVBuXzlnP3ZlcnNpb249MQ/thumbnail?scopes=b360project.295285be-9cac-44d6-b365-625ebd327483,global,O2tenant.tenantId"
          }
        }
      },
      "downloadFormats": {
        "links": {
          "related": {
            "href": "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.b909RzMKR4mhc3O7UBY_8g%3Fversion%3D2/downloadFormats"
          }
        }
      }
    }
  }
}

```

Show More
