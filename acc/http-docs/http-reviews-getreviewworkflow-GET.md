# projects/{projectId}/reviews/{reviewId}/workflow

Source: https://aps.autodesk.com/en/docs/acc/reference/http/reviews-getreviewworkflow-GET/

---

Get the Workflow For This Review

GET

# projects/{projectId}/reviews/{reviewId}/workflow

Retrieves the approval workflow associated with a specific review.

This endpoint provides the exact workflow structure used when the review was created, including its steps, candidates, approval status options, and post-review actions.

To retrieve all workflows defined in a project (not just for one review), call [GET workflows](http-reviews-workflows-GET.md).

For more details about reviews, see the [Help documentation](https://help.autodesk.com/view/DOCS/ENU/?guid=Reviews).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/reviews/v1/projects/{projectId}/reviews/{reviewId}/workflow |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring: UUID The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You can provide the project ID with or without the â**b.**" prefix.

- Example with prefix: **b.563a4c30-e30d-4869-ac02-2a18b6447abe**
- Example without prefix: **563a4c30-e30d-4869-ac02-2a18b6447abe**
- reviewIdstring: UUID The unique ID of the review.
It must be in UUID format â not the numeric sequence ID shown in the Reviews UI. To find the review ID, call [GET reviews](en/docs/acc/v1/reference/http/reviews-reviews-GET/).

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the requested review workflow data |
| --- | --- |
| 400   Bad Request | Bad request. The input parameters were invalid. |
| 403   Forbidden | Forbidden. The user does not have permission to access this resource. |
| 404   Not Found | Not found. The resource does not exist or is inaccessible. |
| 500   Internal Server Error | An unexpected server error occurred. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| name   string | The name of the workflow. It must be unique within the project. <br>Max length: 255 |
| --- | --- |
| description   string | A description of the workflow. <br>Max length: 4096 |
| notes   string | A custom note associated with the workflow. Visible to all reviewers during the review process. <br>Max length: 4096 |
| additionalOptions   object | Workflow-level settings that control whether the initiator can modify certain fields when starting a review. |
| allowInitiatorToEdit   boolean | (`Allow Initiators to edit the review` in the UI). Indicates whether the initiator can adjust reviewer assignments and step durations. <br>`true`: the initiator can change reviewer assignments and durations.<br>`false`: (default) reviewers and durations are fixed. |
| id   string: UUID | The ID of the workflow. |
| approvalStatusOptions   array: object | A list of file review status options to the workflow, which contains two built in options returned by the system. |
| label   string | The display name shown in the UI. It m ust be unique across all status options (built-in and custom). <br>Maximum length: 255 characters.<br>Max length: 255 |
| value   enum:string | The value representing the approval outcome. Possible values: `APPROVED`, `REJECTED`. |
| id   string: UUID | The unique identifier of this approval status entry in the workflow. |
| builtIn   boolean | Indicates whether the approval status is a built-in option. <br>`true`: the status is built in (e.g., `APPROVED`, `REJECTED`).<br>`false`: the status is a custom option created by a user. |
| steps   array: object | A list of steps specify the details for each step in the workflow. |
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

## [Example](#example)

Successfully retrieved the requested review workflow data

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/reviews/v1/projects/563a4c30-e30d-4869-ac02-2a18b6447abe/reviews/73c8b3ec-eea2-4240-9c69-f9563e2fec0c/workflow' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "name": "Final Structural Review",
  "description": "Used to review structural plans before finalizing IFC drawings.",
  "notes": "Please check all rebar annotations before approving. Include markup if changes are required.",
  "additionalOptions": {
    "allowInitiatorToEdit": true
  },
  "id": "dab28823-7ecc-47b4-a92a-37540d777751",
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
  }
}

```

Show More
