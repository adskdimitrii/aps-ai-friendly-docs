# Directly Attach Local Files to a Cost Item (new)

Source: https://aps.autodesk.com/en/docs/acc/tutorials/cost/attach-cost-file-s3/

---

# Directly Attach Local Files to a Cost Item (new)

This tutorial demonstrates how to attach local files directly to a cost item in BIM 360 Cost Management.

Note that the attachment folder is a hidden folder that doesnât appear in the BIM 360 Document Management UI. If you directly attach a local file, it doesnât get associated with other BIM 360 features such as BIM 360 Document Management; it remains as an attachment only for the cost item.

The steps here include finding the folder for the cost item, creating an empty storage object in the folder, uploading the file to the storage object, creating a version of the file, and attaching the file version to the cost item.

For more details about this API, see the Cost Management API Field Guide .

## Before you begin

- Register an app

- Acquire a 3-legged OAuth token with data:create , data:read , and data:write scopes.

- Verify that you have access to the relevant BIM 360 account and BIM 360 project.

- Retrieve the project ID for your project. To obtain a project ID, use GET projects .

## Step 1: Find a cost item in BIM 360 Cost Management

Use the GET cost-items endpoint to find the ID of the cost item to which you want to attach the file. This example uses the container ID value 18ece8b1-204d-11e8-ad71-d73b169f902a .

### Request

```
curl -X GET 'https://developer.api.autodesk.com/cost/v1/containers/18ece8b1-204d-11e8-ad71-d73b169f902a/cost-items?limit=100&offset=0' \ -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0'
```

### Response

```
{ "results" : [{ "id" : "328f3a40-3167-11e8-a044-01a43a3d152c" , "..." : "..." }], "pagination" : { "totalResults" : 7 , "limit" : 100 , "offset" : 0 } }
```

The response payload includes the cost item ID ( results[0].id ) value of 328f3a40-3167-11e8-a044-01a43a3d152c . Youâll use it in the next step.

## Step 2: Find the attachment folder of the cost item

Use the POST attachment-folders endpoint to retrieve the cost itemâs attachment folder. Provide an associationType value of CostItem , and an associationId value of the cost item ID that you retrieved in the previous step ( 328f3a40-3167-11e8-a044-01a43a3d152c ).

### Request

```
curl -X POST 'https://developer.api.autodesk.com/cost/v1/containers/18ece8b1-204d-11e8-ad71-d73b169f902a/attachment-folders' \ -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0' \ -H 'Content-Type: application/json' \ -d '{ "associationType": "CostItem", "associationId": "328f3a40-3167-11e8-a044-01a43a3d152c" }'
```

### Response

```
{ "id" : "80b446f0-4261-11e9-9f1f-e19f7c813519" , "urn" : "urn:adsk.wipprod:fs.folder:co.p0G_54wNRUuAfQQc4DCPEA" , "..." : "..." }
```

The urn value in the response ( urn:adsk.wipprod:fs.folder:co.p0G_54wNRUuAfQQc4DCPEA ) is the folder URN youâll use to access the storage service in the next step. Youâll use the returned attachment folder ID ( 80b446f0-4261-11e9-9f1f-e19f7c813519 ) to create attachments in the last step to attach the file to the cost item.

Note: Instead of using this folder, you can use an existing folder retrieved from BIM 360 Docs. Follow the tutorial Upload Files to BIM 360 Document Management to upload a file to BIM 360 Docs directly, then jump to step 6 to add the file as an attachment to the cost item.

Note that the following steps 3 to 5 are the same as the generic uploading process if youâre already familiar with the Data Management API.

## Step 3: Create a storage object in the attachment folder

Use the Data Management APIâs POST projects/:project_id/storage endpoint to create an empty storage object for the file in the folder.

Provide a project ID value b.6b975448-835b-4625-ad1a-0e9961749de3 (the prefix b. denotes this as a BIM 360 project). The attachment folder URN  is urn:adsk.wipprod:fs.folder:co.p0G_54wNRUuAfQQc4DCPEA .

### Request

```
curl -X POST "https://developer.api.autodesk.com/data/v1/projects/b.6b975448-835b-4625-ad1a-0e9961749de3/storage" \ -H "Content-Type: application/vnd.api+json" \ -H "Accept: application/vnd.api+json" \ -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0" \ -d '{ "jsonapi": { "version": "1.0" }, "data": { "type": "objects", "attributes": { "name": "My First File.jpg" }, "relationships": { "target": { "data": { "type": "folders", "id": "urn:adsk.wipprod:fs.folder:co.p0G_54wNRUuAfQQc4DCPEA" } } } } }'
```

### Response

```
{ "jsonapi" : { "version" : "1.0" }, "data" : { "type" : "objects" , "id" : "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg" , "relationships" : { "target" : { "data" : { "type" : "folders" , "id" : "urn:adsk.wipprod:fs.folder:co.p0G_54wNRUuAfQQc4DCPEA" }, } } } }
```

The response contains the empty storage objectâs ID ( data.id ) value of urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg . The object ID parses into three sections:

- urn:adsk.objects:os.object

- wip.dm.prod (the bucket key)

- 2a6d61f2-49df-4d7b.jpg (the object name)

## Step 4: Generate a signed S3 URL

Use the Data Management APIâs GET buckets/:bucketKey/objects/:objectKey/signeds3upload endpoint to generate a signed URL for the storage object. Include the bucket key ( wip.dm.prod ) and the object name ( 2a6d61f2-49df-4d7b.jpg ) that you retrieved in the previous step. This endpoint supports generating multiple signed URLs, which enables you to upload multiple chunks of the same file in parallel.

### Request

```
curl -X GET "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/2a6d61f2-49df-4d7b.jpg/signeds3upload" \ -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT"
```

### Response

```
{ "uploadKey" : "AQICAHifrJ6-BSHUmjAat4..........QWI-fuvghN23akgePMdmykV" , "uploadExpiration" : "2022-02-05T00:00:00Z" , "urlExpiration" : "2022-02-03T05:23:29Z" , "urls" : [ "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/26668812-6bb1-4f80-bab2-09776f24fd98?uploadId=[UPLOAD_ID]&partNumber=1&X-Amz-Security-Token=[AMZ_TOKEN]%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220203T052230Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=[AMZ_CREDENTIAL]%2F20220203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=[AMZ_SIGNATURE]" ] }
```

Note the urls and uploadKey response attributes, which youâll use in the following steps.

## Step 5: Initiate upload of a file to the signed URL

To upload the file to the signed URL, use a PUT method and the previously returned urls attribute as the URI.

Note that a bearer token is not required.

### Request

```
curl -X PUT --data-binary @D: \M y First File.jpg "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/26668812-6bb1-4f80-bab2-09776f24fd98?uploadId=[UPLOAD_ID]&partNumber=1&X-Amz-Security-Token=[AMZ_TOKEN]%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220203T052230Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=[AMZ_CREDENTIAL]%2F20220203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=[AMZ_SIGNATURE]"
```

A successful call ( 200 ) returns an empty response.

## Step 6: Complete the upload

Use the Data Management APIâs POST buckets/:bucket_key/objects/:object_key/signeds3upload endpoint to complete the upload. Include the bucket key ( wip.dm.prod ), the object name ( 2a6d61f2-49df-4d7b.jpg` ), and the upload key ( AQICAHifrJ6-BSHUmjAat4..........QWI-fuvghN23akgePMdmykV ) returned by the previous two steps.

Note that this endpoint must be called within 24 hours from the time you began uploading the file.

### Request

```
curl -X POST "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg/signeds3upload" \ -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \ --data-raw '{ "uploadKey":"AQICAHifrJ6-BSHUmjAat4..........QWI-fuvghN23akgePMdmykV" }'
```

### Response

```
{ "bucketKey" : "wip.dm.prod" , "objectId" : "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg" , "objectKey" : "2ac28abc-9f6e-463d-bcc4-5c194d552beb.jpg" , "size" : 879394 , "contentType" : "application/octet-stream" , "location" : "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg" }
```

The file has been uploaded to the storage object.

## Step 7: Create a version of the uploaded file

Before attaching the file to the cost item, use the Data Management APIâs POST projects/:project_id/items endpoint to create the first version of the file. Include the project ID ( b.6b975448-835b-4625-ad1a-0e9961749de3 ), the folder URN ( urn:adsk.wipprod:fs.folder:co.p0G_54wNRUuAfQQc4DCPEA ), and the Object ID ( urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg ) in the request.

### Request

```
curl -X POST "https://developer.api.autodesk.com/data/v1/projects/b.6b975448-835b-4625-ad1a-0e9961749de3/items" \ -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \ -H "Content-Type: application/vnd.api+json" \ -H "Accept: application/vnd.api+json" \ -d '{ "jsonapi": { "version": "1.0" }, "data": { "type": "items", "attributes": { "displayName": "My First File.jpg", "extension": { "type": "items:autodesk.bim360:File", "version": "1.0" } }, "relationships": { "tip": { "data": { "type": "versions", "id": "1" } }, "parent": { "data": { "type": "folders", "id": "urn:adsk.wipprod:fs.folder:co.p0G_54wNRUuAfQQc4DCPEA" } } } }, "included": [ { "type": "versions", "id": "1", "attributes": { "name": "My First File.jpg", "extension": { "type": "versions:autodesk.bim360:File", "version": "1.0" } }, "relationships": { "storage": { "data": { "type": "objects", "id": "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg" } } } } ] }'
```

### Response

The file is now ready to be attached to the cost item. Note the versioned file included.id value of urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ?version=1 . Youâll use it in the next step.

## Step 8: Attach the file to the Cost item

Use the POST cost/v1/containers/{containerId}/attachments endpoint to attach the file. Include the
container ID ( 18ece8b1-204d-11e8-ad71-d73b169f902a ), the cost item ID ( 328f3a40-3167-11e8-a044-01a43a3d152c ), and the versioned file ID ( urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ?version=1 ) in the request.

Note that folderId is not required if youâre saving the attachment into an existing folder in BIM 360 Docs. In this example, the folderId is from the Step 2 above.

### Request

```
curl -X POST 'https://developer.api.autodesk.com/cost/v1/containers/18ece8b1-204d-11e8-ad71-d73b169f902a/attachments' \ -H 'Accept: application/json' \ -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0' \ -H 'Content-Type: application/json' \ -d '{ "urn":"urn:adsk.wipprod:fs.file:vf.ywE-g1asTFO2LVyI9TiiwA?version=1", "folderId":"80b446f0-4261-11e9-9f1f-e19f7c813519", "name":"My First File.png", "associationType":"CostItem", "associationId":"328f3a40-3167-11e8-a044-01a43a3d152c", "type":"Upload" }'
```

### Response

```
{ "id" : "891F5C5A-4356-482E-AC9C-585ED7DE1611" , "urn" : "urn:adsk.wipprod:fs.file:vf.ywE-g1asTFO2LVyI9TiiwA?version=1" , "folderId" : "80b446f0-4261-11e9-9f1f-e19f7c813519" , "name" : "My First File.png" , "associationType" : "CostItem" , "associationId" : "328f3a40-3167-11e8-a044-01a43a3d152c" , "type" : "Upload" }
```

Congratulations! You have added an attachment to a cost item.
