# projects/{projectId}/specs

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-specs-POST/

---

Specs

POST

# projects/{projectId}/specs

Creates a spec section to organize and categorize submittals.

For more information about spec sections, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Create_Spec_section).

For information on how spec sections are used in the submittal workflow, see the [Create Submittal Item tutorial](https://aps-stg.autodesk.com/en/docs/acc/v1/tutorials/submittals/create-submittal-item/).
> Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/specs |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

| title*   string | The title of the spec section to be created. |
| --- | --- |
| identifier*   string | The unique ID to be assigned to the spec section within the UI. Ensure this ID is unique by checking existing spec sections using [GET specs](/en/docs/acc/v1/reference/http/submittals-specs-GET/). |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Successful request to create a new spec section. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. |
| 401   Unauthorized | Invalid or missing authorization header. Verify the Bearer token and try again. |
| 403   Forbidden | The user is not authorized to perform this action. |
| 404   Not Found | The specified resource was not found. |
| 500   Internal Server Error | An unexpected error occurred on the server while processing the request. |

### Response

## [Body Structure (201)](#body-structure-201)

| id   string: UUID | The internal, globally unique identifier (UUID) for the spec section. |
| --- | --- |
| title   string | The title of the spec section. |
| identifier   string | The unique ID assigned to the spec section within the UI. |
| createdBy   string | The Autodesk ID of the user who created the spec section. |
| createdAt   datetime: ISO 8601 | The time and date when the spec section was created. |
| updatedBy   string | The Autodesk ID of the user who last updated the spec section. |
| updatedAt   datetime: ISO 8601 | The time and date when spec section was last updated. |

## [Example](#example)

Successful request to create a new spec section.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/specs' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "title": "Materials",
        "identifier": "500"
      }'

```

Show More

### Response

```
{
  "id": "e6111f96-8437-491e-a1ae-16fd53f0cbef",
  "title": "Materials",
  "identifier": "500",
  "createdBy": "WD43ZJGKDFLFH",
  "createdAt": "2018-02-01T12:09:24.198466Z",
  "updatedBy": "WD43ZJGKDFLFH",
  "updatedAt": "2018-02-01T12:09:24.198466Z"
}

```

Show More
