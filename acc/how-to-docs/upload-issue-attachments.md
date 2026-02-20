# Upload Issue Attachments

Source: https://aps.autodesk.com/en/docs/acc/tutorials/issues/upload-issue-attachments/

---

# Upload Issue Attachments

This tutorial demonstrates how to attach a local file to an issue in an Autodesk Construction Cloud project.

The steps include finding the ID of the projectâs top-level folder, creating an empty storage object for the file, uploading the file to the storage object in OSS, and creating the attachment record in the issue.

## Before You Begin

- Register an app .

- Acquire a 3-legged OAuth token with data:read , data:write , and data:create scopes.

- Verify that you have access to the relevant account and ACC project.

- Find the relevant project ID for the project you want to add an attachment to by following the Retrieve an Account ID and Project ID tutorial. In this example, assume the account ID is b.cGVyc29uYWw6cGUyOWNjZjMy , and the project ID is b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5 .

- This tutorial assumes you have an existing issue to attach the file to. For more information on creating an issue, see the Create an Issue tutorial. In this example, assume the issue ID is d4f9c2e1-3b8a-4c7d-9e2f-1a5b8c9d0e3f . This is also known as the domainEntityId .

## Step 1: Find the Root Folder ID

Call GET projects/:projectId/topFolders using the account ID ( b.cGVyc29uYWw6cGUyOWNjZjMy ) and project ID ( b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5 ) to get a list of the highest-level folders in the project.

### Request

```
curl -v 'https://developer.api.autodesk.com/project/v1/hubs/b.cGVyc29uYWw6cGUyOWNjZjMy/projects/b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/topFolders' \ -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'
```

### Response

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/project/v1/hubs/b.cGVyc29uYWw6cGUyOWNjZjMy/projects/b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/topFolders" } }, "data" : [ { "type" : "folders" , "id" : "urn:adsk.wipprod:fs.folder:co.DtCxJN-3S3yVHFClpSLafw" , "attributes" : { "name" : "Project Files" , "displayName" : "Project Files" , "createTime" : "2025-05-11T13:06:46.0000000Z" , "createUserId" : "" , "createUserName" : "" , "lastModifiedTime" : "2025-06-15T14:30:44.0000000Z" , "lastModifiedUserId" : "A8K8LGLZRDGA" , "lastModifiedUserName" : "John Doe" , "lastModifiedTimeRollup" : "2025-06-15T14:30:44.0000000Z" , "objectCount" : 3 , "hidden" : false , "extension" : { "type" : "folders:autodesk.bim360:Folder" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/folders:autodesk.bim360:Folder-1.0" }, "data" : { "visibleTypes" : [ "items:autodesk.bim360:File" ], "actions" : [ "CONVERT" ], "allowedTypes" : [ "items:autodesk.bim360:File" , "folders:autodesk.bim360:Folder" ], "isRoot" : true , "folderType" : "normal" , "namingStandardIds" : [] } } }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/folders/urn:adsk.wipprod:fs.folder:co.DtCxJN-3S3yVHFClpSLafw" }, "webView" : { "href" : "https://acc.autodesk.com/docs/files/projects/b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5?folderUrn=urn%3Aadsk.wipprod%3Afs.folder%3Aco.DtCxJN-3S3yVHFClpSLafw" } }, "relationships" : { "contents" : { "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/folders/urn:adsk.wipprod:fs.folder:co.DtCxJN-3S3yVHFClpSLafw/contents" } } }, "parent" : { "data" : { "type" : "folders" , "id" : "urn:adsk.wip:fs.folder:co.1838SAGCQ3SPn7lqOXMaJQ" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/folders/urn:adsk.wipprod:fs.folder:co.DtCxJN-3S3yVHFClpSLafw/parent" } } }, "refs" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/folders/urn:adsk.wipprod:fs.folder:co.DtCxJN-3S3yVHFClpSLafw/relationships/refs" }, "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projectsb8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/folders/urn:adsk.wipprod:fs.folder:co.DtCxJN-3S3yVHFClpSLafw/refs" } } }, "links" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/folders/urn:adsk.wipprod:fs.folder:co.DtCxJN-3S3yVHFClpSLafw/relationships/links" } } } } } ] }
```

Note the root folder ID by finding the object where attributes.name equals Project Files , then use its parent folder ID. In this case, look at data[0].relationships.parent.data.id â urn:adsk.wip:fs.folder:co.1838SAGCQ3SPn7lqOXMaJQ .

The root folder (parent of Project Files) will be used to create the storage object in the next step.

## Step 2: Create a Storage Object

Use the project ID ( b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5 ) and the root folder ID ( urn:adsk.wip:fs.folder:co.1838SAGCQ3SPn7lqOXMaJQ ) to call POST projects/:project_id/storage to create an empty storage object for the file in the folder.

Note that you must assign a filename and file extension (such as .pdf , .jpg , .txt , etc.) to the name parameter (for example, 86360940-0703-4884-9130-9cb30b82e063e.pdf ). You can use a UUID as the name .

### Request

```
curl -X POST -H "Content-Type: application/vnd.api+json" -H "Accept: application/vnd.api+json" -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/data/v1/projects/b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/storage" -d '{ "jsonapi": { "version": "1.0" }, "data": { "type": "objects", "attributes": { "name": "86360940-0703-4884-9130-9cb30b82e063e.pdf" }, "relationships": { "target": { "data": { "type": "folders", "id": "urn:adsk.wip:fs.folder:co.1838SAGCQ3SPn7lqOXMaJQ" } } } } }'
```

### Response

```
{ "jsonapi" : { "version" : "1.0" }, "data" : { "type" : "objects" , "id" : "urn:adsk.objects:os.object:wip.dm.prod/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf" , "relationships" : { "target" : { "data" : { "type" : "folders" , "id" : "urn:adsk.wip:fs.folder:co.1838SAGCQ3SPn7lqOXMaJQ" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/folders/urn:adsk.wip:fs.folder:co.1838SAGCQ3SPn7lqOXMaJQ" } } } } } }
```

Note the Storage URN (known in Data Management as object ID): data.id - urn:adsk.objects:os.object:wip.dm.prod/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf

The storage URN includes the following sections: <urn:adsk.objects:os.object>:<bucket key>/<object key>

From this value, extract the following:

bucket key - wip.dm.prod . This will be used in step 3.

object key - a9d330bc-411f-4aaf-874a-9844cc002d00.pdf . Depending on the step, this is also referred to as the filename (includes the extension). This value will be required in steps 3, 5, and 6.

attachment ID - a9d330bc-411f-4aaf-874a-9844cc002d00 . This is derived from the object key/file name by removing the extension. This identifier will be used in step 6 when creating the attachment.

## Step 3: Generate a Signed URL

Use the bucket key ( wip.dm.prod ) and object key ( a9d330bc-411f-4aaf-874a-9844cc002d00.pdf ) to call GET signeds3upload to generate a signed URL for the storage object.

This endpoint supports generating multiple signed URLs, which allows you to upload multiple chunks of the same file in parallel.

### Request

```
curl -v 'https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf/signeds3upload' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "uploadKey" : "AQICAHgdUabBXKpMwUkoF5ivioCSHNq_j4g7HRbexUuXMaEMKgErLyuCRjoF46bviMXV-sbuAAAB7TCCAekGCSqGSIb3DQEHBqCCAdowggHWAgEAMIIBzwYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAxG3C2tr0WU_T43gXwCARCAggGgtWbNXJc6yIEVkQJjWoLmM0-Nuo1xXmx9C-vSZesB09y27QOgqhQN5BSJxKEVLllcvWGJTeKn3p6mAI2TKwnXswUseNCx_p_EhlYydzfYE8VHixCywEmBkOMIPX9OV0RogT1PjpQWobcM-_3W6Dnh9xtmpQ595QWLCGfVQdW8eg7XsdDP6i-ltDIbm4QMIXHgoX3zJ2Xk6c3tNAco_PuI3JYTRCSt1mwDZp7EeWK299HLn2qCZ_7O0wGNJjQMFJW0QMDcaHFRj75rCawWW-feAuUIVUisvVyimlZrqNU0LytKxfhP2wJ3WEc7pT0Ny18hTsIi8TAPcUa9VclEluFUJk5FP_jaRmQ9quol9cI1CQAxcbbes-F8rP2D-Xk87JXhbB5ik76SxvPZCT0eG7n9gYsD0PCRBFw5R-BqJL7k9AHTNKzObp14Of9rNWVNMFROQaR9zjLlC4z1hBsCrsdmauTPLcxNVkbVmO5ZNYw_uSxGIRtpJk2MEqRyqwVXiqla2CZvBo71v556jQ_PpBB634zfTar9wlbUbHJ5QNz9quo=" , "urls" : [ "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/8b/5d/bf/b1/bucket/wip.dm.prod/signed-url-uploads/a9d330bc-411f-4aaf-874a-9844cc002d00?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIA2P7NLTTBQB5AI5ET%2F20241109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241109T193928Z&X-Amz-Expires=900&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH8gvlQJF7xc%2FkSPHqbJCqGQwZeDk1WH%2FI3%2BK5nM7Q7bAiB8%2BpRvXYQ1L%2FRLQ1N3M4K6eE%2F5dY3%2FmP7wH4R1Q%3D%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=abcd1234567890abcdef1234567890abcdef1234567890abcdef1234567890" ] }
```

Note the uploadKey and the urls response attributes.

## Step 4: Upload a File to the Signed URL

To upload the file to the signed URL, use a PUT method and the urls attribute as the URI.

Note that you should not use a bearer token with this call.

### Request

```
curl -X PUT --data-binary @D: \s bc1-file1.pdf "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/a9d330bc-411f-4aaf-874a-9844cc002d00?uploadId=[UPLOAD_ID]&partNumber=1&X-Amz-Security-Token=[AMZ_TOKEN]%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220203T052230Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=[AMZ_CREDENTIAL]%2F20220203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=[AMZ_SIGNATURE]"
```

### Response

Note that a successful call ( 200 ) returns an empty response.

## Step 5: Complete the Upload

Use the bucket key ( wip.dm.prod ) the object key ( a9d330bc-411f-4aaf-874a-9844cc002d00.pdf` ) and the upload key ( AQICAHifrJ6-BSHUmjAat4..........QWI-fuvghN23akgePMdmykV ) to call POST signeds3upload to finalize the upload and register the file in Autodesk Docs.

This endpoint needs to be called within 24 hours from the time you began uploading the file.

### Request

```
curl -X POST "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf/signeds3upload" \ -H "Content-Type: application/json" \ -H "Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a" \ -d '{ "uploadKey": "AQICAHgdUabBXKpMwUkoF5ivioCSHNq_j4g7HRbexUuXMaEMKgErLyuCRjoF46bviMXV-sbuAAAB7TCCAekGCSqGSIb3DQEHBqCCAdowggHWAgEAMIIBzwYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAxG3C2tr0WU_T43gXwCARCAggGgtWbNXJc6yIEVkQJjWoLmM0-Nuo1xXmx9C-vSZesB09y27QOgqhQN5BSJxKEVLllcvWGJTeKn3p6mAI2TKwnXswUseNCx_p_EhlYydzfYE8VHixCywEmBkOMIPX9OV0RogT1PjpQWobcM-_3W6Dnh9xtmpQ595QWLCGfVQdW8eg7XsdDP6i-ltDIbm4QMIXHgoX3zJ2Xk6c3tNAco_PuI3JYTRCSt1mwDZp7EeWK299HLn2qCZ_7O0wGNJjQMFJW0QMDcaHFRj75rCawWW-feAuUIVUisvVyimlZrqNU0LytKxfhP2wJ3WEc7pT0Ny18hTsIi8TAPcUa9VclEluFUJk5FP_jaRmQ9quol9cI1CQAxcbbes-F8rP2D-Xk87JXhbB5ik76SxvPZCT0eG7n9gYsD0PCRBFw5R-BqJL7k9AHTNKzObp14Of9rNWVNMFROQaR9zjLlC4z1hBsCrsdmauTPLcxNVkbVmO5ZNYw_uSxGIRtpJk2MEqRyqwVXiqla2CZvBo71v556jQ_PpBB634zfTar9wlbUbHJ5QNz9quo=" }'
```

### Response

```
{ "bucketKey" : "wip.dm.prod" , "objectId" : "urn:adsk.objects:os.object:wip.dm.prod/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf" , "objectKey" : "a9d330bc-411f-4aaf-874a-9844cc002d00.pdf" , "size" : 4729968 , "contentType" : "application/octet-stream" , "location" : "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf" }
```

The file has been uploaded to the storage object.

Note that the objectId â urn:adsk.objects:os.object:wip.dm.prod/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf is the same as the storage URN.

## Step 6: Attach the File to the Issue

Call POST attachments to attach the uploaded file to an existing issue, using the following values:

- domainEntityId - the ID of the issue to attach the file to. We defined the issue ID in the Before you Begin section.

- storageUrn - the storage URN from step 2 - urn:adsk.objects:os.object:wip.dm.prod/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf

- fileName â the full filename including extension. This is the same as the object key from step 2. In this example - a9d330bc-411f-4aaf-874a-9844cc002d00.pdf .

- displayName â a human-readable name for the attachment. In this example, Project Plans.pdf . This is what users will see in the ACC interface.

- attachmentType â  this is always set to issue-attachment .

- attachmentId â the file name derived from step 2 without the extension. In this example, a9d330bc-411f-4aaf-874a-9844cc002d00 .

### Request

```
curl -X POST 'https://developer.api.autodesk.com/construction/issues/v1/projects/b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/attachments' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "domainEntityId": "d4f9c2e1-3b8a-4c7d-9e2f-1a5b8c9d0e3f", "attachments": [ { "attachmentId": "a9d330bc-411f-4aaf-874a-9844cc002d00", "displayName": "Project Plans.pdf", "fileName": "a9d330bc-411f-4aaf-874a-9844cc002d00.pdf", "attachmentType": "issue-attachment", "storageUrn": "urn:adsk.objects:os.object:wip.dm.prod/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf" } ] }'
```

### Response

```
{ "attachments" : [ { "attachmentId" : "a9d330bc-411f-4aaf-874a-9844cc002d00" , "displayName" : "Project Plans.pdf" , "fileName" : "a9d330bc-411f-4aaf-874a-9844cc002d00.pdf" , "attachmentType" : "issue-attachment" , "storageUrn" : "urn:adsk.objects:os.object:wip.dm.prod/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf" , "fileSize" : 4729968 , "fileType" : "pdf" , "domainEntityId" : "d4f9c2e1-3b8a-4c7d-9e2f-1a5b8c9d0e3f" , "lineageUrn" : "urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ" , "version" : 1 , "versionUrn" : "urn:adsk.wipprod:fs.file:vf.1HROnsnfQgq4N0b-nUoGge?version=1" , "tipVersionUrn" : "urn:adsk.wipprod:fs.file:vf.1HROnsnfQgq4N0b-nUoGge?version=1" , "createdBy" : "A3RGM375QTZ7" , "createdOn" : "2024-11-09T19:39:28.779314Z" , "deletedBy" : null , "deletedOn" : null , "isDeleted" : false } ] }
```

Congratulations! You have successfully attached a file to an issue in Autodesk Construction Cloud. The attachment is now associated with the issue and ready for viewing by team members.
