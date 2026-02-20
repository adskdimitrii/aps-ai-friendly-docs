# v2/projects/{projectId}/trees/{treeId}/nodes/{nodeId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/locations-nodesnodeid-DELETE/

---

# v2/projects/{projectId}/trees/{treeId}/nodes/{nodeId}

Deletes the specified node from the specified locations tree.

Important: If this node has any descendant nodes, they will also be deleted, and the objects linked to those locations will be unlinked.

Note that deleting the root node is not allowed.

For more information about working with a locations tree, see the Configure a Locations Tree tutorial .

For more details about the Locations API, see Locations API Field Guide .

## Resource Information

Method and URI DELETE https://developer.api.autodesk.com/construction/locations/v2/projects/:projectId/trees/:treeId/nodes/:nodeId Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

projectId string: UUID The identifier of the project that contains your locations tree. Use the Data Management API to retrieve the relevant ACC account and project IDs . treeId string Must be default . Currently a project can contain only the default tree. nodeId string: UUID The unique identifier of an LBS node. To find node IDs, call the GET nodes endpoint and check the value of results.id in the returned nodes.

Use the Data Management API to retrieve the relevant ACC account and project IDs .

To find node IDs, call the GET nodes endpoint and check the value of results.id in the returned nodes.

### Response

## HTTP Status Code Summary

204 No Content Node deleted 400 Bad Request Bad request 403 Forbidden Forbidden. The caller has no permission to perform this operation. 404 Not Found The specified project, tree or node was not found.

### Response

## Body Structure (204)

Response for 204 has no body.

## Example

Node deleted

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/locations/v2/projects/:projectId/trees/:treeId/nodes/:nodeId' \ -X 'DELETE' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
204 No Content
```
