# projects/:project_id/items

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-items-POST/

---

# projects/:project_id/items

Creates the first version of a file (item). To create additional versions of an item, use POST versions .

Before you create the first version you need to create a storage location for the file, and upload the file to the storage object . For more details about the workflow, see the tutorial on uploading a file .

This endpoint also copies versions of items to other folders in the same project. The endpoint creates a new item and a first version of the item in the target folder. You cannot copy versions of items across different projects and accounts.

To copy versions of items to existng items in other folders, use POST versions . POST versions creates a new version of the existing item in the target folder.

Note that to access BIM 360 Docs files using the Data Management API you need to provision your app in the BIM 360 Account Administrator portal. For more details, see the Manage Access to Docs tutorial.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/data/v1/projects/:project_id/items Authentication Context user context optional Required OAuth Scopes data:create Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. Content-Type * string Must be application/vnd.api+json x-user-id string In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified. Note that for a three-legged OAuth flow or for a two-legged OAuth flow with user impersonation ( x-user-id ), the user must have permission to upload files to the specified parent folder ( data.attributes.relationships.parent.data.id ). For copying files, the user must have permission to view the source folder. For information about managing and verifying folder permissions for BIM 360 Docs, see the section on Managing Folder Permissions .

Note that for a three-legged OAuth flow or for a two-legged OAuth flow with user impersonation ( x-user-id ), the user must have permission to upload files to the specified parent folder ( data.attributes.relationships.parent.data.id ).

For copying files, the user must have permission to view the source folder.

For information about managing and verifying folder permissions for BIM 360 Docs, see the section on Managing Folder Permissions .

### Request

## URI Parameters

project_id string The unique identifier of a project. For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a â b. " prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of b. c8b0c73d-3ae9.

For BIM 360 Docs, the project ID in the Data Management API corresponds to the project ID in the BIM 360 API. To convert a project ID in the BIM 360 API into a project ID in the Data Management API you need to add a â b. " prefix. For example, a project ID of c8b0c73d-3ae9 translates to a project ID of b. c8b0c73d-3ae9.

### Request

## Query String Parameters

copyFrom string Only relevant for copying files to BIM 360 Docs - the version ID (URN) of the file to copy. For details about finding the URN, follow the initial steps in the Download a File tutorial. You can only copy files to the Plans folder or to subfolders of the Plans folder with an item:autodesk.bim360:Document item extension type, and you can only copy files to the Project Files folder or to subfolders of the Project Files folder with an item:autodesk.bim360:File item extension type. To verify an itemâs extension type, use GET item , and check the attributes.extension.type attribute. Note that if you copy a file to the Plans folder or to a subfolder of the Plans folder, the copied file inherits the permissions of the source file. For example, if the end user did not have permission to download files in the source folder, but does have permission to download files in the target folder, he/she will not be able to download the copied file. Note that you cannot copy a file if it is in the middle of being uploaded, updated, or copied. To verify the current process state of a file, call GET item , and check the attributes.extension.data.processState attribute.

For details about finding the URN, follow the initial steps in the Download a File tutorial.

You can only copy files to the Plans folder or to subfolders of the Plans folder with an item:autodesk.bim360:Document item extension type, and you can only copy files to the Project Files folder or to subfolders of the Project Files folder with an item:autodesk.bim360:File item extension type.

To verify an itemâs extension type, use GET item , and check the attributes.extension.type attribute.

Note that if you copy a file to the Plans folder or to a subfolder of the Plans folder, the copied file inherits the permissions of the source file. For example, if the end user did not have permission to download files in the source folder, but does have permission to download files in the target folder, he/she will not be able to download the copied file.

Note that you cannot copy a file if it is in the middle of being uploaded, updated, or copied. To verify the current process state of a file, call GET item , and check the attributes.extension.data.processState attribute.

### Request

## Body Structure

describe the item to be created.

jsonapi * object The JSON API object. version * enum:string The version of JSON API. Will always be: 1.0 data * object The data object. type * enum:string The type of this resource. Will always be: items attributes * object The attributes of the data object. displayName string The name of the file (1-255 characters). Reserved characters: < , > , : , " , / , \ , | , ? , * , ` , \n , \r , \t , \0 , \f , Â¢ , â¢ , $ , Â® . This must be the same as included[i].attributes.name . Copied files are assigned the displayName of the source file by default, unless you specify a different name. Note that you need to add the same file extension that you added when you created a storage location for the file . Note that for A360 projects, this field is required. Note that for BIM 360 projects, this field is reserved for future releases and should not be used. Use included[0].attributes.name for the file name. extension * object Extended information on the resource. type string Only relevant for creating files - the type of file extension. For BIM 360 Docs files, use items:autodesk.bim360:File . For all other services, use items:autodesk.core:File . version string The version of the item extension type ( data.attributes.extension.type ). The current version is 1.0 . data object The properties of item. The property should conform to schema requirements; otherwise, it will be ignored. relationships * object The resources that share a relationship with this resource. tip * object The information on the tip version of this resource. data * object The data object. type * enum:string The type of this resource. Will always be: versions id * enum:string The id of the resource. Will always be: 1 parent * object Information on the parent resource of this resource. data * object The data object. type * enum:string The type of this resource. Will always be: folders id * string The URN of the parent folder in which you want to create a version of a file or to copy a file to. Note that you cannot copy files between folders in different BIM 360 Docs projects and accounts. For details about how to find the URN, follow the initial steps in the Download a File tutorial. included * array: object The array of resources included within this resource. type * enum:string The type of this resource. Will always be: versions id * enum:string The id of the resource. Will always be: 1 attributes * object The attributes of the resource. name * string The name of the version of the file (1-255 characters). Reserved characters: < , > , : , " , / , \ , | , ? , * , ` , \n , \r , \t , \0 , \f , Â¢ , â¢ , $ , Â® . Copied files are assigned the name of the source file by default, unless you specify a name. extension * object Extended information on the resource. type string Only relevant for creating files - the type of version extension. For BIM 360 Docs files, use versions:autodesk.bim360:File . For A360 composite design files, use versions:autodesk.a360:CompositeDesign . For A360 Personal, Fusion Team, or BIM 360 Team files, use versions:autodesk.core:File . version string The version of the version extension type ( included[i].attributes.extension.type ). The current version is 1.0 . data object The properties of the itemâs version. The property should conform to schema requirements; otherwise, it will be ignored. relationships object The object containing information on other resources that are related to this resource. storage object The object containing information on the storage resource. data * object The data object. type * enum:string Only relevant for creating files - the type of resource of the object. Will always be: objects id * string Only relevant for creating files - the storage URN of the version. The storage URN is the objectId returned when uploading the file to the storage object . refs object Only relevant for creating files. data * array: object The array of ref objects. type * enum:string Will always be: versions id * string The URN of Version. meta * object The meta-information of this resource. refType * enum:string Will always be: xrefs direction * enum:string Possible values: from , to extension * object Extended information on the resource. type * enum:string The type of the resource. Will always be: xrefs:autodesk.core:Xref version * string The version of xref type. The current version is 1.1.0. data object The data object. nestedType * enum:string The type of the resource.
Possible values: attachment , overlay meta object Meta-information for the resource creation. workflow * string Only relevant for BIM 360 Docs. The workflow id created for a webhook, used to listen to Model Derivative events. It needs to be no more than 36 chars, and only ASCII, decimal and hyphen are accepted. See the Creating a Webhook and Listening to Events tutorial for details. workflowAttribute object Only relevant for BIM 360 Docs. A user-defined JSON object, which you can use to set some custom workflow information. It needs to be less than 1KB and will be ignored if meta.workflow parameter is not set.

Copied files are assigned the displayName of the source file by default, unless you specify a different name.

Note that you need to add the same file extension that you added when you created a storage location for the file .

Note that for A360 projects, this field is required.

Note that for BIM 360 projects, this field is reserved for future releases and should not be used. Use included[0].attributes.name for the file name.

For BIM 360 Docs files, use items:autodesk.bim360:File .

For all other services, use items:autodesk.core:File .

Note that you cannot copy files between folders in different BIM 360 Docs projects and accounts.

For details about how to find the URN, follow the initial steps in the Download a File tutorial.

Copied files are assigned the name of the source file by default, unless you specify a name.

For BIM 360 Docs files, use versions:autodesk.bim360:File .

For A360 composite design files, use versions:autodesk.a360:CompositeDesign .

For A360 Personal, Fusion Team, or BIM 360 Team files, use versions:autodesk.core:File .

### Response

## HTTP Status Code Summary

201 Created Successful creation of a version of a file, or the file was successfully copied. 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request headers.
The client SHOULD NOT repeat the request without modifications. The response body may give an indication
of what is wrong with the request. 403 Forbidden The request was successfully validated but permission is not granted or the
application has not been white-listed.
Do not try again unless you solve permissions first. 404 Not Found The specified resource was not found. 409 Conflict The specified resource already exists, has been modified, or is in the middle of being uploaded, updated, or copied. 423 Locked The source or destination resource is locked or being modifed.

### Response

## Body Structure (201)

jsonapi object The JSON API object. version enum:string The version of JSON API. Will always be: 1.0 links object Information on links to this resource. self object An object containing an API link property. href string A hyperlink reference to this resource. data object The object containing information on the item. type enum:string The type of this resource. Will always be: items id string The unique identifier of the item. attributes object Attributes of the latest version of an item. displayName string Displayable name of an item. Note that for BIM 360 projects, this field is reserved for future releases and should not be used. Use versionâs attributes.name for the file name. createTime datetime: ISO 8601 The time the item was created, in the following format: YYYY-MM-DDThh:mm:ss.sz . createUserId string The unique identifier of the user who created the item. createUserName string The name of the user who created the item. lastModifiedTime datetime: ISO 8601 The last time the item was modified, in the following format: YYYY-MM-DDThh:mm:ss.sz . lastModifiedUserId string The unique identifier of the user who last modified the item. lastModifiedUserName string The name of the user who last modified the item. hidden boolean true if the file has been deleted. false if the file has not been deleted. reserved boolean true if the file has been locked.``false`` if the file has not been locked. Note that you can lock BIM 360 Project Files folder files and A360 files, but you cannot lock BIM 360 Plans Folder files. reservedTime datetime: ISO 8601 The time the item was reserved. reservedUserId string The unique identifier of the user who reserved the item. reservedUserName string The name of the user who reserved the item. extension object The extension object of the data. type string The type of the schema that the resourceâs data object adheres to. version string The version of the schema that the data is adhering to. schema object An object containing an API link property. href string A hyperlink reference to this resource. data object Additional properties that the resourceâs data possesses. relationships object Information on other resources that shares a relationship with this item. parent object Information on resources that are found above this resource. links object The object containing information on links of related resources. related object An object containing an API link property. href string A hyperlink reference to this resource. data object An object containing the id and type properties of a resource. id string The id of the resource. type string The type of this resource. tip object Information on resources that are found above this resource. links object The object containing information on links of related resources. related object An object containing an API link property. href string A hyperlink reference to this resource. data object An object containing the id and type properties of a resource. id string The id of the resource. type string The type of this resource. versions object Information on resources that are found under this resource. links object The object containing information on links of related resources. related object An object containing an API link property. href string A hyperlink reference to this resource. refs object Information on other resources that shares a custom relationship with this resource. links object The object containing information on links of related resources that shares a custom relationship with this resource. self object An object containing an API link property. href string A hyperlink reference to this resource. related object An object containing an API link property. href string A hyperlink reference to this resource. links object Information on the link resources found in this resource. links object The object containing information on links to this resource. self object An object containing an API link property. href string A hyperlink reference to this resource. links object Information on links to this resource. self object An object containing an API link property. href string A hyperlink reference to this resource. webView object An object containing a link that opens the resource in a browser. href string The location (URL) of the resource the link goes to. included array: object The array of resources included within this resource. type enum:string The type of this resource. Will always be: versions id string The id of the resource. attributes object The attributes of the resource. name string The filename used when synced to local disk. displayName string Displayable name of the version. Note that for BIM 360 projects, this field is reserved for future releases and should not be used. Use versionâs attributes.name for the file name. versionNumber int Version number of this versioned file. mimeType string Mimetype of the versionâs content. fileType string File type, only present if this version represents a file. storageSize int File size in bytes, only present if this version represents a file. createTime datetime: ISO 8601 The time that the resource was created at. createUserId string The userId that created the resource. createUserName string The username that created the resource. lastModifiedTime datetime: ISO 8601 The time that the resource was last modifed. lastModifiedUserId string The userId that last modified the resource. lastModifiedUserName string The username that last modified the resource. extension object The extension object of the data. type string The type of the schema that the resourceâs data object adheres to. version string The version of the schema that the data is adhering to. schema object An object containing an API link property. href string A hyperlink reference to this resource. data object Additional properties that the resourceâs data possesses. conformingStatus enum:string A status indicating whether or not this version conforms to its parent folderâs file naming standard. Possible values: NONE : The conforming status is not applicable for the version. CONFORMING : The version conforms to its parent folderâs file naming standard. NON_CONFORMING : The version does not conform to its parent folderâs file naming standard. In the event of a NON_CONFORMING status, call GET folders/folder_id to get the file naming standards IDs that have been applied to the versionâs parent folder, and then use the ID to call GET naming-standards to get the details of the file naming standard. Note that this feature is only available for BIM 360 projects. To learn more about the file naming standard feature, see the BIM 360 File Naming Standard help documentation. relationships object Information on other resources that shares a relationship with this resource. item object Information on resources that are found above this resource. links object The object containing information on links of related resources. related object An object containing an API link property. href string A hyperlink reference to this resource. data object An object containing the id and type properties of a resource. id string The id of the resource. type string The type of this resource. refs object Information on other resources that shares a custom relationship with this resource. links object The object containing information on links of related resources that shares a custom relationship with this resource. self object An object containing an API link property. href string A hyperlink reference to this resource. related object An object containing an API link property. href string A hyperlink reference to this resource. links object Information on the link resources found in this resource. links object The object containing information on links to this resource. self object An object containing an API link property. href string A hyperlink reference to this resource. storage object Information on resources that are indirectly related to this resource. meta object Meta-information on links to this resource. link object An object containing an API link property. href string A hyperlink reference to this resource. data object An object containing the id and type properties of a resource. id string The id of the resource. type string The type of this resource. derivatives object Information on resources that are indirectly related to this resource. meta object Meta-information on links to this resource. link object An object containing an API link property. href string A hyperlink reference to this resource. data object An object containing the id and type properties of a resource. id string The id of the resource. type string The type of this resource. thumbnails object Information on resources that are indirectly related to this resource. meta object Meta-information on links to this resource. link object An object containing an API link property. href string A hyperlink reference to this resource. data object An object containing the id and type properties of a resource. id string The id of the resource. type string The type of this resource. downloadFormats object Information on resources that are found under this resource. links object The object containing information on links of related resources. related object An object containing an API link property. href string A hyperlink reference to this resource. links object Information on links to this resource. self object An object containing an API link property. href string A hyperlink reference to this resource. webView object An object containing a link that opens the resource in a browser. href string The location (URL) of the resource the link goes to. meta object The object containing information on the command id of the command processor. bim360DmCommandId string The command id of command processor. Can be used to check the status of processing.

Possible values:

- NONE : The conforming status is not applicable for the version.

- CONFORMING : The version conforms to its parent folderâs file naming standard.

- NON_CONFORMING : The version does not conform to its parent folderâs file naming standard.

In the event of a NON_CONFORMING status, call GET folders/folder_id to get the file naming standards IDs that have been applied to the versionâs parent folder, and then use the ID to call GET naming-standards to get the details of the file naming standard.

Note that this feature is only available for BIM 360 projects.

To learn more about the file naming standard feature, see the BIM 360 File Naming Standard help documentation.

## Example

Successful creation of a version of a file, or the file was successfully copied.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/items' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/vnd.api+json' \ -d '{ "jsonapi": { "version": "1.0" }, "data": { "type": "items", "attributes": { "displayName": "drawing.dwg", "extension": { "type": "items:autodesk.core:File", "version": "1.0" } }, "relationships": { "tip": { "data": { "type": "versions", "id": "1" } }, "parent": { "data": { "type": "folders", "id": "urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA" } } } }, "included": [ { "type": "versions", "id": "1", "attributes": { "name": "drawing.dwg", "extension": { "type": "versions:autodesk.core:File", "version": "1.0" } }, "relationships": { "storage": { "data": { "type": "objects", "id": "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b-9aed-439586d61df7.dwg" } } } } ] }'
```

### Response

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3Aadsk.wipprod%3Adm.lineage%3AhC6k4hndRWaeIVhIjvHu8w" } }, "data" : { "type" : "items" , "id" : "urn:adsk.wipprod:dm.lineage:hC6k4hndRWaeIVhIjvHu8w" , "attributes" : { "displayName" : "drawing.dwg" , "createTime" : "2018-03-26T09:40:16.0000000Z" , "createUserId" : "CGT5PFDIZMAS" , "createUserName" : "Owen" , "lastModifiedTime" : "2018-03-26T09:40:16.0000000Z" , "lastModifiedUserId" : "CGT5PFDIZMAS" , "lastModifiedUserName" : "Owen" , "hidden" : false , "reserved" : false , "extension" : { "type" : "items:autodesk.core:File" , "version" : "1.0" } }, "relationships" : { "tip" : { "links" : { "related" : { "href" : "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.d34fdsg3g%3Fversion%3D1" } }, "data" : { "type" : "versions" , "id" : "urn:adsk.wipprod:fs.file:vf.d34fdsg3g?version=1" } } }, "links" : { "self" : { "href" : "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn:adsk.wipprod:dm.lineage:hC6k4hndRWaeIVhIjvHu8w" }, "webView" : { "href" : "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.0J4paz_FQgWPX2QRsaBkiw/detail/viewer/items/urn:adsk.wipprod:dm.lineage:hC6k4hndRWaeIVhIjvHu8w" } } }, "included" : [ { "type" : "versions" , "id" : "urn:adsk.wipprod:fs.file:vf.d34fdsg3g?version=1" , "attributes" : { "name" : "drawing.dwg" , "displayName" : "drawing.dmg" , "createTime" : "2018-03-26T09:40:16.0000000Z" , "createUserId" : "CGT5PFDIZMAS" , "createUserName" : "Owen" , "lastModifiedTime" : "2018-03-26T09:40:16.0000000Z" , "lastModifiedUserId" : "CGT5PFDIZMAS" , "lastModifiedUserName" : "Owen" , "versionNumber" : 1 , "extension" : { "type" : "versions:autodesk.bim360:File" , "version" : "1.0" , "data" : { "conformingStatus" : "NONE" } } }, "relationships" : {}, "links" : { "self" : { "href" : "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn:adsk.wipprod:fs.file:vf.d34fdsg3g?version=1" }, "webView" : { "href" : "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn:adsk.wipprod%3Afs.folder%3Aco.nent0xPeT1yLnrAPJb0v0g/detail/viewer/items/urn:adsk.wipprod:fs.file:vf.d34fdsg3g%3Fversion%3D1" } } } ] }
```

## Example 2

Successful creation of a version of a file with workflow.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/items?copyFrom=urn%3Aadsk%3Awipprod%3Afs.file%3ASOME.SOURCE%3Fversion%3D1' \ -X 'POST' \ -H 'Authorization: Bearer kEnG562yz5bhE9igXf2YTcZ2bu0z' \ -H 'Content-Type: application/vnd.api+json' \ -d '{ "jsonapi": { "version": "1.0" }, "data": { "type": "items", "relationships": { "tip": { "data": { "type": "versions", "id": "1" } }, "parent": { "data": { "type": "folders", "id": "urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA" } } } }, "included": [ { "type": "versions", "id": "1", "attributes": { "name": "new version name" } } ], "meta": { "workflow": "my-workflow-id", "workflowAttribute": { "myfoo": 33, "projectId": "someURN", "myobject": { "nested": true } } } }'
```

### Response

```
{ "included" : [ { "relationships" : {}, "attributes" : { "name" : "new version name" , "extension" : { "version" : "1.0" , "type" : "versions:autodesk.core:File" } }, "type" : "versions" , "id" : "urn:adsk:wipprod:fs.file:vf.AABBCCDD?version=1" } ], "data" : { "relationships" : { "tip" : { "data" : { "type" : "versions" , "id" : "urn:adsk:wipprod:fs.file:vf.AABBCCDD?version=1" }, "links" : { "related" : { "href" : "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk%3Awipprod%3Afs.file%3Avf.AABBCCDD%3Fversion%3D1" } } } }, "attributes" : { "displayName" : "filename" , "extension" : { "version" : "1.0" , "type" : "items:autodesk.core:File" } }, "type" : "items" , "id" : "urn:adsk:wipprod:dm.lineage:vf.AABBCCDD" , "links" : { "self" : { "href" : "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3aadsk%3awipprod%3adm.lineage%3avf.AABBCCDD" }, "webView" : { "href" : "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.akd2j_B3Tsu7v6v7Kxf2oQ/detail/viewer/items/urn%3aadsk%3awipprod%3adm.lineage%3avf.AABBCCDD" } } }, "jsonapi" : { "version" : "1.0" } }
```

## Example 3

The file was successfully copied.

### Request

```
curl -v 'https://developer.api.autodesk.com/data/v1/projects/:project_id/items?copyFrom=urn%3Aadsk%3Awipprod%3Afs.file%3ASOME.SOURCE%3Fversion%3D1' \ -X 'POST' \ -H 'Authorization: Bearer kEnG562yz5bhE9igXf2YTcZ2bu0z' \ -H 'Content-Type: application/vnd.api+json' \ -d '{ "jsonapi": { "version": "1.0" }, "data": { "type": "items", "relationships": { "tip": { "data": { "type": "versions", "id": "1" } }, "parent": { "data": { "type": "folders", "id": "urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA" } } } }, "included": [ { "type": "versions", "id": "1", "attributes": { "name": "new version name" } } ] }'
```

### Response

```
{ "included" : [ { "relationships" : {}, "attributes" : { "name" : "new version name" , "extension" : { "version" : "1.0" , "type" : "versions:autodesk.core:File" } }, "type" : "versions" , "id" : "urn:adsk:wipprod:fs.file:vf.AABBCCDD?version=1" } ], "data" : { "relationships" : { "tip" : { "data" : { "type" : "versions" , "id" : "urn:adsk:wipprod:fs.file:vf.AABBCCDD?version=1" }, "links" : { "related" : { "href" : "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/versions/urn%3Aadsk%3Awipprod%3Afs.file%3Avf.AABBCCDD%3Fversion%3D1" } } } }, "attributes" : { "displayName" : "filename" , "extension" : { "version" : "1.0" , "type" : "items:autodesk.core:File" } }, "type" : "items" , "id" : "urn:adsk:wipprod:dm.lineage:vf.AABBCCDD" , "links" : { "self" : { "href" : "/data/v1/projects/b.c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/items/urn%3aadsk%3awipprod%3adm.lineage%3avf.AABBCCDD" }, "webView" : { "href" : "https://docs.b360.autodesk.com/projects/c2960674-2d1e-4cc8-a5f0-4b9026fd3f5d/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.akd2j_B3Tsu7v6v7Kxf2oQ/detail/viewer/items/urn%3aadsk%3awipprod%3adm.lineage%3avf.AABBCCDD" } } }, "jsonapi" : { "version" : "1.0" } }
```
