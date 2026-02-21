# hubs

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/hubs-GET/

---

Hubs

GET

# hubs

Returns a collection of accessible hubs for this member.

Hubs represent BIM 360 Team hubs, Fusion Team hubs (formerly known as A360 Team hubs), A360 Personal hubs, or BIM 360 Docs accounts.
Team hubs include BIM 360 Team hubs and Fusion Team hubs (formerly known as A360 Team hubs).
Personal hubs include A360 Personal hubs. Only active hubs are listed.

Note that for BIM 360 Docs, a hub ID corresponds to an account ID in the [BIM 360 API](/en/docs/bim360/v1/). To convert an account ID into a hub ID you need to add a "**b.**" prefix. For example, an account ID of c8b0c73d-3ae9 translates to a hub ID of **b.**c8b0c73d-3ae9.

**New!** Autodesk Construction Cloud platform (ACC). Note that this endpoint is compatible with ACC projects. For more information about the Autodesk Construction Cloud APIs, see the [Autodesk Construction Cloud documentation](/en/docs/acc/v1/overview/).

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/project/v1/hubs |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| x-user-id   string | In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified. |

* Required

### Request

## [Query String Parameters](#query-string-parameters)

| filter[id]   array: string | Filter by the `id` of the `ref` target. |
| --- | --- |
| filter[name]   array: string | Filter by the `name` of the `ref` target. |
| filter[extension.type]   array: string | Filter by extension type. Possible values: `hubs:autodesk.core:Hub` (team hubs), `hubs:autodesk.bim360:Account` (BIM 360 Docs accounts), `hubs:autodesk.a360:PersonalHub` (personal hubs). |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful retrieval of the hubs collection. |
| --- | --- |
| 401   Unauthorized | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. |
| 403   Forbidden | The request was successfully validated but permission is not granted or the application has not been white-listed. Do not try again unless you solve permissions first. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| jsonapi   object | The JSON API object. |
| --- | --- |
| version   enum:string | The version of JSON API. Will always be: `1.0` |
| links   object | Information on links to this resource. |
| self   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   array: object | The array of hub objects. |
| type   enum:string | The type of this resource. Will always be: `hubs` |
| id   string | The id of the resource. |
| attributes   object | The attributes of the hub. |
| name   string | Displayable name of the hub. |
| extension   object | The extension object of the data. |
| type   string | The type of the schema that the resourceâs data object adheres to. |
| version   string | The version of the schema that the data is adhering to. |
| schema   object | An object containing an API link property. |
| href   string | A hyperlink reference to this resource. |
| data   object | Additional properties that the resourceâs data possesses. |
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

Successful retrieval of the hubs collection.

### Request

```
curl -v 'https://developer.api.autodesk.com/project/v1/hubs' \
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
      "href": "/project/v1/hubs"
    }
  },
  "data": [
    {
      "type": "hubs",
      "id": "a.ZXhhbXBsZTp3aXAxZnFhYXV0b2Rlc2sxNjE",
      "attributes": {
        "name": "my team hub",
        "extension": {
          "type": "hubs:autodesk.core:Hub",
          "version": "1.0",
          "schema": {
            "href": "/schema/v1/versions/hubs%3Aautodesk.core%3AHub-1.0"
          },
          "data": {}
        },
        "region": "US"
      },
      "links": {
        "self": {
          "href": "/project/v1/hubs/a.ZXhhbXBsZTp3aXAxZnFhYXV0b2Rlc2sxNjE"
        }
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
      }
    },
    {
      "type": "hubs",
      "id": "a.ZXhhbXBsZTp3aXAxZnFhYXV0b2Rlc2sxNjI=",
      "attributes": {
        "name": "my personal hub",
        "extension": {
          "type": "hubs:autodesk.a360:PersonalHub",
          "version": "1.0",
          "schema": {
            "href": "/schema/v1/versions/hubs%3Aautodesk.a360%3APersonalHub-1.0"
          },
          "data": {}
        },
        "region": "US"
      },
      "links": {
        "self": {
          "href": "/project/v1/hubs/a.ZXhhbXBsZTp3aXAxZnFhYXV0b2Rlc2sxNjI="
        }
      },
      "relationships": {
        "projects": {
          "links": {
            "related": {
              "href": "/project/v1/hubs/a.ZXhhbXBsZTp3aXAxZnFhYXV0b2Rlc2sxNjI=/projects"
            }
          }
        },
        "pimCollection": {
          "data": {
            "type": "collection",
            "id": "co.368e3dc4144c0ff253d6"
          }
        }
      }
    }
  ]
}

```

Show More
