# projects/{projectId}/items

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-items-POST/

---

# projects/{projectId}/items

Creates a new submittal item in the specified project.

Note that only Submittal managers can access submittals items in draft state.

For information about submittal items, see the Help documentation .

For detailed steps on creating submittal items, refer to the Create Submittal Item tutorial.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/items Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Request

## Body Structure

customIdentifier string A custom number to assign to the submittal item. Before creating an item, check what the custom numbering type is for the current project by calling GET metadata to get the custom identifier sequence type. Submittals support two custom numbering types: Global Numbering: The custom identifier only contains the sequential number. Spec Section Numbering: When the project uses spec section numbering for custom numbering, ensure that only the sequential number part of the custom identifier is sent in the request, excluding the spec ID. To find the next available custom number in the sequence, call GET items:next-custom-identifier . To verify whether the custom number has not been used and is in a supported format, call POST items:validate-custom-identifier . For more information on custom numbering, see the Help documentation . typeId * string The UUID of the item type to assign to the submittal item, which can be obtained by calling GET item-types or GET item-types/:id . specId * string: UUID The UUID of the spec section to assign to the submittal item. subsection string Define the subsection details of the submittal item. For example, 1.05-B . title * string The title of the submittal item defined by the user when creating the submittal item. description string A description of the submittal item to add context about its purpose. priority enum:string The priority level of the submittal item. Possible values: Low , Normal , High . When the priority is not set, the default value is Normal . stateId * enum:string The initial state of the submittal item, which depends on the role and permitted actions of the user. Possible values: draft , sbc-1 , mgr-1 . The required fields depend on the selected state ID. For example, if the state is mgr-1 , required fields include subcontractor ( subcontractor ), subcontractor type ( subcontractorType ), and submitter due date ( submitterDueDate ). If the state is sbc-1 , required fields include manager ( manager ) and manager type ( manager-type ). The required fields for creating the submittal item depend on the input stateId. The different states will require different mandatory fields. Refer Step 1: Verify User Permissions in the Create a Submittal Item tutorial for details. manager string The Autodesk ID ( autodeskId ) or Group ID ( memberGroupId ) specifying the manager to assign to the submittal item. The manager could be a user, role, or a company. Note that the user must be defined as a manager in the project. You can verify this by calling GET mappings . To get the possible values for a manager, call GET mappings and check the autodeskId. This returns a list of all the users, roles, and companies that are managers in the project. Call GET projects/users to verify the actual name of the user. If a company is a manager, call GET companies to verify the actual name of the company. Note that we do not currently support verifying names of roles. managerType enum:string The type of manager. This attribute is required when a manager is specified. To determine the type of manager, call GET mappings and check the user type. Possible values: 1 (user), 2 (company), 3 (role). subcontractor string The Autodesk ID of the subcontractor to assign to the submittal item. When creating a submittal item as a manager in the UI, you will see âassign to responsible contractorâ. Get the subcontractor ID using: GET projects/users to verify the actual name of the user in case the typs is a user (1). GET companies to determine the name of the company in case the typs is a company (2). Note that we do not currently support verifying names of roles. subcontractorType enum:string The type of subcontractor. This attribute is required when a subcontractor is specified.
Possible values: 1 (user), 2 (company), 3 (role). watchers array: object A list of project watchers, who can be individual users, roles, or companies. id * string The Autodesk ID of the watcher. The watcher can be a user ( autodeskId ), role ( memberGroupId ), or company ( memberGroupId ). To find details about users, call GET users , to find details about companies, call GET companies . Note that we do not currently support finding details about roles for a project. userType * object The type of watcher assigned to the submittal item. Possible values: 1 (user) 2 (company) 3 (role) requiredOnJobDate string The date when the materials are expected to arrive on the site, in the following format: YYYY-MM-DD (ISO 8601) in UTC. For example, 2018-02-15 . leadTime int The duration in days from the approval of the submittal to the delivery of materials or products to the construction site. requiredDate string The date the responsible contractor needs to submit the submittal to the submittal manager, in the following format: YYYY-MM-DD (ISO 8601) in UTC. For example, 2018-02-15 . requiredApprovalDate string The date by which approval for the submittal is required, in the following format: YYYY-MM-DD in UTC (ISO 8601). For example, 2018-02-15 . submitterDueDate string The date by which the subcontractor is expected to submit the submittal to the manager, in the following format: YYYY-MM-DD in UTC (ISO 8601). For example, 2018-02-15 . This corresponds to the sbc-1 state Waiting for submission . managerDueDate string The date by which the manager is expected to prepare the submittal item for review to the reviewer, in the following format: YYYY-MM-DD in UTC (ISO 8601). For example, 2018-02-15 . This corresponds to the mgr-1 state Open (Submitted) . packageId string: UUID The ID of the package associated with the submittal item. To retrieve a list of packages and their corresponding IDs, call GET packages . templateId string: UUID The ID of a review template used to apply predefined steps and tasks when creating a submittal item. Templates must be created in the UI or retrieved by calling GET templates .

Submittals support two custom numbering types:

- Global Numbering: The custom identifier only contains the sequential number.

- Spec Section Numbering: When the project uses spec section numbering for custom numbering, ensure that only the sequential number part of the custom identifier is sent in the request, excluding the spec ID.

To find the next available custom number in the sequence, call GET items:next-custom-identifier .

To verify whether the custom number has not been used and is in a supported format, call POST items:validate-custom-identifier .

For more information on custom numbering, see the Help documentation .

When the priority is not set, the default value is Normal .

Possible values: draft , sbc-1 , mgr-1 .

The required fields depend on the selected state ID. For example, if the state is mgr-1 , required fields include subcontractor ( subcontractor ), subcontractor type ( subcontractorType ), and submitter due date ( submitterDueDate ). If the state is sbc-1 , required fields include manager ( manager ) and manager type ( manager-type ).

The required fields for creating the submittal item depend on the input stateId. The different states will require different mandatory fields. Refer Step 1: Verify User Permissions in the Create a Submittal Item tutorial for details.

To get the possible values for a manager, call GET mappings and check the autodeskId. This returns a list of all the users, roles, and companies that are managers in the project. Call GET projects/users to verify the actual name of the user. If a company is a manager, call GET companies to verify the actual name of the company. Note that we do not currently support verifying names of roles.

Possible values: 1 (user), 2 (company), 3 (role).

Get the subcontractor ID using:

- GET projects/users to verify the actual name of the user in case the typs is a user (1).

- GET companies to determine the name of the company in case the typs is a company (2).

Note that we do not currently support verifying names of roles.

To find details about users, call GET users , to find details about companies, call GET companies . Note that we do not currently support finding details about roles for a project.

Possible values:

- 1 (user)

- 2 (company)

- 3 (role)

To retrieve a list of packages and their corresponding IDs, call GET packages .

### Response

## HTTP Status Code Summary

201 Created Creation of a submittal item. 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request headers. 401 Unauthorized Invalid or missing authorization header. Verify the Bearer token and try again. 403 Forbidden The user is not authorized to perform this action. 404 Not Found The specified resource was not found. 500 Internal Server Error An unexpected error occurred on the server while processing the request.

### Response

## Body Structure (201)

id string: UUID The internal, globally unique identifier (UUID) for the submittal item. identifier int The unique ID assigned to the submittal item within the UI. This ID is system-generated and serves as a reference for users interacting with submittal items through the UI. For example, 111 . customIdentifier string customIdentifier and customIdentifierHumanReadable relate to the Number column in the UI. Submittal managers assign custom numbers to items (manually or automatically). Custom numbers are configured either in global numbering format: <global number>, or in spec section numbering format: <spec ID>-<sequential number>. For projects with a global numbering format, both customIdentifier and customIdentifierHumanReadable represent the global number. For projects with a spec section numbering format (<spec ID>-<sequential number>), customIdentifier represents the sequential number. For example, for a full number of 033100-01 , customIdentifier is 01 . Note that for unnumbered items customIdentifier is null . For more information on custom numbering, see the Help documentation . customIdentifierHumanReadable string customIdentifierHumanReadable and customIdentifier relate to the Number column in the UI. Submittal managers assign custom numbers to items (manually or automatically). Custom numbers are configured either in global numbering format: <global number>, or in spec section numbering format: <spec ID>-<sequential number>. For projects with a global numbering format, both customIdentifier and customIdentifierHumanReadable represent the global number. For projects with a spec section numbering format (<spec ID>-<sequential number>), customIdentifierHumanReadable represents the full number - both the spec ID and the sequential number. For example, for a full number of 033100-01 , customIdentifierHumanReadable is 033100-01 . Note that for unnumbered items customIdentifierHumanReadable is Unspecified . For spec section numbering it also includes the spec ID. For example, 033100-Unspecified . For more information on custom numbering, see the Help documentation . typeId string The ID representing the type of submittal item. specId string: UUID The unique identifier (UUID) of the spec assigned to the submittal item. specIdentifier string The identifier of the spec section that is associated with the submittal item. The identifier is assigned to the spec section in the UI. specTitle string The title of the spec associated with the submittal item. subsection string The sub-spec section associated with the submittal item, providing additional categorization within the main spec. title string The title of the submittal item. description string The description of the submittal item. priority enum:string The priority of the submittal item. Possible values: Low Normal High revision int The revision number of the submittal item, indicating the version of the item in the submittal workflow. For example, 1 for the initial submission or 2 for the first revision. stateId enum:string The current state of the submittal item after the transition. Possible values: sbc-1 (Waiting for Submission) - Assigned to the Responsible Contractor, who needs to submit the submittal to the Manager. mgr-1 (Open - Submitted) - Assigned to the Manager, who needs to prepare the submittal item for review. rev (Open - In Review) - Under review by the reviewers defined in the submittal itemâs review workflow. mgr-2 (Open - Reviewed) - The review is complete, and the submittal is returned to the Manager, who needs to set the final response and close the submittal. sbc-2 : (Closed) - The submittal has been closed and assigned to the Responsible Contractor. void (Voided) - The submittal item has been voided. draft (Draft) - Assigned to the Manager, who must send the submittal item to the Responsible Contractor. statusId enum:string The status of the submittal item. Possible values: 1 - (Required), 2 - (Open), 3 - (Closed), 4 - (Void), 5 - (Empty), 6 - (Draft). To retrieve the full list of possible statuses, call GET metadata . ballInCourtUsers array: string The Autodesk IDs of users who are currently assigned to the submittal item at this stage of the workflow. ballInCourtCompanies array: string The member group IDs of the companies currently assigned to the submittal item at this stage of the workflow. ballInCourtRoles array: string The member group IDs of user roles that are currently assigned to the submittal item at this stage of the workflow. ballInCourtType enum:string âThe type of submittal role assigned to the user currently assigned to the submittal item. Possible values: reviewer , manager , subcontractor .â manager string The ID that was assigned to the manager of the submittal item. If the creator of the submittal item held a manager role, they were automatically set as the manager ( manager ). To determine the type of the manager (i.e., user, role, or company), refer to the manager type ( managerType ) attribute.
In order to get more info about the manager, use: GET projects/users to verify the actual name of the user in case the typs is a user (1). GET companies to determine the name of the company in case the typs is a company (2). Note that we do not currently support verifying names of roles. managerType enum:string The type of manager associated with the submittal item. Possible values: 1 (user), 2 (company), 3 (role). subcontractor string The ID that was assigned to the subcontractor for the submittal item. If a non-manager user created the submittal item and chose a manager, they are automatically assigned as the subcontractor of the submittal item.
In order to get more info about the subcontractor, use: GET projects/users to verify the actual name of the user in case the typs is a user (1). GET companies to determine the name of the company in case the typs is a company (2). Note that we do not currently support verifying names of roles. subcontractorType enum:string The type of subcontractor associated with the submittal item. Possible values: 1 (user), 2 (company), 3 (role). watchers array: object A list of project watchers, who can be individual users, roles, or companies. id string The Autodesk ID of the watcher. The watcher can be a user ( autodeskId ), role ( memberGroupId ), or company ( memberGroupId ). To find details about users, call GET users , to find details about companies, call GET companies . Note that we do not currently support finding details about roles for a project. userType object The type of watcher assigned to the submittal item. Possible values: 1 (user) 2 (company) 3 (role) dueDate string The due date for the submittal item, formatted as YYYY-MM-DD in UTC (ISO 8601). For example, 2018-02-15 . requiredOnJobDate string The date when the materials are expected to arrive on the construction site, formatted as YYYY-MM-DD in UTC (ISO 8601). For example, 2018-02-15 . leadTime int The duration (in days) from the approval of the submittal to delivery of materials or products to the construction site. requiredDate string The date by which the Responsible Contractor must submit the submittal to the submittal manager, formatted as YYYY-MM-DD in UTC (ISO 8601). For example, 2018-02-15 . requiredApprovalDate string The date by which approval for the submittal is required, formatted as YYYY-MM-DD in UTC (ISO 8601). For example, 2018-02-15 . submitterDueDate string The date by which the subcontractor is expected to submit the submittal to the manager, formatted as YYYY-MM-DD in UTC (ISO 8601). For example, 2018-02-15 . This corresponds to the sbc-1 state Waiting for submission . sentToSubmitter datetime: ISO 8601 The date and time when the submittal was sent to the subcontractor for review, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2018-02-15T12:09:24.198466Z . This corresponds to transition to the sbc-1 state. receivedFromSubmitter datetime: ISO 8601 The date when the submittal was received back from the subcontractor after review, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2018-02-15T12:09:24.198466Z . This corresponds to transition to mgr-1 state Open (Submitted) . submittedBy string The Autodesk ID of the user who submitted the submittal item. This is the user who transitioned the item to the manager. managerDueDate string The date by which the manager is expected to prepare the submittal item for review, formatted as YYYY-MM-DD in UTC (ISO 8601). For example, 2018-02-15 . This corresponds to the mgr-1 state Open (Submitted) . sentToReview datetime: ISO 8601 The date and time when the submittal item transitioned to the rev state (Open - In review) , formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2018-02-15T12:09:24.198466Z . sentToReviewBy string The Autodesk ID of the user who transitioned the item to the rev state (Open - In review) . receivedFromReview datetime: ISO 8601 The date and time when the submittal item transitioned from the rev state (Open - In Review) to the mgr-2 state (Close and distribute) , formatted as YYYY-MM-DD (ISO 8601) in UTC. For example, 2022-03-02T12:09:24Z . publishedDate datetime: ISO 8601 The date when the manager closed and distributed the submittal item, in the following format: YYYY-MM-DD (ISO 8601) in UTC. For example, 2018-02-15 . publishedBy string The Autodesk ID of the user who published the submittal item. responseId string The ID of the response associated with the submittal item, linking to the specific feedback or action taken. responseComment string The body of the response comment, containing feedback or instructions related to the submittal item. respondedAt datetime: ISO 8601 The date and time when the response was added, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2018-02-15T12:09:24.198466Z . respondedBy string The Autodesk ID of the user that gave the response to the submittal item. packageId string: UUID The ID of the package associated with the submittal item. packageIdentifier string The package identifier as displayed in the UI. packageTitle string The title of the package associated with the submittal item. packageSpecIdentifier string The identifier of the submittal spec associated with the package. This value corresponds to the âSpec sectionâ displayed in the UI, such as 1 - Cement . folderUrn string The URN of the folder that contains the attachments associated with the submittal items. revisionsFoldersUrns object An object containing URNs that represent folders associated with the revisions of the submittal item. These URNs can be used to access and identify specific folders related to submittal item revisions within the system. createdAt datetime: ISO 8601 The date and time when the submittal item was originally created, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2018-02-15T12:09:24.198466Z . createdBy string The Autodesk ID of the user who created the submittal item. updatedAt datetime: ISO 8601 The time and date when the submittal item was last updated, formatted as YYYY-MM-DDTHH:mm:ss.SSSSSSZ (ISO 8601) in UTC. For example, 2018-02-15T12:09:24.198466Z . updatedBy string The Autodesk ID of the user who last updated the submittal item. permittedActions array: object The list of actions the user is allowed to perform on the submittal item. id string The ID of the action in the format type_of_object::action . For example, Item::retrieve . fields object A list of field names for which values must be provided when performing the action. An empty array indicates no specific set of values. mandatoryFields array: string Lists the fields that are required when updating a submittal item. The required fields depend on the action being performed, the itemâs current state, and the userâs role. For example: To transition the state of a submittal item, stateId and responseId are required.
To reassign the manager, manager and managerType are required.
To modify the spec section, specId is required. transitions array: object The list of possible state transitions for a submittal item within the review workflow. id string The ID of the transition in the format from-state::to-state . For example, create::mgr-1 , mgr-1::mgr-2 , rev::void . name string The descriptive name of the transition. For example, Create , Send to Manager , Send to void . stateFrom object The starting state of the transition, representing the current position of the submittal item in the workflow. id string The unique ID of the starting state. For example, create , mgr-1 , rev . The rev state indicates that the submittal item is currently under review. name string The name of the starting state. For example, Create , Manager Review , Review . stateTo object The target state of the transition, indicating the next position of the submittal item in the workflow. id string The unique ID of the target state. For example, mgr-1 , mgr-2 , void . name string The name of the target state. For example, Manager Review , Manager Final Review , Void . transitionFields array: string Fields that are used in the transition. For example, [ subcontractor , subcontractorType , watchers , responseId ]. mandatoryFields array: string A list of required fields for the transition. For example, [ responseId ]. actionId string Not relevant

For projects with a global numbering format, both customIdentifier and customIdentifierHumanReadable represent the global number.

For projects with a spec section numbering format (<spec ID>-<sequential number>), customIdentifier represents the sequential number. For example, for a full number of 033100-01 , customIdentifier is 01 .

Note that for unnumbered items customIdentifier is null .

For more information on custom numbering, see the Help documentation .

For projects with a global numbering format, both customIdentifier and customIdentifierHumanReadable represent the global number.

For projects with a spec section numbering format (<spec ID>-<sequential number>), customIdentifierHumanReadable represents the full number - both the spec ID and the sequential number. For example, for a full number of 033100-01 , customIdentifierHumanReadable is 033100-01 .

Note that for unnumbered items customIdentifierHumanReadable is Unspecified . For spec section numbering it also includes the spec ID. For example, 033100-Unspecified .

For more information on custom numbering, see the Help documentation .

Possible values:

- Low

- Normal

- High

Possible values:

sbc-1 (Waiting for Submission) - Assigned to the Responsible Contractor, who needs to submit the submittal to the Manager.

mgr-1 (Open - Submitted) - Assigned to the Manager, who needs to prepare the submittal item for review.

rev (Open - In Review) - Under review by the reviewers defined in the submittal itemâs review workflow.

mgr-2 (Open - Reviewed) - The review is complete, and the submittal is returned to the Manager, who needs to set the final response and close the submittal.

sbc-2 : (Closed) - The submittal has been closed and assigned to the Responsible Contractor.

void (Voided) - The submittal item has been voided.

draft (Draft) - Assigned to the Manager, who must send the submittal item to the Responsible Contractor.

Possible values: 1 - (Required), 2 - (Open), 3 - (Closed), 4 - (Void), 5 - (Empty), 6 - (Draft).

To retrieve the full list of possible statuses, call GET metadata .

Possible values: reviewer , manager , subcontractor .â

To determine the type of the manager (i.e., user, role, or company), refer to the manager type ( managerType ) attribute.
In order to get more info about the manager, use:

- GET projects/users to verify the actual name of the user in case the typs is a user (1).

- GET companies to determine the name of the company in case the typs is a company (2).

Note that we do not currently support verifying names of roles.

Possible values: 1 (user), 2 (company), 3 (role).

- GET projects/users to verify the actual name of the user in case the typs is a user (1).

- GET companies to determine the name of the company in case the typs is a company (2).

Note that we do not currently support verifying names of roles.

Possible values: 1 (user), 2 (company), 3 (role).

To find details about users, call GET users , to find details about companies, call GET companies . Note that we do not currently support finding details about roles for a project.

Possible values:

- 1 (user)

- 2 (company)

- 3 (role)

The required fields depend on the action being performed, the itemâs current state, and the userâs role.

For example:

To transition the state of a submittal item, stateId and responseId are required.
To reassign the manager, manager and managerType are required.
To modify the spec section, specId is required.

## Example

Creation of a submittal item

### Request

```
curl - v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/items' \ - X 'POST' \ - H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ - H 'Content-Type: application/json' \ - d '{ "customIdentifier": "A-111", "typeId": "06fa0c1b-6462-459d-8a38-0aff11bfe868", "specId": "62d6f245-b470-4af4-802b-4cb94b5dead1", "subsection": "1.05-B", "title": "Shop Drawings", "description": "Detailed plans by subcontractor, showing project dimensions.", "priority": "Low", "stateId": "sbc-1", "subcontractor": "WD43ZJGKDFLFH", "subcontractorType": "1", "watchers": [ { "id": "224356", "userType": "2" }, { "id": "3522614", "userType": "3" } ], "requiredOnJobDate": "2024-02-15", "leadTime": 100, "requiredDate": "2024-02-15", "requiredApprovalDate": "2024-02-15", "submitterDueDate": "2024-02-15", "packageId": "e8302552-fc5a-42ac-ba4b-e9de9760c356" }'
```

### Response

```
{ "id" : "b8cc9324-6759-4f07-8ce3-725d5afd4f11" , "identifier" : 1111 , "customIdentifier" : "A-111" , "customIdentifierHumanReadable" : "0001-A-111" , "typeId" : "06fa0c1b-6462-459d-8a38-0aff11bfe868" , "specId" : "62d6f245-b470-4af4-802b-4cb94b5dead1" , "specIdentifier" : "09-5300" , "specTitle" : "Acoustical Ceilings" , "subsection" : "1.05-B" , "title" : "Shop Drawings" , "description" : "Detailed plans by subcontractor, showing project dimensions." , "priority" : "Low" , "revision" : 0 , "stateId" : "sbc-1" , "statusId" : "1" , "ballInCourtUsers" : [ "WD43ZJGKDFLFH" ], "ballInCourtCompanies" : [ ], "ballInCourtRoles" : [ ], "ballInCourtType" : "subcontractor" , "manager" : "WD43ZJGKDFLFH" , "managerType" : "1" , "subcontractor" : "WD43ZJGKDFLFH" , "subcontractorType" : "1" , "watchers" : [ { "id" : "224356" , "userType" : "2" }, { "id" : "3522614" , "userType" : "3" } ], "dueDate" : "2024-02-15" , "requiredOnJobDate" : "2024-02-15" , "leadTime" : 100 , "requiredDate" : "2024-02-15" , "requiredApprovalDate" : "2024-02-15" , "submitterDueDate" : "2024-02-15" , "sentToSubmitter" : "2024-02-01T12:09:24.198466Z" , "receivedFromSubmitter" : null , "submittedBy" : null , "managerDueDate" : null , "sentToReview" : null , "sentToReviewBy" : null , "receivedFromReview" : null , "publishedDate" : null , "publishedBy" : null , "responseId" : null , "responseComment" : "" , "respondedAt" : null , "respondedBy" : null , "packageId" : "e8302552-fc5a-42ac-ba4b-e9de9760c356" , "packageIdentifier" : "222" , "packageTitle" : "my package1" , "packageSpecIdentifier" : "A-500" , "folderUrn" : "urn:adsk.wipprod:fs.file:vf.hvNfeldTPm_aDqRNZgKjD" , "revisionsFoldersUrns" : { "0" : { "folderUrnCreatedAt" : "2018-01-28 09:26:36.371607" , "revision" : 0 , "folderUrn" : "urn:adsk.wipprod:fs.folder:co.r04fl5B7QCa1731EeH5dYDQ" } }, "createdAt" : "2024-02-01T12:09:24.198466Z" , "createdBy" : "WD43ZJGKDFLFH" , "updatedAt" : "2024-02-01T12:09:24.198466Z" , "updatedBy" : "WD43ZJGKDFLFH" , "permittedActions" : [ { "id" : "Item::retrieve" , "fields" : {}, "mandatoryFields" : [], "transitions" : [] }, { "id" : "Item::create_revision" , "fields" : { "subcontractor" : [], "subcontractorType" : [], "submitterDueDate" : [], "watchers" : [], "mailNote" : [] }, "mandatoryFields" : [ "subcontractor" , "subcontractorType" , "submitterDueDate" ], "transitions" : [] } ] }
```
