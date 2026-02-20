# v1/containers/{containerId}/segments/{segmentId}/values

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-values-GET/

---

# v1/containers/{containerId}/segments/{segmentId}/values

Retrieves all of the defined segment values for a specific segment.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/segments/:segmentId/values Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. region string Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead. Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page. To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.

Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page.

To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

### Request

## URI Parameters

containerId string: UUID The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see GET projects . segmentId string: UUID The segment ID. To obtain a segment ID, use GET templates/:templateId/segments .

### Request

## Query String Parameters

filter[code] array: string Returns only items that are identified by the specified codes (separated by commas). For example, filter[code]="2703,2704" . Note that even single codes in number format must be enclosed in double quotes: filter[code]="1" or filter[code]="122. 221" . filter[originalCode] array: string Returns only the values of segments with the specified original codes, including delimiters. For example, filter[originalCode]=27-03,27-04 . filter[parentId] array: string: uuid Returns only the values of segments with the specified IDs of parent segments. Separate multiple parent IDs with commas. For example, filter[parentId]=parentId1,parentId2 . You can also return the values of segments that have no parent by including filter[parentId]=blank . filter[lastModifiedSince] string Returns only items that were modified since the specified date and time, in ISO 8601 format. For example, filter[lastModifiedSince]=2020-03-01T13:00:00Z . offset int The number of records to skip before returning results. Used together with limit to paginate through results, where offset specifies the starting point and limit specifies the number of records to return. limit int The maximum number of records returned per page. Default: 100 . A page may contain fewer records than the limit if there are fewer matching items or if it is the last page of results. sort string Defines the sort order for the results. Each attribute can be sorted in asc (default) or desc order. For example, sort=name desc sorts the results by name in descending order.

Note that even single codes in number format must be enclosed in double quotes: filter[code]="1" or filter[code]="122. 221" .

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters are invalid. 401 Unauthorized The provided bearer token is invalid. 403 Forbidden Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The resource or endpoint cannot be found. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 429 Too Many Requests Rate limit exceeded. Retry your request after a few minutes. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Service unavailable.

### Response

## Body Structure (200)

pagination object Contains pagination information when data is returned page by page. limit int The maximum number of records returned in the response. offset int The number of records skipped before returning the page of results. totalResults int The total number of records that matched the request criteria. nextUrl string The URL for the next request to retrieve the next page of results. Max length: 2000. Max length: 2000 results array: object The detailed segment definition values id string: UUID The ID of the code. segmentId string: UUID The ID of the segment this code belongs to. parentId string,null The parent ID of this code if it is the sub item of another code. code string The display code. Max length: 255 originalCode string The original value of the code before the delimiters are removed. Max length: 255 description string The description of the code. Max length: 2048 createdAt datetime: ISO 8601 The date and time that the item was created, in ISO 8601 format. updatedAt datetime: ISO 8601 The date and time that the item was last updated, in ISO 8601 format.

Max length: 2000

Max length: 255

Max length: 255

Max length: 2048

## Example

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/segments/87256c07-5c03-42cd-b4dc-e9d06411c0cc/values?filter[lastModifiedSince]=2020-03-01T13:00:00Z&limit=100&sort=name,createdAt desc' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "pagination" : { "limit" : 20 , "offset" : 0 , "totalResults" : 1 , "nextUrl" : "" }, "results" : [ { "id" : "229d3420-9481-11e8-87fb-215990a8aeb3" , "segmentId" : "87256c07-5c03-42cd-b4dc-e9d06411c0cc" , "parentId" : "null" , "code" : 6656 , "originalCode" : "01 50 00" , "description" : "Temporary Facilities and Controls" , "createdAt" : "2019-01-06T01:24:22.678Z" , "updatedAt" : "2019-09-05T01:00:12.989Z" } ] }
```
