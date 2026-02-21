# CheckPermission

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/CheckPermission/

---

# CheckPermission

Checks if a user has permission to perform specified actions on specified resources.

The userâs identity is derived from the x-user-id header parameter (in a 2-Legged call), or from the Authorization Bearer token (in a 3-Legged call). The actions being checked for and the resources are specified in the JSON payload sent with the request. The resources can be folders, items, or even specified versions of an item.

The JSON response contains an array named permissions , where each element represents a resource that was checked. Each element of the array contains a permission attribute, which becomes true only if the user is permitted to perform all the specified actions for that resource. It becomes false even if one action is not permitted. To determine what action was not permitted, inspect the details object.

You can check up to 50 resources at a time.

The terms used to identify permitted actions by the CheckPermission command can be different from the terms used by the product you usually interact with. For example, the term Admin , which is used by the CheckPermissions command, is referred to as Manage by Fusion 360.

The following table shows which BIM 360 actions you can check for and the equivalent CheckPermission terminology. Note that the command checks for all possible actions assigned to the user, including actions associated with the roles and companies assigned to the user.

BIM 360 Action CheckPermission Terms view view download download upload upload collaborate collaborate edit create, updateMetaData full control admin

For information about which actions are assigned to different BIM 360 permission levels, see the Help documentation .

The following table compares the terms used by BIM 360 Team, Fusion Team, and A360 Personal with the terms used by the CheckPermissions command.

BIM360 Team, Fusion Team, A360 Personal Term CheckPermission Term read (Download and view specified resource) read download view (View specified resource without downloading) view collaborate (Add comments to the specified resource) collaborate write (Write and upload to the specified resource) write create upload updateMetaData delete (Delete the specified resource) delete manage (Perform administrative operations on specified resource) admin share (Share the specified resource) share

Note: CheckPermission is a Data Management command. Unlike typical CRUD operations, commands let you perform complex operations on multiple resources. For more details see Commands .

## Resource Information

Method and URI POST https://developer.api.autodesk.com/data/v1/projects/:project_id/commands Authentication Context user context optional Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained by means of a two-legged or three-legged OAuth flow. x-user-id string In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call is limited to act only on behalf of the specified user. Content-Type * string Must be application/vnd.api+json .

### Request

## URI Parameters

project_id string The unique identifier of a project. For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a â b. " prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of b. c8b0c73d-3ae9.

For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a â b. " prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of b. c8b0c73d-3ae9.

### Request

## Body Structure

The POST body is a JSON object with the following attributes.

jsonapi * object The JSON API object. version * enum:string The version of JSON API. Must always be: 1.0 data * object The data object. type * enum:string The type of resource. Must always be: commands attributes * object The attributes of the data object. extension * object The extension object of the data. type * enum:string The type of command. Must always be: commands:autodesk.core:CheckPermission version * string The version of the command. data * object Additional properties that the resourceâs data possesses. requiredActions * array: enum:string An array containing the list of permitted actions to check for.  Possible values: read , view , download , collaborate , write , create , upload , updateMetaData , delete , admin , share See the tables under the initial description of the command for details. relationships * object An object that specifies information about related resources. In the context of this command, it is used to specify the resources to check. resources * object An object that represents related resources. In the context of this command, it is used to specify the resources to check. data * array: object An Array of objects that represent the resources to check. id * string The URN of the resource being checked. type * string The type of resource. Possible values: folders , items , versions

### Response

## HTTP Status Code Summary

200 OK Successful execution of a command. 400 Bad Input The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. 403 Forbidden The request was successfully validated but permission is not granted or the application has not been white-listed. Do not try again unless you solve permissions first. 404 Not Found The specified resource was not found.

### Response

## Body Structure (200)

A successful response returns a JSON object with the following attributes.

jsonapi object The JSON API object. version enum:string The version of JSON API. Will always be: 1.0 data object The object containing information on the command. id string Unique identifier of the command. type enum:string The type of entity. Will always be: commands attributes object The attributes of the data object. extension object The extension object of the data. type enum:string The type of command. Will always be: commands:autodesk.core:CheckPermission . version string The version of the schema that the data is adhering to. schema object An object containing an API link property. href string A hyperlink reference to this resource. data object Additional properties that the resourceâs data possesses. requiredActions array: enum:string List of permitted actions that were checked for. Possible values: read , view , download , collaborate , write , create , upload , updateMetaData , delete , admin , share . permissions array: object An array of objects representing the resources that were checked. id string The URN of the resource. type enum:string The type of resource. Possible values: folders , items , versions . details object An object that contains the actions that were checked for, and the result, as a boolean value. A value of true indicates that the user is permitted to perform that action and false indicates that the user is not. permission bool true if the user is permitted to perform all the specified actions on the resource. false if the user is not permitted to perform at least one of the specified actions on the resource. relationships object An object that represents related resources. In this case, it is used to list the resources that were checked by the command. resources object An object that represents related resources. In this case, it is used to list the resources that were checked by the command. data array: object An array of objects representing the resources that were checked. id string The URN of the resource being checked. type string The type of resource. Possible values: folders , items , versions

## Example

Successful Execution of CheckPermission (200)

### Request

```
curl -X POST "https://developer.api.autodesk.com/data/v1/projects/a.ZXhhbXBsZTp3aXAxZnFhYXV0b2Rlc2sxNjEjMjAyMzAzMTcwMDAwMDAx/commands/" \ -H "Authorization: Bearer kEnG562yz5bhE9igXf2YTcZ2bu0z" \ -H "Content-Type: application/vnd.api+json" \ -d ' \ { "jsonapi":{ "version":"1.0" }, "data":{ "type":"commands", "attributes":{ "extension":{ "type":"commands:autodesk.core:CheckPermission", "version":"1.0.0", "data":{ "requiredActions":[ "download", "view", "write" ] } } }, "relationships":{ "resources":{ "data":[ { "type":"folders", "id":"urn:adsk.wipprod:dm.folder:hC6k4hndRWaeIVhIjvHu8w" }, { "type":"folders", "id":"urn:adsk.wipprod:dm.folder:iC6k4hndRW5eIVhIjvHu8n" }, { "type":"folders", "id":"urn:adsk.wipprod:dm.folder:jC6k4hndRW5eIVhIjvHu9x" } ] } } } }'
```

### Response

```
{ "data" : { "type" : "commands" , "id" : "d3bbe753-ae0a-450d-bbe3-cfd4648f0437" , "attributes" : { "extension" : { "data" : { "permissions" : [ { "type" : "folders" , "id" : "urn:adsk.wipprod:dm.folder:hC6k4hndRWaeIVhIjvHu8w" , "details" : { "create" : true , "download" : true , "view" : true }, "permission" : true }, { "type" : "folders" , "id" : "urn:adsk.wipprod:dm.folder:iC6k4hndRW5eIVhIjvHu8n" , "details" : { "create" : false , "download" : true , "view" : true }, "permission" : false }, { "type" : "folders" , "id" : "urn:adsk.wipprod:dm.folder:jC6k4hndRW5eIVhIjvHu9x" , "details" : { "create" : false , "download" : false , "view" : false }, "permission" : false } ], "requiredActions" : [ "create" , "download" , "view" ] }, "version" : "1.0.0" , "type" : "commands:autodesk.core:CheckPermission" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/commands:autodesk.core:CheckPermission-1.0.0" } } }, "relationships" : { "resources" : { "data" : [ { "type" : "folders" , "id" : "urn:adsk.wipprod:dm.folder:hC6k4hndRWaeIVhIjvHu8w" }, { "type" : "folders" , "id" : "urn:adsk.wipprod:dm.folder:iC6k4hndRW5eIVhIjvHu8n" }, { "type" : "folders" , "id" : "urn:adsk.wipprod:dm.folder:jC6k4hndRW5eIVhIjvHu9x" } ] } } }, "jsonapi" : { "version" : "1.0" } }
```
