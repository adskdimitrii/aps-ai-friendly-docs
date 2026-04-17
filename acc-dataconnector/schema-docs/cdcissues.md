# cdcissues Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=cdcissues&format=html

---

# cdcissues Schema Description

**Documentation Updated:** 2026-02-04  

- [attachments](#attachments)
- [comments](#comments)
- [custom_attribute_list_values](#custom_attribute_list_values)
- [custom_attributes](#custom_attributes)
- [custom_attributes_mappings](#custom_attributes_mappings)
- [issue_subtypes](#issue_subtypes)
- [issue_types](#issue_types)
- [issues](#issues)
- [placements](#placements)
- [root_cause_categories](#root_cause_categories)
- [root_causes](#root_causes)
- [viewables](#viewables)

**Beta Release**  
This is a Beta release of the cdcissues data set and schema definitions are subject to change or even possibly be removed from the final data set release. Thank you for your understanding with any future schema updates.

## attachments

Attachments on Issue in BIM 360 Issue-Types. - This is the Change Data Capture (CDC) enabled version of the issues.attachments table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | attachment_id | string: UUID |  | ID of the attachment |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | issue_id | string: UUID |  | BIM 360 ID of the issue associated with the attachment. Foreign Key: Table: issues Column: id |
| 5 | display_name | string |  | File name to be displayed |
| 6 | file_name | string |  | Actual file name |
| 7 | storage_urn | string |  | Storage urn |
| 8 | file_size | number |  | File type |
| 9 | file_type | string |  | File size |
| 10 | lineage_urn | string |  | Lineage urn of the attachment |
| 11 | version | number |  | Version number |
| 12 | version_urn | string |  | Version urn |
| 13 | tip_version_urn | string |  | Tip version urn |
| 14 | bubble_urn | string |  | Bubble urn |
| 15 | created_at | timestamp: SQL |  | Created at timestamp Column used for filtering Date Range Extraction requests |
| 16 | created_by | string |  | Autodesk User ID of the user who created the attachment. |
| 17 | deleted_at | timestamp: SQL |  | Deleted at timestamp Column used for filtering Date Range Extraction requests |
| 18 | deleted_by | string |  | Autodesk User ID of the user who deleted the attachment. |
| 19 | updated_at | timestamp: SQL |  | Date and time the attachment was updated in ISO8601 format Column used for filtering Date Range Extraction requests |
| 20 | updated_by | string |  | Autodesk User ID of the user who updated the attachment. |
| 21 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## comments

Comments associated with BIM 360 issues. - This is the Change Data Capture (CDC) enabled version of the issues.comments table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | comment_id | string: UUID |  | Unique identifier of the comment |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | issue_id | string: UUID |  | BIM 360 ID of the issue associated with this comment. Foreign Key: Table: issues Column: id |
| 5 | comment_body | string |  | Content of the comment. |
| 6 | created_by | string |  | Autodesk User ID of the user who created the comment |
| 7 | created_at | timestamp: SQL |  | Timestamp of the date and time the comment was created Column used for filtering Date Range Extraction requests |
| 8 | updated_at | timestamp: SQL |  | Timestamp when the comment was updated Column used for filtering Date Range Extraction requests |
| 9 | deleted_at | timestamp: SQL |  | Timestamp when the comment was deleted Column used for filtering Date Range Extraction requests |
| 10 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## custom_attribute_list_values

The list values for a customer attribute of list type - This is the Change Data Capture (CDC) enabled version of the issues.custom_attribute_list_values table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | attribute_mappings_id | string: UUID |  | The ID of the custom attribute mapping definition Foreign Key: Table: custom_attributes_mappings Column: id |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | list_id | string: UUID |  | ID of the customer attribute list value |
| 5 | list_value | string |  | Display name of the custom attribute list value |
| 6 | created_at | timestamp: SQL |  | Timestamp when the custom_attribute_list_value was created Column used for filtering Date Range Extraction requests |
| 7 | updated_at | timestamp: SQL |  | Timestamp when the custom_attribute_list_value was updated Column used for filtering Date Range Extraction requests |
| 8 | deleted_at | timestamp: SQL |  | Timestamp when the custom_attribute_list_value was deleted Column used for filtering Date Range Extraction requests |
| 9 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## custom_attributes

Custom attributes for Issues  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | issue_id | string: UUID |  | Unique identifier of the issue |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | mapped_item_type | enum: string | Possible Values: container issueType issueSubtype | The type of item the custom attribute is mapped to. Possible values: container (all types and subtypes inherit the mapping), issueType (subtypes inherit the mapping), issueSubtype |
| 5 | attribute_mapping_id | string: UUID |  | The ID of the custom attribute mapping definition Foreign Key: Table: custom_attributes_mappings Column: id |
| 6 | attribute_title | string | Max length: 100 | The title of the custom attribute. |
| 7 | attribute_description | string | Max length: 500 | The description of the custom attribute. |
| 8 | attribute_data_type | enum: string | Possible Values: list text paragraph numeric | The type of custom attribute. |
| 9 | is_required | boolean |  | true if the custom attribute is required false if the custom attribute is not required |
| 10 | attribute_value | string |  | Custom attribute value. In the case of a list option, the id of the selected option, otherwise the value will the actual value |
| 11 | created_at | timestamp: SQL |  | Date and time the attribute was created in ISO8601 format Column used for filtering Date Range Extraction requests |
| 12 | created_by | string |  | Autodesk User ID of the user who created the attribute |
| 13 | updated_at | timestamp: SQL |  | Date and time the attribute was updated in ISO8601 format Column used for filtering Date Range Extraction requests |
| 14 | updated_by | string |  | Autodesk User ID of the user who updated the attribute |
| 15 | deleted_at | timestamp: SQL |  | Date and time the attribute was deleted in ISO8601 format Column used for filtering Date Range Extraction requests |
| 16 | deleted_by | string |  | Autodesk User ID of the user who deleted the attribute. |
| 17 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## custom_attributes_mappings

Custom attributes for a project, including the custom attribute title, description and type. - This is the Change Data Capture (CDC) enabled version of the issues.custom_attributes_mappings table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID of the custom attribute mapping. |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | mapped_item_type | enum: string | Possible Values: container issueType issueSubtype | The type of item the custom attribute is mapped to. Possible values: container (all types and subtypes inherit the mapping) issueType (subtypes inherit the mapping) issueSubtype. |
| 5 | mapped_item_id | string: UUID |  | The ID of the item (container - type - or subtype) the custom attribute is mapped to. |
| 6 | title | string | Max length: 100 | The title of the custom attribute. |
| 7 | description | string | Max length: 500 | The description of the custom attribute. |
| 8 | data_type | enum: string | Possible Values: list text paragraph numeric | The type of custom attribute. |
| 9 | order | number |  | The order that the custom attributes were mapped to the item (container - type - subtype). This is only relevant to non-inherited mappings. |
| 10 | is_required | boolean |  | true if the custom attribute is required false if the custom attribute is not required |
| 11 | created_at | timestamp: SQL |  | The date and time the custom attribute mapping was created - in the following format: YYYY-MM-DDThh:mm:ss.sz. Column used for filtering Date Range Extraction requests |
| 12 | created_by | string |  | The BIM 360 ID of the user who created the custom attribute mapping. To verify the actual name of the user - call GET users and find the BIM 360 ID (uid). Note that you need to use a 2-legged token to call GET users. |
| 13 | updated_at | timestamp: SQL |  | The last date and time the custom attribute was updated - in the following format: YYYY-MM-DDThh:mm:ss.sz. Column used for filtering Date Range Extraction requests |
| 14 | updated_by | string |  | The BIM 360 ID of the user who last updated the custom attribute mapping. To verify the actual name of the user - call GET users and find the BIM 360 ID (uid). Note that you need to use a 2-legged token to call GET users. |
| 15 | deleted_at | timestamp: SQL |  | Timestamp when the custom_attributes_mapping was deleted Column used for filtering Date Range Extraction requests |
| 16 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## issue_subtypes

Subtypes for BIM 360 Issue-Types. - This is the Change Data Capture (CDC) enabled version of the issues.issue_subtypes table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | issue_subtype_id | string: UUID |  | ID for the Issue Subtype |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | issue_type_id | string: UUID |  | Parent Issue Type ID for this Subtype Foreign Key: Table: issue_types Column: id |
| 5 | issue_subtype | string | Max length: 250 | Title of the Issue Subtype |
| 6 | is_active | boolean |  | Is the Issue Subtype Active |
| 7 | created_by | string |  | Autodesk User ID of the user who created the issue type |
| 8 | created_at | timestamp: SQL |  | Date and time the issue type was created in ISO8601 format Column used for filtering Date Range Extraction requests |
| 9 | updated_by | string |  | Autodesk User ID of the user who updated the issue type |
| 10 | updated_at | timestamp: SQL |  | Date and time the issue type was updated in ISO8601 format Column used for filtering Date Range Extraction requests |
| 11 | deleted_by | string |  | Autodesk User ID of the user who deleted the issue type |
| 12 | deleted_at | timestamp: SQL |  | Date and time the issue type was deleted in ISO8601 format Column used for filtering Date Range Extraction requests |
| 13 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## issue_types

Issue Types for BIM 360 Issues. - This is the Change Data Capture (CDC) enabled version of the issues.issue_types table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | issue_type_id | string: UUID |  | ID of the Issue Type |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | issue_type | string | Max length: 250 | Title of the Issue Type |
| 5 | is_active | boolean |  | Is the Issue Type active |
| 6 | created_by | string |  | Autodesk User ID of the user who created the issue type |
| 7 | created_at | timestamp: SQL |  | Date and time the issue type was created in ISO8601 format Column used for filtering Date Range Extraction requests |
| 8 | updated_by | string |  | Autodesk User ID of the user who updated the issue type |
| 9 | updated_at | timestamp: SQL |  | Date and time the issue type was updated in ISO8601 format Column used for filtering Date Range Extraction requests |
| 10 | deleted_by | string |  | Autodesk User ID of the user who deleted the issue type |
| 11 | deleted_at | timestamp: SQL |  | Date and time the issue type was deleted in ISO8601 format Column used for filtering Date Range Extraction requests |
| 12 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## issues

Issues created in the BIM 360 system. - This is the Change Data Capture (CDC) enabled version of the issues.issues table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | issue_id | string: UUID |  | Unique identifier of the issue |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | display_id | number |  | Chronological user-friendly identifier of the issue |
| 5 | title | string: null |  | Name of the issue |
| 6 | description | string: null |  | Description of the purpose of the issue |
| 7 | type_id | string: UUID |  | Unique identifier of the type of the issue |
| 8 | subtype_id | string: UUID |  | Unique identifier of the subtype of the issue |
| 9 | status | string: null | Possible Values: open work_completed ready_to_inspect not_approved in_dispute closed void answered draft pending in_progress completed in_review | Unique identifier of the current status of the issue |
| 10 | assignee_id | string: null |  | Autodesk User ID of the current assignee of this issue |
| 11 | assignee_type | string: null | Possible Values: user company role | Type of the current assignee of this issue |
| 12 | due_date | timestamp: SQL |  | Due date of the issue in ISO8601 format |
| 13 | location_id | string: UUID |  | Unique LBS (Location Breakdown Structure) identifier that relates to the issue |
| 14 | location_details | string: null |  | Location as plain text that relates to the issue |
| 15 | linked_document_urn | string: null |  | Linked document URN |
| 16 | owner_id | string: null |  | Autodesk User ID of the user who owns this issue. Used in case this issue was created on-behalf of another person |
| 17 | root_cause_id | string: UUID |  | Unique identifier of the type of root cause for the issue |
| 18 | root_cause_category_id | string: UUID |  | Unique identifier of the category for the root cause |
| 19 | response | string: null |  | Official response of the user for the issue |
| 20 | response_by | string: null |  | Who responded to the issue |
| 21 | response_at | timestamp: SQL |  | When was the response made |
| 22 | opened_by | string: null |  | Autodesk User ID of the user who opened the issue |
| 23 | opened_at | timestamp: SQL |  | Date and time the issue was opened in ISO8601 format |
| 24 | closed_by | string: null |  | Autodesk User ID of the user who closed the issue |
| 25 | closed_at | timestamp: SQL |  | Date and time the issue was closed in ISO8601 format |
| 26 | created_by | string: null |  | Autodesk User ID of the user who created the issue |
| 27 | created_at | timestamp: SQL |  | Date and time the issue was created in ISO8601 format Column used for filtering Date Range Extraction requests |
| 28 | updated_by | string: null |  | Autodesk User ID of the user who updated the issue |
| 29 | updated_at | timestamp: SQL |  | Date and time the issue was updated in ISO8601 format Column used for filtering Date Range Extraction requests |
| 30 | start_date | timestamp: SQL |  | Start date of the issue in ISO8601 format |
| 31 | deleted_at | timestamp: SQL |  | deleted_at. If set the issue is 'soft deleted' Column used for filtering Date Range Extraction requests |
| 32 | snapshot_urn | string: null |  | Snapshot URN |
| 33 | published | boolean |  | published: shows if the issues is published or not. |
| 34 | gps_coordinates | string |  | GPS location of the issues in (latitude, longitude) format |
| 35 | deleted_by | string |  | Autodesk User ID of the user who deleted the issue |
| 36 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## placements

Placements associated with ACC issues. - This is the Change Data Capture (CDC) enabled version of the issues.placements table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | placement_id | string: UUID |  | ID of the placement |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | issue_id | string: UUID |  | ID of the issue associated with this placement. Foreign Key: Table: issues Column: id |
| 5 | lineage_urn | string |  | Lineage URN of the file |
| 6 | type | string |  | Type of placement |
| 7 | created_at_version | number |  | Version at which the placement was created |
| 8 | origin_product | string |  | Product where the placement originated |
| 9 | origin_tool | string |  | Tool used to create the placement |
| 10 | created_by | string |  | Autodesk User ID of the user who created the placement |
| 11 | created_at | timestamp: SQL |  | Date and time the placement was created in ISO8601 format Column used for filtering Date Range Extraction requests |
| 12 | updated_by | string |  | Autodesk User ID of the user who updated the placement |
| 13 | updated_at | timestamp: SQL |  | Date and time the placement was updated in ISO8601 format Column used for filtering Date Range Extraction requests |
| 14 | deleted_by | string |  | Autodesk User ID of the user who deleted the placement |
| 15 | deleted_at | timestamp: SQL |  | Date and time the placement was deleted in ISO8601 format Column used for filtering Date Range Extraction requests |
| 16 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## root_cause_categories

Root Cause Categories for BIM 360 Issues. - This is the Change Data Capture (CDC) enabled version of the issues.root_cause_categories table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | root_cause_category_id | string: UUID |  | ID of Root Cause Category |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | root_cause_category | string | Max length: 100 | Title of the root cause category |
| 5 | is_active | boolean |  | Always returns TRUE, regardless of the real value. Will be deprecated in the future. |
| 6 | created_by | string |  | Autodesk User ID of the user who created the issue type |
| 7 | created_at | timestamp: SQL |  | Date and time the issue type was created in ISO8601 format Column used for filtering Date Range Extraction requests |
| 8 | updated_by | string |  | Autodesk User ID of the user who updated the issue type |
| 9 | updated_at | timestamp: SQL |  | Date and time the issue type was updated in ISO8601 format Column used for filtering Date Range Extraction requests |
| 10 | deleted_by | string |  | Autodesk User ID of the user who deleted the issue type |
| 11 | deleted_at | timestamp: SQL |  | Date and time the issue type was deleted in ISO8601 format Column used for filtering Date Range Extraction requests |
| 12 | is_system | boolean |  | Is this a system level root cause category? |
| 13 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## root_causes

Root Causes for BIM 360 Issues. - This is the Change Data Capture (CDC) enabled version of the issues.root_causes table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | root_cause_id | string: UUID |  | ID of the root cause |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | root_cause_category_id | string: UUID |  | BIM 360 ID of the root cause category associated with this root cause Foreign Key: Table: root_cause_categories Column: id |
| 5 | title | string | Max length: 100 | Title of the root cause |
| 6 | is_active | boolean |  | Always returns TRUE, regardless of the real value. Will be deprecated in the future. |
| 7 | created_by | string |  | Autodesk User ID of the user who created the issue type |
| 8 | created_at | timestamp: SQL |  | Date and time the issue type was created in ISO8601 format Column used for filtering Date Range Extraction requests |
| 9 | updated_by | string |  | Autodesk User ID of the user who updated the issue type |
| 10 | updated_at | timestamp: SQL |  | Date and time the issue type was updated in ISO8601 format Column used for filtering Date Range Extraction requests |
| 11 | deleted_by | string |  | Autodesk User ID of the user who deleted the issue type |
| 12 | deleted_at | timestamp: SQL |  | Date and time the issue type was deleted in ISO8601 format Column used for filtering Date Range Extraction requests |
| 13 | is_system | boolean |  | Is this a system level root cause? |
| 14 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## viewables

Viewables associated with placements of ACC issues. - This is the Change Data Capture (CDC) enabled version of the issues.viewables table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | placement_id | string: UUID |  | Unique identifier of the placement associated with this viewable Foreign Key: Table: placements Column: id |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | issue_id | string: UUID |  | BIM 360 ID of the issue associated with the viewable. Foreign Key: Table: issues Column: id |
| 5 | file_version | number |  | File version identifier |
| 6 | file_version_urn | string |  | URN of the file version |
| 7 | guid | string |  | GUID of the viewable |
| 8 | name | string |  | Name of the viewable |
| 9 | viewable_id | string |  | Identifier of the viewable |
| 10 | is_3d | boolean |  | Indicates if the viewable is 3D |
| 11 | created_at | timestamp: SQL |  | Date and time the viewable was created in ISO8601 format Column used for filtering Date Range Extraction requests |
| 12 | updated_at | timestamp: SQL |  | Date and time the viewable was updated in ISO8601 format Column used for filtering Date Range Extraction requests |
| 13 | deleted_at | timestamp: SQL |  | Date and time the viewable was deleted in ISO8601 format Column used for filtering Date Range Extraction requests |
| 14 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
