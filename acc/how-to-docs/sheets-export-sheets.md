# Export Sheets from ACC Build

Source: https://aps.autodesk.com/en/docs/acc/tutorials/sheets/export-sheets/

---

# Export Sheets from ACC Build

This tutorial demonstrates how to export sheets from the Sheets tool in ACC Build into a new downloadable PDF file. The steps include finding the IDs of the sheets you want to export, exporting the sheets (you can optionally also export associated markups and hyperlinks), verifying the status of the export, getting a download link, and downloading the exported sheets.

Note the following limitations for exporting sheets:

- You can export up to 1000 sheets at a time.
- Currently, sheets can only be exported into PDF format.

For more information about exporting sheets, See the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Export_Sheets).

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps), and select the Autodesk Construction Cloud API.
- [Provision your app](https://aps.autodesk.com/en/docs/bim360/v1/tutorials/getting-started/manage-access-to-docs/) to acquire access to your ACC account.
- Acquire a [2-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [3-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth token with `data:write` scope.
- Find the project ID for the project that contains the sheets you want to export by following the [Retrieve a Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this tutorial, assume that the project ID is `b.139532ee-5cdb-4c9e-a293-652693991e65`.
- Verify that you have access to the relevant ACC project, and that you have the permissions to export sheets. Note that by default, users are allowed to export sheets.

## [Step 1: Find the IDs of the Sheets to Export](#step-1-find-the-ids-of-the-sheets-to-export)

Find the IDs of the sheets you want to export using the project ID (`b.139532ee-5cdb-4c9e-a293-652693991e65`), by calling [GET sheets](../http-docs/http-sheets-sheets-GET.md).

If you want to export sheets associated with a specific version set, first call [GET version sets](../http-docs/http-sheets-version-sets-GET.md) to get the version set ID, and then call [GET sheets](../http-docs/http-sheets-sheets-GET.md) using the version set filter (`filter[versionSetId]`).

In this example we are using a version set filter (`7c2ecde0-2406-49f9-9199-50176848a0b7`) to retrieve all the sheets associated with the specific version set.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/b.139532ee-5cdb-4c9e-a293-652693991e65/sheets?currentOnly=true&filter[versionSetId]=7c2ecde0-2406-49f9-9199-50176848a0b7' \
     -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

Note that some lines in this payload example have been omitted for readability.

```
 {
  "results": [
    {
      "id": "0d7a5883-1694-3078-a06d-ad24413f8b06",
      "number": "A-01",
      "versionSet": {
        "id": "7c2ecde0-2406-49f9-9199-50176848a0b7",
        "name": "one set",
        "issuanceDate": "2021-07-01T00:00:00.000Z",
        "deleted": false
      },
      "createdAt": "2021-07-01T05:21:05.391Z",
      "createdBy": "45GPJ4KAX789",
      "createdByName": "John Smith",
      "updatedAt": "2021-07-01T05:21:05.391Z",
      "updatedBy": "45GPJ4KAX789",
      "updatedByName": "John Smith",
      "title": "Floor One",
      "uploadFileName": "example.pdf",
      "uploadId": "5cb5d9da-060e-421e-bca9-97dd8b5cd800",
      "tags": [
        "april",
        "floor"
      ],
      "paperSize": [
        1000,
        600
      ],
      "isCurrent": true,
      "deleted": false,
      "deletedAt": null,
      "deletedBy": null,
      "deletedByName": null,
      "viewable": {
        "urn": "urn:adsk.bimdocs:seed:207edb73-69c2-43d2-ba0e-e2ffe9fdcb56",
        "guid": "cc3eb847-737f-3408-bdbd-e2628a02b8de"
      }
    }
  ],
  "pagination": {
    "limit": 100,
    "offset": 0,
    "previousUrl": null,
    "nextUrl": null,
    "totalResults": 1
  }
}

```

Show More

Note the IDs of the sheets (`results[i].id`) you want to export (`0d7a5883-1694-3078-a06d-ad24413f8b06`).

## [Step 2: Export the ACC Sheets](#step-2-export-the-acc-sheets)

To export the sheet, use the project ID (`b.139532ee-5cdb-4c9e-a293-652693991e65`) and the sheet ID (`0d7a5883-1694-3078-a06d-ad24413f8b06`) to call [POST exports](../http-docs/http-sheets-exports-POST.md).

By default, both standard and feature markups (issues and photos) are exported along with the sheets. However, hyperlinks are not included in the default export. You need to specifically indicate if you want to export them.

In this example, we are exporting all types of markups, which includes published (public), unpublished (private), standard, and feature markups (issues and photos). However, note that only the hyperlinks tied to standard markups will be exported. Currently, we do not support the export of hyperlinks associated with feature markups.

For more information about markups, see the [Markups References Help Documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Markups_References).

Note that this endpoint is asynchronous and initiates a job that runs in the background rather than halting execution of your program. You can check whether the asynchronous job is complete by calling [GET exports/:export_id](https://aps.autodesk.com/en/docs/acc/v1/reference/http/sheets-getexportstatus-GET/).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/b.139532ee-5cdb-4c9e-a293-652693991e65/exports' \
  -X 'POST' \
  -H 'authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'content-type: application/json' \
  -d '{
      "options": {
        "outputFileName": "MyOutputFile",
        "standardMarkups": {
          "includePublishedMarkups": true,
          "includeUnpublishedMarkups": true,
          "includeMarkupLinks": true
        },
        "issueMarkups": {
          "includePublishedMarkups": true,
          "includeUnpublishedMarkups": true
        },
        "photoMarkups": {
          "includePublishedMarkups": true,
          "includeUnpublishedMarkups": true
        }
      },
      "sheets": [
        "0d7a5883-1694-3078-a06d-ad24413f8b06"
      ]
    }'

```

Show More

### Response

```
{
  "id":"225eb2fb-d5b0-44c9-a50a-2c792d833f2e",
  "status":"processing"
}

```

Note the export ID (`id` - `225eb2fb-d5b0-44c9-a50a-2c792d833f2e`). You use the export ID to verify the status of the export and to get a download link for the export.

## [Step 3: Verify the Status of the Export and Get a Download Link](#step-3-verify-the-status-of-the-export-and-get-a-download-link)

To verify the status of the export job, and to get a download link for the exported sheets, use the project ID (`b.139532ee-5cdb-4c9e-a293-652693991e65`) and the export ID (`225eb2fb-d5b0-44c9-a50a-2c792d833f2e`) to call [GET exports/:export_id](../http-docs/http-sheets-exports-exportId-GET.md).

When the status is `successful` the export is copmlete and a signed URL appears in the response, which you can use to download the sheets.

### Request

```
curl -X GET 'https://developer.api.autodesk.com/construction/sheets/v1/projects/b.139532ee-5cdb-4c9e-a293-652693991e65/exports/225eb2fb-d5b0-44c9-a50a-2c792d833f2e' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "225eb2fb-d5b0-44c9-a50a-2c792d833f2e",
  "status": "successful",
  "result": {
    "output": {
      "signedUrl": "https://accpes-p-ue1-storage.s3.amazonaws.com/{bucketId}/jobs/{jobId}/result.pdf?response-content-disposition={fileName}&AWSAccessKeyId={awsKey}&Signature={signature}&x-amz-security-token={token}&Expires={expire}"
    }
  }
}

```

Show More

Note the signed URL (`result.output.signedUrl`) that you can use for downloading the exported file directly from S3. The link is available for one hour. If you need to download the result after one hour, you need to recall `POST /projects/{projectId}/exports`.

## [Step 4: Download the Exported File](#step-4-download-the-exported-file)

To download the file from the signed URL, use a GET method and the URL attribute (`result.output.signedUrl`) as the URI.

Note that you should not use a bearer token with this call.

### Request

```
curl -X 'GET' -v 'https://accpes-p-ue1-storage.s3.amazonaws.com/{bucketId}/jobs/{jobId}/result.pdf?response-content-disposition={fileName}&AWSAccessKeyId={awsKey}&Signature={signature}&x-amz-security-token={token}&Expires={expire}'

```

### Response:

```
Status Code: 200 OK
Content-Type:application/pdf
Content-Length:90616

with chunked content body

```

Congratulations! You have exported sheets from ACC Build.
