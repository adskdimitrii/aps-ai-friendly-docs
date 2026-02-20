# projects/{projectId}/item-types

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-item-types-GET/

---

# projects/{projectId}/item-types

Retrieves all submittal itme types for the specified project. Submittal item types categorize the various submittal items submitted for review and approval in a construction project. Examples of submittal item types could be Attic Stock or Sample.

For more information about submittal item types, see the Help documentation .

For details on using submittal item types, refer to the Create Submittal Item tutorial.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/item-types Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Request

## Query String Parameters

limit int The maximum number of results per page. Possible values: 1 - 50 . Default value: 20 . For example, to limit the response to two results per page, use limit=2 . offset int The number of results to skip before starting to return data. For example, to skip the first 20 results, include offset=20 in the query string. For more details, see the JSON API Paging Help documentation .

### Response

## HTTP Status Code Summary

200 OK A list of item types. 401 Unauthorized Invalid or missing authorization header. Verify the Bearer token and try again. 403 Forbidden The user is not authorized to perform this action. 404 Not Found The specified resource was not found. 500 Internal Server Error An unexpected error occurred on the server while processing the request.

### Response

## Body Structure (200)

pagination object Describes pagination details for the response, including information about the current page and navigation to other pages. limit int The maximum number of results to be displayed on each page. offset int The number of results skipped before starting the current page. totalResults int The overall count of results available across all pages. previousUrl string The URL to retrieve the preceding page of results, if applicable. Not returned on the first page of results. nextUrl string The URL to retrieve the subsequent page of results, if available. If not included, this is the last page of data. results array: object The list of submittal types. id string: UUID The internal, globally unique identifier (UUID) for the item type. key string Not relevant value string The name of the submittal item type. platformId string Not relevant isActive boolean true : (default) if the submittal item type has not been deleted. false : if the submittal item type has been deleted. isInUse boolean true : if the submittal item type is currently associated with a submittal item. false : if the submittal item type is not currently associated with a submittal item. createdBy string The Autodesk ID of the user who created the submittal item type. createdAt datetime: ISO 8601 The date and time when the submittal item type was originally created. updatedAt datetime: ISO 8601 The date and time when the submittal item type was last updated. updatedBy string The Autodesk ID of the user who last updated the submittal item type.

false : if the submittal item type has been deleted.

false : if the submittal item type is not currently associated with a submittal item.

## Example

A list of item types.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/item-types' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "pagination" : { "limit" : 10 , "offset" : 100 , "totalResults" : 25 , "previousUrl" : "https://developer.api.autodesk.com/construction/submittals/v2/projects/87e0e671-7837-4bee-91de-93fd3af9eb53/item-types?limit=5&offset=10" , "nextUrl" : "https://developer.api.autodesk.com/construction/submittals/v2/projects/87e0e671-7837-4bee-91de-93fd3af9eb53/item-types?limit=5" }, "results" : [ { "id" : "5bab7f9b-61cf-45bc-8bce-f88ddd9d380e" , "key" : "my-type" , "value" : "Attic Stock" , "platformId" : "attic stock" , "isActive" : true , "isInUse" : true , "createdBy" : "WD43ZJGKDFLFH" , "createdAt" : "2018-02-01T12:09:24.198466Z" , "updatedAt" : "2018-02-01T12:09:24.198466Z" , "updatedBy" : "WD43ZJGKDFLFH" } ] }
```
