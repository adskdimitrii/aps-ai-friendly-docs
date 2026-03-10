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

| projectId   string | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
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
| 429   Too Many Requests | The request could not be completed due to a conflict with the current state of the target resource |
| 500   Internal Server Error | The request could not be completed due to a conflict with the current state of the target resource |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| data   array: object | List of form templates in the project. |
| --- | --- |
| projectId   string | Unique indentifier of the project the template belongs to. |
| id   string | The unique identifier of the template. |
| name   string | Display name of template. |
| status   string | Status of template: `"active"`, `"inactive"` (archived), or `"deleted"` |
| templateType   string | User supplied type of template |
| userPermissions   array | Permissions on this template assigned to individual users. |
| groupPermissions   array | Permissions on this template assigned to companies and roles. |
| createdBy   string | The unique identifier of the user who created the template. |
| updatedAt   datetime: ISO 8601 | When the template was last updated, UTC date and time in ISO-8601 format. |
| isPdf   boolean | A flag that indicates whether the template has a PDF or not. |
| pdfUrl   string | For PDF forms, the URL to download the form’s PDF. |
| forms   object | Reference to fetch forms created from this template. |
| url   string | URL to retrieve resources. |
| pagination   object | Request pagination information. |
| offset   int | Number of items skipped. |
| limit   int | Number of items returned. |
| totalResults   int | Total number of items that can be returned. |
| nextUrl   string | URL for the next page of items. Next page url is null on the last page. |
