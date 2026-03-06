# rfis Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=rfis&format=html

---

# rfis Schema Description

**Documentation Updated:** 2025-01-29  

- [acc_attachments](#acc_attachments)
- [attachments](#attachments)
- [category](#category)
- [comments](#comments)
- [discipline](#discipline)
- [project_custom_attributes](#project_custom_attributes)
- [project_custom_attributes_enums](#project_custom_attributes_enums)
- [rfi_assignees](#rfi_assignees)
- [rfi_co_reviewers](#rfi_co_reviewers)
- [rfi_custom_attributes](#rfi_custom_attributes)
- [rfi_distribution_list](#rfi_distribution_list)
- [rfi_location](#rfi_location)
- [rfi_responses](#rfi_responses)
- [rfi_reviewers](#rfi_reviewers)
- [rfi_transitions](#rfi_transitions)
- [rfi_types](#rfi_types)
- [rfis](#rfis)

## acc_attachments

The attachments associated with ACC RFIs

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID for the acc attachment |
| 2 | rfi_id | string: UUID |  | Foreign Key: Table: rfis.id The ID for the RFI Column: |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 5 | entity_id | string: UUID |  | The entity ID the attachment associated with |
| 6 | entity_type | enum: string | Possible Values: rfiResponse rfiOfficialResponse | The entity type the attachment associated with |
| 7 | display_name | string |  | The name of the attachment |
| 8 | created_at | timestamp: SQL |  | The timestamp of the date and time the attachment was created |
| 9 | created_by | string |  | The Autodesk User ID of the user who created the attachment. |
| 10 | deleted_at | timestamp: SQL |  | The timestamp of the date and time the attachment was deleted. This is only relevant for deleted attachments. |
| 11 | deleted_by | string |  | The Autodesk User ID of the user who deleted the attachment. This is only relevant for deleted attachments. |

## attachments

The attachments associated with BIM 360 Project Management RFIs.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | rfi_id | string: UUID |  | The ID for the RFI. Foreign Key: Table: rfis Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 4 | id | string: UUID |  | The ID of the attachment. |
| 5 | created_at | timestamp: SQL |  | The timestamp of the date and time the attachment was created |
| 6 | created_by | string |  | The Autodesk User ID of the user who created the attachment. |
| 7 | updated_at | timestamp: SQL |  | The last time the attachment attributes were updated |
| 8 | deleted_at | timestamp: SQL |  | The timestamp of the date and time the attachment was deleted This is only relevant for deleted attachments. |
| 9 | deleted_by | string |  | The Autodek User ID of the user who deleted the attachment. This is only relevant for deleted attachments. |
| 10 | name | string |  | The name of the attachment. |

## category

Alternative reviewers for RFIs

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | rfi_id | string: UUID |  | ID for the RFI. Foreign Key: Table: rfis Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 4 | category | string |  | The category to associate with this RFI |

## comments

Comments associated with BIM 360 Project Management RFIs.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | rfi_id | string: UUID |  | The ID for the RFI. Foreign Key: Table: rfis Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 4 | id | string: UUID |  | The ID of the comment. |
| 5 | created_at | timestamp: SQL |  | The timestamp of the date and time the comment was created. |
| 6 | created_by | string |  | The Autodesk User ID of the user who created the comment. |
| 7 | updated_at | timestamp: SQL |  | The last time the comment attributes were updated. |
| 8 | body | string |  | The content of the comment |

## discipline

Alternative reviewers for RFIs

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | rfi_id | string: UUID |  | ID for the RFI. Foreign Key: Table: rfis Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 4 | discipline | string |  | The discipline to associate with this RFI |

## project_custom_attributes

The Custom Attributes per project

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID of the Project Custom Attributes |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 4 | name | string |  | The name of the Custom Attribute |
| 5 | type | enum: string | Possible Values: text numeric | The type of the Custom Attribute |
| 6 | description | string |  | Description of the Custom Attribute |
| 7 | multiple_choice | boolean |  | When the value is NULL then the field is not selectable. When the value is false it is a single select. When the value is TRUE then the value is multi select. |
| 8 | status | enum: string | Possible Values: active inactive hidden | Active: default status when the Custom Attribute is active. Inactive: when the Custom Attribute is not active(reversible). Hidden - when the Custom Attribute is soft deleted(not reversible) |

## project_custom_attributes_enums

The Custom Attributes Enums options for the selectable Custom Attributes per container

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID of the Project Custom Attributes Enums |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 4 | custom_attribute_id | string: UUID |  | The Custom Attribute ID which has the selectable value |
| 5 | name | string |  | The value of the enum |

## rfi_assignees

The assignees associated with the RFIs.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID of the assignee. |
| 2 | rfi_id | string: UUID |  | The ID for the RFI. Foreign Key: Table: rfis Column: id |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 5 | oxygen_id | string |  | The Autodesk User ID of the user assignee. |
| 6 | type | enum: string | Possible Values: user | The assignee type |
| 7 | created_at | timestamp: SQL |  | The timestamp of the date and time of the assignee assigment |
| 8 | updated_at | timestamp: SQL |  | The last time the assignee attributes were updated |
| 9 | deleted_at | timestamp: SQL |  | The timestamp of the date and time the assignee was deleted This is only relevant for deleted assignee. |

## rfi_co_reviewers

Alternative reviewers for RFIs

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | rfi_id | string: UUID |  | ID for the RFI. Foreign Key: Table: rfis Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 4 | user_id | string |  | The Autodesk User ID of the alternate reviewer |

## rfi_custom_attributes

The table that indicates which custom attribute value related to a specific RFI

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID of the Rfi Custom Attribute |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 4 | rfi_id | string: UUID |  | The ID for the RFI |
| 5 | custom_attribute_id | string: UUID |  | The Custom Attribute ID which the value was set for |
| 6 | value_enum_id | string: UUID |  | If the custom attribute is selectable (not free text/numbers) then the value will be a UUID in container_custom_attributes_enums which is the selected value. If the Custom Attribute is multi select and more then one selected then more than one value_enum_id will appear for the same custom_attribute_id |
| 7 | value_float | number |  | The numeric value of a Custom Attribute |
| 8 | value_str | string |  | The textual value of a Custom Attribute |

## rfi_distribution_list

List of users who will be notified of changes to the RFI.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | rfi_id | string: UUID |  | ID for the RFI. Foreign Key: Table: rfis Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 4 | user_id | string |  | The Autodesk User ID of the user to be notified of changes to RFI. |

## rfi_location

The location details for an RFI

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | rfi_id | string: UUID |  | ID for the RFI. Foreign Key: Table: rfis Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 4 | location | string |  | A description of the location of the RFI in the construction project. |

## rfi_responses

The responses associated with the RFIs.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID of the response. |
| 2 | rfi_id | string: UUID |  | The ID for the RFI. Foreign Key: Table: rfis Column: id |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 5 | content | string |  | The content of the response |
| 6 | updated_by | string |  | The Autodesk User ID of the user who updated the response. |
| 7 | created_by | string |  | The Autodesk User ID of the user who created the response. |
| 8 | on_behalf | string |  | The Autodesk User ID of the user assignee. |
| 9 | status | enum: string | Possible Values: answered rejected | The response status |
| 10 | created_at | timestamp: SQL |  | The timestamp of the date and time the response was created |
| 11 | updated_at | timestamp: SQL |  | The last time the response attributes were updated |
| 12 | deleted_at | timestamp: SQL |  | The timestamp of the date and time the response was deleted This is only relevant for deleted responses. |
| 13 | state | enum: string | Possible Values: submitted draft | The response state |

## rfi_reviewers

Reviewers for RFIs

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | rfi_id | string: UUID |  | ID for the RFI. Foreign Key: Table: rfis Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 4 | user_id | string |  | The Autodesk User ID of the reviewer |
| 5 | type | string | Possible Values: user | Reviewer type |

## rfi_transitions

The lifecycle of the RFI - each row represents a transition of the RFI from one status to another

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID of the transition |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 4 | rfi_id | string: UUID |  | The RFI ID for the transition |
| 5 | from_status | string: null | Possible Values: draft submitted open answered openRev1 answeredRev1 openRev2 answeredManager closed void | The status of the RFI before the transition occurred. If the RFI was newly created, the value will be null. |
| 6 | to_status | string | Possible Values: draft submitted open answered openRev1 answeredRev1 openRev2 answeredManager closed void | The status of the RFI after the transition. |
| 7 | created_at | timestamp: SQL |  | The timestamp of the date and time the RFI transition was made. |
| 8 | created_by | string |  | The Autodesk User ID of the user who made the transition. |

## rfi_types

The type of the RFI

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID of the RFI Type |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 4 | name | string |  | The name of the RFI Type |
| 5 | wf_type | enum: string | Possible Values: reviewer_only reviewer_and_coordinator unknown | The workflow type of the RFI Type |

## rfis

Information about all the BIM 360 RFIs (requests for information) in a project, including details about their associated comments and attachments.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID for the RFI. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of RFI data |
| 4 | custom_identifier | string | Max length: 15 + Unique per container | Custom identifier for the RFI |
| 5 | title | string |  | Title for the RFI |
| 6 | question | string |  | Question for the RFI |
| 7 | status | enum: string | Possible Values: draft submitted open answered openRev1 answeredRev1 openRev2 answeredManager closed void | The current status of the RFI. |
| 8 | due_date | timestamp: SQL |  | The timestamp of the due date for the RFI. |
| 9 | linked_document | string |  | The URN of the document |
| 10 | linked_document_version | number |  | The document's version when the RFI was assigned to it |
| 11 | linked_document_close_version | number |  | The document's version when the RFI, that assigned to it, was closed |
| 12 | official_response | string |  | Official response of the RFI |
| 13 | official_response_status | enum: string | Possible Values: answered rejected | The RFI official response status of approval (if exists) |
| 14 | responded_at | timestamp: SQL |  | The timestamp of the date and time the RFI was responded to |
| 15 | responded_by | string |  | Autodesk User ID of the user who created the RFI |
| 16 | created_by | string |  | The Autodesk User ID of the user who created the RFI. |
| 17 | created_at | timestamp: SQL |  | The timestamp of the date and time the RFI was created. |
| 18 | updated_by | string |  | The Autodesk User ID of the user who updated the RFI |
| 19 | updated_at | timestamp: SQL |  | The timestamp of the date and time the RFI was updated |
| 20 | closed_by | string |  | The Autodesk User ID of the ID of the user who closed the RFI |
| 21 | closed_at | timestamp: SQL |  | The timestamp of the date and time the RFI was closed |
| 22 | suggested_answer | string |  | The suggested answer for the RFI. |
| 23 | manager_id | string |  | Manager for the RFI |
| 24 | answered_at | timestamp: SQL |  | The last time the RFI answer attribute was updated. |
| 25 | answered_by | string |  | The Autodesk User ID of the user who updated the RFI answer attribute |
| 26 | cost_impact | enum: string | Possible Values: Yes No Unknown | Is the cost impact of this RFI known? |
| 27 | schedule_impact | enum: string | Possible Values: Yes No Unknown | Is the schedule impact of this RFI known? |
| 28 | priority | string |  | The priority of he RFI |
| 29 | reference | string | Max length: 20 | The reference of the RFI |
| 30 | opened_at | timestamp: SQL |  | The timestamp of the RFI submition or in review date |
| 31 | location_id | string |  | The associated Location object ids |
| 32 | rfi_type | string: UUID |  | The type of the RFI |
| 33 | bridged_source | boolean |  | Is the RFI was a source of a bridge action |
| 34 | bridged_target | boolean |  | Is the RFI was a target of a bridge action |

© Copyright 2026 Autodesk Inc. | [Autodesk Construction Cloud](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
