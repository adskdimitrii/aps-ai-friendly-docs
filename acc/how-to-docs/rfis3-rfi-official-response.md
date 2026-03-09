# Create RFI Official Response

Source: https://aps.autodesk.com/en/docs/acc/tutorials/rfis3/rfi-official-response/

---

# Create RFI Official Response

This tutorial demonstrates how to create an official response for an RFI in an Autodesk Construction Cloud (ACC) project. The steps include verifying the userâs permissions, creating an official response, and optionally adding attachments. You can only create an official response for an RFI that is in open status and that has not yet received an official response. You must be assigned to the RFI or included in its list of permitted reviewers.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:write` `account:read` scopes.
- Verify that you have access to the relevant account and ACC project.
- Find the relevant project ID for the project you want to create an RFI in by following the [Retrieve an Account ID and Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the account ID is `g5s4e3b5-vbta-6b02-d23a-5d55f36ba876`, the project ID is `ce8edd30-ef28-467c-8d99-7d7051097ee0` and the RFI ID is `a1d12f69-3c02-4bba-936d-cccd73f001ee`.

## [Step 1: Find the RFI ID](#step-1-find-the-rfi-id)

To post an official response, you need the RFI ID. Call [POST rfis:search](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-V3-rfi-search-POST/) using the project ID (`ce8edd30-ef28-467c-8d99-7d7051097ee0`) to search for RFIs in the project.

### Request

```
curl -X POST 'https://developer.api.autodesk.com/construction/rfis/v3/projects/ce8edd30-ef28-467c-8d99-7d7051097ee0/rfis:search' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'

```

### Response

```
{
  "results": [
    {
      "id": "a1d12f69-3c02-4bba-936d-cccd73f001ee",
      "title": "Window Flashing Detail at East Elevation",
      "status": "open",
      "rfiTypeId": "294f293c-aad0-43db-ba2b-c7eed815bbb7",
      ...
    }
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 1
  }
}

```

Show More

Take note of the RFI ID (`a1d12f69-3c02-4bba-936d-cccd73f001ee`). You will use this ID in the next step.

## [Step 2: Verify Permissions and RFI Status](#step-2-verify-permissions-and-rfi-status)

To confirm the user can create an official response, call [GET rfis/:rfiId](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-V3-rfisrfiid-GET/) using the project ID and RFI ID.

Only users with Manager permissions can create an official response, and only if:
> - The RFI `status` is answered.
> - The RFI does not yet have an official response.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/ce8edd30-ef28-467c-8d99-7d7051097ee0/rfis/a1d12f69-3c02-4bba-936d-cccd73f001ee' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "answeredAt": "2025-03-10T10:03:17.906Z",
  "answeredBy": "KMQ7KREACSE7",
  "id": "a1d12f69-3c02-4bba-936d-cccd73f001ee",
  "title": "RFIs tutorial",
  "question": "what should be the color of the outer wall?",
  "status": "answered",
  "previousStatus": "open",
  "virtualFolderUrn": "urn:adsk.wipqa:fs.folder:co.U1jbZlVKT--j9dg3WWpLlg",
  "createdBy": "KMQ7KREACSE7",
  "updatedBy": "KMQ7KREACSE7",
  "workflowType": "US",
  "suggestedAnswer": "blue",
  "coReviewers": [],
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
  "customIdentifier": "G30ww16r8",
  "discipline": [],
  "category": [],
  "syncVersion": "11870",
  "commentsCount": 0,
  "rfiTypeId": "294f293c-aad0-43db-ba2b-c7eed815bbb7",
  "attachmentsCount": 1,
  "platform": "acc",
  "bridgedSource": false,
  "bridgedTarget": false,
  "bridgeSyncOutdated": false,
  "createdAt": "2025-03-09T16:28:19.261Z",
  "updatedAt": "2025-03-10T10:03:17.909Z",
  "assignedTo": [
    {
      "id": "KMQ7KREACSE7",
      "type": "user"
    }
  ],
  "architects": [
    {
      "id": "878RRNYF8QAB",
      "type": "user"
    },
    {
      "id": "N7W3QVQ6ANSD",
      "type": "user"
    }
  ],
  "responses": [
    {
      "id": "0fb9cdab-8268-4346-80d3-7bc35c1c4fa9",
      "text": "This is my response",
      "createdBy": "KMQ7KREACSE7",
      "updatedBy": null,
      "onBehalf": "878RRNYF8QAB",
      "status": "answered",
      "state": "submitted",
      "rfiId": "a1d12f69-3c02-4bba-936d-cccd73f001ee",
      "containerId": "ce8edd30-ef28-467c-8d99-7d7051097ee0",
      "syncVersion": "192",
      "createdAt": "2025-03-09T20:20:40.324Z",
      "updatedAt": "2025-03-09T20:20:40.324Z",
      "deletedAt": null,
      "isEditable": false
    },
    {
      "id": "840a5b4d-7bbb-4132-aa5c-37509c082e56",
      "text": "This is my response2",
      "createdBy": "KMQ7KREACSE7",
      "updatedBy": null,
      "onBehalf": "N7W3QVQ6ANSD",
      "status": "answered",
      "state": "submitted",
      "rfiId": "a1d12f69-3c02-4bba-936d-cccd73f001ee",
      "containerId": "ce8edd30-ef28-467c-8d99-7d7051097ee0",
      "syncVersion": "193",
      "createdAt": "2025-03-10T10:03:17.900Z",
      "updatedAt": "2025-03-10T10:03:17.900Z",
      "deletedAt": null,
      "isEditable": false
    }
  ],
  "customAttributes": [
    {
      "id": "09b37029-bf1b-47b6-b9f1-c56735b2fc52",
      "values": [
        "3ff28f60-33ae-4b90-a55f-53ab305c9591"
      ]
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
              "value": "2UDYLKMEVARC",
              "type": "user"
            },
            {
              "value": "336SNF7WG2KU",
              "type": "user"
            }
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
    "remainingReviewers": [],
    "createResponseOnBehalf": false
  },
  "draftResponses": [],
  "officialResponseActors": [],
  "locations": [],
  "maxAssignees": 1,
  "watchers": []
}

```

Show More

Verify the following:
> - The RFI `status` is `answered`.
> - The current user is listed under `managerId` or permitted reviewers.
> - The `officialResponse` field is not yet populated.

## [Step 3: (Optional) Upload Attachments](#step-3-optional-upload-attachments)

To include attachments in your official response, first upload the file to Autodeskâs Object Storage Service (OSS). For detailed steps, see the [Upload Attachments tutorial](https://aps.autodesk.com/en/docs/acc/v1/tutorials/rfi-upload/).

After uploading, note the following values from the response:
> - `objectId` â The unique identifier for the uploaded file.
> - `objectKey` â The file name used in storage.

```
{
  "objectId": "urn:adsk.objects:os.object:wip.dm.prod/a2615894-f133-4334-a235-5f8d558a2467.pdf",
  "objectKey": "a2615894-f133-4334-a235-5f8d558a2467.pdf"
}

```

These values will be required when adding attachments to your RFI official response.

## [Step 4: Create the Official Response](#step-4-create-the-official-response)

To create the official response, call [PATCH rfis/:rfiId](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-V3-rfisrfiid-PATCH/) using the project ID (`ce8edd30-ef28-467c-8d99-7d7051097ee0`), and the RFI ID (`rfiId`) (`a1d12f69-3c02-4bba-936d-cccd73f001ee`).

Set the following fields:
> - `status` to `closed`
> - `officialResponse` to your response text
> - `officialResponseStatus` to `answered`
> - Optionally, include attachments

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/ce8edd30-ef28-467c-8d99-7d7051097ee0/rfis/a1d12f69-3c02-4bba-936d-cccd73f001ee' \
  -X 'PATCH' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "status": "closed",
        "officialResponse": "This is my official response text",
        "officialResponseStatus": "answered",
        "attachments": [
          {
            "attachmentType": "rfiOfficialResponse"
            "displayName": "My attachments.pdf"
            "fileName": "a2615894-f133-4334-a235-5f8d558a2467.pdf"
            "storageUrn": "urn:adsk.objects:os.object:wip.dm.prod/a2615894-f133-4334-a235-5f8d558a2467.pdf"
          }
        ]
      }'

```

Show More

### Response

```
{
  "id": "a1d12f69-3c02-4bba-936d-cccd73f001ee",
  "title": "RFIs tutorial",
  "question": "what should be the color of the outer wall?",
  "status": "closed",
  "previousStatus": "answered",
  "virtualFolderUrn": "urn:adsk.wipqa:fs.folder:co.U1jbZlVKT--j9dg3WWpLlg",
  "officialResponse": "This is my official response",
  "officialResponseStatus": "answered",
  "createdBy": "KMQ7KREACSE7",
  "updatedBy": "KMQ7KREACSE7",
  "closedBy": "KMQ7KREACSE7",
  "closedAt": "2025-03-10T11:12:17.420Z",
  "workflowType": "US",
  "suggestedAnswer": "blue",
  "coReviewers": [],
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
  "answeredAt": "2025-03-10T10:03:17.906Z",
  "answeredAtV2": "2025-03-10T11:12:17.420Z",
  "answeredBy": "KMQ7KREACSE7",
  "answeredByV2": "KMQ7KREACSE7",
  "customIdentifier": "G30ww16r8",
  "discipline": [],
  "category": [],
  "syncVersion": "11871",
  "commentsCount": 0,
  "rfiTypeId": "294f293c-aad0-43db-ba2b-c7eed815bbb7",
  "attachmentsCount": 0,
  "officialResponseActors": [
    {
      "id": "KMQ7KREACSE7",
      "type": "user"
    }
  ],
  "officialResponseEditByManagerState": true,
  "platform": "acc",
  "bridgedSource": false,
  "bridgedTarget": false,
  "bridgeSyncOutdated": false,
  "createdAt": "2025-03-09T16:28:19.261Z",
  "updatedAt": "2025-03-10T11:12:17.443Z",
  "respondedAt": "2025-03-10T11:12:17.420Z",
  "respondedBy": "KMQ7KREACSE7",
  "assignedTo": [
    {
      "id": "KMQ7KREACSE7",
      "type": "user"
    }
  ],
  "architects": [
    {
      "id": "878RRNYF8QAB",
      "type": "user"
    },
    {
      "id": "N7W3QVQ6ANSD",
      "type": "user"
    }
  ],
  "responses": [
    {
      "id": "0fb9cdab-8268-4346-80d3-7bc35c1c4fa9",
      "text": "This is my response",
      "createdBy": "KMQ7KREACSE7",
      "updatedBy": null,
      "onBehalf": "878RRNYF8QAB",
      "status": "answered",
      "state": "submitted",
      "rfiId": "a1d12f69-3c02-4bba-936d-cccd73f001ee",
      "containerId": "ce8edd30-ef28-467c-8d99-7d7051097ee0",
      "syncVersion": "192",
      "createdAt": "2025-03-09T20:20:40.324Z",
      "updatedAt": "2025-03-09T20:20:40.324Z",
      "deletedAt": null,
      "isEditable": false
    },
    {
      "id": "840a5b4d-7bbb-4132-aa5c-37509c082e56",
      "text": "This is my response2",
      "createdBy": "KMQ7KREACSE7",
      "updatedBy": null,
      "onBehalf": "N7W3QVQ6ANSD",
      "status": "answered",
      "state": "submitted",
      "rfiId": "a1d12f69-3c02-4bba-936d-cccd73f001ee",
      "containerId": "ce8edd30-ef28-467c-8d99-7d7051097ee0",
      "syncVersion": "193",
      "createdAt": "2025-03-10T10:03:17.900Z",
      "updatedAt": "2025-03-10T10:03:17.900Z",
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
            "status": "answered",
            "requiredAttributes": [],
            "permittedAttributes": [
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
            "status": "submitted",
            "requiredAttributes": [],
            "permittedAttributes": [
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
            "status": "answeredManager",
            "requiredAttributes": [],
            "permittedAttributes": [
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
  "attachments": [
    {
      "attachmentId": "2a748b51-9540-4e76-af98-3d170fbd1a63",
      "rfiId": "a1d12f69-3c02-4bba-936d-cccd73f001ee",
      "attachmentType": "rfiOfficialResponse",
      "displayName": "My attachments.pdf",
      "domainEntityId": "c2f34fa7-ec75-4755-8795-56caa0b7b342",
      "fileName": "a2615894-f133-4334-a235-5f8d558a2467.pdf"
      "fileSize": 538736,
      "fileType": "pdf",
      "docsId": "a8bc37d6-dafd-4494-aff3-34a2d4de46ad",
      "version": 1,
      "storageUrn": "urn:adsk.objects:os.object:wip.dm.prod/a2615894-f133-4334-a235-5f8d558a2467.pdf",
      "lineageUrn": "urn:adsk.wipqa:dm.lineage:qLw31tr9RJSv8zSi1N5GrQ",
      "versionUrn": "urn:adsk.wipqa:fs.file:vf.qLw31tr9RJSv8zSi1N5GrQ?version=1",
      "tipVersionUrn": "urn:adsk.wipqa:fs.file:vf.qLw31tr9RJSv8zSi1N5GrQ?version=1",
      "bubbleUrn": null,
      "createdBy": "KMQ7KREACSE7",
      "createdByName": "Jon Doe",
      "createdOn": "2025-03-09T20:17:19.000Z",
      "modifiedBy": "KMQ7KREACSE7",
      "modifiedOn": "2025-03-09T20:17:19.000Z",
      "isDeleted": false,
      "deletedBy": null,
      "deletedOn": null
    }
  ],
  "locations": [],
  "maxAssignees": 1,
  "watchers": []
}

```

Show More

Congratulations! Youâve successfully created an official response for the RFI.
