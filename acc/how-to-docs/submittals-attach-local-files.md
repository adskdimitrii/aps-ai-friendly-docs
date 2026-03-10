# Attach Local Files to Submittals

Source: https://aps.autodesk.com/en/docs/acc/tutorials/submittals/attach-local-files/

---

# Attach Local Files to Submittals

This tutorial demonstrates how to attach local files to a submittal item in an Autodesk Construction Cloud (ACC) project. The steps include verifying the user’s permissions and gathering required fields, creating the attachment object, generating a signed S3 URL, uploading the file to the signed URL, and updating the attachment status. For more information on working with submittals, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Create_Submittal).

For information about attaching files to submittals that were already uploaded to the ACC Files tool, see the [Attach Files to Submittals from the Files Tool](en/docs/acc/v1/tutorials/attach-files-tool/) tutorial.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:read` `data:write` scopes.
- Verify that you have access to the relevant account and ACC project.
- Find the relevant project ID for the project you want to create a submittal item in by following the [Retrieve an Account ID and Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the project ID is `91b5ea71-e3ea-495b-999d-57443a8af6a4`.
- This tutorial assumes an item was created in Submit state `sbc-1` by a user with manager permissions. For more information on creating a submittal item, see the [Create a Submittal Item](submittals-create-submittal-item.md) tutorial. In this example, assume the submittal item ID is `938eb16d-5603-4df9-adcd-00f75d48e145`.
- Ensure you have assigned manager-level permissions to at least one user for the project via the UI. To assign a manager to a submittal item, you need to ensure the user has the necessary permissions and roles set within the project. For instructions on setting up roles and permissions see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittals_Permissions).
- The Submittal Item workflow progresses through several sequential states. Below are the states in the UI and their equivalent API names:
    | UI State | API Name |
    | --- | --- |
    | Submit | `sbc-1` |
    | Prepare for Review | `mgr-1` |
    | Review | `rev` |
    | Close and Distribute | `mgr-2` |
    | Closed | `sbc-2` |

## [Step 1: Verify Permissions and Fields](#step-1-verify-permissions-and-fields)

Before uploading an attachment, verify the user’s permissions and gather the mandatory and optional fields required to make the [POST attachment](../http-docs/http-submittals-attachments-POST.md) request in step 2.

Call [GET item/:id](../http-docs/http-submittals-items-itemId-GET.md) using the project ID (`2570d4e5-9aef-4b41-8e45-a454f2f3fd65`) and the submittal item ID (`938eb16d-5603-4df9-adcd-00f75d48e145`). Check the `permittedActions` object for `Attachment::create`. If this action is listed, the user has permission to create an attachment.

The `permittedActions` object also provides the `mandatoryFields` and `fields` arrays, which specify the required and optional parameters for the POST attachments request. Calling [GET item/:id](../http-docs/http-submittals-items-itemId-GET.md) at any stage in the workflow will return the permitted actions for the user at that point for the submittal item.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/2570d4e5-9aef-4b41-8e45-a454f2f3fd65/items/938eb16d-5603-4df9-adcd-00f75d48e145' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
  {
    "id": "938eb16d-5603-4df9-adcd-00f75d48e145",
    "identifier": 12,
    "typeId": "3379aa42-1650-4375-a5df-94b33a51020e",
    "specId": "65bf7408-93f3-462e-84ab-17e5710c7536",
    "specIdentifier": "1",
    "specTitle": "1",
    "subsection": null,
    "title": "demo create attachment item",
    "description": "",
    "priority": "Normal",
    "revision": 0,
    "stateId": "sbc-1",
    "statusId": "1",
    "ballInCourt": [],
    "ballInCourtUsers": [
        "MFEGJ9W5GGQL"
    ],
    "ballInCourtCompanies": [],
    "ballInCourtRoles": [],
    "ballInCourtType": "subcontractor",
    "manager": "MFEGJ9W5GGQL",
    "managerType": "1",
    "subcontractor": "MFEGJ9W5GGQL",
    "subcontractorType": "1",
    "watchers": [],
    "dueDate": "2024-11-23",
    "requiredOnJobDate": null,
    "leadTime": null,
    "requiredDate": null,
    "requiredApprovalDate": null,
    "submitterDueDate": "2024-11-23",
    "sentToSubmitter": "2024-11-07T13:31:27.823547Z",
    "receivedFromSubmitter": null,
    "submittedBy": null,
    "managerDueDate": null,
    "sentToReview": null,
    "sentToReviewBy": null,
    "receivedFromReview": null,
    "publishedDate": null,
    "publishedBy": null,
    "responseId": null,
    "responseComment": "",
    "respondedAt": null,
    "respondedBy": null,
    "packageId": null,
    "packageIdentifier": null,
    "packageTitle": null,
    "packageSpecIdentifier": null,
    "folderUrn": "urn:adsk.wipqa:fs.folder:co.TEK6K9PaSPqfowbE80rOJw",
    "revisionsFoldersUrns": {
        "0": {
            "revision": 0,
            "folderUrn": "urn:adsk.wipqa:fs.folder:co.TEK6K9PaSPqfowbE80rOJw",
            "folderUrnCreatedAt": "2024-11-07 13:31:28.812408+00:00"
        }
    },
    "createdAt": "2024-11-07T13:31:27.827379Z",
    "createdBy": "MFEGJ9W5GGQL",
    "updatedAt": "2024-11-07T13:31:28.818762Z",
    "updatedBy": "MFEGJ9W5GGQL",
    "permittedActions": [
        {
            "id": "Item::retrieve",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Item::add_reference",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Item::delete_reference",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Attachment::list",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "AttachmentDraft::list",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Comment::list",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Step::list",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Item::partial_update",
            "fields": {
                "description": [],
                "subsection": [],
                "typeId": [],
                "mailNote": [],
                "sendEmails": [
                    true,
                    false
                ],
                "title": [],
                "packageId": [],
                "specId": [],
                "priority": [],
                "ballInCourtUsers": [],
                "ballInCourtRoles": [],
                "ballInCourtCompanies": [],
                "dueDate": [],
                "manager": [],
                "managerType": [],
                "subcontractor": [],
                "subcontractorType": [],
                "watchers": [],
                "submitterDueDate": [],
                "sentToSubmitter": [],
                "receivedFromSubmitter": [],
                "managerDueDate": [],
                "sentToReview": [],
                "receivedFromReview": [],
                "publishedDate": [],
                "requiredDate": [],
                "requiredApprovalDate": [],
                "requiredOnJobDate": [],
                "leadTime": [],
                "customIdentifier": []
            },
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Item::wf_transition",
            "fields": {
                "stateId": [],
                "title": [],
                "description": [],
                "packageId": [],
                "specId": [],
                "subsection": [],
                "typeId": [],
                "priority": [],
                "ballInCourtUsers": [],
                "ballInCourtRoles": [],
                "ballInCourtCompanies": [],
                "manager": [],
                "managerType": [],
                "subcontractor": [],
                "subcontractorType": [],
                "watchers": [],
                "submitterDueDate": [],
                "sentToSubmitter": [],
                "receivedFromSubmitter": [],
                "managerDueDate": [],
                "sentToReview": [],
                "receivedFromReview": [],
                "publishedDate": [],
                "requiredDate": [],
                "requiredApprovalDate": [],
                "requiredOnJobDate": [],
                "leadTime": [],
                "mailNote": [],
                "sendEmails": [
                    true,
                    false
                ]
            },
            "mandatoryFields": [
                "stateId"
            ],
            "transitions": [
                {
                    "id": "sbc-1::mgr-1",
                    "name": "Submit to Manager",
                    "stateFrom": {
                        "id": "sbc-1",
                        "name": "SBC 1"
                    },
                    "stateTo": {
                        "id": "mgr-1",
                        "name": "MGR 1"
                    },
                    "transitionFields": [
                        "mailNote",
                        "manager",
                        "managerType",
                        "saveAttachmentDrafts"
                    ],
                    "mandatoryFields": [
                        "manager"
                    ],
                    "actionId": "ITEM_TRANSITION_SBC1_MGR1"
                },
                {
                    "id": "sbc-1::void",
                    "name": "Send to Void",
                    "stateFrom": {
                        "id": "sbc-1",
                        "name": "SBC 1"
                    },
                    "stateTo": {
                        "id": "void",
                        "name": "VOID"
                    },
                    "transitionFields": null,
                    "mandatoryFields": null,
                    "actionId": "ITEM_TRANSITION_SBC1_VOID"
                },
                {
                    "id": "sbc-1::sbc-2",
                    "name": "Close and distribute",
                    "stateFrom": {
                        "id": "sbc-1",
                        "name": "SBC 1"
                    },
                    "stateTo": {
                        "id": "sbc-2",
                        "name": "SBC 2"
                    },
                    "transitionFields": [
                        "subcontractor",
                        "subcontractorType",
                        "watchers",
                        "responseId",
                        "responseComment",
                        "saveAttachmentDrafts",
                        "duplicateAttachments",
                        "customIdentifier"
                    ],
                    "mandatoryFields": [
                        "responseId",
                        "customIdentifier"
                    ],
                    "actionId": "ITEM_TRANSITION_SBC1_SBC2"
                }
            ]
        },
        {
            "id": "Item::create_revision",
            "fields": {
                "subcontractor": [],
                "subcontractorType": [],
                "submitterDueDate": [],
                "watchers": [],
                "mailNote": []
            },
            "mandatoryFields": [
                "subcontractor",
                "subcontractorType",
                "submitterDueDate"
            ],
            "transitions": []
        },
        {
            "id": "Attachment::create",
            "fields": {
                "name": [],
                "itemId": [],
                "urn": [],
                "urnTypeId": [],
                "sendEmails": [
                    true,
                    false
                ],
                "isFileUploaded": [
                    true
                ],
                "categoryId": [
                    "4"
                ]
            },
            "mandatoryFields": [
                "urnTypeId",
                "name"
            ],
            "transitions": []
        },
        {
            "id": "Attachment::bulk_destroy",
            "fields": {
                "payloads": []
            },
            "mandatoryFields": [
                "payloads"
            ],
            "transitions": []
        },
        {
            "id": "AttachmentDraft::create",
            "fields": {
                "name": [],
                "itemId": [],
                "urn": [],
                "urnTypeId": [],
                "isFileUploaded": [
                    true
                ],
                "categoryId": [
                    "4"
                ]
            },
            "mandatoryFields": [
                "urnTypeId",
                "name"
            ],
            "transitions": []
        },
        {
            "id": "Comment::create",
            "fields": {
                "body": [],
                "itemId": [],
                "sendEmails": [
                    true,
                    false
                ]
            },
            "mandatoryFields": [
                "body",
                "itemId"
            ],
            "transitions": []
        },
        {
            "id": "Step::create_from_template",
            "fields": {
                "templateId": []
            },
            "mandatoryFields": [
                "templateId"
            ],
            "transitions": []
        },
        {
            "id": "Step::overwrite",
            "fields": {
                "steps": [],
                "fromStepId": []
            },
            "mandatoryFields": [
                "steps"
            ],
            "transitions": []
        }
    ],
    "customIdentifier": "12",
    "customIdentifierHumanReadable": "12"
}

```

Show More

Note the following:

- Mandatory Fields:

> * Locate the `permittedActions` object with `"id": "Attachment::create"`. The `mandatoryFields` array specifies the required fields for creating an attachment:
> + `name`: The name of the attachment.
> + `urnTypeId`: The type of object being referenced. This field must always be included, and its value should always be `2`.

- Optional Fields:

> * Under the same `"id": "Attachment::create"` entry, the `fields` array lists optional parameters:
> + `categoryId`: Links the attachment to a specific workflow state.

Include these fields in your POST attachment request in Step 2.

## [Step 2: Create an Attachment Object](#step-2-create-an-attachment-object)

Call [POST attachment](../http-docs/http-submittals-attachments-POST.md) to create the attachment object. This step registers the attachment metadata with the submittal item but does not yet upload the file.

- The `urnTypeId` field must be included in the request and should always have the value `2`.
- The `categoryId` is typically assigned automatically based on the submittal item’s current state. In most cases, you do not need to include `categoryId` in your request. However, for specific exceptions, you must provide it explicitly:

> * Prepare for Review (`mgr-1`): By default, when the submittal item is in the Prepare for Review state, the `categoryId` is assigned automatically as `2` (for-review). If you want the attachment to be tagged as a Submit state attachment instead, you must explicitly set `categoryId` to `1` in the request.
> * Final Response Attachments: If you are closing a submittal item from a state other than Close and Distribute (`mgr-2`), and you want the attachment to be marked as a final response, explicitly set `categoryId` to `4`.

- For items in the Review (`rev`) state, include the `taskId` field to associate the attachment with a specific task. This ensures the attachment is linked to the relevant task in the review process.

You can retrieve the full list of available `categoryId` values and their corresponding meanings by calling [GET metadata](../http-docs/http-submittals-metadata-GET.md), and reviewing the `attachmentCategories` list in the response.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/2570d4e5-9aef-4b41-8e45-a454f2f3fd65/items/938eb16d-5603-4df9-adcd-00f75d48e145/attachments' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "name":"sbc1-file1.pdf",
        "urnTypeId":"2"
      }'

```

Show More

### Response

```
{
    "id": "c14eabff-d79c-4429-9fa4-504a7aff7a37",
    "revisionFolderUrn": "urn:adsk.wipqa:fs.folder:co.TEK6K9PaSPqfowbE80rOJw",
    "permittedActions": [
        {
            "id": "Attachment::retrieve",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Attachment::partial_update",
            "fields": {
                "isFileUploaded": [
                    true
                ],
                "sendEmails": [
                    true,
                    false
                ]
            },
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Attachment::destroy",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Attachment::annotate",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        }
    ],
    "isFileUploaded": false,
    "url": null,
    "asyncState": "1",
    "createdBy": "MFEGJ9W5GGQL",
    "createdAt": "2024-11-09T19:39:28.779314Z",
    "updatedBy": "MFEGJ9W5GGQL",
    "updatedAt": "2024-11-09T19:39:28.779330Z",
    "name": "sbc1-file1.pdf",
    "uploadUrn": "urn:adsk.objects:os.object:wip.dm.prod/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf",
    "urn": null,
    "urnPage": null,
    "resourceUrns": null,
    "urnTypeId": "2",
    "urnVersion": null,
    "revision": 0,
    "itemId": "938eb16d-5603-4df9-adcd-00f75d48e145",
    "categoryId": "1",
    "taskId": null,
    "duplicatedFrom": null
}

```

Show More

Note the following:

- Attachment ID (`id`): This is required for subsequent steps to update the attachment or finalize its status.
- Category ID (`categoryId`): Ensure it is correctly set, either automatically or manually, depending on the workflow state.
- Permitted Actions: The object containing `"id": "Attachment::partial_update"` in the response indicates that the user can update the attachment with `isFileUploaded=true`. This will be used in Step 6.
- Upload URN (`uploadUrn`- `urn:adsk.objects:os.object:wip.dm.prod/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf`): Use this in Step 3 to generate a signed S3 URL for uploading the file.

The upload URN includes the following sections: `<urn:adsk.objects:os.object>:<bucket key>/<object key>` Note the bucket key - `wip.dm.prod` and the object key - `a9d330bc-411f-4aaf-874a-9844cc002d00.pdf`

## [Step 3: Generate a Signed S3 URL](#step-3-generate-a-signed-s3-url)

Use the bucket key from the uploadUrn (`wip.dm.prod`) and the object key (`a9d330bc-411f-4aaf-874a-9844cc002d00.pdf`) to call [GET signeds3upload](../../data/http-docs/http-buckets--bucketKey-objects--objectKey-signeds3upload-GET.md) to generate a signed URL for the storage object.

This endpoint supports generating multiple signed URLs, which allows you to upload multiple chunks of the same file in parallel. For more information, see [GET signeds3upload](../../data/http-docs/http-buckets--bucketKey-objects--objectKey-signeds3upload-GET.md).

### Request

```
curl -v 'https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf/signeds3upload' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "uploadKey": "AQICAHgdUabBXKpMwUkoF5ivioCSHNq_j4g7HRbexUuXMaEMKgErLyuCRjoF46bviMXV-sbuAAAB7TCCAekGCSqGSIb3DQEHBqCCAdowggHWAgEAMIIBzwYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAxG3C2tr0WU_T43gXwCARCAggGgtWbNXJc6yIEVkQJjWoLmM0-Nuo1xXmx9C-vSZesB09y27QOgqhQN5BSJxKEVLllcvWGJTeKn3p6mAI2TKwnXswUseNCx_p_EhlYydzfYE8VHixCywEmBkOMIPX9OV0RogT1PjpQWobcM-_3W6Dnh9xtmpQ595QWLCGfVQdW8eg7XsdDP6i-ltDIbm4QMIXHgoX3zJ2Xk6c3tNAco_PuI3JYTRCSt1mwDZp7EeWK299HLn2qCZ_7O0wGNJjQMFJW0QMDcaHFRj75rCawWW-feAuUIVUisvVyimlZrqNU0LytKxfhP2wJ3WEc7pT0Ny18hTsIi8TAPcUa9VclEluFUJk5FP_jaRmQ9quol9cI1CQAxcbbes-F8rP2D-Xk87JXhbB5ik76SxvPZCT0eG7n9gYsD0PCRBFw5R-BqJL7k9AHTNKzObp14Of9rNWVNMFROQaR9zjLlC4z1hBsCrsdmauTPLcxNVkbVmO5ZNYw_uSxGIRtpJk2MEqRyqwVXiqla2CZvBo71v556jQ_PpBB634zfTar9wlbUbHJ5QNz9quo=",
  "uploadExpiration": "2024-11-12T00:00:00Z",
  "urlExpiration": "2024-11-09T19:54:47Z",
  "urls": [
    "https://com-autodesk-oss-opsstaging-direct-upload.s3-accelerate.amazonaws.com/87/84/37/b5/bucket/wip.dm.prod/signed-url-uploads/878437b5-de35-4099-b839-6b8d26c89017?partNumber=1&uploadId=ICJ5dAXCqK2scG.PNojqBgRMXyU5GAL4DqwGwyMaxiWXB_iDUA96Kh5NzZGYdhj9WWnKqPH1QzrgCP7tolYFEvmMT8JzRQtUK7XdJodDa2gQzZZMW9OG0nufS9ORuCW9mJ6ou0fgAcUU_I.H_S0pThTC0Qgj7MsIBkBZGAwn9Tdm2IYP37zsZHqr_HcfxJo0&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIAQDIiPq1P0QSdV5pl45oJoevxujuA3zCDsOQISx6Yi5AiEA33FX4GM6Xx1McEmfK9QsgK%2FB%2B66ttSAYShuKhayoW1IquAIIfRAAGgw5OTM3ODk5OTIwNjMiDEoLnUnPIJ%2BwHmyrgSqVAiXz78kIm%2BIEV9l5NWQ%2Fe75tvOfAyLdbPa%2ByLkg7rY6efsKq9l1ypelppRRUinjocOzD4vM90GPU9sCRNWzY2n5Gd7y0mRBJlVAAO%2FuIin2g8kZ4mJp492FYej%2BmS0%2FU4tRFcmvVH7tWYOoTu%2BQDh7prT1aBUQeW74P9%2BF3mviTg7fYPwtpeqcn9Cz3VVYJxEFycCRPSvfucJf2bqBiWr0iXeuxlM0t6WNqw3QtfyozJ2huvbgyNJmhxTen1WKalO1LSR8ZPs4BbQVUjJ%2FPI%2Ffkho9%2FyemVDen02TT10iGULACxnASeNu%2Fs0BW3lBKTdxoWCw1CmRLiJjQQgG%2BCWZGthe%2FTIk7Wq0dK0gt1DJbHRRU9Xlfowofe%2BuQY6nQGxe7krNSw7O%2BaW3NbxXmYBv4SRK3ZpvzTjSenMczJPEvPJVJSUqTB0I7tBcvht6h%2ByUq7LEoKSHIwqfE0Zcyyxi5NPaK1WyAp8SsPp4KwX66WXsLG3X0cG6RgaaMHlgPpkr5NBr2GLGruRhMDi1V0rCFFWTnO%2FooZQkaNVb8Z9qRuJ1Ni7qkyhX7OUbxkfoYF73tkIrubt%2FcDVMhaN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20241109T194437Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=ASIA6OYT73R7WD3UXP63%2F20241109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d425d4a7ea887d022adfa95b56655157fc55214e54e43f83486c1844da151622 "
  ]

}

```

Show More

Note the `uploadKey` and the `urls` response attributes.

## [Step 4: Upload a File to the Signed URL](#step-4-upload-a-file-to-the-signed-url)

To upload the file to the signed URL, use a PUT method and the `urls` attribute as the URI.

Note that you should not use a bearer token with this call.

### Request

```
curl -X PUT --data-binary @D:\sbc1-file1.pdf "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/26668812-6bb1-4f80-bab2-09776f24fd98?uploadId=[UPLOAD_ID]&partNumber=1&X-Amz-Security-Token=[AMZ_TOKEN]%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220203T052230Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=[AMZ_CREDENTIAL]%2F20220203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=[AMZ_SIGNATURE]"

```

Note that a successful call (`200`) returns an empty response.

## [Step 5: Complete the Upload](#step-5-complete-the-upload)

Use the bucket key (`wip.dm.prod`), the object key (`a9d330bc-411f-4aaf-874a-9844cc002d00.pdf`) and the upload key (`AQICAHgdUabBXKpMwUkoF5ivioCSHNq_j4g7HRbexUuX..........UbHJ5QNz9quo=`) to call [POST signeds3upload](../../data/http-docs/http-buckets--bucketKey-objects--objectKey-signeds3upload-POST.md) to complete the upload.

This endpoint needs to be called within 24 hours from the time you began uploading the file.

### Request

```
curl -X POST "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf/signeds3upload" \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a" \
   -d '{
         "uploadKey": "AQICAHgdUabBXKpMwUkoF5ivioCSHNq_j4g7HRbexUuXMaEMKgErLyuCRjoF46bviMXV-sbuAAAB7TCCAekGCSqGSIb3DQEHBqCCAdowggHWAgEAMIIBzwYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAxG3C2tr0WU_T43gXwCARCAggGgtWbNXJc6yIEVkQJjWoLmM0-Nuo1xXmx9C-vSZesB09y27QOgqhQN5BSJxKEVLllcvWGJTeKn3p6mAI2TKwnXswUseNCx_p_EhlYydzfYE8VHixCywEmBkOMIPX9OV0RogT1PjpQWobcM-_3W6Dnh9xtmpQ595QWLCGfVQdW8eg7XsdDP6i-ltDIbm4QMIXHgoX3zJ2Xk6c3tNAco_PuI3JYTRCSt1mwDZp7EeWK299HLn2qCZ_7O0wGNJjQMFJW0QMDcaHFRj75rCawWW-feAuUIVUisvVyimlZrqNU0LytKxfhP2wJ3WEc7pT0Ny18hTsIi8TAPcUa9VclEluFUJk5FP_jaRmQ9quol9cI1CQAxcbbes-F8rP2D-Xk87JXhbB5ik76SxvPZCT0eG7n9gYsD0PCRBFw5R-BqJL7k9AHTNKzObp14Of9rNWVNMFROQaR9zjLlC4z1hBsCrsdmauTPLcxNVkbVmO5ZNYw_uSxGIRtpJk2MEqRyqwVXiqla2CZvBo71v556jQ_PpBB634zfTar9wlbUbHJ5QNz9quo="
       }'

```

### Response

```
{
    "bucketKey": "wip.dm.prod",
    "objectId": "urn:adsk.objects:os.object:wip.dm.prod/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf",
    "objectKey": "a9d330bc-411f-4aaf-874a-9844cc002d00.pdf",
    "size": 4729968,
    "contentType": "application/octet-stream",
    "location": "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf"
}

```

Show More

The file has been uploaded to the storage object.

## [Step 6: Finalize the Attachment Status](#step-6-finalize-the-attachment-status)

Call [PATCH attachment](../http-docs/http-submittals-attachments-attachmentId-PATCH.md) with `isFileUploaded=true` to update the attachment status. This step marks the attachment as fully uploaded and ensures it is recognized as complete in the submittal workflow.

Use the `id` of the attachment generated in Step 2 and update the status.

### Request

```
curl -X PATCH 'https://developer.api.autodesk.com/construction/submittals/v2/projects/2570d4e5-9aef-4b41-8e45-a454f2f3fd65/items/938eb16d-5603-4df9-adcd-00f75d48e145/attachments/c14eabff-d79c-4429-9fa4-504a7aff7a37' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
          "isFileUploaded": true
      }'

```

### Response

```
{
    "id": "c14eabff-d79c-4429-9fa4-504a7aff7a37",
    "revisionFolderUrn": "urn:adsk.wipqa:fs.folder:co.TEK6K9PaSPqfowbE80rOJw",
    "permittedActions": [
        {
            "id": "Attachment::retrieve",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Attachment::partial_update",
            "fields": {
                "isFileUploaded": [
                    true
                ],
                "sendEmails": [
                    true,
                    false
                ]
            },
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Attachment::destroy",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Attachment::annotate",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        }
    ],
    "isFileUploaded": true,
    "url": null,
    "asyncState": "1",
    "createdBy": "MFEGJ9W5GGQL",
    "createdAt": "2024-11-09T19:39:28.779314Z",
    "updatedBy": "MFEGJ9W5GGQL",
    "updatedAt": "2024-11-09T20:02:12.315983Z",
    "name": "sbc1-file1.pdf",
    "uploadUrn": "urn:adsk.objects:os.object:wip.dm.prod/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf",
    "urn": null,
    "urnPage": null,
    "resourceUrns": null,
    "urnTypeId": "2",
    "urnVersion": null,
    "revision": 0,
    "itemId": "938eb16d-5603-4df9-adcd-00f75d48e145",
    "categoryId": "1",
    "taskId": null,
    "duplicatedFrom": null
}

```

Show More

Congratulations! You have successfully added a local attachment to a submittal item in Autodesk Construction Cloud. The attachment is now part of the submittal workflow and ready for further processing or review.
