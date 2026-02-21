# PublishWithoutLinks

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/PublishWithoutLinks/

---

# PublishWithoutLinks

Publishes the latest version of a Collaboration for Revit (C4R) model without the links it contains to BIM 360 Docs. This enables other people to view, search, and socially interact with the model. Note that only the 3D default view and sheets are published.

To publish the latest model, you need to first:

- Initiate collaboration through Revit , and select BIM 360 Docs. This creates the first version in BIM 360 Docs.

- Modify the model locally, and synchronize the changes with the central model .

You can verify whether a model needs to be published with the GetPublishModelJob command.

Note that this command is asynchronous and initiates a job that runs in the background, rather than halting execution of your program. When the model has finished publishing without the links it contains to BIM 360 Docs, a new version of the model is created. The latest version can only be published once, this means that once it has been published without links, it cannot be republished with links. You can track the jobâs progress by using the GET projects/:project_id/items/:item_id endpoint, or the Webhooks API.

For more details about the workflow for using the PublishWithoutLinks command, see the Publish a C4R Model to BIM 360 Docs tutorial.

Note that you do not need to create an empty storage object when uploading models using the PublishWithoutLinks command. If you publish a C4R model using the PublishWithoutLinks command, you cannot add new versions to the model using POST versions .

Note that PublishWithoutLinks is a Data Management command. Commands enable you to perform complex operations on multiple resources
rather than standard CRUD operations. For more details about commands, see the Commands overview section.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/data/v1/projects/:project_id/commands Authentication Context user context required Required OAuth Scopes data:create data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. Note that it will not accept a two-legged token, unless you add the x-user-id header. x-user-id string In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified. Content-Type * string Must be application/vnd.api+json .

Note that for a three-legged OAuth flow or for a two-legged OAuth flow with user impersonation ( x-user-id ), the user must have at least edit permission for the BIM 360 Docs folder you publish the model to.

### Request

## URI Parameters

project_id string The unique identifier of a project. For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a â b. " prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of b. c8b0c73d-3ae9.

For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a â b. " prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of b. c8b0c73d-3ae9.

### Request

## Body Structure

The POST body is a JSON object with the following attributes.

jsonapi * object The JSON API object. version * enum:string The version of JSON API. Must always be: 1.0 data * object The data object. type * enum:string The type of entity. Must always be: commands attributes * object The attributes of the data object. extension * object The extension object of the data. type * enum:string The type of command. Must always be: commands:autodesk.bim360:C4RPublishWithoutLinks version * string The version of the command. The current version is 1.0.0 relationships * object An object that represents related resources. In this case, it is used to list the resources which should be published. resources * object An object that represents related resources. In this case, it is used to list the resources which should be published. data * array: object The list of resources you want to publish. id * string The URN of the resource; for details about finding the URN, follow the initial steps in the Publish a C4R Model to BIM 360 Docs tutorial. type * enum:string The type of resource. Must always be: items

### Response

## HTTP Status Code Summary

200 OK Successful execution of a command. 400 Bad Input The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. 403 Forbidden The request was successfully validated but permission is not granted or the application has not been white-listed. Do not try again unless you solve permissions first. 404 Not Found The specified resource was not found.

### Response

## Body Structure (200)

A successful response returns a JSON object with the following attributes.

jsonapi object The JSON API object. version enum:string The version of JSON API. Will always be: 1.0 data object The data object. id string Unique identifier of the command. type enum:string The type of entity. Will always be: commands attributes object The attributes of the data object. status enum:string The status of the comand. Possible values: committed , complete . Note that if you republish the same version to BIM 360 Docs, it will return a committed response. extension object The extension object of the data. type enum:string The type of command. Will always be: commands:autodesk.bim360:C4RPublishWithoutLinks version string The version of the command.

## Example

C4R Model Successfully Published to BIM 360 Docs (200)

### Request

```
curl -X POST -v "https://developer.api.autodesk.com/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/commands/" -H "Authorization: Bearer kEnG562yz5bhE9igXf2YTcZ2bu0z" -H "Content-Type: application/vnd.api+json" -d ' { "jsonapi": { "version": "1.0" }, "data": { "type": "commands", "attributes": { "extension": { "type": "commands:autodesk.bim360:C4RPublishWithoutLinks", "version": "1.0.0" } }, "relationships": { "resources": { "data": [ { "type": "items", "id": "urn:adsk.wip:dm.file:hC6k4hndRWaeIVhIjvHu8w" } ] } } } }'
```

### Response

```
{ "data" : { "type" : "commands" , "id" : "d3bbe753-ae0a-450d-bbe3-cfd4648f0437" , "attributes" : { "status" : "committed" , "extension" : { "type" : "commands:autodesk.bim360:C4RPublishWithoutLinks" , "version" : "1.0.0" } } }, "jsonapi" : { "version" : "1.0" } }
```
