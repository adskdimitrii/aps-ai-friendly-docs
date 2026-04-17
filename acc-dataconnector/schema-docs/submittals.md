# submittals Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=submittals&format=html

---

# submittals Schema Description

**Documentation Updated:** 2023-12-04  

- [attachments](#attachments)
- [comments](#comments)
- [item_cc_users](#item_cc_users)
- [item_co_reviewers_users](#item_co_reviewers_users)
- [item_distribution_list_users](#item_distribution_list_users)
- [itemrevisions](#itemrevisions)
- [items](#items)
- [packages](#packages)
- [specs](#specs)

## attachments

Attachments for BIM 360 Submittal items.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID for the Attachment |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | item_id | string: UUID |  | The ID for the parent Item Foreign Key: Table: items Column: id |
| 5 | name | string |  | Name of the file |
| 6 | is_response | boolean |  | is this attachment should be marked as a response |
| 7 | revision | number |  | Revision of the item when the attachment was added |
| 8 | attachment_type_id | enum: string | Possible Values: 1 - Document 2 - Photo 3 - PDF | ID of the attachment type (document/ photo/ pdf) |
| 9 | type_value | string |  | value of the attachment_type_id |
| 10 | created_by | string |  | Autodesk User ID of the user that created the attachment |
| 11 | created_at | timestamp: SQL |  | Date and time when the attachment created |
| 12 | updated_at | timestamp: SQL |  | Date and time when the attachment last updated |
| 13 | updated_by | string |  | Autodesk User ID of the user that last updated the attachment |
| 14 | is_review | boolean |  | Attachment is a part of a review process |
| 15 | is_deleted | boolean |  | was the attachment deleted |
| 16 | deleted_at | timestamp: SQL |  | when was the attachment deleted |
| 17 | upload_urn | string |  | storage URN where attachments are uploaded |

## comments

Comments for BIM 360 Submittal items.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID for the Comment |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | item_id | string: UUID |  | The ID for the parent Item Foreign Key: Table: items Column: id |
| 5 | updated_by | string |  | Autodesk User ID of the user that last updated the comment |
| 6 | updated_at | timestamp: SQL |  | Date and time when the comment updated |
| 7 | created_by | string |  | Autodesk User ID of the user that created the comment |
| 8 | created_at | timestamp: SQL |  | Date and time when the comment was created |
| 9 | body | string |  | Body of the comment |
| 10 | is_deleted | boolean |  | was the comment deleted |
| 11 | deleted_at | timestamp: SQL |  | when was the comment deleted |

## item_cc_users

List of Autodesk User IDs of cc'ed users. This table is going to be deprecated and replaced by item_distribution_list_users

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | item_id | string: UUID |  | ID for the Item Foreign Key: Table: items Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | user_id | string |  | Autodesk User IDs of cc'ed user |

## item_co_reviewers_users

List of Autodesk User IDs of consultant users

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | item_id | string: UUID |  | ID for the Item Foreign Key: Table: items Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | user_id | string |  | Autodesk User IDs of the reviewer user |

## item_distribution_list_users

List of Autodesk User IDs of distribution_list users and their type

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | item_id | string: UUID |  | ID for the Item Foreign Key: Table: items Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | user_id | string |  | Autodesk User IDs of cc'ed user/role/company |
| 5 | user_type_id | string | Possible Values: 1 - user 2 - company 3 - role | if of the distribution_list member user_type (user/role/company) |
| 6 | user_type_value | string |  | value of the user_type_id |

## itemrevisions

Revisions for BIM 360 Submittals

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | revision | number |  | Revision of the item when it was recorded |
| 2 | item_id | string: UUID |  | The ID for the Submittal. |
| 3 | item_title | string |  | Title (name) of the item, when new revision created |
| 4 | item_identifier | number |  | Identifier of the item. Created automatically |
| 5 | spec_title | string |  | Title of the spec |
| 6 | spec_identifier | string |  | Spec identifier. Created by the user |
| 7 | spec_id | string: UUID |  | ID for the Spec Section |
| 8 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 9 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |

## items

Submittal items for the BIM 360 system.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID for the Submittal. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | spec_id | string: UUID |  | ID for the associated Spec Foreign Key: Table: specs Column: id |
| 5 | spec_identifier | string |  | Identifier of the spec this item related to |
| 6 | title | string |  | Title (name) of the item |
| 7 | type_id | enum: string | Possible Values: 1 - Attic Stock 2 - Certificates 3 - O&M Manuals 4 - Product Data 5 - Samples 6 - Shop Drawings 7 - Test Data 8 - Warranty/Guarantee 9 - Other 10 - Documentation 11 - LEED 12 - Reports 13 - Schedule 14 - Qualification Data 15 - Mockup | ID of the item type |
| 8 | type_value | string |  | value of the item type_id |
| 9 | response_comment | string |  | Response comment of the item (in addition to response id) |
| 10 | assigned_to | string |  | Autodesk User ID of the user that the item is assigned to |
| 11 | revision | number |  | Revision of the item |
| 12 | responded_by | string |  | Autodesk User ID of the user that responded |
| 13 | description | string |  | Description of the item |
| 14 | responded_at | timestamp: SQL |  | Date and time when response was added |
| 15 | due_date | date: string |  | Date and time for the item to be done with current state |
| 16 | required_on_job_date | date: string |  | Date and time for the item to be done on site |
| 17 | manager | string |  | Autodesk User ID of the manager |
| 18 | reviewer | string |  | Autodesk User ID of the reviewer |
| 19 | created_by | string |  | Autodesk User ID of the user that created the item |
| 20 | created_at | timestamp: SQL |  | when was the item created |
| 21 | state_id | string |  | State of the item |
| 22 | response_id | enum: string | Possible Values: 1 - Rejected 2 - Revise and resubmit 3 - Approved as noted 4 - Approved 5 - For record only | ID of the response, if was added. |
| 23 | response_value | string |  | value of the response_id |
| 24 | subsection | string |  | Sub spec section |
| 25 | subcontractor | string |  | Autodesk User ID of the user that assigned as subcontractor |
| 26 | identifier | number |  | Identifier of the item. Created automatically |
| 27 | updated_by | string |  | Autodesk User ID of the user the last updated the item |
| 28 | updated_at | timestamp: SQL |  | last time the item was updated |
| 29 | status_id | enum: string | Possible Values: 1 - Required 2 - Open 3 - Closed 4 - Void 5 - Empty 6 - Draft | Status ID |
| 30 | status_value | string |  | value of the status_id |
| 31 | package_title | string |  | Title of the package the item is related to (if any) |
| 32 | package | string: UUID |  | ID for the associated Package Foreign Key: Table: packages Column: id |
| 33 | package_identifier | number |  | Identifier of the package the item is related to (if any) |
| 34 | priority_id | number | Possible Values: 1 - Low 2- Normal 3 - High | id of the priority the item is related to (if any) |
| 35 | priority_value | string |  | value of the priority_id |
| 36 | required_date | date: string |  | item's required date |
| 37 | required_approval_date | date: string |  | item's required approval date |
| 38 | lead_time | number |  | item's lead time |
| 39 | sent_to_submitter | timestamp: SQL |  | when the submitter received the item |
| 40 | received_from_submitter | timestamp: SQL |  | When the submitter moved the item forward |
| 41 | sent_to_reviewer | timestamp: SQL |  | When the reviewer received the item |
| 42 | received_from_reviewer | timestamp: SQL |  | When the reviewer moved the item forward |
| 43 | published_date | timestamp: SQL |  | When the item was closed and distributed |
| 44 | submitter_due_date | date: string |  | When the responsible contractor submission is due |
| 45 | manager_due_date | date: string |  | When the manager review is due |
| 46 | reviewer_due_date | date: string |  | When the reviewer review is due |

## packages

Submittal Packages for the BIM 360 system.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID for the Package |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | spec_id | string: UUID |  | ID for the associated Spec Foreign Key: Table: specs Column: id |
| 5 | title | string |  | Title of the package |
| 6 | identifier | number |  | Identifier of the package. Created Automatically |
| 7 | updated_by | string |  | Autodesk User ID of the user that last updated the package |
| 8 | created_at | timestamp: SQL |  | Date and time when the spec was created |
| 9 | created_by | string |  | Autodesk User ID of the user that created the package |
| 10 | updated_at | timestamp: SQL |  | Date and time when spec was last updated |
| 11 | deleted_at | timestamp: SQL |  | Date and time when package was deleted |
| 12 | is_deleted | boolean |  | Was the package deleted |
| 13 | spec_identifier | string |  | Identifier of the spec this package related to |

## specs

Submittal Spec Sections for the BIM 360 system.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID for the Spec Section |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | updated_by | string |  | Autodesk User ID of the user that last updated the spec |
| 5 | title | string |  | Title of the spec |
| 6 | identifier | string |  | Spec identifier. Created by the user |
| 7 | created_by | string |  | Autodesk User ID of the user that created the spec |
| 8 | created_at | timestamp: SQL |  | Date and time when the spec was created |
| 9 | updated_at | timestamp: SQL |  | Date and time when the spec was updated |
| 10 | is_deleted | boolean |  | is the spec deleted |
| 11 | deleted_at | timestamp: SQL |  | when was the spec deleted |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
