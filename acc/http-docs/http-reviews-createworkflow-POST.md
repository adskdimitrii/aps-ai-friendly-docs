# projects/{projectId}/workflows

Source: https://aps.autodesk.com/en/docs/acc/reference/http/reviews-createworkflow-POST/

---

Create an Approval Workflow

POST

# projects/{projectId}/workflows

Creates a new approval workflow in the specified project.

The workflow defines the steps, reviewers, durations, approval statuses, and post-review actions, and it can include customized configuration options. Note that `updateAttributesOptions` and `attachedAttributes` are not configurable and are automatically set to `false`.

For more details about approval workflows, see the [Help documentation](https://help.autodesk.com/view/DOCS/ENU/?guid=Reviews_Workflow).

The `Authorization` header token can be obtained through either the [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token/) OAuth flow or the [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token/) OAuth flow with user impersonation, which requires the `x-user-id` header.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/reviews/v1/projects/{projectId}/workflows |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| x-user-id   string | The ID of a user on whose behalf the request is made. Your application has access to all users specified by the administrator in the SaaS Integrations UI. Use this header to specify which user should be affected by the request. <br>This header is only required when using two-legged authentication. It is not needed for three-legged authentication.<br>Only userâs Autodesk ID (`autodeskId`) can be accepted. |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You can provide the project ID with or without the â**b.**" prefix.<br>Example with prefix: **b.563a4c30-e30d-4869-ac02-2a18b6447abe**Example without prefix: **563a4c30-e30d-4869-ac02-2a18b6447abe** |
| --- | --- |

### Request

## [Body Structure](#body-structure)

Expand all

| name*   string | The name of the workflow. It must be unique within the project. <br>Max length: 255 |
| --- | --- |
| description   string | A description of the workflow. <br>Max length: 4096 |
| notes   string | A custom note associated with the workflow. Visible to all reviewers during the review process. <br>Max length: 4096 |
| additionalOptions   object | Workflow-level settings that control whether the initiator can modify certain fields when starting a review. |
| allowInitiatorToEdit   boolean | (`Allow Initiators to edit the review` in the UI). Indicates whether the initiator can adjust reviewer assignments and step durations. <br>`true`: the initiator can change reviewer assignments and durations.<br>`false`: (default) reviewers and durations are fixed. |
| additionalApprovalStatusOptions   array: object | Custom approval statuses to add in addition to the built-in statuses (`APPROVED`, `REJECTED`). You can define up to 50. |
| label*   string | The display name shown in the UI. It m ust be unique across all status options (built-in and custom). <br>Maximum length: 255 characters.<br>Max length: 255 |
| value*   enum:string | The value representing the approval outcome. Possible values: `APPROVED`, `REJECTED`. |
| copyFilesOptions*   object | (`Copy approved files` in the UI) The configuration for copying approved files to a target folder when the review is complete. |
| enabled*   boolean | Indicates whether approved files should be copied to a target folder after the review is complete. <br>`true`: copy approved files to the target folder.<br>`false`: do not copy approved files. |
| allowOverride   boolean | (`Allow the initiator to change the target folder` in the UI) Allows the initiator to change the target folder when creating a review. <br>`true`: the initiator can choose a different target folder.<br>`false`: the folder defined in the workflow is used. |
| condition   string | (`All/Any files in the review have been approved` in the UI) Specifies the condition under which approved files will be copied. <br>Possible values:<br>`ANY`: copy files if at least one file in the review is approved.<br>`ALL`: copy files only if all files in the review are approved. |
| folderUrn   string | (`Then copy approved files to` in the UI) The URN of the target folder where approved files will be copied. |
| includeMarkups   boolean | (`Include all published markups on approved files` in the UI) Indicates whether published markups should be included when copying files. <br>`true`: include all published (unarchived) markups from the source version.<br>`false`: (default) do not include markups. |
| disableOverrideMarkupSetting   boolean | (`Allow approvers to change whether or not markups are included` in the UI) Controls whether approvers or admins can change the markup inclusion setting when starting the review. <br>`true`: the markup setting is locked and cannot be changed.<br>`false`: the setting can be changed during review setup. |
| steps*   array: object | Defines the sequence of steps in the workflow. Steps run in the order they appear. |
| name*   string | The name of the step, as defined in the workflow. It appears in the UI and is used in workflow configuration. Maximum length: 255 characters. <br>Max length: 255 |
| type*   enum:string | Indicates the step type in the workflow. Possible values: <br>`INITIATOR`: the first step. It typically represents the person who launches the review.`REVIEWER`: an intermediate step. It allows one or more reviewers to evaluate the files.`APPROVER`: the final step. It represents the decision maker who approves or rejects the files. |
| duration   int | (`Time allowed` in the UI) The number of days allocated to complete this step. <br>This field applies only to `REVIEWER` and `APPROVER` steps. It is used to calculate the due date based on the selected `dueDateType`.<br>Valid range: `1â99`. |
| dueDateType   enum:string | Specifies how the due date is calculated for this step. It works together with duration. <br>This field applies only to `REVIEWER` and `APPROVER` steps.<br>Possible values:<br>`CALENDAR_DAY` (default): the due date includes all calendar days, including weekends and holidays.`WORKDAY`: the due date excludes weekends and project holidays. |
| groupReview   object | (`Reviewer Type` in the UI) Defines whether multiple reviewers can participate in this step and how their responses are handled. It applies only to `REVIEWER` steps. |
| enabled*   boolean | Indicates whether group review is enabled for this step. <br>`true`: multiple reviewers can participate in the step.<br>`false`: (default) only a single reviewer is allowed. |
| type   enum:string | (Displayed under `More options` in the UI) Specifies the group review rule for this step. <br>Possible values:<br>`ALL`: every reviewer assigned to the step must submit a response (up to 30).`MINIMUM`: only a specified number of reviewers must respond, as defined in `min`. |
| min   int | The minimum number of reviewers required for this step. This field is set automatically when the group review type is set to `MINIMUM`. It is not independently configurable. Valid range: `1â30`. |
| candidates*   object | (Displayed in the UI when selecting Reviewers/Approvers for a step) Defines the users, roles, or companies to specify for this step of the approval workflow. At least one of the fields (`users`, `roles`, or `companies`) must be provided. |
| users   array: object | A list of individual users assigned as candidates for this step. |
| autodeskId*   string | The Autodesk ID of the user. To find the Autodesk IDs of users for a project, call [GET projects/users](/en/docs/acc/v1/reference/http/admin-projectsprojectId-users-GET/). |
| roles   array: object | A list of project roles assigned as candidates for this step. |
| autodeskId*   string | The Autodesk ID of the role. Note that we do not currently support finding details about roles for a project. |
| companies   array: object | A list of companies assigned as candidates for this step. |
| autodeskId*   string | The Autodesk ID of the company. To find the Autodesk IDs of companies for a project, call [GET companies](/en/docs/acc/v1/reference/http/companies-GET/). |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | The workflow was created successfully. |
| --- | --- |
| 400   Bad Request | Bad request. The input parameters were invalid. |
| 403   Forbidden | Forbidden. The user does not have permission to access this resource. |
| 404   Not Found | Not found. The resource does not exist or is inaccessible. |
| 409   Conflict | Existing a same name workflow in the project |
| 500   Internal Server Error | An unexpected server error occurred. |

### Response

## [Body Structure (201)](#body-structure-201)

Expand all

| name   string | The name of the workflow. It must be unique within the project. <br>Max length: 255 |
| --- | --- |
| description   string | A description of the workflow. <br>Max length: 4096 |
| notes   string | A custom note associated with the workflow. Visible to all reviewers during the review process. <br>Max length: 4096 |
| additionalOptions   object | Workflow-level settings that control whether the initiator can modify certain fields when starting a review. |
| allowInitiatorToEdit   boolean | (`Allow Initiators to edit the review` in the UI). Indicates whether the initiator can adjust reviewer assignments and step durations. <br>`true`: the initiator can change reviewer assignments and durations.<br>`false`: (default) reviewers and durations are fixed. |
| id   string: UUID | The unique identifier of the approval workflow returned in the response. This ID can be used in subsequent API calls to reference this workflow. |
| status   enum:string | The current status of the approval workflow. Possible values: <br>`ACTIVE`: the workflow is active and available for use.<br>`INACTIVE`: the workflow has been deactivated and cannot be used to create new reviews. |
| approvalStatusOptions   array: object | A list of approval status options defined for this workflow. It includes two built-in options by default (typically `APPROVED` and `REJECTED`), and may also include custom statuses added by the user. |
| label   string | The display name shown in the UI. It m ust be unique across all status options (built-in and custom). <br>Maximum length: 255 characters.<br>Max length: 255 |
| value   enum:string | The value representing the approval outcome. Possible values: `APPROVED`, `REJECTED`. |
| id   string: UUID | The unique identifier of this approval status entry in the workflow. |
| builtIn   boolean | Indicates whether the approval status is a built-in option. <br>`true`: the status is built in (e.g., `APPROVED`, `REJECTED`).<br>`false`: the status is a custom option created by a user. |
| steps   array: object | A list of steps defined in the approval workflow. Each step defines who reviews the files, how long they have, and whether it involves multiple reviewers. |
| name   string | The name of the step, as defined in the workflow. It appears in the UI and is used in workflow configuration. Maximum length: 255 characters. <br>Max length: 255 |
| type   enum:string | Indicates the step type in the workflow. Possible values: <br>`INITIATOR`: the first step. It typically represents the person who launches the review.`REVIEWER`: an intermediate step. It allows one or more reviewers to evaluate the files.`APPROVER`: the final step. It represents the decision maker who approves or rejects the files. |
| duration   int | (`Time allowed` in the UI) The number of days allocated to complete this step. <br>This field applies only to `REVIEWER` and `APPROVER` steps. It is used to calculate the due date based on the selected `dueDateType`.<br>Valid range: `1â99`. |
| dueDateType   enum:string | Specifies how the due date is calculated for this step. It works together with duration. <br>This field applies only to `REVIEWER` and `APPROVER` steps.<br>Possible values:<br>`CALENDAR_DAY` (default): the due date includes all calendar days, including weekends and holidays.`WORKDAY`: the due date excludes weekends and project holidays. |
| groupReview   object | (`Reviewer Type` in the UI) Defines whether multiple reviewers can participate in this step and how their responses are handled. It applies only to `REVIEWER` steps. |
| enabled   boolean | Indicates whether group review is enabled for this step. <br>`true`: multiple reviewers can participate in the step.<br>`false`: (default) only a single reviewer is allowed. |
| type   enum:string | (Displayed under `More options` in the UI) Specifies the group review rule for this step. <br>Possible values:<br>`ALL`: every reviewer assigned to the step must submit a response (up to 30).`MINIMUM`: only a specified number of reviewers must respond, as defined in `min`. |
| min   int | The minimum number of reviewers required for this step. This field is set automatically when the group review type is set to `MINIMUM`. It is not independently configurable. Valid range: `1â30`. |
| id   string | The ID of the step. |
| candidates   object | (Displayed in the UI when selecting reviewers for a step) Lists the users, roles, or companies that were configured as reviewers for this step. <br>These candidates are defined during workflow setup and determine who will be invited to participate in the step during a review. |
| roles   array: object | A list of project roles assigned as candidates for this step. |
| autodeskId   string | The Autodesk ID of the role. |
| name   string | The name of the role. |
| users   array: object | A list of individual users assigned as candidates for this step. |
| autodeskId   string | The Autodesk ID of the user. |
| name   string | The name of the user. |
| companies   array: object | A list of companies assigned as candidates for this step. |
| autodeskId   string | The Autodesk ID of the company. |
| name   string | The name of the company. |
| copyFilesOptions   object | (`Copy approved files` in the UI) The configuration for copying approved files to a target folder when the review is complete. |
| enabled   boolean | Indicates whether approved files should be copied to a target folder after the review is complete. <br>`true`: copy approved files to the target folder.<br>`false`: do not copy approved files. |
| allowOverride   boolean | (`Allow the initiator to change the target folder` in the UI) Allows the initiator to change the target folder when creating a review. <br>`true`: the initiator can choose a different target folder.<br>`false`: the folder defined in the workflow is used. |
| condition   string | (`All/Any files in the review have been approved` in the UI) Specifies the condition under which approved files will be copied. <br>Possible values:<br>`ANY`: copy files if at least one file in the review is approved.<br>`ALL`: copy files only if all files in the review are approved. |
| folderUrn   string | (`Then copy approved files to` in the UI) The URN of the target folder where approved files will be copied. |
| includeMarkups   boolean | (`Include all published markups on approved files` in the UI) Indicates whether published markups should be included when copying files. <br>`true`: include all published (unarchived) markups from the source version.<br>`false`: (default) do not include markups. |
| disableOverrideMarkupSetting   boolean | (`Allow approvers to change whether or not markups are included` in the UI) Controls whether approvers or admins can change the markup inclusion setting when starting the review. <br>`true`: the markup setting is locked and cannot be changed.<br>`false`: the setting can be changed during review setup. |
| attachedAttributes   array: object | (`Update Attributes` in the UI) The list of attributes added in the `Update Attributes` action. <br>These attributes will be applied to the approved files in the target folder, or optionally also in the source folder depending on the configuration. |
| id   int | The ID of the custom attribute to be applied after review completion. |
| required   boolean | (`Attribute â Required by approver` in the UI) Indicates whether the approver must enter a value for this attribute to submit the review. <br>`true`: the attribute is required.<br>`false`: (default) the attribute is optional. |
| updateAttributesOptions   object | The configuration for applying attribute updates when a review is completed. This applies only if the workflow includes a file copy action and the `Update Attributes` action is enabled. |
| enableAttachedAttributes   boolean | (`Update attributes` in the UI) Indicates whether the `Update Attributes` action is enabled. <br>`true`: attributes will be applied after the review.<br>`false`: (default) attributes will not be updated. |
| updateSourceAndCopiedFiles   boolean | (`Update attributes both for target folder and source folder` or `Update attributes only for target folder` in the UI) Determines whether attributes are updated only for files in the target folder, or for both the target and source folders. <br>`true`: update attributes in both folders.<br>`false`: (default) update only the target folder.<br>Only available when the approval workflow includes a copy post-action. |
| createdAt   datetime: ISO 8601 | The date and time when the workflow was created. |
| updatedAt   datetime: ISO 8601 | The date and time when the workflow was last updated. |

## [Example](#example)

The workflow was created successfully.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/reviews/v1/projects/563a4c30-e30d-4869-ac02-2a18b6447abe/workflows' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "Final Structural Review",
        "description": "Used to review structural plans before finalizing IFC drawings.",
        "notes": "Please check all rebar annotations before approving. Include markup if changes are required.",
        "additionalOptions": {
          "allowInitiatorToEdit": true
        },
        "additionalApprovalStatusOptions": [
          {
            "label": "Approved w/ comments",
            "value": "APPROVED"
          }
        ],
        "copyFilesOptions": {
          "enabled": true,
          "allowOverride": false,
          "condition": "ANY",
          "folderUrn": "urn:adsk.wipprod:fs.folder:co.CplBAmvXRWGqsvN1Nabvd2",
          "includeMarkups": false,
          "disableOverrideMarkupSetting": false
        },
        "steps": [
          {
            "name": "Reviewer",
            "type": "REVIEWER",
            "duration": 3,
            "dueDateType": "CALENDAR_DAY",
            "groupReview": {
              "enabled": true,
              "type": "MINIMUM",
              "min": 3
            },
            "candidates": {
              "users": [
                {
                  "autodeskId": "HWUBNU689CRU"
                }
              ],
              "roles": [
                {
                  "autodeskId": "1473817"
                }
              ],
              "companies": [
                {
                  "autodeskId": "26980302"
                }
              ]
            }
          }
        ]
      }'

```

Show More

### Response

```
{
  "name": "Final Structural Review",
  "description": "Used to review structural plans before finalizing IFC drawings.",
  "notes": "Please check all rebar annotations before approving. Include markup if changes are required.",
  "additionalOptions": {
    "allowInitiatorToEdit": true
  },
  "id": "4e609369-e950-4097-b7d3-e6cf1c3c5415",
  "status": "ACTIVE",
  "approvalStatusOptions": [
    {
      "label": "Approved w/ comments",
      "value": "APPROVED",
      "id": "b2a3c3b7-4fef-40a4-868b-981b23e7182f",
      "builtIn": false
    }
  ],
  "steps": [
    {
      "name": "Reviewer",
      "type": "REVIEWER",
      "duration": 3,
      "dueDateType": "CALENDAR_DAY",
      "groupReview": {
        "enabled": true,
        "type": "MINIMUM",
        "min": 3
      },
      "id": "Lane_uJtTI3vjaF",
      "candidates": {
        "roles": [
          {
            "autodeskId": "1473817",
            "name": "Architect"
          }
        ],
        "users": [
          {
            "autodeskId": "HWUBNU689CRU",
            "name": "James Smith"
          }
        ],
        "companies": [
          {
            "autodeskId": "26980302",
            "name": "Autodesk Co. Ltd."
          }
        ]
      }
    }
  ],
  "copyFilesOptions": {
    "enabled": true,
    "allowOverride": false,
    "condition": "ANY",
    "folderUrn": "urn:adsk.wipprod:fs.folder:co.CplBAmvXRWGqsvN1Nabvd2",
    "includeMarkups": false,
    "disableOverrideMarkupSetting": false
  },
  "attachedAttributes": [
    {
      "id": 1001,
      "required": false
    }
  ],
  "updateAttributesOptions": {
    "enableAttachedAttributes": false,
    "updateSourceAndCopiedFiles": false
  },
  "createdAt": "2024-07-07T09:21:17.577Z",
  "updatedAt": "2025-01-07T08:43:10.189Z"
}

```

Show More
