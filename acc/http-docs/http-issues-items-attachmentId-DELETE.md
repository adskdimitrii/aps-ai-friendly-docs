# projects/{projectId}/attachments/{issueId}/items/{attachmentId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/issues-items-attachmentId-DELETE/

---

Issue Attachments

DELETE

# projects/{projectId}/attachments/{issueId}/items/{attachmentId}

Deletes a specific attachment from an issue in a project.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/construction/issues/v1/projects/{projectId}/attachments/{issueId}/items/{attachmentId} |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |
| issueId   string: UUID | The unique identifier of the issue. To find the ID, call [GET issues](http-issues-issues-GET.md). |
| attachmentId   string: UUID | The unique identifier of the attachment. To find the ID, call [GET attachments](http-issues-attachments-issueId-items-GET.md). |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | OK |
| --- | --- |
| 400   Bad Request | Invalid input |
| 403   Forbidden | The request is valid but lacks the necessary permissions. |
| 404   Not Found | Issue or attachment not found, or attachment has already been deleted |
| 500   Internal Server Error | Internal server error |

### Response

## [Body Structure (204)](#body-structure-204)

Response for 204 has no body.

## [Example](#example)

OK

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/:projectId/attachments/:issueId/items/:attachmentId' \
  -X 'DELETE' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
204 No Content

```
