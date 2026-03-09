# rfi-search

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-rfi-search-POST/

---

RFIs

POST

# rfi-search

Retrieves information about all the RFIs (Requests for Information) in a project, including details about their associated comments and attachments.

To retrieve full information for a specific RFI, use [GET rfis/:id](http-rfis-rfis-id-GET.md).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/search:rfis |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

Search request

Expand all

| limit   int | The number of RFIs to return. Default: `10`. Maximum: `200`. |
| --- | --- |
| offset   int | The number of items to skip before starting the result set. Default: `0`. |
| search   string | Searches for a string in the `title`, `question`, and `officialResponse` fields. |
| sort   array: object | A list of sort rules to apply. Each item includes a `field` to sort by and the sort `order`. |
| field   enum:string | The field to sort by. Possible values: `createdAt`, `status`, `dueDate`, `title`, `location`, `updatedAt`, `closedAt`, `costImpact`, `scheduleImpact`, `priority`, `discipline`, `category`, `reference`, `customIdentifier`, `customAttribute` |
| order   enum:string | The sort order. Possible values: `DESC`, `ASC` |
| filter   object | A set of optional filters to narrow the results. You can combine multiple filters. |
| status   array: string | Filter by RFI status. Possible values: `draft`, `submitted`, `open`, `openRev1`, `openRev2`, answered, `answeredRev1`, `answeredManager`, `closed`, `void`. Note that workflow types determine which statuses are used. |
| officialResponseStatus   array: string | Filters RFIs by the official response status. Possible values: `answered`, `unanswered`. |
| includeHidden   boolean | `true`: include RFIs that are hidden from the user. <br>`false`: (default) exclude hidden RFIs from the results. |
| assignedTo   array: string | Filter RFIs assigned to specific users. <br>To find the ID call [GET users/me](http-rfis-users-me-GET.md) and check `user.id`. |
| locations   array: string | Filter RFIs by location using Location Breakdown Structure (LBS) node IDs. <br>To retrieve location IDs, call [GET nodes](http-locations-nodes-GET.md).â |
| createdAt   string | Filter RFIs created after a specific date or within a date range. <br>Format: `YYYY-MM-DDThh:mm:ss.sz..YYYY-MM-DDThh:mm:ss.sz`. |
| updatedAt   string | Filter RFIs updated after a specific date, or within a date range. <br>Format: `YYYY-MM-DDThh:mm:ss.sz..YYYY-MM-DDThh:mm:ss.sz`. |
| closedAt   string | Filter RFIs by close date or date range. <br>Format: `YYYY-MM-DDThh:mm:ss.sz..YYYY-MM-DDThh:mm:ss.sz`. |
| createdBy   array: string | Filter RFIs by the user who created them. <br>To find the ID call [GET users/me](http-rfis-users-me-GET.md) and check `user.id`.â |
| dueDate   string | Filter RFIs by due date or due date range. <br>Format: `YYYY-MM-DDThh:mm:ss.sz..YYYY-MM-DDThh:mm:ss.sz`. |
| costImpact   array: string | Filter RFIs by cost impact value. <br>Possible values: `Yes`, `No`, `Unknown`. For example, `filter[costImpact]=Yes`â |
| scheduleImpact   array: string | Filter RFIs by schedule impact value. <br>Possible values**: `Yes`, `No`, `Unknown`. For example, `filter[scheduleImpact]=Yes`â |
| priority   array: string | Filter RFIs by priority level. <br>Possible values: `High`, `Normal`, `Low`. For example, `filter[priority]=High`.â |
| id   array: string | Filter by a list of specific RFI IDs. <br>To find the RFI IDs call [GET rfis](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/rfis-v2-rfis-GET/) and check `results.id`. |
| reference   string | Filter RFIs by the external reference ID (e.g., model number or spec reference). <br>Max length: 20 characters.<br>Max length: 20 |
| discipline   array: string | Filter RFIs by discipline. <br>Values depend on the project configuration. Examples include `Architectural`. For example, `filter[discipline]=Architectural`.<br>Possible values: `Building Management System`, `Electrical Substation`, `Security`, `Audio Visual`, `Food Service`, `Fire Alarm`, `Power Systems`, `Design Systems Integrator`, `Signage`, `Pathways`, `Cabling`, `Networks`, `Distributed Antenna System`, `Lighting`, `Vertical Transportation`, `Roofing`, `Architectural`, `Civil/Site`, `Concrete`, `Electrical`, `Exterior Envelope`, `Fire Protection`, `Interior/Finishes`, `Landscaping`, `Masonry`, `Mechanical`, `Plumbing`, `Structural`, `Other`, `Unspecified`. |
| category   array: string | Filter RFIs by category. <br>Categories are customizable per project. Examples include `Constructability`, `Code Compliance`. For example, `filter[category]=Constructability`.<br>Possible values: `Code Compliance`, `Constructability`, `Design Coordination`, `Documentation Conflict`, `Documentation Incomplete`, `Field condition`, `Other`, `Unspecified`. |
| customAttributes   object | Filter RFIs by custom attributes. <br>Provide a map of key-value pairs using attribute ID and selected value ID.<br>For example, `fd9a1234-aaaa-4444-bbbb-8888aa77ee66: value-id-1`. |
| rfiTypeId   array: string | Filter RFIs by RFI type ID. <br>RFI types are defined at the project level. Use UUIDs returned from the project configuration. |
| fields   array: string | Specify which attributes to include in the response. <br>Use this to limit the response to only the fields you need.<br>For example, `fields=id, title`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | A list of RFIs |
| --- | --- |
| 400   Bad Request | The parameters are invalid |
| 401   Unauthorized | The provided bearer token is not valid |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation |
| 500   Internal Server Error | An unknown error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of RFIs. |
| --- | --- |
| id   string | The system-generated ID of the RFI. |
| customIdentifier   string | The user-defined identifier of the RFI. |
| title   string | The title of the RFI. |
| question   string,null | The question submitted in the RFI. |
| virtualFolderUrn   string,null | The URN of the virtual folder created for the RFI. This folder stores all attachments related to the RFI. <br>The `virtualFolderUrn` is required when uploading attachments to an RFI. See the [Upload Attachment](../how-to-docs/files-upload-document-s3.md) tutorial for more details. |
| status   enum:string | The current status of the RFI. Available values depend on the RFIâs workflow type: <br>For single-reviewer workflows (US):<br>Possible values: `draft`, `submitted`, `open`, `answered`, `rejected`, `closed`, `void`.<br>For multi-reviewer workflows (EMEA):<br>Possible values: `draft`, `submitted`, `openRev1` (manager), `openRev2` (reviewers), `answeredRev1`, `answeredManager`, `closed`, `void`.<br>To determine the workflow type, call [GET users/me](http-rfis-users-me-GET.md) and check the `workflowType` value.<br>For details on RFI workflows in the ACC UI, see [About RFI Workflows â Autodesk Help](https://help.autodesk.com/view/BUILD/ENU/?guid=RFI_Workflow_Setup). |
| previousStatus   enum:string | The previous status of the RFI, if one exists. This field is omitted if the RFI has no prior status (e.g., when newly created).  > For single-reviewer workflows (US): >  >  > > Possible values: > > `draft`, `submitted`, `open`, `answered`, `rejected`, `closed`, `void`. > <br>For multi-reviewer workflows (EMEA):<br>Possible values: > `draft`, `submitted`, `openRev1` (manager), `openRev2` (reviewers), `answeredRev1`, `answeredManager`, `closed`, `void`.<br>To determine the workflow type, call [GET users/me](http-rfis-users-me-GET.md) and check the `workflowType` value.<br>For details on RFI workflows in the ACC UI, see [About RFI Workflows â Autodesk Help](https://help.autodesk.com/view/BUILD/ENU/?guid=RFI_Workflow_Setup). |
| workflowType   enum:string | The workflow type assigned to the RFI, which determines the allowed status transitions and the review path. Possible values: <br>`US`: Single-reviewer workflow`EU`: Multi-reviewer workflow<br>This value affects how statuses like `submitted`, `openRev1`, or `answeredManager` behave. For status definitions, see the `status` and `previousStatus` fields. |
| assignedTo   array: object | The list of users assigned to the RFI. |
| id   string | The Autodesk ID of the assigned user. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md).<br>To retrieve the list of available assignees, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/) and check the `manager` and `projectReviewer` fields. |
| type   enum:string | The type of assignee. Will always be `user`. |
| managerId   string | The Autodesk ID of the user designated as the RFI Manager. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md). |
| constructionManagerId   string | The Autodesk ID of the user designated as the Construction Manager for this RFI. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md). |
| architects   array: object | The list of architect users associated with the RFI. |
| type   enum:string | The type of architect. Will always be `user`. |
| id   string | The Autodesk ID of the architect. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md). |
| reviewers   array: object | The list of users assigned to review the RFI before it is closed. |
| type   enum:string | The type of reviewer. Will always be `user`. |
| id   string | The Autodesk ID of the reviewer. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md). |
| dueDate   string,null | The date and time by which a response to the RFI is expected, in ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sZ`). |
| locationDescription   string,null | The default text for the Location field when creating a new RFI. <br>Note that the API does not auto-populate this value. Clients are responsible for applying the default if desired.<br>To retrieve the default value configured for this field, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/). |
| locations   array: string | A list of predefined location IDs associated with the RFI, based on the projectâs Location Breakdown Structure (LBS). To get more information about the locations, call [GET nodes](http-locations-nodes-GET.md). |
| commentsCount   int | The number of comments associated with the RFI. |
| officialResponse   string | The text of the official response submitted for the RFI. <br>Always empty when creating an RFI. |
| officialResponseStatus   enum:string | The status of the official response to the RFI. <br>Possible values: `unanswered`, `answered`.<br>Always `unanswered` when creating an RFI. |
| officialResponseActors   array: object | The list of users who contributed to the official response. <br>Always empty when creating an RFI. |
| type   enum:string | The type of actor. Will always be `user`. |
| id   string | The Autodesk ID of the user. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md). |
| officialResponseEditByManagerState   boolean | `true`: the RFI Manager is allowed to edit the official response after submission. <br>`false`: editing the official response is disabled. (default). |
| respondedAt   datetime: ISO 8601 | The date and time when the RFI was officially responded to, in ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sZ`). |
| respondedBy   string | The Autodesk ID of the user who submitted the official response to the RFI. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md). |
| createdBy   string | The Autodesk ID of the user who created the RFI. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md). |
| createdAt   datetime: ISO 8601 | The date and time when the RFI was created, in ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sZ`). |
| updatedBy   string | The Autodesk ID of the user who last updated the RFI. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md). |
| updatedAt   datetime: ISO 8601 | The date and time when the RFI was last updated, in ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sZ`). |
| closedAt   datetime: ISO 8601 | The date and time when the RFI was closed, in ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sZ`). |
| closedBy   string | The Autodesk ID of the user who closed the RFI. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md). |
| containerId   string | The ID of the container. |
| projectId   string | The Autodesk ID of the project the RFI belongs to. |
| suggestedAnswer   string | A suggested answer for the RFI, typically entered by the assignee before submission of the official response. |
| coReviewers   array: object | A list of reviewers assigned to the RFI. Each entry may represent a user, role, or company. |
| id   string | The Autodesk ID of the reviewer. The reviewer can be a user (`autodeskId`), role (`memberGroupId`), or company (`memberGroupId`). <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](en/docs/acc/v1/reference/http/projects-:project_id-companies-GET/).<br>Note that we do not currently support finding details about roles for a project. |
| type   enum:string | The type of reviewer. Possible values: `user`, `role`, `company` |
| watchers   array: object | A list of watchers who are notified about changes to the RFI. Each entry may represent a user, role, or company. |
| id   string | The Autodesk ID of the assigned user. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md).<br>To retrieve the list of available assignees, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/) and check the `manager` and `projectReviewer` fields. |
| type   enum:string | The type of watcher. Possible values: `user`, `role`, `company` |
| answeredAt   datetime: ISO 8601 | The date and time when the official response to the RFI was submitted, in ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sZ`). <br>Empty when creating an RFI. |
| answeredBy   string | The Autodesk ID of the user who submitted the official response to the RFI. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md).<br>Empty when creating an RFI. |
| costImpact   string,null | The default cost impact value for new RFIs of this type. <br>Possible values: `null`, `Yes`, `No`, `Unknown`.<br>To check whether cost impact options are enabled and to retrieve the default value, call [GET rfi-types](en/docs/acc/v1/reference/http/rfis-RFI-types-GET/). |
| scheduleImpact   string,null | The default schedule impact value for new RFIs of this type. <br>Possible values: `null`, `Yes`, `No`, `Unknown`.<br>To verify whether schedule impact tracking is enabled for the project and what the default value is, call [GET rfi-types](en/docs/acc/v1/reference/http/rfis-RFI-types-GET/). |
| priority   string,null | The default priority for new RFIs of this type. <br>The available priority values are configured in Project Admin.<br>If no default is set, this field is `null`.<br>Note that the API does not auto-populate this value when creating an RFI. Clients are responsible for applying the default if desired.<br>The valid priority options can be retrieved by calling GET rfi-types <en/docs/acc/v1/reference/http/rfis-RFI-types-GET/>_. Some possible values: ``null`, `High`, `Normal`, `Low`. |
| discipline   array: string | The discipline associated with the RFI. To retrieve the supported values for the current project, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/). <br>Some possible values: `Building Management System`, `Electrical Substation`, `Security`, `Audio Visual`, `Food Service`, `Fire Alarm`, `Power Systems`, `Design Systems Integrator`, `Signage`, `Pathways`, `Cabling`, `Networks`, `Distributed Antenna System`, `Lighting`, `Vertical Transportation`, `Roofing`, `Architectural`, `Civil/Site`, `Concrete`, `Electrical`, `Exterior Envelope`, `Fire Protection`, `Interior/Finishes`, `Landscaping`, `Masonry`, `Mechanical`, `Plumbing`, `Structural`, `Other`.â |
| category   array: string | A list of predefined categories to assign to the RFI. <br>Categories help group RFIs for filtering and reporting. Each value must match a category configured in the projectâs RFI settings. Categories are case-sensitive and project-specific.<br>RFI categories are configured in Project Admin and may differ between projects. Call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/) to retrieve the allowed values for this field.<br>Some possible values: `Code Compliance`, `Constructability`, `Design Coordination`, `Documentation Conflict`, `Documentation Incomplete`, `Field condition`, `Other`. |
| reference   string | A user-provided text reference related to the RFI, such as a model number or spec reference, typically used when the RFI was created in another system. <br>Max length: 20 |
| customAttributes   array: object | A list of custom attributes associated with the RFI. |
| id   string: UUID | The ID of the custom attribute definition. |
| values   array: string | A list of selected values for this custom attribute. |
| isSelectable   boolean | Not relevant |
| rfiTypeId   string: UUID | The ID of the default RFI type assigned to the project. This is the unique identifier of the RFI type that will be selected by default when creating a new RFI. |
| bridgedSource   boolean | Not relevant |
| bridgedTarget   boolean | Not relevant |
| bridgeSyncOutdated   boolean | Not relevant |
| syncVersion   number | Not relevant |
| permittedActions   object | The list of actions that are permitted for the user. |
| share   boolean | Not relevant |
| nudge   boolean | Not relevant |
| pagination   object | The pagination object. |
| limit   int | The number of items returned per page. |
| offset   int | The number of items skipped before this page of results. |
| totalResults   int | The total number of items matching the request. |

## [Example](#example)

A list of RFIs

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/search:rfis' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "limit": 10,
        "offset": 0,
        "search": "HVAC duct routing",
        "sort": [
          {
            "field": "createdAt",
            "order": "DESC"
          }
        ],
        "filter": {
          "status": "draft",
          "officialResponseStatus": "answered",
          "includeHidden": false,
          "assignedTo": [
            "PER8KQPK2JRT"
          ],
          "locations": [
            "AJJASD2-FFE3",
            "JTOEN-FFD33"
          ],
          "createdAt": "2018-08-01T08:56:48.699Z",
          "updatedAt": "2018-08-01T08:56:48.699Z",
          "closedAt": "2018-08-01T08:56:48.699Z",
          "createdBy": [
            "PER8KQPK2JRT"
          ],
          "dueDate": "2018-08-01T08:56:48.699Z",
          "costImpact": "Yes",
          "scheduleImpact": "Yes",
          "priority": "Low",
          "id": [
            "1e6d1d7b-1b1b-4b1b-8b1b-1b1b1b1b1b1b"
          ],
          "reference": "RFI-235-A1",
          "discipline": "Architechural",
          "category": "Constructability",
          "customAttributes": "fd9a1234-aaaa-4444-bbbb-8888aa77ee66: value-id-1",
          "rfiTypeId": [
            "1e6d1d7b-1b1b-4b1b-8b1b-1b1b1b1b1b1b"
          ]
        },
        "fields": [
          "id"
        ]
      }'

```

Show More

### Response

```
{
  "results": [
    {
      "id": "31a3f98d-34a8-4d4c-a362-3cc9de44f89c",
      "customIdentifier": "ID-1234",
      "title": "RFI - pipe is not in right place",
      "question": "Where should we put the pipe?",
      "virtualFolderUrn": "urn:adsk.wip:fs.folder:co.1838SAGCQ3SPn7lqOXMaJQ",
      "status": "open",
      "previousStatus": "submitted",
      "workflowType": "US",
      "assignedTo": [
        {
          "id": "PER8KQPK2JRT",
          "type": "user"
        }
      ],
      "managerId": "KOR8KQPK2GHF",
      "constructionManagerId": "ALW8KQPK2PTB",
      "architects": [
        {
          "type": "user",
          "id": "TKG8KQPK2MNB"
        }
      ],
      "reviewers": [
        {
          "type": "user",
          "id": "IKJ8KQPK2WDV"
        }
      ],
      "dueDate": "2018-01-12T13:06:39.216Z",
      "locationDescription": "In the middle of the room.",
      "locations": [
        "AJJASD2-FFE3",
        "JTOEN-FFD33"
      ],
      "commentsCount": 15,
      "officialResponse": "The measurements are correct.",
      "officialResponseStatus": "answered",
      "officialResponseActors": [
        {
          "id": "AJJASD2-FFE3",
          "type": "user"
        },
        {
          "id": "JTOEN-FFD33",
          "type": "user"
        }
      ],
      "officialResponseEditByManagerState": true,
      "respondedAt": "2018-01-12T13:06:39.216Z",
      "respondedBy": "RFV8KQPK2KHF",
      "createdBy": "PER8KQPK2JRT",
      "createdAt": "2018-07-22T15:05:58.033Z",
      "updatedBy": "ZXC8KQPK2CVB",
      "updatedAt": "2018-07-22T15:05:58.033Z",
      "closedAt": "2018-07-22T15:05:58.033Z",
      "closedBy": "SER8KQPK2JRT",
      "containerId": "31a3f98d-34a8-4d4c-a362-3cc9de44f89c",
      "projectId": "31a3f98d-34a8-4d4c-a362-3cc9de44f89c",
      "suggestedAnswer": "The measurements are correct.",
      "coReviewers": [
        {
          "id": "WSX8KQPK2JRMJ",
          "type": "user"
        }
      ],
      "watchers": [
        {
          "id": "PER8KQPK2JRT",
          "type": "user"
        }
      ],
      "answeredAt": "2018-07-22T15:05:58.033Z",
      "answeredBy": "FGD8KQPK2JKK",
      "costImpact": "Yes",
      "scheduleImpact": "Yes",
      "priority": "High",
      "discipline": [
        "Architectural"
      ],
      "category": [
        "Constructability"
      ],
      "reference": "ID-1234",
      "customAttributes": [
        {
          "id": "c911852d-5957-4145-9c8d-e7cfe9d564df",
          "values": [
            ""
          ],
          "isSelectable": false
        }
      ],
      "rfiTypeId": "c911852d-5957-4145-9c8d-e7cfe9d564df",
      "bridgedSource": "",
      "bridgedTarget": "",
      "bridgeSyncOutdated": "",
      "syncVersion": "",
      "permittedActions": {
        "share": "",
        "nudge": ""
      }
    }
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 97
  }
}

```

Show More
