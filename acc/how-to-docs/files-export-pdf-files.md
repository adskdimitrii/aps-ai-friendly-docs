# Export Files from the ACC Files Tool

Source: https://aps.autodesk.com/en/docs/acc/tutorials/files/export-pdf-files/

---

# Export Files from the ACC Files Tool

This tutorial demonstrates how to export PDF, RVT and DWG files that were uploaded to the ACC Files module. The steps include finding the IDs of the files you want to export, exporting the files (you can optionally also export associated markups and hyperlinks), verifying the status of the export, getting a download link, and downloading the exported files.

Note that you can only export PDF, RVT, and DWG files. A maximum of 200 files is allowed in a single export operation. When exporting multiple files at once, they will be compressed and exported as a single ZIP file.

For more information about exporting files, see the [Export Files help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Export_Files).

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps), and select Autodesk Construction Cloud API.
- [Provision your app](/en/docs/bim360/v1/tutorials/getting-started/manage-access-to-docs/) to acquire access to your ACC account.
- Acquire a [3-legged OAuth token](/en/docs/oauth/v2/tutorials/get-3-legged-token/) with `data:write` scope.
- Find the relevant hub ID and project ID for the project from which you want to export files by following the [Retrieve a Project ID](/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. Assume that the hub ID is `b.cGVyc29uYWw6cGUyOWNjZjMy`, and the project ID is `b.139532ee-5cdb-4c9e-a293-652693991e65`.
- Verify that you have access to the relevant ACC project.

## [Step 1: Find the Folder ID of the Files to Export](#step-1-find-the-folder-id-of-the-files-to-export)

You first need to find the folder ID of the folder containing the files you want to export. Start by retrieving the parent folder ID, then, if necessary, iterate through the child folders until you locate the correct folder ID.

To find the parent folder ID, use the hub ID (`b.cGVyc29uYWw6cGUyOWNjZjMy`) and project ID (`b.139532ee-5cdb-4c9e-a293-652693991e65`) to call [GET hubs/:hub_id/projects/:project_id/topFolders](/en/docs/data/v2/reference/http/hubs-hub_id-projects-project_id-topFolders-GET).

### Request

```
curl -X GET "https://developer.api.autodesk.com/project/v1/hubs/b.cGVyc29uYWw6cGUyOWNjZjMy/projects/b.139532ee-5cdb-4c9e-a293-652693991e65/topFolders" \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT"

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
        "name": "Plans",
        "displayName": "Plans",
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
              "items:autodesk.bim360:Document"
            ],
            "actions": [
              "CONVERT",
              "SPLIT",
              "OCR"
            ],
            "allowedTypes": [
              "items:autodesk.bim360:File",
              "folders:autodesk.bim360:Folder",
              "items:autodesk.bim360:Document",
              "items:autodesk.bim360:TitleBlock",
              "items:autodesk.bim360:ReviewDocument"
            ]
          }
        }
      }
    }
  ]
}

```

Show More

Note the folder ID - `data.id` (`urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA`).

If you want to export a file from a folder nested under the parent folder, you need to call [GET projects/:project_id/folders/:folder_id/contents](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET) repeatedly through the hierarchy of folders until you find the folder ID of the folder that contains the files you want to export.

## [Step 2: Find the Version IDs of the Files to Export](#step-2-find-the-version-ids-of-the-files-to-export)

To export the files, youâll also need the version IDs of the files. To find the version IDs, use the project ID (`b.139532ee-5cdb-4c9e-a293-652693991e65`), and the folder ID (`urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA`) to call [GET projects/:project_id/folders/:folder_id/contents](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET).

Note that you need to URL-encode the folder ID - `urn%3Aadsk.wipprod%3Afs.folder%3Aco.BJU3PTc4Sd2CmXM492XUiA`.

Note that if you want to export a different version of the file, use [GET projects/:project_id/items/:item_id/versions](/en/docs/data/v2/reference/http/projects-project_id-items-item_id-versions-GET) to find the relevant version ID.

### Request

```
curl -X GET 'https://developer.api.autodesk.com/data/v1/projects/b.139532ee-5cdb-4c9e-a293-652693991e65/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.BJU3PTc4Sd2CmXM492XUiA/contents' \
  -H 'authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

### Response

Note that some lines in this payload example have been omitted for readability.

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/data/v1/projects/b.94d60d03-1e8c-4f32-b146-dd3173e655d8/folders/urn:adsk.wipprod:fs.folder:co.hTcJTDRzTQCnxySVOg6avQ/contents"
    }
  },
  "data": [
    {
      "type": "items",
      "id": "urn:adsk.wipprod:dm.lineage:Ww95QMRfTSCJfbSdVat6FQ",
      "attributes": {
        "...": "..."
      },
      "relationships": {
        "tip": {
          "data": {
            "type": "versions",
            "id": "urn:adsk.wipprod:fs.file:vf.Ww95QMRfTSCJfbSdVat6FQ?version=1"
          }
        }
      }
    },
    {
      "type": "items",
      "id": "urn:adsk.wipprod:dm.lineage:15Rg8B38Qp-SEu6HzXlTNg",
      "attributes": {
        "...": "..."
      },
      "relationships": {
        "tip": {
          "data": {
            "type": "versions",
            "id": "urn:adsk.wipprod:fs.file:vf.15Rg8B38Qp-SEu6HzXlTNg?version=1"
          }
        }
      }
    }
  ],
  "included": [
    {
      "type": "versions",
      "id": "urn:adsk.wipprod:fs.file:vf.Ww95QMRfTSCJfbSdVat6FQ?version=1",
      "attributes": {
        "name": "A-101 FLOOR PLANS",
        "displayName": "A-101 FLOOR PLANS",
        "createTime": "2017-08-25T08:58:57.0000000Z",
        "createUserId": "200906020304322",
        "createUserName": "John Smith",
        "lastModifiedTime": "2017-08-25T08:59:05.0000000Z",
        "lastModifiedUserId": "200906020304322",
        "lastModifiedUserName": "John Smith",
        "versionNumber": 1,
        "extension": {
          "type": "versions:autodesk.bim360:Document",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.bim360:Document-1.0"
          },
          "data": {
            "...": "..."
          }
        }
      }
    },
    {
      "type": "versions",
      "id": "urn:adsk.wipprod:fs.file:vf.15Rg8B38Qp-SEu6HzXlTNg?version=1",
      "attributes": {
        "name": "A-102 FLOOR PLANS",
        "displayName": "A-102 FLOOR PLANS",
        "createTime": "2017-08-25T08:58:57.0000000Z",
        "createUserId": "200906020304322",
        "createUserName": "John Smith",
        "lastModifiedTime": "2017-08-25T08:59:05.0000000Z",
        "lastModifiedUserId": "200906020304322",
        "lastModifiedUserName": "John Smith",
        "versionNumber": 1,
        "extension": {
          "type": "versions:autodesk.bim360:Document",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.bim360:Document-1.0"
          },
          "data": {
            "...": "..."
          }
        }
      }
    }
  ]
}

```

Show More

Find the name of the file you want to export - `included[i].attributes.displayName` (A-102 FLOOR PLANS). It is the name that appears in the ACC Files module UI. Note the version ID - `included[i].id` (<urn:adsk.wipprod:fs.file:vf.15Rg8B38Qp-SEu6HzXlTNg?version=1>).

## [Step 3: Export the Files](#step-3-export-the-files)

To export the file, use the project ID ((`b.139532ee-5cdb-4c9e-a293-652693991e65`) and the version ID (`urn:adsk.wipprod:fs.file:vf.15Rg8B38Qp-SEu6HzXlTNg?version=1`), to call [POST exports](/en/docs/acc/v1/reference/http/files-export-pdf-files-POST).

Note that this endpoint is asynchronous and initiates a job that runs in the background rather than halting execution of your program. You can check whether the asynchronous job is complete by calling [GET exports/{exportId}](/en/docs/acc/v1/reference/http/files-get-export-status-GET).

When exporting the markup file, you can also customize the output filename and export the fileâs markup links. For more information about markup links, please see [Markups Links and References Help Documentation](https://help.autodesk.com/view/DOCS/ENU/?guid=Markups_References_Files_Docs).

This example exports all of the available markup types, published (public) and unpublished (private) markups, and all links attached to standard markups.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/files/v1/projects/139532ee-5cdb-4c9e-a293-652693991e65/exports' \
  -X 'POST' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0' \
  -H 'content-type: application/json' \
  -d '{
      "options": {
        "outputFileName": "MyOutputFile",
        "standardMarkups": {
          "includePublishedMarkups": true,
          "includeUnpublishedMarkups": true,
          "includeMarkupLinks": true
        },
        "issueMarkups": {
          "includePublishedMarkups": true,
          "includeUnpublishedMarkups": true
        },
        "photoMarkups": {
          "includePublishedMarkups": true,
          "includeUnpublishedMarkups": true
        }
      },
      "fileVersions": [
        "urn:adsk.wipprod:fs.file:vf.15Rg8B38Qp-SEu6HzXlTNg?version=1"
      ]
    }'

```

Show More

### Response

```
{
  "id":"225eb2fb-d5b0-44c9-a50a-2c792d833f2e",
  "status":"processing"
}

```

Note the export ID (`id` - `225eb2fb-d5b0-44c9-a50a-2c792d833f2e`). You use the export ID to verify the status of the export and to get a download link for the export.

## [Step 4: Verify the Status of the Export and Get a Download Link](#step-4-verify-the-status-of-the-export-and-get-a-download-link)

To verify the status of the export and to retrieve the data you need to download the exported files when the export job is complete, use the project ID (`b.139532ee-5cdb-4c9e-a293-652693991e65`) and the export ID (`225eb2fb-d5b0-44c9-a50a-2c792d833f2e`) to call [GET /exports/{exportId}](/en/docs/acc/v1/reference/http/files-get-export-status-GET).

When the status is `successful` the export is complete and a signed URL appears in the response, which you can use to download the sheets.

### Request

```
curl -X GET 'https://developer.api.autodesk.com/construction/files/v1/projects/139532ee-5cdb-4c9e-a293-652693991e65/exports/225eb2fb-d5b0-44c9-a50a-2c792d833f2e' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response with successful status

```
{
  "id": "636e6a96-d4d2-43e6-b67a-db8618fc0ff9",
  "status": "successful",
  "result": {
    "output": {
      "signedUrl": "https://accpes-s-ue1-storage.s3.amazonaws.com/{bucketId}/jobs/{jobId}/result.pdf?response-content-disposition={fileName}&AWSAccessKeyId={awsKey}&Signature={signature}&x-amz-security-token={token}&Expires={expire}"
    }
  }
}

```

Show More

Note the signed URL (`result.output.signedUrl`), which you can use for downloading the exported files directly from S3. The link is available for one hour. If you need to download the files after that, you need to call `POST /projects/{projectId}/exports` again.

### Response with failed status

```
{
  "id": "636e6a96-d4d2-43e6-b67a-db8618fc0ff9",
  "status": "failed",
  "result": {
    "error": {
      "code": "401",
      "title": "ERR_AUTHORIZATION_ERROR",
      "detail": "Authentication header is not correct"
    }
  }
}

```

Show More

## [Step 5: Download the Exported File](#step-5-download-the-exported-file)

To download the files from the signed URL, use a GET method and the URL attribute (`result.output.signedUrl`) as the URI.

Note that you should not use a bearer token with this call.

### Request

```
curl -X 'GET' -v 'https://accpes-s-ue1-storage.s3.amazonaws.com/{bucketId}/jobs/{jobId}/result.pdf?response-content-disposition={fileName}&AWSAccessKeyId={awsKey}&Signature={signature}&x-amz-security-token={token}&Expires={expire}'

```

### Response:

```
Status Code: 200 OK
Content-Type:application/pdf
Content-Length:90616

with chunked content body

```

Congratulations! You have exported files from the ACC Files module.
