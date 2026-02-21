# containers/:containerId/modelsets/:modelSetId/issues

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-modelset-service-v3-add-model-set-issue-POST/

---

Model Set

POST

# containers/:containerId/modelsets/:modelSetId/issues

Adds a model set visual inspection issue, represented as a BIM360 issue.

The data associated with `pushpin` is supported by the Viewerâs Pushpin extension. See the [pushpin tutorial](/en/docs/bim360/v1/tutorials/pushpins/) for more information.

The created job performs the following steps:

1. Creates a BIM 360 Issue with the requested information.
2. Uploads any provided screenshots to the projectâs photos folder, and attaches them to the newly created BIM 360 Issue.

The response contains information about the created model set job.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/bim360/modelset/v3/containers/:containerId/modelsets/:modelSetId/issues |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:create`, `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token/) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| x-ads-region   enum: string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](/en/docs/acc/v1/overview/acc-regions) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The GUID that uniquely identifies the container. |
| --- | --- |
| modelSetId   string: UUID | The GUID that uniquely identifies the model set. |

### Request

## [Body Structure](#body-structure)

Expand all

| title*   string | The title of the new issue. Min length: 1 Max length: 4200. |
| --- | --- |
| description   string | The description of the new issue. Max length: 10000. |
| assignedTo   string | The user, role or company that the new issue is assigned to. |
| assignedToType   enum: string | Specifies the type that the assignedTo parameter refers to. Possible values: `User`, `Role`, `Company`. |
| dueDate   datetime: ISO 8601 | The date and time that the new issue is due. |
| locationId   string: UUID | The location ID associated with the new issue. |
| locationDescription   string | The description of the location associated with the new issue. |
| owner   string | The user who owns the new issue. |
| status   enum: string | The status of the new issue. Possible values: `Open`, `Draft`. |
| pushpin*   object | An issue push pin object that describes a visual marker to place an issue on the 3D model. |
| location*   object | A vector describing where in 3D space the pushpin is located. |
| x*   int | The X component of the 3D vector. |
| y*   int | The Y component of the 3D vector. |
| z*   int | The Z component of the 3D vector. |
| objectId*   int | The ID of the object in the viewer with which to link this issue. |
| externalId   string | The external ID (for example, derived from the Revit ID) of the object in the viewer with which to link this issue. |
| attributesVersion   int | The version of the data described in the viewer state property. |
| type   enum: string | The type of pushpin. Possible values: `TwoDVectorPushpin`. |
| viewerState   object | An object describing the current state of the viewer, such as the camera position. |
| issueTypeId*   string: UUID | The issue type ID associated with the new issue. |
| issueSubTypeId*   string: UUID | The issue sub-type ID associated with the new issue. |
| rootCauseId   string: UUID | The root cause ID associated with the new issue. |
| customAttributes   array: object | The list of attributes to associate with the new issue. Max items: 64. |
| id   string: UUID | The ID of the custom attribute, as defined in the project settings. |
| value   string | The value of the custom attribute. |
| screenShots   array: string: UUID | The unique identifiers of screenshots associated with the new issue. Max items: 5. |
| documentVersionUrn*   string | A document or seed file version URN with which to associate the issue. Min length: 1 Max length: 80. |
| viewableName   string | The name of the viewable in the Model Derivative manifest to track along the seed file lineage. This setting is ignored if the `lineageUrn` is the URN of a BIM360 Docs Plans folder document. Min length: 1 Max length: 430. |
| viewContext*   array: object | Provides context for when this issue is viewed. Max items: 1000. |
| urn*   string | A document or seed file version URN with which to associate the issue. Min length: 1 Max length: 80. |
| viewableName   string | The name of the viewable in the Model Derivative manifest for the supplied version URN. Min length: 1 Max length: 430. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 202   Accepted | The model set job associated with this request |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 415   Unsupported Media Type | The `Content-Type` header must be `application/json`. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The `Retry-After` header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (202)](#body-structure-202)

Expand all

| jobId   string: UUID | The GUID that uniquely identifies the job. |
| --- | --- |
| modelSetId   string: UUID | The GUID that uniquely identifies the model set associated with the job. |
| resource   string | The resource associated with the job. |
| createdIssueIds   array: string: UUID | If this job tracks the creation of model set inspection issues, the IDs of the created issues. |
| status   enum: string | The current job status. Possible values: `Failed`, `Running`, `Succeeded`, `Archived`. |
| job   object | A job. |
| operation   string | The operation associated with the job. |
| seed   object | The JSON payload which seeded the job. |

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
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911/issues' \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '[
           {
             "title": "Mechanical Return Air 1 and 6 other objects",
             "description": "Reroute Mechanical Return Air 1 along corridor",
             "assignedTo": "PD23PXGV8V3V",
             "assignedToType": "User",
             "pushpin": {
               "location": {
                 "x": 426.77023,
                 "y": 176.68831,
                 "z": 682.2887
               },
               "objectId": 22,
               "type": "TwoDVectorPushpin",
               "viewerState": {}
             },
             "issueTypeId": "9f2b9b56-1e62-76c1-75ab-c6f15a53599d",
             "issueSubTypeId": "7bc10cee-441e-82c3-5c19-1d28c1a5b167",
             "customAttributes": [
               {
                 "id": "74b70bb8-8802-a1fd-f201-890375a60c8f",
                 "value": "Coordination"
               }
             ],
             "screenShots": [
               "d98c1dd4-008f-04b2-e980-0998ecf8427e"
             ],
             "documentVersionUrn": "urn:adsk.wipprod:fs.file:vf.jvMF7mrHR7OwG_DToKsJUA?version=1",
             "viewableName": "Level 1",
             "viewContext": [
               {
                 "urn": "urn:adsk.wipprod:fs.file:vf.jvMF7mrHR7OwG_DToKsJUA?version=1",
                 "viewableName": "Level 1"
               }
             ]
           }
         ]'

```

Show More

### Response (202)

```
{
  "jobId": "49244371-ee08-9afa-01f8-26fcd8ecb03d",
  "modelSetId": "00fb28a5-e8a4-2755-562a-7c2f0fc87911",
  "status": "Succeeded",
  "job": {
    "operation": "OperationName",
    "seed": {}
  }
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
