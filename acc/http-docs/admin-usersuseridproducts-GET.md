# accounts/{accountId}/users/{userId}/products

Source: https://aps.autodesk.com/en/docs/acc/reference/http/admin-usersuseridproducts-GET/

---

# accounts/{accountId}/users/{userId}/products

Returns a list of ACC products the user is associated with in their assigned projects.

Only account administrators can call this endpoint.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/admin/v1/accounts/:accountId/users/:userId/products Authentication Context user context optional Required OAuth Scopes account:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. Region string Specifies the region where your request should be routed. If not set, the request is routed automatically, which may result in a slight increase in latency. Possible values: US , EMEA . For a complete list of supported regions, see the Regions page. User-Id string The ID of a user on whose behalf your request is acting. Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request. You can use either the userâs ACC ID ( id ), or their Autodesk ID ( autodeskId ). Note that this header is required for Account Admin POST, PATCH, and DELETE endpoints if you want to use a 2-legged authentication context. This header is optional for Account Admin GET endpoints.

Possible values: US , EMEA . For a complete list of supported regions, see the Regions page.

Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.

You can use either the userâs ACC ID ( id ), or their Autodesk ID ( autodeskId ).

Note that this header is required for Account Admin POST, PATCH, and DELETE endpoints if you want to use a 2-legged authentication context. This header is optional for Account Admin GET endpoints.

### Request

## URI Parameters

accountId string: UUID The ID of the ACC account that contains the project being created or the projects being retrieved. This corresponds to the hub ID in the Data Management API . To convert a hub ID into an account ID, remove the â b. " prefix. For example, a hub ID of b.c8b0c73d-3ae9 translates to an account ID of c8b0c73d-3ae9 . userId string The ID of the user. To find the ID call GET users . You can use either the ACC ID ( id ) or the Autodesk ID ( autodeskId ).

### Request

## Query String Parameters

filter[projectId] array: string: uuid A list of project IDs. Only results where the user is associated with one or more of the specified projects are returned. filter[key] array: string Filters the list of products by product key â a machine-readable identifier for an ACC product (such as docs , build , or cost ). You can specify one or more keys to return only those products the user is associated with. Example: filter[key]=docs,build Possible values: accountAdministration , autoSpecs , build , buildingConnected , capitalPlanning , cloudWorksharing , cost , designCollaboration , docs , financials , insight , modelCoordination , projectAdministration , takeoff , and workshopxr . fields array: string List of fields to return in the response. Defaults to all fields. Possible values: projectIds , name and icon . sort array: string The list of fields to sort by. Each property can be followed by a direction modifier of either asc (ascending) or desc (descending). The default is asc . Possible values: name . Default is the order in database. limit int The maximum number of records to return in the response. Default: 20 Minimum: 1 Maximum: 200 (If a larger value is provided, only 200 records are returned) offset int The index of the first record to return. Used for pagination in combination with the limit parameter. Example: limit=20 and offset=40 returns records 41â60.

You can specify one or more keys to return only those products the user is associated with.

Example: filter[key]=docs,build

Possible values: accountAdministration , autoSpecs , build , buildingConnected , capitalPlanning , cloudWorksharing , cost , designCollaboration , docs , financials , insight , modelCoordination , projectAdministration , takeoff , and workshopxr .

Possible values: projectIds , name and icon .

Each property can be followed by a direction modifier of either asc (ascending) or desc (descending). The default is asc .

Possible values: name .

Default is the order in database.

Default: 20

Minimum: 1

Maximum: 200 (If a larger value is provided, only 200 records are returned)

Used for pagination in combination with the limit parameter.

Example: limit=20 and offset=40 returns records 41â60.

### Response

## HTTP Status Code Summary

200 OK A list of products associated with the user 400 Bad Request The request could not be understood by the server due to malformed syntax. 401 Unauthorized Request has not been applied because it lacks valid authentication credentials for the target resource. 403 Forbidden The server understood the request but refuses to authorize it. 404 Not Found The resource could not be found. 406 Not Acceptable The server cannot produce a response matching the list of acceptable values defined in the request. 410 Access to the target resource is no longer available. 429 Too Many Requests User has sent too many requests in a given amount of time. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Server is not ready to handle the request.

### Response

## Body Structure (200)

pagination object Contains pagination details for the records returned by the endpoint. limit int The maximum number of records returned per page. The last page may contain fewer records than the specified limit. offset int The index of the first record in the returned page. Used for pagination. totalResults int The total number of records matching the request. nextUrl string The URL for the next page of records, if more results are available. Max length: 2000 characters. Max length: 2000 previousUrl string The URL for the previous page of records, if applicable. Max length: 2000 characters. Max length: 2000 results array: object A list of ACC products the user is associated with. key enum:string A machine-readable identifier for the product (e.g., docs, build). Each product has a unique key used throughout the API for identification, filtering, and integration logic (e.g., in query parameters like filter[key] ). Possible values:
ACC - autoSpecs , build , cost , designCollaboration , docs , insight , modelCoordination , projectAdministration , and takeoff . BIM 360 - assets , costManagement , designCollaboration , documentManagement , field , fieldManagement , glue , insight , modelCoordination , plan , projectAdministration , projectHome , projectManagement , and quantification . Note that this endpoint returns only ACC products. Other endpoints, such as GET projects and GET projects/:projectId , may return both ACC and BIM 360 projects. In those responses, product keys may include BIM 360 values. icon string The URL of the icon associated with the product. name string The name of the product. projectIds array: string The list of projects IDs where the user is associated with the product.

Max length: 2000

Max length: 2000

Each product has a unique key used throughout the API for identification, filtering, and integration logic (e.g., in query parameters like filter[key] ).

Possible values:
ACC - autoSpecs , build , cost , designCollaboration , docs , insight , modelCoordination , projectAdministration , and takeoff .

BIM 360 - assets , costManagement , designCollaboration , documentManagement , field , fieldManagement , glue , insight , modelCoordination , plan , projectAdministration , projectHome , projectManagement , and quantification .

Note that this endpoint returns only ACC products. Other endpoints, such as GET projects and GET projects/:projectId , may return both ACC and BIM 360 projects. In those responses, product keys may include BIM 360 values.

## Example

A list of products associated with the user

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/admin/v1/accounts/d73fc742-4538-401c-8d0f-853b49b750b2/users/6cc15635-2fbd-4f73-afbe-abd833408a1d/products?filter[projectId]=39712a51-bd64-446a-9c72-48c4e43d0a0d,d1163421-e7eb-4862-ac15-b33777ba42de&filter[key]=build,docs&fields=name&sort=name&limit=20' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "pagination" : { "limit" : 20 , "offset" : 10 , "totalResults" : 121 , "nextUrl" : "https://resource?limit=20&offset=30" , "previousUrl" : "https://resource?limit=20&offset=0" }, "results" : [ { "key" : "assets" , "icon" : "https://s3.us-east-1.amazonaws.com/product_icon.png" , "name" : "Document Management" , "projectIds" : [ "3e354e66-ac8b-41dd-9bc1-93fc182c25dd" ] } ] }
```
