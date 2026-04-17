# v2/projects/{projectId}/trees/{treeId}/nodes

Source: https://aps.autodesk.com/en/docs/acc/reference/http/locations-nodes-POST/

---

nodes

POST

# v2/projects/{projectId}/trees/{treeId}/nodes

Creates a node in the specified locations tree. Note that creating the root node is not allowed because the root node is created automatically when the project is created.

Nodes in a given tier of the tree have a defined sequence order. By default, new nodes are appended to the end of the sequence. To specify the sequence position of the new node, include `targetNodeId` and `insertOption` in the request.

For more information about working with a locations tree, see the [Configure a Locations Tree tutorial](../how-to-docs/locations-configure-locations-tree.md).

For more details about the Locations API, see [Locations API Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/locations/) .

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/locations/v2/projects/:projectId/trees/:treeId/nodes |
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

### Request

## [Query String Parameters](#query-string-parameters)

| targetNodeId   string: UUID | Unique identifier of a node that will be the new node’s immediate sibling in the locations tree. The target node’s `parentId` must match the `body.parentId` field in the request. <br>Note that nodes in a given tier of the tree have a defined sequence order. The new node will be created in the same tier, either before or after the target node. You specify the sequence position of the new node using the `insertOption` parameter.<br>Note that this parameter is unavailable if this request is creating an existing node’s first child node.<br>Required only when `insertOption` is also included in the request. |
| --- | --- |
| insertOption   enum:string | Where to insert the new node relative to the target node that you specified with `targetNodeId`. The nodes in a given tier of the tree have a defined sequence order, and `insertOption` specifies whether the new node comes before or after the target node. <br>Required only when `targetNodeId` is also included in the request. Possible values: `After`, `Before` |

### Request

## [Body Structure](#body-structure)

| parentId*   string: UUID | The identifier of the parent node of this LBS node. |
| --- | --- |
| type*   enum:string | The type of this LBS node. Note that only `Area` is a currently supported request value. Possible values: `Area`, `Level`, `Root` |
| name*   string | The name of this LBS node. <br>Max length: 255 |
| description   string | Not relevant |
| barcode   string | The barcode that represents this LBS node. This value must be unique per project. <br>Max length: 255 |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Node created |
| --- | --- |
| 400   Bad Request | Bad request |
| 403   Forbidden | Forbidden. The caller has no permission to perform this operation. |
| 404   Not Found | The specified project or tree was not found. |

### Response

## [Body Structure (201)](#body-structure-201)

| id   string: UUID | The unique identifier of the new LBS node. |
| --- | --- |
| parentId   string: UUID | The identifier of the parent node of this LBS node. |
| type   enum:string | The type of this LBS node. Note that only `Area` is a currently supported request value. Possible values: `Area`, `Level`, `Root` |
| name   string | The name of this LBS node. <br>Max length: 255 |
| description   string | Not relevant |
| barcode   string | The barcode that represents this LBS node. This value must be unique per project. <br>Max length: 255 |
| order   int | This node’s position relative to its sibling nodes. Nodes with the same parent have a defined sequence order. A node with a lower `order` value will be positioned before a node with a higher `order` value. <br>This is zero-based; for example, a node with an `order` value of `3` is the fourth node among its sibling nodes.<br>If an existing sibling node has the same or higher `order` value, that value will be incremented to make room for the new node. |
| documentCount   int | This field is reserved for future use. |

## [Example](#example)

Node created

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/locations/v2/projects/:projectId/trees/:treeId/nodes' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "parentId": "88e07ccb-4594-4dc5-8973-304412b8fa96",
        "type": "Area",
        "name": "Suite 205",
        "description": "The Suite 205 node",
        "barcode": "1234567890"
      }'

```

Show More

### Response

```
{
  "id": "de9aca33-5e0c-4668-85fa-f96273db4b35",
  "parentId": "88e07ccb-4594-4dc5-8973-304412b8fa96",
  "type": "Area",
  "name": "Suite 205",
  "description": null,
  "barcode": "ABC123",
  "order": 0
}

```

Show More
