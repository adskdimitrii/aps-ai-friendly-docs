# projects/{projectId}/users:import

Source: https://aps.autodesk.com/en/docs/acc/reference/http/admin-v2-projects-project-Id-users-import-POST/

---

# projects/{projectId}/users:import

Adds multiple users to a project at once. Can add up to 200 users per request.

Note that the Authorization header token can be obtained either via a three-legged OAuth flow, or via a two-legged Oauth flow with user impersonation , for which the User-Id header is required.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/admin/v2/projects/:projectId/users:import Authentication Context user context optional Required OAuth Scopes account:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. Content-Type * string Must be application/json Accept-Language string This header is not currently supported in the Account Admin API. Region string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA .
For the full list of supported regions, see the Regions page. User-Id string Note that this header is not relevant for Account Admin GET endpoints. The ID of a user on whose behalf your API request is acting. Required if youâre using a 2-legged authentication context, which must be 2-legged OAuth2 security with user impersonation . Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request. You can use either the userâs ACC ID ( id ), or their Autodesk ID ( autodeskId ).

Possible values: US , EMEA .
For the full list of supported regions, see the Regions page.

The ID of a user on whose behalf your API request is acting. Required if youâre using a 2-legged authentication context, which must be 2-legged OAuth2 security with user impersonation .

Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.

You can use either the userâs ACC ID ( id ), or their Autodesk ID ( autodeskId ).

### Request

## URI Parameters

projectId string: UUID The ID of the project. This corresponds to project ID in the Data Management API . To convert a project ID in the Data Management API into a project ID in the ACC API you need to remove the â b. " prefix. For example, a project ID of b.a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7 .

### Request

## Body Structure

The users and their data to import.

users array: object User data to import. firstName string The first name of the user. Max length: 255 lastName string The last name of the user. Max length: 255 email * string The email of the user. Max length: 255 userId string Not relevant companyId null,string The ID of the company that the user is representing in the project. To obtain a list of all company IDs associated with a project, call GET projects/:projectId/companies . roleIds array: string A list of the IDs of the userâs roles in the project. To obtain role IDs for this parameter, you can call GET projects/:projectId/users endpoint or GET projects/:projectId/users/:userId and inspect the roleId field in the response. products * array: object Information about the products activated in the specified project for this imported user. key * string A keyword that identifies the product. Possible values: autoSpecs , build , cost , designCollaboration , docs , insight , modelCoordination , projectAdministration , and takeoff . access * enum:string The userâs type of access to the product identified by key . Possible values: administrator member none Note that when youâre using a POST or PATCH endpoint to set this value, you must adhere to the following guidelines: If you set a productâs key to projectAdministration and you set access to none , all other products should be set to member access for the user. If you set a productâs key to projectAdministration and you set access to administrator , all other products should be set to administrator access for the user. You cannot set a productâs key to projectAdministration and set access to member .

Max length: 255

Max length: 255

Max length: 255

To obtain role IDs for this parameter, you can call GET projects/:projectId/users endpoint or GET projects/:projectId/users/:userId and inspect the roleId field in the response.

Possible values: autoSpecs , build , cost , designCollaboration , docs , insight , modelCoordination , projectAdministration , and takeoff .

- administrator

- member

- none

Note that when youâre using a POST or PATCH endpoint to set this value, you must adhere to the following guidelines:

- If you set a productâs key to projectAdministration and you set access to none , all other products should be set to member access for the user.

- If you set a productâs key to projectAdministration and you set access to administrator , all other products should be set to administrator access for the user.

- You cannot set a productâs key to projectAdministration and set access to member .

### Response

## HTTP Status Code Summary

202 Accepted The request has been received but not yet acted upon. 400 Bad Request The request could not be understood by the server due to malformed syntax. 401 Unauthorized Request has not been applied because it lacks valid authentication credentials for the target resource. 403 Forbidden The server understood the request but refuses to authorize it. 404 Not Found The resource cannot be found. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 410 Access to the target resource is no longer available. 412 The server refuses to accept the request because a pre-condition failed. 415 The server refuses to accept the request because the payload format is in an unsupported format. 429 Too Many Requests User has sent too many requests in a given amount of time. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Server is not ready to handle the request.

### Response

## Body Structure (202)

jobId string: UUID We donât currently support this field, but expect to in a future release. If the response returns jobId with a valid UUID value, the user import operation was successful.

If the response returns jobId with a valid UUID value, the user import operation was successful.

## Example

The request has been received but not yet acted upon.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/admin/v2/projects/367d5cc2-9008-462c-96e5-c9491db85d93/users:import' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "users": [ { "firstName": "Jane", "lastName": "Doe", "email": "sampleUser1@autodesk.com", "userId": "6cc15635-2fbd-4f73-afbe-abd833408a1d", "companyId": "c32ffb13-83f8-43fb-bddf-3e5c0c2dda24", "roleIds": [ "287d5cc2-9008-462c-96e5-c9491db85d97", "cda845af-05f0-4c46-9108-71b993946c35", "b8e84a73-7506-4d3f-b221-93691df2a359" ], "products": [ { "key": "projectAdministration", "access": "administrator" }, { "key": "designCollaboration", "access": "administrator" }, { "key": "build", "access": "administrator" }, { "key": "cost", "access": "administrator" }, { "key": "modelCoordination", "access": "administrator" }, { "key": "docs", "access": "administrator" }, { "key": "insight", "access": "administrator" }, { "key": "takeoff", "access": "administrator" } ] } ] }'
```

### Response

```
{ "jobId" : "fa976214-f1fb-4795-a152-04ad20fa7310" }
```
