# Task 4 â Download OBJ file

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/translate-to-obj/task4-download-obj-file/

---

# Task 4 â Download OBJ file

In order to download the translated OBJ file, you must wait until the translation job is complete. There are two ways you can do this:

1. Periodically download and check the manifest.
2. Set up a webhook to notify you when the job is done.

For the purpose of this walkthrough you will download the manifest and get the information you need to download the OBJ file. For more information on webhooks, see the documentation on [Model Derivative webhook events](/en/docs/webhooks/v1/reference/events/model_derivative_events/)

By the end of this task you will be able to:

- Get the URN of a translated file (Get the URN of a derivative).
- Download a translated file (Download a derivative).

You will use the following operations in this task:

| Operation | HTTP Request |
| --- | --- |
| [Fetch Manifest](/en/docs/model-derivative/v2/reference/http/urn-manifest-GET) | GET /{urn}/manifest |
| [Fetch Derivative Download URL](/en/docs/model-derivative/v2/reference/http/urn-manifest-derivativeUrn-signedcookies-GET/) | GET /{urn}/manifest/{derivativeUrn}/signedcookies |

## [Step 1 - Check status of job](#step-1-check-status-of-job)

In this step you check if the translation job is done (by verifying that `progress` is `complete`). You proceed to the next step only if the translation job is done.

```
curl -X GET \
     -v 'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/manifest' \
     -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

When the translation job completes successfully, you will see a response similar to:

### Response

```
{
  "urn": "<URL_SAFE_URN_OF_SOURCE_FILE>",
  "derivatives": [
      {
          "hasThumbnail": "false",
          "children": [
              {
                  "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/54c07512-6b0c-41fd-8a13-012e0fff3ca9/box.obj",
                  "role": "OBJ",
                  "mime": "application/octet-stream",
                  "guid": "8eac4812-11bd-446a-b8d0-f1d09ebf8d03",
                  "type": "resource",
                  "status": "success"
              },
              {
                  "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/54c07512-6b0c-41fd-8a13-012e0fff3ca9/box.mtl",
                  "role": "OBJ",
                  "mime": "application/octet-stream",
                  "guid": "4e00b88e-cbcb-4644-b6ae-5ef3d206d27d",
                  "type": "resource",
                  "status": "success"
              }
          ],
          "name": "box.ipt",
          "progress": "complete",
          "outputType": "obj",
          "status": "success"
      }
  ],
  "hasThumbnail": "false",
  "progress": "complete",
  "type": "manifest",
  "region": "US",
  "version": "1.0",
  "status": "success"
}

```

Show More

Notice that the translation job has produced two derivatives; an OBJ file and an MTL file. For this walkthrough we are only interested in the OBJ file. The MTL file is an auxiliary file containing material definitions, which can be accessed by the OBJ file. If the source file contained textures, you would have seen a third child in the list of derivatives.

Note down the value of the `urn` of the OBJ file. You will use this value when you download the OBJ file. For the next step we will refer to it as <URN_OF_OBJ_FILE>.

## [Step 2 - Obtain signed cookie](#step-2-obtain-signed-cookie)

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
Vary: Accept-Encoding
x-ads-app-identifier: platform-viewing-2022.05.01.75.c20538dec-production
x-ads-duration: 25 ms
x-ads-region: US
x-ads-startup-time: Tue May 24 06:34:02 UTC 2022
Content-Length: 256
Connection: keep-alive

{
    "etag": "be2a39d08bee2113ca39e64f5d7b9065",
    "size": 4559,
    "url": "<DOWNLOAD_URL>",
    "content-type": "application/x-tgif",
    "expiration": 1653559051930

}

```

Show More

Note down the download URL returned in the response body and the signed cookies returned in the response header. You will use these values for the next step.

## [Step 3 - Download OBJ file](#step-3-download-obj-file)

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

## [Step 4 - Save OBJ file](#step-4-save-obj-file)

- Copy the content to a text file and save it as *box.obj*

**Notes:**

To display the saved file:
1. If you are using an Apple Macintosh, right-click *box.obj* in Finder and select **Quick View** from the menu.
2. If you are using Windows, right-click *box.obj* in Windows Explorer and select **Open with > 3D Viewer** from the menu.
