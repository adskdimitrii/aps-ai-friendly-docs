# projects/{projectId}/packages/{packageId}/resources

Source: https://aps.autodesk.com/en/docs/acc/reference/http/packages-list-package-resources-GET/

---

# projects/{projectId}/packages/{packageId}/resources

Retrieves a list of file versions (âresourcesâ) within a specified package.

With two-legged authentication, returns all resources in the package. With two-legged authentication and the x-user-id header, or with three-legged authentication, returns only the resources the current user has permission to access.

The results include deleted files (indicated by isDeleted=true ), whether the file itself was deleted or its parent folder was deleted.

For information about adding files to a package, see the Add Files documentation.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/packages/v1/projects/{projectId}/packages/{packageId}/resources Authentication Context user context optional Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. x-user-id string The Autodesk ID of the user on whose behalf the request is made. This header is required only when using two-legged authentication. It is not needed for three-legged authentication. Your application can access only those users who are assigned to it in the SaaS Integrations UI. Only user Autodesk IDs ( autodeskId ) are supported.

This header is required only when using two-legged authentication. It is not needed for three-legged authentication.

Your application can access only those users who are assigned to it in the SaaS Integrations UI.

Only user Autodesk IDs ( autodeskId ) are supported.

### Request

## URI Parameters

projectId string: UUID The ID of the project. You can retrieve the project ID using the Data Management API . For more details, see the Retrieve a Project ID tutorial. You may provide the project ID with or without the b. prefix: With prefix: b.657a5565-09b7-48e0-bd03-acacfe42efaf Without prefix: 657a5565-09b7-48e0-bd03-acacfe42efaf packageId string: UUID The ID of the package. To find the package ID, call GET packages .

You can retrieve the project ID using the Data Management API . For more details, see the Retrieve a Project ID tutorial.

You may provide the project ID with or without the b. prefix:

- With prefix: b.657a5565-09b7-48e0-bd03-acacfe42efaf

- Without prefix: 657a5565-09b7-48e0-bd03-acacfe42efaf

To find the package ID, call GET packages .

### Request

## Query String Parameters

limit int The number of resources to return in the response payload. Possible values: 1-1000 . Default: 200 . For example: limit=2 . offset int The number of resources that you want to begin retrieving results from. Default: 0 . For example: offset=10 . filter[fileType] string Filter by file type. This can be a single value or a comma-separated list of values. For example: filter[fileType]=pdf,rvt . Refer to Supported Files for more details. filter[version] string Filter by file version number. This can be a single value or a comma-separated list of values. For example: filter[version]=1,2,3 sort enum:string Provide options to sort on single field, in ascending ( asc ) by default or descending ( desc ) order. Possible values of sorting field: name , description , updatedAt , approvalStatus , version . For example: sort=name desc .

Possible values: 1-1000 . Default: 200 . For example: limit=2 .

Default: 0 . For example: offset=10 .

For example: filter[fileType]=pdf,rvt . Refer to Supported Files for more details.

For example: filter[version]=1,2,3

Possible values of sorting field: name , description , updatedAt , approvalStatus , version . For example: sort=name desc .

### Response

## HTTP Status Code Summary

200 OK Successfully retrieved file versions in a package 400 Bad Request Bad request. The input parameters were invalid. 403 Forbidden Forbidden. The user does not have permission to access this resource. 404 Not Found Not found. The resource does not exist or is inaccessible. 500 Internal Server Error An unexpected server error occurred.

### Response

## Body Structure (200)

results array: object The list of results. urn string The ID (URN) of the file version in ACC. id string: UUID The unique identifier (UUID) of the file version. createdAt string The time and date the file version was created. createdBy string The Autodesk ID of the user who created the version. For details about the user, call GET users . createdByName string The name of the user who created the file version. updatedAt string The time and date when the file version was last modified. updatedBy string The Autodesk ID of the user who last modified the version. For details about the user, call GET users . updatedByName string The name of the user who last modified the file version. name string The file name in ACC Files. Max length: 255 description string The description of the file version. isDeleted boolean Indicates whether the file version has been deleted. true â The file version is deleted, either directly or because its parent folder was deleted. false â The file version is not deleted. entityType enum:string The type of file version. Possible values: SEED_FILE â A document that was not split into sheets when uploaded to ACC Files. DOCUMENT â A document that was split into sheets when uploaded to ACC Files. parentFolderUrn string The ID (URN) of the parent folder that contains the file version. storageUrn string The URN of the file versionâs storage object. customAttributes array: object A list of custom attributes assigned to the file version. For more information, see Customize Documents with Attributes . id int The unique identifier of the custom attribute. type enum:string The data type of the custom attribute. Possible values: string â Text field. date â Date field. array â Drop-down list. name string The name of the custom attribute. value string The value of the custom attribute. version int The version number of the resource in ACC Files. This number increases when the file is completely replaced (for example, re-uploaded and overwritten), not when it is merely updated or saved. approvalStatus object The approval status of the file version. For more information, see File Status documentation. id string The unique identifier of the approval status. label string The customized label of the approval status. Max length: 255 value string The value of the approval status. fileType string The file type of the version. For more details, see the Supported Files documentation. pagination object The pagination information for the response. This object is included when results are returned in multiple pages. limit int The maximum number of objects that may be returned in the page. offset int The offset from the start of the collection to the first entry in the page. It is zero-based. nextUrl string The URL to retrieve the next page of results. If not included, this is the last page of results. totalResults int The total number of results that match the query, regardless of the limit value.

Max length: 255

true â The file version is deleted, either directly or because its parent folder was deleted.

false â The file version is not deleted.

- SEED_FILE â A document that was not split into sheets when uploaded to ACC Files.

- DOCUMENT â A document that was split into sheets when uploaded to ACC Files.

For more information, see Customize Documents with Attributes .

- string â Text field.

- date â Date field.

- array â Drop-down list.

This number increases when the file is completely replaced (for example, re-uploaded and overwritten), not when it is merely updated or saved.

For more information, see File Status documentation.

Max length: 255

For more details, see the Supported Files documentation.

## Example

Successfully retrieved file versions in a package

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/packages/v1/projects/657a5565-09b7-48e0-bd03-acacfe42efaf/packages/c25d1273-41e3-4e04-be1e-f4c1ba809d14/resources?limit=200&filter[fileType]=pdf,rvt&filter[version]=1,2,3&sort=name' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "results" : [ { "urn" : "urn:adsk.wip:fs.file:vf.betLCOhhTF6o1ACTFdEbXA?version=1" , "id" : "f16e92f0-64be-4ae1-bcd6-dd2ad004c8d2" , "createdAt" : "2025-03-27T03:29:48.000Z" , "createdBy" : "L9VDREARJ7X2" , "createdByName" : "John Smith" , "updatedAt" : "2025-03-05T08:14:53.000Z" , "updatedBy" : "L9VDREARJ7X2" , "updatedByName" : "John Smith" , "name" : "101-BIMicon-CD-L2-DR-A-A40-010-R1.pdf" , "description" : "BIM icon CD L2 DR A40 010 R1" , "isDeleted" : false , "entityType" : "SEED_FILE" , "parentFolderUrn" : "urn:adsk.wip:fs.folder:co.rbR46ACySm6qdS4vAOdDDA" , "storageUrn" : "urn:adsk.objects:os.object:wip.dm.prod/c4a75bbc-24eb-41a3-a58b-48e51942222e.pdf" , "customAttributes" : [ { "id" : 123 , "type" : "array" , "name" : "Drawing Type" , "value" : "General" } ], "version" : 1 , "approvalStatus" : { "id" : "f44e623d-f04f-47fe-8195-efc43d1d985b" , "label" : "Approved" , "value" : "approved" }, "fileType" : "pdf" } ], "pagination" : { "limit" : 200 , "offset" : 0 , "nextUrl" : "https://developer.api.autodesk.com/construction/packages/v1/projects/657a5565-09b7-48e0-bd03-acacfe42efaf/packages/c25d1273-41e3-4e04-be1e-f4c1ba809d14/resources?limit=100&offset=200" , "totalResults" : 100 } }
```
