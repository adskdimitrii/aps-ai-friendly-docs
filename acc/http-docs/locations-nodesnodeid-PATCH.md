# v2/projects/{projectId}/trees/{treeId}/nodes/{nodeId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/locations-nodesnodeid-PATCH/

---

# v2/projects/{projectId}/trees/{treeId}/nodes/{nodeId}

Updates the name or barcode of the specified node of the specified locations tree.

Note that at least one of these fields must be included in your request.

For more information about working with a locations tree, see the Configure a Locations Tree tutorial .

For more details about the Locations API, see Locations API Field Guide .

## Resource Information

Method and URI PATCH https://developer.api.autodesk.com/construction/locations/v2/projects/:projectId/trees/:treeId/nodes/:nodeId Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json

### Request

## URI Parameters

projectId string: UUID The identifier of the project that contains your locations tree. Use the Data Management API to retrieve the relevant ACC account and project IDs . treeId string Must be default . Currently a project can contain only the default tree. nodeId string: UUID The unique identifier of an LBS node. To find node IDs, call the GET nodes endpoint and check the value of results.id in the returned nodes.

Use the Data Management API to retrieve the relevant ACC account and project IDs .

To find node IDs, call the GET nodes endpoint and check the value of results.id in the returned nodes.

### Request

## Body Structure

name * string The name of the specified LBS node to update. Note that you must specify name , barcode , or both for this endpoint to succeed. Max length: 255 barcode * string The barcode of the specified LBS node to update. This value must be unique per project. Note that you must specify barcode , name , or both for this endpoint to succeed. Max length: 255

Max length: 255

Max length: 255

### Response

## HTTP Status Code Summary

200 OK Node updated 400 Bad Request Bad request. Note that renaming the root node is not permitted. 403 Forbidden Forbidden. The caller has no permission to perform this operation. 404 Not Found The specified project, tree or node was not found.

### Response

## Body Structure (200)

id string: UUID The unique identifier of the new LBS node. parentId string: UUID The identifier of the parent node of this LBS node. type enum:string The type of this LBS node. Note that only Area is a currently supported request value.
Possible values: Area , Level , Root name string The name of this LBS node. Max length: 255 description string Not relevant barcode string The barcode that represents this LBS node. This value must be unique per project. Max length: 255 order int This nodeâs position relative to its sibling nodes. Nodes with the same parent have a defined sequence order. A node with a lower order value will be positioned before a node with a higher order value. This is zero-based; for example, a node with an order value of 3 is the fourth node among its sibling nodes. If an existing sibling node has the same or higher order value, that value will be incremented to make room for the new node.

Max length: 255

Max length: 255

This is zero-based; for example, a node with an order value of 3 is the fourth node among its sibling nodes.

If an existing sibling node has the same or higher order value, that value will be incremented to make room for the new node.

## Example

Node updated

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/locations/v2/projects/:projectId/trees/:treeId/nodes/:nodeId' \ -X 'PATCH' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "name": "Suite 205", "barcode": "1234567890" }'
```

### Response

```
{ "id" : "802ffa47-6e29-40f5-8e82-65bda03a7f5a" , "parentId" : "88e07ccb-4594-4dc5-8973-304412b8fa96" , "type" : "Area" , "name" : "Suite 205" , "description" : "The Suite 205 node" , "barcode" : "1234567890" , "order" : 0 }
```
