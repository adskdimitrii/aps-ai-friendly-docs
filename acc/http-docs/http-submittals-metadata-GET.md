# projects/{projectId}/metadata

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-metadata-GET/

---

Metadata

GET

# projects/{projectId}/metadata

Retrieves project metadata and static values needed for creating submittal items and translating retrieved data.

This endpoint serves two main purposes:

1. To retrieve static values, such as submittal roles, user types, and statuses.
2. To obtain project-specific information, like the custom identifier sequence type, which indicates whether the project uses a global or spec sequence.

For detailed steps on creating submittal items, refer to the [Create Submittal Item](../how-to-docs/submittals-create-submittal-item.md) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/metadata |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | A successfully retrieved submittal projectâs metadata. |
| --- | --- |
| 401   Unauthorized | Invalid or missing authorization header. Verify the Bearer token and try again. |
| 403   Forbidden | The user is not authorized to perform this action. |
| 404   Not Found | The specified resource was not found. |
| 500   Internal Server Error | An unexpected error occurred on the server while processing the request. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| id   string: UUID | The unique identifier (UUID) for the metadata object. |
| --- | --- |
| submittalRoles   array: object | A list of submittal roles within the project. |
| id   string | The unique identifier for the submittal role. |
| key   string | Not relevant |
| value   string | The display name of the submittal role. |
| attachmentUrnTypes   array: object | A list of attachment URN types. |
| id   string | The unique identifier for the attachment URN type. |
| key   string | Not relevant |
| value   string | The display name of the attachment URN type. |
| itemTypes   array: object | A list of submittal item types. This is the same as calling [GET item-types](http-submittals-item-types-GET.md) |
| id   string: UUID | The internal, globally unique identifier (UUID) for the item type. |
| key   string | Not relevant |
| value   string | The name of the submittal item type. |
| platformId   string | Not relevant |
| isActive   boolean | `true`: (default) if the submittal item type has not been deleted. <br>`false`: if the submittal item type has been deleted. |
| isInUse   boolean | `true`: if the submittal item type is currently associated with a submittal item. <br>`false`: if the submittal item type is not currently associated with a submittal item. |
| createdBy   string | The Autodesk ID of the user who created the submittal item type. |
| createdAt   datetime: ISO 8601 | The date and time when the submittal item type was originally created. |
| updatedAt   datetime: ISO 8601 | The date and time when the submittal item type was last updated. |
| updatedBy   string | The Autodesk ID of the user who last updated the submittal item type. |
| adminMappingsSubmittalRoles   array: object | A list of admin mappings for submittal roles. |
| id   string | The unique identifier for the submittal role. |
| key   string | Not relevant |
| value   string | The display name of the submittal role. |
| userTypes   array: object | Types of users, such as individual users, companies, and roles. |
| id   string | The unique identifier for the user type. |
| key   string | Not relevant |
| value   string | The display name of the user type. |
| statuses   array: object | A list of statuses representing different stages of a submittal item. |
| id   string | The unique identifier for the status. |
| key   string | Not relevant |
| value   string | The display name of the status. |
| responses   array: object | A list of responses.This is the same as calling [GET responses](http-submittals-responses-GET.md) |
| id   string: UUID | The internal, globally unique identifier (UUID) for the response. |
| key   string | Not relevant |
| value   string | The content of the response. |
| platformId   string | Not relevant |
| isActive   boolean | `true`: if the response was not deleted. <br>`false`: if the response was deleted. |
| categoryId   string | The type of response. Possible values: `1` (Approved), `2` (Revise and submit), `3` (Rejected). |
| isApproval   boolean | `true`: settings this response for a submittal item means an approval. <br>`false`: settings this response for a submittal item means dis-approval.<br>This attribute is taken from the related categoryId |
| isInUse   boolean | `true`: if the response is currently associated with a submittal item. <br>`false`: if the response is not currently associated with a submittal item. |
| createdBy   string | The Autodesk ID of the user who created the response. |
| createdAt   datetime: ISO 8601 | The time and date when the response was created. |
| updatedAt   datetime: ISO 8601 | The time and date when the response was last updated. |
| updatedBy   string | The Autodesk ID of the user who last updated the response. |
| attachmentCategories   array: object | A list of attachment categories. |
| id   string | The unique identifier for the attachment category. |
| key   string | Not relevant |
| value   string | The display name of the attachment category. |
| attachmentTypes   array: object | A list of attachment types. |
| id   string | The unique identifier for the attachment type. |
| key   string | Not relevant |
| value   string | The display name of the attachment type. |
| isManagerMappingDefined   boolean | `true`: if there is at least one manager mapping in the project. <br>`false`: if there are no manager mappings in the project. |
| noPackagesInProject   boolean | `true`: if there are no packages in the project. <br>`false`: if there are packages in the project. |
| noItemsInProject   boolean | `true`: if there are no submittal items in the project. <br>`false`: if there are submittal items in the project. |
| responseCategories   array: object | A list of categories for responses to submittals. |
| id   string | The unique ID for the response category. |
| value   string | The display name of the category as shown in the UI. |
| isApproval   boolean | `true`: if this option is for an approved submittal response. <br>`false`: if this option is for other-typed submittal responses. |
| defaultValues   object | An object containing the default values for various settings and configurations in the project. |
| watchers   array: object | A list of project watchers, who can be individual users, roles, or companies. |
| id   string | The Autodesk ID of the watcher. The watcher can be a user (`autodeskId`), role (`memberGroupId`), or company (`memberGroupId`). <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](en/docs/acc/v1/reference/http/projects-:project_id-companies-GET/). Note that we do not currently support finding details about roles for a project. |
| userType   object | The type of watcher assigned to the submittal item. <br>Possible values:<br>`1` (user)`2` (company)`3` (role) |
| manager   string | The Autodesk ID of the user who is assigned as the manager. |
| reviewTime   int | The number of days remaining until the review due date. |
| updatedAt   datetime: ISO 8601 | The date and time when the response was last updated, in ISO 8601 format. |
| updatedBy   string | The Autodesk ID of the user that last updated the response. |
| customIdentifierSequenceType   enum:string | The custom numbering sequence type for the current project. Possible values: `1` (Global sequence), `2` (Spec sequence). |

## [Example](#example)

A successfully retrieved submittal projectâs metadata.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/metadata' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "e8302552-fc5a-42ac-ba4b-e9de9760c356",
  "submittalRoles": [
    {
      "id": "4",
      "key": "admin",
      "value": "Admin"
    }
  ],
  "attachmentUrnTypes": [
    {
      "id": "2",
      "key": "dm",
      "value": "DM"
    }
  ],
  "itemTypes": [
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
  ],
  "adminMappingsSubmittalRoles": [
    {
      "id": "4",
      "key": "admin",
      "value": "Admin"
    }
  ],
  "userTypes": [
    {
      "id": "2",
      "key": "company",
      "value": "Company"
    }
  ],
  "statuses": [
    {
      "id": "2",
      "key": "open",
      "value": "Open"
    }
  ],
  "responses": [
    {
      "id": "5bab7f9b-61cf-45bc-8bce-f88ddd9d380e",
      "key": "my response",
      "value": "Approved",
      "platformId": "approved",
      "isActive": false,
      "categoryId": "1",
      "isApproval": false,
      "isInUse": false,
      "createdBy": "WD43ZJGKDFLFH",
      "createdAt": "2018-02-01T12:09:24.198466Z",
      "updatedAt": "2018-02-01T12:09:24.198466Z",
      "updatedBy": "WD43ZJGKDFLFH"
    }
  ],
  "attachmentCategories": [
    {
      "id": "2",
      "key": "for_review",
      "value": "For Review"
    }
  ],
  "attachmentTypes": [
    {
      "id": "2",
      "key": "photo",
      "value": "Photo"
    }
  ],
  "isManagerMappingDefined": false,
  "noPackagesInProject": false,
  "noItemsInProject": false,
  "responseCategories": [
    {
      "id": "1",
      "value": "Approved",
      "isApproval": "true"
    }
  ],
  "defaultValues": {
    "watchers": [
      {
        "id": "224356",
        "userType": "2"
      },
      {
        "id": "3522614",
        "userType": "3"
      }
    ],
    "manager": "WD43ZJGKDFLFH",
    "reviewTime": 7,
    "updatedAt": "2018-02-01T12:09:24.198466Z",
    "updatedBy": "WD43ZJGKDFLFH"
  },
  "customIdentifierSequenceType": "1"
}

```

Show More
