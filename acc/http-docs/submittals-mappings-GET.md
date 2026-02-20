# projects/{projectId}/settings/mappings

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-mappings-GET/

---

# projects/{projectId}/settings/mappings

Retrieves users, roles, and companies assigned the manager role in the current project. Only users, roles, or companies retrieved from this endpoint can be set as a manager in a submittal item.

For more information about submittal administration, see the Help documentation .

For information on how mappings are used in the Submittal workflow, see the Create Submittal Item tutorial.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/settings/mappings Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Request

## Query String Parameters

limit int The maximum number of results per page. Possible values: 1 - 50 . Default value: 20 . For example, to limit the response to two results per page, use limit=2 . offset int The number of results to skip before starting to return data. For example, to skip the first 20 results, include offset=20 in the query string. For more details, see the JSON API Paging Help documentation . filter[autodeskId] string Comma-seperated list of Autodesk IDs for which the mappings will be returned.

### Response

## HTTP Status Code Summary

200 OK Successful retrieval of user-role mappings. 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request headers. 401 Unauthorized Invalid or missing authorization header. Verify the Bearer token and try again. 403 Forbidden The user is not authorized to perform this action. 404 Not Found The specified resource was not found. 500 Internal Server Error An unexpected error occurred on the server while processing the request.

### Response

## Body Structure (200)

pagination object Describes pagination details for the response, including information about the current page and navigation to other pages. limit int The maximum number of results to be displayed on each page. offset int The number of results skipped before starting the current page. totalResults int The overall count of results available across all pages. previousUrl string The URL to retrieve the preceding page of results, if applicable. Not returned on the first page of results. nextUrl string The URL to retrieve the subsequent page of results, if available. If not included, this is the last page of data. results array: object A list of user-role mappings defined by administrators. id string: UUID The unique identifier (UUID) of the user-role mapping record. userType enum:string The ID for the type of user in the record. Possible values: 1 (user), 2 (company), 3 (role). oxygenId string Not relevant autodeskId string The Autodesk ID of the user ( autodeskId ), role ( memberGroupId ), or company ( memberGroupId ). To find details about users, call GET users , to find details about companies, call GET companies . Note that we do not currently support finding details about roles for a project. submittalsRole enum:string The role of the user in Submittals. Possible values: 1 (manager). updatedBy string Autodesk ID of the last user who updated the record. updatedAt datetime: ISO 8601 When the record was last updated. createdBy string Autodesk ID of the user who has created the project. createdAt datetime: ISO 8601 When the record was created.

To find details about users, call GET users , to find details about companies, call GET companies . Note that we do not currently support finding details about roles for a project.

## Example

Successful retrieval of user-role mappings.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/settings/mappings' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "pagination" : { "limit" : 10 , "offset" : 100 , "totalResults" : 25 , "previousUrl" : "https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/settings/mappings?offset=10&limit=100" , "nextUrl" : null }, "results" : [ { "id" : "ab1754f6-92f1-4caa-87df-e05ba7b917a6" , "userType" : "1" , "oxygenId" : "WD43ZJGKDFLFH" , "autodeskId" : "WD43ZJGKDFLFH" , "submittalsRole" : "1" , "updatedBy" : "WD43ZJGKDFLFH" , "updatedAt" : "2024-02-11T14:14:30.225223Z" , "createdBy" : "WD43ZJGKDFLFH" , "createdAt" : "2024-02-11T14:14:30.225223Z" } ] }
```
