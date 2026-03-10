# hubs/:hub_id/projects/:project_id

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/hubs-hub_id-projects-project_id-GET/

---

Projects

GET

# hubs/:hub_id/projects/:project_id

Returns a project for a given `project_id`.

Note that for BIM 360 Docs, a hub ID corresponds to an account ID in the [BIM 360 API](https://aps.autodesk.com/en/docs/bim360/v1/). To convert an account ID into a hub ID you need to add a "**b.**" prefix. For example, an account ID of c8b0c73d-3ae9 translates to a hub ID of **b.**c8b0c73d-3ae9.

Similarly, for BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a "**b.**" prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of **b.**c8b0c73d-3ae9.

**New!** Autodesk Construction Cloud platform (ACC). Note that this endpoint is compatible with ACC projects. For more information about the Autodesk Construction Cloud APIs, see the [Autodesk Construction Cloud documentation](https://aps.autodesk.com/en/docs/acc/v1/overview/).

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/project/v1/hubs/:hub_id/projects/:project_id |
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
| project_id   string | The unique identifier of a project. <br>For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a “**b.**" prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of **b.**c8b0c73d-3ae9. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful retrieval of a specific project. |
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
| data   object | The object containing information on the project. |
| type   enum:string | The type of this resource. Will always be: `projects` |
| id   string | The id of the resource. |
| attributes   object | The attributes of the project. |
| name   string | Displayable name of the project. |
| scopes   array: string | The array of scopes applicable to this project. |
| extension   object | The extension object of the data. |
| type   string | The type of the schema that the resource’s data object adheres to. |
| version   string | The version of the schema that the data is adhering to. |
| schema   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | Additional properties that the resource’s data possesses. Note that the types of properties in the `data` object changes according to the resource type. |
| projectType   string | The type of project. Only relevant for BIM 360 and ACC projects. Possible values: `BIM360`, `ACC`. |
| relationships   object | The resources that share a relationship with this project. |
| hub   object | Information on resources that are found above this resource. |
| links   object | The object containing information on links of related resources. |
| related   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| rootFolder   object | Information on resources that are indirectly related to this resource. |
| meta   object | Meta-information on links to this resource. |
| link   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| topFolders   object | Information on resources that are found under this resource. |
| links   object | The object containing information on links of related resources. |
| related   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| issues   object | Information on resources that are indirectly related to this resource. This is available only with BIM360. |
| meta   object | Meta-information on links to this resource. |
| link   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| submittals   object | Information on resources that are indirectly related to this resource. This is available only with BIM360. |
| meta   object | Meta-information on links to this resource. |
| link   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| rfis   object | Information on resources that are indirectly related to this resource. This is available only with BIM360. |
| meta   object | Meta-information on links to this resource. |
| link   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| markups   object | Information on resources that are indirectly related to this resource. This is available only with BIM360. |
| meta   object | Meta-information on links to this resource. |
| link   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| checklists   object | Information on resources that are indirectly related to this resource. This is available only with BIM360. |
| meta   object | Meta-information on links to this resource. |
| link   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| cost   object | Information on resources that are indirectly related to this resource. This is available only with BIM360. |
| meta   object | Meta-information on links to this resource. |
| link   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| locations   object | Information on resources that are indirectly related to this resource. This is available only with BIM360. |
| meta   object | Meta-information on links to this resource. |
| link   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| links   object | Information on links to this resource. |
| self   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| webView   object | An object containing a link that opens the resource in a browser. |
| href   string | The location (URL) of the resource the link goes to. |

## [Example](#example)

Successful retrieval of a specific project.

### Request

```
curl -v 'https://developer.api.autodesk.com/project/v1/hubs/:hub_id/projects/:project_id' \
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
      "href": "https://developer.api.autodesk.com/project/v1/hubs/b.622cb5d1-581b-4a46-a6d9-4ebc68ea4051/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d"
    }
  },
  "data": {
    "type": "projects",
    "id": "b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d",
    "attributes": {
      "name": "my project",
      "scopes": [
        "global"
      ],
      "extension": {
        "type": "projects:autodesk.bim360:Project",
        "version": "1.0",
        "schema": {
          "href": "https://developer.api.autodesk.com/schema/v1/versions/projects:autodesk.bim360:Project-1.0"
        },
        "data": {
          "projectType": "BIM360"
        }
      }
    },
    "links": {
      "self": {
        "href": "https://developer.api.autodesk.com/project/v1/hubs/b.622cb5d1-581b-4a46-a6d9-4ebc68ea4051/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d"
      },
      "webView": {
        "href": "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d"
      }
    },
    "relationships": {
      "hub": {
        "data": {
          "type": "hubs",
          "id": "b.622cb5d1-581b-4a46-a6d9-4ebc68ea4051"
        },
        "links": {
          "related": {
            "href": "https://developer.api.autodesk.com/project/v1/hubs/b.622cb5d1-581b-4a46-a6d9-4ebc68ea4051"
          }
        }
      },
      "rootFolder": {
        "data": {
          "type": "folders",
          "id": "urn:adsk.wipprod:fs.folder:co.lw7b0sXUQ-6hWRgf34hBuw"
        },
        "meta": {
          "link": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn:adsk.wipprod:fs.folder:co.lw7b0sXUQ-6hWRgf34hBuw"
          }
        }
      },
      "topFolders": {
        "links": {
          "related": {
            "href": "https://developer.api.autodesk.com/project/v1/hubs/b.622cb5d1-581b-4a46-a6d9-4ebc68ea4051/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/topFolders"
          }
        }
      },
      "issues": {
        "data": {
          "type": "issueContainerId",
          "id": "93f8bd6a-2222-415c-8d58-c8fa7c292044"
        },
        "meta": {
          "link": {
            "href": "https://developer.api.autodesk.com/issues/v1/containers/93f8bd6a-2222-415c-8d58-c8fa7c292044/issues"
          }
        }
      },
      "submittals": {
        "data": {
          "type": "submittalContainerId",
          "id": "c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d"
        },
        "meta": {
          "link": {
            "href": "https://developer.api.autodesk.com/submittals/v1/containers/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items"
          }
        }
      },
      "rfis": {
        "data": {
          "type": "rfisContainerId",
          "id": "93f8bd6a-2222-415c-8d58-c8fa7c292044"
        },
        "meta": {
          "link": {
            "href": "https://developer.api.autodesk.com/bim360/rfis/v1/containers/93f8bd6a-2222-415c-8d58-c8fa7c292044/rfis"
          }
        }
      },
      "markups": {
        "data": {
          "type": "markupsContainerId",
          "id": "93f8bd6a-2222-415c-8d58-c8fa7c292044"
        },
        "meta": {
          "link": {
            "href": "https://developer.api.autodesk.com/issues/v1/containers/93f8bd6a-2222-415c-8d58-c8fa7c292044/markups"
          }
        }
      },
      "checklists": {
        "data": {
          "type": "checklistsContainerId",
          "id": "93f8bd6a-2222-415c-8d58-c8fa7c292044"
        },
        "meta": {
          "link": {
            "href": "https://developer.api.autodesk.com/bim360/checklists/v1/containers/93f8bd6a-2222-415c-8d58-c8fa7c292044/instances"
          }
        }
      },
      "cost": {
        "data": {
          "type": "costContainerId",
          "id": "c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d"
        },
        "meta": {
          "link": {
            "href": "https://developer.api.autodesk.com/cost/v1/containers/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/budgets"
          }
        }
      },
      "locations": {
        "data": {
          "type": "locationsContainerId",
          "id": "5010258a-a341-4d95-8046-3905e1a983a6"
        },
        "meta": {
          "link": {
            "href": "https://developer.api.autodesk.com/bim360/locations/v2/containers/5010258a-a341-4d95-8046-3905e1a983a6/trees/default/nodes"
          }
        }
      }
    }
  }
}

```

Show More
