# projects/{projectId}/item-types/{id}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-item-types-id-GET/

---

ItemTypes

GET

# projects/{projectId}/item-types/{id}

Retrieve the information about a single submittal type. For more information about submittal types, see the [Help documnentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Types).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/item-types/:id |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring: UUID The ID of the project. Use the [Data Management API](/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- idstring The ID of the submittal item to retrieve revisions for. To obtain this ID, call [GET items](/en/docs/acc/v1/reference/http/submittals-items-GET/).

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful retrieval of item type |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. |
| 401   Unauthorized | Invalid or missing authorization header. Verify the Bearer token and try again. |
| 403   Forbidden | The user is not authorized to perform this action. |
| 404   Not Found | The specified resource was not found. |
| 500   Internal Server Error | An unexpected error occurred on the server while processing the request. |

### Response

## [Body Structure (200)](#body-structure-200)

| id   string: UUID | The internal, globally unique identifier (UUID) for the item type. |
| --- | --- |
| key   string | Not relevant |
| value   string | The name of the submittal item type. |
| platformId   string | Not relevant |
| isActive   boolean | `true`: (default) if the submittal item type has not been deleted. <br>`false`: if the submittal item type has been deleted. |
| isInUse   boolean | `true`: if the submittal item type is currently associated with a submittal item. <br>`false`: if the submittal item type is not currently associated with a submittal item. |
| createdBy   string | The Autodesk ID of the user who created the submittal item type. |
| createdAt   datetime: ISO 8601 | The date and time when the submittal item type was originally created. |
| updatedAt   datetime: ISO 8601 | The date and time when the submittal item type was last updated. |
| updatedBy   string | The Autodesk ID of the user who last updated the submittal item type. |

## [Example](#example)

Successful retrieval of item type

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/item-types/:id' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "5bab7f9b-61cf-45bc-8bce-f88ddd9d380e",
  "key": "my-type",
  "value": "Attic Stock",
  "platformId": "attic stock",
  "isActive": true,
  "isInUse": true,
  "createdBy": "WD43ZJGKDFLFH",
  "createdAt": "2018-02-01T12:09:24.198466Z",
  "updatedAt": "2018-02-01T12:09:24.198466Z",
  "updatedBy": "WD43ZJGKDFLFH"
}

```

Show More
