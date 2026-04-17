# Create Approval Workflows

Source: https://aps.autodesk.com/en/docs/acc/tutorials/reviews/reviews-create-workflow/

---

# Create Approval Workflows

This tutorial demonstrates how to create an approval workflow in a project. The steps include preparing the workflow payload, creating the workflow, and confirming that the workflow has been created successfully. You can also query a specific workflow or list all workflows available in the project.

Approval workflows control the sequence of steps that files must pass through before they are approved. Each workflow includes at least an Initiator step and an Approver step, and can also include one or more Reviewer steps. The order of steps must always begin with the Initiator and end with the Approver.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps), and select `Forma APIs` in the `API Access` dropdown.
- Acquire a [3-legged](../../oauth/how-to-docs/get-3-legged-token.md) or [2-legged](../../oauth/how-to-docs/get-2-legged-token.md) OAuth token with `data:read` and `data:write` scopes for operating approval workflows.
  * For a 3-legged token, ensure that the user is a project administrator.
  * For a 2-legged token, the `x-user-id` header is required. Retrieve the user’s Autodesk ID by calling [GET projects/:projectId/users](../http-docs/http-admin-projectsprojectId-users-GET.md) with your 2-legged OAuth token and the user’s email address. Ensure that the user is a project administrator.
- Find the project ID for the project you want to create an approval workflow in by following the [Retrieve a Forma Hub ID and Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the project ID is `9ba6681e-1952-4d54-aac4-9de6d9858dd4`.
- Verify that you have access to the relevant Forma hub, project, and folders.
  * If you need to obtain the URNs of folders, follow the [Export Files From the Forma Files Tool](https://aps.autodesk.com/en/docs/acc/v1/tutorials/files/export-pdf-files/) tutorial to get the URNs you need.

## [Step 1: Prepare the Workflow Payload](#step-1-prepare-the-workflow-payload)

Before creating an approval workflow, you must prepare a JSON-formatted payload that defines the workflow’s steps and options. This payload will be used in Step 2 when you call [POST Workflow](../http-docs/http-reviews-createworkflow-POST.md).

The steps must follow a specific order:
* The Initiator step must come first.
* The Approver step must come last.
* Any Reviewer steps must be placed between them in the order you want them executed.

The Initiator step is not displayed in the web interface diagram of the workflow, so it is usually not considered a user-operated step. However, it is still required in the payload, as it determines who has permission to create a review.

### 1-Step Approval Workflow (Initiator + Approver)

The following example shows a minimal approval workflow with only one Initiator step and one user-operated step, the Approver.

```
{
  "name": "Final Structural Review",
  "description": "Used to review structural plans before finalizing IFC drawings.",
  "notes": "Please check all rebar annotations before approving. Include markup if changes are required.",
  "steps": [
    {
      "name": "Initial Review",
      "type": "INITIATOR",
      "candidates": {
        "roles": [ ],
        "users": [
          {
            "autodeskId": "U5XCJQ22TL8G"
          }
        ],
        "companies": [ ]
      }
    },
    {
      "name": "Final Review",
      "type": "APPROVER",
      "candidates": {
        "users": [
          {
            "autodeskId": "7J9JYVXFM24N4S8R"
          },
          {
            "autodeskId": "5CQFQS4GQCUS"
          }
        ],
        "roles": [ ],
        "companies": [ ]
      },
      "duration": 3,
      "dueDateType": "CALENDAR_DAY"
    }
  ],
  "additionalApprovalStatusOptions": [
    {
      "label": "Approved with comments",
      "value": "APPROVED"
    }
  ],
  "additionalOptions": {
    "allowInitiatorToEdit": true
  },
  "copyFilesOptions": {
    "enabled": true,
    "allowOverride": true,
    "condition": "ANY",
    "folderUrn": "urn:adsk.wipprod:fs.folder:co.XqQ14eRpSZiNe1xB7A_DNQ",
    "includeMarkups": false,
    "disableOverrideMarkupSetting": false
  }
}

```

Show More

### 3-Step Approval Workflow with Reviewers (Initiator + Reviewer 1 + Reviewer 2 + Approver)

You can also define multiple Reviewer steps. Each Reviewer step is executed in sequence. The next step begins only when reviewers in the current step complete their tasks and the configured conditions are met.

Reviewer steps can be **Single** or **Multiple**, depending on the `groupReview` setting:

- If `groupReview.enabled = false`, the step is treated as a Single Reviewer step.
- If `groupReview.enabled = true`, the step is treated as a Multiple Reviewer step. You can configure rules such as a minimum number of reviewers required.

```
{
  "name": "Final Structural Review",
  "description": "Used to review structural plans before finalizing IFC drawings.",
  "notes": "Please check all rebar annotations before approving. Include markup if changes are required.",
  "steps": [
    {
      "name": "Initial Review",
      "type": "INITIATOR",
      "candidates": {
        "roles": [ ],
        "users": [
          {
            "autodeskId": "U5XCJQ22TL8G"
          }
        ],
        "companies": [ ]
      }
    },
    {
      "name": "Multiple Reviewer",
      "type": "REVIEWER",
      "candidates": {
        "users": [
          { "autodeskId": "QZH2T4QCKRCHUUAK" },
          { "autodeskId": "T9V3MNG47NSE" },
          { "autodeskId": "YQKULET3A2P2" }
        ],
        "roles": [ { "autodeskId": "1473816" } ],
        "companies": [ { "autodeskId": "26980302" } ]
      },
      "dueDateType": "CALENDAR_DAY",
      "groupReview": {
        "enabled": true,
        "type": "MINIMUM",
        "min": 2
      },
      "duration": 3
    },
    {
      "name": "Single Reviewer",
      "type": "REVIEWER",
      "candidates": {
        "users": [ { "autodeskId": "5NYJZXZMJTY8J58K" } ],
        "roles": [ { "autodeskId": "81454472" } ],
        "companies": [ ]
      },
      "dueDateType": "WORKDAY",
      "groupReview": {
        "enabled": false,
        "type": "MINIMUM",
        "min": 2
      },
      "duration": 4
    },
    {
      "name": "Final Review",
      "type": "APPROVER",
      "candidates": {
        "users": [
          { "autodeskId": "7J9JYVXFM24N4S8R" },
          { "autodeskId": "5CQFQS4GQCUS" }
        ],
        "roles": [ ],
        "companies": [ ]
      },
      "duration": 3,
      "dueDateType": "CALENDAR_DAY"
    }
  ],
  "additionalApprovalStatusOptions": [
    {
      "label": "Approved with comments",
      "value": "APPROVED"
    }
  ],
  "additionalOptions": {
    "allowInitiatorToEdit": false
  },
  "copyFilesOptions": {
    "enabled": true,
    "allowOverride": true,
    "condition": "ANY",
    "folderUrn": "urn:adsk.wipprod:fs.folder:co.XqQ14eRpSZiNe1xB7A_DNQ",
    "includeMarkups": false,
    "disableOverrideMarkupSetting": false
  }
}

```

Show More

### Notes

- **Step order is required** — The workflow must start with `INITIATOR`, end with `APPROVER`, and place any `REVIEWER` steps in between in execution order.
- **Initiator is required** — The `INITIATOR` step is not shown in the UI diagram but must be included in the payload to control who can create reviews.

## [Step 2: Create an Approval Workflow](#step-2-create-an-approval-workflow)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) and the payload you prepared in Step 1 to call [POST workflow](../http-docs/http-reviews-createworkflow-POST.md), and create a new approval workflow in the project.

The following example shows a 3-step approval workflow (Initiator + Reviewer + Approver).

### Request

```
curl 'https://developer.api.autodesk.com/construction/reviews/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/workflows' \
  -X POST \
  -H 'x-user-id: U5XCJQ22TL8G' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Final Structural Review",
    "description": "Used to review structural plans before finalizing IFC drawings.",
    "notes": "Please check all rebar annotations before approving. Include markup if changes are required.",
    "steps": [
      {
        "name": "Initial Review",
        "type": "INITIATOR",
        "candidates": {
          "roles": [
            { "autodeskId": "1473817" }
          ],
          "users": [
            { "autodeskId": "HWUBNU689CRU" }
          ],
          "companies": [
            { "autodeskId": "26980302" }
          ]
        }
      },
      {
        "name": "Structural Design Reviewer",
        "type": "REVIEWER",
        "candidates": {
          "users": [
            { "autodeskId": "QZH2T4QCKRCHUUAK" },
            { "autodeskId": "T9V3MNG47NSE" },
            { "autodeskId": "YQKULET3A2P2" }
          ],
          "roles": [
            { "autodeskId": "1473816" }
          ],
          "companies": [
            { "autodeskId": "26980302" }
          ]
        },
        "dueDateType": "CALENDAR_DAY",
        "groupReview": { "enabled": true, "type": "MINIMUM", "min": 2 },
        "duration": 3
      },
      {
        "name": "Structural Design Approver",
        "type": "APPROVER",
        "candidates": {
          "users": [
            { "autodeskId": "7J9JYVXFM24N4S8R" },
            { "autodeskId": "5CQFQS4GQCUS" }
          ],
          "roles": [ ],
          "companies": [ ]
        },
        "duration": 3,
        "dueDateType": "CALENDAR_DAY"
      }
    ],
    "additionalApprovalStatusOptions": [
      { "label": "Approved with comments", "value": "APPROVED" }
    ],
    "additionalOptions": { "allowInitiatorToEdit": true },
    "copyFilesOptions": {
      "enabled": true,
      "allowOverride": true,
      "condition": "ANY",
      "folderUrn": "urn:adsk.wipprod:fs.folder:co.XqQ14eRpSZiNe1xB7A_DNQ",
      "includeMarkups": false,
      "disableOverrideMarkupSetting": false
    }
  }'

```

Show More

### Response

```
{
  "name": "Final Structural Review",
  "description": "Used to review structural plans before finalizing IFC drawings.",
  "notes": "Please check all rebar annotations before approving. Include markup if changes are required.",
  "id": "4e609369-e950-4097-b7d3-e6cf1c3c5415",
  "status": "ACTIVE",
  "approvalStatusOptions": [
    { "label": "Approved", "value": "APPROVED", "id": "f44e623d...", "builtIn": true },
    { "label": "Rejected", "value": "REJECTED", "id": "b2a3c3b7...", "builtIn": true },
    { "label": "Approved with comments", "value": "APPROVED", "id": "e683e927...", "builtIn": false }
  ],
  "steps": [
    { "name": "Initial Review", "type": "INITIATOR", "id": "Lane_vCfFkOixUp", ... },
    { "name": "Structural Design Reviewer", "type": "REVIEWER", "id": "Lane_3ReoxO2T0o", ... },
    { "name": "Structural Design Approver", "type": "APPROVER", "id": "Lane_Z76ZdpGSm5", ... }
  ],
  "copyFilesOptions": { "enabled": true, "allowOverride": true, "condition": "ANY", ... },
  "additionalOptions": { "allowInitiatorToEdit": true },
  "attachedAttributes": [],
  "updateAttributesOptions": { "enableAttachedAttributes": false, "updateSourceAndCopiedFiles": false },
  "createdAt": "2024-07-07T09:21:17.577Z",
  "updatedAt": "2025-01-07T08:43:10.189Z"
}

```

Show More

After the workflow is created, its settings can also be updated in the Reviews section of the web interface.

The `id` of each step in the response is automatically generated and must be used when calling [POST review](../http-docs/http-reviews-createreview-POST.md).

## [Step 3: Retrieve an Approval Workflow](#step-3-retrieve-an-approval-workflow)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) and the workflow ID returned in Step 2 to call [GET approval workflow](../http-docs/http-reviews-getworkflow-GET.md), and retrieve the details of a specific workflow.

### Request

```
curl 'https://developer.api.autodesk.com/construction/reviews/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/workflows/4e609369-e950-4097-b7d3-e6cf1c3c5415' \
  -X GET \
  -H 'x-user-id: U5XCJQ22TL8G' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Content-Type: application/json'

```

### Response

```
{
  "name": "Final Structural Review",
  "description": "Used to review structural plans before finalizing IFC drawings.",
  "notes": "Please check all rebar annotations before approving. Include markup if changes are required.",
  "id": "4e609369-e950-4097-b7d3-e6cf1c3c5415",
  "status": "ACTIVE",
  "approvalStatusOptions": [
    { "label": "Approved", "value": "APPROVED", "id": "f44e623d...", "builtIn": true },
    { "label": "Rejected", "value": "REJECTED", "id": "b2a3c3b7...", "builtIn": true },
    { "label": "Approved with comments", "value": "APPROVED", "id": "e683e927...", "builtIn": false }
  ],
  "steps": [
    { "name": "Initial Review", "type": "INITIATOR", "id": "Lane_vCfFkOixUp", ... },
    { "name": "Structural Design Reviewer", "type": "REVIEWER", "id": "Lane_3ReoxO2T0o", ... },
    { "name": "Structural Design Approver", "type": "APPROVER", "id": "Lane_Z76ZdpGSm5", ... }
  ],
  "copyFilesOptions": { "enabled": true, "allowOverride": true, "condition": "ANY", ... },
  "additionalOptions": { "allowInitiatorToEdit": true },
  "attachedAttributes": [],
  "updateAttributesOptions": { "enableAttachedAttributes": false, "updateSourceAndCopiedFiles": false },
  "createdAt": "2024-07-07T09:21:17.577Z",
  "updatedAt": "2025-01-07T08:43:10.189Z"
}

```

Show More

## [Step 4 (optional): List Approval Workflows](#step-4-optional-list-approval-workflows)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) to call [GET workflows](../http-docs/http-reviews-workflows-GET.md). and retrieve all approval workflows available in the project.

Use the `limit` and `offset` parameters to paginate the results. The default `limit` is 50 and the default `offset` is 0. If the response does not include a `nextUrl`, you have reached the last page of results.

### Request

```
curl 'https://developer.api.autodesk.com/construction/reviews/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/workflows?limit=10&offset=0&filter[status]=ACTIVE' \
  -X GET \
  -H 'x-user-id: U5XCJQ22TL8G' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Content-Type: application/json'

```

### Response

```
{
  "results": [
    {
      "name": "Final Structural Review",
      "description": "Used to review structural plans before finalizing IFC drawings.",
      "notes": "Please check all rebar annotations before approving. Include markup if changes are required.",
      "id": "4e609369-e950-4097-b7d3-e6cf1c3c5415",
      "status": "ACTIVE",
      "approvalStatusOptions": [
        {
          "label": "Approved",
          "value": "APPROVED",
          "id": "f44e623d-f04f-47fe-8195-efc43d1d985b",
          "builtIn": true
        },
        {
          "label": "Rejected",
          "value": "REJECTED",
          "id": "b2a3c3b7-4fef-40a4-868b-981b23e7182f",
          "builtIn": true
        },
        {
          "label": "Approved with comments",
          "value": "APPROVED",
          "id": "e683e927-fea7-4858-86af-f022b3c52aa4",
          "builtIn": false
        }
      ],
      "steps": [
        {
          "name": "Initial Review",
          "type": "INITIATOR",
          "id": "Lane_vCfFkOixUp",
          "candidates": {
            "roles": [
              { "autodeskId": "1473817", "name": "Architect" }
            ],
            "users": [
              { "autodeskId": "HWUBNU689CRU", "name": "James Smith" }
            ],
            "companies": [
              { "autodeskId": "26980302", "name": "Autodesk Co. Ltd." }
            ]
          }
        },
        {
          "name": "Structural Design Reviewer",
          "type": "REVIEWER",
          "id": "Lane_3ReoxO2T0o",
          "candidates": {
            "users": [
              { "autodeskId": "QZH2T4QCKRCHUUAK", "name": "John Doe" },
              { "autodeskId": "T9V3MNG47NSE", "name": "Jane Lee" },
              { "autodeskId": "YQKULET3A2P2", "name": "Jim Green" }
            ],
            "roles": [
              { "autodeskId": "1473816", "name": "Structural Engineer" }
            ],
            "companies": [
              { "autodeskId": "26980302", "name": "Autodesk Co. Ltd." }
            ]
          },
          "groupReview": {
            "enabled": true,
            "type": "MINIMUM",
            "min": 2
          },
          "dueDateType": "CALENDAR_DAY",
          "duration": 3
        },
        {
          "name": "Structural Design Approver",
          "type": "APPROVER",
          "id": "Lane_Z76ZdpGSm5",
          "candidates": {
            "users": [
              { "autodeskId": "7J9JYVXFM24N4S8R", "name": "Jimmy Park" },
              { "autodeskId": "5CQFQS4GQCUS", "name": "Kevin Dow" }
            ],
            "roles": [ ],
            "companies": [ ]
          },
          "duration": 3,
          "dueDateType": "CALENDAR_DAY"
        }
      ],
      "copyFilesOptions": {
        "enabled": true,
        "allowOverride": true,
        "condition": "ANY",
        "folderUrn": "urn:adsk.wipprod:fs.folder:co.XqQ14eRpSZiNe1xB7A_DNQ",
        "includeMarkups": false,
        "disableOverrideMarkupSetting": false
      },
      "additionalOptions": {
        "allowInitiatorToEdit": true
      },
      "attachedAttributes": [],
      "updateAttributesOptions": {
        "enableAttachedAttributes": false,
        "updateSourceAndCopiedFiles": false
      },
      "createdAt": "2024-07-07T09:21:17.577Z",
      "updatedAt": "2025-01-07T08:43:10.189Z"
    },
    ...
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 100,
    "nextUrl": "https://developer.api.autodesk.com/construction/reviews/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/workflows?limit=10&offset=10&filter[status]=ACTIVE"
  }
}

```

Show More

### Notes

- Use the `filter[status]` parameter to restrict results (e.g., `ACTIVE` or `INACTIVE`).
- Use the `nextUrl` field to retrieve the next page of results when paginating.
