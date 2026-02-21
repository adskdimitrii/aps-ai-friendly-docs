# Create a Potential Change Order (PCO)

Source: https://aps.autodesk.com/en/docs/acc/tutorials/cost/create-pco/

---

# Create a Potential Change Order (PCO)

Creating a potential change order (PCO) is the beginning of the change process in BIM 360 cost management. This tutorial demonstrates how to create a PCO for a project.

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps)
- Acquire a [3-legged OAuth token](/en/docs/oauth/v2/tutorials/get-3-legged-token/) with the `data:write` scope.
- Verify that you have access to the relevant BIM 360 account and BIM 360 project.
- Retrieve the project ID for your project. To obtain a project ID, use [GET projects](/en/docs/bim360/v1/reference/http/admin-accounts-accountidprojects-GET/).

## [Step 1: Create a PCO](#step-1-create-a-pco)

Use the container ID you retrieved in the first tutorial (`be00f32e-c03c-4c7b-9ec4-d2614bf1980c` in this example) to call [POST change-orders/pco](/en/docs/bim360-private/v1/reference/http/cost-change-orders-changeOrder-POST/).

### Request

```
curl "https://developer.api.autodesk.com/cost/v1/containers/be00f32e-c03c-4c7b-9ec4-d2614bf1980c/change-orders/pco" -d '{
  "name":"Revised Main Entrance Layout per ASI 002",
  "description": "Revised Main Entrance Layout per ASI 002",
  "scope":"out",
  "type":"Owner Change Order",
  "sourceType":"ASI",
  "sourceRef": "ASI 002"
}' -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer XZvCJNhdxESsBRIH28MfLf2hKL5O"

```

Show More

### Response

```
{
  "id": "f5c7869f-faa1-4418-b8e6-e7c23c495560",
  "number": "(0001)",
  "name": "Revised Main Entrance Layout per ASI002",
  "scope": "out",
  "description": "Revised Main Entrance Layout per ASI 002",
  "estimated": 0,
  "proposed": 0,
  "submitted": 0,
  "approved": 0,
  "committed": 0,
  "properties": [{
    "name": "Source Type",
    "value": "ASI",
  }, {
    "name": "Source Ref",
    "value": "ASI 002",
  }, {
    "name": "Type",
    "value": "Owner Change Order",
  }]
}

```

Show More

This example returns the PCO ID `f5c7869f-faa1-4418-b8e6-e7c23c495560`. You can use a PCO ID later to get the latest status of the PCO. For example, for this ID you would call [GET change-orders/pco/f5c7869f-faa1-4418-b8e6-e7c23c495560](/en/docs/bim360-private/v1/reference/http/cost-change-orders-changeOrder-id-GET/).

## [Step 2: Create a Cost Item](#step-2-create-a-cost-item)

You can create cost items to break down change if necessary. Use the container ID you used before (`be00f32e-c03c-4c7b-9ec4-d2614bf1980c`) and the PCO ID you just retrieved (`f5c7869f-faa1-4418-b8e6-e7c23c495560`) to call [POST cost-items](/en/docs/bim360-private/v1/reference/http/cost-cost-items-POST/).

### Request

```
curl "https://developer.api.autodesk.com/cost/v1/containers/be00f32e-c03c-4c7b-9ec4-d2614bf1980c/cost-items" -d '{
  "name":"Revised Main Entrance Layout per ASI 002 - Labor",
  "description": "Labor",
  "changeOrderId": "f5c7869f-faa1-4418-b8e6-e7c23c495560"
}' -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer XZvCJNhdxESsBRIH28MfLf2hKL5O"

```

### Response

```
{
  "id": "f5c7869f-faa1-4418-b8e6-e7c23c495560",
  "number": "0001",
  "name": "Revised Main Entrance Layout per ASI 002 - Labor",
  "scope": "out",
  "description": "Labor",
  "estimated": 0,
  "proposed": 0,
  "submitted": 0,
  "approved": 0,
  "committed": 0,
}

```

Show More

To create more cost items for this PCO, repeat step 2.

Congratulations! You have created a PCO with a cost item in BIM 360 cost management. A cost engineer can use this to start the change process in cost management. It allows you to estimate, quote and review the changes. Later you can call [GET change-orders/pco/f5c7869f-faa1-4418-b8e6-e7c23c495560](/en/docs/bim360-private/v1/reference/http/cost-change-orders-changeOrder-id-GET/) to get the latest status and cost(`estimated`, `proposed`, `submitted`, `approved`, `committed`) of this change.
