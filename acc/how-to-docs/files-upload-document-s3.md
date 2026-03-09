# Upload Files to the ACC Files Tool

Source: https://aps.autodesk.com/en/docs/acc/tutorials/files/upload-document-s3/

---

# Upload Files to the ACC Files Tool

This tutorial demonstrates how to upload files to the ACC Files tool. The steps include finding the ID of the folder where you want to upload the files, creating an empty storage object for the file, generating a signed S3 URL, uploading the file to the signed URL, creating the first version of the file, and, optionally, creating additional versions of the file.

If you want to upload a file to ACC Sheets, see the [Upload Sheets](https://aps.autodesk.com/en/docs/acc/v1/tutorials/sheets/upload-sheets/) tutorial.

In order to complete the upload process, you need to manually review and publish the file in ACC Files. For more details, see the [Help documentation](https://help.autodesk.com/view/DOCS/ENU/?guid=Upload_files).

For more details about ACC Document management, see the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/overview/).

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps), and select the Data Management and Autodesk Construction Cloud APIs.
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:create` `data:read` and `data:write` scopes.
- Verify that you have access to the relevant ACC account, project, and folder.

## [Step 1: Find the Hub ID for the ACC Account](#step-1-find-the-hub-id-for-the-acc-account)

The first few steps of the tutorial demonstrate how to create an empty storage object in the folder where you want to upload the file. This involves iterating through several Data Management endpoints to find the folder ID.

Call [GET hubs](../../data/http-docs/http-hubs-GET.md) to find the hub ID for the ACC account that contains the folder you want to upload the file to.

Note that the ACC account ID corresponds to a Data Management hub ID. To convert an account ID into a hub ID you need to add a â**b.**" prefix. For example, an account ID of c8b0c73d-3ae9 translates to a hub ID of **b.**c8b0c73d-3ae9.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs"

```

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/project/v1/hubs"
    }
  },
  "data": [
    {
      "type": "hubs",
      "id": "b.cGVyc29uYWw6cGUyOWNjZjMy",
      "attributes": {
        "name": "My First Account",
        "extension": {
          "type": "hubs:autodesk.bim360:Account",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/hubs:autodesk.bim360:Account-1.0"
          },
          "data": {}
        }
      }
    }
  ]
}

```

Show More

In this example, assume that the folder you want to upload the file to is in a hub called `My First Account`.

Find the hub (`data.name`), and note the hub ID - `b.cGVyc29uYWw6cGUyOWNjZjMy`.

## [Step 2: Find the Project ID](#step-2-find-the-project-id)

Use the hub ID (`b.cGVyc29uYWw6cGUyOWNjZjMy`) to call [GET hubs/:hub_id/projects](../../data/http-docs/http-hubs-hub_id-projects-GET.md) to get a list of all the projects in the hub. Find the project ID of the project that contains the folder you want to upload the file to.

Note that the project ID in ACC corresponds to the project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). To convert a project ID in ACC to a project ID in the Data Management API, you need to add a â**b.**" prefix. For example, a project ID of a4be0c34a-4ab7 translates to a project ID of **b.**a4be0c34a-4ab7.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs/b.cGVyc29uYWw6cGUyOWNjZjMy/projects"

```

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/project/v1/hubs/b.cGVyc29uYWw6cGUyOWNjZjMy/projects"
    }
  },
  "data": [
    {
      "type": "projects",
      "id": "b.cGVyc29uYWw6d2l",
      "attributes": {
        "name": "My First Project",
        "extension": {
          "type": "projects:autodesk.core:Project",
          "version": "1.0"
        }
      }
    }
  ]
}

```

Show More

In this example, assume that `My First Project` is the project that contains the folder you want to upload the file to.

Find the project (`data.attributes.name`), and note the project ID (`data.id`) - `b.cGVyc29uYWw6d2l`.

## [Step 3: Find the Folder ID](#step-3-find-the-folder-id)

Use the hub ID (`b.cGVyc29uYWw6cGUyOWNjZjMy`) and the project ID (`b.cGVyc29uYWw6d2l`) to call [GET hubs/:hub_id/projects/:project_id/topFolders](../../data/http-docs/http-hubs-hub_id-projects-project_id-topFolders-GET.md) to get the top-level folders.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT"
            "https://developer.api.autodesk.com/project/v1/hubs/b.cGVyc29uYWw6cGUyOWNjZjMy/projects/b.cGVyc29uYWw6d2l/topFolders"

```

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "data": [
    {
      "type": "folders",
      "id": "urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA",
      "attributes": {
        "name": "Project Files",
        "displayName": "Project Files",
        "createTime": "2017-07-17T13:06:56.0000000Z",
        "createUserId": "",
        "createUserName": "",
        "lastModifiedTime": "2017-09-24T07:46:08.0000000Z",
        "lastModifiedUserId": "X9WYLGPNCHSL",
        "lastModifiedUserName": "John Smith",
        "objectCount": 4,
        "hidden": false,
        "extension": {
          "type": "folders:autodesk.bim360:Folder",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/folders:autodesk.bim360:Folder-1.0"
          },
          "data": {
            "visibleTypes": [
              "items:autodesk.bim360:File"
            ],
            "actions": [
              "CONVERT"
            ],
            "allowedTypes": [
              "items:autodesk.bim360:File",
              "folders:autodesk.bim360:Folder"
            ]
          }
        }
      }
    }
  ]
}

```

Show More

Find the relevant folder (`data.attributes.name`); in this example, the Project Files folder, and note the folder ID (`data.id`) - `urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA`

## [Step 4: Find the Nested Folder ID](#step-4-find-the-nested-folder-id)

If you want to upload the document to a folder nested under the top-level folder, you need to call [GET projects/:project_id/folders/:folder_id/contents](../../data/http-docs/http-projects-project_id-folders-folder_id-contents-GET.md) repeatedly through the hierarchy of folders until you find the Folder ID of the folder you want to upload the document to. For the first iteration, use the top-level folder ID. (`urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA`).

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT"
    "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/folders/urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA/contents"

```

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "data": [
    {
      "type": "folders",
      "id": "urn:adsk.wipprod:fs.folder:co.QneBBX7evT2JSrpeQXga0",
      "attributes": {
        "name": "My First Files",
        "displayName": "My First Files",
        "createTime": "2017-07-17T13:06:56.0000000Z",
        "createUserId": "",
        "createUserName": "",
        "lastModifiedTime": "2017-09-24T07:46:08.0000000Z",
        "lastModifiedUserId": "X9WYLGPNCHSL",
        "lastModifiedUserName": "John Smith",
        "objectCount": 4,
        "hidden": false,
        "extension": {
          "type": "folders:autodesk.bim360:Folder",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/folders:autodesk.bim360:Folder-1.0"
          },
          "data": {
            "visibleTypes": [
              "items:autodesk.bim360:File"
            ],
            "actions": [
              "CONVERT"
            ],
            "allowedTypes": [
              "items:autodesk.bim360:File",
              "folders:autodesk.bim360:Folder"
            ]
          }
        }
      }
    }
  ]
}

```

Show More

In this example, assume that `My First Files` is the folder that contains the file you want to upload.

Find the folder (`data.attributes.name`), and note the folder ID (`data.id`) - `urn:adsk.wipprod:fs.folder:co.QneBBX7evT2JSrpeQXga0`.

## [Step 5: Create a Storage Object](#step-5-create-a-storage-object)

Use the project ID (`b.cGVyc29uYWw6d2l`) and the folder ID (`urn:adsk.wipprod:fs.folder:co.QneBBX7evT2JSrpeQXga0`) to call [POST projects/:project_id/storage](../../data/http-docs/http-projects-project_id-storage-POST.md) to create an empty storage object for the file in the folder.

Note that you need to assign a filename and file extension (PNG or JPG) to the `name` parameter (`My First File.jpg`).

### Request

```
curl -X POST -H "Content-Type: application/vnd.api+json" -H "Accept: application/vnd.api+json" -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT"
"https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/storage"
-d '{
      "jsonapi": { "version": "1.0" },
      "data": {
        "type": "objects",
        "attributes": {
          "name": "My First File.jpg"
        },
        "relationships": {
          "target": {
            "data": { "type": "folders", "id": "urn:adsk.wipprod:fs.folder:co.QneBBX7evT2JSrpeQXga0" }
          }
        }
      }
}'

```

Show More

### Repsonse

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "data": {
    "type": "objects",
    "id": "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg",
    "relationships": {
      "target": {
        "data": {
          "type": "folders",
          "id": "urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA"
        }
      }
    }
  }
}

```

Show More

Note the object ID (`data.id`) - `urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg`.

The object ID includes the following sections: `<urn:adsk.objects:os.object>:<bucket key>/<object key>`

Note the bucket key - `wip.dm.prod` and the object key - `2a6d61f2-49df-4d7b.jpg`

## [Step 6: Generate a Signed S3 URL](#step-6-generate-a-signed-s3-url)

Use the bucket key (`wip.dm.prod`) and the object key (`2a6d61f2-49df-4d7b.jpg`) to call [GET buckets/:bucketKey/objects/:objectKey/signeds3upload](../../data/http-docs/http-buckets--bucketKey-objects--objectKey-signeds3upload-GET.md) to generate a signed URL for the storage object.

This endpoint supports generating multiple signed URLs, which allows you to upload multiple chunks of the same file in parallel. For more information, see [GET signeds3upload](../../data/http-docs/http-buckets--bucketKey-objects--objectKey-signeds3upload-GET.md).

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/2a6d61f2-49df-4d7b.jpg/signeds3upload"

```

### Repsonse

```
{
  "uploadKey": "AQICAHifrJ6-BSHUmjAat4..........QWI-fuvghN23akgePMdmykV",
  "uploadExpiration": "2022-02-05T00:00:00Z",
  "urlExpiration": "2022-02-03T05:23:29Z",
  "urls": [
      "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/26668812-6bb1-4f80-bab2-09776f24fd98?uploadId=[UPLOAD_ID]&partNumber=1&X-Amz-Security-Token=[AMZ_TOKEN]%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220203T052230Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=[AMZ_CREDENTIAL]%2F20220203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=[AMZ_SIGNATURE]"
  ]
}

```

Show More

Note the `uploadKey` and the `urls` response attributes.

## [Step 7: Upload a File to the Signed URL](#step-7-upload-a-file-to-the-signed-url)

To upload the file to the signed URL, use a PUT method and the `urls` attribute as the URI.

Note that you should not use a bearer token with this call.

### Request

```
curl -X PUT --data-binary @D:\My First File.jpg "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/26668812-6bb1-4f80-bab2-09776f24fd98?uploadId=[UPLOAD_ID]&partNumber=1&X-Amz-Security-Token=[AMZ_TOKEN]%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220203T052230Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=[AMZ_CREDENTIAL]%2F20220203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=[AMZ_SIGNATURE]"

```

Note that a successful call (`200`) returns an empty response.

## [Step 8: Complete the Upload](#step-8-complete-the-upload)

Use the bucket key (`wip.dm.prod`) the object key (`` 2a6d61f2-49df-4d7b.jpg` ``) and the upload key (`AQICAHifrJ6-BSHUmjAat4..........QWI-fuvghN23akgePMdmykV`) to call [POST buckets/:bucket_key/objects/:object_key/signeds3upload](../../data/http-docs/http-buckets--bucketKey-objects--objectKey-signeds3upload-POST.md) to complete the upload.

This endpoint needs to be called within 24 hours from the time you began uploading the file.

### Request

```
curl -X POST -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" --data-raw '{"uploadKey":"AQICAHifrJ6-BSHUmjAat4..........QWI-fuvghN23akgePMdmykV"}' "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg/signeds3upload"

```

### Repsonse

```
{
  "bucketKey" : "wip.dm.prod",
  "objectId" : "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg",
  "objectKey" : "2ac28abc-9f6e-463d-bcc4-5c194d552beb.jpg",
  "size" : 879394,
  "contentType" : "application/octet-stream",
  "location" : "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg"
}

```

Show More

The file has been uploaded to the storage object.

## [Step 9: Create the First Version of the File](#step-9-create-the-first-version-of-the-file)

Use the project ID (`b.cGVyc29uYWw6d2l`), the folder ID (`urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA`), and the Object ID (`urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg`) to call [POST projects/:project_id/items](../../data/http-docs/http-projects-project_id-items-POST.md) to create the first version of the uploaded file.

### Request

```
curl -X POST -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" -H "Content-Type: application/vnd.api+json" -H "Accept: application/vnd.api+json"
"https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items" -d '{
    "jsonapi": { "version": "1.0" },
    "data": {
      "type": "items",
      "attributes": {
        "displayName": "My First File.jpg",
        "extension": {
          "type": "items:autodesk.bim360:File",
          "version": "1.0"
        }
      },
      "relationships": {
        "tip": {
          "data": {
            "type": "versions", "id": "1"
          }
        },
        "parent": {
          "data": {
            "type": "folders",
            "id": "urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA"
          }
        }
      }
    },
    "included": [
      {
        "type": "versions",
        "id": "1",
        "attributes": {
          "name": "My First File.jpg",
          "extension": {
            "type": "versions:autodesk.bim360:File",
            "version": "1.0"
          }
        },
        "relationships": {
          "storage": {
            "data": {
              "type": "objects",
              "id": "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg"
            }
          }
        }
      }
    ]
  }'

```

Show More

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/items"
    }
  },
  "data": {
    "type": "items",
    "id": "urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ",
    "attributes": {
      "displayName": "My First File.jpg",
      "createTime": "2016-05-30T15:32:05+00:00",
      "createUserId": "KPN8P8P65K",
      "createUserName": "John Smith",
      "lastModifiedTime": "2016-05-30T15:32:05+00:00",
      "lastModifiedUserId": "KPN8P8P65K",
      "lastModifiedUserName": "John Smith",
      "extension": {
        "type": "items:autodesk.core:File",
        "version": "1.0",
        "schema": {
          "href": "https://developer.api.autodesk.com/schema/v1/versions/items%3Aautodesk.core%3AFile-1.0"
        },
        "data": {}
      }
    },
    "included": [
      {
        "type": "versions",
        "id": "urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ?version=1",
        "attributes": {
          "name": "My First File.jpg",
          "displayName": "My First File.jpg",
          "createTime": "2016-05-30T15:32:05+00:00",
          "createUserId": "KPN8P8P65K",
          "createUserName": "John Smith",
          "lastModifiedTime": "2016-05-30T15:32:05+00:00",
          "lastModifiedUserId": "KPN8P8P65K",
          "lastModifiedUserName": "John Smith",
          "versionNumber": 1,
          "mimeType": "application/image",
          "fileType": "jpg",
          "storageSize": 879394,
          "extension": {
            "type": "versions:autodesk.core:File",
            "version": "1.0",
            "schema": {
              "href": "https://developer.api.autodesk.com/schema/v1/versions/versions%3Aautodesk.core%3AFile-1.0"
            },
            "data": {}
          }
        }
      }
    ]
  }
}

```

Show More

Note the item ID (`data.id`) - `urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ`, and version ID (`inlcuded[id]`) - `urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ?version=1`.

## [Step 10: Create Additional Versions of the File](#step-10-create-additional-versions-of-the-file)

To create an additional version of the file, you need to create a new storage object (step 5), upload the new version to the object (step 6), and use the item ID you retrieved in step 7 to call [POST projects/:project_id/versions](../../data/http-docs/http-projects-project_id-versions-POST.md).

### Request

```
   curl -X POST -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" -H "Content-Type: application/vnd.api+json" -H "Accept: application/vnd.api+json" -d '{
  "jsonapi": { "version": "1.0" },
    "data": {
     "type": "versions",
       "attributes": {
          "name": "New Version of My First File.jpg",
          "extension": { "type": "versions:autodesk.bim360:File", "version": "1.0"}
       },
        "relationships": {
        "item": { "data": { "type": "items", "id": "urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ" } },
        "storage": { "data": { "type": "objects", "id": "<new_object_ID>" } }
      }
   }
}' "https://developer.api.autodesk.com/data/v1/projects/b.cGVyc29uYWw6d2l/versions"

```

Show More

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "data": {
    "type": "versions",
    "id": "urn:adsk.wipprod:fs.file:vf.1HROnsnfQgq4N0b-nUoGge?version=2",
    "attributes": {
      "name": "New Version of My First File.jpg",
      "displayName": "new version of my first file.jpg",
      "extension": {
        "type": "versions:autodesk.bim360:File",
        "version": "1.0",
        "data": {}
      }
    },
    "relationships": {}
  },
  "included": [
    {
      "type": "items",
      "id": "urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ",
      "attributes": {
        "extension": {
          "type": "items:autodesk.bim360:File",
          "version": "1.0",
          "data": {}
        }
      },
      "links": {},
      "relationships": {
        "tip": {
          "data": {
            "type": "versions",
            "id": "urn:adsk.wipprod:fs.file:vf.1HROnsnfQgq4N0b-nUoGge?version=2"
          },
          "links": {}
        },
        "versions": {},
        "parent": {},
        "refs": {},
        "links": {}
      }
    }
  ]
}

```

Show More

Congratulations! You have uploaded a file to the ACC Files tool.
