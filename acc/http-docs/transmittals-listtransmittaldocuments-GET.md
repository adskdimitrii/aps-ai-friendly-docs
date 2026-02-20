# projects/{projectId}/transmittals/{transmittalId}/documents

Source: https://aps.autodesk.com/en/docs/acc/reference/http/transmittals-listtransmittaldocuments-GET/

---

# projects/{projectId}/transmittals/{transmittalId}/documents

Retrieves the documents that were included in a specific transmittal.

The response returns the exact versions of the documents as they existed when the transmittal was issued.

If the transmittal is still being processed, the endpoint temporarily returns status code 202 until the document list becomes available.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/transmittals/v1/projects/{projectId}/transmittals/{transmittalId}/documents Authentication Context user context optional Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. x-user-id string The Autodesk ID of the user on whose behalf the request is made. This header is required only when using two-legged authentication. It is not needed for three-legged authentication. Your application can access only those users who are assigned to it in the SaaS Integrations UI. Only user Autodesk IDs ( autodeskId ) are supported.

This header is required only when using two-legged authentication. It is not needed for three-legged authentication.

Your application can access only those users who are assigned to it in the SaaS Integrations UI.

Only user Autodesk IDs ( autodeskId ) are supported.

### Request

## URI Parameters

projectId string: UUID The ID of the project. You can retrieve the project ID using the Data Management API . For more details, see the Retrieve a Project ID tutorial. You may provide the project ID with or without the b. prefix: With prefix: b.657a5565-09b7-48e0-bd03-acacfe42efaf Without prefix: 657a5565-09b7-48e0-bd03-acacfe42efaf transmittalId string: UUID The ID of the transmittal. To find the ID, call GET transmittals .

You can retrieve the project ID using the Data Management API . For more details, see the Retrieve a Project ID tutorial.

You may provide the project ID with or without the b. prefix:

- With prefix: b.657a5565-09b7-48e0-bd03-acacfe42efaf

- Without prefix: 657a5565-09b7-48e0-bd03-acacfe42efaf

### Request

## Query String Parameters

limit int The maximum number of results to return per page. Acceptable values: 1-200. Default value: 20. For example, to limit the response to two results per page, use limit=2 . offset int The index from which the response starts returning results. Default value: 0. For example, to skip the first three results, use offset=3 . sort enum:string Sorts the document results by a supported field and order. By default, results are sorted in ascending order by name ( name asc ). To sort in descending order, add desc after the field name. Format: sort=<field> [asc or desc] Possible values: name , title , version , lastUpdatedAt , updatedByName . Examples: sort=name asc â sorts documents alphabetically by name. sort=lastUpdatedAt desc â sorts documents by last update time (newest first).

Acceptable values: 1-200.

Default value: 20.

For example, to limit the response to two results per page, use limit=2 .

Default value: 0.

For example, to skip the first three results, use offset=3 .

By default, results are sorted in ascending order by name ( name asc ).

To sort in descending order, add desc after the field name.

Format: sort=<field> [asc or desc]

Possible values: name , title , version , lastUpdatedAt , updatedByName .

Examples:

- sort=name asc â sorts documents alphabetically by name.

- sort=lastUpdatedAt desc â sorts documents by last update time (newest first).

### Response

## HTTP Status Code Summary

200 OK Successfully retrieved the documents included in the transmittal 202 Accepted The transmittal has been created and is currently being processed but not ready for review yet. The documents list will be empty. 400 Bad Request Operation failed because of bad user input 401 Unauthorized Unauthorized error 403 Forbidden The user does not have permission to perform this operation. 404 Not Found The project or transmittal does not exist 500 Internal Server Error Internal server error

### Response

## Body Structure (200)

results array: object The list of documents that were included in the transmittal when it was issued. urn string The URN of the document. name string The name of the document. description string The description of the document, if provided. title string The title of the document. version int The version number of the document at the time the transmittal was issued. fileName string The file name of the document. approveStatus object The approval status of the file version. For more information, see File Review Statuses documentation. label string The customized label of the approval status. Max length: 255 value enum:string The value of the approval status.
Possible values: APPROVED , REJECTED lastUpdatedAt datetime: ISO 8601 The date and time when the file was last updated, in ISO 8601 format. updatedByName string The name of the user who last modified the document. updatedBy string The Autodesk ID of the user who created the file. For details about the user, call GET user . isDeleted boolean Indicates whether the file is deleted. true â The file is deleted, either directly or because its parent folder was deleted. false â The file is not deleted. parentFolderUrn string The URN of the folder that contains the document. folderType string The type of folder that contains the document. revisionLabel string The revision label assigned to the document. storageUrn string The storage URN of the document. You can use the storage URN to download the document. For details, see the Download Files tutorial. pagination object The list of pagination details for the response. limit int The maximum number of results returned per page. offset int The number of results skipped before the current page, starting from zero. totalResults int The total number of results that match the query, regardless of pagination. nextUrl string The URL to retrieve the next page of transmittal documents. If this field is not included, the current page is the last page.

For more information, see File Review Statuses documentation.

Max length: 255

true â The file is deleted, either directly or because its parent folder was deleted.

false â The file is not deleted.

### Response

## Body Structure (202)

results array: object This list of results will be empty.

## Example

Successfully retrieved transmittal documents

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/transmittals/v1/projects/657a5565-09b7-48e0-bd03-acacfe42efaf/transmittals/88c286a3-4100-4251-8d0e-830e7726fc17/documents' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response (200)

```
{ "results" : [ { "urn" : "urn:adsk.wipprod:fs.file:vf.jM1_OeAjRL6OWjKQLR3cMg?version=1" , "name" : "Building_Design.pdf" , "description" : "This is a pdf of building design" , "title" : "building design" , "version" : 1 , "fileName" : "Building_Design.pdf" , "approveStatus" : { "label" : "Approved w/ comments." , "value" : "APPROVED" }, "lastUpdatedAt" : "2024-10-21T08:05:54.000Z" , "updatedByName" : "John Smith" , "updatedBy" : "HWUBNU689CRH" , "isDeleted" : false , "parentFolderUrn" : "urn:adsk.wipprod:fs.folder:co.plHRTgMySeK-DIMyDe7aSA" , "folderType" : "normal" , "revisionLabel" : "432" , "storageUrn" : "urn:adsk.objects:os.object:wip.dm.prod?afedb9a6-749c-45cc-9f44-6617cea3a2fd.f3d" } ], "pagination" : { "limit" : 1 , "offset" : 0 , "totalResults" : 10 , "nextUrl" : "https://developer.api.autodesk.com/construction/transmittals/v1/projects/657a5565-09b7-48e0-bd03-acacfe42efaf/transmittals/88c286a3-4100-4251-8d0e-830e7726fc17/documents?limit=1&offset=1" } }
```

### Response (202 when transmittal is being processed)

```
{ "results" : [], "pagination" : { "limit" : 1 , "offset" : 0 , "totalResults" : 0 , "nextUrl" : null } }
```
