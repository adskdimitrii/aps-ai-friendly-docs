# Create Issues

Source: https://aps.autodesk.com/en/docs/acc/tutorials/issues/create-issues/

---

# Create Issues

This tutorial demonstrates how to create a Forma issue for a project. The steps include verifying the user’s permissions, finding the issue type ID, optionally, finding custom fields to add to the new issue, finding the ID of the assignee, and creating the issue.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:write` `account:read` scopes.
- Verify that you have access to the relevant hub and Forma project.
- Find the relevant project ID for the project you want to create an issue in by following the [Retrieve a Hub ID and Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the hub ID is `g5s4e3b5-vbta-6b02-d23a-5d55f36ba876`, and the project ID is `f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`.

## [Step 1: Verify the User’s Permissions](#step-1-verify-the-user-s-permissions)

We recommend that you call [GET users/me](../http-docs/http-issues-users-me-GET.md) to verify that the user has permissions to create issues for the hub. The user can create issues if the `issues.new` object appears in the response. See the [Permissions Table](https://help.autodesk.com/view/BUILD/ENU/?guid=Issues_Permissions) for more information about permissions.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/users/me' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "BXQXL7646C2R",
  "isProjectAdmin": true,
  "canManageTemplates": "",
  "issues": {
    "new": {
      "permittedActions": [
        "add_comment"
      ],
      "permittedAttributes": [
        "title"
      ],
      "permittedStatuses": [
        "open"
      ],
      "permitted_actions": [
        "add_comment"
      ],
      "permitted_attributes": [
        "title"
      ],
      "permitted_statuses": [
        "open"
      ]
    }
  },
  "permissionLevels": [
    "read",
    "write",
    "create"
  ]
}

```

Show More

The user can create issues if the `issues.new` object appears in the response. The user has Manage Issue permissions (`read`, `write`, `create`). See [GET users/me](../http-docs/http-issues-users-me-GET.md) for information about how the API permission level values map to the UI permission levels.

## [Step 2: Find the Issue Type (subtype) ID](#step-2-find-the-issue-type-subtype-id)

To create an issue you need to specify the issue type (`subtype`) ID. Note that the API terminology for issue type is issue `subtype`, and the API terminology for category is `type`. For more details about issue types, see the [Issue Type](https://help.autodesk.com/view/BUILD/ENU/?guid=Issues_Types_Categories) documentation.

To retrieve the issue type (`subtype`) ID call [GET issue-types](../http-docs/http-issues-issue-types-GET.md) using the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`). Note that by default this endpoint does not return types (`subtypes`). To return types (`subtypes`), you need to add the `include=subtypes` query string parameter.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/issue-types?include=subtypes' \
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
      "id": "1110f111-6c54-4b01-90e6-d701748f1111",
      "containerId": "a5f49f04-59bb-477c-97e6-6833cb50bdac",
      "title": "Coordination",
      "isActive": true,
      "orderIndex": 2,
      "permittedActions": [
        "edit"
      ],
      "permittedAttributes": [
        "title"
      ],
      "subtypes": [
        {
          "id": "2220f222-6c54-4b01-90e6-d701748f0222",
          "issueTypeId": "1110f111-6c54-4b01-90e6-d701748f1111",
          "title": "Clash",
          "code": "exo",
          "isActive": true,
          "orderIndex": 5,
          "isReadOnly": false,
          "permittedActions": [
            "edit"
          ],
          "permittedAttributes": [
            "title"
          ],
          "createdBy": "A3RGM375QTZ7",
          "createdAt": "2018-07-22T15:05:58.033Z",
          "updatedBy": "A3RGM375QTZ7",
          "updatedAt": "2018-07-22T15:05:58.033Z",
          "deletedBy": "A3RGM375QTZ7",
          "deletedAt": "2018-07-22T15:05:58.033Z"
        }
      ],
      "statusSet": "gg",
      "createdBy": "A3RGM375QTZ7",
      "createdAt": "2018-07-22T15:05:58.033Z",
      "updatedBy": "A3RGM375QTZ7",
      "updatedAt": "2018-07-22T15:05:58.033Z",
      "deletedBy": "A3RGM375QTZ7",
      "deletedAt": "2018-07-22T15:05:58.033Z"
    }
  ]
}

```

Show More

Find the issue type (`subtype`) - `results[subtypes.[title]]` (`Clash`), and note the type ID (subtype ID) - `results[subtypes.[id]]` (`2220f222-6c54-4b01-90e6-d701748f0222`).

## [Step 3: (Optional) Find Custom Field Mappings](#step-3-optional-find-custom-field-mappings)

When creating an issue you can optionally add custom field values if the custom fields were previously mapped to the category (`type`) or issue type (`subtype`). Each issue type (subtype) is potentially assigned configurable custom attributes. To find the custom attributes that are assigned to the issue type (`subtype`), call [GET issue-attribute-mappings](../http-docs/http-issues-issue-attribute-mappings-GET.md).

You can optimize the call by only including custom attributes that are assigned to the specified issue type (`subtype`). Use the `mappedItemId` filter, which corresponds to the issue type (`subtype`) ID that we retrieved in the previous step - `results[subtypes.[id]]` (`2220f222-6c54-4b01-90e6-d701748f0222`).

Note that the endpoint only retrieves custom fields that were directly assigned to the issue type (`subtype`). It does not retrieve inherited custom fields. To retrieve inherited custom field mappings you need to call this endpoint using the category (`type`) ID of the type (`subtype`).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/issue-attribute-mappings?filter[mappedItemId]=2220f222-6c54-4b01-90e6-d701748f0222' \
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
      "id": "6758h579-6c54-4b01-90e6-d701748a3922",
      "attributeDefinitionId": "1110f111-6c54-4b01-90e6-d701748f1333",
      "containerId": "2220f222-6c54-4b01-90e6-d701748f0222",
      "mappedItemType": "issueSubtype",
      "mappedItemId": "2220f222-6c54-4b01-90e6-d701748f0222",
      "order": 2,
      "isRequired": false,
      "permittedActions": [
        "delete"
      ],
      "permittedAttributes": [
        "isRequired"
      ],
      "createdAt": "2018-07-22T15:05:58.033Z",
      "createdBy": "A3RGM375QTZ7",
      "updatedAt": "2018-07-22T15:05:58.033Z",
      "updatedBy": "A3RGM375QTZ7",
      "deletedAt": "2018-07-22T15:05:58.033Z",
      "deletedBy": "A3RGM375QTZ7"
    }
  ]
}

```

Show More

Note the corresponding attribute definition IDs for the issue type (`subtype`) - `results[attributeDefinitionId] (``1110f111-6c54-4b01-90e6-d701748f1333`).

## [Step 4: (Optional) Find Custom Attribute Definitions](#step-4-optional-find-custom-attribute-definitions)

Before assigning values to the custom attributes you need to know the custom attribute data for the mappings. Use the attribute defintion IDs you retrieved in the previous step to call [GET custom-attribute-definitions](../http-docs/http-issues-issue-attribute-definitions-GET.md) to retrieve the custom attribute definitions.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/issue-attribute-definitions' \
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
      "id": "3521k878-6c54-4b01-90e6-d701747c5575",
      "containerId": "2220f222-6c54-4b01-90e6-d701748f0222",
      "title": "Velocity",
      "description": "How long will it take for this issue to be resolved.",
      "dataType": "numeric",
      "metadata": {},
      "isRequiredDefault": false,
      "permittedActions": [
        "edit"
      ],
      "permittedAttributes": [
        "title"
      ],
      "createdAt": "2018-07-22T15:05:58.033Z",
      "createdBy": "A3RGM375QTZ7",
      "updatedAt": "2018-07-22T15:05:58.033Z",
      "updatedBy": "A3RGM375QTZ7",
      "deletedAt": "2018-07-22T15:05:58.033Z",
      "deletedBy": "A3RGM375QTZ7"
    }
  ]
}

```

Show More

Search for the custom attribute mapping IDs and check the data in the corresponding object.

## [Step 5: (Optional) Find the ID of the Assignee](#step-5-optional-find-the-id-of-the-assignee)

To find the ID of the assignee, use the [Data Connector](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/data-connector/) API. See the [Retrieve Available Members Roles and Companies](https://aps.autodesk.com/en/docs/acc/v1/tutorials/issues/retrieve-members-roles-companies/) tutorial for more details.

Note that the Data Connector API workflow is a temporary method for determining permissions. We will be releasing endpoints that directly retrieve project users in the near future.

## [Step 6: Create the Issue](#step-6-create-the-issue)

Call [POST issues](../http-docs/http-issues-issues-POST.md) using the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`), the issue type (`subtype`) ID (`2220f222-6c54-4b01-90e6-d701748f0222`), and the custom field (`attributeDefinitionId`) ID (`3521k878-6c54-4b01-90e6-d701747c5575`).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/issues' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "title": "Door missing a screw",
        "description": "The door is missing a screw, please fix this",
        "issueSubtypeId": "2220f222-6c54-4b01-90e6-d701748f0222",
        "status": "open",
        "assignedTo": "IKLJ563G",
        "assignedToType": "user",
        "dueDate": "2022-05-21T00:00:00.000Z",
        "startDate": "2022-02-21T00:00:00.000Z",
        "locationId": "35de6f24-39f5-4808-ba5f-6cbbe2a858e1",
        "locationDetails": "issue location details",
        "published": true,
        "watchers": [
          "A3RGM375QTZ7"
        ],
        "customAttributes": [
          {
            "attributeDefinitionId": "3521k878-6c54-4b01-90e6-d701747c5575",
            "value": "368"
          }
        ]
      }'

```

Show More

### Response

```
{
  "id": "3570f222-6c54-4b01-90e6-e701749f0222",
  "containerId": "2220f222-6c54-4b01-90e6-d701748f0222",
  "deleted": false,
  "displayId": 7,
  "title": "Door missing a screw",
  "description": "The door is missing a screw, please fix this",
  "issueTypeId": "8770f222-6c54-4e01-93e6-e701749f0222",
  "issueSubtypeId": "2220f222-6c54-4b01-90e6-d701748f0222",
  "status": "open",
  "assignedTo": "IKLJ563G",
  "assignedToType": "user",
  "dueDate": "2022-05-21T00:00:00.000Z",
  "startDate": "2022-02-21T00:00:00.000Z",
  "locationId": "35de6f24-39f5-4808-ba5f-6cbbe2a858e1",
  "locationDetails": "issue location details",
  "linkedDocuments": [
    {}
  ],
  "links": [
    {}
  ],
  "ownerId": "",
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
  "openedAt": "2022-07-22T15:05:58.033Z",
  "closedBy": "A3RGM375QTZ7",
  "closedAt": "2022-07-22T15:05:58.033Z",
  "createdBy": "A3RGM375QTZ7",
  "createdAt": "2022-07-22T15:05:58.033Z",
  "updatedBy": "A3RGM375QTZ7",
  "updatedAt": "2022-07-22T15:05:58.033Z",
  "watchers": [
    "A3RGM375QTZ7"
  ],
  "customAttributes": [
    {
      "attributeDefinitionId": "1110f111-6c54-4b01-90e6-d701748f1333",
      "value": "368",
      "type": "numeric",
      "title": "Cost Impact ($)"
    }
  ]
}

```

Show More

## [Step 7: (Optional) Subscribe to Webhook Notifications](#step-7-optional-subscribe-to-webhook-notifications)

To receive automated notifications when new issues are created, you can subscribe to the `issue.created-1.0` webhook event. This allows your application to receive a notification whenever a new issue is added to a specified hub or project, and respond programmatically if needed.

For more information about webhooks, see the [Webhooks API](https://aps.autodesk.com/en/docs/webhooks/v1/developers_guide/overview/) and the [Creating a Webhook and Listening to Events](../../webhooks/how-to-docs/create-a-hook-issues.md) tutorial.

For details about the event payload, see the [Forma Issues Events](https://aps.autodesk.com/en/docs/webhooks/v1/reference/events/issues_events/) page.

Congratulations! You have created a Forma issue.
