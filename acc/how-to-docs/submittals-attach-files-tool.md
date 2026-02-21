# Attach Files From the ACC Files Tool to Submittals

Source: https://aps.autodesk.com/en/docs/acc/tutorials/submittals/attach-files-tool/

---

# Attach Files From the ACC Files Tool to Submittals

This tutorial demonstrates how to attach files from the ACC Files tool to a submittal item.

The steps include verifying the user permissions and gathering required fields for attaching the file, finding the folder containing the file in ACC Files, finding the version ID of the file you want to attach, and attaching the file to a submittal item. For information about uploading files to the ACC Files tool, see the [Upload Files to the ACC Files Tool](/en/docs/acc/v1/tutorials/files/upload-document-s3/) tutorial.

ACC files are stored in the Data Management service. To access the files, you need to [provision access](https://get-started.aps.autodesk.com/#provision-access-in-other-products) to the Data Management API.

For information about attaching local files to submittals, see the [Attach Local Files to a Submittal Item](/en/docs/acc/v1/tutorials/attach-local-files) tutorial.

For more information about working with submittals, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Create_Submittal).

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps)
- Acquire a [3-legged OAuth token](/en/docs/oauth/v2/tutorials/get-3-legged-token/) with `data:read` `data:write` scopes.
- This tutorial assumes an item was created in Submit state `sbc-1` by a user with manager permissions. For more information on creating a submittal item, see the [Create a Submittal Item](/en/docs/acc/v1/tutorials/submittals/create-submittal-item/) tutorial. In this example, assume the submittal item ID is `463c0b75-7c85-43ce-aa9f-74781aa29070`.
- Verify that you have access to the relevant account and ACC project.
- Find the relevant account ID and project ID for the account and project that contains the file you want to attach to a submittal item. See the [Retrieve an Account ID and Project ID](/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial for more details. In this example, assume the account ID (hub ID) is `b.43939999-0bf2-490d-8e4a-c1cb1097125c`, and project ID is `b.55451d9a-b6a5-429d-8bc3-6074765c52e0`.
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

You should first verify that the user has permissions to add an attachment to a submittal item and gather the mandatory and optional fields required when calling the add attachment endpoint ([POST attachment](/en/docs/acc/v1/reference/http/submittals-attachments-POST/)) in step 6.

Call [GET item](/en/docs/acc/v1/reference/http/submittals-items-itemId-GET/) using the project ID (`55451d9a-b6a5-429d-8bc3-6074765c52e0`) and the submittal item ID (`463c0b75-7c85-43ce-aa9f-74781aa29070`). Check the `permittedActions` object for `Attachment::create`. If this action is listed, the user has permission to create an attachment.

The `permittedActions` object also provides the `mandatoryFields` and `fields` arrays, which specify the required and optional parameters for the POST attachments request. Calling [GET item](/en/docs/acc/v1/reference/http/submittals-items-itemId-GET/) at any stage in the workflow will return the permitted actions for the user at that point for the submittal item.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/55451d9a-b6a5-429d-8bc3-6074765c52e0/items/463c0b75-7c85-43ce-aa9f-74781aa29070' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
  {
    "id": "463c0b75-7c85-43ce-aa9f-74781aa29070",
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

Note the following fields that are relevant for calling POST attachments in step 5:

- Mandatory Fields:

> * Locate the `permittedActions` object with `"id": "Attachment::create"`. The `mandatoryFields` array specifies the required fields for creating an attachment:
> + `name`: The name of the attachment.
> + `urnTypeId`: The type of object being referenced. This field must always be included, and its value should always be `2`.

- Optional Fields:

> * Under the same `"id": "Attachment::create"` entry, the `fields` array lists optional parameters:
> + `categoryId`: Links the attachment to a specific workflow state.
> + `urn`: The version ID of the file being attached.
> + `isFileUploaded`: Set to `true` if the file has already been uploaded in the ACC Files tool.

## [Step 2: Find the Folder ID](#step-2-find-the-folder-id)

When we attach the file to a submittal item we will need to provide the version ID of the file that was uploaded to the ACC Files tool. To find the version ID we need to use several [Data Management API](/en/docs/data/v2/developers_guide/overview/).

Note that the ACC account ID corresponds to a Data Management hub ID. To convert an account ID into a hub ID you need to add a `b.` prefix. For example, an account ID of `c8b0c73d-3ae9` translates to a hub ID of `b.c8b0c73d-3ae9`.

Note that an account in Data Management is called a hub.

Use the account ID (hub ID) (`b.43939999-0bf2-490d-8e4a-c1cb1097125c`) and the project ID (`b.55451d9a-b6a5-429d-8bc3-6074765c52e0`) to call [GET topFolders](/en/docs/data/v2/reference/http/hubs-hub_id-projects-project_id-topFolders-GET/) to get the top-level folders for the project. For details about retrieving account and project IDs, see the [Retrieve an Account ID and Project ID](/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial.

### Request

```
curl 'https://developer.api.autodesk.com/project/v1/hubs/b.43939999-0bf2-490d-8e4a-c1cb1097125c/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/topFolders' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \

```

### Response

```
{
    "jsonapi": {
        "version": "1.0"
    },
    "links": {
        "self": {
            "href": "https://developer.api.autodesk.com/project/v1/hubs/b.43939999-0bf2-490d-8e4a-c1cb1097125c/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/topFolders"
        }
    },
    "data": [
        {
            "type": "folders",
            "id": "urn:adsk.wipprod:fs.folder:co.-jRpdNhnTAGQPdWTHOqE4w",
            "attributes": {
                "name": "Project Files",
                "displayName": "Project Files",
                "createTime": "2023-12-20T09:05:26.0000000Z",
                "createUserId": "",
                "createUserName": "",
                "lastModifiedTime": "2024-11-14T11:24:38.0000000Z",
                "lastModifiedUserId": "5UNGP2KZFCVW",
                "lastModifiedUserName": "User Name",
                "lastModifiedTimeRollup": "2024-11-14T11:26:11.0000000Z",
                "objectCount": 2,
                "hidden": false,
                "extension": {
                    "type": "folders:autodesk.bim360:Folder",
                    "version": "1.0",
                    "schema": {
                        "href": "https://developer.api.autodesk.com/schema/v1/versions/folders:autodesk.bim360:Folder-1.0"
                    },
                    "data": {
                        "visibleTypes": [
                            "items:autodesk.bim360:File"
                        ],
                        "actions": [
                            "CONVERT"
                        ],
                        "allowedTypes": [
                            "items:autodesk.bim360:File",
                            "folders:autodesk.bim360:Folder"
                        ],
                        "isRoot": true,
                        "folderType": "normal",
                        "namingStandardIds": []
                    }
                }
            },
            "links": {
                "self": {
                    "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/folders/urn:adsk.wipprod:fs.folder:co.-jRpdNhnTAGQPdWTHOqE4w"
                },
                "webView": {
                    "href": "https://acc.autodesk.com/docs/files/projects/55451d9a-b6a5-429d-8bc3-6074765c52e0?folderUrn=urn%3Aadsk.wipprod%3Afs.folder%3Aco.-jRpdNhnTAGQPdWTHOqE4w"
                }
            },
            "relationships": {
                "contents": {
                    "links": {
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/folders/urn:adsk.wipprod:fs.folder:co.-jRpdNhnTAGQPdWTHOqE4w/contents"
                        }
                    }
                },
                "parent": {
                    "data": {
                        "type": "folders",
                        "id": "urn:adsk.wipprod:fs.folder:co.3RgCRi8cTgO4ofr_6qbtJw"
                    },
                    "links": {
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/folders/urn:adsk.wipprod:fs.folder:co.-jRpdNhnTAGQPdWTHOqE4w/parent"
                        }
                    }
                },
                "refs": {
                    "links": {
                        "self": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/folders/urn:adsk.wipprod:fs.folder:co.-jRpdNhnTAGQPdWTHOqE4w/relationships/refs"
                        },
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/folders/urn:adsk.wipprod:fs.folder:co.-jRpdNhnTAGQPdWTHOqE4w/refs"
                        }
                    }
                },
                "links": {
                    "links": {
                        "self": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/folders/urn:adsk.wipprod:fs.folder:co.-jRpdNhnTAGQPdWTHOqE4w/relationships/links"
                        }
                    }
                }
            }
        }
    ]
}

```

Show More

Assume that the file is in the `Project Files` folder (`data.attributes.name`), and note the folder ID (`data.id`) - `urn:adsk.wipprod:fs.folder:co.-jRpdNhnTAGQPdWTHOqE4w`

If you want to attach a file from a folder nested under the `Project Files` folder, you need to call [GET projects/:project_id/folders/:folder_id/contents](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET) repeatedly through the hierarchy of folders until you find the Folder ID of the folder you want to attach to the submittal item. For the first iteration, use the `Project Files` ID (`urn:adsk.wipprod:fs.folder:co.-jRpdNhnTAGQPdWTHOqE4w`).

## [Step 3: Find the Version ID for the File](#step-3-find-the-version-id-for-the-file)

Use the project ID (`b.55451d9a-b6a5-429d-8bc3-6074765c52e0`) and the `Project Files` folder ID (`urn:adsk.wipprod:fs.folder:co.-jRpdNhnTAGQPdWTHOqE4w`) to call [GET contents](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET/) to get the version ID for the file.

### Request

```
curl 'https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/folders/urn:adsk.wipprod:fs.folder:co.-jRpdNhnTAGQPdWTHOqE4w/contents' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \

```

### Response

```
{
    "jsonapi": {
        "version": "1.0"
    },
    "links": {
        "self": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/folders/urn:adsk.wipprod:fs.folder:co.-jRpdNhnTAGQPdWTHOqE4w/contents"
        }
    },
    "data": [
        {
            "type": "items",
            "id": "urn:adsk.wipprod:dm.lineage:g2vEflLTS86eDc1Jx2GJJg",
            "attributes": {
                "displayName": "ElectricalPlan_S456_Rev02.pdf",
                "createTime": "2024-11-02T13:59:09.0000000Z",
                "createUserId": "5UNGP2KZFCVW",
                "createUserName": "User Name",
                "lastModifiedTime": "2024-11-02T13:59:09.0000000Z",
                "lastModifiedUserId": "5UNGP2KZFCVW",
                "lastModifiedUserName": "User Name",
                "hidden": false,
                "reserved": false,
                "extension": {
                    "type": "items:autodesk.bim360:File",
                    "version": "1.0",
                    "schema": {
                        "href": "https://developer.api.autodesk.com/schema/v1/versions/items:autodesk.bim360:File-1.0"
                    },
                    "data": {
                        "sourceFileName": "ElectricalPlan_S456_Rev02.pdf"
                    }
                }
            },
            "links": {
                "self": {
                    "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/items/urn:adsk.wipprod:dm.lineage:g2vEflLTS86eDc1Jx2GJJg"
                },
                "webView": {
                    "href": "https://acc.autodesk.com/docs/files/projects/55451d9a-b6a5-429d-8bc3-6074765c52e0?folderUrn=urn%3Aadsk.wipprod%3Afs.folder%3Aco.-jRpdNhnTAGQPdWTHOqE4w&entityId=urn%3Aadsk.wipprod%3Adm.lineage%3Ag2vEflLTS86eDc1Jx2GJJg"
                }
            },
            "relationships": {
                "tip": {
                    "data": {
                        "type": "versions",
                        "id": "urn:adsk.wipprod:fs.file:vf.g2vEflLTS86eDc1Jx2GJJg?version=1"
                    },
                    "links": {
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/items/urn:adsk.wipprod:dm.lineage:g2vEflLTS86eDc1Jx2GJJg/tip"
                        }
                    }
                },
                "versions": {
                    "links": {
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/items/urn:adsk.wipprod:dm.lineage:g2vEflLTS86eDc1Jx2GJJg/versions"
                        }
                    }
                },
                "parent": {
                    "data": {
                        "type": "folders",
                        "id": "urn:adsk.wipprod:fs.folder:co.-jRpdNhnTAGQPdWTHOqE4w"
                    },
                    "links": {
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/items/urn:adsk.wipprod:dm.lineage:g2vEflLTS86eDc1Jx2GJJg/parent"
                        }
                    }
                },
                "refs": {
                    "links": {
                        "self": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/items/urn:adsk.wipprod:dm.lineage:g2vEflLTS86eDc1Jx2GJJg/relationships/refs"
                        },
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/items/urn:adsk.wipprod:dm.lineage:g2vEflLTS86eDc1Jx2GJJg/refs"
                        }
                    }
                },
                "links": {
                    "links": {
                        "self": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/items/urn:adsk.wipprod:dm.lineage:g2vEflLTS86eDc1Jx2GJJg/relationships/links"
                        }
                    }
                }
            }
        },
        {
            "type": "items",
            "id": "urn:adsk.wipprod:dm.lineage:CcDVL-XYTzK-n6GYP0r0kw",
            "attributes": {
                "displayName": "ElectricalPlan_S456_Rev03.pdf",
                "createTime": "2024-11-14T11:24:38.0000000Z",
                "createUserId": "5UNGP2KZFCVW",
                "createUserName": "User Name",
                "lastModifiedTime": "2024-11-14T11:24:39.0000000Z",
                "lastModifiedUserId": "5UNGP2KZFCVW",
                "lastModifiedUserName": "User Name",
                "hidden": false,
                "reserved": false,
                "extension": {
                    "type": "items:autodesk.bim360:File",
                    "version": "1.0",
                    "schema": {
                        "href": "https://developer.api.autodesk.com/schema/v1/versions/items:autodesk.bim360:File-1.0"
                    },
                    "data": {
                        "sourceFileName": "ElectricalPlan_S456_Rev03.pdf.pdf"
                    }
                }
            },
            "links": {
                "self": {
                    "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/items/urn:adsk.wipprod:dm.lineage:CcDVL-XYTzK-n6GYP0r0kw"
                },
                "webView": {
                    "href": "https://acc.autodesk.com/docs/files/projects/55451d9a-b6a5-429d-8bc3-6074765c52e0?folderUrn=urn%3Aadsk.wipprod%3Afs.folder%3Aco.-jRpdNhnTAGQPdWTHOqE4w&entityId=urn%3Aadsk.wipprod%3Adm.lineage%3ACcDVL-XYTzK-n6GYP0r0kw"
                }
            },
            "relationships": {
                "tip": {
                    "data": {
                        "type": "versions",
                        "id": "urn:adsk.wipprod:fs.file:vf.CcDVL-XYTzK-n6GYP0r0kw?version=1"
                    },
                    "links": {
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/items/urn:adsk.wipprod:dm.lineage:CcDVL-XYTzK-n6GYP0r0kw/tip"
                        }
                    }
                },
                "versions": {
                    "links": {
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/items/urn:adsk.wipprod:dm.lineage:CcDVL-XYTzK-n6GYP0r0kw/versions"
                        }
                    }
                },
                "parent": {
                    "data": {
                        "type": "folders",
                        "id": "urn:adsk.wipprod:fs.folder:co.-jRpdNhnTAGQPdWTHOqE4w"
                    },
                    "links": {
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/items/urn:adsk.wipprod:dm.lineage:CcDVL-XYTzK-n6GYP0r0kw/parent"
                        }
                    }
                },
                "refs": {
                    "links": {
                        "self": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/items/urn:adsk.wipprod:dm.lineage:CcDVL-XYTzK-n6GYP0r0kw/relationships/refs"
                        },
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/items/urn:adsk.wipprod:dm.lineage:CcDVL-XYTzK-n6GYP0r0kw/refs"
                        }
                    }
                },
                "links": {
                    "links": {
                        "self": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/items/urn:adsk.wipprod:dm.lineage:CcDVL-XYTzK-n6GYP0r0kw/relationships/links"
                        }
                    }
                }
            }
        }
    ],
    "included": [
        {
            "type": "versions",
            "id": "urn:adsk.wipprod:fs.file:vf.g2vEflLTS86eDc1Jx2GJJg?version=1",
            "attributes": {
                "name": "ElectricalPlan_S456_Rev02.pdf",
                "displayName": "ElectricalPlan_S456_Rev02.pdf",
                "createTime": "2024-11-02T13:59:09.0000000Z",
                "createUserId": "5UNGP2KZFCVW",
                "createUserName": "User Name",
                "lastModifiedTime": "2024-11-02T14:00:35.0000000Z",
                "lastModifiedUserId": "5UNGP2KZFCVW",
                "lastModifiedUserName": "User Name",
                "versionNumber": 1,
                "storageSize": 56295,
                "fileType": "pdf",
                "extension": {
                    "type": "versions:autodesk.bim360:File",
                    "version": "1.0",
                    "schema": {
                        "href": "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.bim360:File-1.0"
                    },
                    "data": {
                        "processState": "PROCESSING_COMPLETE",
                        "extractionState": "SUCCESS",
                        "splittingState": "NOT_SPLIT",
                        "reviewState": "NOT_IN_REVIEW",
                        "revisionDisplayLabel": "1",
                        "sourceFileName": "ElectricalPlan_S456_Rev02.pdf",
                        "conformingStatus": "NONE"
                    }
                }
            },
            "links": {
                "self": {
                    "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/versions/urn:adsk.wipprod:fs.file:vf.g2vEflLTS86eDc1Jx2GJJg%3Fversion=1"
                },
                "webView": {
                    "href": "https://acc.autodesk.com/docs/files/projects/55451d9a-b6a5-429d-8bc3-6074765c52e0?folderUrn=urn%3Aadsk.wipprod%3Afs.folder%3Aco.-jRpdNhnTAGQPdWTHOqE4w&entityId=urn%3Aadsk.wipprod%3Afs.file%3Avf.g2vEflLTS86eDc1Jx2GJJg%3Fversion%3D1"
                }
            },
            "relationships": {
                "item": {
                    "data": {
                        "type": "items",
                        "id": "urn:adsk.wipprod:dm.lineage:g2vEflLTS86eDc1Jx2GJJg"
                    },
                    "links": {
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/versions/urn:adsk.wipprod:fs.file:vf.g2vEflLTS86eDc1Jx2GJJg%3Fversion=1/item"
                        }
                    }
                },
                "links": {
                    "links": {
                        "self": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/versions/urn:adsk.wipprod:fs.file:vf.g2vEflLTS86eDc1Jx2GJJg%3Fversion=1/relationships/links"
                        }
                    }
                },
                "refs": {
                    "links": {
                        "self": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/versions/urn:adsk.wipprod:fs.file:vf.g2vEflLTS86eDc1Jx2GJJg%3Fversion=1/relationships/refs"
                        },
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/versions/urn:adsk.wipprod:fs.file:vf.g2vEflLTS86eDc1Jx2GJJg%3Fversion=1/refs"
                        }
                    }
                },
                "downloadFormats": {
                    "links": {
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/versions/urn:adsk.wipprod:fs.file:vf.g2vEflLTS86eDc1Jx2GJJg%3Fversion=1/downloadFormats"
                        }
                    }
                },
                "derivatives": {
                    "data": {
                        "type": "derivatives",
                        "id": "dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLmcydkVmbExUUzg2ZURjMUp4MkdKSmc_dmVyc2lvbj0x"
                    },
                    "meta": {
                        "link": {
                            "href": "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLmcydkVmbExUUzg2ZURjMUp4MkdKSmc_dmVyc2lvbj0x/manifest?scopes=b360project.55451d9a-b6a5-429d-8bc3-6074765c52e0,O2tenant.3077712"
                        }
                    }
                },
                "thumbnails": {
                    "data": {
                        "type": "thumbnails",
                        "id": "dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLmcydkVmbExUUzg2ZURjMUp4MkdKSmc_dmVyc2lvbj0x"
                    },
                    "meta": {
                        "link": {
                            "href": "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLmcydkVmbExUUzg2ZURjMUp4MkdKSmc_dmVyc2lvbj0x/thumbnail?scopes=b360project.55451d9a-b6a5-429d-8bc3-6074765c52e0,O2tenant.3077712"
                        }
                    }
                },
                "storage": {
                    "data": {
                        "type": "objects",
                        "id": "urn:adsk.objects:os.object:wip.dm.prod/135415a1-5283-4ffe-98bd-645c65abca74.pdf"
                    },
                    "meta": {
                        "link": {
                            "href": "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/135415a1-5283-4ffe-98bd-645c65abca74.pdf?scopes=b360project.55451d9a-b6a5-429d-8bc3-6074765c52e0,O2tenant.3077712"
                        }
                    }
                }
            }
        },
        {
            "type": "versions",
            "id": "urn:adsk.wipprod:fs.file:vf.CcDVL-XYTzK-n6GYP0r0kw?version=1",
            "attributes": {
                "name": "ElectricalPlan_S456_Rev03.pdf",
                "displayName": "ElectricalPlan_S456_Rev03.pdf",
                "createTime": "2024-11-14T11:24:38.0000000Z",
                "createUserId": "5UNGP2KZFCVW",
                "createUserName": "User Name",
                "lastModifiedTime": "2024-11-14T11:26:11.0000000Z",
                "lastModifiedUserId": "5UNGP2KZFCVW",
                "lastModifiedUserName": "User Name",
                "versionNumber": 1,
                "storageSize": 4729756,
                "fileType": "pdf",
                "extension": {
                    "type": "versions:autodesk.bim360:File",
                    "version": "1.0",
                    "schema": {
                        "href": "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.bim360:File-1.0"
                    },
                    "data": {
                        "processState": "PROCESSING_COMPLETE",
                        "extractionState": "SUCCESS",
                        "splittingState": "NOT_SPLIT",
                        "reviewState": "NOT_IN_REVIEW",
                        "revisionDisplayLabel": "1",
                        "sourceFileName": "ElectricalPlan_S456_Rev03.pdf",
                        "conformingStatus": "NONE"
                    }
                }
            },
            "links": {
                "self": {
                    "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/versions/urn:adsk.wipprod:fs.file:vf.CcDVL-XYTzK-n6GYP0r0kw%3Fversion=1"
                },
                "webView": {
                    "href": "https://acc.autodesk.com/docs/files/projects/55451d9a-b6a5-429d-8bc3-6074765c52e0?folderUrn=urn%3Aadsk.wipprod%3Afs.folder%3Aco.-jRpdNhnTAGQPdWTHOqE4w&entityId=urn%3Aadsk.wipprod%3Afs.file%3Avf.CcDVL-XYTzK-n6GYP0r0kw%3Fversion%3D1"
                }
            },
            "relationships": {
                "item": {
                    "data": {
                        "type": "items",
                        "id": "urn:adsk.wipprod:dm.lineage:CcDVL-XYTzK-n6GYP0r0kw"
                    },
                    "links": {
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/versions/urn:adsk.wipprod:fs.file:vf.CcDVL-XYTzK-n6GYP0r0kw%3Fversion=1/item"
                        }
                    }
                },
                "links": {
                    "links": {
                        "self": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/versions/urn:adsk.wipprod:fs.file:vf.CcDVL-XYTzK-n6GYP0r0kw%3Fversion=1/relationships/links"
                        }
                    }
                },
                "refs": {
                    "links": {
                        "self": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/versions/urn:adsk.wipprod:fs.file:vf.CcDVL-XYTzK-n6GYP0r0kw%3Fversion=1/relationships/refs"
                        },
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/versions/urn:adsk.wipprod:fs.file:vf.CcDVL-XYTzK-n6GYP0r0kw%3Fversion=1/refs"
                        }
                    }
                },
                "downloadFormats": {
                    "links": {
                        "related": {
                            "href": "https://developer.api.autodesk.com/data/v1/projects/b.55451d9a-b6a5-429d-8bc3-6074765c52e0/versions/urn:adsk.wipprod:fs.file:vf.CcDVL-XYTzK-n6GYP0r0kw%3Fversion=1/downloadFormats"
                        }
                    }
                },
                "derivatives": {
                    "data": {
                        "type": "derivatives",
                        "id": "dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLkNjRFZMLVhZVHpLLW42R1lQMHIwa3c_dmVyc2lvbj0x"
                    },
                    "meta": {
                        "link": {
                            "href": "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLkNjRFZMLVhZVHpLLW42R1lQMHIwa3c_dmVyc2lvbj0x/manifest?scopes=b360project.55451d9a-b6a5-429d-8bc3-6074765c52e0,O2tenant.3077712"
                        }
                    }
                },
                "thumbnails": {
                    "data": {
                        "type": "thumbnails",
                        "id": "dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLkNjRFZMLVhZVHpLLW42R1lQMHIwa3c_dmVyc2lvbj0x"
                    },
                    "meta": {
                        "link": {
                            "href": "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLkNjRFZMLVhZVHpLLW42R1lQMHIwa3c_dmVyc2lvbj0x/thumbnail?scopes=b360project.55451d9a-b6a5-429d-8bc3-6074765c52e0,O2tenant.3077712"
                        }
                    }
                },
                "storage": {
                    "data": {
                        "type": "objects",
                        "id": "urn:adsk.objects:os.object:wip.dm.prod/bb29d020-e4d2-49c9-a240-5bb99cba9cef.pdf"
                    },
                    "meta": {
                        "link": {
                            "href": "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/bb29d020-e4d2-49c9-a240-5bb99cba9cef.pdf?scopes=b360project.55451d9a-b6a5-429d-8bc3-6074765c52e0,O2tenant.3077712"
                        }
                    }
                }
            }
        }
    ]
}

```

Show More

In this example, assume that `ElectricalPlan_S456_Rev02.pdf` is the file that you want to attach.

Find the file (`included.attributes.name`), and note the version ID `urn:adsk.wipprod:fs.file:vf.g2vEflLTS86eDc1Jx2GJJg?version=1`.

## [Step 4: Attach the File to the Submittal Item](#step-4-attach-the-file-to-the-submittal-item)

Call [POST attachment](/en/docs/acc/v1/reference/http/submittals-attachments-POST/) to attach the file identified in the previous steps to the specified submittal item. This registers the file within the submittal workflow..

The request must include the following fields:

- `name`: The name of the file attachment.
- `urn`: The version ID of the file (`urn:adsk.wipprod:fs.file:vf.g2vEflLTS86eDc1Jx2GJJg?version=1`) obtained in Step 3.
- `urnTypeId`: This must always have the value `2`.
- `isFileUploaded`: Set to `true`.

The following fields are optional:

- The `categoryId` is typically assigned automatically based on the submittal itemâs current state. In most cases, you do not need to include `categoryId` in your request. However, for specific exceptions, you must provide it explicitly:

> * Prepare for Review (`mgr-1`): By default, when the submittal item is in the Prepare for Review state, the `categoryId` is assigned automatically as `2` (for-review). If you want the attachment to be tagged as a Submit state attachment instead, you must explicitly set `categoryId` to `1` in the request.
> * Final Response Attachments: If you are closing a submittal item from a state other than Close and Distribute (`mgr-2`), and you want the attachment to be marked as a final response, explicitly set `categoryId` to `4`.

- For items in the Review (`rev`) state, include the `taskId` field to associate the attachment with a specific task. This ensures the attachment is linked to the relevant task in the review process.

You can retrieve the full list of available `categoryId` values and their corresponding meanings by calling [GET metadata](/en/docs/acc/v1/reference/http/submittals-metadata-GET/), and reviewing the `attachmentCategories` list in the response.

### Request

```
curl -X POST "https://developer.api.autodesk.com/submittals/v2/projects/55451d9a-b6a5-429d-8bc3-6074765c52e0/items/463c0b75-7c85-43ce-aa9f-74781aa29070/attachments" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a" \
-d '{
       "name":"testprojectFile.pdf",
       "urnTypeId":"2",
       "urn": "urn:adsk.wipprod:fs.file:vf.g2vEflLTS86eDc1Jx2GJJg?version=1",
       "isFileUploaded": true
    }'

```

Show More

### Response

```
{
    "id": "6817093b-6cc8-4d15-9144-f037aff242d1",
    "revisionFolderUrn": "urn:adsk.wipprod:fs.folder:co.3H_1wW5WSj-_IRJK3vIYwg",
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
            "id": "Attachment::annotate",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        },
        {
            "id": "Attachment::destroy",
            "fields": {},
            "mandatoryFields": [],
            "transitions": []
        }
    ],
    "isFileUploaded": true,
    "url": null,
    "asyncState": "1",
    "createdBy": "5UNGP2KZFCVW",
    "createdAt": "2024-12-11T07:26:08.856233Z",
    "updatedBy": "5UNGP2KZFCVW",
    "updatedAt": "2024-12-11T07:26:08.856244Z",
    "name": "testprojectFile.pdf",
    "uploadUrn": "urn:adsk.objects:os.object:wip.dm.prod/6f8a103e-2f3a-4b39-ab2e-446ecb03c441.pdf",
    "urn": "urn:adsk.wipprod:fs.file:vf.g2vEflLTS86eDc1Jx2GJJg?version=1",
    "urnPage": null,
    "resourceUrns": null,
    "urnTypeId": "2",
    "urnVersion": null,
    "revision": 2,
    "itemId": "463c0b75-7c85-43ce-aa9f-74781aa29070",
    "categoryId": "2",
    "taskId": null,
    "duplicatedFrom": null
}

```

Show More

Once the request is completed successfully, the response will include the attachment ID, name, and other metadata, confirming that the file has been linked to the submittal item.

Congratulations, You have added an attachment to a submittal item from the ACC Files tool.
