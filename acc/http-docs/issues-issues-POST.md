# projects/{projectId}/issues

Source: https://aps.autodesk.com/en/docs/acc/reference/http/issues-issues-POST/

---

Issues

POST

# projects/{projectId}/issues

Adds an issue to a project.

To verify whether a user can create issues for a specific project, call [GET users/me](/en/docs/acc/v1/reference/http/issues-me-GET).

To verify whether a user can create issues for a specific project, call GET users/me and verify that the `issues` section includes the `new` object.

You can add references to objects, such as photos and documents. Note that we currently only support directly uploading objects to ACC Docs. You cannot directly upload other objects such as photos and documents unless you upload them to ACC Docs as a file. See the [Add References To Issues](/en/docs/acc/v1/tutorials/issues/add-references-to-issues) tutorial for more details.

We support retrieving file-related (pushpin) issues. However, we do not currently support retrieving sheet-related issues from the ACC Build Sheets tool.

This endpoint automatically triggers the `issue.created-1.0` webhook event when a new issue is created. If youâve configured a webhook subscription for this event, your application will receive a notification. For more information, see the [Issues Webhooks section](/en/docs/acc/v1/overview/field-guide/issues/#issues-webhooks) in the Field Guide.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/issues/v1/projects/{projectId}/issues |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| x-ads-region   string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`.<br>For the full list of supported regions, see the [Regions](/en/docs/acc/v1/overview/acc-regions) page. |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

The payload for creating a new issue.

Expand all

| title*   string | The title of the issue. Maximum 100 characters. |
| --- | --- |
| description   string | A brief description of the issue and its purpose. Maximum 1000 characters. |
| snapshotUrn   string | Not relevant |
| issueSubtypeId*   string: UUID | The unique identifier of the subtype of the issue. |
| status*   enum:string | The current status of the issue. To check the available statuses for the project, call [GET users/me](/en/docs/acc/v1/reference/http/issues-me-GET) and check the list of permitted statuses (`issue.new.permittedStatuses`). For more information about statuses, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Issues_Statuses). Possible values: `draft`, `open`, `pending`, `in_progress`, `completed`, `in_review`, `not_approved`, `in_dispute`, `closed` |
| assignedTo   string | The Autodesk ID of the member, role or company you want to assign to the issue. Note that if you select an assignee ID, you also need to select a type (`assignedToType`). <br>We do not currently provide endpoints to programmatically find the member, role, or company IDs that you are permitted to assign to the issue. We recommend using the Data Connector API to extract the permitted IDs. See the [Retrieve Available Members Roles and Companies](/en/docs/acc/v1/tutorials/issues/retrieve-available-members-roles-companies) tutorial for more details. |
| assignedToType   string | The type of the current assignee of this issue. Possible values: `user`, `company`, `role`, `null`. Note that if you select a type, you also need to select the assignee ID (`assignedTo`). |
| dueDate   string | The due date of the issue, in ISO8601 format. |
| startDate   string | The start date of the issue, in ISO8601 format. |
| locationId   string: UUID | The unique LBS (Location Breakdown Structure) identifier that relates to the issue. |
| locationDetails   string | The location related to the issue, provided as plain text. Maximum 250 characters. |
| rootCauseId   string: UUID | The unique identifier of the type of root cause for the issue. |
| issueTemplateId   string: UUID | Not relevant |
| published   boolean | States whether the issue is published. Default value: `false` (e.g. unpublished). |
| permittedActions   array: string | The list of actions permitted for the user for this issue in its current state. <br>Note that if a user with *View and assign to their company* permissions attempts to assign a user from a another company to the issue, it will return an error.<br>Possible Values: `assign_all` (can assign another user from another company to the issue), `assign_same_company` (can only assign another user from the same company to the issue), `clear_assignee`, `delete`, `add_comment`, `add_attachment`, `remove_attachment`.<br>The following values are not relevant: `add_attachment`, `remove_attachment`. |
| watchers   array: string | The Autodesk ID of the member you want to assign as a watcher for the issue. <br>We do not currently provide endpoints to programmatically find the member IDs that you are permitted to assign as watchers for the issue. We recommend using the Data Connector API to extract the permitted IDs. See the [Retrieve Available Members](/en/docs/acc/v1/tutorials/issues/retrieve-available-members-roles-companies) tutorial for more details. |
| customAttributes   array: object | A list of custom attributes of the specific issue. |
| attributeDefinitionId*   string: UUID | The unique identifier of the custom attribute. |
| value*   object | Custom attribute value. Possible value types: `string`, `number`, `null`. |
| gpsCoordinates   object | A GPS Coordinate which represents the geo location of the issue. |
| latitude   number |  |
| longitude   number |  |
| snapshotHasMarkups   boolean | Not relevant |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Returns the created issue |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request |
| 403   Forbidden | The request is valid but lacks the necessary permissions. |
| 409   Conflict | The request contained a data conflict |

### Response

## [Body Structure (201)](#body-structure-201)

Expand all

| id   string: UUID | The unique identifier of the issue. |
| --- | --- |
| containerId   string: UUID | Not relevant |
| deleted   boolean | Indicates whether the issue was deleted. Default value: `false`. <br>Deleted issues can only be accessed by specific users. Project members with *View and assign to their company* and *Full visibility* permissions can view deleted published and unpublished issues they originally created. Project members with *Manage issues* or Manage member permissions access can view all published issues that were deleted in a project. In addition, they can see unpublished deleted issues if they are an issue watcher, assignee, or creator.<br>For more information about deleted issues see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Issues_Search_Filter). |
| deletedAt   datetime: ISO 8601 | The date and time the issue was deleted, in ISO8601 format. This is only relevant for deleted issues. |
| deletedBy   string | The Autodesk ID of the user who deleted the issue. This is only relevant for deleted issues. |
| displayId   int | The chronological user-friendly identifier of the issue. |
| title   string | The title of the issue. Maximum 100 characters. |
| description   string | A brief description of the issue and its purpose. Maximum 1000 characters. |
| snapshotUrn   string | Not relevant |
| issueTypeId   string: UUID | The unique identifier of the type of the issue. |
| issueSubtypeId   string: UUID | The unique identifier of the subtype of the issue. |
| status   enum:string | The current status of the issue. <br>Possible values: `draft`, `open`, `pending`, `in_progress`, `completed`, `in_review`, `not_approved`, `in_dispute`, `closed`.<br>For more information about statuses, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Issues_Statuses). |
| assignedTo   string | The unique Autodesk ID of the member, company, or role of the current assignee for this issue. Note that if you select an assignee ID, you also need to select a type (`assignedToType`). |
| assignedToType   string | The type of the current assignee of this issue. Possible values: `user`, `company`, `role`, `null`. Note that if you select a type, you also need to select the assignee ID (`assignedTo`). |
| dueDate   string | The due date of the issue, in ISO8601 format. |
| startDate   string | The start date of the issue, in ISO8601 format. |
| locationId   string: UUID | The unique LBS (Location Breakdown Structure) identifier that relates to the issue. |
| locationDetails   string | The location related to the issue, provided as plain text. Maximum 250 characters. |
| linkedDocuments   array: object | Information about the files associated with issues (pushpins). |
| type   enum:string | The type of file. Possible values: <br>`TwoDVectorPushpin` (3D models) `TwoDRasterPushpin` (2D sheets and views) |
| urn   string | The ID of the file associated with the issue (pushpin). Note that we do not currently support data associated with the ACC Build Sheet tool. |
| createdBy   string | The Autodesk ID of the user who created the pushpin issue. |
| createdAt   datetime: ISO 8601 | The date and time the pushpin was created, in ISO8601 format. |
| createdAtVersion   int | The version of the file the pushin issue was added to. For information about file versions, see the [Data Management API](/en/docs/data/v2/). |
| closedBy   string | The Autodesk ID of the user who closed the pushpin issue. |
| closedAt   datetime: ISO 8601 | The date and time the pushpin issue was closed, in ISO8601 format. |
| closedAtVersion   int | The version of the file when the pushpin issue was closed. |
| details   object | Information about the individual viewable. |
| viewable   object | The individual viewable associated with the issue (pushpin). This is relevant for both individual 2D sheets and views within a 3D model, and individual PDF sheets within a multi-sheet PDF file. It is only relevant if the issue is associated with a file. |
| id   string | Not relevant |
| guid   string | The ID of the viewable (guid). |
| viewableId   string | Not relevant |
| name   string | The name of the viewable. <br>Max length: 1000 |
| is3D   boolean | `true` if it is a 3D viewable `false` if it is a 2D viewable |
| position   object | The position of the pushpin in the viewable. |
| x   number | The x-value of the position in the viewable. |
| y   number | The y-value of the position in the viewable. |
| z   number | The z-value of the position in the viewable. This value is only relevant for 3D views. |
| objectId   int | The ID of the element the pushpin is associated with in the viewable. |
| externalId   string | An external identifier of the element the pushpin is associated with in the viewable. |
| viewerState   object | The viewer state at the time the pushpin was created. Maximum length: 2,500,000 characters. You can get the viewer state object by calling ViewerState.getState(). To restore the viewer instance use ViewerState.restoreState(). See the [`Viewer API documentation https://developer.autodesk.com/en/docs/viewer/v2/reference/javascript/viewerstate/`_](#id10) for more details. |
| links   array: object | Not relevant |
| ownerId   string | Not relevant |
| rootCauseId   string: UUID | The unique identifier of the type of root cause for the issue. |
| officialResponse   object | Not relevant |
| issueTemplateId   string: UUID | Not relevant |
| permittedStatuses   array: string | A list of statuses accessible to the current user, this is based on the current status of the issue and the user permissions. <br>Possible Values: `open`, `pending`, `in_review`, `closed`. |
| permittedAttributes   array: string | A list of attributes the current user can manipulate in the current context. `issueTypeId`, `linkedDocument`, `links`, `ownerId`, `officialResponse`, `rootCauseId`, `snapshotUrn` are not applicable. <br>Possible Values: `title`, `description`, `issueTypeId`, `issueSubtypeId`, `status`, `assignedTo`, `assignedToType`, `dueDate`, `locationId`, `locationDetails`, `linkedDocuments`, `links`, `ownerId`, `rootCauseId`, `officialResponse`, `customAttributes`, `snapshotUrn`, `startDate`, `published`, `deleted`, `watchers`. |
| published   boolean | States whether the issue is published. Default value: `false` (e.g. unpublished). |
| permittedActions   array: string | The list of actions permitted for the user for this issue in its current state. <br>Note that if a user with *View and assign to their company* permissions attempts to assign a user from a another company to the issue, it will return an error.<br>Possible Values: `assign_all` (can assign another user from another company to the issue), `assign_same_company` (can only assign another user from the same company to the issue), `clear_assignee`, `delete`, `add_comment`, `add_attachment`, `remove_attachment`.<br>The following values are not relevant: `add_attachment`, `remove_attachment`. |
| commentCount   int | The number of comments in this issue. |
| attachmentCount   int | Not relevant |
| openedBy   string | Not relevant |
| openedAt   datetime: ISO 8601 | Not relevant |
| closedBy   string | The unique identifier of the user who closed the issue. |
| closedAt   datetime: ISO 8601 | The date and time the issue was closed, in ISO8601 format. |
| createdBy   string | The unique identifier of the user who created the issue. |
| createdAt   datetime: ISO 8601 | The date and time the issue was created, in ISO8601 format. |
| updatedBy   string | The unique identifier of the user who updated the issue. |
| updatedAt   datetime: ISO 8601 | The date and time the issue was updated, in ISO8601 format. |
| watchers   array: string | The list of watchers for the issue. To find the name of the watcher, call [GET users](/en/docs/acc/v1/reference/http/users-GET). |
| customAttributes   array: object | A list of custom attributes of the specific issue. |
| attributeDefinitionId   string: UUID | The unique identifier of the custom attribute. |
| value   object | Custom attribute value. Possible value types: `string`, `number`, `null`. |
| type   enum:string | The type of attribute. Possible values: `numeric`, `paragraph`, `list` (this corresponds to `dropdown` in the UI), `text`. |
| title   string | Free text description of the attribute. |
| gpsCoordinates   object | A GPS Coordinate which represents the geo location of the issue. |
| latitude   number |  |
| longitude   number |  |
| snapshotHasMarkups   boolean | Not relevant |

## [Example](#example)

Returns the created issue

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/:projectId/issues' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "title": "Door missing a screw.",
        "description": "The door is missing a screw. Please fix this",
        "snapshotUrn": "",
        "issueSubtypeId": "1370f222-6c54-3a01-93e6-e701749f0222",
        "status": "open",
        "assignedTo": "A3RGM375QTZ7",
        "assignedToType": "user",
        "dueDate": "2018-07-25",
        "startDate": "1982-06-01",
        "locationId": "35de6f24-39f5-4808-ba5f-6cbbe2a858e1",
        "locationDetails": "issue location details",
        "rootCauseId": "2370f222-6c54-3a01-93e6-f701772f0222",
        "issueTemplateId": "",
        "published": true,
        "permittedActions": [
          "add_comment"
        ],
        "watchers": [
          "A3RGM375QTZ7"
        ],
        "customAttributes": [
          {
            "attributeDefinitionId": "2220f222-6c54-4b01-90e6-d701748f0888",
            "value": "368"
          }
        ],
        "gpsCoordinates": {
          "latitude": 35.7795897,
          "longitude": -78.6381787
        },
        "snapshotHasMarkups": false
      }'

```

Show More

### Response

```
{
  "id": "3570f222-6c54-4b01-90e6-e701749f0222",
  "containerId": "2220f222-6c54-4b01-90e6-d701748f0222",
  "deleted": false,
  "deletedAt": "2018-07-22T15:05:58.033Z",
  "deletedBy": "A3RGM375QTZ7",
  "displayId": 7,
  "title": "Door missing a screw.",
  "description": "The door is missing a screw. Please fix this",
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
    {
      "type": "TwoDVectorPushpin",
      "urn": "urn:adsk.wipprod:dm.lineage:0C9edNQuT2SrfoyKQ1Gv_Q",
      "createdBy": "A3RGM375QTZ7",
      "createdAt": "2018-07-22T15:05:58.033Z",
      "createdAtVersion": 1,
      "closedBy": "A3RGM375QTZ7",
      "closedAt": "2018-08-22T15:05:58.033Z",
      "closedAtVersion": 1,
      "details": {
        "viewable": {
          "id": "24820322-7c54-4a01-93e6-e701749f0345",
          "guid": "24820322-7c54-4a01-93e6-e701749f0345",
          "viewableId": "42",
          "name": "3D view of the 3rd floor of the building",
          "is3D": true
        },
        "position": {
          "x": -0.35907751666652,
          "y": 0.23,
          "z": 0.9998
        },
        "objectId": 3,
        "externalId": "4",
        "viewerState": true
      }
    }
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
  "permittedActions": [
    "add_comment"
  ],
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
  ],
  "gpsCoordinates": {
    "latitude": 35.7795897,
    "longitude": -78.6381787
  },
  "snapshotHasMarkups": false
}

```

Show More
