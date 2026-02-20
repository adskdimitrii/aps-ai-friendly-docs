# containers/:containerId/modelsets

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-modelset-service-v3-get-model-sets-GET/

---

# containers/:containerId/modelsets

Retrieves a list of model sets in a given container that match the provided search parameters.

The response contains a list of matching model sets, restricted by the number specified by the pageLimit property. If set (that is, if there are more results than can be displayed at once), you can provide the continuationToken property in the response in a separate call to retrieve additional results.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/bim360/modelset/v3/containers/:containerId/modelsets Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

containerId string: UUID The GUID that uniquely identifies the container.

### Request

## Query Parameters

pageLimit int The maximum number of model sets to return in a page. If not set, the default page limit is used, as determined by the server. continuationToken string The token indicating the start of the page. If not set, the first page is retrieved. name string A model set name filter. This is an equality filter. folderUrn string A folder URN filter. includeDisabled boolean Determines whether to include disabled model sets.

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

page object Paging information associated with a paging response. continuationToken string A continuation token to retrieve the next page. modelSets array: object List of model set summaries. modelSetId string: UUID The GUID that uniquely identifies the model set. containerId string: UUID The GUID that uniquely identifies the container. name string The name of the model set. description string Additional information about the model set. createdBy string The unique identifier of the user who created the model set. createdTime datetime: ISO 8601 The date and time that the model set was created. isDisabled boolean Indicates if new versions are created for model set changes. isDeleted boolean Indicates whether the model set is deleted.

### Response

## Body Structure (400)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example #1 (no query parameters)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets' \ -H 'Authorization: Bearer <token>'
```

## Example #2 (with all query parameters)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets?pageLimit=134&continuationToken=10&name=Formal+Coordination&folderUrn=urn%3aadsk.wipprod%3afs.folder%3aco.WI8roO18TU2Cl3P9y64z4w&includeDisabled=False' \ -H 'Authorization: Bearer <token>'
```

### Response (200)

```
{ "page" : { "continuationToken" : "10" }, "modelSets" : [ { "modelSetId" : "00fb28a5-e8a4-2755-562a-7c2f0fc87911" , "containerId" : "f0f4f36a-ac64-687f-b132-8efe04b22454" , "name" : "Formal Coordination" , "description" : "Space for coordinating all disciplines" , "createdBy" : "PD23PXGV8V3V" , "createdTime" : "2015-10-21T16:31:44Z" , "isDisabled" : true , "isDeleted" : false } ] }
```

### Response (400)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
