# Delete and Restore Files in BIM 360 Document Management

Source: https://aps.autodesk.com/en/docs/data/v2/tutorials/delete-and-restore-file/

---

# Delete and Restore Files in BIM 360 Document Management

This walkthrough demonstrates how to delete and restore files in BIM 360 Document Management. The steps include finding the ID of the file you want to delete, deleting the file, and restoring it. You can delete both Plans folder files and Project Files folder files.

Note that you cannot permanently delete BIM 360 files. Deleted files remain hidden until they are restored. By default, hidden files do not appear in the UI or in API response payloads. You can include hidden files in API response payloads by adding the hidden query string parameter ( filter[hidden]=true ). See the section on Filtering for more information.

For more details about BIM 360 file management, see the Data Management API .

## Before You Begin

- Register an app

- Acquire an 3-legged OAuth token with data:create data:read and data:write scopes.

- Verify that you have access to the relevant BIM 360 account and BIM 360 project, and that the app is integrated into the account .

- Note the name of the BIM 360 account, project, and folder that contains the file you want to delete.

## Step 1: Find the Hub ID for the BIM 360 Account

The first few steps of the walkthrough demonstrate how to find the ID of file you want to delete, which invovles iterating through several Data Management endpoints.

Find the hub ID of the BIM 360 account that contains the file you want to delete by calling GET hubs .

Note that the BIM 360 account ID corresponds to the Data Management hub ID. To convert an account ID into a hub ID you need to add a â b. " prefix. For example, an account ID of c8b0c73d-3ae9 translates to a hub ID of b. c8b0c73d-3ae9.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs"
```

### Response

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/project/v1/hubs" } }, "data" : [ { "type" : "hubs" , "id" : "b.cGVyc29uYWw6cGUyOWNjZjMy" , "attributes" : { "name" : "My First Account" , "extension" : { "type" : "hubs:autodesk.bim360:Account" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/hubs:autodesk.bim360:Account-1.0" }, "data" : {} } } } ] }
```

In this example, assume that the account (and the corresponding Data Management hub) that contains the file you want to delete is called My First Account .

Find the hub ( data.name ), and note the hub ID - b.cGVyc29uYWw6cGUyOWNjZjMy .

## Step 2: Find the Project ID

Get a list of all the projects in the hub by using the converted hub ID ( b.cGVyc29uYWw6cGUyOWNjZjMy ) to call GET hubs/:hub_id/projects to get a list of all the projects in the hub. Find the project ID of the project that contains the file you want to delete.

Note that the project ID in BIM 360 corresponds to the project ID in the Data Management API . To convert a project ID in BIM 360 to a project ID in the Data Management API, you need to add a â b. " prefix. For example, a project ID of a4be0c34a-4ab7 translates to a project ID of b. a4be0c34a-4ab7.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs/b.cGVyc29uYWw6cGUyOWNjZjMy/projects"
```

### Response

```
{ "jsonapi" :{ "version" : "1.0" }, "links" :{ "self" :{ "href" : "https://developer.api.autodesk.com/project/v1/hubs/b.cGVyc29uYWw6cGUyOWNjZjMy/projects" } }, "data" :[ { "type" : "projects" , "id" : "b.cGVyc29uYWw6d2l" , "attributes" :{ "name" : "My First Project" , "extension" :{ "type" : "projects:autodesk.core:Project" , "version" : "1.0" } } } ] }
```

In this example, assume that My First Project is the project that contains the file you want to delete.

Find the project ( data.attributes.name ), and note the project ID ( data.id ) - b.cGVyc29uYWw6d2l .

## Step 3: Find the Folder ID

In this example, assume that the file you want to delete is in the Project Files folder.

Get the Project Files folder ID by using the hub ID ( b.cGVyc29uYWw6cGUyOWNjZjMy ) and the project ID ( b.cGVyc29uYWw6d2l ) to call GET hubs/:hub_id/projects/:project_id/topFolders .

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs/b.cGVyc29uYWw6cGUyOWNjZjMy/projects/b.cGVyc29uYWw6d2l/topFolders"
```

### Response

```
{ "jsonapi" : { "version" : "1.0" }, }, "data" : [ { "type" : "folders" , "id" : "urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA" , "attributes" : { "name" : "Project Files" , "displayName" : "Project Files" , "createTime" : "2017-07-17T13:06:56.0000000Z" , "createUserId" : "" , "createUserName" : "" , "lastModifiedTime" : "2017-09-24T07:46:08.0000000Z" , "lastModifiedUserId" : "X9WYLGPNCHSL" , "lastModifiedUserName" : "John Smith" , "objectCount" : 4 , "hidden" : false , "extension" : { "type" : "folders:autodesk.bim360:Folder" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/folders:autodesk.bim360:Folder-1.0" }, "data" : { "visibleTypes" : [ "items:autodesk.bim360:File" ], "actions" : [ "CONVERT" ], "allowedTypes" : [ "items:autodesk.bim360:File" , "folders:autodesk.bim360:Folder" ] } } } }
```

Find the Project Files folder ( data.attributes.name ), and note the folder ID ( data.id ) - urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA

If you want to delete a file from a folder nested under the Project Files folder, you need to call GET projects/:project_id/folders/:folder_id/contents repeatedly through the hierarchy of folders until you find the Folder ID of the folder you want to delete. For the first iteration, use the Project Files ID ( urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA ).

## Step 4: Find the File (Item) ID

Get the ID of the file you want to delete by using the project ID ( b.cGVyc29uYWw6d2l ) and the Projet Files folder ID ( urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA ) to call GET projects/:project_id/folders/:folder_id/contents .

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/folders/urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA/contents"
```

### Response

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/folders/urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA/contents" } }, "data" : [ { "type" : "items" , "id" : "urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q" , "attributes" : { "displayName" : "Round Table" , "createTime" : "2017-10-02T11:06:44.0000000Z" , "createUserId" : "X9WYLGPNCHVK" , "createUserName" : "John Smith" , "lastModifiedTime" : "2017-10-02T11:07:45.0000000Z" , "lastModifiedUserId" : "X9WYLGPNCHVK" , "lastModifiedUserName" : "John Smith" , "hidden" : false , "reserved" : false , "extension" : { "type" : "items:autodesk.bim360:File" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/items:autodesk.bim360:File-1.0" }, "data" : {} } } } ], "included" : [ { "type" : "versions" , "id" : "urn:adsk.wipprod:fs.file:vf.II0yMfUPQl6DaOl5z-dhcg?version=1" , "attributes" : { "name" : "Round Table.dwg" , "displayName" : "Round Table.dwg" , "createTime" : "2017-10-02T11:06:44.0000000Z" , "createUserId" : "X9WYLGPNCHVK" , "createUserName" : "John Smith" , "lastModifiedTime" : "2017-10-02T11:07:45.0000000Z" , "lastModifiedUserId" : "X9WYLGPNCHVK" , "lastModifiedUserName" : "John Smith" , "versionNumber" : 1 , "storageSize" : 1952608 , "fileType" : "dwg" , "extension" : { "type" : "versions:autodesk.bim360:File" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.bim360:File-1.0" } } } } ] }
```

In this example, assume that Round Table is the file that you want to delete.

Find the file ( data.attributes.displayName ), and note the file (item) ID ( data.id ) - urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q .

## Step 5: Delete the File

Delete the file by using the project ID ( b.cGVyc29uYWw6d2l ) and the item ID ( urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q ) to call POST versions .

### Request

```
curl -X POST -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions" -H 'content-type: application/vnd.api+json' -d ' { "jsonapi":{ "version":"1.0" }, "data":{ "type":"versions", "attributes":{ "extension":{ "type":"versions:autodesk.core:Deleted", "version":"1.0" } }, "relationships":{ "item":{ "data":{ "type":"items", "id":"urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q" } } } } }'
```

### Response

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions/urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=2" } }, "data" : { "type" : "versions" , "id" : "urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q?version=2" , "attributes" : { "name" : "adf386fe-f914-4409-b463-53c6bf997617" , "displayName" : "adf386fe-f914-4409-b463-53c6bf997617" , "createTime" : "2019-02-17T12:11:39.0000000Z" , "createUserId" : "" , "createUserName" : "" , "lastModifiedTime" : "2019-02-17T12:11:39.0000000Z" , "lastModifiedUserId" : "" , "lastModifiedUserName" : "" , "versionNumber" : 2 , "extension" : { "type" : "versions:autodesk.core:Deleted" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.core:Deleted-1.0" }, "data" : { "originalName" : "Round Table" } } }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions/urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=2" } }, "relationships" : { "item" : { "data" : { "type" : "items" , "id" : "urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions/urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=2/item" } } }, "links" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2le/versions/urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=2/relationships/links" } } }, "refs" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions/urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=2/relationships/refs" }, "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions/urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=2/refs" } } }, "downloadFormats" : { "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions/urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=2/downloadFormats" } } } } }, "included" : [ { "type" : "items" , "id" : "urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q" , "attributes" : { "displayName" : "Round Table" , "createTime" : "2017-12-04T15:59:30.0000000Z" , "createUserId" : "X9WYLGPNCHVK" , "createUserName" : "John Smith" , "lastModifiedTime" : "2019-02-17T12:11:39.0000000Z" , "lastModifiedUserId" : "" , "lastModifiedUserName" : "" , "hidden" : true , "reserved" : false , "extension" : { "type" : "items:autodesk.bim360:File" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/items:autodesk.bim360:File-1.0" }, "data" : { "sourceFileName" : "Round Table" } } }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q" } }, "relationships" : { "tip" : { "data" : { "type" : "versions" , "id" : "urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q?version=2" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q/tip" } } }, "versions" : { "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q/versions" } } }, "parent" : { "data" : { "type" : "folders" , "id" : "urn:adsk.wipprod:fs.folder:co.2N6MkBpuSueF0MkEVQp8jA" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q/parent" } } }, "refs" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q/relationships/refs" }, "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q/refs" } } }, "links" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q/relationships/links" } } } } } ] }
```

Congratulations! You have deleted a file from BIM 360 Document Management.

Note the version ID ( data.id ) - ( urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q?version=2 ), which you will need if you want to restore the file.

Note that you cannot permanently delete BIM 360 files. Deleted files remain hidden until they are restored. By default, hidden files do not appear in the UI or in API response payloads. You can include hidden files in API response payloads by adding the hidden query string parameter ( filter[hidden]=true ). See the section on Filtering for more information.

## Step 6: Restore the File

Restore the file by using the project ID ( b.cGVyc29uYWw6d2l ) and the version ID ( urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=2 ) to call POST versions .

Note that every time you perform an action on a file (including delete or restore) the version number increases. When you restore a file you need to specify the version of the file you want to restore. However, you cannot restore the version of the file that was created when you deleted the file. In this example, version=2 was created when the file was deleted. To restore the file you need to reduce the version number by one. In this example, you need to adjust version=2 to version=1 . To restore the latest version of a file, you need to retrieve the latest version and subtract 1 from the version number.

### Request

```
curl -X POST -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions?copyFrom=urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=1"
     -H 'content-type: application/vnd.api+json' -d '
 {
"data": {
    "type": "versions"
        }
 }'
```

### Response

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions/urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=3" } }, "data" : { "type" : "versions" , "id" : "urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=3" , "attributes" : { "name" : "Round Table" , "displayName" : "Round Table" , "createTime" : "2019-06-18T23:29:21.0000000Z" , "createUserId" : "X9WYLGPNCHVK" , "createUserName" : "John Smith" , "lastModifiedTime" : "2019-06-18T23:29:21.0000000Z" , "lastModifiedUserId" : "" , "lastModifiedUserName" : "" , "versionNumber" : 3 , "extension" : { "type" : "versions:autodesk.bim360:Document" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.bim360:Document-1.0" }, "data" : { "processState" : "PROCESSING_PROMOTING" , "viewableId" : "2" , "viewableGuid" : "09d4fd2c-fe34-43ed-a17e-193c53fdd86e" , "viewableName" : "(2)" , "viewableOrder" : 2 , "sourceFileName" : "Round Table" } } }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions/urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=3" } }, "relationships" : { "item" : { "data" : { "type" : "items" , "id" : "urn:adsk.wipprod:dm.lineage:EMVlFFcFQnSiB-wDDdsfrg" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions/urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=3/item" } } }, "refs" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions/urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=3/relationships/refs" }, "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions/urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=3/refs" } } }, "links" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions/urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=3/relationships/links" } } }, "downloadFormats" : { "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions/urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=3/downloadFormats" } } } } }, "included" : [ { "type" : "items" , "id" : "urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q" , "attributes" : { "displayName" : "version ware" , "createTime" : "2018-03-20T10:11:45.0000000Z" , "createUserId" : "" , "createUserName" : "" , "lastModifiedTime" : "2019-06-18T23:29:21.0000000Z" , "lastModifiedUserId" : "" , "lastModifiedUserName" : "" , "hidden" : false , "reserved" : false , "extension" : { "type" : "items:autodesk.bim360:Document" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/items:autodesk.bim360:Document-1.0" }, "data" : { "sourceFileName" : "name for versions7.pdf" } } }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q" } }, "relationships" : { "tip" : { "data" : { "type" : "versions" , "id" : "urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=3" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q/tip" } } }, "versions" : { "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q/versions" } } }, "parent" : { "data" : { "type" : "folders" , "id" : "urn:adsk.wipprod:fs.folder:co.2N6MkBpuSueF0MkEVQp8jA" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q/parent" } } }, "refs" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q/relationships/refs" }, "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q/refs" } } }, "links" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q/relationships/links" } } } } } ] }
```

Congratulations! You have restored a file.
