# Create Submittal Items

Source: https://aps.autodesk.com/en/docs/acc/tutorials/submittals/create-submittal-item/

---

# Create Submittal Items

This tutorial demonstrates how to create a submittal item for an Autodesk Construction Cloud (ACC) project. The steps include verifying the userâs permissions, retrieving the item type ID, finding or creating the spec ID, optionally setting a custom number for the new item, identifying the assigneeâs ID, and creating the item. For more information on working with submittals, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Create_Submittal).

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:read` `data:write` scopes.
- Verify that you have access to the relevant account and ACC project.
- Find the relevant project ID for the project you want to create an item in by following the [Retrieve an Account ID and Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the project ID is `91b5ea71-e3ea-495b-999d-57443a8af6a4`.
- Make sure you have chosen at least one âmanagerâ through the UI. To assign a manager to a submittal item, you need to ensure the user has the necessary permissions and roles set within the project. For instructions on setting up roles and permissions see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittals_Permissions).

## [Step 1: Verify User Permissions](#step-1-verify-user-permissions)

Call [GET users/me](../http-docs/http-submittals-users-me-GET.md) using the project ID (`91b5ea71-e3ea-495b-999d-57443a8af6a4`) to retrieve the relevant permissions for the user.

You need to check whether the user has permissions to create submittal items, and the states in which the user is allowed to create them. Only a manager (`role[i]=1`) can create an item in a Waiting for submission state (`sbc-1`), and any user can create a submittal item in an Open (Submitted) state (`mgr-1`). Check the `transitions` array for the data.

Use the `permittedActions` array to check which fields are mandatory (`mandatoryFields`) and which fields are optional (`fields`) for the state in which you want to create the submittal item. For example, to create a submittal Waiting for submission state (`sbc-1`), the required fields include subcontractor (`subcontractor`), subcontractor type (`subcontractorType`), and submitter due date (`submitterDueDate`). To create a submittal in an Open (Submitted) state (`mgr-1`), the required fields include manager (`manager`) and manager type (`managerType`).

Note that calling [GET items](../http-docs/http-submittals-items-GET.md) at any stage in the workflow will return the permitted actions for the user at that point in the workflow for that submittal item.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/91b5ea71-e3ea-495b-999d-57443a8af6a4/users/me' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
  {
  "id": "MFEGJ9W5GGQL",
  "roles": [
    "1",
    "2",
    "4"
  ],
  "permittedActions": [
    {
      "id": "Spec::list",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Spec::retrieve",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Spec::create",
      "fields": {
        "id": [],
        "title": [],
        "identifier": []
      },
      "mandatoryFields": [
        "title",
        "identifier"
      ],
      "transitions": []
    },
    {
      "id": "Spec::partial_update",
      "fields": {
        "title": [],
        "identifier": []
      },
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Spec::destroy",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Item::list",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Item::bulk_partial_update",
      "fields": {
        "subcontractor": [],
        "subcontractorType": [],
        "submitterDueDate": [],
        "manager": [],
        "managerType": [],
        "managerDueDate": [],
        "typeId": [],
        "packageId": [],
        "priority": [],
        "specId": [],
        "watchers": []
      },
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Item::xlsx_export",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Item::create",
      "fields": {
        "stateId": [],
        "id": [],
        "specId": [],
        "subsection": [],
        "title": [],
        "description": [],
        "packageId": [],
        "typeId": [],
        "priority": [],
        "watchers": [],
        "requiredOnJobDate": [],
        "leadTime": [],
        "requiredDate": [],
        "requiredApprovalDate": [],
        "customIdentifier": [],
        "templateId": []
      },
      "mandatoryFields": [
        "stateId",
        "specId",
        "title",
        "typeId"
      ],
      "transitions": [
        {
          "id": "create::sbc-1",
          "name": "Create",
          "stateFrom": {
            "id": "create",
            "name": "Create"
          },
          "stateTo": {
            "id": "sbc-1",
            "name": "SBC 1"
          },
          "transitionFields": [
            "subcontractor",
            "subcontractorType",
            "submitterDueDate"
          ],
          "mandatoryFields": [
            "subcontractor",
            "subcontractorType",
            "submitterDueDate"
          ],
          "actionId": "ITEM_TRANSITION_CREATE_SBC1"
        },
        {
          "id": "create::draft",
          "name": "Create draft",
          "stateFrom": {
            "id": "create",
            "name": "Create"
          },
          "stateTo": {
            "id": "draft",
            "name": "DRAFT"
          },
          "transitionFields": [
            "subcontractor",
            "subcontractorType",
            "submitterDueDate",
            "manager",
            "managerType",
            "sentToSubmitter",
            "receivedFromSubmitter",
            "managerDueDate",
            "sentToReview",
            "receivedFromReview",
            "publishedDate"
          ],
          "mandatoryFields": null,
          "actionId": null
        }
      ]
    },
    {
      "id": "Item::import",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Item::bulk_destroy",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Item::bulk_apply_template",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Item::bulk_add_custom_identifier",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Item::bulk_wf_transition",
      "fields": {},
      "mandatoryFields": [],
      "transitions": [
        {
          "id": "draft::sbc-1",
          "name": "Assign to Responsible Contractor",
          "stateFrom": {
            "id": "draft",
            "name": "DRAFT"
          },
          "stateTo": {
            "id": "sbc-1",
            "name": "SBC 1"
          },
          "transitionFields": [
            "subcontractor",
            "subcontractorType",
            "submitterDueDate"
          ],
          "mandatoryFields": [
            "subcontractor",
            "subcontractorType",
            "submitterDueDate"
          ],
          "actionId": "ITEM_TRANSITION_DRAFT_SBC1"
        },
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
            "manager"
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
            "submitterDueDate"
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
      "id": "AdminMapping::list",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "AdminMapping::create",
      "fields": {
        "container": [],
        "oxygenId": [],
        "userType": [],
        "submittalsRole": [
          "1",
          "2"
        ]
      },
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "AdminMapping::destroy",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Package::retrieve",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Package::list",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Package::partial_update",
      "fields": {
        "description": [],
        "title": []
      },
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Package::add_items_to_package",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Package::destroy",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Package::create",
      "fields": {
        "title": [],
        "identifier": [],
        "description": [],
        "specId": []
      },
      "mandatoryFields": [
        "specId",
        "title"
      ],
      "transitions": []
    },
    {
      "id": "DefaultValues::retrieve",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "DefaultValues::partial_update",
      "fields": {
        "reviewTime": [],
        "manager": [],
        "watchers": []
      },
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "ItemResponse::list",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "ItemResponse::retrieve",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "ItemResponse::create",
      "fields": {
        "value": [],
        "categoryId": [
          "1",
          "2",
          "3"
        ],
        "isActive": [
          true,
          false
        ]
      },
      "mandatoryFields": [
        "value",
        "categoryId"
      ],
      "transitions": []
    },
    {
      "id": "ItemResponse::partial_update",
      "fields": {
        "value": [],
        "isActive": [
          true,
          false
        ],
        "categoryId": [
          "1",
          "2",
          "3"
        ]
      },
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "ItemType::list",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "ItemType::retrieve",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "ItemType::create",
      "fields": {
        "value": [],
        "isActive": [
          true,
          false
        ]
      },
      "mandatoryFields": [
        "value"
      ],
      "transitions": []
    },
    {
      "id": "ItemType::partial_update",
      "fields": {
        "value": [],
        "isActive": [
          true,
          false
        ]
      },
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Template::list",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Template::retrieve",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Template::destroy",
      "fields": {},
      "mandatoryFields": [],
      "transitions": []
    },
    {
      "id": "Template::create",
      "fields": {
        "name": [],
        "steps": [],
        "watchers": []
      },
      "mandatoryFields": [
        "name",
        "steps"
      ],
      "transitions": []
    },
    {
      "id": "Template::partial_update",
      "fields": {
        "name": [],
        "steps": [],
        "watchers": []
      },
      "mandatoryFields": [],
      "transitions": []
    }
  ]
}

```

Show More

Note the permissions information in the `roles` array and `permittedActions` array.

## [Step 2: Find or Create the Spec Section ID](#step-2-find-or-create-the-spec-section-id)

Every submittal item must be associated with a spec section. When creating a submittal item you need to either select an exising spec section or create a new spec section.

To retrieve an existing spec section ID, use the project ID (`91b5ea71-e3ea-495b-999d-57443a8af6a4`) to call [GET specs](../http-docs/http-submittals-specs-GET.md).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/91b5ea71-e3ea-495b-999d-57443a8af6a4/specs?limit=50' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 50,
    "offset": 0,
    "totalResults": 70,
    "nextUrl": "https://developer.api.autodesk.com/construction/submittals/v2/projects/91b5ea71-e3ea-495b-999d-57443a8af6a4/specs?limit=50&offset=50&sort=identifier+desc"
  },
  "results": [
    {
      "id": "000ce2cf-4fce-4c84-b993-5068889f8ff8",
      "createdBy": "YSZ8KJBCDY4E",
      "createdAt": "2024-03-20T14:54:23.135846Z",
      "updatedBy": "YSZ8KJBCDY4E",
      "updatedAt": "2024-03-20T14:54:50.297761Z",
      "title": "spec1",
      "identifier": "11"
    },
    {
      "id": "ae1e343d-2249-451e-86ec-954c0d81cc72",
      "createdBy": "YSZ8KJBCDY4E",
      "createdAt": "2024-01-31T15:19:37.685444Z",
      "updatedBy": "YSZ8KJBCDY4E",
      "updatedAt": "2024-03-20T14:54:50.297761Z",
      "title": "spec2",
      "identifier": "22"
    }
  ]
}

```

Show More

Note the spec section ID (`id`).

If you want to create a new spec section, call [POST specs](../http-docs/http-submittals-specs-POST.md). Specify the spec title and identifier in the request.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/91b5ea71-e3ea-495b-999d-57443a8af6a4/specs' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "identifier": "111",
        "title": "my-spec"
      }'

```

### Response

```
{
  "id": "ec3d1e29-4431-452b-8257-15ad0817a730",
  "createdBy": "MFEGJ9W5GGQL",
  "createdAt": "2024-04-09T07:29:34.357926Z",
  "updatedBy": "MFEGJ9W5GGQL",
  "updatedAt": "2024-04-09T07:29:34.357942Z",
  "title": "my-spec",
  "identifier": "111"
}

```

Show More

Note the spec section ID (`id`).

## [Step 3: Find the Item Type ID](#step-3-find-the-item-type-id)

Every submittal item must be associated with an item type. To get a list of existing item types, use the project ID (`91b5ea71-e3ea-495b-999d-57443a8af6a4`) to call [GET item-types](../http-docs/http-submittals-item-types-GET.md).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/91b5ea71-e3ea-495b-999d-57443a8af6a4/item-types' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 100,
    "offset": 0,
    "totalResults": 15
  },
  "results": [
    {
      "id": "530dbe26-6799-413c-9015-937ecfebe0e8",
      "key": "attic_stock",
      "value": "Attic Stock",
      "platformId": "attic_stock",
      "isActive": true,
      "isInUse": false,
      "createdAt": "2024-01-30T09:38:56.374093Z",
      "createdBy": "",
      "updatedAt": "2024-01-30T09:39:25.832679Z",
      "updatedBy": ""
    },
    {
      "id": "010bde2c-4d4d-41c7-84cb-0c26d50c0158",
      "key": "samples",
      "value": "Samples",
      "platformId": "samples",
      "isActive": true,
      "isInUse": false,
      "createdAt": "2024-01-30T09:38:56.374093Z",
      "createdBy": "",
      "updatedAt": "2024-01-30T09:38:56.374093Z",
      "updatedBy": ""
    },
  ]
}

```

Show More

Note the item type ID (`results[id]`) of the relevant item type.

## [Step 4: Select a Custom Submittal Item Number (Optional)](#step-4-select-a-custom-submittal-item-number-optional)

When you create a submittal item you can optionally assign a custom number to it. Note that only managers can assign custom numbers to a submittal item. Projects are configured to either assign a sequential global number to the submittal items or a sequential spec number. For more details about custom numbering, see the Custom Numbering in Submittals [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Custom_Numbering). Alternatively, you can customize the submittal item custom number to be any string that has not yet been assigned to a submittal item, as long it is in a supported format.

If you want to assign the next global or spec number you need to first check the sequence type. To find the sequence type call [GET metadata](../http-docs/http-submittals-metadata-GET.md), and check the `customIdentifierSequenceType` field. If the sequence type is `1` it is a global sequence (global numbering), and if it is `2` it is a spec sequence (spec section numbering).

In this example, assume the project has been assigned a spec sequence. Note that a spec sequence is in the format <spec_identifier>-<sequential_number>. You only need to specify the sequential number. The full number - <spec_identifier>-<sequential_number> - appears in the response payload in the `customIdentifierHumanReadable` attribute.

To find the next number in the sequence, call [GET items:next-custom-identifier](../http-docs/http-submittals-itemsnext-custom-identifier-GET.md).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/91b5ea71-e3ea-495b-999d-57443a8af6a4/items:next-custom-identifier?specId=6468e125-0b48-484c-b871-319d1695edbe' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "previousCustomIdentifier":"110",
  "nextCustomIdentifier":"111"
}

```

Note the `nextCustomIdentifier`.

If you want to assign any customized number to the submittal item we recommend that you validate it to check that it is unique and that is in a supported format. Call [POST items:validate-custom-identifier](../http-docs/http-submittals-itemsvalidate-custom-identifier-POST.md) to validate the number.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/91b5ea71-e3ea-495b-999d-57443a8af6a4/items:validate-custom-identifier?specId=6468e125-0b48-484c-b871-319d1695edbe' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "customIdentifier":"8787e78e7"
      }'

```

### Response
> 204 no-content

If the provided `customIdentifier` is already in use or does not meet the field requirements, an error will be returned.

## [Step 5: Link a Manager to the Submittal Item](#step-5-link-a-manager-to-the-submittal-item)

A manager must be associated with the submittal item. If the submittal item creator is a manager then you do not need to assign a manager to the submittal item. See step 1 for details about checking whether the user is a manager. If the user is not a manager, you need to assign the submittal item to a manager.

To find the list of managers associated with a project, call [GET mappings](../http-docs/http-submittals-mappings-GET.md). This returns a list of all the users, roles, and companies that are managers in the project. `userType` indicates whether it is a user, role, or company. If a user is a manager, call [GET projects/users](../http-docs/http-admin-projectsprojectId-users-GET.md) to verify the actual name of the user. If a copmany is a manager, call [GET companies](../http-docs/http-projects--project_id-companies-GET.md) to verify the actual name of the company. Note that we do not currently support verifying names of roles.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/91b5ea71-e3ea-495b-999d-57443a8af6a4/settings/mappings?limit=200' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 100,
    "offset": 0,
    "totalResults": 1
  },
  "results": [
    {
      "id": "c4feff3c-3d3c-480d-b155-2288f005cd35",
      "createdBy": "MFEGJ9W5GGQL",
      "createdAt": "2024-01-30T10:00:27.207533Z",
      "updatedBy": "MFEGJ9W5GGQL",
      "updatedAt": "2024-01-30T10:00:27.207552Z",
      "oxygenId": "WBGQM228YWFQ",
      "userType": "1",
      "submittalsRole": "1"
    }
  ]
}

```

Show More

## [Step 6: Get Review Templates (Optional)](#step-6-get-review-templates-optional)

In the submittal item workflow, review steps and tasks must be added before transitioning the item to the Review (`rev`) state. Currently, the Submittals API does not support creating custom steps or tasks directly. Instead, the recommended approach is to associate the submittal item with a review template that already includes predefined steps and tasks.

You can retrieve a list of review templates using [GET templates](../http-docs/http-submittals-templates-GET.md), then assign one to the submittal item during creation. This ensures that the necessary steps and tasks are included for managing the submittal lifecycle effectively. For details on retrieving and assigning review templates, see the request/response example in this step and the instructions in Step 7.

You can use [GET templates](../http-docs/http-submittals-templates-GET.md) to verify the steps and tasks associated with a template. This provides details such as step numbers, days to respond, and assigned reviewers.

In this example, we retrieve a review template and use its ID in the next step to assign it to a submittal item.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/91b5ea71-e3ea-495b-999d-57443a8af6a4/templates?limit=200' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 200,
    "offset": 0,
    "totalResults": 4
  },
  "results": [
    {
        "id": "8af9317c-dc73-4cf4-8085-9601bb96219e",
        "name": "template1",
        "steps": [
            {
                "id": "3099a035-f6ee-41ed-a384-12f23b4d0fcc",
                "stepNumber": 1,
                "daysToRespond": 14,
                "tasks": [
                    {
                        "id": "73f459eb-3cc1-403a-abea-182bb9ecae95",
                        "assignedTo": "MFEGJ9W5GGQL",
                        "assignedToType": "1",
                        "isRequired": true
                    },
                    {
                        "id": "5f23fa24-e15b-462e-a4b4-081b004221c3",
                        "assignedTo": "WBGQM228YWFQ",
                        "assignedToType": "1",
                        "isRequired": true
                    },
                    {
                        "id": "a45807f1-d252-43c1-826f-e746caf07c8b",
                        "assignedTo": "150468349",
                        "assignedToType": "2",
                        "isRequired": false
                    }
                ]
            }
        ],
        "createdAt": "2024-02-15T15:58:22.294867Z",
        "createdBy": "MFEGJ9W5GGQL",
        "updatedAt": "2024-02-15T18:01:23.783098Z",
        "updatedBy": "MFEGJ9W5GGQL",
        "watchers": [
            {
                "id": "MFEGJ9W5GGQL",
                "userType": "1"
            }
        ]
    },
    {
        "id": "3c9d83d6-84bf-4682-a945-41459c6f5582",
        "name": "template2",
        "steps": [
            {
                "id": "721de5a2-f255-46bb-bcfd-69692cbb8fd9",
                "stepNumber": 1,
                "daysToRespond": 8,
                "tasks": [
                    {
                        "id": "0c794baf-96a2-4be5-ab8e-1e65a0922dbe",
                        "assignedTo": "WBGQM228YWFQ",
                        "assignedToType": "1",
                        "isRequired": true
                    },
                    {
                        "id": "8fc546e8-19bf-44fa-a000-f16810fbd542",
                        "assignedTo": "MFEGJ9W5GGQL",
                        "assignedToType": "1",
                        "isRequired": true
                    },
                    {
                        "id": "78e1eaa1-19d4-4308-8892-3657b3efa86b",
                        "assignedTo": "150468349",
                        "assignedToType": "2",
                        "isRequired": false
                    }
                ]
            }
        ],
        "createdAt": "2024-02-15T16:01:28.660134Z",
        "createdBy": "MFEGJ9W5GGQL",
        "updatedAt": "2024-02-15T17:59:16.806768Z",
        "updatedBy": "MFEGJ9W5GGQL",
        "watchers": [
            {
                "id": "WBGQM228YWFQ",
                "userType": "1"
            }
        ]
    },
    {
        "id": "10be91e4-0ef8-4eb9-b567-b120ef329db8",
        "name": "template3",
        "steps": [
            {
                "id": "98f87fe4-0ffc-44b3-9c06-de97825acb3d",
                "stepNumber": 1,
                "daysToRespond": 21,
                "tasks": [
                    {
                        "id": "21aabd90-98ac-41c0-b240-5865bb0918ef",
                        "assignedTo": "WBGQM228YWFQ",
                        "assignedToType": "1",
                        "isRequired": true
                    },
                    {
                        "id": "354887ed-9f75-4af2-a3bb-5514f23fbce1",
                        "assignedTo": "150468349",
                        "assignedToType": "2",
                        "isRequired": false
                    }
                ]
            }
        ],
        "createdAt": "2024-02-15T16:55:03.631947Z",
        "createdBy": "MFEGJ9W5GGQL",
        "updatedAt": "2024-02-15T16:55:21.569878Z",
        "updatedBy": "MFEGJ9W5GGQL",
        "watchers": []
    }
  ]
}

```

Show More

The `steps` array provides detailed information about the steps in each template, including:

- `stepNumber`: The stepâs sequence number in the review process.
- `daysToRespond`: The allowed response time for this step.
- `tasks`: A list of tasks associated with the step, each specifying:

> * `id`: The unique identifier for the task.
> * `assignedTo`: The Autodesk ID of the person, role, or company assigned to the task.
> * `assignedToType`: Indicates whether the assignee is a user (1), role (2), or company (3).
> * `isRequired`: Whether the task is mandatory.

You can review this information to confirm whether a template meets the requirements of your submittal workflow before assigning it.

In this example, we will assign the first template (`id`: `8af9317c-dc73-4cf4-8085-9601bb96219e`) to the submittal item in the next step.

## [Step 7: Create a Submittal Item](#step-7-create-a-submittal-item)

To create the submittal item, you must include specific required fields, depending on the userâs role and the state in which the submittal item is being created.

**Required fields for all user roles:**

- **stateId**: The state in which you want to create the item. See step 1.
- **specId**: The ID of the spec section associated with the submittal item. See step 2.
- **typeId**: The ID of item type associated with the submittal item. See step 3.
- **title**: A title for the submittal item.
- **description**: A description of the submittal item (optional).
- **customIdentifier** (optional): A custom number for the submittal item. See step 4.

**Additional fields required for users with non-manager roles (``mgr-1``):**

- **manager**: The Autodesk ID of a manager. See step 4.
- **managerType**: The type of manager (user, role, or company). See step 4.

**Additional fields required for users with a manager role (``sbc-1``):**

- **subcontractor**: The Autodesk ID of user who will be assigned to the submittal item when it is created (`subcontractor`).
- **subcontractorType**: The type of subcontractor who will be assigned to the submittal item (`user`, `role`, or `company`).
- **submitterDueDate**: The due date for the Waiting for submission (`sbc-1`) state to end.

**Optional Field for Review Steps and Tasks:**

- **templateId** (optional): The ID of the review template that contains predefined steps and tasks for the submittal item. Refer to Step 6 for details.

Note that the required fields for creating a submittal item depend on the user role. Managers need to provide subcontractor details, while non-managers need to provide details about the manager assigned to the submittal item.

In this example, we assume the user is not a manager and include the required and optional fields in the payload.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/91b5ea71-e3ea-495b-999d-57443a8af6a4/items' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
      "specId": "000ce2cf-4fce-4c84-b993-5068889f8ff8",
      "title": "create-item1",
      "description": "my item description",
      "typeId": "530dbe26-6799-413c-9015-937ecfebe0e8",
      "manager": "WBGQM228YWFQ",
      "managerType": "1",
      "stateId": "mgr-1",
      "templateId": "8af9317c-dc73-4cf4-8085-9601bb96219e"
      }'

```

Show More

### Response

```
{
  "id": "09492800-4822-4854-a18a-0ec5d38b56b7",
  "identifier": 1,
  "typeId": "530dbe26-6799-413c-9015-937ecfebe0e8",
  "specId": "000ce2cf-4fce-4c84-b993-5068889f8ff8",
  "specIdentifier": "11",
  "specTitle": "spec1",
  "subsection": null,
  "title": "create-item1",
  "description": "my item description",
  "priority": "Normal",
  "revision": 0,
  "stateId": "mgr-1",
  "statusId": "2",
  "ballInCourt": [
    "WBGQM228YWFQ"
  ],
  "ballInCourtUsers": [
    "WBGQM228YWFQ"
  ],
  "ballInCourtCompanies": [],
  "ballInCourtRoles": [],
  "ballInCourtType": "manager",
  "manager": "WBGQM228YWFQ",
  "managerType": "1",
  "subcontractor": "MFEGJ9W5GGQL",
  "subcontractorType": "1",
  "watchers": [],
  "dueDate": null,
  "requiredOnJobDate": null,
  "leadTime": null,
  "requiredDate": null,
  "requiredApprovalDate": null,
  "submitterDueDate": null,
  "sentToSubmitter": null,
  "receivedFromSubmitter": "2024-02-11T14:14:04.088555Z",
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
  "folderUrn": null,
  "revisionsFoldersUrns": null,
  "createdAt": "2024-02-11T14:14:04.094908Z",
  "createdBy": "MFEGJ9W5GGQL",
  "updatedAt": "2024-02-11T14:14:04.094925Z",
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
        "customIdentifier": [],
        "title": [],
        "description": [],
        "packageId": [],
        "specId": [],
        "subsection": [],
        "typeId": [],
        "priority": [],
        "ballInCourt": [],
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
        ]
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
        "ballInCourt": [],
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
        "itemId",
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
        "itemId",
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
  "customIdentifier": null,
  "customIdentifierHumanReadable": "11-Unspecified"
}

```

Show More

Congratulations! You have successfully created a submittal item in ACC.
