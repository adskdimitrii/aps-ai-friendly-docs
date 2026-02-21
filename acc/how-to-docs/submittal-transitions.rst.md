# Manage Submittal Item Transitions

Source: https://aps.autodesk.com/en/docs/acc/tutorials/submittals/submittal-transitions.rst/

---

# Manage Submittal Item Transitions

This tutorial demonstrates how to transition submittal items through the submittal lifecycle for an Autodesk Construction Cloud (ACC) project.
The steps include verifying the userâs permissions and transitioning the submittal item to different states.

For more information about working with submittals, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Create_Submittal).

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps)
- Acquire a [3-legged OAuth token](/en/docs/oauth/v2/tutorials/get-3-legged-token/) with `data:read` `data:write` scopes.
- Verify that you have access to the relevant account and ACC project.
- Find the relevant project ID for the project you want to create an item in by following the [Retrieve an Account ID and Project ID](/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. In this example, assume the project ID is `91b5ea71-e3ea-495b-999d-57443a8af6a4`.
- Ensure you have assigned manager-level permissions to at least one user for the project via the UI. You will need to assign the submittal item to a user with manager-level permissions during the tutorial. For instructions on setting up roles and permissions see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittals_Permissions).
- This tutorial assumes an item was created in Submit state `sbc-1` by a user with manager permissions. For more information on creating a submittal item, see the [Create a Submittal Item](/en/docs/acc/v1/tutorials/submittals/create-submittal-item/) tutorial.
- This tutorial assumes that a review workflow has already been added to the item and that the workflow includes one step with one required task. Currently, the Submittals API does not support creating custom steps or tasks directly. The recommended approach is to associate the submittal item with a review template that already includes predefined steps and tasks. See the [Create Submittal Items](/en/docs/acc/v1/tutorials/submittals/create-submittal-item/#step-6-get-review-templates-optional) tutorial (step 6) for more details.
- Some transitions, such as transitioning to the Review (`rev`) state, require a custom identifier. For more information on custom numbering and retrieving the next sequential identifier, see Step 4 of the [Create a Submittal Item Tutorial](/en/docs/acc/v1/tutorials/submittals/create-submittal-item/).
- The Submittal Item workflow progresses through several sequential states. Below are the states in the UI and their equivalent API names:
    | UI State | API Name |
    | --- | --- |
    | Submit | `sbc-1` |
    | Prepare for Review | `mgr-1` |
    | Review | `rev` |
    | Close and Distribute | `mgr-2` |
    | Closed | `sbc-2` |

## [Step 1: Verify User Permissions](#step-1-verify-user-permissions)

Call [GET item](/en/docs/acc/v1/reference/http/submittals-items-itemId-GET/) using the project ID (`2570d4e5-9aef-4b41-8e45-a454f2f3fd65`) and the item ID (`2ae22463-83d2-4f1a-9b2f-6898e616bfc3`) to retrieve the relevant permissions for the user for the submttal item in Submit (`sbc-1`) state.

- Look for the `permittedActions` array in the response.
- Verify that the user can transition the submittal item by checking that the object with `id: "Item::wf_transition"` appears in this array.
- Find the relevant transition in the `transitions` array within this object (e.g., `"sbc-1::mgr-1"` for the `Submit to Manager` transition).
- You need to note two sets of mandatory fields for transitioning the submittal item:

> * General mandatory fields: These are listed under `"mandatoryFields"` in the object with `id: "Item::wf_transition"`.
> * Specific mandatory fields: These are listed under `"mandatoryFields"` in the `transitions` array for the specific transition (e.g., `"sbc-1::mgr-1"`).

Note that calling [GET item](/en/docs/acc/v1/reference/http/submittals-items-itemId-GET/) at any stage in the workflow will return the permitted actions for the user at that point in the workflow for that submittal item.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/2570d4e5-9aef-4b41-8e45-a454f2f3fd65/items/2ae22463-83d2-4f1a-9b2f-6898e616bfc3' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
  {
    "id": "2ae22463-83d2-4f1a-9b2f-6898e616bfc3",
    "identifier": 8,
    "typeId": "ffad8b30-0e5f-4767-aab5-4c17f88d91ef",
    "specId": "65bf7408-93f3-462e-84ab-17e5710c7536",
    "specIdentifier": "1",
    "specTitle": "1",
    "subsection": null,
    "title": "demo item workflow",
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
    "dueDate": "2024-11-21",
    "requiredOnJobDate": null,
    "leadTime": null,
    "requiredDate": null,
    "requiredApprovalDate": null,
    "submitterDueDate": "2024-11-21",
    "sentToSubmitter": "2024-11-05T14:24:21.242156Z",
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
    "folderUrn": "urn:adsk.wipqa:fs.folder:co.H8XWJqeLQjaYPigEYQwfQQ",
    "revisionsFoldersUrns": {
        "0": {
            "revision": 0,
            "folderUrn": "urn:adsk.wipqa:fs.folder:co.H8XWJqeLQjaYPigEYQwfQQ",
            "folderUrnCreatedAt": "2024-11-05 14:24:22.548713+00:00"
        }
    },
    "createdAt": "2024-11-05T14:24:21.245789Z",
    "createdBy": "MFEGJ9W5GGQL",
    "updatedAt": "2024-11-05T14:24:22.553907Z",
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
                "itemId",
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
                "itemId",
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
                "itemId",
                "body"
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
    "customIdentifier": "8",
    "customIdentifierHumanReadable": "8"
}

```

Show More

- Locate the `permittedActions` array.
- Within the `permittedActions` array, identify the object with `id: "Item::wf_transition"`. This object contains two types of mandatory fields:

> * General mandatory fields: Listed under the `mandatoryFields` property of the `Item::wf_transition` object itself. These apply to actions related to workflow transitions in general. This includes `stateId` - `mgr-1`. This indicates the target state.
> * Specific mandatory fields: Found within the `transitions` array inside the `Item::wf_transition` object. Each transition (e.g., `sbc-1::mgr-1`) includes its own `mandatoryFields` property that lists fields required specifically for that transition. This includes `manager` and `managerType`, which specify the manager assigned to the submittal and the type of manager.

## [Step 2: Transition the Submittal Item to Prepare for Review (mgr-1) State](#step-2-transition-the-submittal-item-to-prepare-for-review-mgr-1-state)

To promote the submittal item in the workflow and transition it from Submit (`sbc-1`) state to Prepare for Review (`mgr-1`) state, use [POST item:transition](/en/docs/acc/v1/reference/http/submittals-items-itemIdtransition-POST/).

Use the following mandatory values collected in Step 1:

- `stateId`: The target state ID (`mgr-1`).
- `manager`: The assigned managerâs ID (`MFEGJ9W5GGQL`).
- `managerType`: The type of manager (`1`).

### Request

```
curl -v 'https://developer.api.autodesk.com/constructoin/submittals/v2/projects/2570d4e5-9aef-4b41-8e45-a454f2f3fd65/items/2ae22463-83d2-4f1a-9b2f-6898e616bfc3:transition' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "stateId":"mgr-1",
        "manager":"MFEGJ9W5GGQL",
        "managerType":"1"
      }'

```

Show More

### Response

```
{
    "id": "2ae22463-83d2-4f1a-9b2f-6898e616bfc3",
    "identifier": 8,
    "typeId": "ffad8b30-0e5f-4767-aab5-4c17f88d91ef",
    "specId": "65bf7408-93f3-462e-84ab-17e5710c7536",
    "specIdentifier": "1",
    "specTitle": "1",
    "subsection": null,
    "title": "demo item workflow",
    "description": "this is a new description",
    "priority": "Normal",
    "revision": 0,
    "stateId": "mgr-1",
    "statusId": "2",
    "ballInCourt": [],
    "ballInCourtUsers": [
        "MFEGJ9W5GGQL"
    ],
    "ballInCourtCompanies": [],
    "ballInCourtRoles": [],
    "ballInCourtType": "manager",
    "manager": "MFEGJ9W5GGQL",
    "managerType": "1",
    "subcontractor": "MFEGJ9W5GGQL",
    "subcontractorType": "1",
    "watchers": [],
    "dueDate": null,
    "requiredOnJobDate": null,
    "leadTime": 14,
    "requiredDate": null,
    "requiredApprovalDate": null,
    "submitterDueDate": "2024-11-21",
    "sentToSubmitter": "2024-11-05T14:24:21.242156Z",
    "receivedFromSubmitter": "2024-11-05T14:50:09.304489Z",
    "submittedBy": "MFEGJ9W5GGQL",
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
    "folderUrn": "urn:adsk.wipqa:fs.folder:co.H8XWJqeLQjaYPigEYQwfQQ",
    "revisionsFoldersUrns": {
        "0": {
            "revision": 0,
            "folderUrn": "urn:adsk.wipqa:fs.folder:co.H8XWJqeLQjaYPigEYQwfQQ",
            "folderUrnCreatedAt": "2024-11-05 14:24:22.548713+00:00"
        }
    },
    "createdAt": "2024-11-05T14:24:21.245789Z",
    "createdBy": "MFEGJ9W5GGQL",
    "updatedAt": "2024-11-05T14:50:09.307266Z",
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
                "requiredOnJobDate": [],
                "requiredDate": [],
                "requiredApprovalDate": [],
                "leadTime": [],
                "mailNote": [],
                "sendEmails": [
                    true,
                    false
                ],
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
                "requiredOnJobDate": [],
                "requiredDate": [],
                "requiredApprovalDate": [],
                "leadTime": [],
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
                    "id": "mgr-1::sbc-2",
                    "name": "Close and distribute",
                    "stateFrom": {
                        "id": "mgr-1",
                        "name": "MGR 1"
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
                    "actionId": "ITEM_TRANSITION_MGR1_SBC2"
                },
                {
                    "id": "mgr-1::void",
                    "name": "Send to Void",
                    "stateFrom": {
                        "id": "mgr-1",
                        "name": "MGR 1"
                    },
                    "stateTo": {
                        "id": "void",
                        "name": "VOID"
                    },
                    "transitionFields": null,
                    "mandatoryFields": null,
                    "actionId": "ITEM_TRANSITION_MGR1_VOID"
                },
                {
                    "id": "mgr-1::sbc-1",
                    "name": "Return to Responsible Contractor",
                    "stateFrom": {
                        "id": "mgr-1",
                        "name": "MGR 1"
                    },
                    "stateTo": {
                        "id": "sbc-1",
                        "name": "SBC 1"
                    },
                    "transitionFields": [
                        "subcontractor",
                        "subcontractorType",
                        "submitterDueDate",
                        "mailNote"
                    ],
                    "mandatoryFields": [
                        "subcontractor",
                        "subcontractorType",
                        "submitterDueDate"
                    ],
                    "actionId": "ITEM_TRANSITION_MGR1_SBC1"
                },
                {
                    "id": "mgr-1::rev",
                    "name": "Submit to Review",
                    "stateFrom": {
                        "id": "mgr-1",
                        "name": "MGR 1"
                    },
                    "stateTo": {
                        "id": "rev",
                        "name": "REV"
                    },
                    "transitionFields": [
                        "watchers",
                        "stepDueDate",
                        "mailNote",
                        "saveAttachmentDrafts",
                        "duplicateAttachments",
                        "customIdentifier"
                    ],
                    "mandatoryFields": [
                        "customIdentifier"
                    ],
                    "actionId": "ITEM_TRANSITION_MGR1_REV"
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
                    "1",
                    "4"
                ]
            },
            "mandatoryFields": [
                "name",
                "itemId",
                "urnTypeId"
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
                "sendEmails": [
                    true,
                    false
                ],
                "isFileUploaded": [
                    true
                ],
                "categoryId": [
                    "1",
                    "4"
                ]
            },
            "mandatoryFields": [
                "name",
                "itemId",
                "urnTypeId"
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
    "customIdentifier": "8",
    "customIdentifierHumanReadable": "8"

}

```

Show More

The submittal item has transitioned to `mgr-1` state.

## [Step 3: Retrieve Details for Transition to Review (rev) State](#step-3-retrieve-details-for-transition-to-review-rev-state)

Before transitioning from Prepare for Review (`mgr-1`) state to Review (`rev`) state, you need to use the project ID and item ID to call [GET item](/en/docs/acc/v1/reference/http/submittals-items-itemId-GET/) to retrieve the information necessary for the transition (`mgr-1::rev`).

- Look for the `permittedActions` array in the response.
- Verify that the user can transition the submittal item by checking that the transition object appears (`id: Item::wf_transition`).
- Find the relevant transition in the transitions array (`Submit to Review - "mgr-1::rev"`).
- You need to note 2 sets of mandatory fields you will need to transition the submittals item:

> * The general mandatory fields (`"permittedActions"."mandatoryFields"`).
> * Mandatory fields for this transition (`permittedActions."id": "Item::wf_transition"."transitions"."mandatoryFields"`).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/2570d4e5-9aef-4b41-8e45-a454f2f3fd65/items/2ae22463-83d2-4f1a-9b2f-6898e616bfc3'
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
"id": "2ae22463-83d2-4f1a-9b2f-6898e616bfc3",
"stateId": "mgr-1",
// .....
"permittedActions": [
    {
        "id": "Item::wf_transition",
        "fields": {
            "stateId": [],
            // .....
        },
        "mandatoryFields": [
            "stateId"
        ],
        "transitions": [
            // .....
            {
                "id": "mgr-1::rev",
                "name": "Submit to Review",
                "stateFrom": {
                    "id": "mgr-1",
                    "name": "MGR 1"
                },
                "stateTo": {
                    "id": "rev",
                    "name": "REV"
                },
                "transitionFields": [
                    "watchers",
                    "stepDueDate",
                    "mailNote",
                    "saveAttachmentDrafts",
                    "duplicateAttachments",
                    "customIdentifier"
                ],
                "mandatoryFields": [
                    "customIdentifier"
                ],
                // .....
            }
        ]
    },
    // .....
]
}

```

Show More

Note the following values from the response, located within the `Item::wf_transition` object:

- General mandatory fields: These are listed under the `mandatoryFields` property of the `Item::wf_transition` object itself. For example, `stateId` indicates the target state (`rev` in this case).
- Specific mandatory fields for the transition `mgr-1::rev:` These are located in the `mandatoryFields` property within the relevant transition object in the `transitions` array. For example, `customIdentifier` is required for this specific transition.

## [Step 4: Transition to Review (rev) State](#step-4-transition-to-review-rev-state)

Use [POST item:transition](/en/docs/acc/v1/reference/http/submittals-items-itemIdtransition-POST/) to transition the submittal item to Review (`rev`) state, using the values retrieved in Step 3:

- `stateId`: The target state ID (`rev`).
- `customIdentifier`: A unique identifier for the item. You can set it either before or as part of the transition request. In this example, it was set beforehand when creating the item.

As mentioned earlier, this tutorial assumes the submittal item already has a review workflow (steps and tasks associated with the item). This is a prerequisite for transitioning the item to the `rev` state. Once transitioned, the first review step will turn `in-progress` and become active.

### Request

```
curl -v 'https://developer.api.autodesk.com/constructoin/submittals/v2/projects/2570d4e5-9aef-4b41-8e45-a454f2f3fd65/items/2ae22463-83d2-4f1a-9b2f-6898e616bfc3:transition' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "stateId": "rev"
      }'

```

### Response

```
{
    "id": "2ae22463-83d2-4f1a-9b2f-6898e616bfc3",
    "identifier": 8,
    "typeId": "ffad8b30-0e5f-4767-aab5-4c17f88d91ef",
    "specId": "65bf7408-93f3-462e-84ab-17e5710c7536",
    "specIdentifier": "1",
    "specTitle": "1",
    "subsection": null,
    "title": "demo item workflow",
    "description": "this is a new description",
    "priority": "Normal",
    "revision": 0,
    "stateId": "rev",
    "statusId": "2",
    "ballInCourt": [],
    "ballInCourtUsers": [
        "MFEGJ9W5GGQL"
    ],
    "ballInCourtCompanies": [],
    "ballInCourtRoles": [],
    "ballInCourtType": "reviewer",
    "manager": "MFEGJ9W5GGQL",
    "managerType": "1",
    "subcontractor": "MFEGJ9W5GGQL",
    "subcontractorType": "1",
    "watchers": [],
    "dueDate": "2024-11-19",
    "requiredOnJobDate": null,
    "leadTime": 14,
    "requiredDate": null,
    "requiredApprovalDate": null,
    "submitterDueDate": "2024-11-21",
    "sentToSubmitter": "2024-11-05T14:58:25.743021Z",
    "receivedFromSubmitter": "2024-11-05T14:59:34.283317Z",
    "submittedBy": "MFEGJ9W5GGQL",
    "managerDueDate": null,
    "sentToReview": "2024-11-05T15:27:54.708226Z",
    "sentToReviewBy": "MFEGJ9W5GGQL",
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
    "folderUrn": "urn:adsk.wipqa:fs.folder:co.H8XWJqeLQjaYPigEYQwfQQ",
    "revisionsFoldersUrns": {
        "0": {
            "revision": 0,
            "folderUrn": "urn:adsk.wipqa:fs.folder:co.H8XWJqeLQjaYPigEYQwfQQ",
            "folderUrnCreatedAt": "2024-11-05 14:24:22.548713+00:00"
        }
    },
    "createdAt": "2024-11-05T14:24:21.245789Z",
    "createdBy": "MFEGJ9W5GGQL",
    "updatedAt": "2024-11-05T15:27:54.769126Z",
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
                "title": [],
                "description": [],
                "packageId": [],
                "specId": [],
                "subsection": [],
                "typeId": [],
                "priority": [],
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
                "requiredOnJobDate": [],
                "requiredDate": [],
                "requiredApprovalDate": [],
                "leadTime": [],
                "sendEmails": [
                    true,
                    false
                ],
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
                "requiredOnJobDate": [],
                "requiredDate": [],
                "requiredApprovalDate": [],
                "leadTime": [],
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
                    "id": "rev::sbc-2",
                    "name": "Close and distribute",
                    "stateFrom": {
                        "id": "rev",
                        "name": "REV"
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
                    "actionId": "ITEM_TRANSITION_REV_SBC2"
                },
                {
                    "id": "rev::void",
                    "name": "Send to Void",
                    "stateFrom": {
                        "id": "rev",
                        "name": "REV"
                    },
                    "stateTo": {
                        "id": "void",
                        "name": "VOID"
                    },
                    "transitionFields": null,
                    "mandatoryFields": null,
                    "actionId": "ITEM_TRANSITION_REV_VOID"
                },
                {
                    "id": "rev::mgr-1",
                    "name": "Return to Manager",
                    "stateFrom": {
                        "id": "rev",
                        "name": "REV"
                    },
                    "stateTo": {
                        "id": "mgr-1",
                        "name": "MGR 1"
                    },
                    "transitionFields": [
                        "manager",
                        "managerType",
                        "mailNote"
                    ],
                    "mandatoryFields": [
                        "manager",
                        "managerType"
                    ],
                    "actionId": "ITEM_TRANSITION_REV_MGR1"
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
                "taskId": [],
                "categoryId": [
                    "4"
                ]
            },
            "mandatoryFields": [
                "urnTypeId",
                "itemId",
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
                "itemId",
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
                "itemId",
                "body"
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
    "customIdentifier": "8",
    "customIdentifierHumanReadable": "8"
}

```

Show More

Note the `stateId` which is now in the Review (`rev`) state.

## [Step 5: Retrieve the Review Task and Step IDs](#step-5-retrieve-the-review-task-and-step-ids)

Once transitioned to the Review (`rev`) state, the first review step and task will start and become `in-progress`.

In submittals, a task represents a specific review action within a step. Each task corresponds to a review being carried out, with details about the assigned reviewer provided for context. The main objective of this step is to retrieve the Step ID and Task ID required to perform actions in later steps (e.g., submitting the reviewerâs review in Step 7).

Additionally, the API identifies `Task::close` in the `permittedActions` array, defining the allowed action for submitting the reviewerâs review. This action requires specific fields, such as `responseId`, to be provided in [POST task/:id:close](/en/docs/acc/v1/reference/http/submittals-tasks-taskIdclose-POST/), ensuring the review is submitted and the workflow progresses.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/2570d4e5-9aef-4b41-8e45-a454f2f3fd65/items/2ae22463-83d2-4f1a-9b2f-6898e616bfc3/steps' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
   "pagination":{
      "limit":100,
      "offset":0,
      "totalResults":1
   },
   "results":[
      {
         "id":"e00a643d-e862-4be1-a6a3-aaa6acb118f0",
         "itemId":"2ae22463-83d2-4f1a-9b2f-6898e616bfc3",
         "status":"in-progress",
         "stepNumber":1,
         "daysToRespond":14,
         "dueDate":"2024-11-19",
         "startedAt":"2024-11-05T15:27:54.711930Z",
         "completedAt":null,
         "tasks":[
            {
               "id":"00369989-8bf3-4ed2-beaf-99352393688c",
               "stepId":"e00a643d-e862-4be1-a6a3-aaa6acb118f0",
               "createdBy":"MFEGJ9W5GGQL",
               "createdAt":"2024-11-05T15:01:37.224027Z",
               "updatedBy":"MFEGJ9W5GGQL",
               "updatedAt":"2024-11-05T15:27:54.761120Z",
               "status":"in-progress",
               "assignedTo":"MFEGJ9W5GGQL",
               "assignedToType":"1",
               "isRequired":true,
               "stepDueDate":"2024-11-19",
               "responseComment":null,
               "respondedAt":null,
               "respondedBy":null,
               "startedAt":"2024-11-05T15:27:54.761112Z",
               "completedAt":null,
               "completedBy":null,
               "responseId":null,
               "permittedActions":[
                  {
                     "id":"Task::retrieve",
                     "fields":{

                     },
                     "mandatoryFields":[

                     ],
                     "transitions":[

                     ]
                  },
                  {
                     "id":"Task::partial_update",
                     "fields":{
                        "startedAt":[

                        ]
                     },
                     "mandatoryFields":[

                     ],
                     "transitions":[

                     ]
                  },
                  {
                     "id":"Task::close",
                     "fields":{
                        "responseComment":[

                        ],
                        "responseId":[

                        ],
                        "saveAttachmentDrafts":[

                        ],
                        "duplicateAttachments":[

                        ]
                     },
                     "mandatoryFields":[
                        "responseId"
                     ],
                     "transitions":[

                     ]
                  }
               ]
            }
         ],
         "createdBy":"MFEGJ9W5GGQL",
         "createdAt":"2024-11-05T15:01:37.222541Z",
         "updatedBy":"MFEGJ9W5GGQL",
         "updatedAt":"2024-11-05T15:27:54.712353Z",
         "permittedActions":[
            {
               "id":"Step::retrieve",
               "fields":{

               },
               "mandatoryFields":[

               ],
               "transitions":[

               ]
            },
            {
               "id":"Step::partial_update",
               "fields":{
                  "daysToRespond":[

                  ],
                  "startedAt":[

                  ],
                  "dueDate":[

                  ]
               },
               "mandatoryFields":[

               ],
               "transitions":[

               ]
            },
            {
               "id":"Task::list",
               "fields":{

               },
               "mandatoryFields":[

               ],
               "transitions":[

               ]
            },
            {
               "id":"Step::overwrite_step",
               "fields":{
                  "tasks":[

                  ]
               },
               "mandatoryFields":[
                  "tasks"
               ],
               "transitions":[

               ]
            }
         ]
      }
   ]
}

```

Show More

Note the following:

- Step ID (`results.id`): `e00a643d-e862-4be1-a6a3-aaa6acb118f0` - identifies the review step.
- Task ID (`results.tasks.id`): `00369989-8bf3-4ed2-beaf-99352393688c` - identifies the active task for the review.
- Mandatory Fields for Task Closure: Within the `permittedActions` array, locate the object with `id: "Task::close"`. The `mandatoryFields` property of this object lists the required fields. For example, `responseId` is required to submit the reviewerâs review.
- `Task::close` Action: This action allows the reviewer to submit their review, transitioning the taskâs status from `in-progress` to `completed` within the review workflow. The `responseId` field is mandatory for this action, as described in Step 7.
- Assigned Reviewer (`results.tasks.assignedTo`): The `assignedTo` field (`MFEGJ9W5GGQL`) provides the user ID of the reviewer.

## [Step 6: Retrieve the List of Possible Responses](#step-6-retrieve-the-list-of-possible-responses)

To complete the review, the reviewer must submit a response. Use [GET responses](/en/docs/acc/v1/reference/http/submittals-responses-GET/) to fetch the available options.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/2570d4e5-9aef-4b41-8e45-a454f2f3fd65/responses' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
    "pagination": {
        "limit": 20,
        "offset": 0,
        "totalResults": 5
    },
    "results": [
        {
            "id": "38ffb07d-d734-4aa6-bbf4-cb121c56972f",
            "key": "approved",
            "value": "Approved",
            "platformId": "approved",
            "categoryId": "1",
            "isApproval": true,
            "isActive": true,
            "isInUse": true,
            "createdAt": "2024-05-12T10:38:33.147339Z",
            "createdBy": "",
            "updatedAt": "2024-05-12T10:38:40.346414Z",
            "updatedBy": ""
        },
        {
            "id": "85bd95d5-84d8-4b55-a5c1-fb507ca2146c",
            "key": "approved_as_noted",
            "value": "Approved as noted",
            "platformId": "approved_as_noted",
            "categoryId": "1",
            "isApproval": true,
            "isActive": true,
            "isInUse": true,
            "createdAt": "2024-05-12T10:38:33.147401Z",
            "createdBy": "",
            "updatedAt": "2024-05-12T10:38:40.346414Z",
            "updatedBy": ""
        },
        {
            "id": "9ca0466e-8007-496e-afd4-22272b4dec26",
            "key": "for_record_only",
            "value": "For record only",
            "platformId": "for_record_only",
            "categoryId": "1",
            "isApproval": true,
            "isActive": true,
            "isInUse": false,
            "createdAt": "2024-05-12T10:38:33.147443Z",
            "createdBy": "",
            "updatedAt": "2024-05-12T10:38:40.346414Z",
            "updatedBy": ""
        },
        {
            "id": "d1001860-da66-4ea3-b704-52c669fdb5e3",
            "key": "rejected",
            "value": "Rejected",
            "platformId": "rejected",
            "categoryId": "2",
            "isApproval": false,
            "isActive": true,
            "isInUse": false,
            "createdAt": "2024-05-12T10:38:33.147523Z",
            "createdBy": "",
            "updatedAt": "2024-05-12T10:38:40.346414Z",
            "updatedBy": ""
        },
        {
            "id": "20dcd972-39e3-4e6b-9326-5a928efbdc25",
            "key": "revise_and_resubmit",
            "value": "Revise and resubmit",
            "platformId": "revise_and_resubmit",
            "categoryId": "3",
            "isApproval": false,
            "isActive": true,
            "isInUse": false,
            "createdAt": "2024-05-12T10:38:33.147483Z",
            "createdBy": "",
            "updatedAt": "2024-05-12T10:38:40.346414Z",
            "updatedBy": ""
        }
    ]
}

```

Show More

Select the appropriate Response ID (`results.id`) to complete the review in the next step. For example, `38ffb07d-d734-4aa6-bbf4-cb121c56972f` for `Approved`.

## [Step 7: Submit the Reviewerâs Review](#step-7-submit-the-reviewers-review)

The reviewer submits a review by adding the selected response using [POST task/:id:close](/en/docs/acc/v1/reference/http/submittals-tasks-taskIdclose-POST/).

As seen in Step 5, the `Task::close` permitted action requires the `responseId` field, and optionally, a `responseComment` can be included. When the last required task in a review step is submitted, the item transitions to the next step. If this is the final review step in the Review (`rev`) state, the workflow automatically advances to the Close and Distribute (`mgr-2`) state.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/2570d4e5-9aef-4b41-8e45-a454f2f3fd65/items/2ae22463-83d2-4f1a-9b2f-6898e616bfc3/steps/e00a643d-e862-4be1-a6a3-aaa6acb118f0/tasks/00369989-8bf3-4ed2-beaf-99352393688c:close' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
      {
          "responseId": "38ffb07d-d734-4aa6-bbf4-cb121c56972f",
          "responseComment": "reviewed and approved"

      }'

```

Show More

### Response

```
{
    "id": "00369989-8bf3-4ed2-beaf-99352393688c",
    "stepId": "e00a643d-e862-4be1-a6a3-aaa6acb118f0",
    "createdBy": "MFEGJ9W5GGQL",
    "createdAt": "2024-11-05T15:01:37.224027Z",
    "updatedBy": "MFEGJ9W5GGQL",
    "updatedAt": "2024-11-05T15:49:22.929427Z",
    "status": "completed",
    "assignedTo": "MFEGJ9W5GGQL",
    "assignedToType": "1",
    "isRequired": true,
    "stepDueDate": "2024-11-19",
    "responseComment": "reviewed and approved",
    "respondedAt": "2024-11-05T15:49:22.928729Z",
    "respondedBy": "MFEGJ9W5GGQL",
    "startedAt": "2024-11-05T15:38:39.271240Z",
    "completedAt": "2024-11-05T15:49:22.928729Z",
    "completedBy": "MFEGJ9W5GGQL",
    "responseId": "38ffb07d-d734-4aa6-bbf4-cb121c56972f",
    "permittedActions": [
        {
            "id": "Task::retrieve",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Task::partial_update",
            "fields": {
                "startedAt": [],
                "completedAt": []
            },
            "mandatoryFields": [],
            "transitions": []
        }
    ]
}

```

Show More

Note that the `status` field in the Task model is now updated to `completed`, indicating that the reviewer has submitted their review. This action transitions the workflow to the next step, as appropriate.

## [Step 8: Transition to Close and Distribute (mgr-2)](#step-8-transition-to-close-and-distribute-mgr-2)

After each reviewer completes their assigned task (representing their review), the system transitions the workflow automatically to the Close and Distribute (`mgr-2`) state. To confirm the transition or check for additional tasks or steps, start by calling [GET steps](en/docs/acc/v1/reference/http/submittals-steps-GET/). This will verify whether there are any remaining tasks or review steps.

Once you confirm that all tasks and review steps are complete, use [GET item](/en/docs/acc/v1/reference/http/submittals-items-itemId-GET/) to verify the submittalâs overall state and retrieve the permitted actions required for transitioning to the Closed (`sbc-2`) state.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/2570d4e5-9aef-4b41-8e45-a454f2f3fd65/items/2ae22463-83d2-4f1a-9b2f-6898e616bfc3' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
    "id": "2ae22463-83d2-4f1a-9b2f-6898e616bfc3",
    "identifier": 8,
    "typeId": "ffad8b30-0e5f-4767-aab5-4c17f88d91ef",
    "specId": "65bf7408-93f3-462e-84ab-17e5710c7536",
    "specIdentifier": "1",
    "specTitle": "1",
    "subsection": null,
    "title": "demo item workflow",
    "description": "this is a new description",
    "priority": "Normal",
    "revision": 0,
    "stateId": "mgr-2",
    "statusId": "2",
    "ballInCourt": [],
    "ballInCourtUsers": [
        "MFEGJ9W5GGQL"
    ],
    "ballInCourtCompanies": [],
    "ballInCourtRoles": [],
    "ballInCourtType": "manager",
    "manager": "MFEGJ9W5GGQL",
    "managerType": "1",
    "subcontractor": "MFEGJ9W5GGQL",
    "subcontractorType": "1",
    "watchers": [],
    "dueDate": null,
    "requiredOnJobDate": null,
    "leadTime": 14,
    "requiredDate": null,
    "requiredApprovalDate": null,
    "submitterDueDate": "2024-11-21",
    "sentToSubmitter": "2024-11-05T14:58:25.743021Z",
    "receivedFromSubmitter": "2024-11-05T14:59:34.283317Z",
    "submittedBy": "MFEGJ9W5GGQL",
    "managerDueDate": null,
    "sentToReview": "2024-11-05T15:38:39.224037Z",
    "sentToReviewBy": "MFEGJ9W5GGQL",
    "receivedFromReview": "2024-11-05T15:49:23.059642Z",
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
    "folderUrn": "urn:adsk.wipqa:fs.folder:co.H8XWJqeLQjaYPigEYQwfQQ",
    "revisionsFoldersUrns": {
        "0": {
            "revision": 0,
            "folderUrn": "urn:adsk.wipqa:fs.folder:co.H8XWJqeLQjaYPigEYQwfQQ",
            "folderUrnCreatedAt": "2024-11-05 14:24:22.548713+00:00"
        }
    },
    "createdAt": "2024-11-05T14:24:21.245789Z",
    "createdBy": "MFEGJ9W5GGQL",
    "updatedAt": "2024-11-05T15:49:23.062527Z",
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
                "responseId": [],
                "responseComment": [],
                "mailNote": [],
                "sendEmails": [
                    true,
                    false
                ],
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
                "responseId": [],
                "responseComment": [],
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
                    "id": "mgr-2::sbc-2",
                    "name": "Close and distribute",
                    "stateFrom": {
                        "id": "mgr-2",
                        "name": "MGR 2"
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
                    "actionId": "ITEM_TRANSITION_MGR2_SBC2"
                },
                {
                    "id": "mgr-2::void",
                    "name": "Send to Void",
                    "stateFrom": {
                        "id": "mgr-2",
                        "name": "MGR 2"
                    },
                    "stateTo": {
                        "id": "void",
                        "name": "VOID"
                    },
                    "transitionFields": null,
                    "mandatoryFields": null,
                    "actionId": "ITEM_TRANSITION_MGR2_VOID"
                },
                {
                    "id": "mgr-2::rev",
                    "name": "Return for Review",
                    "stateFrom": {
                        "id": "mgr-2",
                        "name": "MGR 2"
                    },
                    "stateTo": {
                        "id": "rev",
                        "name": "REV"
                    },
                    "transitionFields": [
                        "watchers",
                        "stepDueDate",
                        "mailNote"
                    ],
                    "mandatoryFields": [
                        "stepDueDate"
                    ],
                    "actionId": "ITEM_TRANSITION_MGR2_REV"
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
                "name",
                "itemId",
                "urnTypeId"
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
                "name",
                "itemId",
                "urnTypeId"
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
                "itemId",
                "body"
            ],
            "transitions": []
        }
    ],
    "customIdentifier": "8",
    "customIdentifierHumanReadable": "8"
}

```

Show More

Note the following:

- State ID: `mgr-2` confirms that the submittal is in the Close and Distribute state, indicating readiness for the next transition.
- Permitted Actions: The `permittedActions` array includes the transition with `id='mgr-2::sbc-2'`. Ensure that this transition is listed and note the required field, such as `responseId`, which is mandatory for progressing to the Closed (`sbc-2`) state.

## [Step 9: Close the Submittal Item](#step-9-close-the-submittal-item)

To close the submittal item, transition it to the Closed (`sbc-2`) state using [POST item:transition](/en/docs/acc/v1/reference/http/submittals-items-itemIdtransition-POST/). See Step 6 for the required `responseId`.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/2570d4e5-9aef-4b41-8e45-a454f2f3fd65/items/2ae22463-83d2-4f1a-9b2f-6898e616bfc3:transition' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
      {
          "stateId": "sbc-2",
          "responseComment": "final response",
          "responseId": "38ffb07d-d734-4aa6-bbf4-cb121c56972f"
      }'

```

Show More

### Response

```
{
    "id": "2ae22463-83d2-4f1a-9b2f-6898e616bfc3",
    "identifier": 8,
    "typeId": "ffad8b30-0e5f-4767-aab5-4c17f88d91ef",
    "specId": "65bf7408-93f3-462e-84ab-17e5710c7536",
    "specIdentifier": "1",
    "specTitle": "1",
    "subsection": null,
    "title": "demo item workflow",
    "description": "this is a new description",
    "priority": "Normal",
    "revision": 0,
    "stateId": "sbc-2",
    "statusId": "3",
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
    "dueDate": null,
    "requiredOnJobDate": null,
    "leadTime": 14,
    "requiredDate": null,
    "requiredApprovalDate": null,
    "submitterDueDate": "2024-11-21",
    "sentToSubmitter": "2024-11-05T14:58:25.743021Z",
    "receivedFromSubmitter": "2024-11-05T14:59:34.283317Z",
    "submittedBy": "MFEGJ9W5GGQL",
    "managerDueDate": null,
    "sentToReview": "2024-11-05T15:38:39.224037Z",
    "sentToReviewBy": "MFEGJ9W5GGQL",
    "receivedFromReview": "2024-11-05T15:49:23.059642Z",
    "publishedDate": "2024-11-05T16:21:20.386996Z",
    "publishedBy": "MFEGJ9W5GGQL",
    "responseId": "38ffb07d-d734-4aa6-bbf4-cb121c56972f",
    "responseComment": "final response",
    "respondedAt": "2024-11-05T16:21:20.388Z",
    "respondedBy": "MFEGJ9W5GGQL",
    "packageId": null,
    "packageIdentifier": null,
    "packageTitle": null,
    "packageSpecIdentifier": null,
    "folderUrn": "urn:adsk.wipqa:fs.folder:co.H8XWJqeLQjaYPigEYQwfQQ",
    "revisionsFoldersUrns": {
        "0": {
            "revision": 0,
            "folderUrn": "urn:adsk.wipqa:fs.folder:co.H8XWJqeLQjaYPigEYQwfQQ",
            "folderUrnCreatedAt": "2024-11-05 14:24:22.548713+00:00"
        }
    },
    "createdAt": "2024-11-05T14:24:21.245789Z",
    "createdBy": "MFEGJ9W5GGQL",
    "updatedAt": "2024-11-05T16:21:20.390193Z",
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
                "sendEmails": [
                    true,
                    false
                ],
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
                "requiredDate": [],
                "requiredApprovalDate": [],
                "requiredOnJobDate": [],
                "leadTime": [],
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
                    "id": "sbc-2::mgr-2",
                    "name": "Reopen to Manager",
                    "stateFrom": {
                        "id": "sbc-2",
                        "name": "SBC 2"
                    },
                    "stateTo": {
                        "id": "mgr-2",
                        "name": "MGR 2"
                    },
                    "transitionFields": null,
                    "mandatoryFields": null,
                    "actionId": "ITEM_TRANSITION_SBC2_MGR2"
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
        }
    ],
    "customIdentifier": "8",
    "customIdentifierHumanReadable": "8"
}

```

Show More

- The `stateId` is now `sbc-2`, confirming the submittal has transitioned to the Closed state.
- The `statusId` is `3`, indicating that the submittal item is officially closed and the workflow is complete.

Congratulations! You have successfully transitioned submittal items through their lifecycle in ACC.
