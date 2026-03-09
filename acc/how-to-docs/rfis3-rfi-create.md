# Create an RFI

Source: https://aps.autodesk.com/en/docs/acc/tutorials/rfis3/rfi-create/

---

# Create an RFI

This tutorial demonstrates how to create an RFI item for an Autodesk Construction Cloud (ACC) project. The steps include verifying the userâs permissions, retrieving the RFI type ID, retrieving the next custom identifier (optional), identifying the assigneeâs ID, and creating the RFI.

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:write` `account:read` scopes.
- Verify that you have access to the relevant account and ACC project.
- Find the relevant project ID for the project you want to create an RFI in by following the [Retrieve an Account ID and Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the account ID is `g5s4e3b5-vbta-6b02-d23a-5d55f36ba876`, and the project ID is `ce8edd30-ef28-467c-8d99-7d7051097ee0`.

## [Step 1: Verify the Userâs Permissions](#step-1-verify-the-user-s-permissions)

To check if the user has permission to create RFIs, call [GET users/me](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-v3-users-me-GET/).

If the `permittedActions.createRfi` object appears in the response, the user has permission to create RFIs. This object includes a list of allowed initial statuses (`permittedStatuses`), each with its own required and optional attributes. It also specifies which users the RFI can be assigned to.

For example, to create an RFI with status `submitted`, you must include all fields listed under `requiredAttributes` for that status (such as `title` and `assignedTo`), and choose an `assignedTo` value from the permitted list.

If `permittedActions.createRfi` is not present, the user does **not** have permission to create RFIs in the project.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/ce8edd30-ef28-467c-8d99-7d7051097ee0/users/me' \
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

From the response above, you can extract the required information to build your RFI request:

- The user ID is `KMQ7KREACSE7`.
- Under workflow `wfUS`, the user can create an RFI in the `draft`, `submitted`, or `open` status.
- To create a `draft` RFI:
  * The required attribute is `title`.
  * The permitted `assignedTo` value is `KMQ7KREACSE7`.
- To create a `submitted` RFI:
  * Required attributes: `title` and `assignedTo`.
  * Permitted `assignedTo` values: `2UDYLKMEVARC`, `336SNF7WG2KU`, `V3KTJ2YVRF29`.

In the next step, youâll use these values to build the request body. Make sure the status and required fields you send match whatâs allowed for your workflow, or the request will be rejected.

## [Step 2: Find the RFI Type ID](#step-2-find-the-rfi-type-id)

To create an RFI, you must include the RFI type ID (`rfiTypeId`) in the request body.

To retrieve a list of available RFI types for the project, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-V3-types-GET/) using the project ID (`ce8edd30-ef28-467c-8d99-7d7051097ee0`).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/ce8edd30-ef28-467c-8d99-7d7051097ee0/rfi-types' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "id": "294f293c-aad0-43db-ba2b-c7eed815bbb7",
      "containerId": "ce8edd30-ef28-467c-8d99-7d7051097ee0",
      "name": "My_rfi_type",
      "wfType": "US",
      "status": "inactive",
      "syncVersion": "181",
      "createdAt": "2023-07-11T05:55:38.116Z",
      "updatedAt": "2023-09-15T06:54:12.082Z",
      "isDefault": true,
      "projectReviewer": [
        {
          "id": "933GPNQYBGD4",
          "type": "user"
        }
      ],
      "projectCoordinator": []
    },
    {
      "id": "728329b2-00a7-4958-8b7b-0e50620cd7f2",
      "containerId": "ce8edd30-ef28-467c-8d99-7d7051097ee0",
      "name": "01",
      "wfType": "EU",
      "status": "active",
      "syncVersion": "442",
      "createdAt": "2024-09-25T08:35:39.254Z",
      "updatedAt": "2024-09-25T08:35:39.255Z",
      "isDefault": false,
      "projectReviewer": [],
      "projectCoordinator": []
    },
    {
      "id": "f55fb338-56bd-4456-8c08-82ff972625e3",
      "containerId": "ce8edd30-ef28-467c-8d99-7d7051097ee0",
      "name": "07_test_10",
      "wfType": "US",
      "status": "inactive",
      "syncVersion": "160",
      "createdAt": "2023-07-11T07:07:33.750Z",
      "updatedAt": "2023-07-11T08:12:58.914Z",
      "isDefault": false,
      "projectReviewer": [],
      "projectCoordinator": []
    },
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 3
  }
}

```

Show More

Find the RFI type (`rfiType`) - `results[rfiTypes.[name]]` (`My_rfi_type`), and note the type ID (rfiType ID) - `results[rfiTypes.[id]]` (`294f293c-aad0-43db-ba2b-c7eed815bbb7`).

## [Step 3: (Optional) Find Next Custom Identifier](#step-3-optional-find-next-custom-identifier)

If your project uses custom identifiers for RFIs, you can retrieve the next available value by calling [GET custom-identifier](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-V3-customidentifier-GET/).

Use the project ID (`ce8edd30-ef28-467c-8d99-7d7051097ee0`) in the request.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfi/v3/projects/ce8edd30-ef28-467c-8d99-7d7051097ee0/custom-identifier' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "current": "G30ww16r7",
  "next": "G30ww16r8"
}

```

Use the `next` value (e.g., `G30ww16r8`) as the `customIdentifier` when creating the RFI.

## [Step 4: (Optional) Find Custom Attribute Definitions](#step-4-optional-find-custom-attribute-definitions)

If your project uses custom attributes, you must first retrieve their definitions before assigning values. Call [GET attributes](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-V3-attributes-GET/) using the project ID (`ce8edd30-ef28-467c-8d99-7d7051097ee0`).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/ce8edd30-ef28-467c-8d99-7d7051097ee0/attributes' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "id": "176e1daf-1b05-4a85-92a0-17e4db0631ba",
      "containerId": "ce8edd30-ef28-467c-8d99-7d7051097ee0",
      "name": "545",
      "type": "numeric",
      "status": "active",
      "description": "2522",
      "createdBy": "PVC2VDW3PFQEC6SX",
      "syncVersion": "617",
      "createdAt": "2025-02-10T07:40:02.562Z",
      "updatedAt": "2025-02-10T07:40:02.562Z"
    },
    {
      "id": "da90b250-1541-42db-a12b-8ed05f40031b",
      "containerId": "ce8edd30-ef28-467c-8d99-7d7051097ee0",
      "name": "55",
      "type": "text",
      "status": "active",
      "createdBy": "PVC2VDW3PFQEC6SX",
      "syncVersion": "622",
      "createdAt": "2025-02-11T02:40:36.908Z",
      "updatedAt": "2025-02-11T02:40:36.908Z"
    },
    {
      "id": "09b37029-bf1b-47b6-b9f1-c56735b2fc52",
      "containerId": "ce8edd30-ef28-467c-8d99-7d7051097ee0",
      "name": "5545",
      "type": "text",
      "multipleChoice": true,
      "status": "active",
      "createdBy": "WWSQPJXYF2LJ",
      "updatedBy": "W5PJDVC3P4XTCB3Y",
      "syncVersion": "568",
      "createdAt": "2024-03-29T06:15:33.864Z",
      "updatedAt": "2024-05-03T18:54:38.725Z",
      "possibleValues": [
        {
          "name": "111",
          "id": "47b60bcc-3b57-4506-ac81-c078f70f292a"
        },
        {
          "name": "1252",
          "id": "3ff28f60-33ae-4b90-a55f-53ab305c9591"
        }
      ]
    }
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 3
  }
}

```

Show More

Search for the custom attribute mapping IDs and check the data in the corresponding object. For this tutorial, we will use the custom attribute ID (`09b37029-bf1b-47b6-b9f1-c56735b2fc52`) and the custom attribute value (`1252`).

## [Step 5: (Optional) Find the ID of the Assignee](#step-5-optional-find-the-id-of-the-assignee)

To find the ID of the assignee, use the [GET projects/users](../http-docs/http-admin-projectsprojectId-users-GET.md) from the Admin API.

## [Step 6: Create the RFI](#step-6-create-the-rfi)

Call [POST rfis](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-V3-rfi-POST/) using the project ID (`ce8edd30-ef28-467c-8d99-7d7051097ee0`), the RFI type (`rfiTypeId`) ID (`294f293c-aad0-43db-ba2b-c7eed815bbb7`), and the custom identifier (`G30ww16r8`) the custom attribute ID (`09b37029-bf1b-47b6-b9f1-c56735b2fc52`) and the custom attribute value (`1252`).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/ce8edd30-ef28-467c-8d99-7d7051097ee0/rfis' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "status": "open",
        "title": "RFIs tutorial",
        "question": "what should be the color of the outer wall?",
        "suggestedAnswer": "blue",
        "rfiTypeId": "294f293c-aad0-43db-ba2b-c7eed815bbb7",
        "customIdentifier": "G30ww16r8",
        "customAttributes": [
          {
            "id": "09b37029-bf1b-47b6-b9f1-c56735b2fc52",
            "values": ["3ff28f60-33ae-4b90-a55f-53ab305c9591"]
          }
        ],
        "assignedTo": [
          {
            "id": "N7W3QVQ6ANSD",
            "type": "user"
          },
          {
            "id": "878RRNYF8QAB",
            "type": "user"
          }
        ]
      }'

```

Show More

### Response

```
{
  "createdAt": "2025-03-09T16:28:19.261Z",
  "updatedAt": "2025-03-09T16:28:19.261Z",
  "id": "a1d12f69-3c02-4bba-936d-cccd73f001ee",
  "coReviewers": [],
  "discipline": [],
  "category": [],
  "commentsCount": 0,
  "attachmentsCount": 0,
  "bridgedSource": false,
  "bridgedTarget": false,
  "bridgeSyncOutdated": false,
  "rfiTypeId": "294f293c-aad0-43db-ba2b-c7eed815bbb7",
  "status": "open",
  "title": "RFIs tutorial",
  "question": "what should be the color of the outer wall?",
  "suggestedAnswer": "blue",
  "customIdentifier": "G30ww16r8",
  "workflowType": "US",
  "createdBy": "KMQ7KREACSE7",
  "managerId": "KMQ7KREACSE7",
  "reviewers": [
    {
      "id": "N7W3QVQ6ANSD",
      "type": "user"
    },
    {
      "id": "878RRNYF8QAB",
      "type": "user"
    }
  ],
  "platform": "acc",
  "customAttributes": [
    {
      "id": "09b37029-bf1b-47b6-b9f1-c56735b2fc52",
      "values": [
        "3ff28f60-33ae-4b90-a55f-53ab305c9591"
      ]
    }
  ],
  "assignedTo": [
    {
      "id": "N7W3QVQ6ANSD",
      "type": "user"
    },
    {
      "id": "878RRNYF8QAB",
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
              "value": "N7W3QVQ6ANSD",
              "type": "user"
            },
            {
              "value": "878RRNYF8QAB",
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
                    "value": "2UDYLKMEVARC",
                    "type": "user"
                  },
                  {
                    "value": "336SNF7WG2KU",
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
        "wfEU": []
      }
    },
    "createComment": true,
    "createResponse": false,
    "remainingReviewers": [
      {
        "id": "N7W3QVQ6ANSD",
        "type": "user"
      },
      {
        "id": "878RRNYF8QAB",
        "type": "user"
      }
    ],
    "createResponseOnBehalf": true
  },
  "architects": [
    {
      "id": "N7W3QVQ6ANSD",
      "type": "user"
    },
    {
      "id": "878RRNYF8QAB",
      "type": "user"
    }
  ],
  "officialResponseActors": [],
  "locations": [],
  "maxAssignees": 10,
  "watchers": []
}

```

Show More

Note that virtual folder creation is triggered as a separate asynchronous job when an RFI is created.
Until this folder is successfully created, users cannot upload files into it.
To confirm that the folder is ready, call GET rfis/:id </en/docs/acc/v1/reference/http/rfis-rfis-id-GET/> and check that the `virtualFolderUrn` field appears in the response.

Congratulations! You have created an ACC RFI.
