# Task 4 – Download STL file

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/translate-source-file-containing-xref/task4-download-stl-file/

---

# Task 4 – Download STL file

In order to download the translated STL file, you must wait until the translation job is complete. There are two ways you can do this:

1. Periodically download and check the manifest.
2. Set up a webhook to notify you when the job is done.

For the purpose of this walkthrough you will download the manifest and get the information you need to download the STL file. For more information on webhooks, see the documentation on [Model Derivative webhook events](https://aps.autodesk.com/en/docs/webhooks/v1/reference/events/model_derivative_events/)

By the end of this task you will be able to:

- Get the URN of a translated file (Get the URN of a derivative).
- Download a translated file (Download a derivative).

You will use the following operations in this task:

| Operation | HTTP Request |
| --- | --- |
| [Fetch Manifest](../http-docs/http-urn-manifest-GET.md) | GET /{urn}/manifest |
| [Fetch Derivative Download URL](../http-docs/http-urn-manifest-derivativeUrn-signedcookies-GET.md) | GET {urn}/manifest/{derivativeUrn}/signedcookies |

## [Step 1 - Check the status of translation job](#step-1-check-the-status-of-translation-job)

```
curl  -X GET \
      'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/manifest' \
      -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

When the translation job completes successfully, you will see a response similar to:

### Response

```
{
  "urn": "dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c2pzXzAzL3NjaXNzb3JzLmlhbQ",
  "derivatives": [
      {
          "children": [
              {
                  "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/ae8fcf0e-6820-4ae8-8e78-82960f5d9070/scissors.stl",
                  "role": "STL",
                  "exportFileStructure": "single",
                  "mime": "application/octet-stream",
                  "exportColor": true,
                  "format": "binary",
                  "guid": "3aa8c215-9f66-45c6-aa80-3b0edeabcdff",
                  "type": "resource",
                  "status": "success"
              }
          ],
          "progress": "complete",
          "outputType": "stl",
          "status": "success"
      }
  ],
  "hasThumbnail": "false",
  "messages": [
      {
          "code": "ATF-1023",
          "message": [
              "The file: {0} does not exist",
              "C:\\Users\\itools\\Desktop\\autodesk_inventor_2018_samples\\Models\\Assemblies\\Scissors\\Components\\blade_main.ipt"
          ],
          "type": "warning"
      }
  ],
  "progress": "complete",
  "type": "manifest",
  "region": "US",
  "version": "1.0",
  "status": "success"
}

```

Show More

Note down the value of the `urn` of the STL file. You will use this value when you download the STL file. For the next step we will refer to it as <URN_OF_STL_FILE>.

## [Step 2 - Obtain Signed Cookie](#step-2-obtain-signed-cookie)

In this step, you obtain a CloudFront download URL and a set of CloudFront signed cookies to download the STL file that was generated in task 3.

### Request

```
curl -X GET \

     'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/manifest/<URN_OF_STL_FILE>/signedcookies' \
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
x-ads-duration: 48 ms
x-ads-region: US
x-ads-startup-time: Tue May 24 06:11:48 UTC 2022
Content-Length: 262
Connection: keep-alive

{

  "etag": "561cd8670926bc0acd8d431d51c6b1c3",
  "size": 89884,
  "url": "<DOWNLOAD_URL>",
  "content-type": "application/vnd.ms-pki.stl",
  "expiration": 1653576191971
}

```

Show More

Note down the download URL returned in the response body and the signed cookies returned in the response header. You will use these values for the next step.

## [Step 3 - Download the STL file](#step-3-download-the-stl-file)

Use the download URL and the signed cookies to download OBJ file that was generated in task 3. The signed cookies protect access to the STL file while letting you download it securely.

### Request

```
curl -X GET \
    '<SIGNED_DOWNLOAD_URL>'\
     -H 'Cookie: <FIRST_SIGNED_COOKIE>;<SECOND_SIGNED_COOKIE>;<THIRD_SIGNED_COOKIE>'

```

### Response

```
<CONTENT_OF_STL_FILE>

```

## [Step 4 - Save the STL file](#step-4-save-the-stl-file)

- Copy the chunked content body to a text file and save it as *scissors.stl*

**Notes:**

To display the saved file:
:   1. If you are using an Apple Macintosh, right-click *scissors.stl* in Finder and select **Quick View** from the menu.
    2. If you are using Windows, right-click *scissors.stl* in Windows Explorer and select **Open with > 3D Viewer** from the menu.
