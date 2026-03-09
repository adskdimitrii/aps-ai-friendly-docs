# projects/:project_id/items/:item_id/relationships/refs

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-items-item_id-relationships-refs-POST/

---

Items

POST

# projects/:project_id/items/:item_id/relationships/refs

Creates a custom relationship between an item and another resource within the `data` domain service (folder, item, or version).

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/data/v1/projects/:project_id/items/:item_id/relationships/refs |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:create` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
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

describe the ref to be created.

Expand all

| jsonapi*   object | The JSON API object. |
| --- | --- |
| version*   enum:string | The version of JSON API. Will always be: `1.0` |
| data*   object | The data object. |
| type*   enum:string | The type of this resource. Possible values: `folders`, `items`, `versions` |
| id*   string | The id of the resource. |
| meta*   object | The meta-information of this resource. |
| extension*   object | The object containing information on the base attributes of the extension of an object. |
| type*   string | The type of this resource. |
| version*   string | The version of the resource. |
| data   object | The data object. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | Successful creation of a reference between two resources. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 403   Forbidden | The request was successfully validated but permission is not granted or the application has not been white-listed. Do not try again unless you solve permissions first. |
| 404   Not Found | The specified resource was not found. |

### Response

## [Body Structure (204)](#body-structure-204)

Response for 204 has no body.

## [Example](#example)

Successful creation of a reference between two resources.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/items/:item_id/relationships/refs' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/vnd.api+json' \
  -d '{
        "jsonapi": {
          "version": "1.0"
        },
        "data": {
          "type": "versions",
          "id": "urn:adsk.wipprod:fs.file:vf.ooWjwAQJR0uEoPRyfEnvew?version=1",
          "meta": {
            "extension": {
              "type": "auxiliary:autodesk.core:Attachment",
              "version": "1.0"
            }
          }
        }
      }'

```

Show More

### Response

```
204 No Content

```
