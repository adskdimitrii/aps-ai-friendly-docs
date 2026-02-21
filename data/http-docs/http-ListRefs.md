# ListRefs

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/ListRefs/

---

Commands

# ListRefs

Retrieves the custom relationships between specified versions of items and other resources in the `data` domain service (folders, items, and versions). You can retrieve the relationships of up to 50 versions.

Note that ListRefs is a Data Management command. Commands enable you to perform complex operations on multiple resources
rather than standard CRUD operations. For more details about commands, see the[Commands](/en/docs/data/v2/overview/commands) overview section.

**New!** Autodesk Construction Cloud platform (ACC). Note that this endpoint is compatible with ACC projects. For more information about the Autodesk Construction Cloud APIs, see the [Autodesk Construction Cloud documentation](/en/docs/acc/v1/overview/).

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/data/v1/projects/:project_id/commands |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| x-user-id   string | In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified. |
| Content-Type*   string | Must be `application/vnd.api+json`. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| project_id   string | The unique identifier of a project. <br>For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a â**b.**" prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of **b.**c8b0c73d-3ae9. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

The POST body is a JSON object with the following attributes.

Expand all

| *jsonapi**   object | The JSON API object. |
| --- | --- |
| version*   enum:string | The version of JSON API. Must always be: `1.0` |
| *data**   object | The data object. |
| type*   enum:string | The type of this resource. Must always be: `commands` |
| attributes*   object | The attributes of the data object. |
| extension*   object | The extension object of the data. |
| type*   enum:string | The type of command. Must always be: `commands:autodesk.core:ListRefs` |
| version*   string | The version of the command. |
| relationships*   object | An object that represents related resources.   In this case, it is used to list the resourceâs metadata which should be retrieved. |
| resources*   object | An object that represents related resources.   In this case, it is used to list the resourceâs metadata which should be retrieved. |
| data*   array:object | The list of versions you want to retrieve the relationships for. |
| type*   enum:string | The type of resource. Must always be: `versions` |
| id*   string | The URN of the version; to verify the URN, see the [GET projects/:project_id/items/:item_id/versions](/en/docs/data/v2/reference/http/projects-project_id-items-item_id-versions-GET) endpoint. |

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
| id   string | Unique identifier of the command. |
| type   enum:string | The type of entity. Will always be: `commands` |
| attributes   object | The attributes of the data object. |
| status   enum:string | The status of the requested command. Possible values: `accepted`, `committed`, `completed`, `failed` |
| extension   object | The extension object of the data. |
| type   enum:string | The type of command. Will always be: `commands:autodesk.core:ListRefs` |
| version   string | The version of the command. |
| schema   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| relationships   object | An object that represents related resources.   In this case, it is used to list the resourceâs metadata. |
| resources   object | An object that represents related resources.   In this case, it is used to list the resourceâs metadata. |
| data   array: object | List of the relationships between the specified versions and other versions, items and folders. Each relationship returns a `type`, an `id`, and a `meta` object. |
| type   enum:string | The type of resource. Must always be: `versions` |
| id   string | The URN of the version. |
| meta   object | Includes metadata about the type and direction of the relationships. For information about the metadata, see the Custom Relationships and Extension Types sections in the [API Basics](/en/docs/model-derivative/v2/overview/basics) section. |
| *included*   array: object | List of relationships for each version that was passed in data.relationships.resources.data. |
| id   string | The URN of the resource. |
| type   enum:string | The type of the resource. Possible values: `items`, `versions` |
| attributes   object | The attributes of the resource. |
| displayName   string | Displayable name of the version. |
| hidden   boolean | `true` if the file has been deleted. `false` if the file has not been deleted. |
| reserved   boolean | Indicates the availability of the file. A reserved file can only be modified by the user that reserved it. |
| reservedTime   datetime: ISO 8601 | The time the item was reserved. |
| reservedUserId   string | The unique identifier of the user who reserved the item. |
| reservedUserName   string | The name of the user who reserved the item. |
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
| extension   object | The extension object of the resource. |
| type   string | The type of the schema that the resourceâs data object adheres to. |
| version   string | The version of the schema that the data is adhering to. |
| schema   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | Additional properties that the resourceâs data possesses. |
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
curl -X POST -H "Authorization: Bearer kEnG562yz5bhE9igXf2YTcZ2bu0z" -H "Content-Type: application/vnd.api+json" -d '
{
    "jsonapi": {
        "version": "1.0"
    },
    "data": {
        "type": "commands",
        "attributes": {
            "extension": {
                "type": "commands:autodesk.core:ListRefs",
                "version": "1.0.0"
            }
        },
        "relationships": {
            "resources": {
                "data": [
                    {
                        "type": "versions",
                        "id": "urn:adsk.wipqa:fs.file:vf.3pGffROYQx6efm0eR26DEg?version=1"
                    }
                ]
            }
        }
    }
}' "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/commands/"

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
        "id": "61f0f2fe-a71f-4004-a5e4-de0ce2cd968c",
        "attributes": {
            "status": "complete",
            "extension": {
                "type": "commands:autodesk.core:ListRefs",
                "version": "1.0.0"
            }
        },
        "relationships": {
            "resources": {
                "data": [
                    {
                        "type": "versions",
                        "id": "urn:adsk.wipqa:fs.file:vf.3fcaI3iqS56R8OHUMdDSdg?version=1",
                        "meta": {
                            "refType": "derived",
                            "fromId": "urn:adsk.wipqa:fs.file:vf.3fcaI3iqS56R8OHUMdDSdg?version=1",
                            "fromType": "versions",
                            "toId": "urn:adsk.wipqa:fs.file:vf.3pGffROYQx6efm0eR26DEg?version=1",
                            "toType": "versions",
                            "direction": "to",
                            "extension": {
                                "type": "derived:autodesk.bim360:FileToDocument",
                                "version": "1.0",
                                "schema": {
                                    "href": "https://developer.api.autodesk.com/schema/v1/versions/derived:autodesk.bim360:FileToDocument-1.0"
                                },
                                "data": {}
                            }
                        }
                    }
                ]
            }
        }
    },
    "included": [
        {
            "type": "items",
            "id": "urn:adsk.wipqa:dm.lineage:3pGffROYQx6efm0eR26DEg",
            "attributes": {
                "displayName": "",
                "hidden": false,
                "reserved": false,
                "extension": {
                    "type": "items:autodesk.bim360:Document",
                    "version": "1.0",
                    "schema": {
                        "href": "https://developer.api.autodesk.com/schema/v1/versions/items:autodesk.bim360:Document-1.0"
                    },
                    "data": {}
                }
            },
            "links": {
                "self": {
                    "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn:adsk.wipqa:dm.lineage:3pGffROYQx6efm0eR26DEg"
                },
                "webView": {
                    "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.0J4paz_FQgWPX2QRsaBkiw/detail/viewer/items/urn:adsk.wipqa:dm.lineage:3pGffROYQx6efm0eR26DEg"
                }
            }
        },
        {
            "type": "items",
            "id": "urn:adsk.wipqa:dm.lineage:3fcaI3iqS56R8OHUMdDSdg",
            "attributes": {
                "displayName": "BD4359-A-SK035-009_WC_Mock-up_Plan.pdf",
                "hidden": false,
                "reserved": false,
                "extension": {
                    "type": "items:autodesk.bim360:File",
                    "version": "1.0",
                    "schema": {
                        "href": "https://developer.api.autodesk.com/schema/v1/versions/items:autodesk.bim360:File-1.0"
                    },
                    "data": {}
                }
            },
            "links": {
                "self": {
                    "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn:adsk.wipqa:dm.lineage:3fcaI3iqS56R8OHUMdDSdg"
                }
            }
        },
        {
            "type": "versions",
            "id": "urn:adsk.wipqa:fs.file:vf.3pGffROYQx6efm0eR26DEg?version=1",
            "attributes": {
                "name": "SK035 INFORMATION",
                "displayName": "SK035 INFORMATION",
                "versionNumber": 1,
                "extension": {
                    "type": "versions:autodesk.bim360:Document",
                    "version": "1.0",
                    "schema": {
                        "href": "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.bim360:Document-1.0"
                    },
                    "data": {
                        "processState": "PROCESSING_COMPLETE",
                        "viewableId": "1",
                        "viewableGuid": "bcd84049-3c9a-469f-b053-40cd535fe883",
                        "viewableName": "1",
                        "viewableOrder": 1
                    }
                }
            },
            "links": {
                "self": {
                    "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn:adsk.wipqa:fs.file:vf.3pGffROYQx6efm0eR26DEg%3Fversion=1"
                }
            }
        },
        {
            "type": "versions",
            "id": "urn:adsk.wipqa:fs.file:vf.3fcaI3iqS56R8OHUMdDSdg?version=1",
            "attributes": {
                "name": "BD4359-A-SK035-009_WC_Mock-up_Plan.pdf",
                "displayName": "BD4359-A-SK035-009_WC_Mock-up_Plan.pdf",
                "versionNumber": 1,
                "storageSize": 46197,
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
                    "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn:adsk.wipqa:fs.file:vf.3fcaI3iqS56R8OHUMdDSdg%3Fversion=1"
                }
            }
        }
    ]
}

```

Show More
