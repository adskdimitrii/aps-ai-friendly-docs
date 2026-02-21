# Download Files from the ACC Files Tool

Source: https://aps.autodesk.com/en/docs/acc/tutorials/files/download-document-s3/

---

# Download Files from the ACC Files Tool

This tutorial demonstrates how to download files from the ACC Files tool. The steps include finding the ID of the folder that contains the file, locating the storage object for the file, generating a signed S3 URL, and downloading the file from the signed S3 URL.

For more details about the ACC files management, see the [Data Management API](/en/docs/data/v2/overview/).

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps), and select the Data Management and Autodesk Construction Cloud APIs.
- Acquire a [3-legged OAuth token](/en/docs/oauth/v2/tutorials/get-3-legged-token/) with `data:create` `data:read` and `data:write` scopes.
- Verify that you have access to the relevant ACC account and ACC project.
- Note the name of the ACC account, project, and folder that contains the file you want to download.

## [Step 1: Find the Hub ID for the ACC Account](#step-1-find-the-hub-id-for-the-acc-account)

The first few steps of the tutorial demonstrate how to find the ID of the folder that contains the file you want to download, which invovles iterating through several Data Management endpoints.

Call [GET hubs](/en/docs/data/v2/reference/http/hubs-GET/) to find the hub ID for the ACC account that contains the file you want to download.

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
          "type": "hubs:autodesk.acc:Account",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/hubs:autodesk.acc:Account-1.0"
          },
          "data": {}
        }
      }
    }
  ]
}

```

Show More

In this example, assume that the account (and the corresponding Data Management hub) that contains the file you want to download is called `My First Account`.

Find the hub (`data.name`), and note the hub ID - `b.cGVyc29uYWw6cGUyOWNjZjMy`.

## [Step 2: Find the Project ID](#step-2-find-the-project-id)

Use the hub ID (`b.cGVyc29uYWw6cGUyOWNjZjMy`) to call [GET hubs/:hub_id/projects](/en/docs/data/v2/reference/http/hubs-hub_id-projects-GET) to get a list of all the projects in the hub. Find the project ID of the project that contains the folder you want to download the file from.

Note that the project ID in ACC corresponds to the project ID in the [Data Management API](/en/docs/data/v2/). To convert a project ID in ACC to a project ID in the Data Management API, you need to add a â**b.**" prefix. For example, a project ID of a4be0c34a-4ab7 translates to a project ID of **b.**a4be0c34a-4ab7.

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
       "data": [{
               "type": "projects",
               "id": "b.cGVyc29uYWw6d2l",
               "attributes": {
                       "name": "My First Project",
                       "extension": {
                               "type": "projects:autodesk.core:Project",
                               "version": "1.0"
                       }
               }
       }]
}

```

Show More

In this example, assume that `My First Project` is the project that contains the folder you want to download the document from.

Find the project (`data.attributes.name`), and note the project ID (`data.id`) - `b.cGVyc29uYWw6d2l`.

## [Step 3: Find the Folder ID](#step-3-find-the-folder-id)

Use the hub ID (`b.cGVyc29uYWw6cGUyOWNjZjMy`) and the project ID (`b.cGVyc29uYWw6d2l`) to call [GET hubs/:hub_id/projects/:project_id/topFolders](/en/docs/data/v2/reference/http/hubs-hub_id-projects-project_id-topFolders-GET) to get the top-level folders.

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

      "data": [{
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
                              "type": "folders:autodesk.acc:Folder",
                              "version": "1.0",
                              "schema": {
                                      "href": "https://developer.api.autodesk.com/schema/v1/versions/folders:autodesk.acc:Folder-1.0"
                              },
                              "data": {
                                      "visibleTypes": [
                                              "items:autodesk.acc:File"
                                      ],
                                      "actions": [
                                              "CONVERT"
                                      ],
                                      "allowedTypes": [
                                              "items:autodesk.acc:File",
                                              "folders:autodesk.acc:Folder"
                                      ]
                              }
                      }
              }
      }]
}

```

Show More

Find the relevant folder (`data.attributes.name`), and note the folder ID (`data.id`) - `urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA`

If you want to download a file from a folder nested under the top-level folder, you need to call [GET projects/:project_id/folders/:folder_id/contents](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET) repeatedly through the hierarchy of folders until you find the Folder ID of the folder you want to upload the file to. For the first iteration, use the top-level folder ID (`urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA`).

## [Step 4: Find the Storage Object ID for the File](#step-4-find-the-storage-object-id-for-the-file)

Use the project ID (`b.cGVyc29uYWw6d2l`) and the Projet Files folder ID (`urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA`) to call [GET projects/:project_id/folders/:folder_id/contents](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET) to get the storage object ID.

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
      "included": [{
              "type": "versions",
              "id": "urn:adsk.wipprod:fs.file:vf.II0yMfUPQl6DaOl5z-dhcg?version=1",
              "attributes": {
                      "name": "My First File.dwg",
                      "displayName": "My First File.dwg",
                      "createTime": "2017-10-02T11:06:44.0000000Z",
                      "createUserId": "X9WYLGPNCHVK",
                      "createUserName": "John Smith",
                      "lastModifiedTime": "2017-10-02T11:07:45.0000000Z",
                      "lastModifiedUserId": "X9WYLGPNCHVK",
                      "lastModifiedUserName": "John Smith",
                      "versionNumber": 1,
                      "storageSize": 1952608,
                      "fileType": "dwg",
                      "extension": {
                              "type": "versions:autodesk.acc:File",
                              "version": "1.0",
                              "schema": {
                                      "href": "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.acc:File-1.0"
                              },
                              "data": {
                                      "processState": "PROCESSING_COMPLETE",
                                      "extractionState": "FAILED",
                                      "splittingState": "NOT_SPLIT",
                                      "reviewState": "NOT_IN_REVIEW",
                                      "revisionDisplayLabel": "1"
                              }
                      }
              },
              "links": {
                      "relationships": {
                              "storage": {
                                      "data": {
                                              "type": "objects",
                                              "id": "urn:adsk.objects:os.object:wip.dm.prod/72d5e7e4-89a7-4cb9-9da0-2e2bbc61ca8e.dwg"
                                      },
                                      "meta": {
                                              "link": {
                                                      "href": "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/72d5e7e4-89a7-4cb9-9da0-2e2bbc61ca8e.dwg"
                                              }
                                      }
                              }
                      }
              }
      }]

```

Show More

}

In this example, assume that `My First File` is the file that you want to download.

Find the file (`included.attributes.name`), and note the storage object ID (`relationships.storage.data.id`) - `urn:adsk.objects:os.object:wip.dm.prod/72d5e7e4-89a7-4cb9-9da0-2e2bbc61ca8e.dwg`.

The storage object ID includes of the following sections: `<urn:adsk.objects:os.object>:<bucket_key>/<object_key>`

Note the bucket key - `wip.dm.prod` and the storage object key - `72d5e7e4-89a7-4cb9-9da0-2e2bbc61ca8e.dwg`

## [Step 5: Generate a Signed S3 URL](#step-5-generate-a-signed-s3-url)

Use the bucket key (`wip.dm.prod`) and the object key (`72d5e7e4-89a7-4cb9-9da0-2e2bbc61ca8e.dwg`) to call [GET buckets/:bucketKey/objects/:objectKey/signeds3download](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3download-GET) to generate a signed URL for the storage object, which you can use to download the file directly from S3.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/72d5e7e4-89a7-4cb9-9da0-2e2bbc61ca8e.dwg/signeds3download"

```

### Response

```
{
  "status": "complete",
  "url": "https://cdn.us.oss.api.autodesk.com/com.autodesk.oss-persistent/us-east-1/3f/bf/5f/0137a7d9dc53af930bc1b527320d50fb5f/wip.dm.prod?response-content-type=application%2Foctet-stream&response-content-disposition=attachment%3B+filename%3D%977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt%22&Expires=1643864703&Signature=00PZYS6gL~Nc6aRG2HAhOCKYl0xtqsuujMJ~VKSXm1vBa-OxS4lPQBSlTx5bswpLBe1W6Rz94eIZW2sPN-v6Mzz~JyXNZ-V9Z7zlBoE1VoQhspLioC225hxq6ZmDSU5QnZXuNDV4ih~p1n3xacYvUvQWX-ONAGVUgQvZ253Svw~qx-pO4j-Yh4kVRmzDZqQut1xOI5ZGH6JFGhXLSzkgbYcfYx6fvCxnvYUJrgAcqncIwGVewI3uC0I84Fzrj8nXE8ojuojqJP0pNlxkfBe~2LfjjzqKDKaNvfC2Grt12j9QgC~cN7nQCRcVUhExpoV1VVB5x3AkVTJ-q5NoedvsfO__&Key-Pair-Id=95HRZD7MMO1UK",
  "params": {
    "content-type": "application/octet-stream",
    "content-disposition": "attachment; filename=\"977d69b1-43e7-40fa-8ece-6ec4602892f3.rvt\""
  },
  "size": 472424,
  "sha1": "ffbf5f0137a7d9dc53af930bc1b527320d50fb53"
}

```

Show More

## [Step 6: Download the File](#step-6-download-the-file)

To download the file from the signed URL, use a GET method and the `url` attribute as the URI.

Note that you should not use a bearer token with this call.

### Request

```
curl -X GET "https://cdn.us.oss.api.autodesk.com/com.autodesk.oss-persistent/us-east-1/3f/bf/5f/0137a7d9dc53af930bc1b527320d50fb5f/wip.dm.prod?response-content-type=application%2Foctet-stream&response-content-disposition=attachment%3B+filename%3D%977d69b1-43e7-40fa-8ece-6ec4602892f3.dwg%22&Expires=1643864703&Signature=00PZYS6gL~Nc6aRG2HAhOCKYl0xtqsuujMJ~VKSXm1vBa-OxS4lPQBSlTx5bswpLBe1W6Rz94eIZW2sPN-v6Mzz~JyXNZ-V9Z7zlBoE1VoQhspLioC225hxq6ZmDSU5QnZXuNDV4ih~p1n3xacYvUvQWX-ONAGVUgQvZ253Svw~qx-pO4j-Yh4kVRmzDZqQut1xOI5ZGH6JFGhXLSzkgbYcfYx6fvCxnvYUJrgAcqncIwGVewI3uC0I84Fzrj8nXE8ojuojqJP0pNlxkfBe~2LfjjzqKDKaNvfC2Grt12j9QgC~cN7nQCRcVUhExpoV1VVB5x3AkVTJ-q5NoedvsfO__&Key-Pair-Id=95HRZD7MMO1UK" --output "My First File.dwg"

```

Congratulations! You have downloaded a file from the ACC Files tool.
