# Querying Model Properties

Source: https://aps.autodesk.com/en/docs/acc/tutorials/model-properties/query/

---

# Querying Model Properties

The following step-by-step tutorial describes how to create a basic property index and run a simple query against this index.

## [Step 1: Specify the index](#step-1-specify-the-index)

To create a basic index, call the [batch status method](../http-docs/http-index-v2-index-jobs-batch-status-post.md), which allows you to check the status of one or more file version indexes. The batch status endpoint is lazy, meaning that if an indexing job for the file(s) specified in batch status check have not been executed, the service will automatically start the missing job(s). For the purposes of this tutorial, however, we will use the simple single file mode.

### Example Request

In the request below a `POST` is made to the [index batch status endpoint](../http-docs/http-index-v2-index-jobs-batch-status-post.md) passing in a single model file. There are no `query` or `columns` properties set in the payload so no query results will be generated in response to this operation.

```
curl --request POST 'https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes:batch-status' \
     --header 'Authorization: Bearer ****' \
     --header 'Content-Type: application/json' \
     --data-raw '{
        "versions": [
             {
                 "versionUrn": "urn:adsk.wipprod:fs.file:vf.DyTWutcvTcOLUNUARxcTzQ?version=4"
             }
         ]
     }'

```

Show More

### Example Response

The response to a batch status request is an array of status objects, one per file being indexed. The `indexId` on the status object is the unique identifier for this index and can be used in subsequent calls to check the progress of the indexing job and to later download the resources associated with the index. Calling the batch status endpoint multiple times will not result in multiple, duplicate indexes as long as the input parameters of the request do not change. Provided the array of objects in the `versions` set, `query`, and optionally `columns` properties passed to the endpoints remain unchanged, the caller will always be returned the same `indexId`.

In addition to the `indexId` the the status response object contains the status of the indexing job. Indexes once calculated are cached for 30 days on a rolling event horizon that is incremented every time the index is accessed. If an index is not accessed for 30 days it will fall out of the cache and will need to be subsequently recalculated. A status of `PROCESSING` indicates that the service is building the index. This could include waiting for SVF2 translation to complete. When the service has successfully created an index the status will be set to `FINISHED`. This indicates that the index and all its resources are available for download. The contract returned by the index service in response to an index status request also includes a suggested `retryAt` timestamp, which can be used to regulate status polling frequency.

```
[
    {
        "projectId": "f83cef12-deef-4771-9feb-4f85643e3c46",
        "indexId": "qTmPiKJZ7siqxkTNpWGANw",
        "type": "INDEX",
        "state": "PROCESSING",
        "selfUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw",
        "versionUrns": [
            "urn:adsk.wipprod:fs.file:vf.DyTWutcvTcOLUNUARxcTzQ?version=4"
        ],
        "updatedAt": "2021-08-19T08:21:13.8771187+00:00",
        "retryAt": "2021-08-27T14:28:28.8382067+00:00",
        "stats": null,
        "manifestUrl": null,
        "fieldsUrl": null,
        "propertiesUrl": null
    }
]

```

Show More

The properties returned by this endpoint are as follows:

| Property | Description |
| --- | --- |
| `projectId` | The project GUID |
| `indexId` | The unique ID for the index |
| `type` | The type of index INDEX (standard) or DIFF |
| `state` | The status of the indexing job (PROCESSING, FINISHED, FAILED) |
| `selfUrl` | The URL to this index job |
| `versionUrns` | The array of file version URNs passed to the indexing job |
| `updatedAt` | The date time the status of this job was last refreshed |
| `retryAt` | The suggested date time at which callers should poll for an updated status |
| `stats` | If the index state is FINISHED, the statistics for this index in terms of the number of objects |
| `manifestUrl` | If the index state is FINISHED, the URL to the manifest for this index, otherwise null |
| `fieldsUrl` | If the index state is FINISHED, the URL to the fields for this index, otherwise null |
| `propertiesUrl` | If the index state is FINISHED, the URL to the properties for this index, otherwise null |

## [Step 2: Poll for progress](#step-2-poll-for-progress)

To track the progress of an indexing request, send a `GET` request to the [index status endpoint](../http-docs/http-index-v2-index-status-get.md) using the `indexId` obtained in the batch status request. When the index has a status of `FINISHED` processing, the index is available for querying and download.

### Example Request

```
curl --request GET 'https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw' \
     --header 'Authorization: Bearer ****'

```

### Example Response

```
{
    "projectId": "f83cef12-deef-4771-9feb-4f85643e3c46",
    "indexId": "qTmPiKJZ7siqxkTNpWGANw",
    "type": "INDEX",
    "state": "FINISHED",
    "selfUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw",
    "versionUrns": [
        "urn:adsk.wipprod:fs.file:vf.DyTWutcvTcOLUNUARxcTzQ?version=4"
    ],
    "updatedAt": "2021-08-19T08:21:13.8771187+00:00",
    "retryAt": "2021-08-27T14:31:55.1444684+00:00",
    "stats": {
        "objects": 33097
    },
    "manifestUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/manifest",
    "fieldsUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/fields",
    "propertiesUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/properties"
}

```

Show More

When an index has been successfully created (`state` equals `FINISHED`), it contains three downloadable json.gz resources: a manifest describing the files and SVF2 database resources that were used to create the index, a list of fields (dimensions) in the index, and the index property data. Each of these resources has a URL that can be used to fetch the corresponding resource. The response JSON is identical to the response returned by the `POST` to the batch status endpoint (step 1 above).

## [Step 3: (Optional) Download the manifest](#step-3-optional-download-the-manifest)

To retrieve the index manifest make a `GET` to the [manifest endpoint](../http-docs/http-index-v2-index-manifest-get.md) as described in the [field guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/model-properties/)

### Example Request

```
curl --request GET 'https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/manifest' \
     --header 'Authorization: Bearer ****'

```

### Example Response

```
{
    "schema": "2.0.0",
    "projectId": "f83cef12-deef-4771-9feb-4f85643e3c46",
    "status": "Succeeded",
    "createdAt": "2021-07-23T08:56:07.0868303+00:00",
    "seedFiles": [
        {
            "lineageId": "a19f7db",
            "lineageUrn": "urn:adsk.wipprod:dm.lineage:DyTWutcvTcOLUNUARxcTzQ",
            "versionUrn": "urn:adsk.wipprod:fs.file:vf.DyTWutcvTcOLUNUARxcTzQ?version=4",
            "databases": [
                {
                    "id": "3747dccf",
                    "offsets": "urn:adsk.viewing:fs.file:dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLkR5VFd1dGN2VGNPTFVOVUFSeGNUelE_dmVyc2lvbj00/output/Resource/objects_offs.json.gz",
                    "attributes": "urn:adsk.viewing:fs.file:dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLkR5VFd1dGN2VGNPTFVOVUFSeGNUelE_dmVyc2lvbj00/output/Resource/objects_attrs.json.gz",
                    "values": "urn:adsk.viewing:fs.file:dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLkR5VFd1dGN2VGNPTFVOVUFSeGNUelE_dmVyc2lvbj00/output/Resource/objects_vals.json.gz",
                    "mapping": "urn:adsk.viewing:fs.file:dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLkR5VFd1dGN2VGNPTFVOVUFSeGNUelE_dmVyc2lvbj00/output/Resource/objects_avs.json.gz",
                    "ids": "urn:adsk.viewing:fs.file:dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLkR5VFd1dGN2VGNPTFVOVUFSeGNUelE_dmVyc2lvbj00/output/Resource/objects_ids.json.gz"
                }
            ],
            "views": [
                {
                    "id": "e7fda9d5",
                    "urn": "urn:adsk.wipprod:fs.file:vf.DyTWutcvTcOLUNUARxcTzQ?version=4",
                    "is3d": true,
                    "viewableName": "{3D}",
                    "viewableId": "0935d8b2-149b-4a0d-b816-863f0d595a20-000bcd64",
                    "viewableGuid": "00cd2da3-fbfa-44a9-7a33-cad0bc4720cb"
                },
                {
                    "id": "12fcb372",
                    "urn": "urn:adsk.wipprod:fs.file:vf.DyTWutcvTcOLUNUARxcTzQ?version=4",
                    "is3d": true,
                    "viewableName": "New Construction",
                    "viewableId": "c884ae1b-61e7-4f9d-0001-719e20b22d0b-00120bb2",
                    "viewableGuid": "4a966c2a-ead6-65c3-4f98-273dd7543047"
                }
            ]
        }
    ],
    "errors": [],
    "stats": {
        "objects": 33097,
        "contentLength": 1881318
    }
}

```

Show More

The structure of the manifest resource returned by this endpoint is described in the [field guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/model-properties/) page.

## [Step 4: (Optional) Download the fields](#step-4-optional-download-the-fields)

In order to query the index, [download the fields resource](../http-docs/http-index-v2-index-fields-get.md), which describes the columns available in the index. The index fields are obtained by a call to the `fieldsUrl` returned either by a call to the batch status endpoint (Step 1) or by polling the state of a running indexing job (Step 2). If you already know the field keys you require for your query you can skip this step.

### Example Request

```
curl --request GET 'https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/fields' \
     --header 'Authorization: Bearer ****'

```

### Example Response

```
{"key":"p153cb174","category":"__name__","type":"String","name":"name","uom":null}
{"key":"p74a9a490","category":"__document__","type":"String","name":"schema_name","uom":null}
{"key":"p137c14f2","category":"__document__","type":"String","name":"schema_version","uom":null}
{"key":"p1490bcea","category":"__document__","type":"Boolean","name":"is_doc_property","uom":null}
{"key":"p5eddc473","category":"__category__","type":"String","name":"Category","uom":null}
{"key":"p00723fa6","category":"Identity Data","type":"String","name":"Design Option","uom":null}
{"key":"pe8094f29","category":"Other","type":"String","name":"Project Issue Date","uom":null}
{"key":"p50756a0d","category":"Other","type":"String","name":"Client Name","uom":null}
{"key":"p32791eb0","category":"Other","type":"String","name":"Project Address","uom":null}
{"key":"pbf75ced9","category":"Other","type":"String","name":"Project Name","uom":null}
{"key":"p8213f1ad","category":"Other","type":"String","name":"Project Number","uom":null}
{"key":"pa7275c45","category":"__categoryId__","type":"Integer","name":"CategoryId","uom":null}
{"key":"p93e93af5","category":"__parent__","type":"DbKey","name":"parent","uom":null}
{"key":"pdf1348b1","category":"Constraints","type":"Double","name":"Elevation","uom":"ft"}
{"key":"p9513b772","category":"Constraints","type":"String","name":"Story Above","uom":null}
{"key":"p1d45bc4f","category":"Dimensions","type":"Double","name":"Computation Height","uom":"ft"}
{"key":"pe01bd7ef","category":"Extents","type":"String","name":"Scope Box","uom":null}
TRUNCATED

```

Show More

The structure of the fields resource returned by this endpoint is described in the [field guide](https://aps.autodesk.com/en/docs/acc/v1/tutorials/model-properties/overview/) page.

## [Step 5: (Optional) Download the raw index](#step-5-optional-download-the-raw-index)

While the indexing service is designed to run SQL-like queries targeting the fields contained within the indexes it hosts, it is possible to download raw indexes created by the service in their entirety. The raw index properties are obtained by a call to the `propertiesUrl` returned either by a call to the batch status endpoint (Step 1) or by polling the state of a running indexing job (Step 2).

### Example Request

```
curl --request GET 'https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/properties' \
     --header 'Authorization: Bearer ****'

```

### Example Response

```
{"svf2Id":1,"lineageId":"a19f7db","externalId":"doc_4c0302d4-8355-4bba-aa3e-02ea475a867c","lmvId":1,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p137c14f2":"1.0","p1490bcea":true,"p153cb174":"Model","p32791eb0":"Enter address here","p50756a0d":"AUDUBON OHIO","p5eddc473":"Revit Document","p74a9a490":"rvt","p8213f1ad":"1-06-444","pbf75ced9":"GRANGE INSURANCE AUDUBON CENTER","pe8094f29":"3-10-2008"},"propsHash":"16231084","views":[]}
{"svf2Id":2,"lineageId":"a19f7db","externalId":"b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f50a","lmvId":2,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p153cb174":"FOUNDATION PLAN","p1d45bc4f":0.0,"p5463fc28":false,"p5eddc473":"Revit Level","p5f2f196f":true,"p9513b772":"Default","pa7275c45":-2000240,"pdf1348b1":100.0,"pdf772b6f":"FOUNDATION PLAN","pe01bd7ef":"None"},"propsHash":"ca71d10d","propsIgnored":{"p93e93af5":1},"views":[]}
{"svf2Id":3,"lineageId":"a19f7db","externalId":"b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f50b","lmvId":3,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p153cb174":"BEARING","p1d45bc4f":0.0,"p5463fc28":false,"p5eddc473":"Revit Level","p5f2f196f":true,"p9513b772":"Default","pa7275c45":-2000240,"pdf1348b1":112.0,"pdf772b6f":"BEARING","pe01bd7ef":"None"},"propsHash":"4b5d70be","propsIgnored":{"p93e93af5":1},"views":[]}
{"svf2Id":4,"lineageId":"a19f7db","externalId":"b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f50c","lmvId":4,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p153cb174":"MEZZANINE","p1d45bc4f":0.0,"p5463fc28":false,"p5eddc473":"Revit Level","p5f2f196f":true,"p9513b772":"Default","pa7275c45":-2000240,"pdf1348b1":110.0,"pdf772b6f":"MEZZANINE","pe01bd7ef":"None"},"propsHash":"599fbb59","propsIgnored":{"p93e93af5":1},"views":[]}
{"svf2Id":5,"lineageId":"a19f7db","externalId":"0935d8b2-149b-4a0d-b816-863f0d595a20-000bcd64","lmvId":5,"databaseId":"3747dccf","props":{"p10c1a84a":false,"p114b1425":false,"p121ac73d":"Show Parts","p153cb174":"{3D}","p21b83ee9":1000.0,"p24044fbb":false,"p30015eee":"Medium","p31561b85":"None","p326e867f":99.66666666666666,"p345273d1":false,"p43766fd1":"96","p52413328":"By Discipline","p532f0ad6":"New Construction","p5eddc473":"Revit View","p79f5f88c":"Show All","p90dddb61":false,"p9ced1273":"{3D}","pa5fef29f":"all","pa7275c45":-2000279,"paea62326":"Adjusting","pb940b1a4":"Structural","pc2252206":"1/8\" = 1'-0\"","pd0d53a26":false,"pd45a2b8e":"Standard 3D Views","pe01bd7ef":"None","pe73257b1":"Independent","pf2c65ab9":271.2188634353403,"pfa32ecb1":"Orthographic","pfa463ea8":false},"propsHash":"64f41a52","propsIgnored":{"p93e93af5":1},"views":[]}
{"svf2Id":8,"lineageId":"a19f7db","externalId":"71cf8a75-c0d8-48db-b905-1eac3b6c8be7","lmvId":8,"databaseId":"3747dccf","props":{"p153cb174":"Phases","p20d8441e":"Phases","p5eddc473":"Revit Category"},"propsHash":"b9b0c2ee","propsIgnored":{"p93e93af5":1},"views":[]}
{"svf2Id":10,"lineageId":"a19f7db","externalId":"1513ee78-71c7-465f-9054-8ff932cfe1b9","lmvId":32,"databaseId":"3747dccf","props":{"p153cb174":"Materials","p20d8441e":"Materials","p5eddc473":"Revit Category"},"propsHash":"b1bec97b","propsIgnored":{"p93e93af5":1},"views":[]}
{"svf2Id":11,"lineageId":"a19f7db","externalId":"1d261fa6-2326-43bf-9ae8-b808ad2d3003","lmvId":320,"databaseId":"3747dccf","props":{"p153cb174":"Primary Contours","p20d8441e":"Primary Contours","p5eddc473":"Revit Category"},"propsHash":"6dbfc0eb","propsIgnored":{"p93e93af5":1},"views":[]}
{"svf2Id":12,"lineageId":"a19f7db","externalId":"31c7bc94-932d-411b-be66-433f5caf2c71","lmvId":529,"databaseId":"3747dccf","props":{"p153cb174":"Views","p20d8441e":"Views","p5eddc473":"Revit Category"},"propsHash":"d6fe53a3","propsIgnored":{"p93e93af5":1},"views":[]}
TRUNCATED

```

Show More

Index rows are returned as compressed (gzip) line-delimited JSON. The following is an example viewable index row, formatted as a single JSON document to make reading the property description table below easier.

```
{
    "svf2Id": 68,
    "lineageId": "a19f7db",
    "externalId": "b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f740",
    "lmvId": 2388,
    "databaseId": "3747dccf",
    "props": {
        "p00723fa6": "Main Model",
        "p09faf620": "HSS7X7X.250",
        "p0e507bbe": "None",
        "p13b6b3a0": "HSS7X7X.250",
        "p153cb174": "HSS-Hollow Structural Section-Column [259904]",
        "p188478f2": 0.485383241976329e0,
        "p20d8441e": "Structural Columns",
        "p2a0774a1": 0e0,
        "p30db51f9": "HSS-Hollow Structural Section-Column",
        "p34ed55db": "F-1.2",
        "p3c57b64e": "New Construction",
        "p54217060": "B10",
        "p5eddc473": "Revit Structural Columns",
        "p63ed81bb": "Superstructure",
        "p6637df3c": "Metal - Steel - ASTM A500 - Grade B - Rectangular and Square",
        "p69a0daab": 5833333333333334e-16,
        "p6aba1771": 0.01953125e0,
        "p751e1b21": true,
        "p773b5bd7": "Not Defined",
        "p801ffb64": 0.0390625e0,
        "p809920c7": "Square",
        "p953136d0": 0.04e0,
        "pa128dfb9": "Vertical",
        "pa57238c6": "Minimum Intersection",
        "pa7275c45": -2001330,
        "pa7456b2d": true,
        "pb5b8cef7": true,
        "pbadfe721": "BEARING",
        "pbb4f1bfe": "None",
        "pc2b858d6": 22.4e0,
        "pddd761c6": "FOUNDATION PLAN",
        "pe61a57c3": 0e0,
        "pee815a7f": "None",
        "pef87fde6": 0e0,
        "pf4ca60ab": 5833333333333334e-16,
        "pfa63d9d0": -9803431364364671e-16
    },
    "propsHash": "bcde34b3",
    "propsIgnored": {
        "p6a81eafd": 2386,
        "p93e93af5": 2387
    },
    "geomHash": "TCC2Cc9tvO4EVazM73O8BQ",
    "bboxMin": {
        "x": -1413565004170512e-13,
        "y": -5410244931321833e-14,
        "z": 10000000002097008e-14
    },
    "bboxMax": {
        "x": -14063352214982766e-14,
        "y": -53379471045994805e-15,
        "z": 11101965298365471e-14
    },
    "views": [
        "e7fda9d5",
        "12fcb372"
    ]
}

```

Show More

The structure of the properties resource returned by this endpoint is described in the [field guide](https://aps.autodesk.com/en/docs/acc/v1/tutorials/model-properties/overview/) page.

## [Step 6: Build and run a query](#step-6-build-and-run-a-query)

Once an index has been successfully created, it can be queried using the `queries` endpoint for the index via the `indexId` that can be obtained by a call to the index status tracking endpoints (Steps 1 or 2 above). Index queries are described using a custom JSON schema that is converted to a filter expression and applied line by line to the index. This documentation includes a [comprehensive query language reference](model-properties-query-ref.md) that describes how to form index and diff queries by example using this JSON schema.

### Example Request

The query schema targets the structure of the JSON index rows. In the example `POST` to the `queries` endpoint below, only rows that have a `views` array with a count greater than 0 will be returned, i.e. only the rows in the index that are associated with a model element that can be viewed in the Viewer.

```
curl --request POST 'https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/queries' \
     --header 'Authorization: Bearer ****' \
     --header 'Content-Type: application/json' \
     --data-raw '{
        "query": {
            "$gt": [{ "$count": "s.views" }, 0]
        }
     }'

```

Show More

### Example Response

The response from the `queries` endpoint is very similar to the response from the index status endpoints. The only additional property returned by this endpoint is a `queryId` value. This `queryId` is a unique identifier for the query execution and can be used to poll the progress of the query job. As with index status operations, a query is successful when its `state` is set to `FINISHED`. Index queries also have the standard `manifestUrl`, `fieldsUrl`, and `propertiesUrl` values that point to the index resources used when performing the query. In addition the `queries` endpoint also returns a `queryResultsUrl` property that points to a gzip’d, line delimited JSON resource that contains the filtered index rows that match the query filter expression when the query reaches the `FINISHED` state.

```
{
    "projectId": "f83cef12-deef-4771-9feb-4f85643e3c46",
    "indexId": "qTmPiKJZ7siqxkTNpWGANw",
    "queryId": "1uqaSYj39pOIaAuQutmZpg",
    "type": "INDEX",
    "state": "RUNNING",
    "selfUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/queries/1uqaSYj39pOIaAuQutmZpg",
    "versionUrns": [
        "urn:adsk.wipprod:fs.file:vf.DyTWutcvTcOLUNUARxcTzQ?version=4"
    ],
    "updatedAt": "2021-08-23T08:42:38.6922628+00:00",
    "retryAt": "2021-08-27T14:45:12.6504394+00:00",
    "stats": null,
    "manifestUrl": null,
    "fieldsUrl": null,
    "propertiesUrl": null,
    "queryResultsUrl": null
}

```

Show More

## [Step 7: Poll for query progress](#step-7-poll-for-query-progress)

The index `queries` endpoint follows the same pattern as the status endpoint. The `queryId` obtained in the `POST` to the `queries` endpoint can be used to poll the progress of the query.

### Example Request

In this example request the `queryId` and `indexId` from the previous Step (5) are used to poll the progress of the query.

```
curl --request GET 'https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/queries/1uqaSYj39pOIaAuQutmZpg' \
     --header 'Authorization: Bearer ****'

```

### Example Response

The response to this status `GET` is identical to the response returned by the `POST` to the `queries` endpoint. In the example below the query `state` is set to `FINISHED` and the `queryResultsUrl` is not null, indicating that the query has been completed successfully and the results are available for download.

```
{
    "projectId": "f83cef12-deef-4771-9feb-4f85643e3c46",
    "indexId": "qTmPiKJZ7siqxkTNpWGANw",
    "queryId": "1uqaSYj39pOIaAuQutmZpg",
    "type": "INDEX",
    "state": "FINISHED",
    "selfUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/queries/1uqaSYj39pOIaAuQutmZpg",
    "versionUrns": [
        "urn:adsk.wipprod:fs.file:vf.DyTWutcvTcOLUNUARxcTzQ?version=4"
    ],
    "updatedAt": "2021-08-23T08:42:38.6922628+00:00",
    "retryAt": "2021-08-27T14:47:59.2677745+00:00",
    "stats": {
        "objects": 6523
    },
    "manifestUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/manifest",
    "fieldsUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/fields",
    "propertiesUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/properties",
    "queryResultsUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/queries/1uqaSYj39pOIaAuQutmZpg/properties"
}

```

Show More

## [Step 8: Download the query results](#step-8-download-the-query-results)

The final step in the process is to use the `queryResultsUrl` to download the index rows which match the submitted query expression. These line delimited JSON result rows are a sub-set of the property index rows and have exactly the same format.

### Example Request

```
curl --request GET 'https://developer.api.autodesk.com/construction/index/v2/projects/f83cef12-deef-4771-9feb-4f85643e3c46/indexes/qTmPiKJZ7siqxkTNpWGANw/queries/1uqaSYj39pOIaAuQutmZpg/properties' \
     --header 'Authorization: Bearer ****'

```

### Example Response

```
{"svf2Id":68,"lineageId":"a19f7db","externalId":"b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f740","lmvId":2388,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p09faf620":"HSS7X7X.250","p0e507bbe":"None","p13b6b3a0":"HSS7X7X.250","p153cb174":"HSS-Hollow Structural Section-Column [259904]","p188478f2":0.485383241976329e0,"p20d8441e":"Structural Columns","p2a0774a1":0e0,"p30db51f9":"HSS-Hollow Structural Section-Column","p34ed55db":"F-1.2","p3c57b64e":"New Construction","p54217060":"B10","p5eddc473":"Revit Structural Columns","p63ed81bb":"Superstructure","p6637df3c":"Metal - Steel - ASTM A500 - Grade B - Rectangular and Square","p69a0daab":5833333333333334e-16,"p6aba1771":0.01953125e0,"p751e1b21":true,"p773b5bd7":"Not Defined","p801ffb64":0.0390625e0,"p809920c7":"Square","p953136d0":0.04e0,"pa128dfb9":"Vertical","pa57238c6":"Minimum Intersection","pa7275c45":-2001330,"pa7456b2d":true,"pb5b8cef7":true,"pbadfe721":"BEARING","pbb4f1bfe":"None","pc2b858d6":22.4e0,"pddd761c6":"FOUNDATION PLAN","pe61a57c3":0e0,"pee815a7f":"None","pef87fde6":0e0,"pf4ca60ab":5833333333333334e-16,"pfa63d9d0":-9803431364364671e-16},"propsHash":"bcde34b3","propsIgnored":{"p6a81eafd":2386,"p93e93af5":2387},"geomHash":"TCC2Cc9tvO4EVazM73O8BQ","bbox":{"min":[-1413565004170512e-13,-5410244931321833e-14,10000000002097008e-14],"max":[-14063352214982766e-14,-53379471045994805e-15,11101965298365471e-14]},"views":["e7fda9d5","12fcb372"]}
{"svf2Id":69,"lineageId":"a19f7db","externalId":"b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f742","lmvId":2389,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p09faf620":"HSS7X7X.250","p0e507bbe":"None","p13b6b3a0":"HSS7X7X.250","p153cb174":"HSS-Hollow Structural Section-Column [259906]","p188478f2":5285644531249998e-16,"p20d8441e":"Structural Columns","p30db51f9":"HSS-Hollow Structural Section-Column","p34ed55db":"F-3","p3c57b64e":"New Construction","p54217060":"B10","p5eddc473":"Revit Structural Columns","p63ed81bb":"Superstructure","p6637df3c":"Metal - Steel - ASTM A500 - Grade B - Rectangular and Square","p69a0daab":5833333333333334e-16,"p6aba1771":0.01953125e0,"p773b5bd7":"Not Defined","p801ffb64":0.0390625e0,"p809920c7":"Square","p953136d0":0.04e0,"pa128dfb9":"Vertical","pa7275c45":-2001330,"pa7456b2d":true,"pb5b8cef7":true,"pbadfe721":"BEARING","pbb4f1bfe":"None","pc2b858d6":22.4e0,"pddd761c6":"FOUNDATION PLAN","pe61a57c3":0e0,"pee815a7f":"None","pef87fde6":0e0,"pf4ca60ab":5833333333333334e-16,"pfa63d9d0":0e0},"propsHash":"6f21f5ef","propsIgnored":{"p6a81eafd":2386,"p93e93af5":2387},"geomHash":"Yjh1a5R5k7OIuzFlup7U/A","bbox":{"min":[-11740090260815661e-14,-6244930357652374e-14,10000000002097008e-14],"max":[-11667791541749409e-14,-6172631768493561e-14,11199999966334221e-14]},"views":["e7fda9d5","12fcb372"]}
{"svf2Id":70,"lineageId":"a19f7db","externalId":"b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f743","lmvId":2392,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p09faf620":"HSS6X6X.1875","p0e507bbe":"None","p13b6b3a0":"HSS6X6X.1875","p153cb174":"HSS-Hollow Structural Section-Column [259907]","p188478f2":5622698018705423e-16,"p20d8441e":"Structural Columns","p30db51f9":"HSS-Hollow Structural Section-Column","p34ed55db":"A-7","p3c57b64e":"New Construction","p54217060":"B10","p5eddc473":"Revit Structural Columns","p63ed81bb":"Superstructure","p6637df3c":"Metal - Steel - ASTM A500 - Grade B - Rectangular and Square","p69a0daab":0.5e0,"p6aba1771":0.0146484375e0,"p773b5bd7":"Not Defined","p801ffb64":0.029296875e0,"p809920c7":"Square","p953136d0":0.03e0,"pa128dfb9":"Vertical","pa7275c45":-2001330,"pa7456b2d":true,"pb5b8cef7":true,"pbadfe721":"BEARING","pbb4f1bfe":"None","pc2b858d6":14.5e0,"pddd761c6":"FOUNDATION PLAN","pe61a57c3":0e0,"pee815a7f":"None","pef87fde6":0e0,"pf4ca60ab":0.5e0,"pfa63d9d0":7771382285923252e-15},"propsHash":"ca9845fe","propsIgnored":{"p6a81eafd":2390,"p93e93af5":2391},"geomHash":"KzBnTTzXjGBfEq4yR8VtzA","bbox":{"min":[-4067314124452854e-14,7.05652589540108e0,10000000002097008e-14],"max":[-40025658785271645e-15,7704008354657972e-15,1197713848562133e-13]},"views":["e7fda9d5","12fcb372"]}
{"svf2Id":71,"lineageId":"a19f7db","externalId":"b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f744","lmvId":2393,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p09faf620":"HSS6X6X.1875","p0e507bbe":"None","p13b6b3a0":"HSS6X6X.1875","p153cb174":"HSS-Hollow Structural Section-Column [259908]","p188478f2":5260619140289455e-16,"p20d8441e":"Structural Columns","p2a0774a1":0e0,"p30db51f9":"HSS-Hollow Structural Section-Column","p34ed55db":"A-8","p3c57b64e":"New Construction","p54217060":"B10","p5eddc473":"Revit Structural Columns","p63ed81bb":"Superstructure","p6637df3c":"Metal - Steel - ASTM A500 - Grade B - Rectangular and Square","p69a0daab":0.5e0,"p6aba1771":0.0146484375e0,"p751e1b21":true,"p773b5bd7":"Not Defined","p801ffb64":0.029296875e0,"p809920c7":"Square","p953136d0":0.03e0,"pa128dfb9":"Vertical","pa57238c6":"Minimum Intersection","pa7275c45":-2001330,"pa7456b2d":true,"pb5b8cef7":true,"pbadfe721":"BEARING","pbb4f1bfe":"None","pc2b858d6":14.5e0,"pddd761c6":"FOUNDATION PLAN","pe61a57c3":0e0,"pee815a7f":"None","pef87fde6":0e0,"pf4ca60ab":0.5e0,"pfa63d9d0":6498185699693238e-15},"propsHash":"d295b8c2","propsIgnored":{"p6a81eafd":2390,"p93e93af5":2391},"geomHash":"sKxntR3859ILOVn7pKKhIQ","bbox":{"min":[-23.9879046768966e0,12428865208033102e-16,10000000002097008e-14],"max":[-2334041855459337e-14,18903700449577627e-16,11849818386744377e-14]},"views":["e7fda9d5","12fcb372"]}
{"svf2Id":72,"lineageId":"a19f7db","externalId":"b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f748","lmvId":2396,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p09faf620":"HSS4X4X.1875","p0e507bbe":"None","p13b6b3a0":"HSS4X4X.1875","p153cb174":"HSS-Hollow Structural Section-Column [259912]","p188478f2":26921418830460175e-17,"p20d8441e":"Structural Columns","p30db51f9":"HSS-Hollow Structural Section-Column","p34ed55db":"F-13.8","p3c57b64e":"New Construction","p54217060":"B10","p5eddc473":"Revit Structural Columns","p63ed81bb":"Superstructure","p6637df3c":"Metal - Steel - ASTM A500 - Grade B - Rectangular and Square","p69a0daab":3333333333333333e-16,"p6aba1771":0.0146484375e0,"p773b5bd7":"Not Defined","p801ffb64":0.029296875e0,"p809920c7":"Square","p953136d0":0.02e0,"pa128dfb9":"Vertical","pa7275c45":-2001330,"pa7456b2d":true,"pb5b8cef7":true,"pbadfe721":"BEARING","pbb4f1bfe":"None","pc2b858d6":9.4e0,"pddd761c6":"FOUNDATION PLAN","pe61a57c3":0e0,"pee815a7f":"None","pef87fde6":0e0,"pf4ca60ab":3333333333333333e-16,"pfa63d9d0":2417340996715339e-15},"propsHash":"8b568853","propsIgnored":{"p6a81eafd":2394,"p93e93af5":2395},"geomHash":"cAWPEx2yBSeJGrInzF1/aw","bbox":{"min":[-5372055725666179e-15,-10128624040894114e-14,10000000002097008e-14],"max":[-4941667181569901e-15,-10085585121530767e-14,11441734280299065e-14]},"views":["e7fda9d5","12fcb372"]}
{"svf2Id":73,"lineageId":"a19f7db","externalId":"b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f749","lmvId":2397,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p09faf620":"HSS6X6X.1875","p0e507bbe":"None","p13b6b3a0":"HSS6X6X.1875","p153cb174":"HSS-Hollow Structural Section-Column [259913]","p188478f2":4100085339756494e-16,"p20d8441e":"Structural Columns","p30db51f9":"HSS-Hollow Structural Section-Column","p34ed55db":"F-12","p3c57b64e":"New Construction","p54217060":"B10","p5eddc473":"Revit Structural Columns","p63ed81bb":"Superstructure","p6637df3c":"Metal - Steel - ASTM A500 - Grade B - Rectangular and Square","p69a0daab":0.5e0,"p6aba1771":0.0146484375e0,"p773b5bd7":"Not Defined","p801ffb64":0.029296875e0,"p809920c7":"Square","p953136d0":0.03e0,"pa128dfb9":"Vertical","pa7275c45":-2001330,"pa7456b2d":true,"pb5b8cef7":true,"pbadfe721":"BEARING","pbb4f1bfe":"None","pc2b858d6":14.5e0,"pddd761c6":"FOUNDATION PLAN","pe61a57c3":0e0,"pee815a7f":"None","pef87fde6":0e0,"pf4ca60ab":0.5e0,"pfa63d9d0":24173409967153106e-16},"propsHash":"5c430fc7","propsIgnored":{"p6a81eafd":2390,"p93e93af5":2391},"geomHash":"Ef2OUDgFZDndJH9a648+6w","bbox":{"min":[-2751472931099257e-14,-9371743688325377e-14,10000000002097008e-14],"max":[-2686724540352532e-14,-9306995232624932e-14,11441734280299065e-14]},"views":["e7fda9d5","12fcb372"]}
{"svf2Id":74,"lineageId":"a19f7db","externalId":"b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f74a","lmvId":2398,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p09faf620":"HSS6X6X.1875","p0e507bbe":"None","p13b6b3a0":"HSS6X6X.1875","p153cb174":"HSS-Hollow Structural Section-Column [259914]","p188478f2":4135579583143538e-16,"p20d8441e":"Structural Columns","p30db51f9":"HSS-Hollow Structural Section-Column","p34ed55db":"E-3","p3c57b64e":"New Construction","p54217060":"B10","p5eddc473":"Revit Structural Columns","p63ed81bb":"Superstructure","p6637df3c":"Metal - Steel - ASTM A500 - Grade B - Rectangular and Square","p69a0daab":0.5e0,"p6aba1771":0.0146484375e0,"p773b5bd7":"Not Defined","p801ffb64":0.029296875e0,"p809920c7":"Square","p953136d0":0.03e0,"pa128dfb9":"Vertical","pa7275c45":-2001330,"pa7456b2d":true,"pb5b8cef7":true,"pbadfe721":"BEARING","pbb4f1bfe":"None","pc2b858d6":14.5e0,"pddd761c6":"FOUNDATION PLAN","pe61a57c3":0e0,"pee815a7f":"None","pef87fde6":0e0,"pf4ca60ab":0.5e0,"pfa63d9d0":25421512306314895e-16},"propsHash":"fcb8d37a","propsIgnored":{"p6a81eafd":2390,"p93e93af5":2391},"geomHash":"aUZjfH/wOI8ffqpcAzQcxw","bbox":{"min":[-11164540474581231e-14,-4277749229053744e-14,10000000002097008e-14],"max":[-11102570368482772e-14,-4215779122955284e-14,11454215206812736e-14]},"views":["e7fda9d5","12fcb372"]}
{"svf2Id":75,"lineageId":"a19f7db","externalId":"b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f74b","lmvId":2399,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p09faf620":"HSS6X6X.1875","p0e507bbe":"None","p13b6b3a0":"HSS6X6X.1875","p153cb174":"HSS-Hollow Structural Section-Column [259915]","p188478f2":41000853397562853e-17,"p20d8441e":"Structural Columns","p30db51f9":"HSS-Hollow Structural Section-Column","p34ed55db":"F-9","p3c57b64e":"New Construction","p54217060":"B10","p5eddc473":"Revit Structural Columns","p63ed81bb":"Superstructure","p6637df3c":"Metal - Steel - ASTM A500 - Grade B - Rectangular and Square","p69a0daab":0.5e0,"p6aba1771":0.0146484375e0,"p773b5bd7":"Not Defined","p801ffb64":0.029296875e0,"p809920c7":"Square","p953136d0":0.03e0,"pa128dfb9":"Vertical","pa7275c45":-2001330,"pa7456b2d":true,"pb5b8cef7":true,"pbadfe721":"BEARING","pbb4f1bfe":"None","pc2b858d6":14.5e0,"pddd761c6":"FOUNDATION PLAN","pe61a57c3":0e0,"pee815a7f":"None","pef87fde6":0e0,"pf4ca60ab":0.5e0,"pfa63d9d0":24173409967152963e-16},"propsHash":"81b2febb","propsIgnored":{"p6a81eafd":2390,"p93e93af5":2391},"geomHash":"5aq5RLee7AB70heqgw2t9g","bbox":{"min":[-5065056277327119e-14,-8565621912069254e-14,10000000002097008e-14],"max":[-50.0030803140143e0,-8500873666143565e-14,11441734280299065e-14]},"views":["e7fda9d5","12fcb372"]}
{"svf2Id":76,"lineageId":"a19f7db","externalId":"b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f74c","lmvId":2400,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p09faf620":"HSS6X6X.1875","p0e507bbe":"None","p13b6b3a0":"HSS6X6X.1875","p153cb174":"HSS-Hollow Structural Section-Column [259916]","p188478f2":0.410008533679623e0,"p20d8441e":"Structural Columns","p30db51f9":"HSS-Hollow Structural Section-Column","p34ed55db":"F-6","p3c57b64e":"New Construction","p54217060":"B10","p5eddc473":"Revit Structural Columns","p63ed81bb":"Superstructure","p6637df3c":"Metal - Steel - ASTM A500 - Grade B - Rectangular and Square","p69a0daab":0.5e0,"p6aba1771":0.0146484375e0,"p773b5bd7":"Not Defined","p801ffb64":0.029296875e0,"p809920c7":"Square","p953136d0":0.03e0,"pa128dfb9":"Vertical","pa7275c45":-2001330,"pa7456b2d":true,"pb5b8cef7":true,"pbadfe721":"BEARING","pbb4f1bfe":"None","pc2b858d6":14.5e0,"pddd761c6":"FOUNDATION PLAN","pe61a57c3":0e0,"pee815a7f":"None","pef87fde6":0e0,"pf4ca60ab":0.5e0,"pfa63d9d0":2417340986305419e-15},"propsHash":"2e8116ef","propsIgnored":{"p6a81eafd":2390,"p93e93af5":2391},"geomHash":"yR0kW3rbrpd8Lqpxsvx8Ng","bbox":{"min":[-7378639425489068e-14,-7759499822753376e-14,10000000002097008e-14],"max":[-7313891179563379e-14,-7694751576827687e-14,11441734280299065e-14]},"views":["e7fda9d5","12fcb372"]}
{"svf2Id":77,"lineageId":"a19f7db","externalId":"b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f750","lmvId":2401,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p09faf620":"HSS6X6X.1875","p0e507bbe":"None","p13b6b3a0":"HSS6X6X.1875","p153cb174":"HSS-Hollow Structural Section-Column [259920]","p188478f2":0.413755448370708e0,"p20d8441e":"Structural Columns","p30db51f9":"HSS-Hollow Structural Section-Column","p34ed55db":"E-1","p3c57b64e":"New Construction","p54217060":"B10","p5eddc473":"Revit Structural Columns","p63ed81bb":"Superstructure","p6637df3c":"Metal - Steel - ASTM A500 - Grade B - Rectangular and Square","p69a0daab":0.5e0,"p6aba1771":0.0146484375e0,"p773b5bd7":"Not Defined","p801ffb64":0.029296875e0,"p809920c7":"Square","p953136d0":0.03e0,"pa128dfb9":"Vertical","pa7275c45":-2001330,"pa7456b2d":true,"pb5b8cef7":true,"pbadfe721":"BEARING","pbb4f1bfe":"None","pc2b858d6":14.5e0,"pddd761c6":"FOUNDATION PLAN","pe61a57c3":0e0,"pee815a7f":"None","pef87fde6":0e0,"pf4ca60ab":0.5e0,"pfa63d9d0":25490956750758897e-16},"propsHash":"bc834fe3","propsIgnored":{"p6a81eafd":2390,"p93e93af5":2391},"geomHash":"m1uJ9gbzWIwZ0Y/RHTL3ww","bbox":{"min":[-13827222772628218e-14,-3503671150408979e-14,10000000002097008e-14],"max":[-1376525266652976e-13,-34417010443105184e-15,1145490948171508e-13]},"views":["e7fda9d5","12fcb372"]}
{"svf2Id":78,"lineageId":"a19f7db","externalId":"b5c4b31f-321a-418d-a61a-0c8e326aa154-0003f751","lmvId":2402,"databaseId":"3747dccf","props":{"p00723fa6":"Main Model","p09faf620":"HSS6X6X.1875","p0e507bbe":"None","p13b6b3a0":"HSS6X6X.1875","p153cb174":"HSS-Hollow Structural Section-Column [259921]","p188478f2":34126281738281244e-17,"p20d8441e":"Structural Columns","p30db51f9":"HSS-Hollow Structural Section-Column","p34ed55db":"B-10","p3c57b64e":"New Construction","p54217060":"B10","p5eddc473":"Revit Structural Columns","p63ed81bb":"Superstructure","p6637df3c":"Metal - Steel - ASTM A500 - Grade B - Rectangular and Square","p69a0daab":0.5e0,"p6aba1771":0.0146484375e0,"p773b5bd7":"Not Defined","p801ffb64":0.029296875e0,"p809920c7":"Square","p953136d0":0.03e0,"pa128dfb9":"Vertical","pa7275c45":-2001330,"pa7456b2d":true,"pb5b8cef7":true,"pbadfe721":"BEARING","pbb4f1bfe":"None","pc2b858d6":14.5e0,"pddd761c6":"FOUNDATION PLAN","pe61a57c3":0e0,"pee815a7f":"None","pef87fde6":0e0,"pf4ca60ab":0.5e0,"pfa63d9d0":0e0},"propsHash":"4d9b58db","propsIgnored":{"p6a81eafd":2390,"p93e93af5":2391},"geomHash":"N427c0D7TagBJXgRhaOOng","bbox":{"min":[-23171833458388303e-15,-2024642145398657e-14,10000000002097008e-14],"max":[-22.5521323974037e0,-19626720393001968e-15,11199999966334221e-14]},"views":["e7fda9d5","12fcb372"]}
TRUNCATED

```

Show More
