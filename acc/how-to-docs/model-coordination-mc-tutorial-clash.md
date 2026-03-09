# Model Set Version Clash

Source: https://aps.autodesk.com/en/docs/acc/tutorials/model-coordination/mc-tutorial-clash/

---

# Model Set Version Clash

This tutorial demonstrates how to work with the results of the automated clash testing that the BIM 360 Model Coordination clash service performs whenever a new [model set version](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/model-coordination/mcfg-model-set/) is created. New model set versions are typically created by users uploading new versions of model files to folders that have been configured as model sets by model coordination administrators. The results of clash testing are a set of compressed, versioned, JSON files. You need to download these files locally before you can interpret them. The API provides endpoints to discover and download these result files.

## [Before You Begin](#before-you-begin)

Make sure that you have [registered an app](../../oauth/how-to-docs/create-app.md). and successfully [acquired an OAuth token](https://aps.autodesk.com/en/docs/oauth/v2/tutorials/http/get-2-legged-token/) with the `data:read`, `data:write` and `data:create` scopes.

You also need a configured a`BIM 360 Model Coordination space <<https://help.autodesk.com/view/BIM360D/ENU/?guid=GUID-8B8DB128-F95B-461D-B265-468481208944>>`_ with some uploaded models, and must ensure that the clash process has completed successfully.

## [Step 1: Get the latest Model Set Version](#step-1-get-the-latest-model-set-version)

Before working with model set clash data, you need to decide which set version you want to use. [GET modelsets/:modelSetId/versions/latest](../http-docs/http-mc-modelset-service-v3-get-model-set-version-latest-GET.md) allows you to obtain the latest model set version for the model set. You can use this endpoint to obtain a model set version number that you can use in conjunction with the clash endpoints to interrogate the results of clash testing.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/e6efd20e-f971-4705-aae0-1e5faa2eec11/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911/versions/latest' \
   -H 'Authorization: Bearer <token>'

```

### Example Response

```
{
    "modelSetId": "00fb28a5-e8a4-2755-562a-7c2f0fc87911",
    "version": 42,
    "createTime": "2015-10-21T16:29:30.0000000+00:00",
    "status": "Successful",
    "documentVersions": [
        {
          "documentLineage": {
              "lineageUrn": "urn:adsk.wipprod:dm.lineage:jvMF7mrHR7OwG_DToKsJUA",
              "parentFolderUrn": "urn:adsk.wipprod:fs.folder:co.WI8roO18TU2Cl3P9y64z4w",
              "isAligned": false,
              "tipVersionUrn": "urn:adsk.wipprod:vf.file:vf.jvMF7mrHR7OwG_DToKsJUA?version=1"
          },
          "documentStatus": "Succeeded",
          "versionUrn": "urn:adsk.wipprod:vf.file:vf.jvMF7mrHR7OwG_DToKsJUA?version=1",
          "displayName": "example_document.rvt",
          "createUserId": "PD23PXGV8V3V",
          "createTime": "2015-10-21T16:29:30.0000000+00:00",
          "viewableGuid": "b1e3fda8-9a15-8cb9-9951-6f4781f8f897",
          "viewableId": "2df27d58-d1c2-467b-be10-80baf501cb87-0008ebd5",
          "viewableMime": "application/autodesk-svf",
          "bubbleUrn": "urn:adsk.wipprod:fs.file:vf.M7KsPcpXTn6nPPRhrQnjGA?version=1",
          "originalSeedFileVersionUrn": "urn:adsk.wipprod:fs.file:vf.M7KsPcpXTn6nPPRhrQnjGA?version=1"
        },
        {
          "...": ""
        }
    ]
}

```

Show More

You can use the value of `version` in the response above to obtain the clash tests performed for the latest model set version.

## [Step 2: Get the Clash Tests for the Model Set Version](#step-2-get-the-clash-tests-for-the-model-set-version)

The step above demonstrated how to get the latest version of a model set, but other methods on the model set service allow you to discover all the versions of a model set. Once you have determined the model set version you want to use, you can call [GET modelsets/:modelSetId/versions/:version/tests](../http-docs/http-mc-clash-service-v3-get-model-set-version-clash-tests-GET.md) to get the list of clash tests that have been performed against the model set version. This endpoint returns the test ID (a GUID) and the status of the test. A status of `Success` indicates that the test is complete and the test results are ready to download. You cannot download clash results unless the test is successful. You can use the clash test ID (GUID) to access the clash test result resources.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/clash/v3/containers/e6efd20e-f971-4705-aae0-1e5faa2eec11/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911/versions/42/tests' \
 -H 'Authorization: Bearer <token>'

```

### Example Response

```
{
    "page": {},
    "tests": [
        {
            "id": "74b70bb8-8802-a1fd-f201-890375a60c8f",
            "modelSetId": "00fb28a5-e8a4-2755-562a-7c2f0fc87911",
            "modelSetVersion": 42,
            "status": "Success"
        }
    ]
}

```

Show More

## [Step 3: Get the Clash Test Result Resource URLs](#step-3-get-the-clash-test-result-resource-urls)

The results of clash testing are a set of gzip compressed JSON documents that are generated by the clash test process and written to cloud storage. To work with the clash test results, you need to download these files locally. The [GET tests/:testId/resources](../http-docs/http-mc-clash-service-v3-get-clash-test-resources-GET.md) endpoint returns the URLs necessary to download the compressed clash result files. Note that the individual resource URLs returned by the clash service are time limited; you can use the validUntil property in the response from the resources endpoint to determine the viability of the associated URL. If the lease expires before you have downloaded a file, subsequent calls to the resources endpoint yield a new set of URLs with a new lease.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/clash/v3/containers/e6efd20e-f971-4705-aae0-1e5faa2eec11/tests/74b70bb8-8802-a1fd-f201-890375a60c8f/resources' \
     -H 'Authorization: Bearer <token>'

```

### Example Response

```
{
  "page": {},
  "resources": [
    {
      "type": "scope-version-clash.2.0.0",
      "extension": "json.gz",
      "url": "https://example.com/6f760056-db07-4239-ba4c-d9739ac50142/scope-version-clash.2.0.0.json.gz?token=da39a3ee5e6b4b0d3255bfef95601890afd80709",
      "headers": {},
      "validUntil": "2015-10-21T16:29:19.0000000+00:00"
    },
    {
      "type": "scope-version-clash-instance.2.0.0",
      "extension": "json.gz",
      "url": "https://example.com/6f760056-db07-4239-ba4c-d9739ac50142/scope-version-clash-instance.2.0.0.json.gz?token=da39a3ee5e6b4b0d3255bfef95601890afd80709",
      "headers": {},
      "validUntil": "2015-10-21T16:29:19.0000000+00:00"
    },
    {
      "type": "scope-version-document.2.0.0",
      "extension": "json.gz",
      "url": "https://example.com/6f760056-db07-4239-ba4c-d9739ac50142/scope-version-document.2.0.0.json.gz?token=da39a3ee5e6b4b0d3255bfef95601890afd80709",
      "headers": {},
      "validUntil": "2015-10-21T16:29:19.0000000+00:00"
    }
  ]
}

```

Show More

The following table summarises the three key resource files available via the resources endpoint:

| Type | Description |
| --- | --- |
| scope-version-clash.*.*.* | Pairwise, object-object clash results |
| scope-version-clash-instance.*.*.* | Viewable data for the objects listed in in scope-version-clash.*.*.* |
| scope-version-document.*.*.* | Document URNs for the objects listed in scope-version-clash-instance.*.*.* |

You can use the individual `url` properties in the response above to download the clash resources described by the `type` property.

## [Step 4: Download the individual Clash Test resources](#step-4-download-the-individual-clash-test-resources)

To download a clash test resource file, invoke GET on the URLs provided by the resources endpoint.

### Example Request

```
curl -v 'https://example.com/6f760056-db07-4239-ba4c-d9739ac50142/scope-version-clash.2.0.0.json.gz?token=da39a3ee5e6b4b0d3255bfef95601890afd80709'

```

This image illustrates the relationship between the JSON objects contained in these three files.



Every clash in scope-version-clash.2.0.0.json.gz is given a stable clash ID (id), 2202 in our example above. The ID is referred to as *stable* because it is invariant between clash tests performed on successive versions of the model set. For this to work, the IDs of the objects that are clashed also need to be stable. The clash[] array property on clash objects in the scope-version-clash.2.0.0.json.gz file contains the two stable object IDs participating in the clash pair (482 and 136, in our example).

Object stability in BIM 360 Model Coordination is maintained by the system. As part of the clash workflow, the system maintains a set of stable object identities for individual objects on a seed file lineage. As users upload new versions of a seed file onto an existing seed file lineage, the system uses the SIDs (stable object identities) from the previous version of the seed file to determine if the new objects it is encountering are actually new to the lineage, objects that were already on the lineage and might have stayed the same, or objects that changed only in terms of their graphical dimensions or the BIM data associated with them.

In order to view the clash results in the Viewer, it is necessary to process the scope-version-clash-instance.2.0.0.json.gz and scope-version-document.2.0.0.json.gz resources. The scope-version-clash-instance.2.0.0.json.gz resource contains the viewable object details of the clashes in the scope-version-clash.2.0.0.json.gz resource. The cid on the objects in the scope-version-clash-instance.2.0.0.json.gz is the ID of the clash in the scope-version-clash.2.0.0.json.gz resource. cid is the foreign key between scope-version-clash.2.0.0.json.gz and scope-version-clash-instance.2.0.0.json.gz; likewise, the loid and roid, left and right (stable) object ID, are the IDs of the stable objects reported in the scope-version-clash.2.0.0.json.gz clash[] array (482 and 136).

To view these objects in the Viewer, you must use another foreign key, ldid and rdid (left and right document ID), to ascertain the document version URNs that need to be loaded into the Viewer to view these clashes. ldid and rdid are indexes into the objects in scope-version-document.2.0.0.json.gz. You use these IDs to look up the document URNs in the scope-version-document.2.0.0.json.gz resource (2 and 3 on our example). Once you load these documents, you can find the objects in the Viewer using the lvid and rvid (left and right viewable IDs), which are the Viewer object identities associated with these specific versions of the document (17299 and 3403). Note that these viewable object IDs are not stable between successive seed file versions (that is, the system makes no guarantee that stable object 482 will have a Viewer viewable ID of 17299 in the next version of the document extracted by BIM 360 Docs following the upload of a new seed file version).

The red/green colour coding seen in the BIM 360 Model Coordination app is arbitrary, with the colouration being assigned to the left and right objects participating in the clash instance.


