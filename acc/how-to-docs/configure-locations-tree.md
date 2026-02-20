# Configure a Locations Tree

Source: https://aps.autodesk.com/en/docs/acc/tutorials/locations/configure-locations-tree/

---

# Configure a Locations Tree

This tutorial demonstrates how to configure a hierarchy (a tree) of building areas (locations), also known as a location breakdown structure (LBS). Each location is a node in the tree. The steps include retrieving the treeâs root node ID (representing the project); creating two second-tier nodes with the root as their parent; adding a third-tier node under one of the second-tier nodes; renaming a node; and deleting a node.

For more details about this API, see the Locations API Field Guide .

## Before you begin

- Register an app

- Acquire a 3-legged OAuth token with data:read and data:write scope.

- Verify that you have access to the relevant Autodesk Construction Cloud account and project.

- Use the Data Management API to retrieve the relevant ACC account and project IDs . This tutorial uses the example project ID e4ae9874-0ab6-4b33-ac91-ff70e806e013 , but you should replace that with the project ID you have retrieved for your project.

In this tutorial, the LBS is used as follows:

- The top-tier (root) node represents a hotel.

- The second-tier nodes represent floors of the hotel.

- The third-tier nodes represent rooms on each floor.

Note that the nodes in a given tier donât all have to represent the same type of location. For example, a second-tier node could represent the hotelâs roof.

## Step 1: Retrieve the root node ID

Use the GET nodes endpoint to retrieve the root node of your projectâs LBS. This tutorial uses 24d53a28-cda0-43b0-9021-863736edebf8 as an example of the root node ID of the tree.

Note that when the project is new, only the root node is returned, so no pagination is necessary.

### Request

```
curl --request GET 'https://developer.api.autodesk.com/construction/locations/v2/projects/e4ae9874-0ab6-4b33-ac91-ff70e806e013/trees/default/nodes' \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'
```

### Response

```
200 Succeeded

{
    {
        "results": [
            { "id": "24d53a28-cda0-43b0-9021-863736edebf8", "parentId": null,
                "type": "Root",
                "name": "Project",
                "description": null,
                "barcode": null,
                "order": 0
            }
        ]
    }
}
```

The response payload includes the root node ID ( results.id ) value of 24d53a28-cda0-43b0-9021-863736edebf8 .

## Step 2: Create the first and second floor nodes

Use the POST nodes endpoint to create the new nodes in the second tier of the LBS.

Note that the root node is automatically created with the project.

### Step 2.1: Create the second floor node

Create a new node and name it Floor 2 ( not Floor 1 ). Assign Floor 2 âs parent by specifying the root nodeâs ID as the value of parentId . In this way you start to define the tree hierarchy.

### Request

```
curl --request POST 'https://developer.api.autodesk.com/construction/locations/v2/projects/e4ae9874-0ab6-4b33-ac91-ff70e806e013/trees/default/nodes' \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \ -d '{ "parentId": "24d53a28-cda0-43b0-9021-863736edebf8", "type": "Area", "name": "Floor 2", "barcode": "barcodeFloor2" }'
```

### Response

```
201 Created

{
    { "id": "15e5bd3f-8334-4a98-9365-3489b83506f1", "parentId": "24d53a28-cda0-43b0-9021-863736edebf8",
        "type": "Area",
        "name": "Floor 2",
        "description": null,
        "barcode": "barcodeFloor2",
        "order": 0
    }
}
```

Now your LBS should look as follows:

```
Project ( Hotel ) / / Floor 2
```

The response payload includes the Floor 2 ID ( id ) value of 15e5bd3f-8334-4a98-9365-3489b83506f1 .

### Step 2.2: Create the first floor node

Create a new node and name it Floor 1 . Assign Floor 1âs parent by specifying the root nodeâs ID as the value of parentId .

Note that this request contains two query parameters: The targetNodeId value is the id of the Floor 2 node, and the insertOption value is Before , indicating that the Floor 1 node should come before the Floor 2 node in sequence order. For more details, see POST nodes .

### Request

```
curl --request POST 'https://developer.api.autodesk.com/construction/locations/v2/projects/e4ae9874-0ab6-4b33-ac91-ff70e806e013/trees/default/nodes?targetNodeId=15e5bd3f-8334-4a98-9365-3489b83506f1&insertOption=Before' \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \ -d '{ "parentId": "24d53a28-cda0-43b0-9021-863736edebf8", "type": "Area", "name": "Floor 1", "barcode": "barcodeFloor1" }'
```

### Response

```
201 Created

{
    { "id": "94eb2ce9-8b3f-45e8-a178-894c8c49725b", "parentId": "24d53a28-cda0-43b0-9021-863736edebf8",
        "type": "Area",
        "name": "Floor 1",
        "description": null,
        "barcode": "barcodeFloor1", "order": 0 }
}
```

Now your LBS should look as follows:

```
Project ( Hotel ) / \ / \ Floor 1 Floor 2
```

The response payload includes the Floor 1 ID ( id ) value of 94eb2ce9-8b3f-45e8-a178-894c8c49725b , and the order value of 0 , indicating that Floor 1 is before Floor 2 in sequence order (Floor 2âs order is now 1 ).

## Step 3: Create a second floor suite node

Under the Floor 2 node, use the POST nodes endpoint to create a new node and name it Suite 205 . Assign Suite 205 âs parent by specifying the Floor 2 ID as the value of parentId .

### Request

```
curl --request POST 'https://developer.api.autodesk.com/construction/locations/v2/projects/e4ae9874-0ab6-4b33-ac91-ff70e806e013/trees/default/nodes' \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \ -d '{ "parentId": "15e5bd3f-8334-4a98-9365-3489b83506f1", "type": "Area", "name": "Suite 205", "barcode": "barcodeSuite205" }'
```

### Response

```
201 Created

{
    { "id": "76e6814b-4a10-4347-80bd-d9b429453807", "parentId": "15e5bd3f-8334-4a98-9365-3489b83506f1",
        "type": "Area",
        "name": "Suite 205",
        "description": null,
        "barcode": "barcodeSuite205",
        "order": 0
    }
}
```

Your LBS should look as follows:

```
Project ( Hotel ) / \ / \ Floor 1 Floor 2 \
                 \ Suite 205
```

The response payload includes the Suite 205 ID ( id ) value of 76e6814b-4a10-4347-80bd-d9b429453807 .

## Step 4: Update the suite node

Use the PATCH nodes/{nodeId} endpoint to update the nodeâs name , barcode , or both.

Note that you cannot send the request without at least one of these two fields.

Update node Suite 205 âs name to be â Suite 211 â, and its barcode to be â barcodeSuite211 â (passing the nodeâs ID as a URI parameter).

### Request

```
curl --request PATCH 'https://developer.api.autodesk.com/construction/locations/v2/projects/e4ae9874-0ab6-4b33-ac91-ff70e806e013/trees/default/nodes/76e6814b-4a10-4347-80bd-d9b429453807' \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \ -d '{ "name": "Suite 211", "barcode": "barcodeSuite211" }'
```

### Response

```
200 Ok

{
    { "name": "Suite 211", "description": null, "barcode": "barcodeSuite211", "parentId": "15e5bd3f-8334-4a98-9365-3489b83506f1",
        "id": "76e6814b-4a10-4347-80bd-d9b429453807",
        "type": "Area",
        "order": 0
    }
}
```

Your LBS should look as follows:

```
Project ( Hotel ) / \ / \ Floor 1 Floor 2 \
                 \ Suite 211
```

The response payload includes the nodeâs updated name and barcode .

## Step 5: Delete the suite node

Use the DELETE nodes/{nodeId} endpoint to delete the Suite 211 node by passing the nodeâs ID ( 76e6814b-4a10-4347-80bd-d9b429453807 ) as a URI parameter.

### Request

```
curl --request DELETE 'https://developer.api.autodesk.com/construction/locations/v2/projects/e4ae9874-0ab6-4b33-ac91-ff70e806e013/trees/default/nodes/76e6814b-4a10-4347-80bd-d9b429453807' \ -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'
```

### Response

```
204 No Content
```

Finally, your LBS should look as follows:

```
Project ( Hotel ) / \ / \ Floor 1 Floor 2
```

Congratulations! You have created a location breakdown structure and modified it using the Locations API.
