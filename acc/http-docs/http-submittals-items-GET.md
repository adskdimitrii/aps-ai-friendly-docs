# projects/{projectId}/items

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-items-GET/

---

Items

GET

# projects/{projectId}/items

Retrieves information about all the submittal items in a project that the user has permission to view.

Note that only managers can access submittals items in `draft` state.

Note also that submittal items in `void` state are excluded by default.

For information about submittal items, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Items).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/items |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The maximum number of results per page. Possible values: `1`- `50`. Default value: `20`. For example, to limit the response to two results per page, use `limit=2`. |
| --- | --- |
| offset   int | The number of results to skip before starting to return data. For example, to skip the first 20 results, include `offset=20` in the query string. For more details, see the [JSON API Paging Help documentation](https://jsonapi.org/format/#fetching-pagination). |
| sort   string | Sort items by specified fields. Separate multiple values with commas. To sort in descending or ascending order, add `desc` or `asc` after the sort criteria. For example, `statusId asc`. <br>Possible values: `ballInCourtUsers`, `ballInCourtCompanies`, `ballInCourtRoles`, `ballInCourtType`, `customIdentifier`, `customIdentifierHumanReadable`, `createdAt`, `createdBy`, `description`, `dueDate`, `id`, `identifier`, `leadTime`, `manager`, `managerType`, `managerDueDate`, `package.identifier`, `package.spec.identifier`, `packageId`, `packageIdentifier`, `packageSpecIdentifier`, `packageTitle`, `priority`, `publishedBy`, `publishedDate`, `receivedFromReview`, `receivedFromSubmitter`, `requiredApprovalDate`, `requiredDate`, `requiredOnJobDate`, `respondedAt`, `respondedBy`, `response.value`, `responseComment`, `responseId`, `revision`, `sentToReview`, `sentToReviewBy`, `sentToSubmitter`, `spec.identifier`, `specId`, `specIdentifier`, `specTitle`, `stateId`, `statusId`, `subcontractor`, `subcontractorType`, `submittedBy`, `submitterDueDate`, `subsection`, `title`, `type.value`, `typeId`, `updatedAt`, `updatedBy`, `watchers`. |
| search   string | Search for items by querying a specified string within specific fields (`identifier`, `title`, `specIdentifier`, `ballInCourt`), and retrieve the associated items that match the search criteria. This includes items where the string matches part of a field. For example, `search=1`. |
| filter[title]   string | Filter items with the specified title. You can specify multiple values. Separate multiple values with commas. For example, `filter[title]="Shop Drawings"`. |
| filter[statusId]   string | Filter items with the specified status ID. You can specify multiple values. Separate multiple values with commas. For example, `filter[statusId]=1` |
| filter[specId]   string | Filter items with the specified spec ID. You can specify multiple values. Separate multiple values with commas. For example, `filter[specId]=b4aa3864-5706-4a7b-b06c-a792e8b2df23` |
| filter[ballInCourtUsers]   string | Filter items associated with the specified ball-in-court user ID. You can specify multiple users. Separate multiple values with commas. For example, `filter[ballInCourtUsers]=HNRCQ6JTWAED`. |
| filter[ballInCourtCompanies]   string | Filter items associated with the specified ball-in-court company ID. You can specify multiple companies. Separate multiple values with commas. For example, `filter[ballInCourtCompanies]=WD43ZJGKDFLFH`. |
| filter[ballInCourtRoles]   string | Filter items associated with the specified ball-in-court role ID. You can specify multiple roles. Separate multiple values with commas. For example, `filter[ballInCourtRoles]=WD43ZJGKDFLFH`. |
| filter[responseId]   string | Filter items with the specified final response ID. You can specify multiple IDs. You can specify multiple values. Separate multiple values with commas. For example, `filter[responseId]=1w66d30b-7dc1-4a65-991d-d739a1381rf4`. |
| filter[reviewResponseId]   string | Filter items with the specified review response ID. You can specify multiple IDs. You can specify multiple values. Separate multiple values with commas. For example, `filter[reviewResponseId]=1w66d30b-7dc1-4a65-991d-d739a1381rf4`. |
| filter[typeId]   string | Filter items with the specified type ID. You can specify multiple values. Separate multiple values with commas. For example, `filter[typeId]=06fa0c1b-6462-459d-8a38-0aff11bfe868`. |
| filter[packageId]   string | Filter items with the specified package ID. You can specify multiple values. Separate multiple values with commas. For example, `filter[packageId]=06fa0c1b-6462-459d-8a38-0aff11bfe868`. In order to filter items with no package, use ânoPackageâ value. |
| filter[stateId]   string | Filter items with the specified state ID. You can specify multiple values. Separate multiple values with commas. For example, `filter[stateId]=rev`. |
| filter[identifier]   string | Filter items with the specified submittal item ID (the submittal item ID in the UI). You can specify multiple values. Separate multiple values with commas. For example, `filter[identifier]=2`. |
| filter[leadTime]   string | Filter items with the specified lead time. You can specify multiple values. Separate multiple values with commas. For example, `filter[leadTime]=100`. |
| filter[revision]   string | Filter items with the specified revision number. You can specify multiple values. Separate multiple values with commas. For example, `filter[revision]=1`. |
| filter[manager]   string | Filter items with the specified manager Autodesk ID. You can specify multiple values. Separate multiple values with commas. For example, `filter[manager]=WD43ZJGKDFLFH`. |
| filter[managerType]   string | Filter items with the specified manager type. You can specify multiple values. Separate multiple values with commas. For example, `filter[managerType]=1`. |
| filter[subcontractor]   string | Filter items with the specified subcontractor Autodesk ID. You can specify multiple values. Separate multiple values with commas. For example, `filter[subcontractor]=WD43ZJGKDFLFH`. |
| filter[subcontractorType]   string | Filter items with the specified subcontractor type. You can specify multiple values. Separate multiple values with commas. For example, `filter[subcontractorType]=1`. |
| filter[createdBy]   string | Filter items that were created by the specified user by specifying the userâs Autodesk ID. For example, `filter[createdBy]=PER8KQPK2JRT`. To find the ID call [GET users](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-projectsprojectId-users-GET/). |
| filter[watchers]   string | Filter items that are associated with the specified watcher, by specifying the watcherâs Autodesk ID. For example, `filter[watchers]=PER8KQPK2JRT`. You can specify more than one watcher. Separate multiple values with commas. To find the ID call [GET users](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-projectsprojectId-users-GET/). |
| filter[dueDate]   string | Filter items with the specified due date, using the following URL-encoded format YYYY-MM-DD. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[submitterDueDate]   string | Filter items with the specified submitterâs due date, using the following URL-encoded format YYYY-MM-DD. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[managerDueDate]   string | Filter items with the specified managerâs due date, using the following URL-encoded format YYYY-MM-DD. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[createdAt]   string | Filter items with the specified creation date, using the following URL-encoded format YYYY-MM-DD. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[sentToSubmitter]   string | Filter items based on the date they were sent to the submitter. Use the following URL-encoded format: YYYY-MM-DD. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[receivedFromSubmitter]   string | Filter items based on the date they were received from the submitter. Use the following URL-encoded format: YYYY-MM-DD. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[sentToReview]   string | Filter items based on the date they were sent for review, in the URL-encoded format: YYYY-MM-DD. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[receivedFromReview]   string | Filter items based on the date they were moved forward by the reviewer using the URL-encoded format: YYYY-MM-DD. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[publishedDate]   string | Filter items based on their published date using the following URL-encoded format: YYYY-MM-DD. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[requiredDate]   string | Filter items based on the date the responsible contractor needs to submit the submittal to the submittal manager, using the following URL-encoded format: YYYY-MM-DD. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[requiredApprovalDate]   string | Filter items based on their required approval date using the following URL-encoded format: YYYY-MM-DD. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[requiredOnJobDate]   string | Filter items based on their required on-job (jobsite) date using the following URL-encoded format: YYYY-MM-DD. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[updatedAt]   string | Filter items by their last updated date using the following URL-encoded format: YYYY-MM-DD. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03`Specific day: e.g., `2022-03-02`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[id]   string | Filter submittal items by their unique internal submittal item ID (UUID). You can specify multiple values. Separate multiple values with commas. For example `filter[id]=b8cc9324-6759-4f07-8ce3-725d5afd4f11`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | A list of items. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. |
| 401   Unauthorized | Invalid or missing authorization header. Verify the Bearer token and try again. |
| 403   Forbidden | The user is not authorized to perform this action. |
| 404   Not Found | The specified resource was not found. |
| 500   Internal Server Error | An unexpected error occurred on the server while processing the request. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of submittal items. |
| --- | --- |
| id   string: UUID | The internal, globally unique identifier (UUID) for the submittal item. |
| identifier   int | The unique ID assigned to the submittal item within the UI. This ID is system-generated and serves as a reference for users interacting with submittal items through the UI. For example, `111`. |
| customIdentifier   string | `customIdentifier` and `customIdentifierHumanReadable` relate to the `Number` column in the UI. Submittal managers assign custom numbers to items (manually or automatically). Custom numbers are configured either in global numbering format: <global number>, or in spec section numbering format: <spec ID>-<sequential number>. <br>For projects with a global numbering format, both `customIdentifier` and `customIdentifierHumanReadable` represent the global number.<br>For projects with a spec section numbering format (<spec ID>-<sequential number>), `customIdentifier` represents the sequential number. For example, for a full number of `033100-01`, `customIdentifier` is `01`.<br>Note that for unnumbered items `customIdentifier` is `null`.<br>For more information on custom numbering, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Custom_Numbering). |
| customIdentifierHumanReadable   string | `customIdentifierHumanReadable` and `customIdentifier` relate to the `Number` column in the UI. Submittal managers assign custom numbers to items (manually or automatically). Custom numbers are configured either in global numbering format: <global number>, or in spec section numbering format: <spec ID>-<sequential number>. <br>For projects with a global numbering format, both `customIdentifier` and `customIdentifierHumanReadable` represent the global number.<br>For projects with a spec section numbering format (<spec ID>-<sequential number>), `customIdentifierHumanReadable` represents the full number - both the spec ID and the sequential number. For example, for a full number of `033100-01`, `customIdentifierHumanReadable` is `033100-01`.<br>Note that for unnumbered items `customIdentifierHumanReadable` is `Unspecified`. For spec section numbering it also includes the spec ID. For example, `033100-Unspecified`.<br>For more information on custom numbering, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Custom_Numbering). |
| typeId   string | The ID representing the type of submittal item. |
| specId   string: UUID | The unique identifier (UUID) of the spec assigned to the submittal item. |
| specIdentifier   string | The identifier of the spec section that is associated with the submittal item. The identifier is assigned to the spec section in the UI. |
| specTitle   string | The title of the spec associated with the submittal item. |
| subsection   string | The sub-spec section associated with the submittal item, providing additional categorization within the main spec. |
| title   string | The title of the submittal item. |
| description   string | The description of the submittal item. |
| priority   enum:string | The priority of the submittal item. <br>Possible values:<br>`Low``Normal``High` |
| revision   int | The revision number of the submittal item, indicating the version of the item in the submittal workflow. For example, `1` for the initial submission or `2` for the first revision. |
| stateId   enum:string | The current state of the submittal item after the transition. <br>Possible values:<br>`sbc-1` (Waiting for Submission) - Assigned to the Responsible Contractor, who needs to submit the submittal to the Manager.<br>`mgr-1` (Open - Submitted) - Assigned to the Manager, who needs to prepare the submittal item for review.<br>`rev` (Open - In Review) - Under review by the reviewers defined in the submittal itemâs review workflow.<br>`mgr-2` (Open - Reviewed) - The review is complete, and the submittal is returned to the Manager, who needs to set the final response and close the submittal.<br>`sbc-2`: (Closed) - The submittal has been closed and assigned to the Responsible Contractor.<br>`void` (Voided) - The submittal item has been voided.<br>`draft` (Draft) - Assigned to the Manager, who must send the submittal item to the Responsible Contractor. |
| statusId   enum:string | The status of the submittal item. <br>Possible values: `1` - (Required), `2` - (Open), `3` - (Closed), `4` - (Void), `5` - (Empty), `6` - (Draft).<br>To retrieve the full list of possible statuses, call [GET metadata](http-submittals-metadata-GET.md). |
| ballInCourtUsers   array: string | The Autodesk IDs of users who are currently assigned to the submittal item at this stage of the workflow. |
| ballInCourtCompanies   array: string | The member group IDs of the companies currently assigned to the submittal item at this stage of the workflow. |
| ballInCourtRoles   array: string | The member group IDs of user roles that are currently assigned to the submittal item at this stage of the workflow. |
| ballInCourtType   enum:string | âThe type of submittal role assigned to the user currently assigned to the submittal item. <br>Possible values: `reviewer`, `manager`, `subcontractor`.â |
| manager   string | The ID that was assigned to the manager of the submittal item. <br>To determine the type of the manager (user, role, or company), refer to the manager type (`managerType`) attribute. In order to get more info about the manager, use:  > [GET projects/users](http-admin-projectsprojectId-users-GET.md) to verify the actual name of the user in case the typs is a `user` (1).[GET companies](http-projects--project_id-companies-GET.md) to determine the name of the company in case the typs is a `company` (2). <br>Note that we do not currently support verifying names of roles. |
| managerType   enum:string | The type of manager associated with the submittal item. <br>Possible values: `1` (user), `2` (company), `3` (role). |
| subcontractor   string | The ID that was assigned to the subcontractor for the submittal item. If a non-manager user created the submittal item and chose a manager, they are automatically assigned as the `subcontractor` of the submittal item. In order to get more info about the subcontractor, use:  > [GET projects/users](http-admin-projectsprojectId-users-GET.md) to verify the actual name of the user in case the typs is a `user` (1).[GET companies](http-projects--project_id-companies-GET.md) to determine the name of the company in case the typs is a `company` (2). <br>Note that we do not currently support verifying names of roles. |
| subcontractorType   enum:string | The type of subcontractor associated with the submittal item. <br>Possible values: `1` (user), `2` (company), `3` (role). |
| watchers   array: object | A list of project watchers, who can be individual users, roles, or companies. |
| id   string | The Autodesk ID of the watcher. The watcher can be a user (`autodeskId`), role (`memberGroupId`), or company (`memberGroupId`). <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](en/docs/acc/v1/reference/http/projects-:project_id-companies-GET/). Note that we do not currently support finding details about roles for a project. |
| userType   object | The type of watcher assigned to the submittal item. <br>Possible values:<br>`1` (user)`2` (company)`3` (role) |
| dueDate   string | The due date for the submittal item, formatted as YYYY-MM-DD in UTC (ISO 8601). For example, `2018-02-15`. |
| requiredOnJobDate   string | The date when the materials are expected to arrive on the construction site, formatted as YYYY-MM-DD in UTC (ISO 8601). For example, `2018-02-15`. |
| leadTime   int | The duration (in days) from the approval of the submittal to delivery of materials or products to the construction site. |
| requiredDate   string | The date by which the Responsible Contractor must submit the submittal to the submittal manager, formatted as YYYY-MM-DD in UTC (ISO 8601). For example, `2018-02-15`. |
| requiredApprovalDate   string | The date by which approval for the submittal is required, formatted as YYYY-MM-DD in UTC (ISO 8601). For example, `2018-02-15`. |
| submitterDueDate   string | The date by which the subcontractor is expected to submit the submittal to the manager, formatted as YYYY-MM-DD in UTC (ISO 8601). For example, `2018-02-15`. This corresponds to the `sbc-1` state `Waiting for submission`. |
| sentToSubmitter   datetime: ISO 8601 | The date and time when the submittal was sent to the subcontractor for review, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2018-02-15T12:09:24.198466Z`. This corresponds to transition to the `sbc-1` state. |
| receivedFromSubmitter   datetime: ISO 8601 | The date when the submittal was received back from the subcontractor after review, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2018-02-15T12:09:24.198466Z`. This corresponds to transition to `mgr-1` state `Open (Submitted)`. |
| submittedBy   string | The Autodesk ID of the user who submitted the submittal item. This is the user who transitioned the item to the manager. |
| managerDueDate   string | The date by which the manager is expected to prepare the submittal item for review, formatted as YYYY-MM-DD in UTC (ISO 8601). For example, `2018-02-15`. This corresponds to the `mgr-1` state `Open (Submitted)`. |
| sentToReview   datetime: ISO 8601 | The date and time when the submittal item transitioned to the `rev` state `(Open - In review)`, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2018-02-15T12:09:24.198466Z`. |
| sentToReviewBy   string | The Autodesk ID of the user who transitioned the item to the `rev` state `(Open - In review)`. |
| receivedFromReview   datetime: ISO 8601 | The date and time when the submittal item transitioned from the `rev` state `(Open - In Review)` to the `mgr-2` state `(Close and distribute)`, formatted as YYYY-MM-DD (ISO 8601) in UTC. For example, `2022-03-02T12:09:24Z`. |
| publishedDate   datetime: ISO 8601 | The date when the manager closed and distributed the submittal item, in the following format: YYYY-MM-DD (ISO 8601) in UTC. For example, `2018-02-15`. |
| publishedBy   string | The Autodesk ID of the user who published the submittal item. |
| responseId   string | The ID of the response associated with the submittal item, linking to the specific feedback or action taken. |
| responseComment   string | The body of the response comment, containing feedback or instructions related to the submittal item. |
| respondedAt   datetime: ISO 8601 | The date and time when the response was added, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2018-02-15T12:09:24.198466Z`. |
| respondedBy   string | The Autodesk ID of the user that gave the response to the submittal item. |
| packageId   string: UUID | The ID of the package associated with the submittal item. |
| packageIdentifier   string | The package identifier as displayed in the UI. |
| packageTitle   string | The title of the package associated with the submittal item. |
| packageSpecIdentifier   string | The identifier of the submittal spec associated with the package. This value corresponds to the âSpec sectionâ displayed in the UI, such as `1 - Cement`. |
| folderUrn   string | The URN of the folder that contains the attachments associated with the submittal items. |
| revisionsFoldersUrns   object | An object containing URNs that represent folders associated with the revisions of the submittal item. These URNs can be used to access and identify specific folders related to submittal item revisions within the system. |
| createdAt   datetime: ISO 8601 | The date and time when the submittal item was originally created, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2018-02-15T12:09:24.198466Z`. |
| createdBy   string | The Autodesk ID of the user who created the submittal item. |
| updatedAt   datetime: ISO 8601 | The time and date when the submittal item was last updated, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2018-02-15T12:09:24.198466Z`. |
| updatedBy   string | The Autodesk ID of the user who last updated the submittal item. |
| permittedActions   array: object | The list of actions the user is allowed to perform on the submittal item. |
| id   string | The ID of the action in the format `type_of_object::action`. For example, `Item::retrieve`. |
| fields   object | A list of field names for which values must be provided when performing the action. An empty array indicates no specific set of values. |
| mandatoryFields   array: string | Lists the fields that are required when updating a submittal item. <br>The required fields depend on the action being performed, the itemâs current state, and the userâs role.<br>For example:<br>To transition the state of a submittal item, `stateId` and `responseId` are required. To reassign the manager, `manager` and `managerType` are required. To modify the spec section, `specId` is required. |
| transitions   array: object | The list of possible state transitions for a submittal item within the review workflow. |
| id   string | The ID of the transition in the format `from-state::to-state`. For example, `create::mgr-1`, `mgr-1::mgr-2`, `rev::void`. |
| name   string | The descriptive name of the transition. For example, `Create`, `Send to Manager`, `Send to void`. |
| stateFrom   object | The starting state of the transition, representing the current position of the submittal item in the workflow. |
| id   string | The unique ID of the starting state. For example, `create`, `mgr-1`, `rev`. The `rev` state indicates that the submittal item is currently under review. |
| name   string | The name of the starting state. For example, `Create`, `Manager Review`, `Review`. |
| stateTo   object | The target state of the transition, indicating the next position of the submittal item in the workflow. |
| id   string | The unique ID of the target state. For example, `mgr-1`, `mgr-2`, `void`. |
| name   string | The name of the target state. For example, `Manager Review`, `Manager Final Review`, `Void`. |
| transitionFields   array: string | Fields that are used in the transition. For example, [`subcontractor`, `subcontractorType`, `watchers`, `responseId`]. |
| mandatoryFields   array: string | A list of required fields for the transition. For example, [`responseId`]. |
| actionId   string | Not relevant |
| pagination   object | Describes pagination details for the response, including information about the current page and navigation to other pages. |
| limit   int | The maximum number of results to be displayed on each page. |
| offset   int | The number of results skipped before starting the current page. |
| totalResults   int | The overall count of results available across all pages. |
| previousUrl   string | The URL to retrieve the preceding page of results, if applicable. Not returned on the first page of results. |
| nextUrl   string | The URL to retrieve the subsequent page of results, if available. If not included, this is the last page of data. |

## [Example](#example)

A list of items.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/items' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "id": "b8cc9324-6759-4f07-8ce3-725d5afd4f11",
      "identifier": 1111,
      "customIdentifier": "A-111",
      "customIdentifierHumanReadable": "0001-A-111",
      "typeId": "06fa0c1b-6462-459d-8a38-0aff11bfe868",
      "specId": "62d6f245-b470-4af4-802b-4cb94b5dead1",
      "specIdentifier": "09-5300",
      "specTitle": "Acoustical Ceilings",
      "subsection": "1.05-B",
      "title": "Shop Drawings",
      "description": "Detailed plans by subcontractor, showing project dimensions.",
      "priority": "Low",
      "revision": 0,
      "stateId": "mgr-1",
      "statusId": "1",
      "ballInCourtUsers": [
        "WD43ZJGKDFLFH"
      ],
      "ballInCourtCompanies": [
        "WD43ZJGKDFLFH"
      ],
      "ballInCourtRoles": [
        "WD43ZJGKDFLFH"
      ],
      "ballInCourtType": "reviewer",
      "manager": "WD43ZJGKDFLFH",
      "managerType": "1",
      "subcontractor": "WD43ZJGKDFLFH",
      "subcontractorType": "1",
      "watchers": [
        {
          "id": "224356",
          "userType": "2"
        },
        {
          "id": "3522614",
          "userType": "3"
        }
      ],
      "dueDate": "2018-02-15",
      "requiredOnJobDate": "2018-02-15",
      "leadTime": 100,
      "requiredDate": "2018-02-15",
      "requiredApprovalDate": "2018-02-15",
      "submitterDueDate": "2018-02-15",
      "sentToSubmitter": "2018-02-01T12:09:24.198466Z",
      "receivedFromSubmitter": "2018-02-01T12:09:24.198466Z",
      "submittedBy": "WD43ZJGKDFLFH",
      "managerDueDate": "2018-02-15",
      "sentToReview": "2018-02-01T12:09:24.198466Z",
      "sentToReviewBy": "WD43ZJGKDFLFH",
      "receivedFromReview": "2018-02-01T12:09:24.198466Z",
      "publishedDate": "2018-02-01T12:09:24.198466Z",
      "publishedBy": "WD43ZJGKDFLFH",
      "responseId": "2d46d30b-7dc1-4a65-991d-d739a1381eb8",
      "responseComment": "Revisions required before approval.",
      "respondedAt": "2018-02-01T12:09:24.198466Z",
      "respondedBy": "WD43ZJGKDFLFH",
      "packageId": "e8302552-fc5a-42ac-ba4b-e9de9760c356",
      "packageIdentifier": "222",
      "packageTitle": "my package1",
      "packageSpecIdentifier": "A-500",
      "folderUrn": "urn:adsk.wipprod:fs.file:vf.hvNfeldTPm_aDqRNZgKjD",
      "revisionsFoldersUrns": {
        "0": {
          "folderUrnCreatedAt": "2018-01-28 09:26:36.371607",
          "revision": 0,
          "folderUrn": "urn:adsk.wipprod:fs.folder:co.r04fl5B7QCa1731EeH5dYDQ"
        }
      },
      "createdAt": "2018-02-01T12:09:24.198466Z",
      "createdBy": "WD43ZJGKDFLFH",
      "updatedAt": "2018-04-04T12:09:24.198466Z",
      "updatedBy": "WD43ZJGKDFLFH",
      "permittedActions": [
        {
          "id": "Item::update",
          "fields": {
            "subcontractor": [],
            "manager": []
          },
          "mandatoryFields": [
            ""
          ],
          "transitions": [
            {
              "id": "rev::void",
              "name": "Send to void",
              "stateFrom": {
                "id": "rev",
                "name": "Review"
              },
              "stateTo": {
                "id": "void",
                "name": "Void"
              },
              "transitionFields": [
                "subcontractor",
                "subcontractorType",
                "watchers",
                "responseId"
              ],
              "mandatoryFields": [
                "responseId"
              ],
              "actionId": "ITEM_TRANSITION_REV_VOID"
            }
          ]
        }
      ]
    }
  ],
  "pagination": {
    "limit": 10,
    "offset": 100,
    "totalResults": 25,
    "previousUrl": "https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/settings/mappings?offset=10&limit=100",
    "nextUrl": null
  }
}

```

Show More
