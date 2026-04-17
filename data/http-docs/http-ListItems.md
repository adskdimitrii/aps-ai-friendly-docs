# ListItems

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/ListItems/

---

Commands

# ListItems

Retrieves metadata for up to 50 specified items. For example, an item name, or the date it was created. It returns the `tip` (latest) version of the items.

Note that ListItems is a Data Management command. Commands enable you to perform complex operations on multiple resources
rather than standard CRUD operations. For more details about commands, see the[Commands](https://aps.autodesk.com/en/docs/data/v2/overview/commands/) overview section.

Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/data/v1/projects/:project_id/commands |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-user-id   string | In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified. |
| Content-Type*   string | Must be `application/vnd.api+json`. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| project_id   string | The unique identifier of a project. <br>For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a “**b.**" prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of **b.**c8b0c73d-3ae9. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

The POST body is a JSON object with the following attributes.

Expand all

| *jsonapi**   object | The JSON API object. |
| --- | --- |
| version*   enum:string | The version of JSON API. Must always be: `1.0` |
| *data**   object | The data object. |
| type*   enum:string | The type of entity. Will always be: `commands` |
| attributes*   object | The attributes of the data object. |
| extension*   object | The extension object of the data. |
| type*   enum:string | The type of command. Will always be: `commands:autodesk.core:ListItems` |
| version*   string | The version of the command. |
| data   object | Additional properties that the resource’s data possesses. |
| includePathInProject   boolean | Specify whether to return pathInProject attribute in response for BIM 360 Docs projects. pathInProject is the relative path of the item starting from project’s root folder. <br>`true`: response will include pathInProject attribute for BIM 360 Docs projects.<br>`false` (default): response will not include pathInProject attribute for BIM 360 Docs projects. |
| relationships*   object | An object that represents related resources.   In this case, it is used to list the resource’s metadata which should be retrieved. |
| resources*   object | An object that represents related resources.   In this case, it is used to list the resource’s metadata which should be retrieved. |
| data*   array:object | List of items. Each item requires a `type` and `id` |
| type*   string | The type of resource. Will always be: `items` |
| id*   string | The URN of the item; to verify a URN, see the [GET projects/:project_id/items/:item_id](http-projects-project_id-items-item_id-GET.md) endpoint. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful execution of a command. |
| --- | --- |
| 400   Bad Input | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 403   Forbidden | The request was successfully validated but permission is not granted or the application has not been white-listed. Do not try again unless you solve permissions first. |
| 404   Not Found | The specified resource was not found. |

### Response

## [Body Structure (200)](#body-structure-200)

A successful response returns a JSON object with the following attributes.

Expand all

| *jsonapi*   object | The JSON API object. |
| --- | --- |
| version   enum:string | The version of JSON API. Will always be: `1.0` |
| *data*   object | The data object. |
| id   string | Unique identifier of the command.. |
| type   enum:string | The type of entity. Will always be: `commands` |
| attributes   object | The attributes of the data object. |
| extension   object | The extension object of the data. |
| type   enum:string | The type of command. Will always be: `commands:autodesk.core:ListItems` |
| version   string | The version of the command. |
| schema   string | The link to the schema. |
| relationships   object | An object that represents related resources.   In this case, it is used to list the resource’s metadata. |
| resources   object | An object that represents related resources.   In this case, it is used to list the resource’s metadata. |
| data   array:object | List of metadata for the specified items. |
| type   string | The type of resource. Will always be: `items` |
| id   string | The URN of the item; to verify a URN, see the [GET projects/:project_id/items/:item_id](http-projects-project_id-items-item_id-GET.md) endpoint. |
| meta   object | The meta-information of this resource. See [GET projects/:project_id/items/:item_id](http-projects-project_id-items-item_id-GET.md). |
| webView   object | An object containing a link that opens the resource in a browser. |
| href   string | The location (URL) of the resource the link goes to. |
| *included*   array:object | List of metadata for the tip (latest) version of each item. |
| type   enum:string | The type of this resource. Will always be: `versions` |
| id   string | The id of the resource. |
| attributes   object | The attributes of the resource. |
| name   string | The filename used when synced to local disk. |
| displayName   string | Displayable name of the version. |
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

Successful Execution of a Command (200)

### Request

```
curl -X POST -v "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/commands" -H "Authorization: Bearer kEnG562yz5bhE9igXf2YTcZ2bu0z" -H "Content-Type: application/vnd.api+json" -d '
{
  "jsonapi": {
    "version": "1.0"
  },
  "data": {
    "type": "commands",
    "attributes": {
      "extension": {
        "type": "commands:autodesk.core:ListItems",
        "version": "1.1.0",
        "data": {
          "includePathInProject": true
        }
      }
    },
    "relationships": {
      "resources": {
        "data": [
          {
            "type": "items",
            "id": "urn:adsk.wipprod:dm.lineage:b909RzMKR4mhc3O7UBY_8g"
          }
        ]
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
  "data": {
    "type": "commands",
    "id": "fa214233-abef-4c48-a3de-253bde80cfe4",
    "attributes": {
      "status": "complete",
      "extension": {
        "type": "commands:autodesk.core:ListItems",
        "version": "1.0.0"
      }
    },
    "relationships": {
      "resources": {
        "data": [
          {
            "type": "items",
            "id": "urn:adsk.wipprod:dm.lineage:b909RzMKR4mhc3O7UBY_8g",
            "meta": {
              "type": "items",
              "id": "urn:adsk.wipprod:dm.lineage:b909RzMKR4mhc3O7UBY_8g",
              "attributes": {
                "displayName": "version-test",
                "createTime": "2016-04-01T11:09:03.000Z",
                "createUserId": "BW9RM76WZBGL",
                "createUserName": "Eason Kang",
                "lastModifiedTime": "2016-04-01T11:11:18.000Z",
                "lastModifiedUserId": "BW9RM76WZBGL",
                "lastModifiedUserName": "Eason Kang",
                "hidden": false,
                "reserved": false,
                "extension": {
                  "type": "items:autodesk.bim360:File",
                  "version": "1.0",
                  "schema": {
                    "href": "https://developer.api.autodesk.com/schema/v1/versions/items:autodesk.bim360:File-1.0"
                  },
                  "data": {

                  }
                },
                "pathInProject": "/Project Files/ExampleFolder/SubFolder/4d7daeda-6g7a-4aac-a52a-158833233da3"
              },
              "links": {
                "self": {
                  "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn:adsk.wipprod:dm.lineage:b909RzMKR4mhc3O7UBY_8g"
                },
                "webView": {
                  "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.0J4paz_FQgWPX2QRsaBkiw/detail/viewer/items/urn:adsk.wipprod:dm.lineage:b909RzMKR4mhc3O7UBY_8g"
                }
              },
              "relationships": {
                "tip": {
                  "data": {
                    "type": "versions",
                    "id": "urn:adsk.wipprod:fs.file:vf.wX8PdF8GSa27Zw-Vgd939Q?version=1"
                  },
                  "links": {
                    "related": {
                      "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn:adsk.wipprod:dm.lineage:b909RzMKR4mhc3O7UBY_8g/tip"
                    }
                  }
                },
                "versions": {
                  "links": {
                    "related": {
                      "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn:adsk.wipprod:dm.lineage:b909RzMKR4mhc3O7UBY_8g/versions"
                    }
                  }
                },
                "parent": {
                  "data": {
                    "type": "folders",
                    "id": "urn:adsk.wipprod:dm.folder:sdfedf8wefl"
                  },
                  "links": {
                    "related": {
                      "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn:adsk.wipprod:dm.lineage:b909RzMKR4mhc3O7UBY_8g/parent"
                    }
                  }
                },
                "refs": {
                  "links": {
                    "self": {
                      "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn:adsk.wipprod:dm.lineage:b909RzMKR4mhc3O7UBY_8g/relationships/refs"
                    },
                    "related": {
                      "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn:adsk.wipprod:dm.lineage:b909RzMKR4mhc3O7UBY_8g/refs"
                    }
                  }
                },
                "links": {
                  "links": {
                    "self": {
                      "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn:adsk.wipprod:dm.lineage:b909RzMKR4mhc3O7UBY_8g/relationships/links"
                    }
                  }
                }
              }
            }
          }
        ]
      }
    }
  },
  "included": [
    {
      "type": "versions",
      "id": "urn:adsk.wipprod:fs.file:vf.d34fdsg3g?version=2",
      "attributes": {
        "name": "version-test.pdf",
        "displayName": "version-test",
        "createTime": "2016-04-01T11:09:03.000Z",
        "createUserId": "BW9RM76WZBGL",
        "createUserName": "Eason Kang",
        "lastModifiedTime": "2016-04-01T11:11:18.000Z",
        "lastModifiedUserId": "BW9RM76WZBGL",
        "lastModifiedUserName": "Eason Kang",
        "versionNumber": 1,
        "fileType": "pdf",
        "extension": {
          "type": "versions:autodesk.bim360:File",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.bim360:File-1.0"
          },
          "data": {
            "processState": "PROCESSING_COMPLETE",
            "extractionState": "SUCCESS",
            "splittingState": "SPLIT",
            "reviewState": "ACCEPTED",
            "revisionDisplayLabel": "1"
          }
        }
      },
      "links": {
        "self": {
          "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn:adsk.wipprod:fs.file:vf.d34fdsg3g?version=2"
        },
        "webView": {
          "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.0J4paz_FQgWPX2QRsaBkiw/detail/viewer/items/urn:adsk.wipprod:fs.file:vf.d34fdsg3g%3Fversion%3D2"
        }
      },
      "relationships": {
        "item": {
          "data": {
            "type": "items",
            "id": "urn:adsk.wipprod:dm.lineage:b909RzMKR4mhc3O7UBY_8g"
          },
          "links": {
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn:adsk.wipprod:fs.file:vf.d34fdsg3g?version=2/item"
            }
          }
        },
        "links": {
          "links": {
            "self": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn:adsk.wipprod:fs.file:vf.d34fdsg3g?version=2/relationships/links"
            }
          }
        },
        "refs": {
          "links": {
            "self": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn:adsk.wipprod:fs.file:vf.d34fdsg3g?version=2/relationships/refs"
            },
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn:adsk.wipprod:fs.file:vf.d34fdsg3g?version=2/refs"
            }
          }
        },
        "downloadFormats": {
          "links": {
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn:adsk.wipprod:fs.file:vf.d34fdsg3g?version=2/downloadFormats"
            }
          }
        },
        "derivatives": {
          "data": {
            "type": "derivatives",
            "id": "dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLmQzNGZkc2czZw_dmVyc2lvbj0x"
          },
          "meta": {
            "link": {
              "href": "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLmQzNGZkc2czZw_dmVyc2lvbj0x/manifest"
            }
          }
        },
        "thumbnails": {
          "data": {
            "type": "thumbnails",
            "id": "dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLmQzNGZkc2czZw_dmVyc2lvbj0x"
          },
          "meta": {
            "link": {
              "href": "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLmQzNGZkc2czZw_dmVyc2lvbj0x/thumbnail"
            }
          }
        },
        "storage": {
          "data": {
            "type": "objects",
            "id": "urn:adsk.objects:os.object:wip.dm.prod/3c8f6bbc-fe5c-4815-a92e-8b8635e7b1cb.pdf"
          },
          "meta": {
            "link": {
              "href": "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/3c8f6bbc-fe5c-4815-a92e-8b8635e7b1cb.pdf"
            }
          }
        }
      }
    }
  ]
}

```

Show More
