# Download a File

Source: https://aps.autodesk.com/en/docs/data/v2/tutorials/download-file/

---

# Download a File

This walkthrough explains how to navigate the project and data domains to find a resource, then download it.

## Before You Begin

Make sure that you have registered an app and successfully acquired an OAuth token .

See the Authentication and Scopes section in the API Basics for the appropriate token based on the data you are accessing.

In general, access to BIM 360 Team, BIM 360 Docs, Fusion Team, and A360 Personal data requires the use of a 3-legged OAuth2 token .

HTTP GET requests to the Project and Data services require the data:read scope.

HTTP POST requests to the Data service require the data:create scope, but can also be called with the data:write scope.

## Step 1: Find the hub that has your resource

The Data Management service exposes a GET hubs endpoint that provides a list of available hubs for the logged in user.
A GET request to that endpoint allows us to find the URL for the hub we want.

### Example

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs"
```

The resource provides the following response:

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/project/v1/hubs" } }, "data" : [ { "type" : "hubs" , "id" : "a.cGVyc29uYWw6cGUyOWNjZjMy" , "attributes" : { "name" : "John's Hub" , "extension" : { "type" : "hubs:autodesk.core:Hub" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/hubs%3Aautodesk.core%3AHub-1.0" }, "data" : {} } } } ] }
```

## Step 2: Find the project that has your resource

In the above example, assume that your resource exists in John's Hub .
Make note of the the hub ID a.cGVyc29uYWw6cGUyOWNjZjMy .
The hub ID can be used with the GET hubs/:hub_id/projects endpoint to obtain a list of all the projects the user has access to within the hub.
For our example we are going to filter the projects to just the one we are interested in.

### Example

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs/a.cGVyc29uYWw6cGUyOWNjZjMy/projects?filter%5Battributes.name%5D=Demo%20Project"
```

The resource provides the following response:

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/project/v1/hubs/a.cGVyc29uYWw6cGUyOWNjZjMy/projects" } }, "data" : [ { "type" : "projects" , "id" : "a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY" , "attributes" : { "name" : "Demo Project" , "extension" : { "type" : "projects:autodesk.core:Project" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/projects%3Aautodesk.core%3AProject-1.0" }, "data" : {} } }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/project/v1/hubs/a.cGVyc29uYWw6cGUyOWNjZjMy/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY" } }, "relationships" : { "hub" : { "data" : { "type" : "hubs" , "id" : "a.cGVyc29uYWw6cGUyOWNjZjMy" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/project/v1/hubs/a.cGVyc29uYWw6cGUyOWNjZjMy" } } }, "rootFolder" : { "data" : { "type" : "folders" , "id" : "urn:adsk.wipprod:fs.folder:co.uvDiLQ5DRYidDQ_EFW1OOg" }, "meta" : { "link" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.uvDiLQ5DRYidDQ_EFW1OOg" } } } } } ] }
```

## Step 3: Find the resource item in a project folder

In the above example, assume that your resource exists in Demo Project .
Make note of the the project and folder IDs a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY and urn:adsk.wipprod:fs.folder:co.uvDiLQ5DRYidDQ_EFW1OOg respectively.
The GET projects/:project_id/folders/:folder_id/contents endpoint allows us to retrieve all the contents of the specified folder.

### Example

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/folders/urn:adsk.wipprod:fs.folder:co.uvDiLQ5DRYidDQ_EFW1OOg/contents"
```

The resource provides the following response:

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/folders/urn:adsk.wipprod:fs.folder:co.uvDiLQ5DRYidDQ_EFW1OOg/contents" } }, "data" : [ { "type" : "items" , "id" : "urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q" , "attributes" : { "displayName" : "House Design.rvt" , "createTime" : "2016-05-24T19:25:23+00:00" , "createUserId" : "38SCJGX4R4PV" , "createUserName" : "John Doe" , "lastModifiedTime" : "2016-05-24T19:25:23+00:00" , "lastModifiedUserId" : "38SCJGX4R4PV" , "lastModifiedUserName" : "John Doe" , "extension" : { "type" : "items:autodesk.core:File" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/items%3Aautodesk.core%3AFile-1.0" }, "data" : {} } }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q" } }, "relationships" : { "tip" : { "data" : { "type" : "versions" , "id" : "urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q?version=1" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q/tip" } } }, "versions" : { "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q/versions" } } }, "parent" : { "data" : { "type" : "folders" , "id" : "urn:adsk.wipprod:fs.folder:co.uvDiLQ5DRYidDQ_EFW1OOg" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q/parent" } } }, "refs" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q/relationships/refs" }, "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q/refs" } } } } } ], "included" : [ { "type" : "versions" , "id" : "urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q?version=1" , "attributes" : { "name" : "House Design.rvt" , "displayName" : "House Design.rvt" , "createTime" : "2016-05-24T19:25:23+00:00" , "createUserId" : "38SCJGX4R4PV" , "createUserName" : "John Doe" , "lastModifiedTime" : "2016-05-24T19:25:23+00:00" , "lastModifiedUserId" : "38SCJGX4R4PV" , "lastModifiedUserName" : "John Doe" , "versionNumber" : 1 , "mimeType" : "application/vnd.autodesk.revit" , "fileType" : "rvt" , "storageSize" : 12550144 , "extension" : { "type" : "versions:autodesk.core:File" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/versions%3Aautodesk.core%3AFile-1.0" }, "data" : {} } }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/versions/urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q%3Fversion%3D1" } }, "relationships" : { "item" : { "data" : { "type" : "items" , "id" : "urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/versions/urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q%3Fversion%3D1/item" } } }, "refs" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/versions/urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q%3Fversion%3D1/relationships/refs" }, "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/versions/urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q%3Fversion%3D1/refs" } } }, "derivatives" : { "data" : { "type" : "derivatives" , "id" : "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNmJWcjRFVkRTYU9weWtjemVRWVIyUT92ZXJzaW9uPTE" }, "meta" : { "link" : { "href" : "https://developer.api.autodesk.com/viewingservice/v1/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNmJWcjRFVkRTYU9weWtjemVRWVIyUT92ZXJzaW9uPTE" } } }, "thumbnails" : { "data" : { "type" : "thumbnails" , "id" : "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNmJWcjRFVkRTYU9weWtjemVRWVIyUT92ZXJzaW9uPTE" }, "meta" : { "link" : { "href" : "https://developer.api.autodesk.com/viewingservice/v1/thumbnails/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNmJWcjRFVkRTYU9weWtjemVRWVIyUT92ZXJzaW9uPTE" } } }, "storage" : { "data" : { "type" : "objects" , "id" : "urn:adsk.objects:os.object:wip.dm.prod/977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt" }, "meta" : { "link" : { "href" : "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt" } } } } } ] }
```

## Step 4: Find the storage location of the item

In the above example, we can see the House Design.rvt item listed.
Make note of the itemâs ID urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q .
The GET projects/:project_id/items/:item_id endpoint provides the storage location of the targeted item.

### Example

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q"
```

The resource provides the following response:

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q" } }, "data" : { "type" : "items" , "id" : "urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q" , "attributes" : { "displayName" : "House Design.rvt" , "createTime" : "2016-05-24T19:25:23+00:00" , "createUserId" : "38SCJGX4R4PV" , "createUserName" : "John Doe" , "lastModifiedTime" : "2016-05-24T19:25:23+00:00" , "lastModifiedUserId" : "38SCJGX4R4PV" , "lastModifiedUserName" : "John Doe" , "extension" : { "type" : "items:autodesk.core:File" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/items%3Aautodesk.core%3AFile-1.0" }, "data" : {} } }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q" } }, "relationships" : { "tip" : { "data" : { "type" : "versions" , "id" : "urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q?version=1" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q/tip" } } }, "versions" : { "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q/versions" } } }, "parent" : { "data" : { "type" : "folders" , "id" : "urn:adsk.wipprod:fs.folder:co.uvDiLQ5DRYidDQ_EFW1OOg" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q/parent" } } }, "refs" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q/relationships/refs" }, "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q/refs" } } } } }, "included" : [ { "type" : "versions" , "id" : "urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q?version=1" , "attributes" : { "name" : "House Design.rvt" , "displayName" : "House Design.rvt" , "createTime" : "2016-05-24T19:25:23+00:00" , "createUserId" : "38SCJGX4R4PV" , "createUserName" : "John Doe" , "lastModifiedTime" : "2016-05-24T19:25:23+00:00" , "lastModifiedUserId" : "38SCJGX4R4PV" , "lastModifiedUserName" : "John Doe" , "versionNumber" : 1 , "mimeType" : "application/vnd.autodesk.revit" , "fileType" : "rvt" , "storageSize" : 12550144 , "extension" : { "type" : "versions:autodesk.core:File" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/versions%3Aautodesk.core%3AFile-1.0" }, "data" : {} } }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/versions/urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q%3Fversion%3D1" } }, "relationships" : { "item" : { "data" : { "type" : "items" , "id" : "urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/versions/urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q%3Fversion%3D1/item" } } }, "refs" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/versions/urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q%3Fversion%3D1/relationships/refs" }, "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/versions/urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q%3Fversion%3D1/refs" } } }, "derivatives" : { "data" : { "type" : "derivatives" , "id" : "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNmJWcjRFVkRTYU9weWtjemVRWVIyUT92ZXJzaW9uPTE" }, "meta" : { "link" : { "href" : "https://developer.api.autodesk.com/viewingservice/v1/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNmJWcjRFVkRTYU9weWtjemVRWVIyUT92ZXJzaW9uPTE" } } }, "thumbnails" : { "data" : { "type" : "thumbnails" , "id" : "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNmJWcjRFVkRTYU9weWtjemVRWVIyUT92ZXJzaW9uPTE" }, "meta" : { "link" : { "href" : "https://developer.api.autodesk.com/viewingservice/v1/thumbnails/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNmJWcjRFVkRTYU9weWtjemVRWVIyUT92ZXJzaW9uPTE" } } }, "storage" : { "data" : { "type" : "objects" , "id" : "urn:adsk.objects:os.object:wip.dm.prod/977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt" }, "meta" : { "link" : { "href" : "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt" } } } } } ] }
```

## Step 5: Find the versions of an item

If you only want the latest version, you can simply get the link from the response body of the previous step.  In the above example, we can see the storage location of House Design.rvt in the included.relationships.storage.meta.link.href attribute ( https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt ) which can be used to download the item.

If you want a version other than the latest version, the GET projects/:project_id/items/:item_id/versions endpoint returns the versions of an uploaded item. Find the version of the resource item that you want to download.

### Example

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q/versions"
```

The resource provides the following response:

```
{ "jsonapi" : { "version" : "1.0" }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/items/urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q/versions" } }, "data" : [ { "type" : "versions" , "id" : "urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q?version=1" , "attributes" : { "name" : "House Design.rvt" , "displayName" : "House Design.rvt" , "createTime" : "2016-05-24T19:25:23+00:00" , "createUserId" : "38SCJGX4R4PV" , "createUserName" : "John Doe" , "lastModifiedTime" : "2016-05-24T19:25:23+00:00" , "lastModifiedUserId" : "38SCJGX4R4PV" , "lastModifiedUserName" : "John Doe" , "versionNumber" : 1 , "mimeType" : "application/vnd.autodesk.revit" , "fileType" : "rvt" , "storageSize" : 12550144 , "extension" : { "type" : "versions:autodesk.core:File" , "version" : "1.0" , "schema" : { "href" : "https://developer.api.autodesk.com/schema/v1/versions/versions%3Aautodesk.core%3AFile-1.0" }, "data" : {} } }, "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/versions/urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q%3Fversion%3D1" } }, "relationships" : { "item" : { "data" : { "type" : "items" , "id" : "urn:adsk.wipprod:dm.lineage:6bVr4EVDSaOpykczeQYR2Q" }, "links" : { "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/versions/urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q%3Fversion%3D1/item" } } }, "refs" : { "links" : { "self" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/versions/urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q%3Fversion%3D1/relationships/refs" }, "related" : { "href" : "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6cGUyOWNjZjMyI0QyMDE2MDUyNDEyOTI5NzY/versions/urn:adsk.wipprod:fs.file:vf.6bVr4EVDSaOpykczeQYR2Q%3Fversion%3D1/refs" } } }, "derivatives" : { "data" : { "type" : "derivatives" , "id" : "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNmJWcjRFVkRTYU9weWtjemVRWVIyUT92ZXJzaW9uPTE" }, "meta" : { "link" : { "href" : "https://developer.api.autodesk.com/viewingservice/v1/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNmJWcjRFVkRTYU9weWtjemVRWVIyUT92ZXJzaW9uPTE" } } }, "thumbnails" : { "data" : { "type" : "thumbnails" , "id" : "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNmJWcjRFVkRTYU9weWtjemVRWVIyUT92ZXJzaW9uPTE" }, "meta" : { "link" : { "href" : "https://developer.api.autodesk.com/viewingservice/v1/thumbnails/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuNmJWcjRFVkRTYU9weWtjemVRWVIyUT92ZXJzaW9uPTE" } } }, "storage" : { "data" : { "type" : "objects" , "id" : "urn:adsk.objects:os.object:wip.dm.prod/977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt" }, "meta" : { "link" : { "href" : "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt" } } } } } ] }
```

The response is similar to the one in Step 4 other than multiple versions of the item returned.

## Step 6: Get the S3 URL

The GET buckets/:bucket_key/objects/:object_key/signeds3download endpoint will generate a signed URL to an object, which can be used to download it directly from S3.

The following example shows how to get the signed url.

### Example

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt/signeds3download"
```

A successful response contains the signed url as per the following example.

```
{ "status" : "complete" , "url" : "https://cdn.us.oss.api.autodesk.com/com.autodesk.oss-persistent/us-east-1/3f/bf/5f/0137a7d9dc53af930bc1b527320d50fb5f/wip.dm.prod?response-content-type=application%2Foctet-stream&response-content-disposition=attachment%3B+filename%3D%977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt%22&Expires=1643864703&Signature=00PZYS6gL~Nc6aRG2HAhOCKYl0xtqsuujMJ~VKSXm1vBa-OxS4lPQBSlTx5bswpLBe1W6Rz94eIZW2sPN-v6Mzz~JyXNZ-V9Z7zlBoE1VoQhspLioC225hxq6ZmDSU5QnZXuNDV4ih~p1n3xacYvUvQWX-ONAGVUgQvZ253Svw~qx-pO4j-Yh4kVRmzDZqQut1xOI5ZGH6JFGhXLSzkgbYcfYx6fvCxnvYUJrgAcqncIwGVewI3uC0I84Fzrj8nXE8ojuojqJP0pNlxkfBe~2LfjjzqKDKaNvfC2Grt12j9QgC~cN7nQCRcVUhExpoV1VVB5x3AkVTJ-q5NoedvsfO__&Key-Pair-Id=95HRZD7MMO1UK" , "params" : { "content-type" : "application/octet-stream" , "content-disposition" : "attachment; filename=\"977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt\"" }, "size" : 472424 , "sha1" : "ffbf5f0137a7d9dc53af930bc1b527320d50fb53" }
```

Please refer to the linked endpoint to read more about expiry of signed URLs

## Step 7: Download the item

The signed url can be used download the requested file as per the following example.

Note: This download is directly from S3 (or a CDN) and as such doesnât need an âAuthorizationâ header.

### Example

```
curl -X GET "https://cdn.us.oss.api.autodesk.com/com.autodesk.oss-persistent/us-east-1/3f/bf/5f/0137a7d9dc53af930bc1b527320d50fb5f/wip.dm.prod?response-content-type=application%2Foctet-stream&response-content-disposition=attachment%3B+filename%3D%977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt%22&Expires=1643864703&Signature=00PZYS6gL~Nc6aRG2HAhOCKYl0xtqsuujMJ~VKSXm1vBa-OxS4lPQBSlTx5bswpLBe1W6Rz94eIZW2sPN-v6Mzz~JyXNZ-V9Z7zlBoE1VoQhspLioC225hxq6ZmDSU5QnZXuNDV4ih~p1n3xacYvUvQWX-ONAGVUgQvZ253Svw~qx-pO4j-Yh4kVRmzDZqQut1xOI5ZGH6JFGhXLSzkgbYcfYx6fvCxnvYUJrgAcqncIwGVewI3uC0I84Fzrj8nXE8ojuojqJP0pNlxkfBe~2LfjjzqKDKaNvfC2Grt12j9QgC~cN7nQCRcVUhExpoV1VVB5x3AkVTJ-q5NoedvsfO__&Key-Pair-Id=95HRZD7MMO1UK" --output "House Design.rvt"
```

Also, if a header in the format of âRange: bytes=<start>-<end>â is included, the url can be used for multithreaded download.

### Example

```
export DL_URL = "https://cdn.us.oss.api.autodesk.com/com.autodesk.oss-persistent/us-east-1/3f/bf/5f/0137a7d9dc53af930bc1b527320d50fb5f/wip.dm.prod?response-content-type=application%2Foctet-stream&response-content-disposition=attachment%3B+filename%3D%977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt%22&Expires=1643864703&Signature=00PZYS6gL~Nc6aRG2HAhOCKYl0xtqsuujMJ~VKSXm1vBa-OxS4lPQBSlTx5bswpLBe1W6Rz94eIZW2sPN-v6Mzz~JyXNZ-V9Z7zlBoE1VoQhspLioC225hxq6ZmDSU5QnZXuNDV4ih~p1n3xacYvUvQWX-ONAGVUgQvZ253Svw~qx-pO4j-Yh4kVRmzDZqQut1xOI5ZGH6JFGhXLSzkgbYcfYx6fvCxnvYUJrgAcqncIwGVewI3uC0I84Fzrj8nXE8ojuojqJP0pNlxkfBe~2LfjjzqKDKaNvfC2Grt12j9QgC~cN7nQCRcVUhExpoV1VVB5x3AkVTJ-q5NoedvsfO__&Key-Pair-Id=95HRZD7MMO1UK" curl -X GET -H "Range: bytes=0-199999" $DL_URL --output "House Design.rvt_pt1" curl -X GET -H "Range: bytes=200000-472723" $DL_URL --output "House Design.rvt_pt2" cat "House Design.rvt_pt1" "House Design.rvt_pt2" >House Design.rvt
rm "House Design.rvt_pt1" "House Design.rvt_pt2"
```
