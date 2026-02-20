# Set Up a Budget Code Template

Source: https://aps.autodesk.com/en/docs/acc/tutorials/cost/cost-setup-budget-code-template/

---

# Set Up a Budget Code Template

This tutorial demonstrates how to create a budget code template.
A budget code template is the schema for a budget code used in a BIM 360 Cost Management project. Only one template is allowed in a project. A budget code template is created when your project is initialized. One template has multiple segments. Each segment has a list of values as available codes. One code from each segment comprises a valid budget code that can be used by a budget item.

## Before You Begin

- Register an app

- Acquire a 3-legged OAuth token with data:read and data:write scopes.

- Verify that you have access to the relevant BIM 360 account and BIM 360 project.

- Retrieve the project ID for your project. To obtain a project ID, use GET projects .

## Step 1: Get the ID of the Budget Code Template in BIM 360 Cost Management

To retrieve the ID of the budget code template you want to update, call GET Template . In this example, assume that the project container ID is 18ece8b1-204d-11e8-ad71-d73b169f902a .

### Request

```
curl 'https://developer.api.autodesk.com/cost/v1/containers/18ece8b1-204d-11e8-ad71-d73b169f902a/templates' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0'
```

### Response

```
{ [{ "id" : "55254a50-44d9-11e9-99d7-79aa05d3109e" , "name" : "Default Template" , "..." : "..." , }] }
```

Note the template ID in the first element in the array of the response ( response[0].id ) - 55254a50-44d9-11e9-99d7-79aa05d3109e .

## Step 2: Create a Segment for the Template

Use the template ID to call POST Segments to create a segment.

### Request

```
curl -X POST 'https://developer.api.autodesk.com/cost/v1/containers/18ece8b1-204d-11e8-ad71-d73b169f902a/templates/55254a50-44d9-11e9-99d7-79aa05d3109e/segments' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0' \ -d '{"name": "Job Number", "type": "code", "delimiter": "none", "length": 5, "position": 0}'
```

### Response

```
{ "id" : "9bd1ed70-783b-11e8-acb8-8b72f6541e12" , "name" : "Job Number" , "type" : "code" , "delimiter" : "none" , "length" : 5 , "position" : 0 , "sampleCode" : "#####" , "createdAt" : "2020-01-06T01:24:22.678Z" , "updatedAt" : "2020-01-06T01:24:22.678Z" }
```

Note the segment ID in the response ( id ) - 9bd1ed70-783b-11e8-acb8-8b72f6541e12 .

Repeat this step to create more segments, as needed.

## Step 3: Create a Code for the Segment

Use the container ID ( 18ece8b1-204d-11e8-ad71-d73b169f902a ), template ID ( 55254a50-44d9-11e9-99d7-79aa05d3109e ), and segment ID ( 9bd1ed70-783b-11e8-acb8-8b72f6541e12 ) to call POST values to create a code.

### Request

```
curl 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/segments/55254a50-44d9-11e9-99d7-79aa05d3109e/values' -X 'POST' -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' -H 'Content-Type: application/json' \ -d '{"segmentId": "55254a50-44d9-11e9-99d7-79aa05d3109e", "code": "84720", "description": "Future City"}'
```

### Response

This endpoint returns the full content of the newly created segment.

```
{ "id" : "2236aea0-783c-11e8-926b-e3dd8c091ed4" , "segmentId" : "55254a50-44d9-11e9-99d7-79aa05d3109e" , "parentId" : null , "code" : "84720" , "description" : "Future City" , "createdAt" : "2019-01-06T01:24:22.678Z" , "updatedAt" : "2019-01-06T01:24:22.678Z" }
```

Repeat the previous step to add more codes into segments. You can also use POST values:import to create segment codes in a batch.

Congratulations! You set up a budget code template. You can now create budget items with codes that follow the definition in your budget code template.
