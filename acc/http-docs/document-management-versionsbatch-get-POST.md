# projects/{project_id}/versions:batch-get

Source: https://aps.autodesk.com/en/docs/acc/reference/http/document-management-versionsbatch-get-POST/

---

# projects/{project_id}/versions:batch-get

Retrieves a list of custom attribute values for multiple BIM 360 Document Management documents. For information about custom attributes, see the Help documentation . This endpoint also retrieves information about a documentâs approval status and revision number.

You can either retrieve the custom attributes using the version ID or the item ID. If you use the item ID it returns the custom attributes for the latest (tip) version of the file. For information about finding the version ID and item ID for a document, see the initial steps of the Download File tutorial.

Note that this endpoint only retrieves custom attributes that have been assigned a value. To retrieve the full list of the documentâs custom attributes including custom attributes that have not been assigned a value, call GET custom-attribute-definitions .

To assign values to a documentâs custom attributes or to clear custom attribute values, call POST custom-attributes:batch-update .

For more details about custom attributes, see the Update Custom Attributes tutorial.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/bim360/docs/v1/projects/:project_id/versions:batch-get Authentication Context user context optional Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. Content-Type * string Must be application/json x-user-id string In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified.

### Request

## URI Parameters

project_id string The ID of the project. This corresponds to project ID in the Data Management API . To convert a project ID in the Data Management API into a project ID in the BIM 360 API you need to remove the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Request

## Body Structure

urns * array: string A list of version IDs or item IDs. If you use item IDs it retrieves the values for the latest (tip) versions. You can specify up to 50 documents. To find the version ID and item ID of a document follow the initial steps of the Download Files tutorial.

### Response

## HTTP Status Code Summary

200 OK Successful retrieval of versions. 400 Bad Request The parameters of the requested operation are invalid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The project does not exist. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

results array: object The list of results. urn string The ID of the version. itemUrn string The ID of the related item. name string The name of the version. This corresponds to the file name in BIM 360 Document Management. title string The title of the version. number string The sheet number. This is only relevant for documents uploaded to the Plans folder that were split into sheets. createTime string The time and date the version was created. createUserId string The ID of the user who created the version. createUserName string The name of the user who created the version. lastModifiedTime string The time and date the version was last modified. lastModifiedUserId string The ID of the user who last modified the version. lastModifiedUserName string The name of the user who last modified the version. storageUrn string The ID of the versionâs storage object. This is only relevant for documents that were not split into sheets when they were uploaded to BIM 360 Document Management. storageSize int The file size of the versionâs storage object, in bytes. This is only relevant for documents that were not split into sheets when they were uploaded to BIM 360 Document Management. entityType enum:string The type of version. Possible values: SEED_FILE : Documents that were not split into sheets when they were uploaded to BIM 360 Document Management. DOCUMENT : Documents that were split into sheets when they were uploaded to BIM 360 Document Management. revisionNumber int The revision number of the version. The revision number increases when you completely replace the version. For example when you reupload a document and overwrite the current document. Note that this is not the same as the version number, which increases when you update the document. For example, when you save the document. The revision number corresponds to the version in BIM 360 Document Management. processState enum:string The process state of the version.
Possible values: NEEDS_PROCESSING , PROCESSING , PREVIOUS_SEED_PENDING , EXTRACTION_PENDING , SPLITTING , PREVIOUS_DOC_PENDING , PROCESSING_ABORTING , PROCESSING_ABORTED , PROCESSING_COMPLETE , PROCESSING_PROMOTION , PROCESSING_COPY , PROCESSING_PROMOTING , PROCESSING_COPYING , PROCESSING_SUSPEND approvalStatus object The approval status of the version. Only available when the review has been approved or rejected. For more information about the approval workflow, see the Approval Workflows and Document Review documentation. label string The customized label of the approval status. Max length: 255 value enum:string The value of the approval status.
Possible values: approved , rejected customAttributes array: object The list of custom attributes for each document. For more information about custom attributes, see the Customize Documents with Attributes documentation. id int The ID of the attribute. type enum:string The data type of the attribute. Possible values: string (text field), date , array (drop-list). name string The name of the attribute. value string The value of the attribute. errors array: object The list of errors. urn string The ID of the version or item associated with the error. code string The error code. title string The title of the error. detail string The details about the error.

- SEED_FILE : Documents that were not split into sheets when they were uploaded to BIM 360 Document Management.

- DOCUMENT : Documents that were split into sheets when they were uploaded to BIM 360 Document Management.

Max length: 255

## Example

Successful retrieval of versions.

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/docs/v1/projects/:project_id/versions:batch-get' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "urns": [ "urn:adsk.wipprod:fs.file:vf.zSoimiozRD6qdgHwfykp_w?version=6", "urn:adsk.wipprod:dm.lineage:AS3XD9MzQvu4MakMF-w7vQ" ] }'
```

### Response

```
{ "results" : [ { "urn" : "urn:adsk.wipprod:fs.file:vf.AS3XD9MzQvu4MakMF-w7vQ?version=1" , "itemUrn" : "urn:adsk.wipprod:dm.lineage:AS3XD9MzQvu4MakMF-w7vQ" , "name" : "Oct.pdf" , "title" : "Bin Work" , "number" : "" , "createTime" : "2019-04-18T03:33:36+0000" , "createUserId" : "CGZ5PG7PZMAS" , "createUserName" : "Tom Jerry" , "lastModifiedTime" : "2019-04-18T03:33:36+0000" , "lastModifiedUserId" : "CGZ5PG7PZMAS" , "lastModifiedUserName" : "Tom Jerry" , "storageUrn" : "urn:adsk.objects:os.object:wip.dm.prod/c4a75bbc-24eb-41a3-a58b-48e51942222e.pdf" , "storageSize" : 7164826 , "entityType" : "SEED_FILE" , "revisionNumber" : 1 , "processState" : "PROCESSING_COMPLETE" , "approvalStatus" : { "label" : "Approved w/ comments." , "value" : "approved" }, "customAttributes" : [ { "id" : 123 , "type" : "array" , "name" : "Drawing Type" , "value" : "General" } ] } ], "errors" : [ { "urn" : "urn:adsk.wipprod:fs.file:vf.zSoimiozRD6qdgHwfykp_w?version=6" , "code" : "ERR_RESOURCE_NOT_EXIST" , "title" : "The resource does not exist" , "detail" : "The resource XXX does not exist." } ] }
```
