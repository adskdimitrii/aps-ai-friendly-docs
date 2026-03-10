# projects/{projectId}/issues

Source: https://aps.autodesk.com/en/docs/acc/reference/http/issues-issues-GET/

---

Issues

GET

# projects/{projectId}/issues

Retrieves information about all the issues in a project, including details about their associated comments and attachments.

We support retrieving file-related (pushpin) issues. However, we do not currently support retrieving sheet-related issues from the ACC Build Sheets tool.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/issues/v1/projects/{projectId}/issues |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-ads-region   string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`.<br>For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| filter[id]   array: string: uuid | Filter issues by the unique issue ID. Separate multiple values with commas. |
| --- | --- |
| filter[issueTypeId]   array: string: uuid | Filter issues by the unique identifier of the category of the issue. Note that the API name for category is `type`. Separate multiple values with commas. |
| filter[issueSubtypeId]   array: string: uuid | Filter issues by the unique identifier of the type of the issue. Note that the API name for type is `subtype`. Separate multiple values with commas. |
| filter[status]   string | Filter issues by their status. Separate multiple values with commas. |
| filter[linkedDocumentUrn]   array: string | Retrieves pushpin issues associated with the specified files. We support all file types that are compatible with the Files tool. You need to specify the URL-encoded file item IDs. To find the file item IDs, use the [Data Management](en/docs/data/v2/developers_guide/overview/) API. <br>Note that you need to specify the 3D model item ID, which retrieves all pushpins associated with all 2D sheets and views associated with the 3D model. Similarly, if you specify a specific PDF file it retrieves all the pushpin issues associated with all the PDF file pages. We do not currently support retrieving pushpin issues associated with a specific 2D sheet or view.<br>By default, it returns pushpins for the latest version of the file. To retrieve pushpins for a specific version of a file together with pushpins for all previous versions of the specified file version, specify the version number, in the following format: `@[version-number]`.<br>For example, `filter[linkedDocument]=urn%3Aadsk.wipprod%3Adm.lineage%3AtFbo9zuDTW-nPh45gnM4gA@2`.<br>Separate multiple values with commas.<br>Note that we do not currently support filtering sheets from the ACC Build Sheets tool. |
| filter[dueDate]   string | Filter issues by due date, in one of the following URL-encoded format: YYYY-MM-DD. Separate multiple values with commas. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`Specific start date: e.g., `2022-03-02..`Specific end date: e.g., `..2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[startDate]   string | Filter issues by start date, in one of the following URL-encoded format: YYYY-MM-DD. Separate multiple values with commas. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`Specific start date: e.g., `2022-03-02..`Specific end date: e.g., `..2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[deleted]   boolean | Filter deleted issues. For example, `filter[deleted]=true`. If set to `true` it only returns deleted issues. If set to `false` it only returns undeleted issues. Note that we do not currently support returning both deleted and undeleted issues. Default value: `false`. <br>Project members with *View and assign to their company* and *Full visibility* can view deleted published and unpublished issues they originally created. Project members with Manage issues or Manage member permissions access can view all published issues that were deleted in a project. In addition, they can see unpublished deleted issues if they are an issue watcher, assignee, or creator.<br>For more information about deleted issues see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Issues_Search_Filter). |
| filter[createdAt]   datetime: ISO 8601 | Filter issues created at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03` or `2022-02-28T22:00:00.000Z..2022-03-28T22:00:00.000Z`Specific day: e.g., `2022-03-02` or `2022-02-28T22:00:00.000Z`Specific start date: e.g., `2022-03-02..` or `2022-02-28T22:00:00.000Z..`Specific end date: e.g., `..2022-03-02` or `..2022-02-28T22:00:00.000Z`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[createdBy]   array: string | Filter issues by the unique identifier of the user who created the issue. Separate multiple values with commas. For Example: `A3RGM375QTZ7`. |
| filter[updatedAt]   datetime: ISO 8601 | Filter issues updated at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03` or `2022-02-28T22:00:00.000Z..2022-03-28T22:00:00.000Z`Specific day: e.g., `2022-03-02` or `2022-02-28T22:00:00.000Z`Specific start date: e.g., `2022-03-02..` or `2022-02-28T22:00:00.000Z..`Specific end date: e.g., `..2022-03-02` or `..2022-02-28T22:00:00.000Z`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[updatedBy]   array: string | Filter issues by the unique identifier of the user who updated the issue. Separate multiple values with commas. For Example: `A3RGM375QTZ7`. |
| filter[assignedTo]   array: string | Filter issues by the unique Autodesk ID of the User/Company/Role identifier of the current assignee of this issue. Separate multiple values with commas. For Example: `A3RGM375QTZ7`. |
| filter[rootCauseId]   array: string: uuid | Filter issues by the unique identifier of the type of root cause for the issue. Separate multiple values with commas. |
| filter[locationId]   array: string: uuid | Retrieves issues associated with the specified location but not the location’s sublocations. To also retrieve issues that relate to the locations’s sublocations use the `sublocationId` filter. Separate multiple values with commas. |
| filter[subLocationId]   array: string: uuid | Retrieves issues associated with the specified unique LBS (Location Breakdown Structure) identifier, as well as issues associated with the sub locations of the LBS identifier. Separate multiple values with commas. |
| filter[closedBy]   array: string | Filter issues by the unique identifier of the user who closed the issue. Separate multiple values with commas. For Example: `A3RGM375QTZ7`. |
| filter[closedAt]   datetime: ISO 8601 | Filter issues closed at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03` or `2022-02-28T22:00:00.000Z..2022-03-28T22:00:00.000Z`Specific day: e.g., `2022-03-02` or `2022-02-28T22:00:00.000Z`Specific start date: e.g., `2022-03-02..` or `2022-02-28T22:00:00.000Z..`Specific end date: e.g., `..2022-03-02` or `..2022-02-28T22:00:00.000Z`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[search]   string | Filter issues using ‘search’ criteria. this will filter both title and issues display ID. For example, use filter[search]=300 |
| filter[displayId]   int | Filter issues by the chronological user-friendly identifier. Separate multiple values with commas. |
| filter[assignedToType]   string | Filter issues by the type of the current assignee of this issue. Separate multiple values with commas. Possible values: Possible values: `user`, `company`, `role`, `null`. For Example: `user`. |
| filter[customAttributes]   array: string | Filter issues by the custom attributes. Each custom attribute filter should be defined by it’s uuid. For example: `filter[customAttributes][f227d940-ae9b-4722-9297-389f4411f010]=1,2,3`. Separate multiple values with commas. |
| filter[valid]   boolean | Only return valid issues (=no empty type/subtype). Default value: `undefined` (meaning will return both valid & invalid issues). |
| limit   int | Return specified number of issues. Acceptable values are 1-100. Default value: `100`. |
| offset   int | Return issues starting from the specified offset number. Default value: `0`. |
| sortBy   array: string | Sort issues by specified fields. Separate multiple values with commas. To sort in descending order add a `-` (minus sign) before the sort criteria. Possible values: `displayId`, `title`, `description`, `status`, `assignedTo`, `assignedToType`, `dueDate`, `locationDetails`, `published`, `closedBy`, `closedAt`, `createdBy`, `createdAt`, `updatedAt`, `issueSubType`, `issueType`, `customAttributes`, `startDate`, `rootCause`. For example: `sortBy=status,-displayId,-dueDate,customAttributes[5c07cbe2-256a-48f1-b35b-2e5e00914104]`. |
| fields   array: string | Return only specific fields in issue object. Separate multiple values with commas. Fields which will be returned in any case: `id`, `title`, `status`, `issueTypeId`. Possible values: `id`, `displayId`, `title`, `description`, `issueTypeId`, `issueSubtypeId`, `status`, `assignedTo`, `assignedToType`, `dueDate`, `startDate`, `locationId`, `locationDetails`, `rootCauseTitle`, `rootCauseId`, `permittedStatuses`, `permittedAttributes`, `permittedActions`, `published`, `commentCount`, `openedBy`, `openedAt`, `closedBy`, `closedAt`, `createdBy`, `createdAt`, `updatedBy`, `updatedAt`, `customAttributes`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | List of relevant issues in combination with pagination details |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request |
| 403   Forbidden | The request is valid but lacks the necessary permissions. |
| 404   Not Found | The specified resource was not found |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| pagination   object | The pagination object defining the limit, offset, total number of issues, next and previous URL |
| --- | --- |
| limit   int | The maximum number of issues to be returned in each page |
| offset   int | The offset defining the start position from where the issues are returned |
| totalResults   int | The total number of issues including the ones of the current page |
| results   array: object | The list of issues in the current page |
| id   string: UUID | The unique identifier of the issue. |
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
| createdAtVersion   int | The version of the file the pushin issue was added to. For information about file versions, see the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). |
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
| viewerState   object | The viewer state at the time the pushpin was created. Maximum length: 2,500,000 characters. You can get the viewer state object by calling ViewerState.getState(). To restore the viewer instance use ViewerState.restoreState(). See the [`Viewer API documentation https://developer.autodesk.com/en/docs/viewer/v2/reference/javascript/viewerstate/`_](#id13) for more details. |
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
| watchers   array: string | The list of watchers for the issue. To find the name of the watcher, call [GET users](http-users-GET.md). |
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

List of relevant issues in combination with pagination details

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/:projectId/issues?filter[linkedDocumentUrn]=urn%3Aadsk.wipprod%3Afs.folder%3Aco.rLYHljHURdiG-o4HXOwByg%403' \
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
  ]
}

```

Show More
