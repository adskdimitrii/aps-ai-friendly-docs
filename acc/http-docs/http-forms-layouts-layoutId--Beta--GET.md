# v1/projects/{projectId}/layouts/{layoutId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/forms-layouts-layoutId-(Beta)-GET/

---

Templates

GET

# v1/projects/{projectId}/layouts/{layoutId}

Returns layout information for a form template.

Layouts define the structure and configuration of form templates, including sections, fields, and their properties.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/layouts/:layoutId |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |
| layoutId   string | The unique identifier of the layout. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Layout information. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found |
| 429   Too Many Requests | The request could not be completed due to the rate limit of the target resource |
| 500   Internal Server Error | The request could not be completed due to an internal server error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| layout   object |  |
| --- | --- |
| uid   string: UUID | The unique identifier of the layout. |
| type   enum:string | The type of the layout. Will always be: `form` |
| description   string | The description of the layout. |
| hasSectionAssignees   boolean | Determines if section assignment is enabled. |
| sections   array: object | The list of sections within the layout. |
| uid   string: UUID | The unique identifier of the section. |
| layoutUid   string: UUID | The unique identifier of the parent layout. |
| sortIndex   int | The sort order index of the section. |
| displayIndex   int | The display order index of the section. |
| type   enum:string | The type of the section. Will always be: `section` |
| assigneeType   enum:string | The type of assignee for the section. Possible values: `user`, `company`, `role` |
| assigneeId   string | The ID of the assignee for the section. |
| label   string | The label of the section. |
| description   string | The description of the section. |

## [Example](#example)

Layout information.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/layouts/:layoutId' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "layout": {
    "uid": "123e4567-e89b-12d3-a456-426614174000",
    "type": "form",
    "description": "Standard form layout for field reports",
    "hasSectionAssignees": false
  },
  "sections": [
    {
      "uid": "123e4567-e89b-12d3-a456-426614174001",
      "layoutUid": "123e4567-e89b-12d3-a456-426614174000",
      "sortIndex": 0,
      "displayIndex": 0,
      "type": "section",
      "assigneeType": "user",
      "assigneeId": "",
      "label": "General Information",
      "description": ""
    }
  ]
}

```

Show More
