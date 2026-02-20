# v2/projects/{projectId}/trees/{treeId}/nodes

Source: https://aps.autodesk.com/en/docs/acc/reference/http/locations-nodes-GET/

---

# v2/projects/{projectId}/trees/{treeId}/nodes

Retrieves an array of nodes (locations) from the specified locations tree (LBS). Returns all nodes in the tree by default.

To include each nodeâs path (an array of its ancestor nodesâ names) in the response, use the filter[id] parameter to specify a comma-separated list of nodes to return.

For more information about working with a locations tree, see the Configure a Locations Tree tutorial .

For more details about the Locations API, see Locations API Field Guide .

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/locations/v2/projects/:projectId/trees/:treeId/nodes Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. region string The region where the Locations service you are using is located. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

projectId string: UUID The identifier of the project that contains your locations tree. Use the Data Management API to retrieve the relevant ACC account and project IDs . treeId string Must be default . Currently a project can contain only the default tree.

Use the Data Management API to retrieve the relevant ACC account and project IDs .

### Request

## Query String Parameters

filter[id] array: string Specifies one or more nodes (locations) in the LBS tree to retrieve. Separate multiple node IDs with commas (no space); for example, filter[id]=88e07ccb-4594-4dc5-8973-304412b8fa96,de9aca33-5e0c-4668-85fa-f96273db4b35 . To find node IDs, call this endpoint and check the value of results.id in the returned nodes. Note that when you use this parameter, the server ignores the limit and offset parameters, and each node in the response includes a path array containing its ancestor nodes in the tree. limit int The maximum number of location nodes to return per page. Acceptable values: 1-10000 . Default value: 10000 . offset int The node index at which the pagination starts. This is zero-based; for example, with a value of 6 , the response starts with the seventh node.

To find node IDs, call this endpoint and check the value of results.id in the returned nodes.

Note that when you use this parameter, the server ignores the limit and offset parameters, and each node in the response includes a path array containing its ancestor nodes in the tree.

### Response

## HTTP Status Code Summary

200 OK Succeeded 400 Bad Request Bad request 403 Forbidden Forbidden. The caller has no permission to perform this operation. 404 Not Found The specified project or tree was not found.

### Response

## Body Structure (200)

pagination object limit int The maximum number of LBS nodes returned per page. offset int The node index at which the pagination starts. This is zero-based; for example, with a value of 6 , the response starts with the seventh node. totalResults int The total number of nodes returned. previousUrl string The URL path that returns the previous page of data. nextUrl string The URL path that returns the next page of data. results array: object id string: UUID The unique identifier of the new LBS node. parentId string: UUID The identifier of the parent node of this LBS node. type enum:string The type of this LBS node. Note that only Area is a currently supported request value.
Possible values: Area , Level , Root name string The name of this LBS node. Max length: 255 description string Not relevant barcode string The barcode that represents this LBS node. This value must be unique per project. Max length: 255 order int This nodeâs position relative to its sibling nodes. Nodes with the same parent have a defined sequence order. A node with a lower order value will be positioned before a node with a higher order value. This is zero-based; for example, a node with an order value of 3 is the fourth node among its sibling nodes. If an existing sibling node has the same or higher order value, that value will be incremented to make room for the new node. documentCount int This field is reserved for future use. path array: string The path from the root node to the current node. Note that this is only included if you use the filter[id] parameter.

Max length: 255

Max length: 255

This is zero-based; for example, a node with an order value of 3 is the fourth node among its sibling nodes.

If an existing sibling node has the same or higher order value, that value will be incremented to make room for the new node.

## Example

Succeeded

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/locations/v2/projects/:projectId/trees/:treeId/nodes' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "pagination" : { "limit" : 3 , "offset" : 0 , "totalResults" : 7 , "nextUrl" : "/locations/v2/projects/4a327b27-897c-4e5a-8e48-6e01c21377f3/trees/default/nodes?limit=3&offset=3" }, "results" : [ { "id" : "5add4375-f223-4201-88b9-8049e68416aa" , "parentId" : null , "type" : "Root" , "name" : "Project" , "description" : null , "barcode" : null , "order" : 0 }, { "id" : "d14ce3a6-e61b-4ab0-a9be-5acf7b5366df" , "parentId" : "5add4375-f223-4201-88b9-8049e68416aa" , "type" : "Area" , "name" : "Floor 1" , "description" : null , "barcode" : "ABC123" , "order" : 0 }, { "id" : "8da1faf2-a72f-421b-89df-00d77e545faf" , "parentId" : "5add4375-f223-4201-88b9-8049e68416aa" , "type" : "Area" , "name" : "Floor 2" , "description" : null , "barcode" : "DEF456" , "order" : 1 } ] }
```
