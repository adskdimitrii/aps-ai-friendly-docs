# Model Sets and Versions

Source: https://aps.autodesk.com/en/docs/acc/tutorials/model-coordination/mc-tutorial-model-set/

---

# Model Sets and Versions

This tutorial demonstrates the various features of the Model Set Service. Model sets and [model set versions](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/model-coordination/mcfg-model-set/) are the unit of coordination used in BIM 360 Model Coordination. Model sets are equivalent to the coordination spaces configured via the Model Coordination Project Admin web UI. There is currently a limitation in the BIM 360 Model Coordination application resulting in the API not being accessible on new BIM 360 projects until the first coordination space has been defined by a project administrator. Essentially, the administrative process of creating the first collaboration space initializes the model set service container. If you are running these samples against a new BIM 360 project with no coordination spaces, you first need to manually create a coordination space via the Model Coordination Project Admin web UI.

## [Before You Begin](#before-you-begin)

Make sure that you have [registered an app](../../oauth/how-to-docs/create-app.md). and successfully [acquired an OAuth token](https://aps.autodesk.com/en/docs/oauth/v2/tutorials/http/get-2-legged-token/) with the `data:read`, `data:write` and `data:create` scopes.

## [Creating model sets](#creating-model-sets)

Once the model coordination container is initialized, you can programmatically create new model sets (coordination spaces) by posting a BIM 360 Docs Plans or Project Files folder URN on to [POST modelsets](../http-docs/http-mc-modelset-service-v3-create-model-set-POST.md) endpoint. All of the endpoints in the model coordination API that change data are asynchronous. The initial POST, PATCH, PUT, or DELETE call starts a job. The various resource collections in the API each have corresponding job endpoints that you can use to track the success or failure of asynchronous operations.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f83cef12-deef-4771-9feb-4f85643e3c46/modelsets'
     -X POST
     -H 'Authorization: Bearer <token>'
     -H 'Content-Type: application/json'
     -d '{
       "name": "My Model Set",
       "description": "Space for coordinating all disciplines",
       "folders": [
         {
           "folderUrn": "urn:adsk.wipprod:fs.folder:co.WI8roO18TU2Cl3P9y64z4w"
         }
       ]
     }'

```

Show More

The initial response from the POST to the modelsets endpoint returns a job response body containing the `jobId`, status, and metadata associated with the job (in this case, the creation of a new model set). The job seed encapsulates the original input to the job, and provides a mechanism for correlating the job with the original POST, PATCH, PUT, or DELETE call that started the job. The initial response from the POST onto the modesets endpoint returns a status of `Running`, indicating that the job is executing. Also note that the system has allocated the new model set a GUID identity that is returned in the modelSetId property on the response object.

### Example Response

```
{
    "jobId":"d41e37e7-921f-4e72-a33a-906085dc052b",
    "modelSetId":"a5fea9de-7487-45b8-a9f2-878cf7069053",
    "status":"Running",
    "job": {
        "operation":"CreateScope",
        "seed": {
            "createdBy":"DLLKP4DBC383",
            "name":"My Model Set",
            "description":"Space for coordinating all disciplines",
            "scopeId":"a5fea9de-7487-45b8-a9f2-878cf7069053",
            "containerId":"f83cef12-deef-4771-9feb-4f85643e3c46",
            "folders":[
                {
                    "folderUrn":"urn:adsk.wipprod:fs.folder:co.WI8roO18TU2Cl3P9y64z4w",
                    "documentFilters":null
                }
            ],
            "isDisabled":false
        }
    }
}

```

Show More

Taking the `jobId` from the response, you can call the container [GET jobs/:jobId](../http-docs/http-mc-modelset-service-v3-get-container-job-by-container-GET.md) endpoint. Model sets belong to containers (that is, the process of adding a new model set to a container is a container-level operation, so you can use the container jobs endpoint to track the progress of the job).

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f83cef12-deef-4771-9feb-4f85643e3c46/jobs/d41e37e7-921f-4e72-a33a-906085dc052b'
     -H 'Authorization: Bearer <token>'

```

Each call to a jobs endpoint yields a response similar to the initial response returned by the POST, PATCH, PUT, or DELETE operation that originally started the job. In the response below, the status is changed to `Succeeded` and you can interrogate the seed to get the data associated with the operation that originally started the job (in this case, a POST onto the modelsets endpoint).

### Example Response

```
{
    "jobId":"d41e37e7-921f-4e72-a33a-906085dc052b",
    "modelSetId":"a5fea9de-7487-45b8-a9f2-878cf7069053",
    "status":"Succeeded",
    "job": {
        "operation":"CreateScope",
        "seed": {
            "createdBy":"DLLKP4DBC383",
            "name":"My Model Set",
            "description":"Space for coordinating all disciplines",
            "scopeId":"a5fea9de-7487-45b8-a9f2-878cf7069053",
            "containerId":"f83cef12-deef-4771-9feb-4f85643e3c46",
            "folders":[
                {
                    "folderUrn":"urn:adsk.wipprod:fs.folder:co.WI8roO18TU2Cl3P9y64z4w",
                    "documentFilters":null
                }
            ],
            "isDisabled":false
        }
    }
}

```

Show More

## [Querying model sets](#querying-model-sets)

You can also use the [GET modelsets](../http-docs/http-mc-modelset-service-v3-get-model-sets-GET.md) endpoint on a container to list the currently defined model sets in the container. This endpoint is paged and returns all of the data necessary to interrogate an individual model set for its versions and the clash and index data associated with these versions.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f83cef12-deef-4771-9feb-4f85643e3c46/modelsets'
     -H 'Authorization: Bearer <token>'

```

In addition to returning display properties such as the name and description of the model set (as presented to the user in the BIM 360 Model Coordination web UI), you can also determine when the model set was created and obtain the ID of the user who created the model set. Model sets also have an `isDeleted` flag, indicating that the model set is no longer accessible via the web UI. Model sets and the data associated with them are only physically deleted when the model set container is deleted. The following sample response shows four model sets in this container.

### Example Response

```
{
    "page": {},
    "modelSets": [
        {
            "modelSetId": "a5fea9de-7487-45b8-a9f2-878cf7069053",
            "containerId": "f83cef12-deef-4771-9feb-4f85643e3c46",
            "name": "My Model Set",
            "description": "Space for coordinating all disciplines",
            "createdBy": "DLLKP4DBC383",
            "createdTime": "2019-11-06T08:13:44.271173+00:00",
            "isDisabled": false,
            "isDeleted": false
        },
        {
            "modelSetId": "9338f1cb-3b63-465f-8c16-7719318fd2bb",
            "containerId": "f83cef12-deef-4771-9feb-4f85643e3c46",
            "name": "MC_20190909190333",
            "description": "This model set has been created to demonstrate the Model Coordination API and encapsulates MC_20190909190333",
            "createdBy": "7ERBMBR9EA4A",
            "createdTime": "2019-09-09T19:04:00.982144+00:00",
            "isDisabled": false,
            "isDeleted": false
        },
        {
            "modelSetId": "c85f934f-9945-4172-b905-5ec57dea09db",
            "containerId": "f83cef12-deef-4771-9feb-4f85643e3c46",
            "name": "MC_20190906122228",
            "description": "This model set has been created to demonstrate the Model Coordination API and encapsulates MC_20190906122228",
            "createdBy": "7ERBMBR9EA4A",
            "createdTime": "2019-09-06T12:23:25.33839+00:00",
            "isDisabled": false,
            "isDeleted": false
        },
        {
            "modelSetId": "e1e51b92-fccf-4672-9dd7-9bd66471cfa2",
            "containerId": "f83cef12-deef-4771-9feb-4f85643e3c46",
            "name": "MC_20190903092025",
            "description": "This model set has been created to demonstrate the Model Coordination API and encapsulates MC_20190903092025",
            "createdBy": "7ERBMBR9EA4A",
            "createdTime": "2019-09-03T09:21:08.256452+00:00",
            "isDisabled": false,
            "isDeleted": false
        }
    ]
}

```

Show More

To obtain the full details of a given model set, you can call the [GET modelsets/:modelSetId](../http-docs/http-mc-modelset-service-v3-get-model-set-GET.md) endpoint, supplying a `modelSetId` GUID identity returned in the above response.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f83cef12-deef-4771-9feb-4f85643e3c46/modelsets/a5fea9de-7487-45b8-a9f2-878cf7069053'
     -H 'Authorization: Bearer <token>'

```

The response is very similar to the paged summary response returned above; however, the detailed response also includes the folder URN associated with the model set, along with the current `tipVersion` of the model set. Model set versioning is the subject of the next section in this tutorial.

### Example Response

```
{
    "modelSetId": "a5fea9de-7487-45b8-a9f2-878cf7069053",
    "modelSetType": "Plans",
    "containerId": "f83cef12-deef-4771-9feb-4f85643e3c46",
    "folders": [
        {
            "folderUrn": "urn:adsk.wipprod:fs.folder:co.WI8roO18TU2Cl3P9y64z4w"
        }
    ],
    "name": "My Model Set",
    "description": "Space for coordinating all disciplines",
    "createdBy": "DLLKP4DBC383",
    "createdTime": "2019-11-06T08:13:44.271173+00:00",
    "isDisabled": false,
    "tipVersion": 3
}

```

Show More

## [Querying model set versions](#querying-model-set-versions)

Once a model set is defined, it is automatically “enabled” by the system. An enabled model set results in the system automatically creating model set versions as users interact with BIM 360 Docs. If a user changes the file content in a folder associated with a model set, the system automatically scans the tip versions of the 3D model content in the folder. If this scan yields a set of file versions different to any proceeding scan, a new model set version is created. Model set versions are sequential for a model set and have sequential version numbers. To page through the model set versions for a model set, you call its [GET modelsets/:modelSetId/versions](../http-docs/http-mc-modelset-service-v3-get-model-set-versions-GET.md) endpoint.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f83cef12-deef-4771-9feb-4f85643e3c46/modelsets/a5fea9de-7487-45b8-a9f2-878cf7069053/versions'
     -H 'Authorization: Bearer <token>'

```

The *versions* endpoint returns paged model set version summaries. These summaries include the status of each model set `version`, the date and time they were created, and the unique (within the context of a model set) version number.

### Example Response

```
{
    "page": {},
    "modelSetVersions": [
        {
            "version": 3,
            "createTime": "2019-11-06T08:16:28.747403+00:00",
            "status": "Successful"
        },
        {
            "version": 2,
            "createTime": "2019-11-06T08:15:36.867067+00:00",
            "status": "Successful"
        },
        {
            "version": 1,
            "createTime": "2019-11-06T08:15:02.273917+00:00",
            "status": "Successful"
        }
    ]
}

```

Show More

You can query a specific model set version by calling the [GET modelsets/:modelSetId/versions/:version](../http-docs/http-mc-modelset-service-v3-get-model-set-version-GET.md) endpoint and passing the version number of the model set version.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f83cef12-deef-4771-9feb-4f85643e3c46/modelsets/61b5025d-59d0-43fd-add4-bdbd9b59119a/versions/3'
     -H 'Authorization: Bearer <token>'

```

This returns the immutable set of 3D model files that was found when the system queried the tip versions of the document lineages beneath the folder associated with the model set definition. You can use the model set version `status` and individual document version `status` properties to determine whether or not the system was able to successfully process all the files in the model set version. The ability of the system to track model content at the object/element level between successive versions of a file is dependent on an underlying object tracking capability of the model set service. Under certain conditions, object tracking is not possible for a file version. Under these conditions the document version is still visible via the BIM 360 model viewer, but the tracking IDs for objects in the model cannot be determined. Any downstream model set version workflow that is dependent on these IDs (for example, clash testing) uses these status values to determine if the model set version can be processed or partially processed.

### Example Response

```
{
    "modelSetId": "a5fea9de-7487-45b8-a9f2-878cf7069053",
    "version": 3,
    "createTime": "2019-11-06T08:16:28.747403+00:00",
    "status": "Successful",
    "documentVersions": [
        {
            "documentLineage": {
                "lineageUrn": "urn:adsk.wipprod:dm.lineage:9IeFYnYxTB-OMsg3vwb3hQ",
                "parentFolderUrn": "urn:adsk.wipprod:fs.folder:co.-iqpHJcgSS6oVHYtZjoYnw",
                "isAligned": true,
                "tipVersionUrn": "urn:adsk.wipprod:fs.file:vf.9IeFYnYxTB-OMsg3vwb3hQ?version=1"
            },
            "documentStatus": "Succeeded",
            "forgeType": "versions:autodesk.bim360:Document",
            "versionUrn": "urn:adsk.wipprod:fs.file:vf.9IeFYnYxTB-OMsg3vwb3hQ?version=1",
            "displayName": "{3D}_Audubon_Structure.rvt",
            "viewableName": "{3D}",
            "createUserId": "ERZWLHJGT7NE",
            "createTime": "2019-11-06T08:14:55+00:00",
            "viewableGuid": "00cd2da3-fbfa-44a9-7a33-cad0bc4720cb",
            "viewableId": "0935d8b2-149b-4a0d-b816-863f0d595a20-000bcd64",
            "viewableMime": "application/autodesk-svf",
            "bubbleUrn": "urn:adsk.wipprod:fs.file:vf.NKGUU8CLQ8WP_dCM54KKKg?version=1",
            "originalSeedFileVersionUrn": "urn:adsk.wipprod:fs.file:vf.NKGUU8CLQ8WP_dCM54KKKg?version=1",
            "originalSeedFileVersionName": "Audubon_Structure.rvt"
        },
        {
            "documentLineage": {
                "lineageUrn": "urn:adsk.wipprod:dm.lineage:bAGrilc0SDyczBLIHEQFdA",
                "parentFolderUrn": "urn:adsk.wipprod:fs.folder:co.-iqpHJcgSS6oVHYtZjoYnw",
                "isAligned": true,
                "tipVersionUrn": "urn:adsk.wipprod:fs.file:vf.bAGrilc0SDyczBLIHEQFdA?version=1"
            },
            "documentStatus": "Skipped",
            "forgeType": "versions:autodesk.bim360:Document",
            "versionUrn": "urn:adsk.wipprod:fs.file:vf.bAGrilc0SDyczBLIHEQFdA?version=1",
            "displayName": "New Construction_Audubon_Mechanical.rvt",
            "viewableName": "New Construction",
            "createUserId": "ERZWLHJGT7NE",
            "createTime": "2019-11-06T08:16:21+00:00",
            "viewableGuid": "38c10754-d1f9-5bf6-2546-4bac2d3dab5b",
            "viewableId": "c884ae1b-61e7-4f9d-0001-719e20b22d0b-00121ed3",
            "viewableMime": "application/autodesk-svf",
            "bubbleUrn": "urn:adsk.wipprod:fs.file:vf.ajkTDG4eQeuDpBvbwX8Gfw?version=1",
            "originalSeedFileVersionUrn": "urn:adsk.wipprod:fs.file:vf.ajkTDG4eQeuDpBvbwX8Gfw?version=1",
            "originalSeedFileVersionName": "Audubon_Mechanical.rvt"
        },
        {
            "documentLineage": {
                "lineageUrn": "urn:adsk.wipprod:dm.lineage:eFcw-VElSrG-6SxjvnBHgA",
                "parentFolderUrn": "urn:adsk.wipprod:fs.folder:co.-iqpHJcgSS6oVHYtZjoYnw",
                "isAligned": true,
                "tipVersionUrn": "urn:adsk.wipprod:fs.file:vf.eFcw-VElSrG-6SxjvnBHgA?version=1"
            },
            "documentStatus": "Succeeded",
            "forgeType": "versions:autodesk.bim360:Document",
            "versionUrn": "urn:adsk.wipprod:fs.file:vf.eFcw-VElSrG-6SxjvnBHgA?version=1",
            "displayName": "{3D}_Audubon_Architecture.rvt",
            "viewableName": "{3D}",
            "createUserId": "ERZWLHJGT7NE",
            "createTime": "2019-11-06T08:15:30+00:00",
            "viewableGuid": "5d41dda7-eea1-eff5-77dd-ee1aa81fc3a8",
            "viewableId": "845097d1-c3be-4a6f-9dbe-51582fa6d465-002c2f04",
            "viewableMime": "application/autodesk-svf",
            "bubbleUrn": "urn:adsk.wipprod:fs.file:vf.kPYVVTK4SC2TcE2XJJdvuw?version=1",
            "originalSeedFileVersionUrn": "urn:adsk.wipprod:fs.file:vf.kPYVVTK4SC2TcE2XJJdvuw?version=1",
            "originalSeedFileVersionName": "Audubon_Architecture.rvt"
        },
        {
            "documentLineage": {
                "lineageUrn": "urn:adsk.wipprod:dm.lineage:EmoWniVZQlua5GTXFWwfTA",
                "parentFolderUrn": "urn:adsk.wipprod:fs.folder:co.-iqpHJcgSS6oVHYtZjoYnw",
                "isAligned": true,
                "tipVersionUrn": "urn:adsk.wipprod:fs.file:vf.EmoWniVZQlua5GTXFWwfTA?version=1"
            },
            "documentStatus": "Skipped",
            "forgeType": "versions:autodesk.bim360:Document",
            "versionUrn": "urn:adsk.wipprod:fs.file:vf.EmoWniVZQlua5GTXFWwfTA?version=1",
            "displayName": "New Construction_Audubon_Architecture.rvt",
            "viewableName": "New Construction",
            "createUserId": "ERZWLHJGT7NE",
            "createTime": "2019-11-06T08:15:30+00:00",
            "viewableGuid": "10c25a10-5469-3aef-b0a6-1c27c7b8e93b",
            "viewableId": "c884ae1b-61e7-4f9d-0001-719e20b22d0b-0032f400",
            "viewableMime": "application/autodesk-svf",
            "bubbleUrn": "urn:adsk.wipprod:fs.file:vf.kPYVVTK4SC2TcE2XJJdvuw?version=1",
            "originalSeedFileVersionUrn": "urn:adsk.wipprod:fs.file:vf.kPYVVTK4SC2TcE2XJJdvuw?version=1",
            "originalSeedFileVersionName": "Audubon_Architecture.rvt"
        },
        {
            "documentLineage": {
                "lineageUrn": "urn:adsk.wipprod:dm.lineage:r4Boku9qT9iQ6C1ofbYaCg",
                "parentFolderUrn": "urn:adsk.wipprod:fs.folder:co.-iqpHJcgSS6oVHYtZjoYnw",
                "isAligned": true,
                "tipVersionUrn": "urn:adsk.wipprod:fs.file:vf.r4Boku9qT9iQ6C1ofbYaCg?version=1"
            },
            "documentStatus": "Succeeded",
            "forgeType": "versions:autodesk.bim360:Document",
            "versionUrn": "urn:adsk.wipprod:fs.file:vf.r4Boku9qT9iQ6C1ofbYaCg?version=1",
            "displayName": "{3D}_Audubon_Mechanical.rvt",
            "viewableName": "{3D}",
            "createUserId": "ERZWLHJGT7NE",
            "createTime": "2019-11-06T08:16:21+00:00",
            "viewableGuid": "a3186f12-7750-fa47-f60a-610a779ba5ac",
            "viewableId": "24bb580c-5e74-4a65-bcae-e97c21424529-00027e16",
            "viewableMime": "application/autodesk-svf",
            "bubbleUrn": "urn:adsk.wipprod:fs.file:vf.ajkTDG4eQeuDpBvbwX8Gfw?version=1",
            "originalSeedFileVersionUrn": "urn:adsk.wipprod:fs.file:vf.ajkTDG4eQeuDpBvbwX8Gfw?version=1",
            "originalSeedFileVersionName": "Audubon_Mechanical.rvt"
        },
        {
            "documentLineage": {
                "lineageUrn": "urn:adsk.wipprod:dm.lineage:xMPsOKv5RIWG4pdPJ5IY5Q",
                "parentFolderUrn": "urn:adsk.wipprod:fs.folder:co.-iqpHJcgSS6oVHYtZjoYnw",
                "isAligned": true,
                "tipVersionUrn": "urn:adsk.wipprod:fs.file:vf.xMPsOKv5RIWG4pdPJ5IY5Q?version=1"
            },
            "documentStatus": "Skipped",
            "forgeType": "versions:autodesk.bim360:Document",
            "versionUrn": "urn:adsk.wipprod:fs.file:vf.xMPsOKv5RIWG4pdPJ5IY5Q?version=1",
            "displayName": "New Construction_Audubon_Structure.rvt",
            "viewableName": "New Construction",
            "createUserId": "ERZWLHJGT7NE",
            "createTime": "2019-11-06T08:14:55+00:00",
            "viewableGuid": "4a966c2a-ead6-65c3-4f98-273dd7543047",
            "viewableId": "c884ae1b-61e7-4f9d-0001-719e20b22d0b-00120bb2",
            "viewableMime": "application/autodesk-svf",
            "bubbleUrn": "urn:adsk.wipprod:fs.file:vf.NKGUU8CLQ8WP_dCM54KKKg?version=1",
            "originalSeedFileVersionUrn": "urn:adsk.wipprod:fs.file:vf.NKGUU8CLQ8WP_dCM54KKKg?version=1",
            "originalSeedFileVersionName": "Audubon_Structure.rvt"
        }
    ]
}

```

Show More

The previous example described how to navigate from a model set to discover its versions, then how to select one of these versions to display the content associated with this version. The model set service provides a [GET modelsets/:modelSetId/versions/latest](../http-docs/http-mc-modelset-service-v3-get-model-set-version-latest-GET.md) short-cut API call that returns the details of the most recently available model set version.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f83cef12-deef-4771-9feb-4f85643e3c46/modelsets/a5fea9de-7487-45b8-a9f2-878cf7069053/versions/latest'
     -H 'Authorization: Bearer <token>'

```

## [Controlling automatic model set version creation](#controlling-automatic-model-set-version-creation)

Up to this point, the examples work on the principle that model set versions should be created automatically as users interact with BIM 360 Docs (uploading, moving, and copying content). This has the potential to create redundant model set versions, representing intermediate states on the project that have no real value from a data analysis point of view. The model set service solves this potential issue by allowing API users to enable and disable automatic model set version creation. You can use the [PATCH modelsets/:modelSetId/versions:disable](../http-docs/http-mc-modelset-service-v3-disable-model-set-versions-PATCH.md) endpoint to switch off automatic model set version creation.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f83cef12-deef-4771-9feb-4f85643e3c46/modelsets/a5fea9de-7487-45b8-a9f2-878cf7069053/versions:disable'
     -X PATCH
     -H 'Authorization: Bearer <token>'

```

The response from this endpoint is a model set job, the seed of which indicates that the `isDisabled` setting on a model set is toggled from false to true.

### Example Response

```
{
    "jobId":"37ec9440-6ff8-4d7c-a817-78c527d4982e",
    "modelSetId":"a5fea9de-7487-45b8-a9f2-878cf7069053",
    "status":"Running",
    "job": {
        "seed": {
            "scopeId":"a5fea9de-7487-45b8-a9f2-878cf7069053",
            "isDisabled": {
                "original":false,
                "new":true
            }
        }
    }
}

```

Show More

As before, you can track the status of this job using the [GET modelsets/:modelSetId/jobs/:jobId](../http-docs/http-mc-modelset-service-v3-get-model-set-job-GET.md) endpoint.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f83cef12-deef-4771-9feb-4f85643e3c46/modelsets/a5fea9de-7487-45b8-a9f2-878cf7069053/jobs/37ec9440-6ff8-4d7c-a817-78c527d4982e'
     -H 'Authorization: Bearer <token>'

```

A status of `Succeeded` indicates that automatic model set version creation is disabled. At this point, all user interaction with BIM 360 Docs within the context of the disabled model set are ignored by the system and no further model set versions are created for the disable model set.

### Example Response

```
{
    "jobId":"37ec9440-6ff8-4d7c-a817-78c527d4982e",
    "modelSetId":"a5fea9de-7487-45b8-a9f2-878cf7069053",
    "status":"Succeeded",
    "job": {
        "operation":"UpdateScope",
        "seed": {
            "scopeId":"a5fea9de-7487-45b8-a9f2-878cf7069053",
            "isDisabled": {
                "original":false,
                "new":true
            }
        }
    }
}

```

Show More

You can enable a disabled model set version by calling the [PATCH modelsets/:modelSetId/versions:enable](../http-docs/http-mc-modelset-service-v3-enable-model-set-versions-PATCH.md) endpoint, which starts a job to re-enable automatic model set versioning.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f83cef12-deef-4771-9feb-4f85643e3c46/modelsets/a5fea9de-7487-45b8-a9f2-878cf7069053/versions:enable'
     -X PATCH
     -H 'Authorization: Bearer <token>'

```

Once again, this endpoint returns a job that you can track using the [GET modelsets/:modelSetId/jobs/:jobId](../http-docs/http-mc-modelset-service-v3-get-model-set-job-GET.md) endpoint.

### Example Response

```
{
    "jobId":"ca8c7d00-fe59-4173-ba80-449cbe5a6ab2",
    "modelSetId":"a5fea9de-7487-45b8-a9f2-878cf7069053",
    "status":"Running",
    "job": {
        "seed": {
            "scopeId":"a5fea9de-7487-45b8-a9f2-878cf7069053",
            "isDisabled": {
                "original":true,
                "new":false
            }
        }
    }
}

```

Show More

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f83cef12-deef-4771-9feb-4f85643e3c46/modelsets/a5fea9de-7487-45b8-a9f2-878cf7069053/jobs/ca8c7d00-fe59-4173-ba80-449cbe5a6ab2'
     -H 'Authorization: Bearer <token>'

```

A status of `Succeeded` indicates that automatic model set version creation is enabled. At this point, all user interaction with BIM 360 Docs within the context of the enabled model set is processed by the system creating new model set versions for the newly enabled model set.

### Example Response

```
{
    "jobId":"ca8c7d00-fe59-4173-ba80-449cbe5a6ab2",
    "modelSetId":"a5fea9de-7487-45b8-a9f2-878cf7069053",
    "status":"Succeeded",
    "job": {
        "operation":"UpdateScope",
        "seed": {
            "scopeId":"a5fea9de-7487-45b8-a9f2-878cf7069053",
            "isDisabled": {
                "original":true,
                "new":false
            }
        }
    }
}

```

Show More

## [Manually creating a model set version](#manually-creating-a-model-set-version)

If you disable automatic model set version creation, it is still possible to get the system to create new model set versions by calling the [POST modelsets/:modelSetId/versions](../http-docs/http-mc-modelset-service-v3-create-model-set-version-POST.md) endpoint. This has the net effect of invoking the same workflow that is run when automatic model set version creation is enabled. The logic is identical: if a new model set version can be calculated, then it is persisted. If, however, the tip versions of the models in the model set have not changed since the last time the model set version workflow was invoked, a new model set version is not persisted. As with all other data modifying workflows in the model coordination API, this call starts a job.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f83cef12-deef-4771-9feb-4f85643e3c46/modelsets/a5fea9de-7487-45b8-a9f2-878cf7069053/versions'
     -X POST
     -H 'Authorization: Bearer <token>'

```

The scopeId in the seed returned in response to the POST on the model set versions endpoint is the ID of the model set that is being targeted by the new model set version workflow.

### Example Response

```
{
    "jobId": "98d1aab3-209b-489e-96e9-51cf7d3c4724",
    "modelSetId": "a5fea9de-7487-45b8-a9f2-878cf7069053",
    "status": "Running",
    "job": {
        "seed": {
            "scopeId": "a5fea9de-7487-45b8-a9f2-878cf7069053"
        }
    }
}

```

Show More

As before, you can use a call to the [GET modelsets/:modelSetId/jobs/:jobId](../http-docs/http-mc-modelset-service-v3-get-model-set-job-GET.md) endpoint to track the progress of the new model set version workflow.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f83cef12-deef-4771-9feb-4f85643e3c46/modelsets/a5fea9de-7487-45b8-a9f2-878cf7069053/jobs/98d1aab3-209b-489e-96e9-51cf7d3c4724'
     -H 'Authorization: Bearer <token>'

```

A status of `Succeeded` indicates that the new model set version workflow has completed successfully.

### Example Response

```
{
    "jobId": "98d1aab3-209b-489e-96e9-51cf7d3c4724",
    "modelSetId": "a5fea9de-7487-45b8-a9f2-878cf7069053",
    "status": "Succeeded",
    "job": {
        "operation": "CreateScopeVersion",
        "seed": {
            "scopeId": "a5fea9de-7487-45b8-a9f2-878cf7069053"
        }
    }
}

```

Show More
