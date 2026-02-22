# Task 3 â Translate to SVF2

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/prep-file4viewer/task3-translate-source-file/

---

# Task 3 â Translate to SVF2

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
              "urn": "<BASE64_ENCODED_URN_OF_SOURCE_FILE>",
              "rootFilename": "Suspension.iam",
              "compressedUrn": true
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
  "urn": "<URL_SAFE_URN_OF_SOURCE_FILE>",
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

```

Show More

}

Note down the value of `urn`. This is the URL safe Base64-encoded URN of the source file. It is this URN you use to check the status of the translation job.

## [Step 2 - Check the Status of the translation job](#step-2-check-the-status-of-the-translation-job)

To check the status of the translation job, you must look at the manifest produced by the translation job. The `status` attribute in the manifest reports the status of the translation job. The status can be:

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
   "urn": "<URL_SAFE_URN_OF_SOURCE_FILE>",
   "derivatives": [
      {
         "hasThumbnail": "true",
         "children": [
            {
               "role": "3d",
               "hasThumbnail": "true",
               "children": [
                  {
                     "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmMl9nYV90ZXN0L1N1c3BlbnNpb24uemlw/output/1/Suspension.svf.png01_thumb_400x400.png",
                     "role": "thumbnail",
                     "mime": "image/png",
                     "guid": "422273d9-06ba-45a1-b861-c8616fd48279",
                     "type": "resource",
                     "resolution": [
                        400,
                        400
                     ]
                  },
                  {
                     "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmMl9nYV90ZXN0L1N1c3BlbnNpb24uemlw/output/1/Suspension.svf.png01_thumb_200x200.png",
                     "role": "thumbnail",
                     "mime": "image/png",
                     "guid": "156bbe62-914d-4479-bc85-02771568a8dd",
                     "type": "resource",
                     "resolution": [
                        200,
                        200
                     ]
                  },
                  {
                     "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmMl9nYV90ZXN0L1N1c3BlbnNpb24uemlw/output/1/Suspension.svf.png01_thumb_100x100.png",
                     "role": "thumbnail",
                     "mime": "image/png",
                     "guid": "1dd08431-b9c7-4b27-b362-009f2d22a167",
                     "type": "resource",
                     "resolution": [
                        100,
                        100
                     ]
                  },
                  {
                     "role": "graphics",
                     "mime": "application/autodesk-svf2",
                     "guid": "d9104a8d-fb59-4e0d-b5d9-93e0f254aba0",
                     "type": "resource"
                  }
               ],
               "name": "Scene",
               "guid": "0a6f031a-79dc-4fba-8bb3-6c5b4301b391",
               "progress": "complete",
               "type": "geometry",
               "status": "success"
            },
            {
               "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmMl9nYV90ZXN0L1N1c3BlbnNpb24uemlw/output/1/properties.db",
               "role": "Autodesk.CloudPlatform.PropertyDatabase",
               "mime": "application/autodesk-db",
               "guid": "86d50222-8a24-487e-ad5a-26126ef1fedb",
               "type": "resource",
               "status": "success"
            }
         ],
         "name": "Suspension.iam",
         "progress": "complete",
         "outputType": "svf2",
         "status": "success"
      }
   ],
   "hasThumbnail": "true",
   "progress": "complete",
   "type": "manifest",
   "region": "US",
   "version": "1.0",
   "status": "success"
}

```

Show More

Note down the value of the `urn` attribute highlighted above. This is the URL safe Base64-encoded of the source file. You must embed this value in the JavaScript code handling the viewer in order to display this model in the viewer.
