# projects/{projectId}/items:validate-custom-identifier

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-itemsvalidate-custom-identifier-POST/

---

Items

POST

# projects/{projectId}/items:validate-custom-identifier

Validates a custom identifier for a submittal item in a project. It ensures the identifier is not currently in use and adheres to the required formatting rules. Use this endpoint to validate a custom identifier you intend to use.

For information about custom numbering in Submittals, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Custom_Numbering).

For details on validating custom identifiers in the Submittal workflow, see the [Create Submittal Item](../how-to-docs/submittals-create-submittal-item.md) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/items:validate-custom-identifier |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| specId   string: UUID | The item spec ID. This parameter is only required when the project is in spec sequence type (as opposed to global sequence). <br>To verify the sequence type, call [GET metadata](http-submittals-metadata-GET.md), and check `customIdentifierSequenceType`.<br>To get the spec ID call [GET specs](http-submittals-specs-GET.md), and select the relevant ID (`id`). |
| --- | --- |

### Request

## [Body Structure](#body-structure)

| customIdentifier*   string | The `customIdentifier` is used to ensure that the chosen identifier adheres to format rules and is unique within the project. Submittal managers can assign custom numbers manually or automatically. <br>When validating a custom identifier, consider the following rules:<br>Ensure the identifier is unique within the project.For global sequences, ensure it is unique within the entire project.For spec sequences, ensure it is unique within the specific spec section.Spec sequence is in the format `<spec_identifier>-<sequential_number>`. You only need to specify the sequential number. The full number - `<spec_identifier>-<sequential_number>` - appears in the response payload in the `customIdentifierHumanReadable` attribute.  > Regardless of whether the project uses a global or spec sequence, you should always provide only the sequential number portion without the spec ID when sending the `customIdentifier`.<br>For more information on custom numbering, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Custom_Numbering). |
| --- | --- |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | Validating a Custom Identifier. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. |
| 401   Unauthorized | Invalid or missing authorization header. Verify the Bearer token and try again. |
| 403   Forbidden | The user is not authorized to perform this action. |
| 404   Not Found | The specified resource was not found. |
| 409   Conflict | The custom identifier is already taken |
| 500   Internal Server Error | An unexpected error occurred on the server while processing the request. |

### Response

## [Body Structure (204)](#body-structure-204)

Response for 204 has no body.

## [Example](#example)

Validating a Custom Identifier.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/items:validate-custom-identifier' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "customIdentifier": "01"
      }'

```

### Response

```
204 No Content

```
