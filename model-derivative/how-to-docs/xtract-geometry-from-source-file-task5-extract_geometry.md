# Task 5 – Extract Geometry

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/xtract-geometry-from-source-file/task5-extract_geometry/

---

# Task 5 – Extract Geometry

In the previous task you listed the properties of the objects contained within a view. In this task, you select two specific objects and translate them into the OBJ format. You use [`Create Translation Job`_](#id7) to translate the objects. This request is the same as the one you sent in Task 3 when you translated the Inventor model to SVF2. However, for this task you explicitly specify what objects to translate, so that the server doesn’t translate the entire model. When you translate specific objects, you can only translate to the OBJ format.

By the end of this task you will be able to:

- Translate specific objects to the OBJ format.
- Check the state of a translation for a source file that has multiple derivatives.

  Note: The translation job you kick off in this task updates the same manifest you created in Task 3 (translation to SVF2).

You will use the following operations in this task:

| Operation | HTTP Request |
| --- | --- |
| [Start Translation Job](../http-docs/http-job-POST.md) | POST /job |
| [Fetch All Properties](../http-docs/http-urn-metadata-guid-properties-GET.md) | GET /{urn}/metadata/{modelGuid}/properties |
| [Fetch Derivative Download URL](../http-docs/http-urn-manifest-derivativeUrn-signedcookies-GET.md) | GET /{urn}/manifest/{derivativeUrn}/signedcookies |

## [Step 1 - Translate specific objects to the OBJ format](#step-1-translate-specific-objects-to-the-obj-format)

Once you have the `objectid` of geometry, you can translate it to the OBJ format.

### Request

```
curl -X POST \
     'https://developer.api.autodesk.com/modelderivative/v2/designdata/job' \
     -H 'Content-Type: application/json' \
     -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
     -H 'x-ads-force: true' \
     -d '{
      "input": {
          "urn": "<URL_SAFE_URN_OF_SOURCE_FILE>"
      },
      "output": {
          "destination": {
              "region": "us"
          },
          "formats": [
              {
                  "type": "obj",
                  "advanced": {
                      "modelGuid":"b5664c2a-5c6c-4c04-bf07-3474278a9df3",
                      "objectIds" : [4,5]
                  }
              }
          ]
      }
  }'

```

Show More

Note `modelGuid` and `objectIds`. The value of `modelGuid` is the `guid` of the Viewable that contains the geometry to extract. You obtained this ID in Step 2 of the previous task. The value of `objectIds` is taken from the value of `objectid` in the list of objects you extracted in Step 2 of the previous task.

### Response

```
{
  "result": "success",
  "urn": "<URL_SAFE_URN_OF_SOURCE_FILE>",
  "acceptedJobs": {
    "output": {
      "destination": {
        "region": "us"
      },
      "formats": [
        {
          "type": "obj",
          "advanced": {
            "modelGuid": "404842ee-2a8c-4166-814a-121e382a7d1b",
            "objectIds": [
              4,
              5
            ]
          }
        }
      ]
    }
  }
}

```

Show More

## [Step 2 - Check status of job](#step-2-check-status-of-job)

Note: This is the same request you used in Task 3 to check the status of the job.

### Request

```
curl  -X GET \
      'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/manifest' \
      -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

The manifest contains details of the previous translation (to SVF2) as well as the translation job you just kicked off (to OBJ). To check if the translation job is complete, verify whether the `status` of the OBJ derivative is `success` (see line numbers 80 to 82, which are highlighted in the response).

### Response

```
{
      "urn": "<URL_SAFE_URN_OF_SOURCE_FILE>",
      "derivatives": [
          {
              "hasThumbnail": "true",
              "children": [
                  {
                      "guid": "5a77338a-ba86-4cdd-9e14-c5d3f252108d",
                      "hasThumbnail": "true",
                      "role": "3d",
                      "name": "Scene",
                      "progress": "complete",
                      "type": "geometry",
                      "status": "success",
                      "children": [
                          {
                              "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/1/Stapler.svf2",
                              "role": "graphics",
                              "mime": "application/autodesk-svf2",
                              "guid": "b90bbb37-d60e-412c-aedc-bf8c049f0dc7",
                              "type": "resource"
                          },
                          {
                              "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/1/Stapler.svf2.png01_thumb_400x400.png",
                              "role": "thumbnail",
                              "mime": "image/png",
                              "guid": "827199c4-4bc9-487c-9a3b-d5777ba7e84e",
                              "type": "resource",
                              "resolution": [
                                  400,
                                  400
                              ]
                          },
                          {
                              "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/1/Stapler.svf2.png01_thumb_200x200.png",
                              "role": "thumbnail",
                              "mime": "image/png",
                              "guid": "25797df6-0f7d-4ab4-ad51-614b98365ff9",
                              "type": "resource",
                              "resolution": [
                                  200,
                                  200
                              ]
                          },
                          {
                              "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/1/Stapler.svf2.png01_thumb_100x100.png",
                              "role": "thumbnail",
                              "mime": "image/png",
                              "guid": "64efdc65-7471-475d-8dab-ab28e1e0e595",
                              "type": "resource",
                              "resolution": [
                                  100,
                                  100
                              ]
                          }
                      ]
                  },
                  {
                      "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/1/properties.db",
                      "role": "Autodesk.CloudPlatform.PropertyDatabase",
                      "mime": "application/autodesk-db",
                      "guid": "855a4640-d702-401a-8c77-56cc0b4b6146",
                      "type": "resource",
                      "status": "success"
                  }
              ],
              "name": "Stapler.iam",
              "progress": "complete",
              "outputType": "svf2",
              "status": "success"
          },
          {
              "hasThumbnail": "false",
              "children": [
                  {
                      "modelGuid": "b90bbb37-d60e-412c-aedc-bf8c049f0dc7",
                      "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/geometry/b576231b-9684-3609-8fa0-1221a424a77c.obj",
                      "role": "obj",
                      "guid": "1bbf31c4-99f9-36e7-af03-d7b2e0caa93b",
                      "type": "resource",
                      "objectIds": [
                          4,
                          5
                      ],
                      "status": "success"
                  },
                  {
                      "modelGuid": "b90bbb37-d60e-412c-aedc-bf8c049f0dc7",
                      "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/geometry/b576231b-9684-3609-8fa0-1221a424a77c.mtl",
                      "role": "obj",
                      "guid": "fed3c1b1-3c99-34d1-81f1-79f6fea72576",
                      "type": "resource",
                      "objectIds": [
                          4,
                          5
                      ],
                      "status": "success"
                  }
              ],
              "progress": "complete",
              "outputType": "obj",
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

Note down the URN of the translated OBJ file (see line 77, which is highlighted in the response). You use this URN to download the OBJ file.

## [Step 3 - Obtain Signed Cookie](#step-3-obtain-signed-cookie)

In this step, you obtain a CloudFront download URL and a set of CloudFront signed cookies to download the OBJ file that was generated in task 3.

### Request

```
curl -X GET \
     'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/manifest/<URN_OF_OBJ_FILE>/signedcookies' \
     -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

### Response

```
HTTP/1.1 200 OK
Content-Encoding: gzip
Content-Type: application/json; charset=utf-8
Date: Thu, 26 May 2022 03:57:31 GMT
Set-Cookie: <FIRST_SIGNED_COOKIE>
Set-Cookie: <SECOND_SIGNED_COOKIE>
Set-Cookie: <THIRD_SIGNED_COOKIE>
Strict-Transport-Security: max-age=31536000; includeSubDomains
Vary: Accept-Encoding
x-ads-app-identifier: platform-viewing-2022.05.01.75.c20538dec-production
x-ads-duration: 37 ms
x-ads-region: US
x-ads-startup-time: Tue May 24 06:34:02 UTC 2022
Content-Length: 260
Connection: keep-alive

{
    "etag": "1b2b87eeba06472a166cae60eda14f8d",
    "size": 79577,
    "url": "<DOWNLOAD_URL>",
    "content-type": "application/x-tgif",
    "expiration": 1653578910721
}

```

Show More

Note down the download URL returned in the response body and the signed cookies returned in the response header. You will use these values for the next step.

## [Step 4 - Download the OBJ file containing the extracted geometry](#step-4-download-the-obj-file-containing-the-extracted-geometry)

Use the download URL and the signed cookies to download OBJ file that was generated in task 3. The signed cookies protect access to the OBJ file while letting you download it securely.

### Request

```
curl -X GET \
    '<SIGNED_DOWNLOAD_URL>'\
     -H 'Cookie: <FIRST_SIGNED_COOKIE>;<SECOND_SIGNED_COOKIE>;<THIRD_SIGNED_COOKIE>'

```

### Response

```
<CONTENT_OF_OBJ_FILE>

```

## [Step 5 - Save the OBJ file](#step-5-save-the-obj-file)

- Copy the chunked content body to a text file and save it as *stapler-geometry.obj*

**Notes**

To display the saved file:
:   1. If you are using an Apple Macintosh, right-click *stapler-geometry.obj* in Finder and select **Quick View** from the menu.
    2. If you are using Windows, right-click *stapler-geometry.obj* in Windows Explorer and select **Open with > 3D Viewer** from the menu.
