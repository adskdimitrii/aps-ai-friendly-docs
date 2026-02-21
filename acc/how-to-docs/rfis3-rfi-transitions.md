# RFI Transitions

Source: https://aps.autodesk.com/en/docs/acc/tutorials/rfis3/rfi-transitions/

---

# RFI Transitions

This tutorial demonstrates a typical RFI workflow. The steps include:

- Verifying whether a user has permissions to create an RFI (creator or manager workflow role).
- Creating an RFI with draft status.
- Verifying whether a user has permissions to transition an RFI from draft status to open status (creator workflow role), and verifying which users can be assigned to the RFI when it is transitioned to open status (manager workflow role).
- Transitioning the RFI to open status and assigning the RFI to reviewers.
- Verifying whether a user has permissions to submit a response on the RFI.
- Submiting responses and Transitioning the RFI to answered status.
- Verifying whether a user has permissions to submit an official response and close the RFI.
- Repeating the process for transitioning from open status to answered status and for transitioning from answered status to closed status.
- Submiting an official response and Transitioning the RFI to closed status.

Note that the RFIs API does not use the same names for workflow roles as the RFIs module. To configure workflow roles for a project, click Settings on the top right, and select RFI Workflow. The following table displays RFI module workflow role names and the corresponding RFIs API workflow role names:

| Project Admin Module Workflow Role Name | RFIs API Workflow Role Name |
| --- | --- |
| Creator | Subcontractor (`projectSC`) |
| Manager | General Contractor (`projectGC`) |
| Reviewer 1 (EMEA workflow) | Construction Manager (`projectCoordinator`) |
| Reviewer (US workflow) / Reviewer 2 (EMEA workflow) | Architect (`projectReviewer`) |

To assign users to workflow roles, open the ACC RFIs module, click Settings on the top right, and select Permissions. Select the appropriate role from the Workflow role dropdown on the right. Note that in order to allocate workflow roles, you must have User Admin status.

At each stage in the workflow you can assign an RFI to a user. In order to assign an RFI to a user at specific stages in the workflow, the user needs to have been assigned specific workflow roles. For more details, see the [RFIs help](https://help.autodesk.com/view/BUILD/ENU/?guid=RFI_Workflow_Setup) documentation.

There are two RFI workflow options you can assign to a project:

- The default RFI workflow which has a single reviewer. The RFIs API uses the term `US` for this workflow.
- A workflow with an additional reviewer. The RFIs API uses the term - `EMEA` for this workflow.

This tutorial is using the default RFI workflow with a single reviewer. For information about selecting an RFI workflow for a project, see the [RFIs help](https://help.autodesk.com/view/BUILD/ENU/?guid=RFI_Workflow_Setup) documentation. Note that currently you cannot use the RFIs API to select an RFI workflow.

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps)
- Acquire a [3-legged OAuth token](/en/docs/oauth/v2/tutorials/get-3-legged-token/) with `data:create` `data:read` and `data:write` scopes.
- In this example, assume the project ID is `afc6e536-3a12-4ecf-8302-3f283d50dc6f`.

## [Step 1: Verify the Userâs Permissions](#step-1-verify-the-user-s-permissions)

Before the user creates an RFI you need to verify that the user has permissions to create it. Users who have been assigned either creator (`projectSC`) or manager (`projectGC`) workflow roles can create RFIs. All users in the project are automatically assigned the creator workflow role. To assign creator or manager workflow roles to project members, open the ACC RFIs module, click Settings on the top right, and select Permissions. A list of users is displayed. Select the appropriate role from the Workflow role dropdown on the right. Note that in order to allocate workflow roles, you must have User Admin status.

Use the project ID (`afc6e536-3a12-4ecf-8302-3f283d50dc6f`) to call [GET users/me](/en/docs/acc/v1/reference/http/rfis-v3-users-me-GET/) to verify the userâs permissions for creating RFIs.

Note that only users who are members of a project can potentially create and edit RFIs for the project. To check which users are members of a project, call GET users ([BIM 360](/en/docs/bim360/v1/reference/http/admin-v1-projects-projectId-users-GET) or [ACC](en/docs/acc/v1/reference/http/users-GET)). If a user is not a project member, the endpoint will return an error. Note that although we support grouping users by project for BIM 360 projects, we currently only support grouping users by account for ACC projects.

Note that if a user is not a project member, the endpoint will return an error.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/afc6e536-3a12-4ecf-8302-3f283d50dc6f/users/me' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "user": {
    "id": "KMQ7KREACSE7",
    "name": "Jon Doe",
    "role": "project_admin"
  },
  "permittedActions": {
    "createRfi": {
      "permittedStatuses": {
        "wfUS": [
          {
            "status": "draft",
            "requiredAttributes": [
              {
                "name": "title"
              }
            ],
            "permittedAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "KMQ7KREACSE7",
                    "type": "user"
                  }
                ]
              },
              {
                "name": "category"
              },
              {
                "name": "costImpact"
              },
              {
                "name": "customFields"
              },
              {
                "name": "discipline"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              },
              {
                "name": "documentReferenceRemove"
              },
              {
                "name": "dueDate"
              },
              {
                "name": "lbs"
              },
              {
                "name": "locations"
              },
              {
                "name": "locationDescription"
              },
              {
                "name": "priority"
              },
              {
                "name": "question"
              },
              {
                "name": "reference"
              },
              {
                "name": "scheduleImpact"
              },
              {
                "name": "suggestedAnswer"
              }
            ],
            "maxAssignees": 1
          },
          {
            "status": "submitted",
            "requiredAttributes": [
              {
                "name": "title"
              },
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "2UDYLKMEVARC",
                    "type": "user"
                  },
                  {
                    "value": "336SNF7WG2KU",
                    "type": "user"
                  },
                  {
                    "value": "V3KTJ2YVRF29",
                    "type": "user"
                  }
                ]
              }
            ],
            "permittedAttributes": [
              {
                "name": "category"
              },
              {
                "name": "coReviewers"
              },
              {
                "name": "costImpact"
              },
              {
                "name": "customFields"
              },
              {
                "name": "customIdentifier"
              },
              {
                "name": "discipline"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              },
              {
                "name": "documentReferenceRemove"
              },
              {
                "name": "dueDate"
              },
              {
                "name": "lbs"
              },
              {
                "name": "locations"
              },
              {
                "name": "locationDescription"
              },
              {
                "name": "nudge"
              },
              {
                "name": "priority"
              },
              {
                "name": "question"
              },
              {
                "name": "reference"
              },
              {
                "name": "rfiTypeId"
              },
              {
                "name": "scheduleImpact"
              },
              {
                "name": "sendNudgeEmail"
              },
              {
                "name": "suggestedAnswer"
              }
            ],
            "maxAssignees": 1
          },
          {
            "status": "open",
            "requiredAttributes": [
              {
                "name": "title"
              },
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "N7W3QVQ6ANSD",
                    "type": "user"
                  },
                  {
                    "value": "878RRNYF8QAB",
                    "type": "user"
                  },
                  {
                    "value": "Z8YKNL3KGDVN",
                    "type": "user"
                  }
                ]
              }
            ],
            "permittedAttributes": [
              {
                "name": "category"
              },
              {
                "name": "coReviewers"
              },
              {
                "name": "costImpact"
              },
              {
                "name": "customFields"
              },
              {
                "name": "customIdentifier"
              },
              {
                "name": "discipline"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              },
              {
                "name": "documentReferenceRemove"
              },
              {
                "name": "dueDate"
              },
              {
                "name": "lbs"
              },
              {
                "name": "locations"
              },
              {
                "name": "locationDescription"
              },
              {
                "name": "nudge"
              },
              {
                "name": "officialResponse"
              },
              {
                "name": "priority"
              },
              {
                "name": "question"
              },
              {
                "name": "reference"
              },
              {
                "name": "rfiTypeId"
              },
              {
                "name": "scheduleImpact"
              },
              {
                "name": "sendNudgeEmail"
              },
              {
                "name": "suggestedAnswer"
              }
            ],
            "maxAssignees": 10
          }
        ],
        "wfEU": [
          {
            "status": "draft",
            "requiredAttributes": [
              {
                "name": "title"
              }
            ],
            "permittedAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "KMQ7KREACSE7",
                    "type": "user"
                  }
                ]
              },
              {
                "name": "category"
              },
              {
                "name": "costImpact"
              },
              {
                "name": "customFields"
              },
              {
                "name": "discipline"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              },
              {
                "name": "documentReferenceRemove"
              },
              {
                "name": "dueDate"
              },
              {
                "name": "lbs"
              },
              {
                "name": "locations"
              },
              {
                "name": "locationDescription"
              },
              {
                "name": "priority"
              },
              {
                "name": "question"
              },
              {
                "name": "reference"
              },
              {
                "name": "scheduleImpact"
              },
              {
                "name": "suggestedAnswer"
              }
            ],
            "maxAssignees": 1
          },
          {
            "status": "submitted",
            "requiredAttributes": [
              {
                "name": "title"
              },
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "2UDYLKMEVARC",
                    "type": "user"
                  },
                  {
                    "value": "336SNF7WG2KU",
                    "type": "user"
                  },
                  {
                    "value": "3AGRNXCG4FZ9",
                    "type": "user"
                  }
                ]
              }
            ],
            "permittedAttributes": [
              {
                "name": "category"
              },
              {
                "name": "coReviewers"
              },
              {
                "name": "costImpact"
              },
              {
                "name": "customFields"
              },
              {
                "name": "customIdentifier"
              },
              {
                "name": "discipline"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              },
              {
                "name": "documentReferenceRemove"
              },
              {
                "name": "dueDate"
              },
              {
                "name": "lbs"
              },
              {
                "name": "locations"
              },
              {
                "name": "locationDescription"
              },
              {
                "name": "nudge"
              },
              {
                "name": "priority"
              },
              {
                "name": "question"
              },
              {
                "name": "reference"
              },
              {
                "name": "rfiTypeId"
              },
              {
                "name": "scheduleImpact"
              },
              {
                "name": "sendNudgeEmail"
              },
              {
                "name": "suggestedAnswer"
              }
            ],
            "maxAssignees": 1
          },
          {
            "status": "openRev1",
            "requiredAttributes": [
              {
                "name": "title"
              },
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "226RQRYXACZN",
                    "type": "user"
                  },
                  {
                    "value": "22KFLV244MC7",
                    "type": "user"
                  },
                  {
                    "value": "273JYAXWLURVSHKZ",
                    "type": "user"
                  }
                ]
              }
            ],
            "permittedAttributes": [
              {
                "name": "category"
              },
              {
                "name": "coReviewers"
              },
              {
                "name": "costImpact"
              },
              {
                "name": "customFields"
              },
              {
                "name": "customIdentifier"
              },
              {
                "name": "discipline"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              },
              {
                "name": "documentReferenceRemove"
              },
              {
                "name": "dueDate"
              },
              {
                "name": "lbs"
              },
              {
                "name": "locations"
              },
              {
                "name": "locationDescription"
              },
              {
                "name": "nudge"
              },
              {
                "name": "officialResponse"
              },
              {
                "name": "priority"
              },
              {
                "name": "question"
              },
              {
                "name": "reference"
              },
              {
                "name": "rfiTypeId"
              },
              {
                "name": "scheduleImpact"
              },
              {
                "name": "sendNudgeEmail"
              },
              {
                "name": "suggestedAnswer"
              }
            ],
            "maxAssignees": 1
          }
        ]
      }
    }
  },
  "workflow": {
    "roles": [
      "projectCoordinator",
      "projectReviewer"
    ],
    "type": "EU"
  },
  "externalUsers": [
    {
      "oxygenId": "ZKH2EWMURBU2Y8TD",
      "id": "aaffdf22-c5bb-4fa2-ae9f-c2e2ebb95040",
      "city": null,
      "name": "invitetry87 invitetry87",
      "email": "invitetry87@ooo.com",
      "phone": null,
      "status": "not_invited",
      "aboutMe": null,
      "country": null,
      "roleIds": [],
      "imageUrl": null,
      "industry": null,
      "jobTitle": null,
      "lastName": "invitetry87",
      "companyId": null,
      "createdAt": "2024-01-09T10:11:11.419Z",
      "firstName": "invitetry87",
      "updatedAt": "2024-01-09T10:11:11.419Z",
      "autodeskId": "ZKH2EWMURBU2Y8TD",
      "lastSignIn": null,
      "postalCode": null,
      "analyticsId": null,
      "accessLevels": {
        "noAccess": true,
        "executive": false,
        "accountAdmin": false,
        "projectAdmin": false,
        "projectMember": false
      },
      "addressLine1": null,
      "addressLine2": null,
      "defaultRoleId": null,
      "defaultRoleName": null,
      "stateOrProvince": null,
      "defaultCompanyId": null,
      "defaultCompanyName": null
    }
  ]
  "defaultRfiType": "ab8ed772-276e-4dcf-9d24-03809ddc3f93",
  "maintenanceEndDate": null
}

```

Show More

Find the `workflow.roles` list. If it includes either `projectSC`, or `projectGC` it indicates that the user can create RFIs.

The `permittedActions.createRfi.permittedStatuses` section informs you which types of statuses the user can create the RFI with; in this example - `draft`, `submitted`, and `open`. It also lists the attributes that are required for each status.

In our example, the user will create the RFI in `draft` status, and will include the `title` attribute in the request body.

Note also:
> - `user.id`: the user who creates the RFI
> - `workflow.type`: the status transitions available throughout the workfllow.
> - `permittedStatuses`: the initial status (`draft`, `submitted`, or `open`) the user can use.

## [Step 2: Create the RFI](#step-2-create-the-rfi)

Use the project ID (`afc6e536-3a12-4ecf-8302-3f283d50dc6f`) to call [POST rfis](/en/docs/acc/v1/reference/http/rfis-V3-rfi-POST/).

### Request

```
curl "https://developer.api.autodesk.com/construction/rfis/v3/projects/afc6e536-3a12-4ecf-8302-3f283d50dc6f/rfis" -d '{
    "title": "Pipe Size",
    "status": "draft",
    "question": "Is the pipe in room 3 the correct size?",
    "suggestedAnswer": "No",
    "dueDate": "2025-07-31T09:35:54.000Z"
  }' -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer XZvCJNhdxESsBRIH28MfLf2hKL5O"

```

Show More

### Response

```
{
  "createdAt": "2025-03-13T10:59:09.249Z",
  "updatedAt": "2025-03-13T10:59:09.249Z",
  "id": "48ae70ef-c215-4781-a7c2-394afaae0d9c",
  "coReviewers": [],
  "discipline": [],
  "category": [],
  "commentsCount": 0,
  "attachmentsCount": 0,
  "bridgedSource": false,
  "bridgedTarget": false,
  "bridgeSyncOutdated": false,
  "rfiTypeId": "92da943f-9f3e-408d-981d-41b4a087f7a3",
  "title": "Pipe Size",
  "status": "draft",
  "question": "Is the pipe in room 3 the correct size?",
  "suggestedAnswer": "No",
  "dueDate": "2025-07-31T09:35:54.000Z",
  "workflowType": "US",
  "createdBy": "KMQ7KREACSE7",
  "platform": "acc",
  "assignedTo": [
    {
      "id": "KMQ7KREACSE7",
      "type": "user"
    }
  ],
  "permittedActions": {
    "linkPCO": true,
    "createDocumentReference": true,
    "removeDocumentReference": true,
    "share": false,
    "updateRfi": {
      "useCustomAttributes": true,
      "permittedAttributes": [
        {
          "name": "assignedTo",
          "values": [
            {
              "value": "FRW2E3YWRS84GQF4",
              "type": "user"
            },
            {
              "value": "HVW3M3CLCSN5",
              "type": "user"
            }
          ]
        },
        {
          "name": "category"
        },
        {
          "name": "costImpact"
        },
        {
          "name": "customFields"
        },
        {
          "name": "discipline"
        },
        {
          "name": "watchers"
        },
        {
          "name": "documentReferenceCreate"
        },
        {
          "name": "documentReferenceRemove"
        },
        {
          "name": "dueDate"
        },
        {
          "name": "lbs"
        },
        {
          "name": "locations"
        },
        {
          "name": "locationDescription"
        },
        {
          "name": "priority"
        },
        {
          "name": "question"
        },
        {
          "name": "reference"
        },
        {
          "name": "scheduleImpact"
        },
        {
          "name": "suggestedAnswer"
        },
        {
          "name": "title"
        },
        {
          "name": "status",
          "values": [
            {
              "value": "open"
            },
            {
              "value": "void"
            }
          ]
        }
      ],
      "permittedStatuses": {
        "wfUS": [
          {
            "status": "open",
            "requiredAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "WZJ23QYPPEBML8BG",
                    "type": "user"
                  },
                  {
                    "value": "Z762FZR9LSEHQASK",
                    "type": "user"
                  }
                ]
              }
            ],
            "permittedAttributes": [
              {
                "name": "category"
              },
              {
                "name": "coReviewers"
              },
              {
                "name": "costImpact"
              },
              {
                "name": "customFields"
              },
              {
                "name": "customIdentifier"
              },
              {
                "name": "discipline"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              },
              {
                "name": "documentReferenceRemove"
              },
              {
                "name": "dueDate"
              },
              {
                "name": "lbs"
              },
              {
                "name": "locations"
              },
              {
                "name": "locationDescription"
              },
              {
                "name": "nudge"
              },
              {
                "name": "officialResponse"
              },
              {
                "name": "priority"
              },
              {
                "name": "question"
              },
              {
                "name": "reference"
              },
              {
                "name": "rfiTypeId"
              },
              {
                "name": "scheduleImpact"
              },
              {
                "name": "sendNudgeEmail"
              },
              {
                "name": "suggestedAnswer"
              },
              {
                "name": "title"
              }
            ],
            "maxAssignees": 10
          },
          {
            "status": "void",
            "requiredAttributes": [],
            "permittedAttributes": [
              {
                "name": "category"
              },
              {
                "name": "coReviewers"
              },
              {
                "name": "costImpact"
              },
              {
                "name": "customFields"
              },
              {
                "name": "customIdentifier"
              },
              {
                "name": "discipline"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              },
              {
                "name": "documentReferenceRemove"
              },
              {
                "name": "dueDate"
              },
              {
                "name": "lbs"
              },
              {
                "name": "locations"
              },
              {
                "name": "locationDescription"
              },
              {
                "name": "officialResponse"
              },
              {
                "name": "priority"
              },
              {
                "name": "question"
              },
              {
                "name": "reference"
              },
              {
                "name": "scheduleImpact"
              },
              {
                "name": "suggestedAnswer"
              },
              {
                "name": "title"
              }
            ],
            "maxAssignees": 1
          }
        ],
        "wfEU": [
          {
            "status": "openRev1",
            "requiredAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "CVRJ3WFQPEQTMXYQ",
                    "type": "user"
                  },
                  {
                    "value": "PS72PV2ZL8UXTDN8",
                    "type": "user"
                  }
                ]
              }
            ],
            "permittedAttributes": [
              {
                "name": "category"
              },
              {
                "name": "coReviewers"
              },
              {
                "name": "costImpact"
              },
              {
                "name": "customFields"
              },
              {
                "name": "customIdentifier"
              },
              {
                "name": "discipline"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              },
              {
                "name": "documentReferenceRemove"
              },
              {
                "name": "dueDate"
              },
              {
                "name": "lbs"
              },
              {
                "name": "locations"
              },
              {
                "name": "locationDescription"
              },
              {
                "name": "nudge"
              },
              {
                "name": "officialResponse"
              },
              {
                "name": "priority"
              },
              {
                "name": "question"
              },
              {
                "name": "reference"
              },
              {
                "name": "rfiTypeId"
              },
              {
                "name": "scheduleImpact"
              },
              {
                "name": "sendNudgeEmail"
              },
              {
                "name": "suggestedAnswer"
              },
              {
                "name": "title"
              }
            ],
            "maxAssignees": 1
          },
          {
            "status": "void",
            "requiredAttributes": [],
            "permittedAttributes": [
              {
                "name": "category"
              },
              {
                "name": "coReviewers"
              },
              {
                "name": "costImpact"
              },
              {
                "name": "customFields"
              },
              {
                "name": "customIdentifier"
              },
              {
                "name": "discipline"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              },
              {
                "name": "documentReferenceRemove"
              },
              {
                "name": "dueDate"
              },
              {
                "name": "lbs"
              },
              {
                "name": "locations"
              },
              {
                "name": "locationDescription"
              },
              {
                "name": "officialResponse"
              },
              {
                "name": "priority"
              },
              {
                "name": "question"
              },
              {
                "name": "reference"
              },
              {
                "name": "scheduleImpact"
              },
              {
                "name": "suggestedAnswer"
              },
              {
                "name": "title"
              }
            ],
            "maxAssignees": 1
          }
        ]
      }
    },
    "createComment": true,
    "createResponse": false,
    "remainingReviewers": [],
    "createResponseOnBehalf": false
  },
  "reviewers": [],
  "architects": [],
  "officialResponseActors": [],
  "locations": [],
  "maxAssignees": 1,
  "watchers": []
}

```

Show More

Find the RFI ID (`id`) and note the ID (`48ae70ef-c215-4781-a7c2-394afaae0d9c`). Weâll use the ID in step 3 to transition the RFI to `open` status.

The `permittedActions.updateRfi.permittedStatuses` section informs you which types of statuses the user can transition the RFI to; in this example - open or void. It also lists which users you can assign to the RFI when you transition to the new status.

In this example, we will transition the RFI to open status. When you transition the RFI to open status, you need to assign the RFI to user(s) (up to 10). Locate the list of users that can potentially be assigned to the RFI when you transition it to open status by finding the `open` status in `permittedActions.updateRfi.permittedStatuses`, and checking the list of users (`requiredAttributes.values`).

Note that only assignees with a manager (`projectGC`) workflow role will be listed as potential assignees. See the [help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=RFI_Workflow_Setup) for more details.

Note the userâs ID. In this example `KMQ7KREACSE7`. This is the same user who created the RFI and will also perform the transition to `open` status in the next step.

To verify the actual name of the user, call [GET accounts/:accountId/users/:userId](/en/docs/bim360/v1/reference/http/admin-v1-accounts-accountId-users-userId-GET/).

## [Step 3: Transition the RFI to Open Status](#step-3-transition-the-rfi-to-open-status)

Use the project ID (`afc6e536-3a12-4ecf-8302-3f283d50dc6f`), the RFI ID (`48ae70ef-c215-4781-a7c2-394afaae0d9c`) and the IDs of the assignees (`Z762FZR9LSEHQASK` and `WZJ23QYPPEBML8BG`) to call [PATCH rfis/:rfiId](/en/docs/acc/v1/reference/http/rfis-V3-rfisrfiid-PATCH/) to transition the RFI from draft status to open status.

In this example, the user who created the RFI will also transition the RFI to open status.

### Request

```
curl --location --request PATCH 'https://developer.api.autodesk.com/construction/rfis/v3/projects/afc6e536-3a12-4ecf-8302-3f283d50dc6f/rfis/48ae70ef-c215-4781-a7c2-394afaae0d9c' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer XZvCJNhdxESsBRIH28MfLf2hKL5O" \
--data '{
  "status": "open",
  "assignedTo": [
    {
      "id": "Z762FZR9LSEHQASK",
      "type": "user"
    },
    {
      "id": "WZJ23QYPPEBML8BG",
      "type": "user"
    }
  ]
}'

```

Show More

### Response

```
{
  "id": "48ae70ef-c215-4781-a7c2-394afaae0d9c",
  "title": "Pipe Size",
  "question": "Is the pipe in room 3 the correct size?",
  "status": "open",
  "previousStatus": "draft",
  "dueDate": "2025-07-31T09:35:54.000Z",
  "createdBy": "KMQ7KREACSE7",
  "updatedBy": "KMQ7KREACSE7",
  "workflowType": "US",
  "suggestedAnswer": "No",
  "coReviewers": [],
  "managerId": "KMQ7KREACSE7",
  "reviewers": [
    {
      "id": "Z762FZR9LSEHQASK",
      "type": "user"
    },
    {
      "id": "WZJ23QYPPEBML8BG",
      "type": "user"
    }
  ],
  "customIdentifier": "12334234e66",
  "discipline": [],
  "category": [],
  "syncVersion": "2533",
  "commentsCount": 0,
  "rfiTypeId": "92da943f-9f3e-408d-981d-41b4a087f7a3",
  "attachmentsCount": 0,
  "platform": "acc",
  "bridgedSource": false,
  "bridgedTarget": false,
  "bridgeSyncOutdated": false,
  "createdAt": "2025-03-13T10:59:09.249Z",
  "updatedAt": "2025-03-13T11:48:24.660Z",
  "assignedTo": [
    {
      "id": "Z762FZR9LSEHQASK",
      "type": "user"
    },
    {
      "id": "WZJ23QYPPEBML8BG",
      "type": "user"
    }
  ],
  "architects": [
    {
      "id": "Z762FZR9LSEHQASK",
      "type": "user"
    },
    {
      "id": "WZJ23QYPPEBML8BG",
      "type": "user"
    }
  ],
  "responses": [],
  "draftResponses": [],
  "permittedActions": {
    "linkPCO": true,
    "createDocumentReference": true,
    "removeDocumentReference": true,
    "share": false,
    "updateRfi": {
      "useCustomAttributes": true,
      "permittedAttributes": [
        {
          "name": "assignedTo",
          "values": [
            {
              "value": "WZJ23QYPPEBML8BG",
              "type": "user"
            },
            {
              "value": "Z762FZR9LSEHQASK",
              "type": "user"
            }
          ]
        },
        {
          "name": "category"
        },
        {
          "name": "coReviewers"
        },
        {
          "name": "costImpact"
        },
        {
          "name": "customFields"
        },
        {
          "name": "customIdentifier"
        },
        {
          "name": "discipline"
        },
        {
          "name": "watchers"
        },
        {
          "name": "documentReferenceCreate"
        },
        {
          "name": "documentReferenceRemove"
        },
        {
          "name": "dueDate"
        },
        {
          "name": "lbs"
        },
        {
          "name": "locations"
        },
        {
          "name": "locationDescription"
        },
        {
          "name": "nudge"
        },
        {
          "name": "officialResponse"
        },
        {
          "name": "priority"
        },
        {
          "name": "question"
        },
        {
          "name": "reference"
        },
        {
          "name": "rfiTypeId"
        },
        {
          "name": "scheduleImpact"
        },
        {
          "name": "sendNudgeEmail"
        },
        {
          "name": "suggestedAnswer"
        },
        {
          "name": "title"
        },
        {
          "name": "status",
          "values": [
            {
              "value": "submitted"
            },
            {
              "value": "void"
            }
          ]
        }
      ],
      "permittedStatuses": {
        "wfUS": [
          {
            "status": "submitted",
            "requiredAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "KMQ7KREACSE7",
                    "type": "user"
                  },
                  {
                    "value": "NVE27LREMTDB5ZM4",
                    "type": "user"
                  }
                ]
              }
            ],
            "permittedAttributes": [
              {
                "name": "category"
              },
              {
                "name": "coReviewers"
              },
              {
                "name": "costImpact"
              },
              {
                "name": "customFields"
              },
              {
                "name": "customIdentifier"
              },
              {
                "name": "discipline"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              },
              {
                "name": "documentReferenceRemove"
              },
              {
                "name": "dueDate"
              },
              {
                "name": "lbs"
              },
              {
                "name": "locations"
              },
              {
                "name": "locationDescription"
              },
              {
                "name": "nudge"
              },
              {
                "name": "priority"
              },
              {
                "name": "question"
              },
              {
                "name": "reference"
              },
              {
                "name": "rfiTypeId"
              },
              {
                "name": "scheduleImpact"
              },
              {
                "name": "sendNudgeEmail"
              },
              {
                "name": "suggestedAnswer"
              },
              {
                "name": "title"
              }
            ],
            "maxAssignees": 1
          },
          {
            "status": "void",
            "requiredAttributes": [],
            "permittedAttributes": [],
            "maxAssignees": 1
          }
        ],
        "wfEU": []
      }
    },
    "createComment": true,
    "createResponse": false,
    "remainingReviewers": [
      {
        "id": "Z762FZR9LSEHQASK",
        "type": "user"
      },
      {
        "id": "WZJ23QYPPEBML8BG",
        "type": "user"
      }
    ],
    "createResponseOnBehalf": true
  },
  "attachments": [],
  "officialResponseActors": [],
  "locations": [],
  "maxAssignees": 10,
  "watchers": []
}

```

Show More

In this example, the `permittedActions.updateRfi.permittedStatuses` section informs you that you can potentially transition the RFI to `submitted` (back to the manager) or `void` statuses. To proceed with the RFI towards the answered status, one of the following conditions must be met:
> 1. All assignees submit their responses.
> 2. At least one assignee submits a response, and the manager skips the remaining reviewers, allowing the RFI to transition to the answered status.

## [Step 4: Change the User and Submit a Response](#step-4-change-the-user-and-submit-a-response)

In the previous step, the RFI was transitioned to `open` status and assigned to two users: `Z762FZR9LSEHQASK` and `WZJ23QYPPEBML8BG`.

Each assigned user is expected to submit a response. You can either switch authentication to act as one of these users, or use the `createResponseOnBehalf` capability if permitted.

For instructions on how to submit a response, see the [Submit an RFI Response](/en/docs/acc/v1/tutorials/rfis3/rfi-response/) tutorial.

Note that at least one response must be submitted before the RFI can be transitioned to `answered` status in Step 5.

## [Step 5: Transition the RFI to Answered Status](#step-5-transition-the-rfi-to-answered-status)

In this tutorial, we assume a scenario where one of the assignees has submitted a response, and the manager intends to skip the remaining reviewers to transition the RFI to the answered status.

(Optional) To review the RFIâs current status, including remaining reviewers and submitted responses, you can call GET rfis/:rfiId. This helps you verify that the RFI is eligible to be transitioned to `answered` status.

When retrieving the RFI data, the `remainingReviewers` field indicates the reviewers who have not yet submitted a response, while the `responses` field contains the responses that have already been provided.

### Request

```
curl --location 'https://developer.api.autodesk.com/construction/rfis/v3/projects/afc6e536-3a12-4ecf-8302-3f283d50dc6f/rfis/48ae70ef-c215-4781-a7c2-394afaae0d9c' \
--header 'Authorization: Bearer l0ZSIsImRhdGE6cmVhZCIsImRhdGE6Y3JlYXRlIiwiZGF0YTpzZWFyY2gi'

```

### Response

```
{
  "id": "48ae70ef-c215-4781-a7c2-394afaae0d9c",
  "title": "Pipe Size",
  "question": "Is the pipe in room 3 the correct size?",
  "status": "open",
  "previousStatus": "draft",
  "dueDate": "2025-07-31T09:35:54.000Z",
  "virtualFolderUrn": "urn:adsk.wipqa:fs.folder:co.nci3h8-zTdG54piczhweqw",
  "createdBy": "KMQ7KREACSE7",
  "updatedBy": "KMQ7KREACSE7",
  "workflowType": "US",
  "suggestedAnswer": "No",
  "coReviewers": [],
  "managerId": "KMQ7KREACSE7",
  "reviewers": [
    {
      "id": "Z762FZR9LSEHQASK",
      "type": "user"
    },
    {
      "id": "WZJ23QYPPEBML8BG",
      "type": "user"
    }
  ],
  "customIdentifier": "12334234e66",
  "discipline": [],
  "category": [],
  "syncVersion": "2533",
  "commentsCount": 0,
  "rfiTypeId": "92da943f-9f3e-408d-981d-41b4a087f7a3",
  "attachmentsCount": 0,
  "platform": "acc",
  "bridgedSource": false,
  "bridgedTarget": false,
  "bridgeSyncOutdated": false,
  "createdAt": "2025-03-13T10:59:09.249Z",
  "updatedAt": "2025-03-13T11:53:57.574Z",
  "assignedTo": [
    {
      "id": "WZJ23QYPPEBML8BG",
      "type": "user"
    },
    {
      "id": "Z762FZR9LSEHQASK",
      "type": "user"
    }
  ],
  "architects": [
    {
      "id": "WZJ23QYPPEBML8BG",
      "type": "user"
    },
    {
      "id": "Z762FZR9LSEHQASK",
      "type": "user"
    }
  ],
  "responses": [
    {
      "id": "07bd6f68-a9e0-4459-b9c2-686cc991509f",
      "text": "dwdq",
      "createdBy": "KMQ7KREACSE7",
      "updatedBy": null,
      "onBehalf": "Z762FZR9LSEHQASK",
      "status": "answered",
      "state": "submitted",
      "rfiId": "48ae70ef-c215-4781-a7c2-394afaae0d9c",
      "containerId": "afc6e536-3a12-4ecf-8302-3f283d50dc6f",
      "syncVersion": "650",
      "createdAt": "2025-03-13T12:08:47.232Z",
      "updatedAt": "2025-03-13T12:08:47.232Z",
      "deletedAt": null,
      "isEditable": true
    }
  ],
  "customAttributes": [],
  "permittedActions": {
    "linkPCO": true,
    "createDocumentReference": true,
    "removeDocumentReference": true,
    "share": false,
    "updateRfi": {
      "useCustomAttributes": true,
      "permittedAttributes": [
        {
          "name": "assignedTo",
          "values": [
            {
              "value": "WZJ23QYPPEBML8BG",
              "type": "user"
            },
            {
              "value": "Z762FZR9LSEHQASK",
              "type": "user"
            }
          ]
        },
        {
          "name": "category"
        },
        {
          "name": "coReviewers"
        },
        {
          "name": "costImpact"
        },
        {
          "name": "customFields"
        },
        {
          "name": "customIdentifier"
        },
        {
          "name": "discipline"
        },
        {
          "name": "watchers"
        },
        {
          "name": "documentReferenceCreate"
        },
        {
          "name": "documentReferenceRemove"
        },
        {
          "name": "dueDate"
        },
        {
          "name": "lbs"
        },
        {
          "name": "locations"
        },
        {
          "name": "locationDescription"
        },
        {
          "name": "nudge"
        },
        {
          "name": "officialResponse"
        },
        {
          "name": "priority"
        },
        {
          "name": "question"
        },
        {
          "name": "reference"
        },
        {
          "name": "rfiTypeId"
        },
        {
          "name": "scheduleImpact"
        },
        {
          "name": "sendNudgeEmail"
        },
        {
          "name": "suggestedAnswer"
        },
        {
          "name": "title"
        },
        {
          "name": "status",
          "values": [
            {
              "value": "submitted"
            },
            {
              "value": "answered"
            },
            {
              "value": "void"
            }
          ]
        }
      ],
      "permittedStatuses": {
        "wfUS": [
          {
            "status": "submitted",
            "requiredAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "KMQ7KREACSE7",
                    "type": "user"
                  },
                  {
                    "value": "NVE27LREMTDB5ZM4",
                    "type": "user"
                  }
                ]
              }
            ],
            "permittedAttributes": [
              {
                "name": "category"
              },
              {
                "name": "coReviewers"
              },
              {
                "name": "costImpact"
              },
              {
                "name": "customFields"
              },
              {
                "name": "customIdentifier"
              },
              {
                "name": "discipline"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              },
              {
                "name": "documentReferenceRemove"
              },
              {
                "name": "dueDate"
              },
              {
                "name": "lbs"
              },
              {
                "name": "locations"
              },
              {
                "name": "locationDescription"
              },
              {
                "name": "nudge"
              },
              {
                "name": "priority"
              },
              {
                "name": "question"
              },
              {
                "name": "reference"
              },
              {
                "name": "rfiTypeId"
              },
              {
                "name": "scheduleImpact"
              },
              {
                "name": "sendNudgeEmail"
              },
              {
                "name": "suggestedAnswer"
              },
              {
                "name": "title"
              }
            ],
            "maxAssignees": 1
          },
          {
            "status": "answered",
            "requiredAttributes": [],
            "permittedAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "KMQ7KREACSE7",
                    "type": "user"
                  },
                  {
                    "value": "NVE27LREMTDB5ZM4",
                    "type": "user"
                  }
                ]
              },
              {
                "name": "category"
              },
              {
                "name": "coReviewers"
              },
              {
                "name": "costImpact"
              },
              {
                "name": "customFields"
              },
              {
                "name": "customIdentifier"
              },
              {
                "name": "discipline"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              },
              {
                "name": "documentReferenceRemove"
              },
              {
                "name": "dueDate"
              },
              {
                "name": "lbs"
              },
              {
                "name": "locations"
              },
              {
                "name": "locationDescription"
              },
              {
                "name": "nudge"
              },
              {
                "name": "officialResponse"
              },
              {
                "name": "officialResponseStatus"
              },
              {
                "name": "priority"
              },
              {
                "name": "question"
              },
              {
                "name": "reference"
              },
              {
                "name": "scheduleImpact"
              },
              {
                "name": "sendNudgeEmail"
              },
              {
                "name": "suggestedAnswer"
              },
              {
                "name": "title"
              }
            ],
            "maxAssignees": 1
          },
          {
            "status": "void",
            "requiredAttributes": [],
            "permittedAttributes": [],
            "maxAssignees": 1
          }
        ],
        "wfEU": []
      }
    },
    "createComment": true,
    "createResponse": false,
    "remainingReviewers": [
      {
        "id": "WZJ23QYPPEBML8BG",
        "type": "user"
      }
    ],
    "createResponseOnBehalf": true
  },
  "draftResponses": [],
  "officialResponseActors": [],
  "locations": [],
  "maxAssignees": 10,
  "watchers": []
}

```

Show More

Use the project ID (`afc6e536-3a12-4ecf-8302-3f283d50dc6f`), the RFI ID (`48ae70ef-c215-4781-a7c2-394afaae0d9c`), and the managerâs ID (`KMQ7KREACSE7`) to call [PATCH rfis/:rfiId](/en/docs/acc/v1/reference/http/rfis-V3-rfisrfiid-PATCH/) to transition the RFI from open status to answered status.

### Request

```
curl --location --request PATCH 'https://developer.api.autodesk.com/construction/rfis/v3/projects/afc6e536-3a12-4ecf-8302-3f283d50dc6f/rfis/48ae70ef-c215-4781-a7c2-394afaae0d9c' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer l0ZSIsImRhdGE6cmVhZCIsImRhdGE6Y3JlYXRlIiwiZGF0YTpzZWFyY2gi' \
--data '{
  "status": "answered"
}'

```

### Response

```
{
  "id": "48ae70ef-c215-4781-a7c2-394afaae0d9c",
  "title": "Pipe Size",
  "question": "Is the pipe in room 3 the correct size?",
  "status": "answered",
  "previousStatus": "open",
  "dueDate": "2025-07-31T09:35:54.000Z",
  "virtualFolderUrn": "urn:adsk.wipqa:fs.folder:co.nci3h8-zTdG54piczhweqw",
  "createdBy": "KMQ7KREACSE7",
  "updatedBy": "KMQ7KREACSE7",
  "workflowType": "US",
  "suggestedAnswer": "No",
  "coReviewers": [],
  "managerId": "KMQ7KREACSE7",
  "reviewers": [
    {
      "id": "Z762FZR9LSEHQASK",
      "type": "user"
    },
    {
      "id": "WZJ23QYPPEBML8BG",
      "type": "user"
    }
  ],
  "answeredAt": "2025-03-13T12:19:27.713Z",
  "answeredBy": "KMQ7KREACSE7",
  "customIdentifier": "12334234e66",
  "discipline": [],
  "category": [],
  "syncVersion": "2534",
  "commentsCount": 0,
  "rfiTypeId": "92da943f-9f3e-408d-981d-41b4a087f7a3",
  "attachmentsCount": 0,
  "platform": "acc",
  "bridgedSource": false,
  "bridgedTarget": false,
  "bridgeSyncOutdated": false,
  "createdAt": "2025-03-13T10:59:09.249Z",
  "updatedAt": "2025-03-13T12:19:27.737Z",
  "assignedTo": [
    {
      "id": "KMQ7KREACSE7",
      "type": "user"
    }
  ],
  "architects": [
    {
      "id": "WZJ23QYPPEBML8BG",
      "type": "user"
    },
    {
      "id": "Z762FZR9LSEHQASK",
      "type": "user"
    }
  ],
  "responses": [
    {
      "id": "07bd6f68-a9e0-4459-b9c2-686cc991509f",
      "text": "dwdq",
      "createdBy": "KMQ7KREACSE7",
      "updatedBy": null,
      "onBehalf": "Z762FZR9LSEHQASK",
      "status": "answered",
      "state": "submitted",
      "rfiId": "48ae70ef-c215-4781-a7c2-394afaae0d9c",
      "containerId": "afc6e536-3a12-4ecf-8302-3f283d50dc6f",
      "syncVersion": "650",
      "createdAt": "2025-03-13T12:08:47.232Z",
      "updatedAt": "2025-03-13T12:08:47.232Z",
      "deletedAt": null,
      "isEditable": false
    }
  ],
  "draftResponses": [],
  "permittedActions": {
    "linkPCO": true,
    "createDocumentReference": true,
    "removeDocumentReference": true,
    "share": false,
    "updateRfi": {
      "useCustomAttributes": true,
      "permittedAttributes": [
        {
          "name": "assignedTo",
          "values": [
            {
              "value": "KMQ7KREACSE7",
              "type": "user"
            },
            {
              "value": "NVE27LREMTDB5ZM4",
              "type": "user"
            }
          ]
        },
        {
          "name": "category"
        },
        {
          "name": "coReviewers"
        },
        {
          "name": "costImpact"
        },
        {
          "name": "customFields"
        },
        {
          "name": "customIdentifier"
        },
        {
          "name": "discipline"
        },
        {
          "name": "watchers"
        },
        {
          "name": "documentReferenceCreate"
        },
        {
          "name": "documentReferenceRemove"
        },
        {
          "name": "dueDate"
        },
        {
          "name": "lbs"
        },
        {
          "name": "locations"
        },
        {
          "name": "locationDescription"
        },
        {
          "name": "nudge"
        },
        {
          "name": "officialResponse"
        },
        {
          "name": "officialResponseStatus"
        },
        {
          "name": "priority"
        },
        {
          "name": "question"
        },
        {
          "name": "reference"
        },
        {
          "name": "scheduleImpact"
        },
        {
          "name": "sendNudgeEmail"
        },
        {
          "name": "suggestedAnswer"
        },
        {
          "name": "title"
        },
        {
          "name": "status",
          "values": [
            {
              "value": "open"
            },
            {
              "value": "closed"
            },
            {
              "value": "void"
            }
          ]
        }
      ],
      "permittedStatuses": {
        "wfUS": [
          {
            "status": "open",
            "requiredAttributes": [
              {
                "name": "returnForReviewerList"
              }
            ],
            "permittedAttributes": [
              {
                "name": "category"
              },
              {
                "name": "coReviewers"
              },
              {
                "name": "costImpact"
              },
              {
                "name": "customFields"
              },
              {
                "name": "customIdentifier"
              },
              {
                "name": "discipline"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              },
              {
                "name": "documentReferenceRemove"
              },
              {
                "name": "dueDate"
              },
              {
                "name": "lbs"
              },
              {
                "name": "locations"
              },
              {
                "name": "locationDescription"
              },
              {
                "name": "nudge"
              },
              {
                "name": "officialResponse"
              },
              {
                "name": "priority"
              },
              {
                "name": "question"
              },
              {
                "name": "reference"
              },
              {
                "name": "rfiTypeId"
              },
              {
                "name": "scheduleImpact"
              },
              {
                "name": "sendNudgeEmail"
              },
              {
                "name": "suggestedAnswer"
              },
              {
                "name": "title"
              }
            ],
            "maxAssignees": 10
          },
          {
            "status": "closed",
            "requiredAttributes": [
              {
                "name": "officialResponse"
              },
              {
                "name": "officialResponseStatus"
              }
            ],
            "permittedAttributes": [
              {
                "name": "bridgeTargetProjectIds"
              },
              {
                "name": "watchers"
              },
              {
                "name": "documentReferenceCreate"
              }
            ],
            "maxAssignees": 1
          },
          {
            "status": "void",
            "requiredAttributes": [],
            "permittedAttributes": [],
            "maxAssignees": 1
          }
        ],
        "wfEU": []
      }
    },
    "createComment": true,
    "createResponse": false,
    "remainingReviewers": [
      {
        "id": "WZJ23QYPPEBML8BG",
        "type": "user"
      }
    ],
    "createResponseOnBehalf": false
  },
  "attachments": [],
  "officialResponseActors": [],
  "locations": [],
  "maxAssignees": 1,
  "watchers": []
}

```

Show More

The response confirms that the RFI status is now `answered`. You can now proceed to the official response step.

## [Step 6: Submit an Official Response and Close the RFI](#step-6-submit-an-official-response-and-close-the-rfi)

Once the RFI has been transitioned to `answered` status, the manager can close the RFI by submitting an official response. This marks the end of the RFI workflow.

To close the RFI, you must update the following fields:
> - `status`: Set to `closed`.
> - `officialResponse`: The final response text.
> - `officialResponseStatus`: The status of the official response (such as `approved` or `notApproved`).

Before proceeding, make sure that:
> - The current RFI status is `answered`.
> - The user performing the transition has a workflow role with permission to close the RFI.
> - The `permittedStatuses` include `closed` and specify `officialResponse` and `officialResponseStatus` as required attributes.

### Request

```
curl --location --request PATCH 'https://developer.api.autodesk.com/construction/rfis/v3/projects/afc6e536-3a12-4ecf-8302-3f283d50dc6f/rfis/48ae70ef-c215-4781-a7c2-394afaae0d9c' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer l0ZSIsImRhdGE6cmVhZCIsImRhdGE6Y3JlYXRlIiwiZGF0YTpzZWFyY2gi' \
--data '{
  "status": "closed",
  "officialResponse": "Yes, the pipe size is correct according to the approved plans.",
  "officialResponseStatus": "approved"
}'

```

Show More

### Response

```
{
  "id": "48ae70ef-c215-4781-a7c2-394afaae0d9c",
  "title": "Pipe Size",
  "status": "closed",
  "previousStatus": "answered",
  "officialResponse": "Yes, the pipe size is correct according to the approved plans.",
  "officialResponseStatus": "approved",
  "answeredBy": "KMQ7KREACSE7",
  "updatedBy": "KMQ7KREACSE7",
  "updatedAt": "2025-03-13T12:25:14.000Z",
  ...
}

```

Show More

The RFI is considered closed and cannot be updated further unless reopened. This is the final step in the RFI workflow.

Congratulations! You have successfully transitioned an ACC RFI from draft to closed.
