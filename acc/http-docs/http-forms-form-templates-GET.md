# v1/projects/{projectId}/form-templates

Source: https://aps.autodesk.com/en/docs/acc/reference/http/forms-form-templates-GET/

---

Templates

GET

# v1/projects/{projectId}/form-templates

Returns all project’s form templates the user has access to.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/form-templates |
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

### Request

## [Query String Parameters](#query-string-parameters)

| offset   int | The number of records to skip before returning the result records. Defaults to 0. Increase this value in subsequent requests to continue getting results when the number of records exceeds the requested limit. |
| --- | --- |
| limit   int | The number of records to return in a single request. Can be a number between 1 and 50. Defaults to 50. |
| updatedAfter   datetime: ISO 8601 | Return Templates updated after specified time. |
| updatedBefore   datetime: ISO 8601 | Return Templates updated before specified time. |
| sortOrder   enum:string | Return Templates in specified sorted order. Possible values: `desc`, `asc` |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Form Templates. |
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

| data   array: object | List of form templates in the project. |
| --- | --- |
| projectId   string | Unique indentifier of the project the template belongs to. |
| id   string | The unique identifier of the template. |
| name   string | Display name of template. |
| status   enum:string | Status of template: `"active"`, `"inactive"` (archived), or `"deleted"` Possible values: `active`, `inactive`, `deleted` |
| templateType   string | User supplied type of template. Can be a custom string or one of the standard template types: pg.template_type.daily_report, pg.template_type.quality, pg.template_type.safety, pg.template_type.punchlist, pg.template_type.commissioning, pg.template_type.time_sheet, pg.template_type.other |
| userPermissions   array | Permissions on this template assigned to individual users. |
| groupPermissions   array | Permissions on this template assigned to companies and roles. |
| createdBy   string | The unique identifier of the user who created the template. |
| updatedAt   datetime: ISO 8601 | The date when the template was last updated, UTC date and time in ISO-8601 format. |
| isPdf   boolean | A flag that indicates whether the template has a PDF or not. |
| pdfUrl   string | For PDF forms, the URL to download the form’s PDF. |
| forms   object | Reference to fetch forms created from this template. |
| url   string | URL to retrieve resources. |
| currentLayoutId   string: UUID | The unique identifier of the form template’s current layout, if it is not a PDF template. This can be used to retrieve detailed layout information via the GET layouts endpoint. |
| pagination   object | Request pagination information. |
| offset   int | Number of items skipped. |
| limit   int | Number of items returned per page. |
| totalResults   int | Total number of items that can be returned. |
| nextUrl   string | URL for the next page of items. Next page url is null on the last page. |

## [Example](#example)

Form Templates.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/form-templates' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "data": [
    {
      "projectId": "9ba6681e-1952-4d54-aac4-9de6d9858dd4",
      "id": "2f634a22-779d-4930-9f08-8391a41fea05",
      "name": "Daily Report",
      "status": "active",
      "templateType": "pg.template_type.daily_report",
      "userPermissions": [
        {
          "permissions": [
            "submit"
          ],
          "userId": "USER123A"
        }
      ],
      "groupPermissions": [
        {
          "permissions": [
            "manage"
          ],
          "roleKey": "hq_access_level:admin",
          "roleName": "Admin"
        }
      ],
      "createdBy": "USER123A",
      "updatedAt": "2020-11-20T16:13:33.615127+00:00",
      "isPdf": true,
      "pdfUrl": "https://link.to/form.pdf",
      "forms": {
        "url": "https://developer.api.autodesk.com/construction/forms/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/forms?templateId=2f634a22-779d-4930-9f08-8391a41fea05"
      },
      "currentLayoutId": "123e4567-e89b-12d3-a456-426614174000"
    }
  ],
  "pagination": {
    "offset": 0,
    "limit": 50,
    "totalResults": 1,
    "nextUrl": null
  }
}

```

Show More
