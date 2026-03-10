# rfis

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-rfis-POST/

---

RFIs

POST

# rfis

Adds an RFI (request for information) to a project.

RFIs are managed in the Project Management module.

Users can create RFIs if they have been assigned either creator (`projectSC`) or manager (`projectGC`) workflow roles. Project admins are automatically assigned the creator workflow role.

Note that you cannot currently use the RFIs API to assign workflow roles to users. To assign workflow roles, open the Project Admin module, select the Services tab, and select the Project Management section.

To verify whether a user can create an RFI, call [GET users/me](http-rfis-users-me-GET.md). If the `createRfi` object appears in the `permittedActions` response, it indicates that the user can create RFIs.

We strongly recommend calling [GET users/me](http-rfis-users-me-GET.md) before creating RFIs in order to verify the most up-to-date permissions and actions.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfis |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` `data:create` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

The RFI object.

Expand all

| id   string: UUID | Unique identifier for the RFI. This is system-generated and should not be included when creating a new RFI unless the client needs to set the RFI ID in advance. |
| --- | --- |
| status*   enum:string | The current status of the RFI. Available values depend on the RFI’s workflow type: <br>For single-reviewer workflows (US):<br>Possible values: `draft`, `submitted`, `open`, `answered`, `rejected`, `closed`, `void`.<br>For multi-reviewer workflows (EMEA):<br>Possible values: `draft`, `submitted`, `openRev1` (manager), `openRev2` (reviewers), `answeredRev1`, `answeredManager`, `closed`, `void`.<br>To determine the workflow type, call [GET users/me](http-rfis-users-me-GET.md) and check the `workflowType` value.<br>For details on RFI workflows in the ACC UI, see [About RFI Workflows – Autodesk Help](https://help.autodesk.com/view/BUILD/ENU/?guid=RFI_Workflow_Setup). |
| title*   string | The title of the RFI. |
| question   string,null | The RFI question. |
| suggestedAnswer   string | The suggested answer for the RFI. |
| assignedTo   array: object | The list of users assigned to the RFI. |
| id*   string | The Autodesk ID of the assigned user. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md).<br>To retrieve the list of available assignees, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/) and check the `manager` and `projectReviewer` fields. |
| type*   enum:string | The type of assignee. Will always be `user`. |
| locationDescription   string,null | The default text for the Location field when creating a new RFI. <br>Note that the API does not auto-populate this value. Clients are responsible for applying the default if desired.<br>To retrieve the default value configured for this field, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/). |
| locations   array: string | A list of predefined location IDs associated with the RFI, based on the project’s Location Breakdown Structure (LBS). To get more information about the locations, call [GET nodes](http-locations-nodes-GET.md). |
| dueDate   string,null | The timestamp of the due date for the RFI, in the following format: YYYY-MM-DDThh:mm:ss.sz. |
| costImpact   string,null | The default cost impact value for new RFIs of this type. <br>Possible values: `null`, `Yes`, `No`, `Unknown`.<br>To check whether cost impact options are enabled and to retrieve the default value, call [GET rfi-types](en/docs/acc/v1/reference/http/rfis-RFI-types-GET/). |
| scheduleImpact   string,null | The default schedule impact value for new RFIs of this type. <br>Possible values: `null`, `Yes`, `No`, `Unknown`.<br>To verify whether schedule impact tracking is enabled for the project and what the default value is, call [GET rfi-types](en/docs/acc/v1/reference/http/rfis-RFI-types-GET/). |
| priority   string,null | The default priority for new RFIs of this type. <br>The available priority values are configured in Project Admin.<br>If no default is set, this field is `null`.<br>Note that the API does not auto-populate this value when creating an RFI. Clients are responsible for applying the default if desired.<br>The valid priority options can be retrieved by calling GET rfi-types <en/docs/acc/v1/reference/http/rfis-RFI-types-GET/>_. Some possible values: ``null`, `High`, `Normal`, `Low`. |
| discipline   array: string | The discipline associated with the RFI. To retrieve the supported values for the current project, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/). <br>Some possible values: `Building Management System`, `Electrical Substation`, `Security`, `Audio Visual`, `Food Service`, `Fire Alarm`, `Power Systems`, `Design Systems Integrator`, `Signage`, `Pathways`, `Cabling`, `Networks`, `Distributed Antenna System`, `Lighting`, `Vertical Transportation`, `Roofing`, `Architectural`, `Civil/Site`, `Concrete`, `Electrical`, `Exterior Envelope`, `Fire Protection`, `Interior/Finishes`, `Landscaping`, `Masonry`, `Mechanical`, `Plumbing`, `Structural`, `Other`.’ |
| category   array: string | A list of predefined categories to assign to the RFI. <br>Categories help group RFIs for filtering and reporting. Each value must match a category configured in the project’s RFI settings. Categories are case-sensitive and project-specific.<br>RFI categories are configured in Project Admin and may differ between projects. Call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/) to retrieve the allowed values for this field.<br>Some possible values: `Code Compliance`, `Constructability`, `Design Coordination`, `Documentation Conflict`, `Documentation Incomplete`, `Field condition`, `Other`. |
| reference   string | An external ID. Typically used when the RFI was created in another system. <br>Max length: 20 |
| coReviewers   array: object | A list of reviewers assigned to the RFI. Each entry may represent a user, role, or company. |
| id*   string | The Autodesk ID of the reviewer. The reviewer can be a user (`autodeskId`), role (`memberGroupId`), or company (`memberGroupId`). <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](en/docs/acc/v1/reference/http/projects-:project_id-companies-GET/).<br>Note that we do not currently support finding details about roles for a project. |
| type*   enum:string | The type of reviewer. Possible values: `user`, `role`, `company` |
| watchers   array: object | A list of watchers who are notified about changes to the RFI. Each entry may represent a user, role, or company. |
| id*   string | The Autodesk ID of the assigned user. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md).<br>To retrieve the list of available assignees, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/) and check the `manager` and `projectReviewer` fields. |
| type*   enum:string | The type of watcher. Possible values: `user`, `role`, `company` |
| customAttributes   array: object | A list of custom attributes associated with the RFI. |
| values*   array: string | A list of selected values for this custom attribute. |
| isSelectable   boolean | Not relevant |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | RFI Created |
| --- | --- |
| 400   Bad Request | The parameters are invalid |
| 401   Unauthorized | The provided bearer token is not valid |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation |
| 500   Internal Server Error | An unknown error occurred on the server |

### Response

## [Body Structure (201)](#body-structure-201)

Expand all

| id   string | The system-generated ID of the RFI. |
| --- | --- |
| customIdentifier   string | The user-defined identifier of the RFI. |
| title   string | The title of the RFI. |
| question   string,null | The question submitted in the RFI. |
| virtualFolderUrn   string,null | The URN of the virtual folder created for the RFI. This folder stores all attachments related to the RFI. <br>The `virtualFolderUrn` is required when uploading attachments to an RFI. See the [Upload Attachment](../how-to-docs/files-upload-document-s3.md) tutorial for more details. |
| status   enum:string | The current status of the RFI. Available values depend on the RFI’s workflow type: <br>For single-reviewer workflows (US):<br>Possible values: `draft`, `submitted`, `open`, `answered`, `rejected`, `closed`, `void`.<br>For multi-reviewer workflows (EMEA):<br>Possible values: `draft`, `submitted`, `openRev1` (manager), `openRev2` (reviewers), `answeredRev1`, `answeredManager`, `closed`, `void`.<br>To determine the workflow type, call [GET users/me](http-rfis-users-me-GET.md) and check the `workflowType` value.<br>For details on RFI workflows in the ACC UI, see [About RFI Workflows – Autodesk Help](https://help.autodesk.com/view/BUILD/ENU/?guid=RFI_Workflow_Setup). |
| previousStatus   enum:string | The previous status of the RFI, if one exists. This field is omitted if the RFI has no prior status (e.g., when newly created).  > For single-reviewer workflows (US): >  >  > > Possible values: > > `draft`, `submitted`, `open`, `answered`, `rejected`, `closed`, `void`. > <br>For multi-reviewer workflows (EMEA):<br>Possible values: > `draft`, `submitted`, `openRev1` (manager), `openRev2` (reviewers), `answeredRev1`, `answeredManager`, `closed`, `void`.<br>To determine the workflow type, call [GET users/me](http-rfis-users-me-GET.md) and check the `workflowType` value.<br>For details on RFI workflows in the ACC UI, see [About RFI Workflows – Autodesk Help](https://help.autodesk.com/view/BUILD/ENU/?guid=RFI_Workflow_Setup). |
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
| locations   array: string | A list of predefined location IDs associated with the RFI, based on the project’s Location Breakdown Structure (LBS). To get more information about the locations, call [GET nodes](http-locations-nodes-GET.md). |
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
| discipline   array: string | The discipline associated with the RFI. To retrieve the supported values for the current project, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/). <br>Some possible values: `Building Management System`, `Electrical Substation`, `Security`, `Audio Visual`, `Food Service`, `Fire Alarm`, `Power Systems`, `Design Systems Integrator`, `Signage`, `Pathways`, `Cabling`, `Networks`, `Distributed Antenna System`, `Lighting`, `Vertical Transportation`, `Roofing`, `Architectural`, `Civil/Site`, `Concrete`, `Electrical`, `Exterior Envelope`, `Fire Protection`, `Interior/Finishes`, `Landscaping`, `Masonry`, `Mechanical`, `Plumbing`, `Structural`, `Other`.’ |
| category   array: string | A list of predefined categories to assign to the RFI. <br>Categories help group RFIs for filtering and reporting. Each value must match a category configured in the project’s RFI settings. Categories are case-sensitive and project-specific.<br>RFI categories are configured in Project Admin and may differ between projects. Call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/) to retrieve the allowed values for this field.<br>Some possible values: `Code Compliance`, `Constructability`, `Design Coordination`, `Documentation Conflict`, `Documentation Incomplete`, `Field condition`, `Other`. |
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
| responses   array: object | A list of responses associated with this RFI. <br>Always empty when creating an RFI. |
| id   string: UUID | The unique identifier of the response. |
| state   enum:string | The state of the response. Possible values: <br>`draft`: The response was returned to the reviewer for changes.`submitted`: The reviewer submitted a finalized response. |
| rfiId   string | The ID of the RFI associated with this response. |
| text   string | The body of the response. |
| status   enum:string | Indicates whether the response was accepted (`answered`) or declined (`rejected`). Possible values: `answered`, `rejected` |
| createdBy   string | The Autodesk ID of the assigned user. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md).<br>To retrieve the list of available assignees, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/) and check the `manager` and `projectReviewer` fields. |
| onBehalf   string | The Autodesk ID of the assigned user. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md).<br>To retrieve the list of available assignees, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/) and check the `manager` and `projectReviewer` fields. |
| isEditable   boolean | Indicates whether the response can be edited. <br>`true`: The response is editable.<br>`false` (default): The response cannot be edited. |
| createdAt   datetime: ISO 8601 | The date and time the response was created, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| updatedBy   string | The Autodesk ID of the user who updated the response. To find the name of the user, call [GET users](http-admin-projectsprojectId-users-GET.md). |
| updatedAt   datetime: ISO 8601 | The date and time the response was updated, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| deletedAt   datetime: ISO 8601 | The date and time the response was deleted, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| draftResponses   array: object | A list of draft responses associated with this RFI. <br>Always empty when creating an RFI. |
| id   string: UUID | The unique identifier of the response. |
| state   enum:string | The state of the response. Possible values: <br>`draft`: The response was returned to the reviewer for changes.`submitted`: The reviewer submitted a finalized response. |
| rfiId   string | The ID of the RFI associated with this response. |
| text   string | The body of the response. |
| status   enum:string | Indicates whether the response was accepted (`answered`) or declined (`rejected`). Possible values: `answered`, `rejected` |
| createdBy   string | The Autodesk ID of the assigned user. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md).<br>To retrieve the list of available assignees, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/) and check the `manager` and `projectReviewer` fields. |
| onBehalf   string | The Autodesk ID of the assigned user. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md).<br>To retrieve the list of available assignees, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/) and check the `manager` and `projectReviewer` fields. |
| isEditable   boolean | Indicates whether the response can be edited. <br>`true`: The response is editable.<br>`false` (default): The response cannot be edited. |
| createdAt   datetime: ISO 8601 | The date and time the response was created, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| updatedBy   string | The Autodesk ID of the user who updated the response. To find the name of the user, call [GET users](http-admin-projectsprojectId-users-GET.md). |
| updatedAt   datetime: ISO 8601 | The date and time the response was updated, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| deletedAt   datetime: ISO 8601 | The date and time the response was deleted, in the following format: `YYYY-MM-DDThh:mm:ss.sz`. |
| permittedActions   object | The list of actions that are permitted for the user. |
| share   boolean | Not relevant |
| nudge   boolean | Not relevant |
| updateRfi   object | Information about the user who most recently updated the RFI. |
| permittedStatuses   object | A list of statuses the user is permitted to transition an RFI to. |
| wfUS   array: object | A list of statuses the user is permitted to transition an RFI to in workflows of type `US`. |
| status   enum:string | The current response status of the RFI for single-reviewer workflows (US):  > Possible values: > `draft`, `submitted`, `open`, `answered`, `rejected`, `closed`, `void`. <br>For more information about workflows, see [About RFI Workflows – Autodesk Help](https://help.autodesk.com/view/BUILD/ENU/?guid=RFI_Types). |
| maxAssignees   int | The maximum number of users that can be assigned to this RFI. |
| requiredAttributes   array: object | The list of attributes that are required when creating or updating an RFI. |
| name   string | The name of the RFI attribute that must be provided when updating or creating an RFI in the specified status. |
| values   array: object | The list of allowed values for the required attribute. |
| value   string | The actual value that must be used for the required attribute when updating or creating the RFI. <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](en/docs/acc/v1/reference/http/projects-:project_id-companies-GET/).<br>Note that we do not currently support finding details about roles for a project. |
| type   string | The type of the required attribute value. Indicates what kind of entity the value represents (e.g., `user`, `role`, or `company`). |
| permittedAttributes   array: object | The list of attributes that the user is optionally allowed to include when updating or creating the RFI in the specified status. |
| name   string | The name of the RFI attribute that must be provided when updating or creating an RFI in the specified status. |
| values   array: object | The list of allowed values for the required attribute. |
| value   string | The actual value that must be used for the required attribute when updating or creating the RFI. <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](en/docs/acc/v1/reference/http/projects-:project_id-companies-GET/).<br>Note that we do not currently support finding details about roles for a project. |
| type   string | The type of the required attribute value. Indicates what kind of entity the value represents (e.g., `user`, `role`, or `company`). |
| wfEU   array: object | A list of statuses the user is permitted to transition an RFI to in workflows of type `EMEA`. |
| status   enum:string | The current response status of the RFI for a multi-reviewer workflow (EMEA): Possible values: `draft`, `submitted`, `openRev1` (manager), `openRev2` (reviewer), `answeredRev1`, `answeredManager`, `closed`, `void`. <br>For more information about workflows, see [About RFI Workflows – Autodesk Help](https://help.autodesk.com/view/BUILD/ENU/?guid=RFI_Types). |
| maxAssignees   int | The maximum number of users that can be assigned to this RFI. |
| requiredAttributes   array: object | The list of attributes that are required when creating or updating an RFI. |
| name   string | The name of the RFI attribute that must be provided when updating or creating an RFI in the specified status. |
| values   array: object | The list of allowed values for the required attribute. |
| value   string | The actual value that must be used for the required attribute when updating or creating the RFI. <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](en/docs/acc/v1/reference/http/projects-:project_id-companies-GET/).<br>Note that we do not currently support finding details about roles for a project. |
| type   string | The type of the required attribute value. Indicates what kind of entity the value represents (e.g., `user`, `role`, or `company`). |
| permittedAttributes   array: object | The list of attributes that the user is optionally allowed to include when updating or creating the RFI in the specified status. |
| name   string | The name of the RFI attribute that must be provided when updating or creating an RFI in the specified status. |
| values   array: object | The list of allowed values for the required attribute. |
| value   string | The actual value that must be used for the required attribute when updating or creating the RFI. <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](en/docs/acc/v1/reference/http/projects-:project_id-companies-GET/).<br>Note that we do not currently support finding details about roles for a project. |
| type   string | The type of the required attribute value. Indicates what kind of entity the value represents (e.g., `user`, `role`, or `company`). |
| permittedAttributes   array: object | The list of attributes that are required when creating an RFI. |
| name   string | The name of the RFI attribute that must be provided when updating or creating an RFI in the specified status. |
| values   array: object | The list of allowed values for the required attribute. |
| value   string | The actual value that must be used for the required attribute when updating or creating the RFI. <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](en/docs/acc/v1/reference/http/projects-:project_id-companies-GET/).<br>Note that we do not currently support finding details about roles for a project. |
| type   string | The type of the required attribute value. Indicates what kind of entity the value represents (e.g., `user`, `role`, or `company`). |
| useCustomAttributes   boolean | `true`: The user is allowed to fill in custom attributes when creating the RFI. <br>`false` (default): The user is not allowed to fill in custom attributes when creating the RFI. |
| createComment   boolean | `true`: The user can create a comment for the RFI. <br>`false` (default): The user cannot create a comment for the RFI. |
| createResponse   boolean | `true`: The user can create a response for the RFI. <br>`false`: The user cannot create a response for the RFI. |
| createResponseOnBehalf   boolean | `true`: The user can create a response on behalf of another user for the RFI. <br>`false`: The user cannot create a response on behalf of another user for the RFI. |
| remainingReviewers   array: object | A list of users who are still expected to review the RFI. |
| id   string | The Autodesk ID of the assigned user. <br>To find details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md).<br>To retrieve the list of available assignees, call [GET rfi-types](https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-rfi-types-GET/) and check the `manager` and `projectReviewer` fields. |
| type   enum:string | The type of reviewer. Will always be `user`. |
| createDocumentReference   boolean | `true`: The user can add a document reference to the RFI. <br>`false`: The user cannot add a document reference to the RFI. |
| removeDocumentReference   boolean | `true`: The user can remove a document reference to the RFI. <br>`false`: The user cannot remove a document reference to the RFI. |
| maxAssignees   int | The max amount of assignees permitted base on the RFIs current status. |

## [Example](#example)

RFI Created

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfis' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "id": "",
        "status": "open",
        "title": "wall color",
        "question": "what should be the color of the outer wall?",
        "suggestedAnswer": "blue",
        "assignedTo": [
          {
            "id": "PER8KQPK2JRT",
            "type": "user"
          }
        ],
        "locationDescription": "In the middle of the room.",
        "locations": [
          "AJJASD2-FFE3",
          "JTOEN-FFD33"
        ],
        "dueDate": "2018-01-12T13:06:39.216Z",
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
        "customAttributes": [
          {
            "values": [
              ""
            ],
            "isSelectable": false
          }
        ]
      }'

```

Show More

### Response

```
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
  "responses": [
    {
      "id": "c911852d-5957-4145-9c8d-e7cfe9d564df",
      "state": "draft",
      "rfiId": "w332252d-5957-4145-9c8d-e7cfe9d975aj",
      "text": "The pipe should be placed in the corner",
      "status": "answered",
      "createdBy": "PER8KQPK2JRT",
      "onBehalf": "PER8KQPK2JRT",
      "isEditable": true,
      "createdAt": "2018-07-22T15:05:58.033Z",
      "updatedBy": "PER8KQPK2JRT",
      "updatedAt": "2018-07-22T15:05:58.033Z",
      "deletedAt": "2018-07-22T15:05:58.033Z"
    }
  ],
  "draftResponses": [
    {
      "id": "c911852d-5957-4145-9c8d-e7cfe9d564df",
      "state": "draft",
      "rfiId": "w332252d-5957-4145-9c8d-e7cfe9d975aj",
      "text": "The pipe should be placed in the corner",
      "status": "answered",
      "createdBy": "PER8KQPK2JRT",
      "onBehalf": "PER8KQPK2JRT",
      "isEditable": true,
      "createdAt": "2018-07-22T15:05:58.033Z",
      "updatedBy": "PER8KQPK2JRT",
      "updatedAt": "2018-07-22T15:05:58.033Z",
      "deletedAt": "2018-07-22T15:05:58.033Z"
    }
  ],
  "permittedActions": {
    "share": "",
    "nudge": "",
    "updateRfi": {
      "permittedStatuses": {
        "wfUS": [
          {
            "status": "open",
            "maxAssignees": "",
            "requiredAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "PER8KQPK2JRT",
                    "type": "user"
                  }
                ]
              }
            ],
            "permittedAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "PER8KQPK2JRT",
                    "type": "user"
                  }
                ]
              }
            ]
          }
        ],
        "wfEU": [
          {
            "status": "open",
            "maxAssignees": "",
            "requiredAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "PER8KQPK2JRT",
                    "type": "user"
                  }
                ]
              }
            ],
            "permittedAttributes": [
              {
                "name": "assignedTo",
                "values": [
                  {
                    "value": "PER8KQPK2JRT",
                    "type": "user"
                  }
                ]
              }
            ]
          }
        ]
      },
      "permittedAttributes": [
        {
          "name": "assignedTo",
          "values": [
            {
              "value": "PER8KQPK2JRT",
              "type": "user"
            }
          ]
        }
      ],
      "useCustomAttributes": ""
    },
    "createComment": "",
    "createResponse": "",
    "createResponseOnBehalf": "",
    "remainingReviewers": [
      {
        "id": "PER8KQPK2JRT",
        "type": "user"
      }
    ],
    "createDocumentReference": "",
    "removeDocumentReference": ""
  },
  "maxAssignees": 10
}

```

Show More
