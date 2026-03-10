# Task 3 – Translate to SVF2

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/xtract-metadata/task3-translate-source-file/

---

# Task 3 – Translate to SVF2

For the server to extract metadata from a model, you must first translate the model to a viewer-friendly format. Because SVF2 handles larger models better, Autodesk recommends SVF2 over SVF.

By the end of this task you will be able to:

- Start a translation job.
- Check the status of a translation job

You will use the following operations in this task:

| Operation | HTTP Request |
| --- | --- |
| [Start Translation Job](../http-docs/http-job-POST.md) | POST /job |
| [Fetch Manifest](../http-docs/http-urn-manifest-GET.md) | GET /{urn}/manifest |

## [Step 1 - Start a translation job](#step-1-start-a-translation-job)

When you start a translation job, you specify the Base64-encoded URN of the source file, as well of the translated file format you require, which is SVF2 in this case. You can optionally specify the region the translation must be stored.

### Request

```
curl  -X POST \
      'https://developer.api.autodesk.com/modelderivative/v2/designdata/job' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
      -H 'x-ads-force: true' \
      -d '{
          "input": {
              "urn": "<BASE64_ENCODED_URN_OF_SOURCE_FILE>"
          },
          "output": {
              "formats": [
                  {
                      "type": "svf2",
                      "views": [
                          "2d",
                          "3d"
                      ]
                  }
              ]
          }
      }'

```

Show More

### Response

```
{
    "result": "success",
    "urn": "dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxfZGVyaXZhdGl2ZV9wcm9wX2VuaGFuY2VtZW50X3Rlc3RpbmcvcmFjX2Jhc2ljX3NhbXBsZV9wcm9qZWN0LnJ2dA",
    "acceptedJobs": {
        "output": {
            "formats": [
                {
                    "type": "svf2",
                    "views": [
                        "2d",
                        "3d"
                    ]
                }
            ]
        }
    }
}

```

Show More

Note down the value of `urn`. This is the URL safe Base64-encoded URN of the source file. It is this URN you use to check the status of the translation job.

## [Step 2 - Check the Status of the translation job](#step-2-check-the-status-of-the-translation-job)

There are two ways to check the status of a translation job. The first is to set up a webhook that notifies you when the jib is done. The second is to poll the status of the job periodically. For this walkthrough, you will be polling the status of the translation job. This means that you must periodically inspect the manifest produced by the translation job. The `status` attribute in the manifest reports the status of the translation job. The status can be:

- `pending`: The job has been received and is pending for processing.
- `inprogress`: The job has started processing, and is running.
- `success`: The job has finished successfully.
- `failed`: The translation has failed.
- `timeout`: The translation has timed out and no output is generated.

### Request

```
curl  -X GET \
      'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/manifest' \
      -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

### Response

```
{
    "urn": "dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxfZGVyaXZhdGl2ZV9wcm9wX2VuaGFuY2VtZW50X3Rlc3RpbmcvcmFjX2Jhc2ljX3NhbXBsZV9wcm9qZWN0LnJ2dA",
    "derivatives": [
        {
            "hasThumbnail": "true",
            "children": [
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxfZGVyaXZhdGl2ZV9wcm9wX2VuaGFuY2VtZW50X3Rlc3RpbmcvcmFjX2Jhc2ljX3NhbXBsZV9wcm9qZWN0LnJ2dA/output/Resource/model.sdb",
                    "role": "Autodesk.CloudPlatform.PropertyDatabase",
                    "mime": "application/autodesk-db",
                    "guid": "6fac95cb-af5d-3e4f-b943-8a7f55847ff1",
                    "type": "resource",
                    "status": "success"
                },
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxfZGVyaXZhdGl2ZV9wcm9wX2VuaGFuY2VtZW50X3Rlc3RpbmcvcmFjX2Jhc2ljX3NhbXBsZV9wcm9qZWN0LnJ2dA/output/Resource/AECModelData.json",
                    "role": "Autodesk.AEC.ModelData",
                    "mime": "application/json",
                    "guid": "a4aac952-a3f4-031c-4113-b2d9ac2d0de6",
                    "type": "resource",
                    "status": "success"
                },
                {
                    "phaseNames": "Working Drawings",
                    "role": "3d",
                    "hasThumbnail": "false",
                    "children": [
                        {
                            "guid": "44745acb-ebea-4fb9-a091-88d28bd746c7-000ea86d",
                            "type": "view",
                            "role": "3d",
                            "name": "{3D}",
                            "status": "inprogress",
                            "progress": "35% complete"
                        }
                    ],
                    "success": "99%",
                    "name": "{3D}",
                    "guid": "250a6ce5-ee70-fdca-bfc9-4111f54e9baa",
                    "progress": "35% complete",
                    "type": "geometry",
                    "viewableID": "44745acb-ebea-4fb9-a091-88d28bd746c7-000ea86d",
                    "status": "inprogress"
                },
                {
                    "guid": "6d3acd40-53b7-41b4-9d96-72e9eaf4bc89-0005d699",
                    "type": "geometry",
                    "role": "2d",
                    "name": "A102 - Plans",
                    "viewableID": "6d3acd40-53b7-41b4-9d96-72e9eaf4bc89-0005d699",
                    "phaseNames": "Working Drawings",
                    "status": "inprogress",
                    "progress": "30% complete"
                },
                {
                    "guid": "96cdd175-e436-4cac-a08f-bf0fabb86ac5-0007af95",
                    "type": "geometry",
                    "role": "2d",
                    "name": "A104 - Elev./Sec./Det.",
                    "viewableID": "96cdd175-e436-4cac-a08f-bf0fabb86ac5-0007af95",
                    "phaseNames": "Working Drawings",
                    "status": "inprogress"
                },
                {
                    "guid": "f11061a0-4a15-4ce6-9ed0-20da98b45046-000e9ee8",
                    "type": "geometry",
                    "role": "2d",
                    "name": "A103 - Elevations/Sections",
                    "viewableID": "f11061a0-4a15-4ce6-9ed0-20da98b45046-000e9ee8",
                    "phaseNames": "Working Drawings",
                    "status": "inprogress"
                },
                {
                    "guid": "f11061a0-4a15-4ce6-9ed0-20da98b45046-000e9f2b",
                    "type": "geometry",
                    "role": "2d",
                    "name": "A105 - Elev./ Stair Sections",
                    "viewableID": "f11061a0-4a15-4ce6-9ed0-20da98b45046-000e9f2b",
                    "phaseNames": "Working Drawings",
                    "status": "inprogress"
                },
                {
                    "guid": "e9248f2e-7bb7-4baf-8541-afac7b6872de-000ea29f",
                    "type": "geometry",
                    "role": "2d",
                    "name": "A101 - Site Plan",
                    "viewableID": "e9248f2e-7bb7-4baf-8541-afac7b6872de-000ea29f",
                    "phaseNames": "Working Drawings",
                    "status": "inprogress"
                },
                {
                    "guid": "666da4f5-76ba-443a-9fe6-0bcd8a1bcfe9-000ea416",
                    "type": "geometry",
                    "role": "2d",
                    "name": "A001 - Title Sheet",
                    "viewableID": "666da4f5-76ba-443a-9fe6-0bcd8a1bcfe9-000ea416",
                    "status": "inprogress"
                }
            ],
            "name": "rac_basic_sample_project.rvt",
            "progress": "20% complete",
            "outputType": "svf2",
            "properties": {
                "Document Information": {
                    "RVTVersion": "2020",
                    "Project Name": "Sample House",
                    "Project Number": "001-00",
                    "Author": "Samuel Macalister",
                    "Project Address": "Enter address here",
                    "Project Issue Date": "Issue Date",
                    "Project Status": "Project Status",
                    "Building Name": "Samuel Macalister sample house design",
                    "Client Name": "Autodesk",
                    "Organization Name": "Autodesk",
                    "Organization Description": ""
                }
            },
            "status": "inprogress"
        },
        {
            "children": [
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxfZGVyaXZhdGl2ZV9wcm9wX2VuaGFuY2VtZW50X3Rlc3RpbmcvcmFjX2Jhc2ljX3NhbXBsZV9wcm9qZWN0LnJ2dA/output/preview1.png",
                    "role": "thumbnail",
                    "mime": "image/png",
                    "guid": "db899ab5-939f-e250-d79d-2d1637ce4565",
                    "type": "resource",
                    "resolution": [
                        100,
                        100
                    ],
                    "status": "success"
                },
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxfZGVyaXZhdGl2ZV9wcm9wX2VuaGFuY2VtZW50X3Rlc3RpbmcvcmFjX2Jhc2ljX3NhbXBsZV9wcm9qZWN0LnJ2dA/output/preview2.png",
                    "role": "thumbnail",
                    "mime": "image/png",
                    "guid": "3f6c118d-f551-7bf0-03c9-8548d26c9772",
                    "type": "resource",
                    "resolution": [
                        200,
                        200
                    ],
                    "status": "success"
                },
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxfZGVyaXZhdGl2ZV9wcm9wX2VuaGFuY2VtZW50X3Rlc3RpbmcvcmFjX2Jhc2ljX3NhbXBsZV9wcm9qZWN0LnJ2dA/output/preview4.png",
                    "role": "thumbnail",
                    "mime": "image/png",
                    "guid": "4e751806-0920-ce32-e9fd-47c3cec21536",
                    "type": "resource",
                    "resolution": [
                        400,
                        400
                    ],
                    "status": "success"
                }
            ],
            "progress": "complete",
            "outputType": "thumbnail",
            "status": "success"
        }
    ],
    "hasThumbnail": "true",
    "progress": "20% complete",
    "type": "manifest",
    "region": "US",
    "version": "1.0",
    "status": "inprogress"
}

```

Show More
