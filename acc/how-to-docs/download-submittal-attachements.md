# Download Submittal Attachments

Source: https://aps.autodesk.com/en/docs/acc/tutorials/submittals/download-submittal-attachements/

---

# Download Submittal Attachments

This tutorial demonstrates how to download attachments that were added to submittal items in ACC Submittals. For more information about ACC Submittals, see the Submittals Help documentation . The steps include finding the ID of the submittal item that is associated with the attachment that you want to download, finding the storage object ID for the relevant attachment, retreiving a signed-URL for the attachment, and using the signed-URL to download the attachment.

## Before You Begin

- Register an app

- Acquire a 3-legged OAuth token with the data:read scope.

- Verify that you have access to the relevant account and ACC project.

- Find the relevant project ID for the project you want to download an attachment from. See the Retrieve a Project ID tutorial for more details. In this example, assume the project ID is f6a1e3b5-abaa-4b01-b33a-5d55f36ba047 .

## Step 1: Find the Submittal Item ID

Find the ID of the submittal item that is associated with the attachment that you want to download by calling GET items using the project ID ( f6a1e3b5-abaa-4b01-b33a-5d55f36ba047 ).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/items' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "results" : [ { "id" : "b8cc9324-6759-4f07-8ce3-725d5afd4f11" , "identifier" : 1111 , "typeId" : "06fa0c1b-6462-459d-8a38-0aff11bfe868" , "specId" : "62d6f245-b470-4af4-802b-4cb94b5dead1" , "specIdentifier" : "09-5300" , "specTitle" : "Acoustical Ceilings" , "subsection" : "1.05-B" , "title" : "Shop Drawings" , "description" : "Detailed plans by subcontractor, showing project dimensions." , "priority" : "Low" , "revision" : 0 , "stateId" : "rev" , "statusId" : "1" , "ballInCourtUsers" : [ "WD43ZJGKDFLFH" ], "ballInCourtCompanies" : [ "WD43ZJGKDFLFH" ], "ballInCourtRoles" : [ "WD43ZJGKDFLFH" ], "ballInCourtType" : "reviewer" , "manager" : "WD43ZJGKDFLFH" , "managerType" : "1" , "subcontractor" : "WD43ZJGKDFLFH" , "subcontractorType" : "1" , "watchers" : [ { "id" : "224356" , "userType" : "2" }, { "id" : "3522614" , "userType" : "3" } ], "dueDate" : "2018-02-15" , "requiredOnJobDate" : "2018-02-15" , "leadTime" : 100 , "requiredDate" : "2018-02-15" , "requiredApprovalDate" : "2018-02-15" , "submitterDueDate" : "2018-02-15" , "sentToSubmitter" : "2018-02-01T12:09:24.198466Z" , "receivedFromSubmitter" : "2018-02-01T12:09:24.198466Z" , "submittedBy" : "WD43ZJGKDFLFH" , "managerDueDate" : "2018-02-15" , "sentToReview" : "2018-02-01T12:09:24.198466Z" , "sentToReviewBy" : "WD43ZJGKDFLFH" , "receivedFromReview" : "2018-02-01T12:09:24.198466Z" , "publishedDate" : "2018-02-01T12:09:24.198466Z" , "publishedBy" : "WD43ZJGKDFLFH" , "responseId" : "2d46d30b-7dc1-4a65-991d-d739a1381eb8" , "responseComment" : "" , "respondedAt" : "2018-02-01T12:09:24.198466Z" , "respondedBy" : "WD43ZJGKDFLFH" , "packageId" : "e8302552-fc5a-42ac-ba4b-e9de9760c356" , "packageIdentifier" : "222" , "packageTitle" : "my package1" , "packageSpecIdentifier" : "A-500" , "folderUrn" : "urn:adsk.wipprod:fs.file:vf.hvNfeldTPm_aDqRNZgKjD" , "revisionsFoldersUrns" : { "0" : { "folderUrnCreatedAt" : "2018-01-28 09:26:36.371607" , "revision" : 0 , "folderUrn" : "urn:adsk.wipprod:fs.folder:co.r04fl5B7QCa1731EeH5dYDQ" } }, "createdAt" : "2018-02-01T12:09:24.198466Z" , "createdBy" : "WD43ZJGKDFLFH" , "updatedAt" : "2018-04-04T12:09:24.198466Z" , "updatedBy" : "WD43ZJGKDFLFH" , "permittedActions" : [ { "id" : "Item::retrieve" , "fields" : {}, "mandatoryFields" : [ "" ], "transitions" : [ { "id" : "rev::void" , "name" : "Send to void" , "stateFrom" : { "id" : "rev" , "name" : "REV" }, "stateTo" : { "id" : "rev" , "name" : "REV" }, "transitionFields" : [ "subcontractor" , "subcontractorType" , "watchers" , "responseId" ], "mandatoryFields" : [ "responseId" ], "actionId" : "ITEM_TRANSITION_REV_VOID" } ] } ] } ], "pagination" : { "limit" : 10 , "offset" : 100 , "totalResults" : 25 , "previousUrl" : "https://developer.api.autodesk.com//construction/submittals/v2/projects/04605b7a-0c53-421e-8e11-c743e75ac10a" , "nextUrl" : null } }
```

Note the ID of the item that is associated with the attachment you want to download ( results.id ) ( b8cc9324-6759-4f07-8ce3-725d5afd4f112 ).

## Step 2: Find the Storage Object ID for the Attachment

Find the storage object ID for the attachment you want to download by calling GET attachments using the project ID ( f6a1e3b5-abaa-4b01-b33a-5d55f36ba047 ) and the item ID ( b8cc9324-6759-4f07-8ce3-725d5afd4f112 ).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/items/attachments' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "pagination" : { "limit" : 10 , "offset" : 100 , "totalResults" : 25 , "previousUrl" : "https://developer.api.autodesk.com//construction/submittals/v2/projects/04605b7a-0c53-421e-8e11-c743e75ac10a" , "nextUrl" : null }, "results" : [ { "id" : "1d0a9b65-f411-4eb2-b6bb-69f8ea483207" , "itemId" : "2df3b4cf-16f4-496e-8173-7125f31e3dd1" , "taskId" : "1ab2ae43-fb33-4868-be85-03f4873915fc" , "name" : "attachment-document.pdf" , "isFileUploaded" : "true" , "url" : null , "asyncState" : "1" , "uploadUrn" : "urn:adsk.objects:os.object:wip.dm.prod/72d5e7e4-89a7-4cb9-9da0-2e2bbc61ca8e.dwg" , "urn" : "urn:adsk.wipprod:fs.file:vf.TQW6YsrTTFGrJVJKAaK_ew?version=1" , "urnVersion" : 1 , "revisionFolderUrn" : "urn:adsk.wipprod:fs.folder:co.3is_lyUzTxu6nNXobG2P7Q\"" , "revision" : 0 , "urnTypeId" : "1" , "categoryId" : "1" , "urnPage" : null , "resourceUrns" : null , "createdBy" : "WD43ZJGKDFLFH" , "createdAt" : "2018-02-01T12:09:24.198466Z" , "updatedAt" : "2018-02-01T12:09:24.198466Z" , "updatedBy" : "WD43ZJGKDFLFH" , "duplicatedFrom" : "f4635373-a5b4-456c-af8d-e0446652967c" , "permittedActions" : [ { "id" : "Item::retrieve" , "fields" : {}, "mandatoryFields" : [ "" ], "transitions" : [ { "id" : "rev::void" , "name" : "Send to void" , "stateFrom" : { "id" : "rev" , "name" : "REV" }, "stateTo" : { "id" : "rev" , "name" : "REV" }, "transitionFields" : [ "subcontractor" , "subcontractorType" , "watchers" , "responseId" ], "mandatoryFields" : [ "responseId" ], "actionId" : "ITEM_TRANSITION_REV_VOID" } ] } ] } ] }
```

Find the relevant attachment ( results.name ), and note the corresponding storage object ID ( results.uploadUrn ) - urn:adsk.objects:os.object:wip.dm.prod/72d5e7e4-89a7-4cb9-9da0-2e2bbc61ca8e.dwg .

The storage object ID includes the following sections: <urn:adsk.objects:os.object>:<bucket_key>/<object_key>

Note the bucket key - wip.dm.prod and the storage object key - 72d5e7e4-89a7-4cb9-9da0-2e2bbc61ca8e.dwg

## Step 3: Generate a Signed S3 URL

Use the bucket key ( wip.dm.prod ) and the object key ( 72d5e7e4-89a7-4cb9-9da0-2e2bbc61ca8e.dwg ) to call GET buckets/:bucketKey/objects/:objectKey/signeds3download to generate a signed URL for the storage object, which you can use to download the file directly from S3.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/72d5e7e4-89a7-4cb9-9da0-2e2bbc61ca8e.dwg/signeds3download"
```

### Response

```
{ "status" : "complete" , "url" : "https://cdn.us.oss.api.autodesk.com/com.autodesk.oss-persistent/us-east-1/3f/bf/5f/0137a7d9dc53af930bc1b527320d50fb5f/wip.dm.prod?response-content-type=application%2Foctet-stream&response-content-disposition=attachment%3B+filename%3D%977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt%22&Expires=1643864703&Signature=00PZYS6gL~Nc6aRG2HAhOCKYl0xtqsuujMJ~VKSXm1vBa-OxS4lPQBSlTx5bswpLBe1W6Rz94eIZW2sPN-v6Mzz~JyXNZ-V9Z7zlBoE1VoQhspLioC225hxq6ZmDSU5QnZXuNDV4ih~p1n3xacYvUvQWX-ONAGVUgQvZ253Svw~qx-pO4j-Yh4kVRmzDZqQut1xOI5ZGH6JFGhXLSzkgbYcfYx6fvCxnvYUJrgAcqncIwGVewI3uC0I84Fzrj8nXE8ojuojqJP0pNlxkfBe~2LfjjzqKDKaNvfC2Grt12j9QgC~cN7nQCRcVUhExpoV1VVB5x3AkVTJ-q5NoedvsfO__&Key-Pair-Id=95HRZD7MMO1UK" , "params" : { "content-type" : "application/octet-stream" , "content-disposition" : "attachment; filename=\"977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt\"" }, "size" : 472424 , "sha1" : "ffbf5f0137a7d9dc53af930bc1b527320d50fb53" }
```

## Step 4: Download the File

To download the file from the signed URL, use a GET method and the url attribute as the URI.

Note that you can only use the signed URL once; after you have used it, it becomes invalid and cannot be used again.

Note that you should not use a bearer token with this call.

### Request

```
curl -X GET "https://cdn.us.oss.api.autodesk.com/com.autodesk.oss-persistent/us-east-1/3f/bf/5f/0137a7d9dc53af930bc1b527320d50fb5f/wip.dm.prod?response-content-type=application%2Foctet-stream&response-content-disposition=attachment%3B+filename%3D%977d69b1-43e7-40fa-8ece-6ec4602892f3.dwg%22&Expires=1643864703&Signature=00PZYS6gL~Nc6aRG2HAhOCKYl0xtqsuujMJ~VKSXm1vBa-OxS4lPQBSlTx5bswpLBe1W6Rz94eIZW2sPN-v6Mzz~JyXNZ-V9Z7zlBoE1VoQhspLioC225hxq6ZmDSU5QnZXuNDV4ih~p1n3xacYvUvQWX-ONAGVUgQvZ253Svw~qx-pO4j-Yh4kVRmzDZqQut1xOI5ZGH6JFGhXLSzkgbYcfYx6fvCxnvYUJrgAcqncIwGVewI3uC0I84Fzrj8nXE8ojuojqJP0pNlxkfBe~2LfjjzqKDKaNvfC2Grt12j9QgC~cN7nQCRcVUhExpoV1VVB5x3AkVTJ-q5NoedvsfO__&Key-Pair-Id=95HRZD7MMO1UK" --output "My First File.dwg"
```

Congratulations! You have downloaded an attachment from ACC submittals.
