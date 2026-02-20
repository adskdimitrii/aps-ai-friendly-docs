# projects/{projectId}/users/{userId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/admin-projectsprojectId-users-userId-GET/

---

# projects/{projectId}/users/{userId}

Retrieves detailed information about the specified user in a project.

There are two primary reasons to do this:

- To verify that the user has been activated as a member of the project.

- To check other information about the user, such as their project user ID, roles, and products.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/admin/v1/projects/:projectId/users/:userId Authentication Context user context optional Required OAuth Scopes account:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. Region string Specifies the region where your request should be routed. If not set, the request is routed automatically, which may result in a slight increase in latency. Possible values: US , EMEA . For a complete list of supported regions, see the Regions page. User-Id string The ID of a user on whose behalf your request is acting. Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request. You can use either the userâs ACC ID ( id ), or their Autodesk ID ( autodeskId ). Note that this header is required for Account Admin POST, PATCH, and DELETE endpoints if you want to use a 2-legged authentication context. This header is optional for Account Admin GET endpoints.

Possible values: US , EMEA . For a complete list of supported regions, see the Regions page.

Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.

You can use either the userâs ACC ID ( id ), or their Autodesk ID ( autodeskId ).

Note that this header is required for Account Admin POST, PATCH, and DELETE endpoints if you want to use a 2-legged authentication context. This header is optional for Account Admin GET endpoints.

### Request

## URI Parameters

projectId string: UUID The ID of the project. This corresponds to project ID in the Data Management API . To convert a project ID in the Data Management API into a project ID in the ACC API you need to remove the â b. " prefix. For example, a project ID of b.a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7 . userId string The ID of the user. To find the ID call GET users . You can use either the ACC ID ( id ) or the Autodesk ID ( autodeskId ).

### Request

## Query String Parameters

fields array: string A list of the project user fields to include in the response. Separate multiple values with commas. Possible values: name , email , firstName , lastName , autodeskId , addressLine1 , addressLine2 , city , stateOrProvince , postalCode , country , imageUrl , lastSignIn , phone , jobTitle , industry , aboutMe , createdAt , updatedAt , accessLevels , companyId , roleIds , roles , status , addedOn , and products .

Possible values: name , email , firstName , lastName , autodeskId , addressLine1 , addressLine2 , city , stateOrProvince , postalCode , country , imageUrl , lastSignIn , phone , jobTitle , industry , aboutMe , createdAt , updatedAt , accessLevels , companyId , roleIds , roles , status , addedOn , and products .

### Response

## HTTP Status Code Summary

200 OK Information about the requested project user. 400 Bad Request The request could not be understood by the server due to malformed syntax. 401 Unauthorized Request has not been applied because it lacks valid authentication credentials for the target resource. 403 Forbidden The server understood the request but refuses to authorize it. 404 Not Found The resource could not be found. 406 Not Acceptable The server cannot produce a response matching the list of acceptable values defined in the request. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 410 Access to the target resource is no longer available. 429 Too Many Requests User has sent too many requests in a given amount of time. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Server is not ready to handle the request.

### Response

## Body Structure (200)

email string The email of the user. Max length: 255 id string: UUID The ACC ID of the user. name string The full name of the user. Max length: 255 firstName string The userâs first name. This data syncs from the userâs Autodesk profile. Max length: 255 lastName string The userâs last name. This data syncs from the userâs Autodesk profile. Max length: 255 autodeskId string The ID of the userâs Autodesk profile. Max length: 255 analyticsId string Not relevant addressLine1 string The userâs address line 1. This data syncs from the userâs Autodesk profile. Max length: 255 addressLine2 string The userâs address line 2. This data syncs from the userâs Autodesk profile. Max length: 255 city string The Userâs city. This data syncs from the userâs Autodesk profile. Max length: 255 stateOrProvince string The state or province of the user. The accepted values here change depending on which country is provided. This data syncs from the userâs Autodesk profile. Max length: 255 postalCode string The zip or postal code of the user. This data syncs from the userâs Autodesk profile. Max length: 255 country string The userâs country. This data syncs from the userâs Autodesk profile. Max length: 255 imageUrl string The URL of the userâs avatar. This data syncs from the userâs Autodesk profile. Max length: 255 phone object The userâs phone number. This data syncs from the userâs Autodesk profile. number string Userâs phone number phoneType enum:string The userâs phone type. Possible values: home , mobile , or office . Default value: mobile . extension string Userâs phone extension. jobTitle string The userâs job title. This data syncs from the userâs Autodesk profile. Max length: 255 industry string The industry the user works in. This data syncs from the userâs Autodesk profile. Max length: 255 aboutMe string A short bio about the user. This data syncs from the userâs Autodesk profile. Max length: 255 accessLevels object Flags that identify a returned userâs access levels in the account or project. accountAdmin boolean Indicates whether the user is an account administrator for the account. Possible values: true : The user is an account administrator. false : The user is not an account administrator. projectAdmin boolean Indicates whether the user is a project administrator for the project. Possible values: true : The user is a project administrator. false : The user is not a project administrator. executive boolean Indicates whether the user is an executive in the account. Possible values: true : The user is an executive. false : The user is not an executive. addedOn datetime: ISO 8601 The timestamp when the user was first given access to any product on the project. updatedAt datetime: ISO 8601 The timestamp when the project user was last updated, in ISO 8601 format. companyId null,string The ID of the company that the user is representing in the project. To obtain a list of all company IDs associated with a project, call GET projects/:projectId/companies . companyName null,string The name of the company to which the user belongs. Max length: 255 roleIds array: string A list of IDs of the roles that the user belongs to in the project. roles array: object A list of the role IDs and names that are associated with the user in the project. id string: UUID The ID of a role that the user belongs to in the project. name string The name of a role that the user belongs to in the project. status string The status of the user in the project. A pending user could be waiting for their products to activate, or the user hasnât accepted an email to create an account with Autodesk. Possible values: active : The user has been added to the project. pending : The user is in the process of being added to the project. disabled : The user has been temporarily suspended from the project. deleted : The user has been removed from the project. products array: object Information about the products activated in the specified project for this user. key enum:string A machine-readable identifier for the product (e.g., docs, build). Each product has a unique key used throughout the API for identification, filtering, and integration logic (e.g., in query parameters like filter[key] ). Possible values:
ACC - autoSpecs , build , cost , designCollaboration , docs , insight , modelCoordination , projectAdministration , and takeoff . BIM 360 - assets , costManagement , designCollaboration , documentManagement , field , fieldManagement , glue , insight , modelCoordination , plan , projectAdministration , projectHome , projectManagement , and quantification . Note that this endpoint returns only ACC products. Other endpoints, such as GET projects and GET projects/:projectId , may return both ACC and BIM 360 projects. In those responses, product keys may include BIM 360 values. access enum:string The userâs type of access to the product identified by key . Possible values: administrator member none Note that when youâre using a POST or PATCH endpoint to set this value, you must adhere to the following guidelines: If you set a productâs key to projectAdministration and you set access to none , all other products should be set to member access for the user. If you set a productâs key to projectAdministration and you set access to administrator , all other products should be set to administrator access for the user. You cannot set a productâs key to projectAdministration and set access to member .

Max length: 255

Max length: 255

Max length: 255

Max length: 255

Max length: 255

Max length: 255

Max length: 255

Max length: 255

Max length: 255

Max length: 255

Max length: 255

Max length: 255

Possible values: home , mobile , or office . Default value: mobile .

Max length: 255

Max length: 255

Max length: 255

- true : The user is an account administrator.

- false : The user is not an account administrator.

- true : The user is a project administrator.

- false : The user is not a project administrator.

- true : The user is an executive.

- false : The user is not an executive.

Max length: 255

Possible values:

- active : The user has been added to the project.

- pending : The user is in the process of being added to the project.

- disabled : The user has been temporarily suspended from the project.

- deleted : The user has been removed from the project.

Each product has a unique key used throughout the API for identification, filtering, and integration logic (e.g., in query parameters like filter[key] ).

Possible values:
ACC - autoSpecs , build , cost , designCollaboration , docs , insight , modelCoordination , projectAdministration , and takeoff .

BIM 360 - assets , costManagement , designCollaboration , documentManagement , field , fieldManagement , glue , insight , modelCoordination , plan , projectAdministration , projectHome , projectManagement , and quantification .

Note that this endpoint returns only ACC products. Other endpoints, such as GET projects and GET projects/:projectId , may return both ACC and BIM 360 projects. In those responses, product keys may include BIM 360 values.

- administrator

- member

- none

Note that when youâre using a POST or PATCH endpoint to set this value, you must adhere to the following guidelines:

- If you set a productâs key to projectAdministration and you set access to none , all other products should be set to member access for the user.

- If you set a productâs key to projectAdministration and you set access to administrator , all other products should be set to administrator access for the user.

- You cannot set a productâs key to projectAdministration and set access to member .

## Example

Information about the requested project user.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/admin/v1/projects/367d5cc2-9008-462c-96e5-c9491db85d93/users/6cc15635-2fbd-4f73-afbe-abd833408a1d?fields=name' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "email" : "sampleUser1@autodesk.com" , "id" : "39712a51-bd64-446a-9c72-48c4e43d0a0d" , "name" : "Bob Smith" , "firstName" : "Bob" , "lastName" : "Smith" , "autodeskId" : "USER123A" , "analyticsId" : "SOMEID123" , "addressLine1" : "123 Main Street" , "addressLine2" : "Suite 2" , "city" : "San Francisco" , "stateOrProvince" : "California" , "postalCode" : "94001" , "country" : "United States" , "imageUrl" : "https://s3.amazonaws.com:443/com.autodesk.storage.public.dev/oxygen/USER123A/profilepictures/x20.jpg" , "phone" : { "number" : "123-345-1234" , "phoneType" : "mobile" , "extension" : "10" }, "jobTitle" : "Owner" , "industry" : "Architecture & Construction Service Providers" , "aboutMe" : "Bob has been in construction for 25 years." , "accessLevels" : { "accountAdmin" : true , "projectAdmin" : true , "executive" : true }, "addedOn" : "2018-01-01T12:45:00.000Z" , "updatedAt" : "2018-01-01T12:45:00.000Z" , "companyId" : "c32ffb13-83f8-43fb-bddf-3e5c0c2dda24" , "companyName" : "Sample Company" , "roleIds" : [ "cda845af-05f0-4c46-9108-71b993946c35" , "b8e84a73-7506-4d3f-b221-93691df2a359" ], "roles" : [ { "id" : "cda845af-05f0-4c46-9108-71b993946c35" , "name" : "Architect" }, { "id" : "b8e84a73-7506-4d3f-b221-93691df2a359" , "name" : "Engineer" } ], "status" : "active" , "products" : [ { "key" : "projectAdministration" , "access" : "administrator" }, { "key" : "designCollaboration" , "access" : "administrator" }, { "key" : "build" , "access" : "administrator" }, { "key" : "cost" , "access" : "administrator" }, { "key" : "modelCoordination" , "access" : "administrator" }, { "key" : "docs" , "access" : "administrator" }, { "key" : "insight" , "access" : "administrator" }, { "key" : "takeoff" , "access" : "administrator" } ] }
```
