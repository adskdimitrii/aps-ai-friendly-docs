# projects/{projectId}/items/{itemId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-items-itemId-PATCH/

---

Items

PATCH

# projects/{projectId}/items/{itemId}

Updates specific attributes of an existing submittal item. Only fields listed in the `permittedActions` object can be modified.

To check which fields can be updated, call [GET item/:id](http-submittals-items-itemId-GET.md) and review the object with `id: "Item::partial_update"` in the `permittedActions` array in the response.

For more information on managing submittals, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Process_Submittal).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/items/:itemId |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring: UUID The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- itemIdstring The ID of the submittal item. To find the item ID, call [GET items](http-submittals-items-GET.md).

### Request

## [Body Structure](#body-structure)

Expand all

| customIdentifier   string | A custom number to assign to the submittal item. Before updating an item, check what the custom numbering type is for the current project by calling [GET metadata](http-submittals-metadata-GET.md) to get the custom identifier sequence type. <br>Submittals support two custom numbering types:<br>Global Numbering: The custom identifier only contains the sequential number.Spec Section Numbering: When the project uses spec section numbering for custom numbering, ensure that only the sequential number part of the custom identifier is sent in the request, excluding the spec ID.<br>To find the next available custom number in the sequence, call [GET items:next-custom-identifier](http-submittals-itemsnext-custom-identifier-GET.md).<br>To verify whether the custom number has not been used and is in a supported format, call [POST items:validate-custom-identifier](http-submittals-itemsvalidate-custom-identifier-POST.md).<br>For more information on custom numbering, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Custom_Numbering). |
| --- | --- |
| typeId   string: UUID | The ID of the item type to assign to the submittal item. To retrieve the type ID, call [GET item-types](http-submittals-item-types-GET.md) or [GET item-types/:id](http-submittals-item-types-id-GET.md). |
| specId   string: UUID | The unique identifier (UUID) of the spec section to assign to the submittal item, which can be obtained by calling [GET specs](http-submittals-specs-GET.md). |
| subsection   string | Define the subsection details of the submittal item. For example, `1.05-B`. |
| title   string | The title of the submittal item defined by the user when updating the submittal item. |
| description   string | A description of the submittal item to add context about its purpose. |
| priority   enum:string | The priority level of the submittal item. <br>Possible values:<br>`Low``Normal``High`<br>When the priority is not set, the default value is `Normal`. |
| manager   string | The Autodesk ID (`autodeskId`) or Group ID (`memberGroupId`) specifying the manager to assign to the submittal item. The manager could be a user, role, or a company. Note that the user must be defined as a manager in the project. You can verify this by calling [GET mappings](http-submittals-mappings-GET.md). <br>To get the possible values for a manager, call [GET mappings](http-submittals-mappings-GET.md) and check the autodeskId. This returns a list of all the users, roles, and companies that are managers in the project. Call [GET projects/users](http-admin-projectsprojectId-users-GET.md) to verify the actual name of the user. If a copmany is a manager, call [GET companies](http-projects--project_id-companies-GET.md) to verify the actual name of the company. Note that we do not currently support verifying names of roles. |
| managerType   enum:string | The type of manager. This attribute is required when a manager is specified. To determine the type of manager, call [GET mappings](http-submittals-mappings-GET.md) and check the user type. <br>Possible values: `1` (user), `2` (company), `3` (role). |
| subcontractor   string | The Autodesk ID of the subcontractor to assign to the submittal item. When updating a submittal item as a manager in the UI, you will see ‘assign to responsible contractor’. The subcontractor can be a user (`autodeskId`), role (`memberGroupId`), or company (`memberGroupId`). <br>For users, call [GET users](http-admin-projectsprojectId-users-GET.md). For companies, call [GET companies](http-projects--project_id-companies-GET.md).<br>Note that we do not currently support finding details about roles for a project. |
| subcontractorType   enum:string | The type of subcontractor. This attribute is required when a subcontrator is specified. Possible values: `1` (user), `2` (company), `3` (role). |
| sentToSubmitter   datetime: ISO 8601 | The date and time when the submittal was sent to the subcontrator for review, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2018-02-15T12:09:24.198466Z`. |
| receivedFromSubmitter   datetime: ISO 8601 | The date and time when the submittal was received back from the subcontractor after review, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2018-02-15T12:09:24.198466Z`. |
| sentToReview   datetime: ISO 8601 | The date and time when the submittal item was transitioned to the `rev` state `(Open - In review)`, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2018-02-15T12:09:24.198466Z`. |
| receivedFromReview   datetime: ISO 8601 | The timestamp marking when the item transitioned from the `rev` state `(Open - In Review)` to the `mgr-2` state `(close and distribute)`, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2018-02-15T12:09:24.198466Z`. |
| publishedDate   datetime: ISO 8601 | The date when the manager closed and distributed the submittal item, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2018-02-15T12:09:24.198466Z`. |
| watchers   array: object | A list of project watchers, who can be individual users, roles, or companies. |
| id*   string | The Autodesk ID of the watcher. The watcher can be a user (`autodeskId`), role (`memberGroupId`), or company (`memberGroupId`). <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](http-projects--project_id-companies-GET.md). Note that we do not currently support finding details about roles for a project. |
| userType*   object | The type of watcher assigned to the submittal item. <br>Possible values:<br>`1` (user)`2` (company)`3` (role) |
| requiredOnJobDate   string | The date when the materials are expected to arrive on the site, in the following format: YYYY-MM-DD (ISO 8601) in UTC. For example, `2018-02-15`. |
| leadTime   int | The duration (in days) from the approval of the submittal to the delivery of materials or products to the construction site. |
| requiredDate   string | The date the responsible contractor needs to submit the submittal to the submittal manager, in the following format: YYYY-MM-DD (ISO 8601) in UTC. For example, `2018-02-15`. |
| requiredApprovalDate   string | The date by which approval for the submittal is required, in the following format: YYYY-MM-DD in UTC (ISO 8601). For example, `2018-02-15`. |
| submitterDueDate   string | The date by which the subcontractor is expected to submit the submittal to the manager, formatted as YYYY-MM-DD in UTC (ISO 8601). For example, `2018-02-15`. |
| managerDueDate   string | The date by which the manager is expected to prepare the submittal item for review to the reviewer, in the following format: YYYY-MM-DD in UTC (ISO 8601). For example, `2018-02-15`. |
| packageId   string: UUID | The ID of the package associated with the submittal item. This attribute is optional and is used for workflows involving attachments. <br>To retrieve package details, call [GET packages](http-submittals-packages-GET.md). |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully updated a submittal item. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. |
| 401   Unauthorized | Invalid or missing authorization header. Verify the Bearer token and try again. |
| 403   Forbidden | The user is not authorized to perform this action. |
| 404   Not Found | The specified resource was not found. |
| 500   Internal Server Error | An unexpected error occurred on the server while processing the request. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| id   string: UUID | The internal, globally unique identifier (UUID) for the submittal item. |
| --- | --- |
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
| stateId   enum:string | The current state of the submittal item after the transition. <br>Possible values:<br>`sbc-1` (Waiting for Submission) - Assigned to the Responsible Contractor, who needs to submit the submittal to the Manager.<br>`mgr-1` (Open - Submitted) - Assigned to the Manager, who needs to prepare the submittal item for review.<br>`rev` (Open - In Review) - Under review by the reviewers defined in the submittal item’s review workflow.<br>`mgr-2` (Open - Reviewed) - The review is complete, and the submittal is returned to the Manager, who needs to set the final response and close the submittal.<br>`sbc-2`: (Closed) - The submittal has been closed and assigned to the Responsible Contractor.<br>`void` (Voided) - The submittal item has been voided.<br>`draft` (Draft) - Assigned to the Manager, who must send the submittal item to the Responsible Contractor. |
| statusId   enum:string | The status of the submittal item. <br>Possible values: `1` - (Required), `2` - (Open), `3` - (Closed), `4` - (Void), `5` - (Empty), `6` - (Draft).<br>To retrieve the full list of possible statuses, call [GET metadata](http-submittals-metadata-GET.md). |
| ballInCourtUsers   array: string | The Autodesk IDs of users who are currently assigned to the submittal item at this stage of the workflow. |
| ballInCourtCompanies   array: string | The member group IDs of the companies currently assigned to the submittal item at this stage of the workflow. |
| ballInCourtRoles   array: string | The member group IDs of user roles that are currently assigned to the submittal item at this stage of the workflow. |
| ballInCourtType   enum:string | ‘The type of submittal role assigned to the user currently assigned to the submittal item. <br>Possible values: `reviewer`, `manager`, `subcontractor`.’ |
| manager   string | The ID that was assigned to the manager of the submittal item. <br>To determine the type of the manager (user, role, or company), refer to the manager type (`managerType`) attribute. In order to get more info about the manager, use:  > [GET projects/users](http-admin-projectsprojectId-users-GET.md) to verify the actual name of the user in case the typs is a `user` (1).[GET companies](http-projects--project_id-companies-GET.md) to determine the name of the company in case the typs is a `company` (2). <br>Note that we do not currently support verifying names of roles. |
| managerType   enum:string | The type of manager associated with the submittal item. <br>Possible values: `1` (user), `2` (company), `3` (role). |
| subcontractor   string | The ID that was assigned to the subcontractor for the submittal item. If a non-manager user created the submittal item and chose a manager, they are automatically assigned as the `subcontractor` of the submittal item. In order to get more info about the subcontractor, use:  > [GET projects/users](http-admin-projectsprojectId-users-GET.md) to verify the actual name of the user in case the typs is a `user` (1).[GET companies](http-projects--project_id-companies-GET.md) to determine the name of the company in case the typs is a `company` (2). <br>Note that we do not currently support verifying names of roles. |
| subcontractorType   enum:string | The type of subcontractor associated with the submittal item. <br>Possible values: `1` (user), `2` (company), `3` (role). |
| watchers   array: object | A list of project watchers, who can be individual users, roles, or companies. |
| id   string | The Autodesk ID of the watcher. The watcher can be a user (`autodeskId`), role (`memberGroupId`), or company (`memberGroupId`). <br>To find details about users, call [GET users](http-admin-projectsprojectId-users-GET.md), to find details about companies, call [GET companies](http-projects--project_id-companies-GET.md). Note that we do not currently support finding details about roles for a project. |
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
| packageSpecIdentifier   string | The identifier of the submittal spec associated with the package. This value corresponds to the “Spec section” displayed in the UI, such as `1 - Cement`. |
| folderUrn   string | The URN of the folder that contains the attachments associated with the submittal items. |
| revisionsFoldersUrns   object | An object containing URNs that represent folders associated with the revisions of the submittal item. These URNs can be used to access and identify specific folders related to submittal item revisions within the system. |
| createdAt   datetime: ISO 8601 | The date and time when the submittal item was originally created, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2018-02-15T12:09:24.198466Z`. |
| createdBy   string | The Autodesk ID of the user who created the submittal item. |
| updatedAt   datetime: ISO 8601 | The time and date when the submittal item was last updated, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, `2018-02-15T12:09:24.198466Z`. |
| updatedBy   string | The Autodesk ID of the user who last updated the submittal item. |
| permittedActions   array: object | The list of actions the user is allowed to perform on the submittal item. |
| id   string | The ID of the action in the format `type_of_object::action`. For example, `Item::retrieve`. |
| fields   object | A list of field names for which values must be provided when performing the action. An empty array indicates no specific set of values. |
| mandatoryFields   array: string | Lists the fields that are required when updating a submittal item. <br>The required fields depend on the action being performed, the item’s current state, and the user’s role.<br>For example:<br>To transition the state of a submittal item, `stateId` and `responseId` are required. To reassign the manager, `manager` and `managerType` are required. To modify the spec section, `specId` is required. |
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

## [Example](#example)

Successfully updated a submittal item.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/items/767b5888-2c6a-413d-8487-613966dd64ce' \
  -X 'PATCH' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "customIdentifier": "A-111",
        "typeId": "06fa0c1b-6462-459d-8a38-0aff11bfe868",
        "specId": "62d6f245-b470-4af4-802b-4cb94b5dead1",
        "subsection": "1.05-B",
        "title": "Shop Drawings",
        "description": "Detailed plans by subcontractor, showing project dimensions.",
        "priority": "Low",
        "manager": "WD43ZJGKDFLFH",
        "managerType": "1",
        "subcontractor": "WD43ZJGKDFLFH",
        "subcontractorType": "1",
        "sentToSubmitter": "2018-02-01T12:09:24.198466Z",
        "receivedFromSubmitter": "2018-02-01T12:09:24.198466Z",
        "sentToReview": "2018-02-01T12:09:24.198466Z",
        "receivedFromReview": "2018-02-01T12:09:24.198466Z",
        "publishedDate": "2018-02-01T12:09:24.198466Z",
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
        "requiredOnJobDate": "2018-02-15",
        "leadTime": 100,
        "requiredDate": "2018-02-15",
        "requiredApprovalDate": "2018-02-15",
        "submitterDueDate": "2018-02-15",
        "managerDueDate": "2018-02-15",
        "packageId": "e8302552-fc5a-42ac-ba4b-e9de9760c356"
      }'

```

Show More

### Response

```
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

```

Show More
