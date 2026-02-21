# Download a Document Generated From an SCO (new)

Source: https://aps.autodesk.com/en/docs/acc/tutorials/cost/download-cost-document-s3/

---

# Download a Document Generated From an SCO (new)

This tutorial demonstrates how to download a generated SCO (*Supplier Change Order*) document from BIM 360 Cost Management. The steps here include finding the URN from the generated document, locating the storage object for the file, and downloading the file from the storage object.

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps).
- Acquire a [3-legged OAuth token](/en/docs/oauth/v2/tutorials/get-3-legged-token/) with `data:create` `data:read` and `data:write` scopes.
- Verify that you have access to the relevant BIM 360 account and BIM 360 project.
- Retrieve the project ID for your project. To obtain a project ID, use [GET projects](/en/docs/bim360/v1/reference/http/admin-accounts-accountidprojects-GET/).
- Verify that you have an SCO and that a document has been generated for it.

## [Step 1: Find an SCO in BIM 360 Cost Management](#step-1-find-an-sco-in-bim-360-cost-management)

Use the [GET SCO](/en/docs/bim360/v1/reference/http/cost-change-orders-changeOrder-GET/) endpoint to find the ID of the SCO from which you want to download.

In this example, the SCO has a generated document. Assume that the container ID is `18ece8b1-204d-11e8-ad71-d73b169f902a`.

### Request

```
curl -X GET 'https://developer.api.autodesk.com/cost/v1/containers/18ece8b1-204d-11e8-ad71-d73b169f902a/change-orders/sco?limit=100&offset=0' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0'

```

### Response

```
{
  "results": [{
      "id": "55254a50-44d9-11e9-99d7-79aa05d3109e",
      "...":"...",
  }],
  "pagination": {
      "totalResults": 1,
      "limit": 100,
      "offset": 0
  }
}

```

Show More

The response payload includes the SCO ID (`results[0].id`) with a value of `55254a50-44d9-11e9-99d7-79aa05d3109e`. Youâll use it in the next step.

## [Step 2: Find the Document Generated for the SCO](#step-2-find-the-document-generated-for-the-sco)

Use the [GET cost/v1/containers/{containerId}/documents](/en/docs/bim360/v1/reference/http/cost-documents-GET/) endpoint to retrieve the generated document. The `associationId` value is the SCO ID `55254a50-44d9-11e9-99d7-79aa05d3109e`. The `associationType` value is `FormInstance`.

### Request

```
curl -X GET 'https://developer.api.autodesk.com/cost/v1/containers/18ece8b1-204d-11e8-ad71-d73b169f902a/documents?associationId=55254a50-44d9-11e9-99d7-79aa05d3109e&associationType=FormInstance' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0' \
-H 'Content-Type: application/json'

```

### Response

```
{
  "id": "80b446f0-4261-11e9-9f1f-e19f7c813519",
  "urn": "urn:adsk.wipprod:fs.file:vf.kYtkYWBsSKSCMXYzEYe80w?version=1",
  "...": "..."
}

```

The `urn` value in the response (`urn:adsk.wipprod:fs.file:vf.kYtkYWBsSKSCMXYzEYe80w?version=1`) is the version URN you use to access the data management service in the next step.

## [Step 3: Find the Storage Object ID](#step-3-find-the-storage-object-id)

Use Mozillaâs [encodeURIComponent](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) operation to encode the object ID `urn:adsk.wipprod:fs.file:vf.kYtkYWBsSKSCMXYzEYe80w?version=1` as `urn%3Aadsk.wipprod%3Afs.file%3Avf.kYtkYWBsSKSCMXYzEYe80w%3Fversion%3D1`.

Next, use the encoded ID as the version ID to call the Data Management APIâs [GET projects/:project_id/versions/:version_id](/en/docs/data/v2/reference/http/projects-project_id-versions-version_id-GET/).

### Request

```
curl -X GET 'https://developer.api.autodesk.com/data/v1/projects/b.e8d3c2a0-b913-11e9-893e-e55449557ed8/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.kYtkYWBsSKSCMXYzEYe80w%3Fversion%3D1' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0' \
-H 'Content-Type: application/json'

```

### Response

```
{
    "jsonapi": {
        "version": "1.0"
    },
    "links": {
        "...": "..."
    },
    "data": {
        "type": "versions",
        "id": "urn:adsk.wipprod:fs.file:vf.kYtkYWBsSKSCMXYzEYe80w?version=1",
        "attributes": {
            "...": "..."
        },
        "links": {
            "...": "..."
        },
        "relationships": {
            "item": {
                "...": "..."
            },
            "links": {
                "...": "..."
            },
            "refs": {
                "...": "..."
            },
            "downloadFormats": {
                "...": "..."
            },
            "derivatives": {
                "...": "..."
            },
            "thumbnails": {
                "...": "..."
            },
            "storage": {
                "data": {
                    "type": "objects",
                    "id": "urn:adsk.objects:os.object:wip.dm.prod/af47b92e-7096-4c1f-b090-f77b1d83485f.docx"
                },
                "meta": {
                    "link": {
                        "href": "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/af47b92e-7096-4c1f-b090-f77b1d83485f.docx?scopes=b360project.6b975448-835b-4625-ad1a-0e9961749de3,global,O2tenant.3751451"
                    }
                }
            }
        }
    }
}

```

Show More

The response contains the storage objectâs ID in `data.relationships.storage.data.id`, with a value of `urn:adsk.objects:os.object:wip.dm.prod/af47b92e-7096-4c1f-b090-f77b1d83485f.docx`. The object ID parses into three sections:

- `urn:adsk.objects:os.object`
- `wip.dm.prod` (the bucket key)
- `af47b92e-7096-4c1f-b090-f77b1d83485f.docx` (the object name)

Youâll use this ID to access the storage service in the next step.

## [Step 4: Generate a Signed S3 URL](#step-4-generate-a-signed-s3-url)

Use the Data Management APIâs [GET buckets/:bucketKey/objects/:objectKey/signeds3download](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3download-GET/) endpoint to generate a signed URL for the storage object, which you can use to download the file directly from S3. Include the bucket key (`wip.dm.prod`) and the object name (`af47b92e-7096-4c1f-b090-f77b1d83485f.docx`) that you retrieved in the previous step.

### Request

```
curl -X GET "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/af47b92e-7096-4c1f-b090-f77b1d83485f.docx/signeds3download" \
-H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT"

```

### Response

```
{
  "status": "complete",
  "url": "https://cdn.us.oss.api.autodesk.com/com.autodesk.oss-persistent/us-east-1/3f/bf/5f/0137a7d9dc53af930bc1b527320d50fb5f/wip.dm.prod?response-content-type=application%2Foctet-stream&response-content-disposition=attachment%3B+filename%3D%af47b92e-7096-4c1f-b090-f77b1d83485f.docx%22&Expires=1643864703&Signature=00PZYS6gL~Nc6aRG2HAhOCKYl0xtqsuujMJ~VKSXm1vBa-OxS4lPQBSlTx5bswpLBe1W6Rz94eIZW2sPN-v6Mzz~JyXNZ-V9Z7zlBoE1VoQhspLioC225hxq6ZmDSU5QnZXuNDV4ih~p1n3xacYvUvQWX-ONAGVUgQvZ253Svw~qx-pO4j-Yh4kVRmzDZqQut1xOI5ZGH6JFGhXLSzkgbYcfYx6fvCxnvYUJrgAcqncIwGVewI3uC0I84Fzrj8nXE8ojuojqJP0pNlxkfBe~2LfjjzqKDKaNvfC2Grt12j9QgC~cN7nQCRcVUhExpoV1VVB5x3AkVTJ-q5NoedvsfO__&Key-Pair-Id=95HRZD7MMO1UK",
  "params": {
    "content-type": "application/octet-stream",
    "content-disposition": "attachment; filename=\"af47b92e-7096-4c1f-b090-f77b1d83485f.docx\""
  },
  "size": 472424,
  "sha1": "ffbf5f0137a7d9dc53af930bc1b527320d50fb53"
}

```

Show More

Note the `url` response attribute, which contains the signed URL youâll use in the following step.

## [Step 5: Download the File](#step-5-download-the-file)

To download the file from the signed URL, use a GET method and the previously returned `url` attribute as the URI.

Note that a bearer token is not required.

### Request

```
curl -X GET "https://cdn.us.oss.api.autodesk.com/com.autodesk.oss-persistent/us-east-1/3f/bf/5f/0137a7d9dc53af930bc1b527320d50fb5f/wip.dm.prod?response-content-type=application%2Foctet-stream&response-content-disposition=attachment%3B+filename%3D%af47b92e-7096-4c1f-b090-f77b1d83485f.docx%22&Expires=1643864703&Signature=00PZYS6gL~Nc6aRG2HAhOCKYl0xtqsuujMJ~VKSXm1vBa-OxS4lPQBSlTx5bswpLBe1W6Rz94eIZW2sPN-v6Mzz~JyXNZ-V9Z7zlBoE1VoQhspLioC225hxq6ZmDSU5QnZXuNDV4ih~p1n3xacYvUvQWX-ONAGVUgQvZ253Svw~qx-pO4j-Yh4kVRmzDZqQut1xOI5ZGH6JFGhXLSzkgbYcfYx6fvCxnvYUJrgAcqncIwGVewI3uC0I84Fzrj8nXE8ojuojqJP0pNlxkfBe~2LfjjzqKDKaNvfC2Grt12j9QgC~cN7nQCRcVUhExpoV1VVB5x3AkVTJ-q5NoedvsfO__&Key-Pair-Id=95HRZD7MMO1UK" \
--output "55254a50-44d9-11e9-99d7-79aa05d3109e.docx"

```

Congratulations! You have downloaded the generated document from BIM 360 Cost Management. You can use it in different ways that include printing it out or sending it to an e-signature provider for signatures.
