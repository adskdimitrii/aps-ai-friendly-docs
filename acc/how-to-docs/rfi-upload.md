# Upload Attachments to RFIs

Source: https://aps.autodesk.com/en/docs/acc/tutorials/rfis3/rfi-upload/

---

# Upload Attachments to RFIs

This tutorial demonstrates how to upload attachments to RFIs. The process includes locating the ID of the project that contains the RFI, identifying the virtual folder where the attachment will be stored, creating an empty storage object, generating a signed S3 URL, and uploading the attachment using that URL.

For more details about ACC Document management, see the Data Management API .

## Before You Begin

- Register an app , and select the Data Management and Autodesk Construction Cloud APIs.

- Acquire a 3-legged OAuth token with data:create data:read and data:write scopes.

- Assume the RFI that you want to add the attachment to is 31a3f98d-34a8-4d4c-a362-3cc9de44f89c .

- Verify that you have access to the relevant ACC account, project, and folder.

## Step 1: Find the Hub ID for the ACC Account

The first few steps of the tutorial demonstrate how to find the ID of the project that contains the RFI. This involves using several Data Management endpoints to find the folder ID.

Call GET hubs to find the hub ID for the ACC account that includes the project that contains the RFI you want to add the attachment to.

Note that the ACC account ID corresponds to a Data Management hub ID. To convert an account ID into a hub ID you need to add a â b. " prefix. For example, an account ID of c8b0c73d-3ae9 translates to a hub ID of b. c8b0c73d-3ae9.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs"
```

### Response

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/project/v1/hubs" } }, "data" : [ { "type" : "hubs" , "id" : "b.cGVyc29uYWw6cGUyOWNjZjMy" , "attributes" : { "name" : "Acme Construction" , "extension" : { "type" : "hubs:autodesk.bim360:Account" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/hubs:autodesk.bim360:Account-1.0" }, "data" : {} } } } ] }
```

In this example, assume that the RFI you want to add the attachment to is in a hub called Acme Construction .

Find the hub ( data.name ), and note the hub ID - b.cGVyc29uYWw6cGUyOWNjZjMy .

## Step 2: Find the Project ID

Use the hub ID ( b.cGVyc29uYWw6cGUyOWNjZjMy ) to call GET hubs/:hub_id/projects to get a list of all the projects in the hub. Find the project ID of the project that contains the RFI you want to upload the attachment to.

Note that the project ID in ACC corresponds to the project ID in the Data Management API . To convert a project ID in ACC to a project ID in the Data Management API, you need to add a â b. " prefix. For example, a project ID of a4be0c34a-4ab7 translates to a project ID of b. a4be0c34a-4ab7.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs/b.cGVyc29uYWw6cGUyOWNjZjMy/projects"
```

### Response

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/project/v1/hubs/b.cGVyc29uYWw6cGUyOWNjZjMy/projects" } }, "data" : [ { "type" : "projects" , "id" : "b.cGVyc29uYWw6d2l" , "attributes" : { "name" : "Main Street School Renovation" , "extension" : { "type" : "projects:autodesk.core:Project" , "version" : "1.0" } } } ] }
```

In this example, assume that Main Street School Renovation is the project that contains the RFI you want to add the attachment to.

Find the project ( data.attributes.name ), and note the project ID ( data.id ) - b.cGVyc29uYWw6d2l .

## Step 3: Find the RFI Virtual Folder ID

Note that virtual folder creation is triggered as a separate asynchronous job when an RFI is created.
Until this folder is successfully created, users cannot upload files into it.
To confirm that the folder is ready, call GET rfis/:id </en/docs/acc/v1/reference/http/rfis-rfis-id-GET/> and check that the virtualFolderUrn field appears in the response.

Use the project ID ( b.cGVyc29uYWw6d2l ) and the RFI ID ( 31a3f98d-34a8-4d4c-a362-3cc9de44f89c to call GET rfis/:id to get the virtual folder ID for the RFI.

To find the RFI ID, call POST search:rfis .

### Request

```
curl -v 'https://developer.api.autodesk.com/v3/projects/b.cGVyc29uYWw6d2l/rfis/31a3f98d-34a8-4d4c-a362-3cc9de44f89c' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "id" : "31a3f98d-34a8-4d4c-a362-3cc9de44f89c" , "customIdentifier" : "ID-1234" , "title" : "RFI - pipe is not in right place" , "question" : "Where should we put the pipe?" , "virtualFolderUrn" : "urn:adsk.wip:fs.folder:co.1838SAGCQ3SPn7lqOXMaJQ" , "status" : "open" , "previousStatus" : "submitted" , "workflowType" : "US" , "assignedTo" : [ { "id" : "PER8KQPK2JRT" , "type" : "user" } ], "managerId" : "KOR8KQPK2GHF" , "constructionManagerId" : "ALW8KQPK2PTB" , "architects" : [ { "type" : "user" , "id" : "TKG8KQPK2MNB" } ], "reviewers" : [ { "type" : "user" , "id" : "IKJ8KQPK2WDV" } ], "dueDate" : "2018-01-12T13:06:39.216Z" , "locationDescription" : "In the middle of the room" , "locations" : [ "AJJASD2-FFE3" , "JTOEN-FFD33" ], "commentsCount" : 15 , "officialResponse" : "The measurements are correct." , "officialResponseStatus" : "answered" , "officialResponseActors" : [ { "id" : "AJJASD2-FFE3" , "type" : "user" }, { "id" : "JTOEN-FFD33" , "type" : "user" } ], "officialResponseEditByManagerState" : true , "respondedAt" : "2018-01-12T13:06:39.216Z" , "respondedBy" : "RFV8KQPK2KHF" , "createdBy" : "PER8KQPK2JRT" , "createdAt" : "2018-07-22T15:05:58.033Z" , "updatedBy" : "ZXC8KQPK2CVB" , "updatedAt" : "2018-07-22T15:05:58.033Z" , "closedAt" : "2018-07-22T15:05:58.033Z" , "closedBy" : "SER8KQPK2JRT" , "containerId" : "31a3f98d-34a8-4d4c-a362-3cc9de44f89c" , "projectId" : "31a3f98d-34a8-4d4c-a362-3cc9de44f89c" , "suggestedAnswer" : "The measurements are correct." , "coReviewers" : [ { "id" : "WSX8KQPK2JRMJ" , "type" : "user" } ], "watchers" : [ { "id" : "PER8KQPK2JRT" , "type" : "user" } ], "answeredAt" : "2018-07-22T15:05:58.033Z" , "answeredBy" : "FGD8KQPK2JKK" , "costImpact" : "Yes" , "scheduleImpact" : "Yes" , "priority" : "High" , "discipline" : [ "Architectural" ], "category" : [ "Constructability" ], "reference" : "ID-1234" , "customAttributes" : [ { "id" : "c911852d-5957-4145-9c8d-e7cfe9d564df" , "values" : [ "" ], "isSelectable" : false } ], "rfiTypeId" : "c911852d-5957-4145-9c8d-e7cfe9d564df" , "bridgedSource" : "" , "bridgedTarget" : "" , "bridgeSyncOutdated" : "" , "syncVersion" : "" , "responses" : [ { "id" : "c911852d-5957-4145-9c8d-e7cfe9d564df" , "state" : "draft" , "rfiId" : "w332252d-5957-4145-9c8d-e7cfe9d975aj" , "text" : "The pipe should be placed in the corner" , "status" : "answered" , "createdBy" : "PER8KQPK2JRT" , "onBehalf" : "PER8KQPK2JRT" , "isEditable" : true , "createdAt" : "2018-07-22T15:05:58.033Z" , "updatedBy" : "PER8KQPK2JRT" , "updatedAt" : "2018-07-22T15:05:58.033Z" , "deletedAt" : "2018-07-22T15:05:58.033Z" } ], "draftResponses" : [ { "id" : "c911852d-5957-4145-9c8d-e7cfe9d564df" , "state" : "draft" , "rfiId" : "w332252d-5957-4145-9c8d-e7cfe9d975aj" , "text" : "The pipe should be placed in the corner" , "status" : "answered" , "createdBy" : "PER8KQPK2JRT" , "onBehalf" : "PER8KQPK2JRT" , "isEditable" : true , "createdAt" : "2018-07-22T15:05:58.033Z" , "updatedBy" : "PER8KQPK2JRT" , "updatedAt" : "2018-07-22T15:05:58.033Z" , "deletedAt" : "2018-07-22T15:05:58.033Z" } ], "permittedActions" : { "share" : "" , "nudge" : "" , "updateRfi" : { "permittedStatuses" : { "wfUS" : [ { "status" : "open" , "maxAssignees" : "" , "requiredAttributes" : [ { "name" : "assignedTo" , "values" : [ { "value" : "PER8KQPK2JRT" , "type" : "user" } ] } ], "permittedAttributes" : [ { "name" : "assignedTo" , "values" : [ { "value" : "PER8KQPK2JRT" , "type" : "user" } ] } ] } ], "wfEU" : [ { "status" : "open" , "maxAssignees" : "" , "requiredAttributes" : [ { "name" : "assignedTo" , "values" : [ { "value" : "PER8KQPK2JRT" , "type" : "user" } ] } ], "permittedAttributes" : [ { "name" : "assignedTo" , "values" : [ { "value" : "PER8KQPK2JRT" , "type" : "user" } ] } ] } ] }, "permittedAttributes" : [ { "name" : "assignedTo" , "values" : [ { "value" : "PER8KQPK2JRT" , "type" : "user" } ] } ], "useCustomAttributes" : "" }, "createComment" : "" , "createResponse" : "" , "createResponseOnBehalf" : "" , "remainingReviewers" : [ { "id" : "PER8KQPK2JRT" , "type" : "user" } ], "createDocumentReference" : "" , "removeDocumentReference" : "" }, "maxAssignees" : 10 }
```

Note the virtual folder ID ( virtualFolderUrn ) - "urn:adsk.wip:fs.folder:co.1838SAGCQ3SPn7lqOXMaJQ" .

## Step 4: Create a Storage Object

Use the project ID ( b.cGVyc29uYWw6d2l ) and the virtual folder ID ( urn:adsk.wip:fs.folder:co.1838SAGCQ3SPn7lqOXMaJQ ) to call POST projects/:project_id/storage to create an empty storage object for the file in the folder.

Note that you must assign a filename and file extension (such as .pdf , .jpg , .txt , etc.) to the name parameter (for example, site-plan-v2.pdf ).

### Request

```
curl -X POST -H "Content-Type: application/vnd.api+json" -H "Accept: application/vnd.api+json" -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/storage" -d '{ "jsonapi": { "version": "1.0" }, "data": { "type": "objects", "attributes": { "name": "site-plan-v2.pdf" }, "relationships": { "target": { "data": { "type": "folders", "id": "urn:adsk.wipprod:fs.folder:co.1838SAGCQ3SPn7lqOXMaJQ" } } } } }'
```

### Response

```
{ "jsonapi" : { "version" : "1.0" }, "data" : { "type" : "objects" , "id" : "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg" , "relationships" : { "target" : { "data" : { "type" : "folders" , "id" : "urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.831f65de-bd1a-44b7-9709-56c4c1294a32/folders/urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA" } } } } } }
```

Note the object ID ( data.id ) - urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg .

The object ID includes the following sections: <urn:adsk.objects:os.object>:<bucket key>/<object key>

Note the bucket key - wip.dm.prod and the object key - 2a6d61f2-49df-4d7b.jpg

## Step 5: Generate a Signed S3 URL

ACC stores files in Amazon S3, and uploads must go through signed URLs for security. Use the bucket key and object key to generate a signed upload URL for your storage object.

Use the bucket key ( wip.dm.prod ) and the object key ( 2a6d61f2-49df-4d7b.jpg ) to call GET buckets/:bucketKey/objects/:objectKey/signeds3upload to generate a signed URL for the storage object.

This endpoint supports generating multiple signed URLs, which allows you to upload multiple chunks of the same file in parallel. For more information, see GET signeds3upload .

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/2a6d61f2-49df-4d7b.jpg/signeds3upload"
```

### Response

```
{ "uploadKey" : "AQICAHifrJ6-BSHUmjAat4..........QWI-fuvghN23akgePMdmykV" , "uploadExpiration" : "2022-02-05T00:00:00Z" , "urlExpiration" : "2022-02-03T05:23:29Z" , "urls" : [ "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/26668812-6bb1-4f80-bab2-09776f24fd98?uploadId=[UPLOAD_ID]&partNumber=1&X-Amz-Security-Token=[AMZ_TOKEN]%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220203T052230Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=[AMZ_CREDENTIAL]%2F20220203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=[AMZ_SIGNATURE]" ] }
```

Note the uploadKey and the urls response attributes.

## Step 6: Upload a File to the Signed URL

To upload the file to the signed URL, use a PUT method and the urls attribute as the URI.

Note that you should not use a bearer token with this call.

### Request

```
curl -X PUT --data-binary @D: \s ite-plan-v2.pdf "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/26668812-6bb1-4f80-bab2-09776f24fd98?uploadId=[UPLOAD_ID]&partNumber=1&X-Amz-Security-Token=[AMZ_TOKEN]%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220203T052230Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=[AMZ_CREDENTIAL]%2F20220203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=[AMZ_SIGNATURE]"
```

Note that a successful call ( 200 ) returns an empty response.

## Step 7: Complete the Upload

Use the bucket key ( wip.dm.prod ) the object key ( 2a6d61f2-49df-4d7b.jpg` ) and the upload key ( AQICAHifrJ6-BSHUmjAat4..........QWI-fuvghN23akgePMdmykV ) to call POST buckets/:bucket_key/objects/:object_key/signeds3upload to complete the upload.

This endpoint needs to be called within 24 hours from the time you began uploading the file.

### Request

```
curl -X POST -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" --data-raw '{"uploadKey":"AQICAHifrJ6-BSHUmjAat4..........QWI-fuvghN23akgePMdmykV"}' "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg/signeds3upload"
```

### Response

```
{ "bucketKey" : "wip.dm.prod" , "objectId" : "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg" , "objectKey" : "2ac28abc-9f6e-463d-bcc4-5c194d552beb.jpg" , "size" : 879394 , "contentType" : "application/octet-stream" , "location" : "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg" }
```

The file has been uploaded to the storage object.

## Step 8: Assign the Attachment to a Response

At this point, the file has been uploaded to the RFIâs virtual folder â but it wonât appear in the RFI interface unless itâs assigned to a specific response.

To complete the workflow, see the Upload Attachments to RFI Responses tutorial , which shows how to attach the file to a draft response.

Note that we do not currently support the workflow to assign attachments directly to the official response via the API. This will be available in a future release.

Congratulations! Youâve completed the upload and assignment process â the attachment is now part of the RFI response and visible in the RFI interface.
