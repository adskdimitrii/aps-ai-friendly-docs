# Add References To Issues

Source: https://aps.autodesk.com/en/docs/acc/tutorials/issues/add-references-to-issues/

---

# Add References To Issues

This tutorial demonstrates how to add references such as ACC photos to ACC issues. The steps include verifying the userâs permissions, finding the ID of the references (in this example, the photo) you want to add to the issue, and using the Relationships API to add it to the issue.

## Before You Begin

- Register an app

- Acquire a 3-legged OAuth token with the data:write scope.

- Verify that you have access to the relevant account and ACC project.

- Find the relevant project ID for the project you want to create an issue in by following the Retrieve a Project ID tutorial. In this example, assume the project ID is f6a1e3b5-abaa-4b01-b33a-5d55f36ba047 .

Note that we do not currently support document-related (pusphin) issues or linked documents.

## Step 1: Verify the Userâs Permissions

We recommend that you call GET users/me to verify that the user has permissions to add photos to issues. The user can add photos if the issues.new object appears in the response. See the Permissions Table for more information about permissions.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/users/me' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "id" : "BXQXL7646C2R" , "isProjectAdmin" : true , "canManageTemplates" : "" , "issues" : { "new" : { "permittedActions" : [ "add_comment" ], "permittedAttributes" : [ "title" ], "permittedStatuses" : [ "open" ], "permitted_actions" : [ "add_comment" ], "permitted_attributes" : [ "title" ], "permitted_statuses" : [ "open" ] } }, "permissionLevels" : [ "read" , "write" , "create" ] }
```

The user can add photos to issues if the issues.new object appears in the response. The user has manage issues permissions if create , write , read appears in the permissionLevels array. For more details about permission levels, see Issues Permissions .

## Step 2: Find the Issue ID

To find the issue ID of the issue you want to add the photo to, call `GET issues /en/docs/acc/v1/reference/http/issues-issues-GET/`_ using the project ID ( f6a1e3b5-abaa-4b01-b33a-5d55f36ba047 ).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/issues' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "pagination" : { "limit" : 10 , "offset" : 100 , "totalResults" : 25 }, "results" : [ { "id" : "3570f222-6c54-4b01-90e6-e701749f0222" , "containerId" : "2220f222-6c54-4b01-90e6-d701748f0222" , "deleted" : false , "displayId" : 7 , "title" : "Door missing a screw" , "description" : "The door is missing a screw, please fix this" , "snapshotUrn" : "" , "issueTypeId" : "8770f222-6c54-4e01-93e6-e701749f0222" , "issueSubtypeId" : "1370f222-6c54-3a01-93e6-e701749f0222" , "status" : "open" , "assignedTo" : "A3RGM375QTZ7" , "assignedToType" : "user" , "dueDate" : "2018-07-25" , "startDate" : "1982-06-01" , "locationId" : "35de6f24-39f5-4808-ba5f-6cbbe2a858e1" , "locationDetails" : "issue location details" , "linkedDocuments" : [ {} ], "links" : [ {} ], "ownerId" : "" , "rootCauseId" : "2370f222-6c54-3a01-93e6-f701772f0222" , "officialResponse" : {}, "issueTemplateId" : "" , "permittedStatuses" : [ "open" ], "permittedAttributes" : [ "title" ], "published" : true , "permittedActions" : {}, "commentCount" : 3 , "attachmentCount" : "" , "openedBy" : "A3RGM375QTZ7" , "openedAt" : "2018-07-22T15:05:58.033Z" , "closedBy" : "A3RGM375QTZ7" , "closedAt" : "2018-07-22T15:05:58.033Z" , "createdBy" : "A3RGM375QTZ7" , "createdAt" : "2018-07-22T15:05:58.033Z" , "updatedBy" : "A3RGM375QTZ7" , "updatedAt" : "2018-07-22T15:05:58.033Z" , "watchers" : [ "A3RGM375QTZ7" ], "customAttributes" : [ { "attributeDefinitionId" : "2220f222-6c54-4b01-90e6-d701748f0888" , "value" : "368" , "type" : "numeric" , "title" : "Cost Impact ($)" } ] } ] }
```

Note the ID ( results.[id] ) - ( 3570f222-6c54-4b01-90e6-e701749f0222 ) of the issue you want to add the photo to.

## Step 3: Find the Reference (Photo) ID

To find the ID of the photo you want to add to the issue, call GET photos using the project ID ( f6a1e3b5-abaa-4b01-b33a-5d55f36ba047 ) to get a list of all the photos for the project.

Note you cannot currently upload photos to the ACC Photo tool using the Photos API. You can only upload photos via the Photos UI. We will be supporting the photos API upload in the near future. As a workaround you can upload photos to the ACC Files tool using the Data Management API and add a file reference to the issue. See the Upload Files tutorial for details.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/photos/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/photos:filter' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \
```

### Response

```
{ "pagination" : { "limit" : 25 , "nextPost" : { "body" : { "cursorState" : "eyJsaW1pdCI6MjUsICJ0aXRsZSI6ICJ3YWxsIn0Ks" }, "url" : "https://developer.api.autodesk.com/construction/photos/v1/projects/8e52b200-f856-4f17-a57c-c03ba2f6673a/photos:filter" } }, "results" : [ { "createdAt" : "2021-03-14T10:20:33" , "createdBy" : "PER8KQPK2JRT" , "deletedAt" : "2021-03-19T11:50:33" , "deletedBy" : "PER8KQPK2JRT" , "description" : "The left side of the office" , "id" : "5439bfb7-8006-4388-a454-f02560f99566" , "isPublic" : false , "latitude" : 37.757497 , "locked" : false , "longitude" : -122.42115 , "mediaType" : "NORMAL" , "projectId" : "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047" , "signedUrls" : { "fileUrl" : "https://s3.amazonaws.com/com.autodesk.oss-persistent/f0/7b/66/4df1b73d0cc643e6179b85eae7d8d529d2/ce8edd30-ef28-467c-8d99-7d7051097ee0?response-content-disposition=attachment%3B%20filename%3D%22c35b8b28-859e-4256-a3bc-41772a673260.jpg%22&response-content-type=image%2Fjpeg&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCOKZyru7bEOWhRlJOiFZUwLwGSFSWPO5VknX%2BIisldAwIgWN6g5zYxXLOzdiZgR4sYuyY4qr1k1SAQOTOCI7EOmKIqvQMI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw5OTM3ODk5OTIwNjMiDK0wr6QcJBV%2BrqLz7iqRA55WGaeF1IZVyH5XzR%2FyR72VqyCRIEwm9D3Pt%2BTOxtaNa519ldQcvjYptWrlwnrgr1T9c3jxtEXxHZveX3XwgaSQq7JyHACBAMVwkKABwczEzPOryCvIJBWjgr2ABoYGr0dDCFdh9IjdoDrOrXDDesn4I5GamK%2BdNzXBR1MJH3ocmoZXxrmaJGigr62ShQ3q7AoqMgIX55XH8DnYMP4k9OlGGJsL7P80OnvOXfNLFl9EVJp5jnp%2BT1eO3FezRxc%2FqkeTG7t6QHh87P4cJKzWV9pW3AQoYvBKyQ5uJn5WA8%2FFg%2BhzYalr5Y%2B4%2FneB0xfn7WS2I%2FvjIo6rOkIqx7K3Ty1p1kuZ6e64%2BlEXx8mYHO2NOYobbSf%2Fx%2B7FU1rhZqvqUGB%2BRoMXFI%2FIkaxe%2B%2Ba6sZYV6Dm6bcim835asw%2B48vkt3XLZ6kBNqOJMdqvIBp%2F7opV9Bc4%2BMkhPc6wT%2BwAoQ0jHGuNZiLh%2BsxcB8EtwziI18v5LFw6WmffTQD3oc8WTb9xUZmoQ8qDq5z%2FY4%2BY2EAq6MNaP7oIGOusBXz4xrUPPH0cr5UO912gp6aysXFnqxu55it8zqPwiGI2Xe0RlaMTAMh1jwDZ4LZD4N2NERk%2F%2BlR1KaRk2Jvo34HIXVnUqNWlYAR3TyV2intl8wwJWlgKQH6DI%2BzwOJ27kDToULG5TQpQk6xAQaToplmERCien7Pi8vlb0JNBCzkoKNh40Z1wPxcS%2BitdU0IkD0n39bvWy5uG0hoUuifHr53vaf7eqFRSdrd%2B%2BYuJ00yT%2FtWS6FLpLKCSgZw8GKoAq3PpfPggmg99bAju7H%2FD8xfVgBPhb91tEGCCdyub4jDtj6euoUFXK%2FiMIVg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210324T193346Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=ASIA6OYT73R75HNE4VUO%2F20210324%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=e694954290d485482c6334b39b591c87e4a16ba2425f05da1dc25faf47afba2d" , "thumbnailUrl" : "https://s3.amazonaws.com/com.autodesk.oss-opsstaging-persistent/81/b8/3d/e2855b46af2060d595ce31923310079c4b/ce8edd30-ef28-467c-8d99-7d7051097ee0?response-content-disposition=attachment%3B%20filename%3D%22c35b8b28-859e-4256-a3bc-41772a673260_t.jpg%22&response-content-type=image%2Fjpeg&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCOKZyru7bEOWhRlJOiFZUwLwGSFSWPO5VknX%2BIisldAwIgWN6g5zYxXLOzdiZgR4sYuyY4qr1k1SAQOTOCI7EOmKIqvQMI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw5OTM3ODk5OTIwNjMiDK0wr6QcJBV%2BrqLz7iqRA55WGaeF1IZVyH5XzR%2FyR72VqyCRIEwm9D3Pt%2BTOxtaNa519ldQcvjYptWrlwnrgr1T9c3jxtEXxHZveX3XwgaSQq7JyHACBAMVwkKABwczEzPOryCvIJBWjgr2ABoYGr0dDCFdh9IjdoDrOrXDDesn4I5GamK%2BdNzXBR1MJH3ocmoZXxrmaJGigr62ShQ3q7AoqMgIX55XH8DnYMP4k9OlGGJsL7P80OnvOXfNLFl9EVJp5jnp%2BT1eO3FezRxc%2FqkeTG7t6QHh87P4cJKzWV9pW3AQoYvBKyQ5uJn5WA8%2FFg%2BhzYalr5Y%2B4%2FneB0xfn7WS2I%2FvjIo6rOkIqx7K3Ty1p1kuZ6e64%2BlEXx8mYHO2NOYobbSf%2Fx%2B7FU1rhZqvqUGB%2BRoMXFI%2FIkaxe%2B%2Ba6sZYV6Dm6bcim835asw%2B48vkt3XLZ6kBNqOJMdqvIBp%2F7opV9Bc4%2BMkhPc6wT%2BwAoQ0jHGuNZiLh%2BsxcB8EtwziI18v5LFw6WmffTQD3oc8WTb9xUZmoQ8qDq5z%2FY4%2BY2EAq6MNaP7oIGOusBXz4xrUPPH0cr5UO912gp6aysXFnqxu55it8zqPwiGI2Xe0RlaMTAMh1jwDZ4LZD4N2NERk%2F%2BlR1KaRk2Jvo34HIXVnUqNWlYAR3TyV2intl8wwJWlgKQH6DI%2BzwOJ27kDToULG5TQpQk6xAQaToplmERCien7Pi8vlb0JNBCzkoKNh40Z1wPxcS%2BitdU0IkD0n39bvWy5uG0hoUuifHr53vaf7eqFRSdrd%2B%2BYuJ00yT%2FtWS6FLpLKCSgZw8GKoAq3PpfPggmg99bAju7H%2FD8xfVgBPhb91tEGCCdyub4jDtj6euoUFXK%2FiMIVg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210324T193346Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=ASIA6OYT73R75HNE4VUO%2F20210324%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=fac56130302305057c9ae301503860edb2d296c43dcfb5a59ebf3744f5126baa" }, "size" : 11359 , "takenAt" : "2021-03-13T18:15:00" , "title" : "Office Dry Wall" , "type" : "FIELD-REPORT" , "updatedAt" : "2021-03-14T11:20:33" , "updatedBy" : "PER8KQPK2JRT" , "urls" : { "fileUrl" : "https://developer.api.autodesk.com/construction/photos/assets/ce8edd30-ef28-467c-8d99-7d7051097ee0/c35b8b28-859e-4256-a3bc-41772a673260.jpg\"" , "thumbnailUrl" : "https://developer.api.autodesk.com/construction/photos/assets/ce8edd30-ef28-467c-8d99-7d7051097ee0/c35b8b28-859e-4256-a3bc-41772a673260_t.jpg\"" }, "userCreatedAt" : "2021-03-13T18:20:33" } ] }
```

Note the ID ( results.[id] ) - ( 5439bfb7-8006-4388-a454-f02560f99566 ) of the photo you want to add to the issue.

If you want to add a new photo to the issue, upload the photo to ACC Docs using the Data Management API. See the Upload Files tutorial for details. Note the item ID ( included.[id] ) in the response.

## Step 4: Add the Reference (Photo) to the Issue

Use the Relationships API to add the photo to the issue. Call PUT relationships using the project ID ( f6a1e3b5-abaa-4b01-b33a-5d55f36ba047 ), the photo ID ( 5439bfb7-8006-4388-a454-f02560f99566 ), and the issue ID ( 3570f222-6c54-4b01-90e6-e701749f0222 ).

If you uploaded the photo via the Photos UI, use the following types and domains:

For the issue: use an issue type, and an autodesk-bim360-issue domain.
For the photo: use a photo type, and an autodesk-contruction-photo domain.

If you uploaded the photo to ACC Files using the Data Management API, use the following types and domains:

For the issue: use an issue type, and an autodesk-bim360-issue domain. (Note that the issues API currently uses the autodesk-bim360-issue domain for both for both ACC and BIM 360 relationships.)
For the file: use a documentlineage type, and an autodesk-bim360-documentmanagement domain.

Note that container ID in the relationships ID is equivalent to the project ID.

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/relationships' \ -X PUT \ -H 'Authorization: Bearer <token>' \ -H 'Content-Type: application/json' \ -d '[ { "entities": [ { "domain": "autodesk-bim360-issue", "type": "issue", "id": "3570f222-6c54-4b01-90e6-e701749f0222", "createdOn": "2021-07-29T11:39:12+01:00" }, { "domain": "autodesk-construction-photo", "type": "photo", "id": "5439bfb7-8006-4388-a454-f02560f99566", "createdOn": "2021-07-29T13:39:12+01:00" } ] } ]'
```

### Response (200)

```
[ { "id" : "74b70bb8-8802-a1fd-f201-890375a60c8f" , "createdOn" : "2015-10-21T16:32:22Z" , "isReadOnly" : true , "isService" : false , "isDeleted" : false , "entities" : [ { "domain" : "autodesk-bim360-issue" , "type" : "issue" , "id" : "3570f222-6c54-4b01-90e6-e701749f0222" , "createdOn" : "2021-07-29T11:39:12+01:00" }, { "domain" : "autodesk-construction-photo" , "type" : "photo" , "id" : "5439bfb7-8006-4388-a454-f02560f99566" , "createdOn" : "2021-07-29T13:39:12+01:00" } ] } ]
```

Congratulations! You have added a photo to an ACC issue.
