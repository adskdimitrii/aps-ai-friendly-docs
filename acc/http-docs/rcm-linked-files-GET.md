# construction/rcm/v1/projects/{projectId}/published-versions/{versionId}/linked-files

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rcm-linked-files-GET/

---

# construction/rcm/v1/projects/{projectId}/published-versions/{versionId}/linked-files

Retrieves metadata and signed download URLs for a published version of a Revit (RVT) cloud model, whether workshared or non-workshared, and any Revit files linked to it.

You can also use this endpoint to retrieve a temporary download link for a specific published host model version, even if it has no linked models.

This API is only supported for models published after February 7, 2025.

The Authorization header token can be obtained through either the three-legged OAuth flow or the two-legged OAuth flow with user impersonation, which requires the x-user-Id header.

For details on how to use this endpoint, see the Download RVT Files from a Published Model tutorial.

Note that for a 3-legged OAuth flow or for a 2-legged OAuth flow with user impersonation ( x-user-id ), the user must have at least download permission to the Revit (RVT) cloud model.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/rcm/v1/projects/{projectId}/published-versions/{versionId}/linked-files Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. x-user-id string The ID of the user on whose behalf the request is made. This header is only required when using two-legged authentication with user impersonation. It is not needed for three-legged authentication. By providing this header, the API call is limited to act on behalf of the user specified. The user must have at least download permission to the host model. Your application can act on behalf of any user who has been authorized in the SaaS Integrations UI. You can only provide the userâs Autodesk ID ( autodeskId ) as the value of this header.

By providing this header, the API call is limited to act on behalf of the user specified. The user must have at least download permission to the host model.

Your application can act on behalf of any user who has been authorized in the SaaS Integrations UI. You can only provide the userâs Autodesk ID ( autodeskId ) as the value of this header.

### Request

## URI Parameters

projectId string The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You can provide the project ID with or without the â b. " prefix. Example with prefix: b.563a4c30-e30d-4869-ac02-2a18b6447abe Example without prefix: 563a4c30-e30d-4869-ac02-2a18b6447abe versionId string The URL-encoded version ID (URN) of the published Revit model version for which you want to retrieve linked files. When a Cloud Workshared Revit model is published in BIM 360 or the Autodesk Construction Cloud (ACC), a new version ID is created for each published Revit model version. Every time a model is updated and published, it receives a new unique version ID. You must provide a version ID to retrieve the linked files for that specific published Revit model version. To retrieve the latest ( tip ) version ID, use GET projects/:project_id/folders/:folder_id/contents . To filter out non-cloud workshared Revit files, use the items:autodesk.bim360:C4RModel filter . To retrieve a specific past version, use GET projects/:project_id/items/:item_id/versions . For more details about retrieving the version ID, see the Retrieve Signed URLs for Linked RVT Files tutorial.

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You can provide the project ID with or without the â b. " prefix.

- Example with prefix: b.563a4c30-e30d-4869-ac02-2a18b6447abe

- Example without prefix: 563a4c30-e30d-4869-ac02-2a18b6447abe

When a Cloud Workshared Revit model is published in BIM 360 or the Autodesk Construction Cloud (ACC), a new version ID is created for each published Revit model version.

Every time a model is updated and published, it receives a new unique version ID.

You must provide a version ID to retrieve the linked files for that specific published Revit model version.

To retrieve the latest ( tip ) version ID, use GET projects/:project_id/folders/:folder_id/contents . To filter out non-cloud workshared Revit files, use the items:autodesk.bim360:C4RModel filter .

To retrieve a specific past version, use GET projects/:project_id/items/:item_id/versions .

For more details about retrieving the version ID, see the Retrieve Signed URLs for Linked RVT Files tutorial.

### Request

## Query String Parameters

limit int The maximum number of linked models to return in a single request. Maxium: 600 . Default: 600 . offset int The index at which the endpoint starts returning results. Used for pagination. Default: 0 . This is a zero-based index (if set to 100 , results start from the 101st entry). filter object Specifies criteria for filtering the linked files by name or publish status. Filter by file name: Example: filter[name]=StructuralModel_2023.rvt&filter[name]=ArchitecturalModel_2023.rvt Filter by publish status: Published files: filter[publishStatus]=published Unpublished files: filter[publishStatus]=notPublished Both published and unpublished: filter[publishStatus]=published,notPublished includeHost boolean Indicates whether to include the signed URL for the host model in the response. true (default): the host modelâs signed URL is included. false : only includes the signed URLs of the linked files.

This is a zero-based index (if set to 100 , results start from the 101st entry).

- Filter by file name: Example: filter[name]=StructuralModel_2023.rvt&filter[name]=ArchitecturalModel_2023.rvt

- Example: filter[name]=StructuralModel_2023.rvt&filter[name]=ArchitecturalModel_2023.rvt

- Filter by publish status: Published files: filter[publishStatus]=published Unpublished files: filter[publishStatus]=notPublished Both published and unpublished: filter[publishStatus]=published,notPublished

- Published files: filter[publishStatus]=published

- Unpublished files: filter[publishStatus]=notPublished

- Both published and unpublished: filter[publishStatus]=published,notPublished

true (default): the host modelâs signed URL is included.

false : only includes the signed URLs of the linked files.

### Response

## HTTP Status Code Summary

200 OK OK, Success. 400 Bad Request Bad request. The request contained invalid parameters or malformed syntax. 401 Unauthorized Unauthorized. The request is missing authentication credentials or contains an invalid authorization token. 403 Forbidden Forbidden. The user does not have permission to access the project or requested version. 404 Not Found Not found. The requested version does not exist or was published before this feature was released. 500 Internal Server Error Internal server error. An unexpected error occurred while processing the request.

### Response

## Body Structure (200)

hostFile object Metadata about the host model (the main Revit model that contains linked files). This object is only returned in the response when includeHost is set to true . modelName string The name of the host model. signedUrl string A temporary URL used to download the host model. Signed URLs are valid for 1 hour. itemId string The URN of the host model. versionId string The version ID of the host model. size int The file size of the host model in bytes. publishStatus enum:string Indicates whether the host model has been published. Possible values: published â The model has been published. notPublished â The model has not been published. linkedFiles object A list of linked Revit (RVT) models associated with the requested published model version.
This object contains a list of linked files and pagination details. pagination object Contains pagination details, including the number of results, starting offset, and total available results. limit int The number of results returned in this response. This may be lower than the requested limit if fewer results are available. offset int The index of the first result in the response, based on the requested offset value. nextUrl string A URL for retrieving the next page of results. If this field is not included, there are no additional pages. A page may be empty but still include a nextUrl , so continue paging until this field is no longer returned. nextOffset int The offset value to use when requesting the next page. This field is useful for clients that build the request URL manually instead of using the nextUrl link. totalResults int The total number of linked files available for the requested published version. results array: object File information about each linked model. This collection is paginated according to the limit and offset parameters. modelName string The name of the linked model, as referenced within the host model. signedUrl string A temporary URL used to download the linked model. Signed URLs are valid for 1 hour. itemId string The URN of the linked model. versionId string The version ID of the linked model. If the model is unpublished, this field is omitted from the response. publishStatus enum:string Indicates whether the linked model has been published. Possible values: published â The model has been published. notPublished â The model has not been published.

published â The model has been published.

notPublished â The model has not been published.

published â The model has been published.

notPublished â The model has not been published.

## Example

OK, Success.

### Request

```
curl -v 'https://developer.api.autodesk.com//construction/rcm/v1/projects/563a4c30-e30d-4869-ac02-2a18b6447abe/published-versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.b909RzMKR4mhc3O7UBY_8g%3Fversion%3D2/linked-files?limit=100&offset=200&includeHost=true' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "hostFile" : { "modelName" : "Arch.rvt" , "signedUrl" : "https://cdn.us.oss.api.autodesk.com/com.autodesk.oss-persistent/us-east-1/3f/bf/5f/0137a7d9dc53af930bc1b527320d50fb5f/wip.dm.prod?response-content-type=application%2Foctet-stream&response-content-disposition=attachment%3B+filename%3D%977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt%22&Expires=1643864703&Signature=00PZYS6gL~Nc6aRG2HAhOCKYl0xtqsuujMJ~VKSXm1vBa-OxS4lPQBSlTx5bswpLBe1W6Rz94eIZW2sPN-v6Mzz~JyXNZ-V9Z7zlBoE1VoQhspLioC225hxq6ZmDSU5QnZXuNDV4ih~p1n3xacYvUvQWX-ONAGVUgQvZ253Svw~qx-pO4j-Yh4kVRmzDZqQut1xOI5ZGH6JFGhXLSzkgbYcfYx6fvCxnvYUJrgAcqncIwGVewI3uC0I84Fzrj8nXE8ojuojqJP0pNlxkfBe~2LfjjzqKDKaNvfC2Grt12j9QgC~cN7nQCRcVUhExpoV1VVB5x3AkVTJ-q5NoedvsfO__&Key-Pair-Id=95HRZD7MMO1UK" , "itemId" : "urn:adsk.wipprod:dm.lineage:f909RzMKR4mhc3O7UBY_3g" , "versionId" : "urn:adsk.wipprod:fs.file:vf.f909RzMKR4mhc3O7UBY_3g?version=2" , "size" : 2003 , "publishStatus" : "published" }, "linkedFiles" : { "pagination" : { "limit" : 100 , "offset" : 200 , "nextUrl" : "https://developer.api.autodesk.com/construction/rcm/v1/projects/563a4c30-e30d-4869-ac02-2a18b6447abe/published-versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.b909RzMKR4mhc3O7UBY_8g%3Fversion%3D2/linked-files?offset=300&limit=100" , "nextOffset" : 300 , "totalResults" : 305 }, "results" : [ { "modelName" : "StructuralModel_2023.rvt" , "signedUrl" : "https://cdn.us.oss.api.autodesk.com/com.autodesk.oss-persistent/us-east-1/3f/bf/5f/0137a7d9dc53af930bc1b527320d50fb5f/wip.dm.prod?response-content-type=application%2Foctet-stream&response-content-disposition=attachment%3B+filename%3D%977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt%22&Expires=1643864703&Signature=00PZYS6gL~Nc6aRG2HAhOCKYl0xtqsuujMJ~VKSXm1vBa-OxS4lPQBSlTx5bswpLBe1W6Rz94eIZW2sPN-v6Mzz~JyXNZ-V9Z7zlBoE1VoQhspLioC225hxq6ZmDSU5QnZXuNDV4ih~p1n3xacYvUvQWX-ONAGVUgQvZ253Svw~qx-pO4j-Yh4kVRmzDZqQut1xOI5ZGH6JFGhXLSzkgbYcfYx6fvCxnvYUJrgAcqncIwGVewI3uC0I84Fzrj8nXE8ojuojqJP0pNlxkfBe~2LfjjzqKDKaNvfC2Grt12j9QgC~cN7nQCRcVUhExpoV1VVB5x3AkVTJ-q5NoedvsfO__&Key-Pair-Id=95HRZD7MMO1UK" , "itemId" : "urn:adsk.wipprod:dm.lineage:XYZ123003443we" , "versionId" : "urn:adsk.wipprod:fs.file:vf.e7r4RzMKR4mhc3Oc4y6?version=1" , "publishStatus" : "published" } ] } }
```
