# projects/{projectId}/exports/{exportId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-exports-exportId-GET/

---

# projects/{projectId}/exports/{exportId}

Retrieves the status of a PDF sheet export job, as well as the signed URL required to download the exported file once the export process is complete.

To initiate a sheet export, use POST exports . This will return an export ID which should be used with this endpoint.

Note that only the authenticated user who initiated the export job can retrieve the signed URL using this endpoint. This signed URL will be available for one hour. If you need to download the file after this period, you will need to make another call to POST exports .

For more details about exporting sheets, see the Export Sheets tutorial.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/exports/{exportId} Authentication Context user context optional Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. x-user-id string The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2. You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId).

When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.

You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId).

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial . You can use a project ID either with a âb.â prefix or without a âb.â prefix. For instance, a project ID of âb.a4be0c34a-4ab7â can also be referred to as âa4be0c34a-4ab7â. exportId string The ID of the export job. The export ID is generated when you initialize an export job using POST exports .

### Response

## HTTP Status Code Summary

200 OK Successfully retrieved export data 400 Bad Request The parameters of the requested operation are invalid. Sample error code with possible messages: ERR_BAD_INPUT: Failed to parse the token 401 Unauthorized The provided bearer token is not valid. Sample error code with possible messages: ERR_AUTHENTICATED_ERROR: Authentication header is not correct 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. Sample error code with possible messages: ERR_NOT_ALLOWED: Account inactive Project inactive User inactive API access denied User {userId} does not have download permission on resource {resource} 404 Not Found The requested resources, such as the project, account, user, sheet, or job, do not exist. Sample error code with possible messages: ERR_RESOURCE_NOT_EXIST: Project not found Project user not found The job does not exist 500 Internal Server Error An unknown error occurred on the server. Sample error code with possible messages: ERR_INTERNAL_SERVER_ERROR: Request failed for internal exception xxx Failed to get account Failed to get project Failed to get user

Sample error code with possible messages:

- ERR_BAD_INPUT: Failed to parse the token

- Failed to parse the token

Sample error code with possible messages:

- ERR_AUTHENTICATED_ERROR: Authentication header is not correct

- Authentication header is not correct

Sample error code with possible messages:

- ERR_NOT_ALLOWED: Account inactive Project inactive User inactive API access denied User {userId} does not have download permission on resource {resource}

- Account inactive

- Project inactive

- User inactive

- API access denied

- User {userId} does not have download permission on resource {resource}

Sample error code with possible messages:

- ERR_RESOURCE_NOT_EXIST: Project not found Project user not found The job does not exist

- Project not found

- Project user not found

- The job does not exist

Sample error code with possible messages:

- ERR_INTERNAL_SERVER_ERROR: Request failed for internal exception xxx Failed to get account Failed to get project Failed to get user

- Request failed for internal exception xxx

- Failed to get account

- Failed to get project

- Failed to get user

### Response

## Body Structure (200)

id string: UUID The ID of the sheets export job. status enum:string The status of the sheets export job.
Possible values: successful , processing , failed result object The result of a completed export job. If the status is successful , a downloadable signed URL will be included in the result.output object. If the status value is failed (e.g., because some files were deleted), the result.error object will include details of the error. output object Details about the downloadable signed URL. signedUrl string The signed URL that you can use to download the PDF file. Note that it expires in one hour. error object Information about the error. code string The code of the error. title string The title of the error. detail string The details of the error.

- If the status is successful , a downloadable signed URL will be included in the result.output object.

- If the status value is failed (e.g., because some files were deleted), the result.error object will include details of the error.

## Example

Successfully retrieved export data

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/exports/5b4bb914-c123-4f10-87e3-579ef934aaf9' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response (200 with signedUrl)

```
{ "id" : "5b4bb914-c123-4f10-87e3-579ef934aaf9" , "status" : "successful" , "result" : { "output" : { "signedUrl" : "https://signedUrl" } } }
```

### Response (200 with failed result)

```
{ "id" : "5b4bb914-c123-4f10-87e3-579ef934aaf9" , "status" : "failed" , "result" : { "error" : { "code" : "401" , "title" : "ERR_AUTHORIZATION_ERROR" , "detail" : "Authentication header is not correct" } } }
```
