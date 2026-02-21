# containers/:containerId/modelsets/:modelSetId

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-modelset-service-v3-get-model-set-GET/

---

Model Set

GET

# containers/:containerId/modelsets/:modelSetId

Retrieves a requested model set based on the model set ID.

Returns the requested model set object.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/bim360/modelset/v3/containers/:containerId/modelsets/:modelSetId |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token/) OAuth flow. |
| --- | --- |
| x-ads-region   enum: string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](/en/docs/acc/v1/overview/acc-regions) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The GUID that uniquely identifies the container. |
| --- | --- |
| modelSetId   string: UUID | The GUID that uniquely identifies the model set. |

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

| modelSetId   string: UUID | The GUID that uniquely identifies the model set. |
| --- | --- |
| modelSetType   enum: string | The type of content this model set tracks. Possible values: `Plans`, `ProjectFiles`. |
| containerId   string: UUID | The GUID that uniquely identifies the container. |
| folders   array: object | The ModelSetFolders that determine the documents included in the model set. |
| folderUrn   string | The ID of the folder in your project (can be found using the Data Management API). |
| name   string | The name of the model set. This name must be unique within the specified container. Min length: 1 Max length: 64. |
| description   string | A textual description of the model set. Min length: 1 Max length: 1024. |
| createdBy   string | The unique identifier of the user who created the model set. |
| createdTime   datetime: ISO 8601 | The date and time that the model set was created. |
| isDisabled   boolean | If set to true, a model set version is not automatically created following changes to documents within the model set. |
| tipVersion   int | The version number of the most recent version of the model set. |

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
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911' \
     -H 'Authorization: Bearer <token>'

```

### Response (200)

```
{
  "modelSetId": "00fb28a5-e8a4-2755-562a-7c2f0fc87911",
  "modelSetType": "Plans",
  "containerId": "f0f4f36a-ac64-687f-b132-8efe04b22454",
  "folders": [
    {
      "folderUrn": "urn:adsk.wipprod:fs.folder:co.WI8roO18TU2Cl3P9y64z4w"
    }
  ],
  "name": "Formal Coordination",
  "description": "Space for coordinating all disciplines",
  "createdBy": "PD23PXGV8V3V",
  "createdTime": "2015-10-21T16:31:44Z",
  "isDisabled": true,
  "tipVersion": 120
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
