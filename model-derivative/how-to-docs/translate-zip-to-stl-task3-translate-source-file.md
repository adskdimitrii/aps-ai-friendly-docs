# Task 3 – Translate Source File

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/translate-zip-to-stl/task3-translate-source-file/

---

# Task 3 – Translate Source File

You can translate the source file to many different formats (see [Supported Translations](en/docs/model-derivative/v2/developers_guide/supported-translations) for details). For the purpose of this walkthrough, we will translate the source file to the STL format.

To translate a file, you must kick off a translation job. The translation job produces a manifest, which lists all the files that are generated. It also reports how far translation has progressed as a percentage, for each file listed in the manifest.

By the end of this task you will be able to:

- Start a translation job where the source files are within a zip file.
- Check the status of a translation job.

You will use the following operations in this task:

| Operation | HTTP Request |
| --- | --- |
| [Start Translation Job](../http-docs/http-job-POST.md) | POST /job |
| [Fetch Manifest](../http-docs/http-urn-manifest-GET.md) | GET /{urn}/manifest |

## [Step 1 - Start a translation job](#step-1-start-a-translation-job)

When you start a translation job, you specify the Base64-encoded URN of the source file, as well of the translated file format you require. You can optionally specify the region the translation must be stored.

### Request

```
curl -X 'POST' \
     -v 'https://developer.api.autodesk.com/modelderivative/v2/designdata/job' \
     -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
     -H 'Content-Type: application/json'
     -d
      '{
          "input": {
            "urn": "<BASE64_ENCODED_URN_OF_SOURCE_FILE>",
            "rootFilename": "Tuner.iam",
            "compressedUrn": true
        },
        "output": {
            "formats": [
                {
                    "type": "stl",
                    "advanced": {
                      "format" : "binary",
                      "exportColor":true,
                      "exportFileStructure" : "single"
                    }
                }
            ]
        }
      }'

```

Show More

Note the use of the `compressedUrn` and `rootFilename` attributes in the JSON payload.

### Response

```
{
  "result": "success",
  "urn": "<URL_SAFE_URN_OF_SOURCE_FILE>",
  "acceptedJobs": {
      "output": {
          "formats": [
              {
                  "type": "stl",
                  "advanced": {
                      "format": "binary",
                      "exportColor": true,
                      "exportFileStructure": "single"
                  }
              }
          ]
      }
  }
}

```

Show More

Note down the value of `urn`. This is the URL safe Base64-encoded URN of the source file. It is this URN you use to check the status of the job.

## [Step 2 - Check the Status of the translation job](#step-2-check-the-status-of-the-translation-job)

To check the status of the translation job, you must look at the manifest produced by the translation job. The `status` attribute in the manifest reports the status of the translation job. The status can be:

- `pending`: The job has been received and is pending for processing.
- `inprogress`: The job has started processing, and is running.
- `success`: The job has finished successfully.
- `failed`: The translation has failed.
- `timeout`: The translation has timed out and no output is generated.

### Request

```
curl -X GET \
     -v 'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/manifest' \
     -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

### Response

```
{
    "urn": "<URL_SAFE_URN_OF_SOURCE_FILE>",
    "derivatives": [
        {
            "children": [
                {
                    "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/799c2d78-8764-4712-bf67-a1e8b10776ff/Tuner.stl",
                    "role": "STL",
                    "exportFileStructure": "single",
                    "mime": "application/octet-stream",
                    "exportColor": true,
                    "format": "binary",
                    "guid": "99f90880-8013-4000-a9fd-dc6dd9c3efbd",
                    "type": "resource",
                    "status": "success"
                }
            ],
            "progress": "40% complete",
            "outputType": "stl",
            "status": "inprogress"
        }
    ],
    "hasThumbnail": "false",
    "progress": "40% complete",
    "type": "manifest",
    "region": "US",
    "version": "1.0",
    "status": "inprogress"
}

```

Show More
