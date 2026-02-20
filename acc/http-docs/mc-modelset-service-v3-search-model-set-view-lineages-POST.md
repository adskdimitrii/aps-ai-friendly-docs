# containers/:containerId/modelsets/:modelSetId/views:lineages

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-modelset-service-v3-search-model-set-view-lineages-POST/

---

# containers/:containerId/modelsets/:modelSetId/views:lineages

Retrieves a list of model set views in a given model set that contain the provided set of document lineage URNs. To match the provided list exactly, set the exact property to true.

This endpoint is deprecated

This endpoint is deprecated. We will continue supporting it until February 24, 2023. We recommend migrating to the GET modelsets/:modelSetId/views endpoint and filtering the response by lineages.

The response contains a list of matching views, restricted by the number specified by the pageLimit property. If set (that is, if there are more results than can be displayed at once), you can provide the continuationToken property in the response in a separate call to retrieve additional results.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/bim360/modelset/v3/containers/:containerId/modelsets/:modelSetId/views:lineages Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

containerId string: UUID The GUID that uniquely identifies the container. modelSetId string: UUID The GUID that uniquely identifies the model set.

### Request

## Query Parameters

exact boolean Determines whether to exactly match the set of lineages passed. pageLimit int The maximum number of views to return in a page. If not set, the default page limit is used, as determined by the server. continuationToken string The token indicating the start of the page. If not set, the first page is retrieved.

### Request

## Body Structure

array: string * array: string An array of lineage URNs. Min items: 1 Max items: 1000.

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request Bad request 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 415 Unsupported Media Type The Content-Type header must be application/json . 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

page object Paging information associated with a paging response. continuationToken string A continuation token to retrieve the next page. modelSetViews array: object The list of model set views. name string The name of the model set view. Min length: 1 Max length: 64. description string The description of the model set view. Min length: 1 Max length: 1024. isPrivate boolean Determines whether the view is only accessible to its creator. definition array: object The definition of models in a model set view, which is used to track the same models through time. Min items: 1 Max items: 1000. lineageUrn string The lineage URN of the seed file or document lineage to track with this view. Min length: 1 Max length: 80. viewableName string The name of the viewable in the Model Derivative manifest to track along the seed file lineage. This value is ignored if lineageUrn is the URN of a BIM360 Docs Plans folder document. Min length: 1 Max length: 430. viewId string: UUID The GUID that uniquely identifies the view. createdBy string The ID of the user or service that created the view. createdTime datetime: ISO 8601 The date and time that the view was created. modifiedBy string The ID of the user or service that last modified the view. modifiedTime datetime: ISO 8601 The date and time that the view was last modified.

### Response

## Body Structure (400)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example #1 (no query parameters)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911/views:lineages' \ -X POST \ -H 'Authorization: Bearer <token>' \ -H 'Content-Type: application/json' \ -d '[ "urn:adsk.wipprod:dm.lineage:jvMF7mrHR7OwG_DToKsJUA" ]'
```

## Example #2 (with all query parameters)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911/views:lineages?exact=False&pageLimit=134&continuationToken=10' \ -X POST \ -H 'Authorization: Bearer <token>' \ -H 'Content-Type: application/json' \ -d '[ "urn:adsk.wipprod:dm.lineage:jvMF7mrHR7OwG_DToKsJUA" ]'
```

### Response (200)

```
{ "page" : { "continuationToken" : "10" }, "modelSetViews" : [ { "name" : "L1 - All disciplines" , "description" : "All discipline models for Level 1" , "isPrivate" : false , "definition" : [ { "lineageUrn" : "urn:adsk.wipprod:dm.lineage:jvMF7mrHR7OwG_DToKsJUA" , "viewableName" : "Level 1" } ], "viewId" : "7ed27144-ac06-4b72-5dd6-76bee05854be" , "createdBy" : "PD23PXGV8V3V" , "createdTime" : "2015-10-21T16:31:44Z" } ] }
```

### Response (400)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
