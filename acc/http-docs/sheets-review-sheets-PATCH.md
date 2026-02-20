# projects/{projectId}/uploads/{uploadId}/review-sheets

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-review-sheets-PATCH/

---

# projects/{projectId}/uploads/{uploadId}/review-sheets

Updates review sheets.

This endpoint is typically used during the process of uploading files to the ACC sheets tool. It enables you to update the review the sheets that you uploaded before publishing them. For more details, see the Upload Sheets tutorial.

Note that in order to update a review sheet, it needs to have been fully processed, i.e., it should have a READY status. To check the process status, call GET review-sheets .

## Resource Information

Method and URI PATCH https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/uploads/{uploadId}/review-sheets Authentication Context user context optional Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. x-user-id string The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2. You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId). Content-Type * string Must be application/json

When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.

You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId).

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial . You can use a project ID either with a âb.â prefix or without a âb.â prefix. For instance, a project ID of âb.a4be0c34a-4ab7â can also be referred to as âa4be0c34a-4ab7â. uploadId string The ID of the upload. The upload ID is generated when you create an upload object .

### Request

## Body Structure

id * string The ID of the review sheet to update. number string The new number of the review sheet. Note the following limitations: The number should not contain these reserved characters: < , > , : , " , / , \\ , | , ? , * , \n , \r , \t , \0 , \f , ' . You cannot assign the following reserved names to the number: CON, PRN, AUX, NUL, COM1, COM2, COM3, COM4, COM5, COM6, COM7, COM8, COM9, LPT1, LPT2, LPT3, LPT4, LPT5, LPT6, LPT7, LPT8, and LPT9. You cannot put a period at the end of the number. The number should not be space only. The max length is 255. The API will format the number in the following ways before applying it to the review sheet: Remove spaces at the end and beginning of the number. Reduce multiple continuous spaces to a single space. Max length: 255 title string The new title of the review sheet. The title should not be space only. The max length is 255. The API will format the title in the following ways before applying it to the review sheet: Remove spaces at the end and beginning of the title. Reduce multiple continuous spaces to a single space. Max length: 255 deleted boolean true if you want to delete the review sheet. false if you want to restore the review sheet. Note that if the review sheet has been deleted, it will not be published. tags array: string The new tags of the review sheet. The max length is 100. The tags should not be space only. The max number of items is 50. The API will format the tags in the following ways before applying them to the review sheet: Remove spaces at the end and beginning of the tags. Reduce multiple continuous spaces to a single space. The tags are case insensitive. Upper case letters will be transformed to lower case. Note that the tags that you specify overwrite existing tags.

- The number should not contain these reserved characters: < , > , : , " , / , \\ , | , ? , * , \n , \r , \t , \0 , \f , ' .

- You cannot assign the following reserved names to the number: CON, PRN, AUX, NUL, COM1, COM2, COM3, COM4, COM5, COM6, COM7, COM8, COM9, LPT1, LPT2, LPT3, LPT4, LPT5, LPT6, LPT7, LPT8, and LPT9.

- You cannot put a period at the end of the number.

- The number should not be space only.

- The max length is 255.

The API will format the number in the following ways before applying it to the review sheet:

- Remove spaces at the end and beginning of the number.

- Reduce multiple continuous spaces to a single space.

Max length: 255

- The title should not be space only.

- The max length is 255.

The API will format the title in the following ways before applying it to the review sheet:

- Remove spaces at the end and beginning of the title.

- Reduce multiple continuous spaces to a single space.

Max length: 255

- true if you want to delete the review sheet.

- false if you want to restore the review sheet.

Note that if the review sheet has been deleted, it will not be published.

- The max length is 100.

- The tags should not be space only.

- The max number of items is 50.

The API will format the tags in the following ways before applying them to the review sheet:

- Remove spaces at the end and beginning of the tags.

- Reduce multiple continuous spaces to a single space.

- The tags are case insensitive. Upper case letters will be transformed to lower case.

Note that the tags that you specify overwrite existing tags.

### Response

## HTTP Status Code Summary

200 OK Successfully updated the review sheets. 400 Bad Request The parameters of the requested operation are invalid. 403 Forbidden The user or client represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource cannot be found. 429 Too Many Requests The server has received too many requests. 500 Internal Server Error An unexpected error occurred on the server.

### Response

## Body Structure (200)

results array: object The list of results. id string The ID of the review sheet. page number The page number of the source file from which the review sheet was generated. fileName string The source file name of the review sheet. number string The number of the review sheet. title string The title of the review sheet. deleted boolean true if the review sheet has been deleted. false if the review sheet has not been deleted. Note that if the review sheet has been deleted, it will not be published. tags array: string The tags of the review sheet. rotation number The rotation of the review sheet. Possible values: 0 , 90 , 180 , 270 . processingState enum:string The processing state of the review sheet. Possible values: PROCESSING : the review sheet is being processed. AUDITING : the review sheet is being audited. ROTATING : the review sheet is being rotated. READY : the review sheet is ready for updating or publishing. FAILED : the processing of the review sheet failed. PUBLISHING the review sheet is publishing.

- true if the review sheet has been deleted.

- false if the review sheet has not been deleted.

Note that if the review sheet has been deleted, it will not be published.

- PROCESSING : the review sheet is being processed.

- AUDITING : the review sheet is being audited.

- ROTATING : the review sheet is being rotated.

- READY : the review sheet is ready for updating or publishing.

- FAILED : the processing of the review sheet failed.

- PUBLISHING the review sheet is publishing.

## Example

Successfully updated the review sheets.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/uploads/5cb5d9da-060e-421e-bca9-97dd8b5cd800/review-sheets' \ -X 'PATCH' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '[ { "id": "0d7a5883-1694-3078-a06d-ad24413f8b06", "number": "A-01", "title": "Floor One", "deleted": false, "tags": [ "april", "floor" ] } ]'
```

### Response

```
{ "results" : [ { "id" : "0d7a5883-1694-3078-a06d-ad24413f8b06" , "page" : 1 , "fileName" : "example.pdf" , "number" : "A-01" , "title" : "Floor One" , "deleted" : false , "tags" : [ "april" , "floor" ], "rotation" : 0 , "processingState" : "READY" } ] }
```
