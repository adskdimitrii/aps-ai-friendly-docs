# hubs/:hub_id/projects/:project_id/hub

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/hubs-hub_id-projects-project_id-hub-GET/

---

Projects

GET

# hubs/:hub_id/projects/:project_id/hub

Returns the hub for a given `project_id`.

Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/project/v1/hubs/:hub_id/projects/:project_id/hub |
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

| hub_id   string | The unique identifier of a hub. |
| --- | --- |
| project_id   string | The unique identifier of a project. <br>To convert BIM 360 or Forma Project IDs to Data Management Project IDs, prefix them with `b.` For example, a Project ID of `c8b0c73d-3ae9` becomes `b.c8b0c73d-3ae9`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful retrieval of a specific hub. |
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
| data   object | The object containing information on the hub. |
| type   enum:string | The type of this resource. Will always be: `hubs` |
| id   string | The id of the resource. |
| attributes   object | The attributes of the hub. |
| name   string | Displayable name of the hub. |
| extension   object | The extension object of the data. |
| type   string | The type of the schema that the resource’s data object adheres to. |
| version   string | The version of the schema that the data is adhering to. |
| schema   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | Additional properties that the resource’s data possesses. |
| region   enum:string | Specifies where the hub is stored. Possible values are: <br>`US` - Data center for the US region.`EMEA` - Data center for the European Union, Middle East, and Africa.`AUS` - Data center for the Australia region.`CAN` - Data center for the Canada region.`DEU` - Data centre for the Germany region.`IND` - Data centre for the India region.`JPN` - Data centre for the Japan region.`GBR` - Data centre for the United Kingdom region. |
| relationships   object | The resources that share a relationship with this hub. |
| projects   object | Information on resources that are found under this resource. |
| links   object | The object containing information on links of related resources. |
| related   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| pimCollection   object | Information on the id and type properties of a resource. This is available only for Fusion Team hubs and A360 Personal hubs. |
| data   object | An object containing the id and type properties of a resource. |
| id   string | The id of the resource. |
| type   string | The type of this resource. |
| links   object | Information on links to this resource. |
| self   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |

## [Example](#example)

Successful retrieval of a specific hub.

### Request

```
curl -v 'https://developer.api.autodesk.com/project/v1/hubs/:hub_id/projects/:project_id/hub' \
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
      "href": "/project/v1/hubs/a.ZXhhbXBsZTp3aXAxZnFhYXV0b2Rlc2sxNjE"
    }
  },
  "data": {
    "type": "hubs",
    "id": "a.ZXhhbXBsZTp3aXAxZnFhYXV0b2Rlc2sxNjE",
    "attributes": {
      "name": "my hub",
      "extension": {
        "data": {},
        "version": "1.0",
        "type": "hubs:autodesk.core:Hub",
        "schema": {
          "href": "/schema/v1/versions/hubs%3Aautodesk.core%3AHub-1.0"
        }
      },
      "region": "US"
    },
    "relationships": {
      "projects": {
        "links": {
          "related": {
            "href": "/project/v1/hubs/a.ZXhhbXBsZTp3aXAxZnFhYXV0b2Rlc2sxNjE/projects"
          }
        }
      },
      "pimCollection": {
        "data": {
          "type": "collection",
          "id": "co.d41d8cd00998ecf8427e"
        }
      }
    },
    "links": {
      "self": {
        "href": "/project/v1/hubs/a.ZXhhbXBsZTp3aXAxZnFhYXV0b2Rlc2sxNjE"
      }
    }
  }
}

```

Show More
