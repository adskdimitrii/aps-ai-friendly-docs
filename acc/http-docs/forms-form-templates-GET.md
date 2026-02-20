# v1/projects/{projectId}/form-templates

Source: https://aps.autodesk.com/en/docs/acc/reference/http/forms-form-templates-GET/

---

# v1/projects/{projectId}/form-templates

Returns all projectâs form templates the user has access to.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/form-templates Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

projectId string The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Request

## Query String Parameters

offset int The number of records to skip before returning the result records. Defaults to 0. Increase this value in subsequent requests to continue getting results when the number of records exceeds the requested limit. limit int The number of records to return in a single request. Can be a number between 1 and 50. Defaults to 50. updatedAfter datetime: ISO 8601 Return Templates updated after specified time. updatedBefore datetime: ISO 8601 Return Templates updated before specified time. sortOrder enum:string Return Templates in specified sorted order.
Possible values: desc , asc

### Response

## HTTP Status Code Summary

200 OK Form Templates. 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request header 401 Unauthorized The request was not accepted because it lacked valid authentication credentials 403 Forbidden The request was not accepted because the client is authenticated, but is not authorized to access the target resource 404 Not Found The resource cannot be found 429 Too Many Requests The request could not be completed due to a conflict with the current state of the target resource 500 Internal Server Error The request could not be completed due to a conflict with the current state of the target resource

### Response

## Body Structure (200)

data array: object List of form templates in the project. projectId string Unique indentifier of the project the template belongs to. id string The unique identifier of the template. name string Display name of template. status string Status of template: "active" , "inactive" (archived), or "deleted" templateType string User supplied type of template userPermissions array Permissions on this template assigned to individual users. groupPermissions array Permissions on this template assigned to companies and roles. createdBy string The unique identifier of the user who created the template. updatedAt datetime: ISO 8601 When the template was last updated, UTC date and time in ISO-8601 format. isPdf boolean A flag that indicates whether the template has a PDF or not. pdfUrl string For PDF forms, the URL to download the formâs PDF. forms object Reference to fetch forms created from this template. url string URL to retrieve resources. pagination object Request pagination information. offset int Number of items skipped. limit int Number of items returned. totalResults int Total number of items that can be returned. nextUrl string URL for the next page of items. Next page url is null on the last page.
