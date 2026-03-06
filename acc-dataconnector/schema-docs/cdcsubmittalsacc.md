# cdcsubmittalsacc Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=cdcsubmittalsacc&format=html

---

# cdcsubmittalsacc Schema Description

**Documentation Updated:** 2025-12-19  

- [attachments](#attachments)
- [comments](#comments)
- [custom_identifier_settings](#custom_identifier_settings)
- [item_custom_attribute_value](#item_custom_attribute_value)
- [item_revision](#item_revision)
- [item_watchers](#item_watchers)
- [items](#items)
- [itemtype](#itemtype)
- [packages](#packages)
- [parameters_collections](#parameters_collections)
- [specs](#specs)
- [steps](#steps)
- [tasks](#tasks)

**Beta Release**  
This is a Beta release of the cdcsubmittalsacc data set and schema definitions are subject to change or even possibly be removed from the final data set release. Thank you for your understanding with any future schema updates.

## attachments

Attachments for ACC Build Submittal items. - This is the Change Data Capture (CDC) enabled version of the submittalsacc.attachments table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID for the Attachment |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | item_id | string: UUID |  | The ID for the parent Item Foreign Key: Table: items Column: id |
| 5 | name | string |  | Name of the file |
| 6 | revision | number |  | Revision of the item when the attachment was added |
| 7 | created_by | string |  | Autodesk User ID of the user that created the attachment |
| 8 | created_at | timestamp: SQL |  | Date and time when the attachment created Column used for filtering Date Range Extraction requests |
| 9 | updated_at | timestamp: SQL |  | Date and time when the attachment last updated Column used for filtering Date Range Extraction requests |
| 10 | updated_by | string |  | Autodesk User ID of the user that last updated the attachment |
| 11 | upload_urn | string |  | storage URN where attachments are uploaded |
| 12 | category_id | string |  | ID of the attachment category |
| 13 | category_value | string |  | value of the category_id |
| 14 | task_id | string: UUID |  | The ID for the parent Task Foreign Key: Table: tasks.id Column: |
| 15 | is_file_uploaded | boolean |  | Was the upload process completed successfully |
| 16 | urn | string |  | ID of the version of the file |
| 17 | deleted_at | timestamp: SQL |  | Timestamp when the attachment was deleted Column used for filtering Date Range Extraction requests |
| 18 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## comments

Comments for ACC Build Submittal items. - This is the Change Data Capture (CDC) enabled version of the submittalsacc.comments table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID for the Comment |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | item_id | string: UUID |  | The ID for the parent Item Foreign Key: Table: items Column: id |
| 5 | updated_by | string |  | Autodesk User ID of the user that last updated the comment |
| 6 | updated_at | timestamp: SQL |  | Date and time when the comment updated Column used for filtering Date Range Extraction requests |
| 7 | created_by | string |  | Autodesk User ID of the user that created the comment |
| 8 | created_at | timestamp: SQL |  | Date and time when the comment was created Column used for filtering Date Range Extraction requests |
| 9 | body | string |  | Body of the comment |
| 10 | deleted_at | timestamp: SQL |  | Timestamp when the comment was deleted Column used for filtering Date Range Extraction requests |
| 11 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## custom_identifier_settings

Submittal custom identifier settings for the ACC Build system. - This is the Change Data Capture (CDC) enabled version of the submittalsacc.custom_identifier_settings table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID for the custom identifier settings |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | updated_by | string |  | Autodesk User ID of the user that last updated the task |
| 5 | updated_at | timestamp: SQL |  | Date and time when the task was updated Column used for filtering Date Range Extraction requests |
| 6 | can_switch_type | boolean |  | Defaults to 'True', after one usage the value will be set to 'False' permanently. |
| 7 | sequence_type | enum: string | Possible Values: 1 - global 2 - spec | Project current sequence type |
| 8 | created_at | timestamp: SQL |  | Timestamp when the custom_identifier_setting was created Column used for filtering Date Range Extraction requests |
| 9 | deleted_at | timestamp: SQL |  | Timestamp when the custom_identifier_setting was deleted Column used for filtering Date Range Extraction requests |
| 10 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## item_custom_attribute_value

Custom fields values for ACC Build Submittal items.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID for the task |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | item_id | string: UUID |  | Foreign Key: Table: items.id (The ID for the parent item) Column: |
| 5 | parameter_id | string: UUID |  | Foreign Key: Table: parameters.id (The ID for related parameter) Column: |
| 6 | parameter_name | string |  | The name of related parameter. |
| 7 | parameter_type | string |  | The type of related parameter. |
| 8 | value | string |  | The value of item custom field. Value is saved as string, actual value type is based on related parameter type |
| 9 | created_at | timestamp: SQL |  | Date and time when the custom attribute value was added Column used for filtering Date Range Extraction requests |
| 10 | created_by | string |  | Autodesk User ID of the user that added the custom attribute value |
| 11 | updated_at | timestamp: SQL |  | Date and time when the custom attribute value updated Column used for filtering Date Range Extraction requests |
| 12 | updated_by | string |  | Autodesk User ID of the user that last updated the custom attribute value |
| 13 | deleted_at | timestamp: SQL |  | Date and time when the custom attribute value got deleted Column used for filtering Date Range Extraction requests |
| 14 | select_value | string |  | Display field for single / multi select parameter type values. |
| 15 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## item_revision

Submittal item revision for the ACC Build system. - This is the Change Data Capture (CDC) enabled version of the submittalsacc.item_revision table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | id | string: UUID |  | The ID for the Submittal revision. |
| 4 | item_id | string: UUID |  | The ID of related Submittal. |
| 5 | manager | string |  | Autodesk User ID / Role member group ID / Company member group ID of the manager |
| 6 | manager_type | enum: string | Possible Values: 1 - user 2 - company 3 - role | Indication for manager id type |
| 7 | subcontractor | string |  | Autodesk User ID / Role member group ID / Company member group ID of the subcontractor |
| 8 | subcontractor_type | enum: string | Possible Values: 1 - user 2 - company 3 - role | Indication for subcontractor id type |
| 9 | revision | number |  | Revision of the item |
| 10 | created_at | timestamp: SQL |  | when was the item created Column used for filtering Date Range Extraction requests |
| 11 | updated_at | timestamp: SQL |  | last time the item was updated Column used for filtering Date Range Extraction requests |
| 12 | sent_to_submitter | timestamp: SQL |  | when the submitter received the item |
| 13 | submitter_due_date | date: string |  | When the responsible contractor submission is due |
| 14 | received_from_submitter | timestamp: SQL |  | When the submitter moved the item forward |
| 15 | submitted_by | string |  | Autodesk User ID of the user that submitted the item to the manager |
| 16 | sent_to_review | timestamp: SQL |  | When the first review step started Schema Change: formerly sent_to_reviewer (now we have multiple reviewers) |
| 17 | manager_due_date | date: string |  | When the manager review is due |
| 18 | sent_to_review_by | string |  | Autodesk User ID of the user that submitted the item to review |
| 19 | received_from_review | timestamp: SQL |  | When the review finished Schema Change: formerly received_from_reviewer |
| 20 | response_id | string |  | ID of the response, if was added. Foreign Key: Table: response Column: id |
| 21 | response_comment | string |  | Response comment of the item (in addition to response id) |
| 22 | responded_at | timestamp: SQL |  | Date and time when response was added |
| 23 | responded_by | string |  | Autodesk User ID of the user that responded |
| 24 | published_date | timestamp: SQL |  | When the item was closed and distributed |
| 25 | published_by | string |  | Autodesk User ID of the user that published the item |
| 26 | deleted_at | timestamp: SQL |  | Timestamp when the item_revision was deleted Column used for filtering Date Range Extraction requests |
| 27 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## item_watchers

List of Autodesk User IDs of distribution_list users and their type - This is the Change Data Capture (CDC) enabled version of the submittalsacc.item_watchers table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | item_id | string: UUID |  | ID for the Item Foreign Key: Table: items Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | user_id | string |  | Autodesk User IDs of cc'ed user/role/company |
| 5 | user_type_id | string | Possible Values: 1 - user 2 - company 3 - role | if of the distribution_list member user_type (user/role/company) |
| 6 | user_type_value | string |  | value of the user_type_id |
| 7 | created_at | timestamp: SQL |  | Timestamp when the item_watcher was created Column used for filtering Date Range Extraction requests |
| 8 | updated_at | timestamp: SQL |  | Timestamp when the item_watcher was updated Column used for filtering Date Range Extraction requests |
| 9 | deleted_at | timestamp: SQL |  | Timestamp when the item_watcher was deleted Column used for filtering Date Range Extraction requests |
| 10 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## items

Submittal items for the ACC Build system. - This is the Change Data Capture (CDC) enabled version of the submittalsacc.items table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID for the Submittal. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | spec_id | string: UUID |  | ID for the associated Spec Foreign Key: Table: specs Column: id |
| 5 | spec_identifier | string |  | Identifier of the spec this item related to |
| 6 | title | string |  | Title (name) of the item |
| 7 | type_id | string |  | ID for the item type Foreign Key: Table: item type Column: id |
| 8 | type_value | string |  | value of the item type_id |
| 9 | response_comment | string |  | Response comment of the item (in addition to response id) |
| 10 | ball_in_court | string |  | Array of Autodesk User IDs of the users that are ball in court for the item workflow Schema Change: formerly assigned_to (now we have multiple reviewers) Schema Change: Deprecated field |
| 11 | revision | number |  | Revision of the item |
| 12 | responded_by | string |  | Autodesk User ID of the user that responded |
| 13 | description | string |  | Description of the item |
| 14 | responded_at | timestamp: SQL |  | Date and time when response was added |
| 15 | due_date | date: string |  | Date and time for the item to be done with current state |
| 16 | required_on_job_date | date: string |  | Date and time for the item to be done on site |
| 17 | manager | string |  | Autodesk User ID / Role member group ID / Company member group ID of the manager |
| 18 | created_by | string |  | Autodesk User ID of the user that created the item |
| 19 | created_at | timestamp: SQL |  | when was the item created Column used for filtering Date Range Extraction requests |
| 20 | state_id | string |  | State of the item |
| 21 | response_id | string |  | ID of the response, if was added. Foreign Key: Table: response Column: id |
| 22 | response_value | string |  | value of the response_id |
| 23 | subsection | string |  | Sub spec section |
| 24 | subcontractor | string |  | Autodesk User ID / Role member group ID / Company member group ID of the subcontractor |
| 25 | identifier | number |  | Identifier of the item. Created automatically |
| 26 | updated_by | string |  | Autodesk User ID of the user the last updated the item |
| 27 | updated_at | timestamp: SQL |  | last time the item was updated Column used for filtering Date Range Extraction requests |
| 28 | status_id | enum: string | Possible Values: 1 - Required 2 - Open 3 - Closed 4 - Void 5 - Empty 6 - Draft | Status ID |
| 29 | status_value | string |  | value of the status_id |
| 30 | package_title | string |  | Title of the package the item is related to (if any) |
| 31 | package | string: UUID |  | ID for the associated Package Foreign Key: Table: packages.id Column: |
| 32 | package_identifier | number |  | Identifier of the package the item is related to (if any) |
| 33 | priority_id | number | Possible Values: 1 - Low 2- Normal 3 - High | id of the priority the item is related to (if any) |
| 34 | priority_value | string |  | value of the priority_id |
| 35 | required_date | date: string |  | item's required date |
| 36 | required_approval_date | date: string |  | item's required approval date |
| 37 | lead_time | number |  | item's lead time |
| 38 | sent_to_submitter | timestamp: SQL |  | when the submitter received the item |
| 39 | received_from_submitter | timestamp: SQL |  | When the submitter moved the item forward |
| 40 | submitted_by | string |  | Autodesk User ID of the user that submitted the item to the manager |
| 41 | sent_to_review | timestamp: SQL |  | When the first review step started Schema Change: formerly sent_to_reviewer (now we have multiple reviewers) |
| 42 | sent_to_review_by | string |  | Autodesk User ID of the user that submitted the item to review |
| 43 | received_from_review | timestamp: SQL |  | When the review finished Schema Change: formerly received_from_reviewer |
| 44 | published_date | timestamp: SQL |  | When the item was closed and distributed |
| 45 | published_by | string |  | Autodesk User ID of the user that published the item |
| 46 | submitter_due_date | date: string |  | When the responsible contractor submission is due |
| 47 | manager_due_date | date: string |  | When the manager review is due |
| 48 | ball_in_court_users | string |  | Array of Autodesk User IDs of the users that are ball in court for the item workflow |
| 49 | ball_in_court_roles | string |  | Array of Role member group IDs of the roles that are ball in court for the item workflow |
| 50 | ball_in_court_companies | string |  | Array of Company member group IDs of the companies that are ball in court for the item workflow |
| 51 | manager_type | enum: string | Possible Values: 1 - user 2 - company 3 - role | Indication for manager id type |
| 52 | subcontractor_type | enum: string | Possible Values: 1 - user 2 - company 3 - role | Indication for subcontractor id type |
| 53 | custom_identifier | string |  | The custom identifier of the item. |
| 54 | custom_identifier_sort | string |  | Same value as 'custom_identifier' but this column has db collation in order to enable sorting by the custom identifier value. |
| 55 | custom_identifier_human_readable | string |  | Ingested custom identifier of the item. May include the item spec identifier along with the custom identifier value. |
| 56 | deleted_at | timestamp: SQL |  | Timestamp when the item was deleted Column used for filtering Date Range Extraction requests |
| 57 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |
| 58 | pending_actions_from | string |  | Array of Autodesk User, Roles and Companies that have yet to respond |

## itemtype

Submittal types for ACC Build Submittal items. - This is the Change Data Capture (CDC) enabled version of the submittalsacc.itemtype table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID for the type |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | created_at | timestamp: SQL |  | Date and time when the typye created Column used for filtering Date Range Extraction requests |
| 5 | updated_by | string |  | Autodesk User ID of the user that last updated the typye |
| 6 | updated_at | timestamp: SQL |  | Date and time when the type last updated Column used for filtering Date Range Extraction requests |
| 7 | created_by | string |  | Autodesk User ID of the user that created the type |
| 8 | value | string |  | Value of the type |
| 9 | platform_id | string |  | For default types |
| 10 | is_active | boolean |  | Is the type active |
| 11 | deleted_at | timestamp: SQL |  | Timestamp when the itemtype was deleted Column used for filtering Date Range Extraction requests |
| 12 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## packages

Submittal Packages for the ACC Build system. - This is the Change Data Capture (CDC) enabled version of the submittalsacc.packages table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID for the Package |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | spec_id | string: UUID |  | ID for the associated Spec Foreign Key: Table: specs Column: id |
| 5 | title | string |  | Title of the package |
| 6 | identifier | number |  | Identifier of the package. Created Automatically |
| 7 | description | string |  | Description for the package |
| 8 | updated_by | string |  | Autodesk User ID of the user that last updated the package |
| 9 | created_at | timestamp: SQL |  | Date and time when the spec was created Column used for filtering Date Range Extraction requests |
| 10 | created_by | string |  | Autodesk User ID of the user that created the package |
| 11 | updated_at | timestamp: SQL |  | Date and time when spec was last updated Column used for filtering Date Range Extraction requests |
| 12 | spec_identifier | string |  | Identifier of the spec this package related to |
| 13 | deleted_at | timestamp: SQL |  | Timestamp when the package was deleted Column used for filtering Date Range Extraction requests |
| 14 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## parameters_collections

Project custom fields of ACC Build Submittals.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID for the task |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | parameter_id | string: UUID |  | Foreign Key: Table: parameters.id (The ID for related parameter) Column: |
| 5 | parameter_external_id | string |  | The external_id of related parameter. |
| 6 | parameter_name | string |  | The name of related parameter. |
| 7 | parameter_description | string |  | The description of related parameter. |
| 8 | parameter_type | string |  | The type of related parameter. |
| 9 | created_at | timestamp: SQL |  | Date and time when the parameter was detached from collection Column used for filtering Date Range Extraction requests |
| 10 | created_by | string |  | Autodesk User ID of the user that detached that parameter |
| 11 | updated_at | timestamp: SQL |  | Date and time when the parameter was attached/detached to/from collection Column used for filtering Date Range Extraction requests |
| 12 | updated_by | string |  | Autodesk User ID of the user that last updated the parameter for collection |
| 13 | deleted_at | timestamp: SQL |  | Date and time when the parameter was attached/detached to/from collection Column used for filtering Date Range Extraction requests |
| 14 | parameter_select_options | string |  | Available select options for single / multi select parameter type. |
| 15 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## specs

Submittal Spec Sections for the ACC Build system. - This is the Change Data Capture (CDC) enabled version of the submittalsacc.specs table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | id | string: UUID |  | ID for the Spec Section |
| 4 | identifier | string |  | Spec identifier. Created by the user |
| 5 | title | string |  | Title of the spec |
| 6 | created_at | timestamp: SQL |  | Date and time when the spec was created Column used for filtering Date Range Extraction requests |
| 7 | created_by | string |  | Autodesk User ID of the user that created the spec |
| 8 | updated_at | timestamp: SQL |  | Date and time when the spec was updated Column used for filtering Date Range Extraction requests |
| 9 | updated_by | string |  | Autodesk User ID of the user that last updated the spec |
| 10 | deleted_at | timestamp: SQL |  | Timestamp when the spec was deleted Column used for filtering Date Range Extraction requests |
| 11 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## steps

Review steps for ACC Build Submittal items. - This is the Change Data Capture (CDC) enabled version of the submittalsacc.steps table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID for the step |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | updated_by | string |  | Autodesk User ID of the user that last updated the step |
| 5 | updated_at | timestamp: SQL |  | Date and time when the step was updated Column used for filtering Date Range Extraction requests |
| 6 | created_by | string |  | Autodesk User ID of the user that created the step |
| 7 | created_at | timestamp: SQL |  | Date and time when the step was created Column used for filtering Date Range Extraction requests |
| 8 | status | enum: string | Possible Values: not-started / in-progress / completed | The status of the step |
| 9 | step_number | number |  | The order of the step in the review workflow |
| 10 | days_to_respond | number |  | Number of days that the reviewers have to respond |
| 11 | due_date | date: string |  | Date for the item to be done with current state |
| 12 | started_at | timestamp: SQL |  | Date and time when the step started |
| 13 | completed_at | timestamp: SQL |  | Date and time when the step finished |
| 14 | item_id | string: UUID |  | The ID for the parent Item Foreign Key: Table: items Column: id |
| 15 | deleted_at | timestamp: SQL |  | Timestamp when the step was deleted Column used for filtering Date Range Extraction requests |
| 16 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## tasks

Review tasks for ACC Build Submittal items. - This is the Change Data Capture (CDC) enabled version of the submittalsacc.tasks table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID for the task |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | updated_by | string |  | Autodesk User ID of the user that last updated the task |
| 5 | updated_at | timestamp: SQL |  | Date and time when the task was updated Column used for filtering Date Range Extraction requests |
| 6 | created_by | string |  | Autodesk User ID of the user that created the task |
| 7 | created_at | timestamp: SQL |  | Date and time when the task was created Column used for filtering Date Range Extraction requests |
| 8 | status | enum: string | Possible Values: not-started / in-progress / completed | The status of the task |
| 9 | assigned_to | string |  | Autodesk User ID / Role member group ID / Company member group ID that the task is assigned to |
| 10 | is_required | boolean |  | Is the task a required task in the review step |
| 11 | response_comment | string |  | Response comment of the task (in addition to response id) |
| 12 | responded_at | timestamp: SQL |  | Date and time when response was added |
| 13 | responded_by | string |  | Autodesk User ID of the user that responded |
| 14 | started_at | timestamp: SQL |  | Date and time when the task started |
| 15 | completed_at | timestamp: SQL |  | Date and time when the task finished |
| 16 | completed_by | string |  | Autodesk User ID of the user that closed the task |
| 17 | response_value | string |  | value of the response_id |
| 18 | response_id | string: UUID |  | ID of the response, if was added. Foreign Key: Table: response.id Column: |
| 19 | step_id | string: UUID |  | ID of the parent step Foreign Key: Table: steps.id Column: |
| 20 | assigned_to_type | enum: string | Possible Values: 1 - user 2 - company 3 - role | Indication for assigned_to id type |
| 21 | deleted_at | timestamp: SQL |  | Timestamp when the task was deleted Column used for filtering Date Range Extraction requests |
| 22 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

© Copyright 2026 Autodesk Inc. | [Autodesk Construction Cloud](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
