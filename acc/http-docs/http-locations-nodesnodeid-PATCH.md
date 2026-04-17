# v2/projects/{projectId}/trees/{treeId}/nodes/{nodeId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/locations-nodesnodeid-PATCH/

---

nodes/:nodeId

PATCH

# v2/projects/{projectId}/trees/{treeId}/nodes/{nodeId}

Updates the `name` or `barcode` of the specified node of the specified locations tree.

Note that at least one of these fields must be included in your request.

For more information about working with a locations tree, see the [Configure a Locations Tree tutorial](../how-to-docs/locations-configure-locations-tree.md).

For more details about the Locations API, see [Locations API Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/locations/) .

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/construction/locations/v2/projects/:projectId/trees/:treeId/nodes/:nodeId |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The identifier of the project that contains your locations tree. <br>Use the Data Management API to [retrieve the relevant Forma hub and project IDs](../how-to-docs/getting-started-retrieve-account-and-project-id.md). |
| --- | --- |
| treeId   string | Must be `default`. Currently a project can contain only the default tree. |
| nodeId   string: UUID | The unique identifier of an LBS node. <br>To find node IDs, call the [GET nodes](http-locations-nodes-GET.md) endpoint and check the value of `results.id` in the returned nodes. |

### Request

## [Body Structure](#body-structure)

| name*   string | The name of the specified LBS node to update. Note that you must specify `name`, `barcode`, or both for this endpoint to succeed. <br>Max length: 255 |
| --- | --- |
| barcode*   string | The barcode of the specified LBS node to update. This value must be unique per project. Note that you must specify `barcode`, `name`, or both for this endpoint to succeed. <br>Max length: 255 |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Node updated |
| --- | --- |
| 400   Bad Request | Bad request. Note that renaming the root node is not permitted. |
| 403   Forbidden | Forbidden. The caller has no permission to perform this operation. |
| 404   Not Found | The specified project, tree or node was not found. |

### Response

## [Body Structure (200)](#body-structure-200)

| id   string: UUID | The unique identifier of the new LBS node. |
| --- | --- |
| parentId   string: UUID | The identifier of the parent node of this LBS node. |
| type   enum:string | The type of this LBS node. Note that only `Area` is a currently supported request value. Possible values: `Area`, `Level`, `Root` |
| name   string | The name of this LBS node. <br>Max length: 255 |
| description   string | Not relevant |
| barcode   string | The barcode that represents this LBS node. This value must be unique per project. <br>Max length: 255 |
| order   int | This node’s position relative to its sibling nodes. Nodes with the same parent have a defined sequence order. A node with a lower `order` value will be positioned before a node with a higher `order` value. <br>This is zero-based; for example, a node with an `order` value of `3` is the fourth node among its sibling nodes.<br>If an existing sibling node has the same or higher `order` value, that value will be incremented to make room for the new node. |

## [Example](#example)

Node updated

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/locations/v2/projects/:projectId/trees/:treeId/nodes/:nodeId' \
  -X 'PATCH' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "Suite 205",
        "barcode": "1234567890"
      }'

```

Show More

### Response

```
{
  "id": "802ffa47-6e29-40f5-8e82-65bda03a7f5a",
  "parentId": "88e07ccb-4594-4dc5-8973-304412b8fa96",
  "type": "Area",
  "name": "Suite 205",
  "description": "The Suite 205 node",
  "barcode": "1234567890",
  "order": 0
}

```

Show More
