# v2/projects/{projectId}/trees/{treeId}/nodes/{nodeId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/locations-nodesnodeid-DELETE/

---

nodes/:nodeId

DELETE

# v2/projects/{projectId}/trees/{treeId}/nodes/{nodeId}

Deletes the specified node from the specified locations tree.

Important: If this node has any descendant nodes, they will also be deleted, and the objects linked to those locations will be unlinked.

Note that deleting the root node is not allowed.

For more information about working with a locations tree, see the [Configure a Locations Tree tutorial](../how-to-docs/locations-configure-locations-tree.md).

For more details about the Locations API, see [Locations API Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/locations/) .

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/construction/locations/v2/projects/:projectId/trees/:treeId/nodes/:nodeId |
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

| projectId   string: UUID | The identifier of the project that contains your locations tree. <br>Use the Data Management API to [retrieve the relevant Forma hub and project IDs](../how-to-docs/getting-started-retrieve-account-and-project-id.md). |
| --- | --- |
| treeId   string | Must be `default`. Currently a project can contain only the default tree. |
| nodeId   string: UUID | The unique identifier of an LBS node. <br>To find node IDs, call the [GET nodes](http-locations-nodes-GET.md) endpoint and check the value of `results.id` in the returned nodes. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | Node deleted |
| --- | --- |
| 400   Bad Request | Bad request |
| 403   Forbidden | Forbidden. The caller has no permission to perform this operation. |
| 404   Not Found | The specified project, tree or node was not found. |

### Response

## [Body Structure (204)](#body-structure-204)

Response for 204 has no body.

## [Example](#example)

Node deleted

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/locations/v2/projects/:projectId/trees/:treeId/nodes/:nodeId' \
  -X 'DELETE' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
204 No Content

```
