# custom-identifier

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-custom-identifier-GET/

---

Custom-Identifier

GET

# custom-identifier

Returns the current and next available RFI custom identifier for the project.

Use this endpoint to display or pre-fill the next custom RFI number when creating a new RFI. The identifier is automatically incremented and skips numbers that are already in use.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfis/custom-identifier |
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

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Details of the last created and the next available custom identifiers. |
| --- | --- |
| 400   Bad Request | The parameters are invalid |
| 401   Unauthorized | The provided bearer token is not valid |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation |
| 500   Internal Server Error | An unknown error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

| current   string,null | The last custom identifier that was used for an RFI in this project. |
| --- | --- |
| next   string | The next available custom identifier for the project. |

## [Example](#example)

Details of the last created and the next available custom identifiers.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfis/custom-identifier' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "current": "353",
  "next": "354"
}

```
