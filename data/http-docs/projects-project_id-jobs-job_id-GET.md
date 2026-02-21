# projects/:project_id/jobs/:job_id

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-jobs-job_id-GET/

---

# projects/:project_id/jobs/:job_id

Returns the job_id object.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/data/v1/projects/:project_id/jobs/:job_id Authentication Context user context optional Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. x-user-id string In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified.

### Request

## URI Parameters

project_id string The unique identifier of a project. For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a â b. " prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of b. c8b0c73d-3ae9. job_id string The unique identifier of a job.

For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a â b. " prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of b. c8b0c73d-3ae9.

### Response

## HTTP Status Code Summary

200 OK Successful retrieval of the details for a specific job. 303 Redirect The request has been redirected to a new location. 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request headers.
The client SHOULD NOT repeat the request without modifications. The response body may give an indication
of what is wrong with the request. 403 Forbidden The request was successfully validated but permission is not granted or the
application has not been white-listed.
Do not try again unless you solve permissions first. 404 Not Found The specified resource was not found.

### Response

## Body Structure (200)

jsonapi object The JSON API object. version enum:string The version of JSON API. Will always be: 1.0 links object Information on links to this resource. self object An object containing an API link property. href string A hyperlink reference to this resource. data object The object containing information on the task job. type enum:string The type of this resource. Will always be: jobs id string The id of the resource. attributes object The attributes of the task job. status enum:string The type of this resource.
Possible values: queued , finished , failed , processing links object Information on links to this resource. self object An object containing an API link property. href string A hyperlink reference to this resource.

## Example

Successful retrieval of the details for a specific job.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/jobs/:job_id' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "/data/v1/projects/{project_id}/jobs/{job_id}" } }, "data" : { "type" : "jobs" , "id" : "{job_id}" , "attributes" : { "status" : "queued" }, "links" : { "self" : { "href" : "/data/v1/projects/{project_id}/jobs/{job_id}" } } } }
```
