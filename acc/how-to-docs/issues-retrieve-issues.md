# Retrieve Issues

Source: https://aps.autodesk.com/en/docs/acc/tutorials/issues/retrieve-issues/

---

# Retrieve Issues

This tutorial demonstrates how to retrieve information about a project’s issues, including details about their associated comments and attachments.

Note that we do not currently support document-related (pusphin) issues or linked documents.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with the `data:read` scope.
- Verify that you have access to the relevant hub and Forma project.
- Find the relevant project ID for the project you want to retrieve the issues from by following the [Retrieve a Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the project ID is `f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`.

## [Find Issue Information](#find-issue-information)

Use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) to retrieve the project’s issues, by calling [GET issues](../http-docs/http-issues-issues-GET.md).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/issues' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 10,
    "offset": 100,
    "totalResults": 25
  },
  "results": [
    {
      "id": "3570f222-6c54-4b01-90e6-e701749f0222",
      "containerId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "deleted": false,
      "displayId": 7,
      "title": "Door missing a screw",
      "description": "The door is missing a screw, please fix this",
      "snapshotUrn": "",
      "issueTypeId": "8770f222-6c54-4e01-93e6-e701749f0222",
      "issueSubtypeId": "1370f222-6c54-3a01-93e6-e701749f0222",
      "status": "open",
      "assignedTo": "A3RGM375QTZ7",
      "assignedToType": "user",
      "dueDate": "2018-07-25",
      "startDate": "1982-06-01",
      "locationId": "35de6f24-39f5-4808-ba5f-6cbbe2a858e1",
      "locationDetails": "issue location details",
      "linkedDocuments": [
        {}
      ],
      "links": [
        {}
      ],
      "ownerId": "",
      "rootCauseId": "2370f222-6c54-3a01-93e6-f701772f0222",
      "officialResponse": {},
      "issueTemplateId": "",
      "permittedStatuses": [
        "open"
      ],
      "permittedAttributes": [
        "title"
      ],
      "published": true,
      "permittedActions": {},
      "commentCount": 3,
      "attachmentCount": "",
      "openedBy": "A3RGM375QTZ7",
      "openedAt": "2018-07-22T15:05:58.033Z",
      "closedBy": "A3RGM375QTZ7",
      "closedAt": "2018-07-22T15:05:58.033Z",
      "createdBy": "A3RGM375QTZ7",
      "createdAt": "2018-07-22T15:05:58.033Z",
      "updatedBy": "A3RGM375QTZ7",
      "updatedAt": "2018-07-22T15:05:58.033Z",
      "watchers": [
        "A3RGM375QTZ7"
      ],
      "customAttributes": [
        {
          "attributeDefinitionId": "2220f222-6c54-4b01-90e6-d701748f0888",
          "value": "368",
          "type": "numeric",
          "title": "Cost Impact ($)"
        }
      ]
    }
  ]
}

```

Show More

The response payload includes the issue IDs (`data.id`).
