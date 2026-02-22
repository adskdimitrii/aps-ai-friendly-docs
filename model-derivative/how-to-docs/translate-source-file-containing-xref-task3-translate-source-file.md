# Task 3 â Translate Source File

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/translate-source-file-containing-xref/task3-translate-source-file/

---

# Task 3 â Translate Source File

You can translate the source file to many different formats (see [Supported Translations](en/docs/model-derivative/v2/developers_guide/supported-translations) for details). For the purpose of this walkthrough, we will translate the source file to the STL format.

To translate a file, you must kick off a translation job. However, before you kick off the translation job, you must link the source file to its references, so that Model Derivative can fetch the referenced files from OSS for translation.

The translation job produces a manifest, which lists all the files that are generated. It also reports how far translation has progressed as a percentage, for each file listed in the manifest.

By the end of this task you will be able to:

- Define the link between a source file and its references.
- Start a translation job where the host model and references are uploaded separately to OSS.
- Check the status of a translation job.

You will use the following operations in this task:

| Operation | HTTP Request |
| --- | --- |
| [Start Translation Job](/en/docs/model-derivative/v2/reference/http/job-POST/) | POST /job |
| [Specify References](/en/docs/model-derivative/v2/reference/http/urn-references-POST/) | POST /{urn}/references |
| [Fetch Manifest](/en/docs/model-derivative/v2/reference/http/urn-manifest-GET/) | GET /{urn}/manifest |

## [Step 1 - Link source file to its references](#step-1-link-source-file-to-its-references)

The Assembly file *scissors.iam* expects its Part files to be placed in a sub-folder named *Components*. When you link the Part files to the Assembly file, you use the `relativePath` attribute in the JSON payload to address this requirement.

### Request

```
curl -X POST \
    'https://developer.api.autodesk.com/modelderivative/v2/designdata/<BASE64_ENCODED_URN_OF_SOURCE_FILE>/references' \
    -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
    -d '{
           "urn": "urn:adsk.objects:os.object:md_tute_01/scissors.iam",
           "filename": "scissors.iam",
           "references": [
              {
                 "urn": "urn:adsk.objects:os.object:md_tute_01/blade_main.ipt",
                 "relativePath": "Components/blade_main.ipt",
                 "filename": "blade_main.ipt"
              },
              {
                 "urn": "urn:adsk.objects:os.object:md_tute_01/blade_top.ipt",
                 "relativePath": "Components/blade_top.ipt",
                 "filename": "blade_top.ipt"
              },
              {
                 "urn": "urn:adsk.objects:os.object:md_tute_01/scissor_spring.ipt",
                 "relativePath": "Components/scissor_spring.ipt",
                 "filename": "scissor_spring.ipt"
              }
           ]
        }'

```

Show More

Note how the URNs of the Assembly file and Part files are specified as Base64-Encoded URNs for the `urn` attributes in the JSON body. Also note the use of the `relativePath` attribute to specify the location of the referenced files (Part files) relative to the source file (Assembly file).

### Response

```
{
    "result": "success"
}

```

## [Step 2 - Start a translation job](#step-2-start-a-translation-job)

When you start a translation job, you specify the Base64-encoded URN of the source file, as well of the translated file format you require. You can optionally specify the region the translation must be stored.

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
              "checkReferences": true
          },
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
      }'

```

Show More

Note the use of the `checkReferences` attribute in the JSON payload. This attribute instructs Model Derivative to check for references and download all referenced files. If you donât specify this attribute, translation fails.

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

## [Step 2 - Check status of translation job](#step-2-check-status-of-translation-job)

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
    "urn": "dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmMl8yMDIwXzA5XzE1L3NjaXNzb3JzLmlhbQ",
    "derivatives": [
        {
            "children": [
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmMl8yMDIwXzA5XzE1L3NjaXNzb3JzLmlhbQ/output/c55352c8-25af-4c1b-b0b5-807d43e3dabe/scissors.stl",
                    "role": "STL",
                    "exportFileStructure": "single",
                    "mime": "application/octet-stream",
                    "exportColor": true,
                    "format": "binary",
                    "guid": "13e5ddbd-1ded-46ba-b1cd-23f3ce6642b1",
                    "type": "resource",
                    "status": "success"
                }
            ],
            "progress": "60% complete",
            "outputType": "stl",
            "status": "inprogress"
        }
    ],
    "hasThumbnail": "false",
    "progress": "60% complete",
    "type": "manifest",
    "region": "US",
    "version": "1.0",
    "status": "inprogress"
}

```

Show More
