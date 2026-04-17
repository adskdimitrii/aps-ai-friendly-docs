# projects/{projectId}/items/{itemId}/attachments/{attachmentId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-attachments-attachmentId-PATCH/

---

Attachments

PATCH

# projects/{projectId}/items/{itemId}/attachments/{attachmentId}

Updates the upload status of an attachment associated with a submittal item. Use this endpoint after completing the file upload to update the attachment status. Note, this endpoint applies to the local files workflow only and is not used for Files tool attachments.

For more details about submittal attachments, see the [Submittal Attachments Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Attachments).

For details about attaching local files, see the [Attach Local File to Submittals](../how-to-docs/submittals-attach-local-files.md) tutorial.

For details about attaching exising files from the Files tool, see the [Attach Files From the Forma Files Tool to Submittals](../how-to-docs/submittals-attach-files-tool.md) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/items/:itemId/attachments/:attachmentId |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |
| itemId   string | The ID of the submittal item. To find the item ID, call [GET items](http-submittals-items-GET.md). |
| attachmentId   string | The ID of the attachment. To find the ID, call [GET attachments](http-submittals-items-itemId-attachments-GET.md). |

### Request

## [Body Structure](#body-structure)

| isFileUploaded   boolean | Indicates whether the attachment upload is complete. <br>Set this field to `true` once the file upload is finished.<br>`true`: the attachment upload is complete.<br>`false`: (default) the attachment upload is still in progress or pending completion. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The attachment object was successfully updated. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. |
| 401   Unauthorized | Invalid or missing authorization header. Verify the Bearer token and try again. |
| 403   Forbidden | The user is not authorized to perform this action. |
| 404   Not Found | The specified resource was not found. |
| 500   Internal Server Error | An unexpected error occurred on the server while processing the request. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| id   string: UUID | The internal, globally unique identifier (UUID) for the attachment. |
| --- | --- |
| itemId   string: UUID | The ID of the submittal item associated with the attachment. |
| taskId   string: UUID | The ID of the task within the review step to which the attachment is associated. - If the attachment was added to a review step, this field contains the task ID that identifies the relevant task. - If the attachment was not part of a review, this field is `null`. |
| name   string | The user-defined name of the attachment. This value is specified when the attachment is created and may differ from the original file name. |
| isFileUploaded   boolean | Indicates whether the attachment upload is complete.  > `true`: the attachment upload is complete.<br>`false`: the upload is still in progress or pending completion. |
| url   string | Not relevant |
| asyncState   enum:string | Represents the state of the asynchronous process triggered after marking the file upload as complete (`isFileUploaded=true`). The backend initiates this process to generate the `URN` for the attachment. <br>Possible values:  > `1` - Pending (the request is queued and awaiting processing).`2` - Started (the backend process to generate the `URN` has begun).`3` - Success (the `URN` was successfully created).`4` - Failure (the process failed, and the `URN` was not created). |
| uploadUrn   string | The unique identifier for the upload session associated with the attachment applicable only to local file uploads. This value is used to generate a URL for uploading the actual file. |
| urn   string | The unique identifier for a specific file version in the Files tool. |
| urnVersion   int | The version number of the file in Autodesk Forma Data Management. |
| revisionFolderUrn   string | Not relevant |
| revision   int | Not relevant |
| urnTypeId   enum:string | Specifies the type of urn associated with the attachment. This value identifies the storage type for the file reference. <br>Possible values: `2` This value is always set to `2` for both local and Files tool attachments. |
| categoryId   enum:string | The workflow state of the submittal item associated with the attachment.  > `Category IDs 1-4`: These represent active workflow states and can be set when creating an attachment.`Category IDs 5-8`: These represent historical records of attachments from earlier revisions of the submittal process and are automatically assigned by the system. <br>Possible values:  > `1` (Submission)`2` (For Review)`3` (Review Response)`4` (Final Response)`5` (Previous Submission)`6` (Previous For Review)`7` (Previous Review Response)`8` (Previous Final Response) |
| urnPage   string | Not relevant |
| resourceUrns   string | Not relevant |
| createdBy   string | The Autodesk ID of the user who created the attachment. |
| createdAt   datetime: ISO 8601 | The date and time when the attachment created, in ISO 8601 format. For example, `2018-02-01T12:09:24.198466Z`. |
| updatedAt   datetime: ISO 8601 | The date and time the attachment was last updated, in ISO 8601 format. For example, `2018-02-01T12:09:24.198466Z`. |
| updatedBy   string | The Autodesk ID of the user who last updated the attachment. |
| duplicatedFrom   string: UUID | The UUID of the source file the attachment was duplicated from. This indicates that the attachment was created as a copy of an existing file, preserving its metadata and association with the original file. |
| permittedActions   array: object | A list of actions that the user is allowed to perform on the attachment. |
| id   string | The ID of the action in the format `type_of_object::action`. For example, `Attachment::retrieve`. |
| fields   object | A mapping of field names to lists of possible values for each field. Note that an empty array indicates that there is no specific set of values for those fields. |
| mandatoryFields   array: string | Fields required to perform specific actions. The required fields depend on the user’s role and the action. |
| transitions   array: string | Not relevant |

## [Example](#example)

The attachment object was successfully updated.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/items/767b5888-2c6a-413d-8487-613966dd64ce/attachments/c0a85932-c7de-4a58-ae82-41ecb1d687d4' \
  -X 'PATCH' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "isFileUploaded": "true"
      }'

```

### Response

```
{
  "id": "1d0a9b65-f411-4eb2-b6bb-69f8ea483207",
  "itemId": "2df3b4cf-16f4-496e-8173-7125f31e3dd1",
  "taskId": "1ab2ae43-fb33-4868-be85-03f4873915fc",
  "name": "attachment-document.pdf",
  "isFileUploaded": "true",
  "url": null,
  "asyncState": "1",
  "uploadUrn": "urn:adsk.objects:os.object:wip.dm.prod/1a8148a6-d74e-4a6b-8cf2-38f2074f87d1.pdf",
  "urn": "urn:adsk.wipprod:fs.file:vf.TQW6YsrTTFGrJVJKAaK_ew?version=1",
  "urnVersion": 1,
  "revisionFolderUrn": "urn:adsk.wipprod:fs.folder:co.3is_lyUzTxu6nNXobG2P7Q\"",
  "revision": 0,
  "urnTypeId": "2",
  "categoryId": "1",
  "urnPage": null,
  "resourceUrns": null,
  "createdBy": "WD43ZJGKDFLFH",
  "createdAt": "2018-02-01T12:09:24.198466Z",
  "updatedAt": "2018-02-01T12:09:24.198466Z",
  "updatedBy": "WD43ZJGKDFLFH",
  "duplicatedFrom": "f4635373-a5b4-456c-af8d-e0446652967c",
  "permittedActions": [
    {
      "id": "Attachment::update",
      "fields": {
        "isFileUploaded": []
      },
      "mandatoryFields": [
        "isFileUploaded"
      ],
      "transitions": [
        ""
      ]
    }
  ]
}

```

Show More
