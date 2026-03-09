# Task 4 â Download STL file

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/translate-zip-to-stl/task4-download-stl-file/

---

# Task 4 â Download STL file

In order to download the translated STL file, you must wait until the translation job is complete. There are two ways to check if the translation job is done:

1. Periodically download and check the manifest.
2. Set up a webhook to notify you when the job is done.

For this walkthrough you download the manifest and check the status of the job. For more information on webhooks, see the documentation on [Model Derivative webhook events](https://aps.autodesk.com/en/docs/webhooks/v1/reference/events/model_derivative_events/)

By the end of this task you will be able to:

- Get the URN of a translated file (Get the URN of a derivative).
- Download a translated file (Download a derivative).

You will use the following operations in this task:

## [Step 1 - Check the status job](#step-1-check-the-status-job)

In this step you check if the translation job is done (by verifying that `progress` is `complete`). You proceed to the next step only if the translation job is done.

```
curl -X GET \
     -v 'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/manifest' \
     -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

When the translation job completes successfully, you see a response similar to:

### Response

```
{
  "urn":"dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c2pzc18wMi9UdW5lci56aXA",
  "derivatives":[
    {
      "children":[
        {
          "urn":"urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c2pzc18wMi9UdW5lci56aXA/output/9ab9410a-38fc-4105-a966-cc5c264e0d52/Tuner.stl",
          "role":"STL",
          "exportFileStructure":"single",
          "mime":"application/octet-stream",
          "exportColor":true,
          "format":"binary",
          "guid":"db55b0eb-649c-415e-b9aa-237744eb8e6f",
          "type":"resource",
          "status":"success"
        }
      ],
      "progress":"complete",
      "outputType":"stl",
      "status":"success"
    }
  ],
  "hasThumbnail":"false",
  "progress":"complete",
  "type":"manifest",
  "region":"US",
  "version":"1.0",
  "status":"success"
}

```

Show More

Notice that the translation job has produced two derivatives; an STL file and an MTL file. For this walkthrough we are only interested in the STL file. The MTL file is an auxiliary file containing material definitions, which can be accessed by the STL file. If the source file contained textures, you would have seen a third child in the list of derivatives.

Note down the value of the `urn` of the STL file. You will use this value when you download the STL file. For the next step we will refer to it as <URN_OF_STL_FILE>.

## [Step 2 - Obtain Signed Cookie](#step-2-obtain-signed-cookie)

In this step, you obtain a CloudFront download URL and a set of CloudFront signed cookies to download the OBJ file that was generated in task 3.

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
Vary: Accept-Encoding
x-ads-app-identifier: platform-viewing-2022.05.01.75.c20538dec-production
x-ads-duration: 29 ms
x-ads-region: US
x-ads-startup-time: Tue May 24 06:19:02 UTC 2022
Content-Length: 257
Connection: keep-alive

{
    "etag": "0559302c6055f38a2a8998781337d3dd",
    "size": 620684,
    "url": "<DOWNLOAD_URL>",
    "content-type": "application/vnd.ms-pki.stl",
    "expiration": 1653573457736
}

```

Show More

Note down the download URL returned in the response body and the signed cookies returned in the response header. You will use these values for the next step.

## [Step 3 - Download the STL file](#step-3-download-the-stl-file)

Use the download URL and the signed cookies to download STL file that was generated in task 3. The signed cookies protect access to the STL file while letting you download it securely.

- Send a request to download the OBJ file.

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

- Copy the chunked content body to a text file and save it as *Tuner.stl*

**Notes**

To display the saved file:
1. If you are using an Apple Macintosh, right-click *Tuner.stl* in Finder and select **Quick View** from the menu.
2. If you are using Windows, right-click *Tuner.stl* in Windows Explorer and select **Open with > 3D Viewer** from the menu.
