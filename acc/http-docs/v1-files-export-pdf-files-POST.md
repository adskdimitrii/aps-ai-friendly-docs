# projects/{projectId}/exports

Source: https://aps.autodesk.com/en/docs/acc/reference/http/v1-files-export-pdf-files-POST/

---

# projects/{projectId}/exports

Exports one or more individual PDFs, or 2D views and sheets (from DWG or RVT files) as PDFs from the ACC files module. All PDFs are packaged into a single ZIP file.

Notes:

- A maximum of 200 files may be exported in a single operation (in a ZIP file).

- For DWG files, 2D views can only be exported from DWG files uploaded after May 1, 2023.

- For RVT files, 2D views and sheets can only be exported from RVT files created with Revit 2022 or newer versions. The name of each sheet or view in the exported result is a combination of the type, level name, and sheet/view name, e.g., Sheets - A001, Views - Structure Plan - A001.

The files can be exported once theyâve been successfully uploaded and processed. For more details about uploading files, see the Upload Files help documentation. For DWG or RVT file, if it is not processed completely, the exporting will skip it and the status will be partialSuccess .

A user must have at least download permission to perform this export operation. For more information about permissions, see the Folder Permissions help documentation.

The file created for export is specified by a file version ID, which identifies a specific version of the file. For how to get version ID, see the tutorial Export Files .

Exporting markups and links:

- You can export files with both standard markups and feature markups (Issues and Photos are the currently supported features). For more information about feature markups, see the Feature Markups and Measurement help documentation.

- For each markup type (standard, Issues, and Photos), you can specify whether to export published markups, unpublished markups, or both. For more information about published and unpublished markups, see the Create and Style Markups help documentation.

- With standard markups, you can also specify whether to include attached links. For more information about markups links, see the Markups Links and References help documentation.

Note that this endpoint is asynchronous and initiates a job that runs in the background, rather than halting execution of your program. The response returns an export ID that you can use to poll GET /projects/{projectId}/exports/{exportId} to verify the status of the job. When the job is completed, an S3 signed url will be available for downloading the exported result.

For more details about exporting files, see the Export Files tutorial.

Note that this endpoint is not compatible with BIM 360 projects. For BIM 360 projects use POST versions/{version_id}/exports .

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/files/v1/projects/{projectId}/exports Authentication Context user context optional Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. x-user-id string The ID of a user on whose behalf your API request is acting. Required if youâre using a 2-legged authentication context, which must be 2-legged OAuth2 security with user impersonation. The app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified. You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId). Content-Type * string Must be application/json

The app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified.

You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId).

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial . You can use a project ID either with a âb.â prefix or without a âb.â prefix. For instance, a project ID of âb.a4be0c34a-4ab7â can also be referred to as âa4be0c34a-4ab7â.

### Request

## Body Structure

The request body includes the URNs of the file versions to export, and the types of markups to include with the exported files.

options object The criteria for the markups and links to include with the exported files. Note that unpublished markups are those visible only to their creator. outputFileName string The name of the file that will be produced by the export operation. This should not include the filename extension. standardMarkups object The options for which standard markups and associated links to export. No markups or links will be exported if all options are set to false . includePublishedMarkups boolean true : (Default) Include all published standard markups in the exported files. Note that published markups are visible to all project members. false : Export files without including any published standard markups. includeUnpublishedMarkups boolean true : (Default) Include in the exported files all standard markups that are only visible to their creators. false : Export files without including unpublished markups. includeMarkupLinks boolean true : Include with each exported file the supported type reference links added to its markups. Supported links are links to Sheets, Files, RFIs, Forms, Submittals, and Assets. false : (Default) Export files without any reference links. Note that this parameter will be treated as false if the values of includePublishedMarkups and includeUnpublishedMarkups are both false . issueMarkups object The options for which Issues markups to export. No Issues markups will be exported if both options are set to false . includePublishedMarkups boolean true : Include all published Issues markups in the exported files. false : (Default) Export files without including any published Issues markups. includeUnpublishedMarkups boolean true : Include in the exported files all Issues markups that are only visible to their creators or assignees. false : (default) Export files without including any unpublished Issues markups. photoMarkups object The options for which Photos markups to export. No Photos markups will be exported if both options are set to false . includePublishedMarkups boolean true : Include all published Photos markups in the exported files. false : (Default) Export files without including any published Photos markups. includeUnpublishedMarkups boolean true : Include in the exported files all Photos markups that are only visible to their creators or assignees. false : (default) Export files without including any unpublished Photos markups. fileVersions * array: string A list of file version URNs. A maximum of 200 files may be included.

Note that unpublished markups are those visible only to their creator.

No markups or links will be exported if all options are set to false .

false : Export files without including any published standard markups.

false : Export files without including unpublished markups.

false : (Default) Export files without any reference links.

Note that this parameter will be treated as false if the values of includePublishedMarkups and includeUnpublishedMarkups are both false .

No Issues markups will be exported if both options are set to false .

false : (Default) Export files without including any published Issues markups.

false : (default) Export files without including any unpublished Issues markups.

No Photos markups will be exported if both options are set to false .

false : (Default) Export files without including any published Photos markups.

false : (default) Export files without including any unpublished Photos markups.

### Response

## HTTP Status Code Summary

202 Accepted Successfully created an export job. 400 Bad Request The parameters of the requested operation are invalid. Sample error code with possible messages: ERR_BAD_INPUT: Multiple documents only can be exported as a ZIP file. 2D views and sheets in DWG or RVT format can only be exported as a ZIP file. Some resources are not valid types (only PDF, DWG, and RVT are accepted). 401 Unauthorized The provided bearer token is not valid. Sample error code with possible messages: ERR_AUTHENTICATED_ERROR: Authentication header is not correct 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. Sample error code with possible messages: ERR_NOT_ALLOWED: Account inactive Project inactive User inactive Api access deny User {userId} does not have download permission on resource {resource} 404 Not Found The resources requested, e.g. project, account, user, and any files included, do not exist. Sample error code with possible messages: ERR_RESOURCE_NOT_EXIST: Some resources are not found Account not found Project not found Project user not found 422 Unprocessable Entity The total file size exceeds the 10GB maximum limit. Sample error code with possible messages: ERR_FILES_TOO_LARGE: The overall file size is over 10GB. 500 Internal Server Error An unknown error occurred on the server. Sample error code with possible messages: ERR_INTERNAL_SERVER_ERROR: Request failed for internal exception xxx Failed to get account Failed to get project Failed to get user

Sample error code with possible messages:

- ERR_BAD_INPUT: Multiple documents only can be exported as a ZIP file. 2D views and sheets in DWG or RVT format can only be exported as a ZIP file. Some resources are not valid types (only PDF, DWG, and RVT are accepted).

- Multiple documents only can be exported as a ZIP file.

- 2D views and sheets in DWG or RVT format can only be exported as a ZIP file.

- Some resources are not valid types (only PDF, DWG, and RVT are accepted).

Sample error code with possible messages:

- ERR_AUTHENTICATED_ERROR: Authentication header is not correct

- Authentication header is not correct

Sample error code with possible messages:

- ERR_NOT_ALLOWED: Account inactive Project inactive User inactive Api access deny User {userId} does not have download permission on resource {resource}

- Account inactive

- Project inactive

- User inactive

- Api access deny

- User {userId} does not have download permission on resource {resource}

Sample error code with possible messages:

- ERR_RESOURCE_NOT_EXIST: Some resources are not found Account not found Project not found Project user not found

- Some resources are not found

- Account not found

- Project not found

- Project user not found

Sample error code with possible messages:

- ERR_FILES_TOO_LARGE: The overall file size is over 10GB.

- The overall file size is over 10GB.

Sample error code with possible messages:

- ERR_INTERNAL_SERVER_ERROR: Request failed for internal exception xxx Failed to get account Failed to get project Failed to get user

- Request failed for internal exception xxx

- Failed to get account

- Failed to get project

- Failed to get user

### Response

## Body Structure (202)

id string: UUID The ID of the PDF export job. status enum:string The status of the PDF export job.
Possible values: successful , processing , failed

## Example

Successfully created an export job.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/files/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/exports' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "options": { "outputFileName": "output_file_name", "standardMarkups": { "includePublishedMarkups": true, "includeUnpublishedMarkups": true, "includeMarkupLinks": false }, "issueMarkups": { "includePublishedMarkups": false, "includeUnpublishedMarkups": false }, "photoMarkups": { "includePublishedMarkups": false, "includeUnpublishedMarkups": false } }, "fileVersions": [ "urn:adsk.wip.file:vf.fileId?version=2" ] }'
```

### Response

```
{ "id" : "636e6a96-d4d2-43e6-b67a-db8618fc0ff9" , "status" : "processing" }
```
