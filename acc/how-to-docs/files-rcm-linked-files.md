# Download RVT Files from a Published Model

Source: https://aps.autodesk.com/en/docs/acc/tutorials/files/rcm-linked-files/

---

# Download RVT Files from a Published Model

This tutorial demonstrates how to retrieve temporary download links (signed URLs) and metadata for a published version of a Cloud Workshared Revit (RVT) model, as well as for any linked RVT models it references.

The steps include finding the version ID of the published host model, generating signed URLs and metadata, and downloading the RVT files using the signed URLs.

You can also use this workflow to retrieve a download URL for a specific published host model version, even if no linked models are present.

Each time you retrieve the signed URLs, they are newly generated and valid for 1 hour.

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps), and select the Data Management and Autodesk Construction Cloud APIs.
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with the `data:read` scope.
- Verify that you have access to the relevant ACC or BIM 360 account, project, and folder.
- Ensure that the Revit model has been published to the cloud from Revit, and that it is a Cloud Workshared model.

## [Step 1: Find the Hub ID for the BIM 360 or ACC Account](#step-1-find-the-hub-id-for-the-bim-360-or-acc-account)

The first four steps show how to use Data Management endpoints to locate the version ID of the Revit host model. You first need to find the ID of the hub (account) that contains the project where the Revit host model is stored.

Call [GET hubs](../../data/http-docs/http-hubs-GET.md) to retrieve a list of the BIM 360 or ACC accounts your app has access to.

Note that the BIM 360 account ID corresponds to a Data Management hub ID. To convert an account ID into a hub ID you need to add a â**b.**" prefix. For example, the account ID `c8b0c73d-3ae9` becomes `b.c8b0c73d-3ae9`.

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
      "id": "b.35da59e5-4acb-4979-85f1-518047215eaa",
      "attributes": {
        "name": "ACME Construction - East Coast",
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

In this example, assume that the Cloud Workshared Revit model from which you want to retrieve the linked RVT files is stored in a hub called `ACME Construction - East Coast`.

Find the hub in the response (`data.attributes.name`), and note the hub ID (`data.id`) â `b.35da59e5-4acb-4979-85f1-518047215eaa`.

## [Step 2: Find the Project ID](#step-2-find-the-project-id)

Find the project that contains the Cloud Workshared Revit model from which you want to retrieve the linked RVT files.

Use the hub ID (`b.35da59e5-4acb-4979-85f1-518047215eaa`) to call [GET hubs/:hub_id/projects](../../data/http-docs/http-hubs-hub_id-projects-GET.md) to get a list of all the projects in the hub. Find the project ID of the project that contains the folder of the Cloud Workshared Revit model from which you want to retrieve the linked RVT files.

Note that the project ID in BIM 360 corresponds to the project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). To convert a project ID in BIM 360 or ACC to a project ID in the Data Management API, you need to add a â**b.**" prefix. For example, a project ID of `a4be0c34a-4ab7` translates to a project ID of `b.a4be0c34a-4ab7`.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs/b.35da59e5-4acb-4979-85f1-518047215eaa/projects"

```

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/project/v1/hubs/b.35da59e5-4acb-4979-85f1-518047215eaa/projects"
    }
  },
  "data": [
    {
      "type": "projects",
      "id": "b.12cd67f0-07e5-4e54-b66b-fb8d1785357a",
      "attributes": {
        "name": "Main Office Tower",
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

In this example, assume that the Cloud Workshared Revit model from which you want to retrieve the linked RVT files is stored in a project called `Main Office Tower`

Find the project (`data.attributes.name`), and note the project ID (`data.id`) - `b.12cd67f0-07e5-4e54-b66b-fb8d1785357a`.

## [Step 3: Find the Project Files Folder ID](#step-3-find-the-project-files-folder-id)

Find the folder where the Cloud Workshared Revit model is stored. Most models are stored in the Project Files folder.

Use the hub ID (`b.35da59e5-4acb-4979-85f1-518047215eaa`) and the project ID (`b.12cd67f0-07e5-4e54-b66b-fb8d1785357a`) to call [GET hubs/:hub_id/projects/:project_id/topFolders](../../data/http-docs/http-hubs-hub_id-projects-project_id-topFolders-GET.md) to get the Project Files folder ID.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT"
            "https://developer.api.autodesk.com/project/v1/hubs/b.35da59e5-4acb-4979-85f1-518047215eaa/projects/b.12cd67f0-07e5-4e54-b66b-fb8d1785357a/topFolders"

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

Find the folder (`data.attributes.name`); in this example, the Project Files folder, and note the folder ID (`data.id`) - `urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA`

## [Step 4: Find the Latest Published Version ID](#step-4-find-the-latest-published-version-id)

Use the project ID and the folder ID to call [GET projects/:project_id/folders/:folder_id/contents](../../data/http-docs/http-projects-project_id-folders-folder_id-contents-GET.md) to get the tip version ID of the Cloud Workshared Revit model from which you want to retreive the linked RVT files.

To filter out non-cloud workshared Revit files, apply the `items:autodesk.bim360:C4RModel` filter.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT"
    "https://developer.api.autodesk.com/data/v1/projects/b.12cd67f0-07e5-4e54-b66b-fb8d1785357a/folders/urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA/contents?filter[attributes.extension.type]=items%3Aautodesk.bim360%3AC4RModel"

```

### Response

```
{
"jsonapi": {
  "version": "1.0"
},
"links": {
  "self": {
    "href": "https://developer.api.autodesk.com/data/v1/projects/b.c8112490-4e08-435c-994b-64fe60fea507/folders/urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA/contents?filter[attributes.extension.type]=items:autodesk.bim360:C4RModel"
  }
},
"data": [
  {
    "type": "items",
    "id": "urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q",
    "attributes": {
      "displayName": "DemoModel",
      "createTime": "2018-02-22T17:51:11.0000000Z",
      "createUserId": "38SCJGX4R4PV",
      "createUserName": "John Doe",
      "lastModifiedTime": "2018-02-22T17:58:36.0000000Z",
      "lastModifiedUserId": "38SCJGX4R4PV",
      "lastModifiedUserName": "John Doe",
      "hidden": false,
      "reserved": false,
      "extension": {
        "type": "items:autodesk.bim360:C4RModel",
        "version": "1.0.0",
        "schema": {
          "href": "https://developer.api.autodesk.com/schema/v1/versions/items:autodesk.bim360:C4RModel-1.0.0"
        },
        "data": {}
      }
    }
  }
],
"included": [
  {
    "type": "versions",
    "id": "urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q?version=3",
    "attributes": {
      "name": "DemoModel.rvt",
      "displayName": "DemoModel",
      "createTime": "2018-02-22T17:57:43.0000000Z",
      "createUserId": "38SCJGX4R4PV",
      "createUserName": "John Doe",
      "lastModifiedTime": "2018-02-22T17:58:37.0000000Z",
      "lastModifiedUserId": "38SCJGX4R4PV",
      "lastModifiedUserName": "John Doe",
      "versionNumber": 3,
      "mimeType": "application/vnd.autodesk.r360",
      "fileType": "rvt",
      "extension": {
        "type": "versions:autodesk.bim360:C4RModel",
        "version": "1.1.0",
        "schema": {
          "href": "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.bim360:C4RModel-1.1.0"
        },
      }
    }
  }
]

```

Show More

}

In this example, assume that the model from which you want to retrieve the linked RVT files is called `DemoModel`.

Find the model in the response (`included[i].attributes.displayName`), and note the latest published version ID (`included[i].id`) â `urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q?version=3`.

## [Step 5: Retrieve Signed URLs for the Host and Linked Models](#step-5-retrieve-signed-urls-for-the-host-and-linked-models)

Use the project ID (`b.12cd67f0-07e5-4e54-b66b-fb8d1785357a`) and the version ID (`urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q?version=3`) of the published Cloud Workshared Revit model to call [GET construction/rcm/v1/projects/:project_id/published-versions/:version_id/linked-files](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rcm-getlinkedfiles-GET/). This call retrieves metadata and temporary download links (signed URLs) for:

- The published version of the host model (unless you set `includeHost=false`)
- Any Revit files that are linked into that version of the model.

Make sure the version ID in the request URL is URL-encoded.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT"
"https://developer.api.autodesk.com/construction/rcm/v1/projects/b.12cd67f0-07e5-4e54-b66b-fb8d1785357a/published-versions/urn%3Aadsk.wipprod%3Adm.lineage%3AhPW2BlBbQG2L5HjCOh7Z8Q%3Fversion%3D3/linked-files"

```

### Repsonse

```
{
  "hostFile": {
      "modelName": "DemoModel.rvt",
      "signedUrl": "https://c4r-s-ue1-project-data.s3.amazonaws.com/publish/0932a81e-e4e1-4e5b-8e65-8406ac3a2eed/version_10.rvt?AWSAccessKeyId",
      "itemId": "urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q",
      "versionId": "urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q?version=3",
      "size": 7184384,
      "publishStatus": "Published"
  },
  "linkedFiles": {
      "pagination": {
          "limit": 600,
          "offset": 0,
          "totalResults": 5
      },
      "results": [{
              "modelName": "Project_2.rvt",
              "signedUrl": "https://c4r-s-ue1-project-data.s3.amazonaws.com/publish/f553a4c1-fc68-4a7d-9459-66c9a9b4d958/version_7.rvt?AWSAccessKeyId",
              "itemId": "urn:adsk.wipstg:dm.lineage:K1IKTUl1Qji7vIEJ3E6FxA",
              "versionId": "urn:adsk.wipstg:fs.file:vf.K1IKTUl1Qji7vIEJ3E6FxA?version=6",
              "size": 5525504,
              "publishStatus": "Published"
          }, {
              "modelName": "Project_3.rvt",
              "signedUrl": "https://c4r-s-ue1-project-data.s3.amazonaws.com/publish/2a08695e-4d60-429c-a2d4-7e1c605be0b5/version_7.rvt?AWSAccessKeyId",
              "itemId": "urn:adsk.wipstg:dm.lineage:E4DVafMOTnqxZ5TiV4qMGw",
              "versionId": "urn:adsk.wipstg:fs.file:vf.BKbru6y-SlSYelQ1DJ0AmQ?version=3",
              "size": 5464064,
              "publishStatus": "Published"
          }, {
              "modelName": "Project_4.rvt",
              "signedUrl": "https://c4r-s-ue1-project-data.s3.amazonaws.com/publish/06c94ed0-1154-4e7f-933e-d0123d5e2a0c/version_10.rvt?AWSAccessKeyId",
              "itemId": "urn:adsk.wipstg:dm.lineage:1eML_KSoQVSkJRT3mkf8Ag",
              "versionId": "urn:adsk.wipstg:fs.file:vf.EIT81_eXRu6Sj_FD2llA_Q?version=3",
              "size": 5636096,
              "publishStatus": "Published"
          }, {
              "modelName": "rme_advanced_sample_project.rvt",
              "signedUrl": "https://c4r-s-ue1-project-data.s3.amazonaws.com/publish/317e60a0-eb91-4c93-9c83-79c92a27a243/version_23.rvt?AWSAccessKeyId",
              "itemId": "urn:adsk.wipstg:dm.lineage:JPmHHTXeQJ6Bna0vdKWeXA",
              "size": 37253120,
              "publishStatus": "NotPublished"
          }, {
              "modelName": "Project_5.rvt",
              "signedUrl": "https://c4r-s-ue1-project-data.s3.amazonaws.com/publish/358e20b7-a989-47e6-8abf-85dcbf41a684/version_6.rvt?AWSAccessKeyId",
              "itemId": "urn:adsk.wipstg:dm.lineage:svs0bN2gSFqPGYtpb9WL9Q",
              "size": 7450624,
              "publishStatus": "NotPublished"
          }
      ]
  }

```

Show More

}

The response includes two top-level keys:

- `hostFile` â Contains metadata and a signed URL for the host model. This object is returned by default unless `includeHost=false` is explicitly set in the request.
- `linkedFiles` â Contains metadata and signed URLs for any Revit models that are linked into the specified version of the host model.

## [Step 6: Download the RVT Files](#step-6-download-the-rvt-files)

To download the host model or any of the linked RVT files, use a GET method and the corresponding `signedUrl` value from the response in Step 5 as the URI.

Note that you should not include a bearer token in this request.

### Request

```
curl -X GET "https://c4r-s-ue1-project-data.s3.amazonaws.com/publish/0932a81e-e4e1-4e5b-8e65-8406ac3a2eed/version_10.rvt?AWSAccessKeyId"

```

Congratulations! You have downloaded a Revit model from ACC using a signed URL.
