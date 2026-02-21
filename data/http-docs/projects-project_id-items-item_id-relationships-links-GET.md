# projects/:project_id/items/:item_id/relationships/links

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-items-item_id-relationships-links-GET/

---

# projects/:project_id/items/:item_id/relationships/links

Returns a collection of links for the given item_id .
Custom relationships can be established between an item and other external resources residing outside the data domain service.
A linkâs href defines the target URI to access a resource.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/data/v1/projects/:project_id/items/:item_id/relationships/links Authentication Context user context optional Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. x-user-id string In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified.

### Request

## URI Parameters

project_id string The unique identifier of a project. For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a â b. " prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of b. c8b0c73d-3ae9. item_id string The unique identifier of an item.

For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a â b. " prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of b. c8b0c73d-3ae9.

### Response

## HTTP Status Code Summary

200 OK Successful retrieval of the links collection associated with a specific resource. 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request headers.
The client SHOULD NOT repeat the request without modifications. The response body may give an indication
of what is wrong with the request. 403 Forbidden The request was successfully validated but permission is not granted or the
application has not been white-listed.
Do not try again unless you solve permissions first. 404 Not Found The specified resource was not found.

### Response

## Body Structure (200)

jsonapi object The JSON API object. version enum:string The version of JSON API. Will always be: 1.0 links object Information on links to this resource. self object An object containing an API link property. href string A hyperlink reference to this resource. data array: object The array of link objects. type enum:string The type of this resource. Will always be: links id string The id of the resource. meta object The meta-information of the links of this resource. extension object The extension object of the data. type string The type of the schema that the resourceâs data object adheres to. version string The version of the schema that the data is adhering to. schema object An object containing an API link property. href string A hyperlink reference to this resource. data object Additional properties that the resourceâs data possesses. link object An object containing an API link property. href string A hyperlink reference to this resource. mimeType string Mimetype of the linkâs content. data object The object containing meta-information on the data of the links of this resource. type string The type of the resource data. id string The id of the resource.

## Example

Successful retrieval of the links collection associated with a specific resource.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/items/:item_id/relationships/links' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "/data/v1/projects/{some_project_id}/folders/{some_folder_id}/relationships/links" } }, "data" : [ { "type" : "links" , "id" : "96af4f60-53b8-4efe-b890-1eaa9ea5cb08" , "meta" : { "link" : { "href" : "/oss/v2/buckets/wipbucket/objects/myfolder.zip" }, "data" : { "type" : "objects" , "id" : "urn:adsk.objects:os.object:wipbucket/myfolder.zip" }, "mimeType" : "application/x-zip-compressed" , "extension" : { "type" : "links:A360:DownloadArchiveFolder" , "version" : "1.0" , "schema" : { "href" : "/schema/v1/versions/links%3AA360%3ADownloadArchiveFolder-1.0" }, "data" : { "createdTime" : "2015-05-22T14:56:28.000Z" } } } }, { "type" : "links" , "id" : "cf755d5e-7876-41c2-a58e-2175f9b0cd4b" , "meta" : { "link" : { "href" : "/a360/v2/items/{a360folder_id}/create_archive" }, "extension" : { "type" : "links:A360:CreateFolderArchive" , "version" : "1.0" , "schema" : { "href" : "/schema/v1/versions/links%3AA360%3ACreateFolderArchive-1.0" } } } } ] }
```
