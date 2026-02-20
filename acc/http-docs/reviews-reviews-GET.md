# projects/{projectId}/reviews

Source: https://aps.autodesk.com/en/docs/acc/reference/http/reviews-reviews-GET/

---

# projects/{projectId}/reviews

Retrieves the list of reviews created in the specified project.

It includes basic information such as review ID, name, status, initiator, and current step information.

For more details about reviews, see the Help documentation .

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/reviews/v1/projects/{projectId}/reviews Authentication Context user context optional Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. x-user-id string The ID of a user on whose behalf the request is made. Your application has access to all users specified by the administrator in the SaaS Integrations UI. Use this header to specify which user should be affected by the request. This header is only required when using two-legged authentication. It is not needed for three-legged authentication. Only userâs Autodesk ID ( autodeskId ) can be accepted.

This header is only required when using two-legged authentication. It is not needed for three-legged authentication.

Only userâs Autodesk ID ( autodeskId ) can be accepted.

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You can provide the project ID with or without the â b. " prefix. Example with prefix: b.563a4c30-e30d-4869-ac02-2a18b6447abe Example without prefix: 563a4c30-e30d-4869-ac02-2a18b6447abe

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You can provide the project ID with or without the â b. " prefix.

- Example with prefix: b.563a4c30-e30d-4869-ac02-2a18b6447abe

- Example without prefix: 563a4c30-e30d-4869-ac02-2a18b6447abe

### Request

## Query String Parameters

limit int The maximum number of reviews to retrieve. Possible values: 1-50 . Maximum: 50 . Default: 50 . For example: limit=2 . offset int The index of the first result to return (zero-based). Default: 0 . For example: offset=10 . sort string Sorts the results by a single field. Use the format fieldName (ascending) or fieldName desc (descending). If no direction is specified, sorting defaults to ascending. Possible values: name , status , sequenceId , currentStepDueDate , createdAt , finishedAt . For example: sort=createdAt desc . filter[workflowId] string: UUID Filter by a specific approval workflow ID in URL-encoded format. For example: filter[workflowId]=497f6eca-6276-4993-bfeb-53cbbbba6f08 . filter[status] string Filter by the review status in URL-encoded format. Possible values: OPEN , CLOSED , VOID , FAILED . For example: filter[status]=OPEN . Reviews with status FAILED are only visible to project administrators. filter[currentStepDueDate] string Filter by the due date of the current review step in URL-encoded format. Provide a date range using the format startDate..endDate . Both values must be in ISO 8601 format. For example: filter[updatedAt]=2023-06-01..2023-06-30 . filter[createdAt] string Filter by review creation date in URL-encoded format. Provide a date range using the format startDate..endDate . Both values must be in ISO 8601 format. For example: filter[createdAt]=2023-06-01..2023-06-30 filter[updatedAt] string Filter by the reviewâs last updated date in URL-encoded format. Provide a date range using the format startDate..endDate . Both values must be in ISO 8601 format. For example: filter[updatedAt]=2023-06-01..2023-06-30 . filter[finishedAt] string Filter by the date the review was finished, in URL-encoded format. Provide a date range using the format startDate..endDate . Both values must be in ISO 8601 format. For example: filter[finishedAt]=2023-06-01..2023-06-30 . filter[nextActionByUser] string Filter by Autodesk ID of a user responsible for the next action, in URL-encoded format. This includes reviews assigned directly to the user or to their role or company. For example: filter[nextActionByUser]=A96JX8NUKRLVFWSR . filter[nextActionByRole] string Filter by Autodesk ID of a role responsible for the next action, in URL-encoded format. For example: filter[nextActionByRole]=1572818 . filter[nextActionByCompany] string Filter by Autodesk ID of a company responsible for the next action, in URL-encoded format. For example: filter[nextActionByCompany]=81768771 . filter[name] string Filter by review name in URL-encoded format. Retrieves reviews with names that contain the specified string (not case-sensitive). For example: filter[name]=Apartment retrieves reviews like Apartment Block A and apartment_rendering . filter[sequenceId] int Filter by review sequence ID in URL-encoded format. Retrieves reviews with sequence IDs that partially match the specified number. For example: filter[sequenceId]=11 may retrieve 113 and 211 . filter[archived] boolean Filter by archive status in URL-encoded format. true : retrieves only archived reviews. false : retrieves only active (non-archived) reviews. If omitted, only active reviews are retrieved. For example: filter[archived]=false . filter[archivedBy] string Filter by the Autodesk ID of the user who archived the review, in URL-encoded format. To find the ID, call GET users . It only takes effect when filter[archived]=true is also set. For example: filter[archivedBy]=A96JX8NUKRLVFWSR . filter[archivedAt] string Filter by the date the review was archived, in URL-encoded format. It only applies if filter[archived]=true . Provide a date range using the format startDate..endDate . Both values must be in ISO 8601 format. For example: filter[archivedAt]=2023-06-01..2023-06-30 .

Possible values: 1-50 . Maximum: 50 . Default: 50 . For example: limit=2 .

Default: 0 . For example: offset=10 .

Use the format fieldName (ascending) or fieldName desc (descending).

If no direction is specified, sorting defaults to ascending.

Possible values: name , status , sequenceId , currentStepDueDate , createdAt , finishedAt .

For example: sort=createdAt desc .

For example: filter[workflowId]=497f6eca-6276-4993-bfeb-53cbbbba6f08 .

Possible values: OPEN , CLOSED , VOID , FAILED .

For example: filter[status]=OPEN .

Reviews with status FAILED are only visible to project administrators.

Provide a date range using the format startDate..endDate .

Both values must be in ISO 8601 format.

For example: filter[updatedAt]=2023-06-01..2023-06-30 .

Provide a date range using the format startDate..endDate .

Both values must be in ISO 8601 format.

For example: filter[createdAt]=2023-06-01..2023-06-30

Provide a date range using the format startDate..endDate .

Both values must be in ISO 8601 format.

For example: filter[updatedAt]=2023-06-01..2023-06-30 .

Provide a date range using the format startDate..endDate .

Both values must be in ISO 8601 format.

For example: filter[finishedAt]=2023-06-01..2023-06-30 .

This includes reviews assigned directly to the user or to their role or company.

For example: filter[nextActionByUser]=A96JX8NUKRLVFWSR .

For example: filter[nextActionByRole]=1572818 .

For example: filter[nextActionByCompany]=81768771 .

Retrieves reviews with names that contain the specified string (not case-sensitive).

For example: filter[name]=Apartment retrieves reviews like Apartment Block A and apartment_rendering .

Retrieves reviews with sequence IDs that partially match the specified number.

For example: filter[sequenceId]=11 may retrieve 113 and 211 .

true : retrieves only archived reviews.

false : retrieves only active (non-archived) reviews.

If omitted, only active reviews are retrieved.

For example: filter[archived]=false .

It only takes effect when filter[archived]=true is also set.

For example: filter[archivedBy]=A96JX8NUKRLVFWSR .

It only applies if filter[archived]=true .

Provide a date range using the format startDate..endDate .

Both values must be in ISO 8601 format.

For example: filter[archivedAt]=2023-06-01..2023-06-30 .

### Response

## HTTP Status Code Summary

200 OK Successfully retrieved the list of reviews 400 Bad Request Bad request. The input parameters were invalid. 403 Forbidden Forbidden. The user does not have permission to access this resource. 404 Not Found Not found. The resource does not exist or is inaccessible. 500 Internal Server Error An unexpected server error occurred.

### Response

## Body Structure (200)

results array: object A list of reviews matching the request parameters id string: UUID The unique identifier of the review. sequenceId int A unique, auto-incrementing number assigned to the review when it is first submitted. This ID does not change, even if the review is sent back to the initiator and goes through multiple rounds.
It identifies the review within the project and reflects the order in which reviews were created. name string The name of the review. status enum:string The current status of the review. Possible values: OPEN , CLOSED , VOID , FAILED . currentStepId string The ID of the current step in the review. currentStepDueDate datetime: ISO 8601 The due date of the current step. createdBy object Information about the user who initiated the review. autodeskId string The Autodesk ID of the initiator. name string The name of the initiator. createdAt datetime: ISO 8601 The date time when the review was initiated. updatedAt datetime: ISO 8601 The date time when the review was last updated. finishedAt datetime: ISO 8601 The date time when the review was completed. archived boolean Indicates whether the review has been archived. true : the review is archived. false : (default) the review is active. archivedBy object Information about the user who archived the review. autodeskId string The Autodesk ID of the archiver. name string The name of the archiver. archivedAt datetime: ISO 8601 The date and time when the review was archived. If the review has not been archived, this value is null . workflowId string: UUID The unique identifier (UUID) of the approval workflow used to create this review. nextActionBy object Information about the claimers and candidates responsible for the current step. claimedBy array: object A list of users who have already claimed the current step. autodeskId string The Autodesk ID of the user. name string The name of the user. candidates object Information about the users, roles, and companies who are eligible to take the next action in this step. roles array: object Project roles that can act in this step. autodeskId string The Autodesk ID of the role. name string The name of the role. users array: object Individual users who can act in this step. autodeskId string The Autodesk ID of the user. name string The name of the user. companies array: object Companies that can act in this step. autodeskId string The Autodesk ID of the company. name string The name of the company. pagination object Metadata about the paginated results. limit int The maximum number of results returned per page. offset int The number of results skipped before the current page. Zero-based index. totalResults int The total number of results that match the query, regardless of pagination. nextUrl string The URL to retrieve the next page of reviews results, if any.
If not included, this is the last page.

This ID does not change, even if the review is sent back to the initiator and goes through multiple rounds.
It identifies the review within the project and reflects the order in which reviews were created.

Possible values: OPEN , CLOSED , VOID , FAILED .

true : the review is archived.

false : (default) the review is active.

## Example

Successfully retrieved the list of reviews

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/reviews/v1/projects/563a4c30-e30d-4869-ac02-2a18b6447abe/reviews?limit=2&offset=10&sort=createdAt desc&filter[workflowId]=497f6eca-6276-4993-bfeb-53cbbbba6f08&filter[status]=OPEN&filter[currentStepDueDate]=2023-06-01..2023-06-30&filter[createdAt]=2023-06-01..2023-06-30&filter[updatedAt]=2023-06-01..2023-06-30&filter[finishedAt]=2023-06-01..2023-06-30&filter[nextActionByUser]=A96JX8NUKRLVFWSR&filter[nextActionByRole]=1572818&filter[nextActionByCompany]=81768771&filter[name]=Apartment&filter[sequenceId]=11&filter[archivedBy]=A96JX8NUKRLVFWSR&filter[archivedAt]=2023-06-01..2023-06-30' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "results" : [ { "id" : "37d5145b-c634-407c-b0b4-a65197e43fce" , "sequenceId" : 23 , "name" : "3rd Floor Design Review" , "status" : "OPEN" , "currentStepId" : "Lane_uJtTI3vjaF" , "currentStepDueDate" : "2024-11-09T01:42:16.600Z" , "createdBy" : { "autodeskId" : "HWUBNU689CRU" , "name" : "James Smith" }, "createdAt" : "2024-11-06T01:42:17.476Z" , "updatedAt" : "2024-11-07T12:33:36.421Z" , "finishedAt" : "2024-11-10T02:33:17.336Z" , "archived" : false , "archivedBy" : { "autodeskId" : "TTFMLCMCRG5F" , "name" : "Tim Hudson" }, "archivedAt" : "2024-11-19T01:38:27.306Z" , "workflowId" : "0b43cedf-5c02-462b-8166-7dfbb13d3476" , "nextActionBy" : { "claimedBy" : [ { "autodeskId" : "HWUBNU689CRU" , "name" : "James Smith" } ], "candidates" : { "roles" : [ { "autodeskId" : "1473817" , "name" : "Architect" } ], "users" : [ { "autodeskId" : "HWUBNU689CRU" , "name" : "James Smith" } ], "companies" : [ { "autodeskId" : "26980302" , "name" : "Autodesk Co. Ltd." } ] } } } ], "pagination" : { "limit" : 10 , "offset" : 0 , "totalResults" : 100 , "nextUrl" : "https://developer.api.autodesk.com/construction/reviews/v1/projects/497f6eca-6276-4993-bfeb-53cbbbba6f08/reviews?limit=50&offset=50" } }
```
