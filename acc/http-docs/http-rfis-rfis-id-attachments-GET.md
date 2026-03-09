# rfis/:id/attachments

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-rfis-id-attachments-GET/

---

Attachments

GET

# rfis/:id/attachments

Retrieves a list of attachments for a specific RFI.

Use this endpoint to access all files uploaded to the RFI, including official responses, additional documents, and markups.

You can filter the results by attachment type or use pagination to retrieve large sets.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfis/:rfiId/attachments |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- rfiIdstring The ID of the RFI. To find the ID, call [POST search:rfis](http-rfis-rfi-search-POST.md).

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The number of attachments to return in the response. Possible values: `1â200`. Default: `10`. <br>For example, to limit the response to two attachments per page, use `limit=2`. |
| --- | --- |
| offset   int | The number of items to skip before starting to return results. <br>For example, to begin the results from the fourth item, use `offset=3`. |
| filter[attachmentTypes]   array: string | Filters the response to only include attachments of the specified types. <br>Possible values: `rfiResponse`, `rfiOfficialResponse`, `rfiWebHiddenFiles`, `bridgeFiles`.<br>If not provided, the default filter is: `rfiResponse`, `rfiOfficialResponse`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success |
| --- | --- |
| 400   Bad Request | The parameters are invalid |
| 401   Unauthorized | The provided bearer token is not valid |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation |
| 404   Not Found | RFI not found |
| 500   Internal Server Error | An unknown error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of attachments. |
| --- | --- |
| attachmentId   string: UUID | The unique ID of the attachment. |
| attachmentType   enum:string | The type of the attachment. <br>Possible values: `rfiResponse`, `rfiOfficialResponse`, `bridgeFiles`, `rfiWebHiddenFiles`. |
| displayName   string | The name of the attachment file as it appears in the UI. |
| fileName   string | The original name of the uploaded file, including its extension. |
| storageUrn   string | The storage URN of the attachment file. <br>Use this value to generate a signed URL and download the file via the Data Management API.<br>For more details, see the [Submit RFI Response](https://aps.autodesk.com/en/docs/acc/v1/tutorials/create-rfi-response/) tutorial. |
| domainEntityId   string: UUID | The ID of the related entity. |
| docsId   string: UUID | Not relevant |
| containerId   string | The ID of the container associated with the attachment. |
| rfiId   string | The ID of the RFI associated with the attachment. |
| lineageUrn   string | Not relevant |
| fileSize   int | The size of the attachment file in bytes. |
| fileType   string | The file extension type for the attachment. |
| version   int | The version number of the uploaded file. |
| versionUrn   string | Not relevant |
| tipVersionUrn   string | Not relevant |
| bubbleUrn   string | Not relevant |
| createdOn   datetime: ISO 8601 | The timestamp of the date and time the attachment was created, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| createdBy   string | The Autodesk ID of the user who added the attachment. |
| modifiedOn   datetime: ISO 8601 | The timestamp of the date and time the attachment was modified, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| modifiedBy   string | The Autodesk ID of the user who has modified the attachment. |
| createdByName   string | The name of the user who added the attachment. |
| isDeleted   boolean | Not relevant |
| deletedOn   datetime: ISO 8601 | The timestamp of the date and time the attachment was deleted, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| deletedBy   string | The Autodesk ID of the user who deleted the attachment. |
| pagination   object | The pagination object. |
| limit   int | The number of items returned per page. |
| offset   int | The number of items skipped before this page of results. |
| totalResults   int | The total number of items matching the request. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfis/:rfiId/attachments' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "attachmentId": "1234852d-5957-4145-9c8d-e7cfe9d564df",
      "attachmentType": "rfiResponse",
      "displayName": "Structural Plan - Rev A.pdf",
      "fileName": "revA_plan_final_v2.pdf",
      "storageUrn": "urn:adsk.objects:os.object:wip.dm.qa/b232ff3f-eff7-4e17-a486-362de84230a3.png",
      "domainEntityId": "c911852d-5957-4145-9c8d-e7cfe9d564df",
      "docsId": "c911852d-5957-4145-9c8d-e7cfe9d564df",
      "containerId": "12302fc6-00a5-45ca-a9df-4427b9247123",
      "rfiId": "0d302fc6-00a5-45ca-a9df-4427b9247c81",
      "lineageUrn": "urn:adsk.wipprod:dm.lineage:1t7QY9-JSxCB0TLh1qMvFQ",
      "fileSize": 1024,
      "fileType": "png",
      "version": 1,
      "versionUrn": "urn:adsk.wipprod:fs.file:vf.1HROnsnfQgq4N0b-nUoGge?version=1",
      "tipVersionUrn": "urn:adsk.wipprod:fs.file:vf.1HROnsnfQgq4N0b-nUoGge?version=1",
      "bubbleUrn": "urn:adsk.objects:os.object:modelderivative/building.rvt",
      "createdOn": "2018-08-01T08:56:48.699Z",
      "createdBy": "PER8KQPK2JRT",
      "modifiedOn": "2018-08-01T08:56:48.699Z",
      "modifiedBy": "PER8KQPK2JRT",
      "createdByName": "Jill Sharp",
      "isDeleted": false,
      "deletedOn": "2018-08-01T08:56:48.699Z",
      "deletedBy": "PER8KQPK2JRT"
    }
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 97
  }
}

```

Show More
