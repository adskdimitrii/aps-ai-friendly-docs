# Submit an RFI Response

Source: https://aps.autodesk.com/en/docs/acc/tutorials/rfis3/rfi-response/

---

# Submit an RFI Response

This tutorial demonstrates how to submit a response to an RFI in a Forma project. The steps include verifying the user’s permissions, creating a response, and optionally including file attachments.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:write` `account:read` scopes.
- Verify that you have access to the relevant hub and Forma project.
- Find the relevant project ID for the project you want to create an RFI in by following the [Retrieve a Hub ID and Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the hub ID is `g5s4e3b5-vbta-6b02-d23a-5d55f36ba876`, the project ID is `ce8edd30-ef28-467c-8d99-7d7051097ee0` and the RFI ID is `a1d12f69-3c02-4bba-936d-cccd73f001ee`.

## [Step 1: Check if the User Can Submit a Response](#step-1-check-if-the-user-can-submit-a-response)

We recommend calling [GET rfis/:rfiId](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-V3-rfisrfiid-GET/) to check whether the user has permission to submit a response to the RFI.
A user can submit a response if either `permittedActions.createResponse` or `permittedActions.createResponseOnBehalf` is set to `true`.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/ce8edd30-ef28-467c-8d99-7d7051097ee0/rfis/a1d12f69-3c02-4bba-936d-cccd73f001ee' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

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
            },
            {
              "value": "Z8YKNL3KGDVN",
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
    "createResponseOnBehalf": true
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

### Important Response Fields

Look for the `permittedActions` object in the response.

- `createResponse` – If `true`, the user can submit a response directly.
- `createResponseOnBehalf` – If `true`, the user can submit a response on behalf of another project member.
- If both are `false`, the user does not have permission to respond via the API.

If `createResponseOnBehalf` is `true`, you must include the `onBehalf` field when posting the response. The value must be a valid user ID (e.g., from `assignedTo` or `reviewers`).

## [Step 2: (Optional) Attach Files to the RFI Response](#step-2-optional-attach-files-to-the-rfi-response)

You can include one or more file attachments as part of the RFI response.
To do this, upload each file to the `virtual folder` associated with the RFI using the steps described in the [Upload Attachments to RFIs](https://aps.autodesk.com/en/docs/acc/v1/tutorials/upload-document-rfis/) tutorial.

After uploading a file, collect the following values for each attachment. These values are required when creating the RFI response payload.

- `objectId` – The unique identifier for the uploaded file. This value also serves as the `storageUrn` when attaching the file to the RFI response.
- `objectKey` – The file name used in the object storage service (OSS).

### Example Attachment Data

```
{
  "objectId": "urn:adsk.objects:os.object:wip.dm.prod/a2615894-f133-4334-a235-5f8d558a2467.pdf",
  "objectKey": "a2615894-f133-4334-a235-5f8d558a2467.pdf"
}

```

## [Step 3: Submit the RFI Response](#step-3-submit-the-rfi-response)

Once you’ve verified that the user has the required permissions and optionally uploaded attachments, you can create the RFI response.

Call [POST response](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-V3-response-POST/) using the project ID (`ce8edd30-ef28-467c-8d99-7d7051097ee0`), the RFI ID (`rfiId`) (`a1d12f69-3c02-4bba-936d-cccd73f001ee`). Include the response text, and if applicable, the `onBehalf` field and attachments.

### Important Request Fields

- `text` – The response text.
- `onBehalf` – Required if `createResponse` is false and `createResponseOnBehalf` is true.
- `attachments` – An optional array of attachment objects. Each object must include:
  * `attachmentType` – Set to `rfiResponse`.
  * `displayName` – The name that will appear in the UI.
  * `fileName` – The actual OSS file name (same as `objectKey`).
  * `storageUrn` – The URN of the uploaded file (same as `objectId` from Step 2).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/ce8edd30-ef28-467c-8d99-7d7051097ee0/rfis/a1d12f69-3c02-4bba-936d-cccd73f001ee/responses' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "status": "answered",
        "text": "This is my response text",
        "onBehalf": "878RRNYF8QAB",
        "attachments": [
          {
            "attachmentType": "rfiResponse",
            "displayName": "My attachments.pdf",
            "fileName": "a2615894-f133-4334-a235-5f8d558a2467.pdf",
            "storageUrn": "urn:adsk.objects:os.object:wip.dm.prod/a2615894-f133-4334-a235-5f8d558a2467.pdf"
          }
        ]
      }'

```

Show More

### Response

```
{
  "rfi": {
    "id": "a1d12f69-3c02-4bba-936d-cccd73f001ee",
    "title": "RFIs tutorial",
    "question": "what should be the color of the outer wall?",
    "status": "open",
    "virtualFolderUrn": "urn:adsk.wipqa:fs.folder:co.U1jbZlVKT--j9dg3WWpLlg",
    "createdBy": "KMQ7KREACSE7",
    "openedBy": "KMQ7KREACSE7",
    "openedAt": "2025-03-09T16:28:19.239Z",
    "workflowType": "US",
    "type": "Rfi",
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
    "clientCreatedAt": "2025-03-09T16:28:19.261Z",
    "clientUpdatedAt": "2025-03-09T16:28:19.261Z",
    "mentionees": [],
    "createdByRole": "sc",
    "customIdentifier": "G30ww16r8",
    "customIdentifierSort": {
      "text": "G30ww16r",
      "number": "8"
    },
    "discipline": [],
    "category": [],
    "commentsCount": 0,
    "rfiTypeId": "294f293c-aad0-43db-ba2b-c7eed815bbb7",
    "attachmentsCount": 0,
    "platform": "acc",
    "rfiDatesMigrated": "Sun Mar 09 2025 16:28:19 GMT+0000 (Coordinated Universal Time)",
    "bridgedSource": false,
    "bridgedTarget": false,
    "bridgeSyncOutdated": false,
    "createdAt": "2025-03-09T16:28:19.261Z",
    "updatedAt": "2025-03-09T16:28:54.020Z",
    "assignedTo": [
      {
        "id": "878RRNYF8QAB",
        "type": "user"
      },
      {
        "id": "N7W3QVQ6ANSD",
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
        "isEditable": true
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
          "wfEU": []
        }
      },
      "createComment": true,
      "createResponse": false,
      "remainingReviewers": [
        {
          "id": "N7W3QVQ6ANSD",
          "type": "user"
        }
      ],
      "createResponseOnBehalf": true
    },
    "officialResponseActors": [],
    "locations": [],
    "maxAssignees": 10,
    "watchers": []
  },
  "response": {
    "createdAt": "2025-03-09T20:20:40.324Z",
    "updatedAt": "2025-03-09T20:20:40.324Z",
    "id": "0fb9cdab-8268-4346-80d3-7bc35c1c4fa9",
    "createdBy": "KMQ7KREACSE7",
    "containerId": "ce8edd30-ef28-467c-8d99-7d7051097ee0",
    "rfiId": "a1d12f69-3c02-4bba-936d-cccd73f001ee",
    "text": "This is my response",
    "onBehalf": "878RRNYF8QAB",
    "status": "answered",
    "state": "submitted"
  },
  "responseAttachments": {
    "attachments": [
        {
          "attachmentId": "2a748b51-9540-4e76-af98-3d170fbd1a63",
          "rfiId": "a1d12f69-3c02-4bba-936d-cccd73f001ee",
          "attachmentType": "rfiResponse",
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
    ]
  }
}

```

Show More

Congratulations! You have successfully submitted an RFI response.
The response is now visible in the Forma RFI UI, along with any files you attached.
