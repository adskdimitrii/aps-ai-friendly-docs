# Task 3 – Translate Source File

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/translate-to-obj/task3-translate-source-file/

---

# Task 3 – Translate Source File

You can translate the source file to many different formats (see [Supported Translations](https://aps.autodesk.com/en/docs/model-derivative/v2/developers_guide/supported-translations/) for details). For the purpose of this walkthrough, we will translate the source file to the OBJ format.

To translate a file, you must kick off a translation job. The translation job produces a manifest, which lists all the files that are generated. It also reports how far translation has progressed as a percentage, for each file listed in the manifest.

By the end of this task you will be able to:

- Start a translation job to translate a single source file.
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
     -H 'Content-Type: application/json' \
     -d
      '{
        "input": {
          "urn": "<BASE64_ENCODED_URN_OF_SOURCE_FILE>"
        },
        "output": {
          "formats": [
            {
              "type": "obj"
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
    "registerKeys": [
        "c7348a17-9e49-4752-8713-75ba2576b87c"
    ],
    "acceptedJobs": {
        "output": {
            "formats": [
                {
                    "type": "obj"
                }
            ]
        }
    }
}

```

Show More

Note down the value of `urn`. This is the URL safe Base64-encoded URN of the source file. It is this URN you use to check the status of the job.

## [Step 2 - Check the status of the translation job](#step-2-check-the-status-of-the-translation-job)

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

### Response 1

```
{
  "urn": "<URL_SAFE_URN_OF_SOURCE_FILE>",
  "derivatives": [],
  "hasThumbnail": "false",
  "progress": "0% complete",
  "type": "manifest",
  "region": "US",
  "version": "1.0",
  "status": "inprogress"
}

```

Show More

### Response 2

```
{
  "urn": "<URL_SAFE_URN_OF_SOURCE_FILE>",
  "derivatives": [
      {
          "hasThumbnail": "false",
          "children": [
              {
                  "urn": "urn:adsk.viewing:fs.file: <URL_SAFE_URN_OF_SOURCE_FILE>/output/54c07512-6b0c-41fd-8a13-012e0fff3ca9/box.obj",
                  "role": "OBJ",
                  "mime": "application/octet-stream",
                  "guid": "8eac4812-11bd-446a-b8d0-f1d09ebf8d03",
                  "type": "resource",
                  "status": "success"
              }
          ],
          "name": "box.ipt",
          "progress": "50% complete",
          "outputType": "obj",
          "status": "success"
      }
  ],
  "hasThumbnail": "false",
  "progress": "50% complete",
  "type": "manifest",
  "region": "US",
  "version": "1.0",
  "status": "inprogress"
}

```

Show More
