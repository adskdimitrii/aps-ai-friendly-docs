# projects/{projectId}/items:next-custom-identifier

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-itemsnext-custom-identifier-GET/

---

Items

GET

# projects/{projectId}/items:next-custom-identifier

Retrieves the next available custom identifier for a submittal item in a project. The identifier is generated based on specific rules:

- Sequentially increments the last created item’s number, relative to either the whole project for a global sequence or the specific spec for a spec sequence.
- Skips numbers already in use.
- Reuses deleted or cleared numbers.
- Increments digits appropriately, and manages leading zeros without increasing character count unless necessary.

For information about custom numbering in Submittals, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Custom_Numbering).

For details on using custom identifiers in the Submittal workflow, see the [Create Submittal Item](../how-to-docs/submittals-create-submittal-item.md) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/items:next-custom-identifier |
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

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| specId   string: UUID | The item spec ID. This parameter is only required when the project is in spec sequence type (as opposed to global sequence). <br>To verify the sequence type, call [GET metadata](http-submittals-metadata-GET.md), and check `customIdentifierSequenceType`.<br>To get the spec ID, call [GET specs](http-submittals-specs-GET.md), and select the relevant ID (`id`). |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Details of the last created and the next available custom identifiers. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. |
| 401   Unauthorized | Invalid or missing authorization header. Verify the Bearer token and try again. |
| 403   Forbidden | The user is not authorized to perform this action. |
| 404   Not Found | The specified resource was not found. |
| 500   Internal Server Error | An unexpected error occurred on the server while processing the request. |

### Response

## [Body Structure (200)](#body-structure-200)

| previousCustomIdentifier   string | The last created custom identifier. |
| --- | --- |
| nextCustomIdentifier   string | The next available custom identifier for the project. |

## [Example](#example)

Details of the last created and the next available custom identifiers.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/items:next-custom-identifier' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "previousCustomIdentifier": "0001",
  "nextCustomIdentifier": "0002"
}

```
