# containers/:containerId/modelsets/:modelSetId/versions/:version/views/:viewId

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-modelset-service-v3-get-model-set-view-version-GET/

---

Model Set: Views

GET

# containers/:containerId/modelsets/:modelSetId/versions/:version/views/:viewId

Retrieves a model set view as it exists in a specific model set version.

This operation determines which specific versions of the document lineages contained in the given view are present in the given model set version.

Returns the requested model set view version object.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/bim360/modelset/v3/containers/:containerId/modelsets/:modelSetId/versions/:version/views/:viewId |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-ads-region   enum: string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The GUID that uniquely identifies the container. |
| --- | --- |
| modelSetId   string: UUID | The GUID that uniquely identifies the model set. |
| version   int | The model set version number. |
| viewId   string: UUID | The GUID that uniquely identifies the view. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The `Retry-After` header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| viewId   string: UUID | The GUID that uniquely identifies the view. |
| --- | --- |
| modelSetId   string: UUID | The GUID that uniquely identifies the model set. |
| documentVersions   array: object | The document versions included in this version of the model set. |
| documentLineage   object | A document from a model set. |
| lineageUrn   string | The URN of the document lineage. |
| parentFolderUrn   string | The URN of the parent folder for the document lineage. |
| isAligned   boolean | Indicates whether the document lineage is aligned. |
| tipVersionUrn   string | The tip version URN for the document lineage. |
| documentStatus   enum: string | The status of the document. Possible values: `Succeeded`, `Failed`, `Running`, `Skipped`. |
| forgeType   enum: string | The forge type associated with this document (used by the Document Management APIs). Possible values: `versions:autodesk.bim360:Document`, `versions:autodesk.bim360:File`. |
| versionUrn   string | The URN of the document version. |
| displayName   string | The display name of the document version. |
| viewableName   string | The name of the viewable in the Model Derivative manifest. |
| createUserId   string | The unique identifier of the user who created the document version. |
| createTime   datetime: ISO 8601 | The date and time that the document version was created. |
| viewableGuid   string | The ID of the geometry node in the derivative manifest to which this document version refers. |
| viewableId   string | The ID of the viewable for the document version. |
| viewableMime   string | The mime type of the viewable for the document version. |
| bubbleUrn   string | The URN of the Model Derivative bubble for the document version. |
| originalSeedFileVersionUrn   string | The URN of the seed file version from which this document was originally extracted. |
| originalSeedFileVersionName   string | The name of the seed file version from which this document was originally extracted. |
| version   int | The model set version number. |

### Response

## [Body Structure (400)](#body-structure-400)

Expand all

| type   string | The error code. |
| --- | --- |
| title   string | A short title for the error. |
| detail   string | A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. |
| errors   array: object | A set of specific validation errors that need to be fixed. |
| field   string | The field which failed validation. |
| title   string | A short title for the error. |
| detail   string | A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. |
| type   string | The error code. |

## [Example](#example)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911/versions/42/views/7ed27144-ac06-4b72-5dd6-76bee05854be' \
     -H 'Authorization: Bearer <token>'

```

### Response (200)

```
{
  "viewId": "7ed27144-ac06-4b72-5dd6-76bee05854be",
  "modelSetId": "00fb28a5-e8a4-2755-562a-7c2f0fc87911",
  "documentVersions": [
    {
      "documentLineage": {
        "lineageUrn": "urn:adsk.wipprod:dm.lineage:jvMF7mrHR7OwG_DToKsJUA",
        "parentFolderUrn": "urn:adsk.wipprod:fs.folder:co.WI8roO18TU2Cl3P9y64z4w",
        "isAligned": false,
        "tipVersionUrn": "urn:adsk.wipprod:fs.file:vf.jvMF7mrHR7OwG_DToKsJUA?version=1"
      },
      "documentStatus": "Succeeded",
      "forgeType": "versions:autodesk.bim360:Document",
      "versionUrn": "urn:adsk.wipprod:fs.file:vf.jvMF7mrHR7OwG_DToKsJUA?version=1",
      "displayName": "example_document.rvt",
      "viewableName": "Level 1",
      "createUserId": "PD23PXGV8V3V",
      "createTime": "2015-10-21T16:29:30Z",
      "viewableGuid": "b1e3fda8-9a15-8cb9-9951-6f4781f8f897",
      "viewableId": "2df27d58-d1c2-467b-be10-80baf501cb87-0008ebd5",
      "viewableMime": "application/autodesk-svf",
      "bubbleUrn": "urn:adsk.wipprod:fs.file:vf.M7KsPcpXTn6nPPRhrQnjGA?version=1",
      "originalSeedFileVersionUrn": "urn:adsk.wipprod:fs.file:vf.M7KsPcpXTn6nPPRhrQnjGA?version=1",
      "originalSeedFileVersionName": "Hospital_Architectural.rvt"
    }
  ],
  "version": 42
}

```

Show More

### Response (400)

```
{
  "type": "BadInput",
  "title": "One or more input values in the request were bad",
  "detail": "The following parameters are invalid: containerId",
  "errors": [
    {
      "field": "containerId",
      "title": "Invalid parameter",
      "detail": "The value 'testing' is not valid.",
      "type": "BadInput"
    }
  ]
}

```

Show More
