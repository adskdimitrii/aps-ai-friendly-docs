# checklists Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=checklists&format=html

---

# checklists Schema Description

**Documentation Updated:** 2024-04-15  

- [checklist_assignees](#checklist_assignees)
- [checklist_attachments](#checklist_attachments)
- [checklist_item_doc_attachments](#checklist_item_doc_attachments)
- [checklist_items](#checklist_items)
- [checklist_items_answers](#checklist_items_answers)
- [checklist_section_assignees](#checklist_section_assignees)
- [checklist_sections](#checklist_sections)
- [checklist_sections_signatures](#checklist_sections_signatures)
- [checklist_signatures](#checklist_signatures)
- [checklists](#checklists)
- [template_item_instructions](#template_item_instructions)
- [template_items](#template_items)
- [template_items_all](#template_items_all)
- [template_items_answers](#template_items_answers)
- [template_sections](#template_sections)
- [template_sections_all](#template_sections_all)
- [template_signatures](#template_signatures)
- [template_signatures_all](#template_signatures_all)
- [templates](#templates)
- [templates_versions](#templates_versions)

## checklist_assignees

The assignees for checklists in BIM 360.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | instance_id | number |  | ID of the Checklist Foreign Key: Table: checklists Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | id | number |  | serial id |
| 5 | assignee_id | string |  | Autodesk ID of the assignee. |
| 6 | name | string |  | Name of the assignee |
| 7 | assignee_type | enum: string | Possible Values: User Company Role | Name of the entity assigned to the checklist. |
| 8 | created_at | timestamp: SQL |  | Date and time the resource was last updated. |
| 9 | updated_at | timestamp: SQL |  | Date and time the resource was created. |
| 10 | deleted_at | timestamp: SQL |  | Date and time the resource was deleted. |
| 11 | is_previous_assignee | boolean |  | true if a user was an assignee and removed. |

## checklist_attachments

Attachments to checklist items

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID of the attachment |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | lineage_urn | string |  | asdk urn at which attachment is uploaded |
| 5 | version | number |  | Version of the attachment. |
| 6 | instance_id | number |  | ID of the Checklist. |

## checklist_item_doc_attachments

Attachments to checklist items

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID of the Item Document Attachment |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | lineage_urn | string |  | asdk urn at which attachment is uploaded |
| 5 | item_id | number |  | ID of the Checklist item |
| 6 | section_id | number |  | ID of the Checklist section |
| 7 | instance_id | number |  | ID of the Checklist. |

## checklist_items

The Checklist items

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | ID of the Checklist item |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | created_at | timestamp: SQL |  | Date and time the resource was last updated. |
| 5 | updated_at | timestamp: SQL |  | Date and time the resource was created. |
| 6 | instance_section_id | number |  | ID of the Checklist Foreign Key: Table: checklist_sections Column: id |
| 7 | template_item_id | number |  | the template item id |
| 8 | modified_by | string |  | The oxygen Id of the last user that modified the item |
| 9 | is_required | boolean |  | Is the answer required for this question |
| 10 | note | string |  | a note of the item |
| 11 | title | string |  | the title of the item |
| 12 | answers | string |  | Answers of the item (can be a UUID FOREIGN KEY for answer_type=6) |
| 13 | instance_id | number |  | ID of the Checklist Foreign Key: Table: checklists Column: id |
| 14 | answer_type | number |  | Type of answer specified for this checklist item. answer_type = 6 means the answers column contains a UUID that is a FOREIGN KEY (id) into the checklist_items_answers table |
| 15 | answers_v2 | string |  | Answers of the checklist item (with normalized formatting across answer types, e.g.: without UUID FOREIGN KEY for answer_type=6) |

## checklist_items_answers

Possible Template Item Answers.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID of the answer. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | answer | string |  | Answer for the checklist item |
| 5 | item_version_id | number |  | Identifier for item version. if not given the lastest version is selected of the item. |

## checklist_section_assignees

The assignees for checklists in BIM 360.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | ID of the Checklist Section Assignees |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | instance_id | number |  | ID of the Checklist Foreign Key: Table: checklists Column: id |
| 5 | instance_section_id | number |  | ID of the Checklist Foreign Key: Table: checklist_sections Column: id |
| 6 | id2 | number |  | Second ID of the Checklist Section Assignees |
| 7 | assignee_id | string |  | Autodesk ID of the assignee. |
| 8 | assignee_type | enum: string | Possible Values: User Company Role | Name of the entity assigned to the checklist. |
| 9 | created_at | timestamp: SQL |  | Date and time the resource was last updated. |
| 10 | updated_at | timestamp: SQL |  | Date and time the resource was created. |
| 11 | deleted_at | timestamp: SQL |  | Date and time the resource was deleted. |
| 12 | is_previous_section_assignee | boolean |  | true if a user was an assignee and removed. |

## checklist_sections

The Checklist Sections

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | ID of the Checklist section |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | created_at | timestamp: SQL |  | Date and time the resource was created. |
| 5 | updated_at | timestamp: SQL |  | Date and time the resource was last updated. |
| 6 | instance_id | number |  | ID of the Checklist Foreign Key: Table: checklists Column: id |
| 7 | template_section_id | number |  | ID of the section template Foreign Key: Table: template_sections Column: id |
| 8 | modified_by | string |  | The oxygen Id of the last user that modified the item |
| 9 | status | string |  | Status of the checklist section |

## checklist_sections_signatures

Information about BIM 360 Field Management checklists section signatures

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID of signature |
| 2 | instance_section_id | number |  | checklist section number |
| 3 | instance_id | number |  | ID of checklist |
| 4 | required_by | string |  | Required by |
| 5 | is_required | boolean |  | Is signature required |
| 6 | instructions | string |  | Instructions for signature |
| 7 | signed_name | string |  | Name for signature |
| 8 | signed_company | string |  | Company for signature |
| 9 | submitted_by | string |  | OxygenId of user who submitted the signature |
| 10 | signed_at | timestamp: SQL |  | Date and time when resource was signed |
| 11 | created_at | timestamp: SQL |  | Date and time when resource was created |
| 12 | deleted_at | timestamp: SQL |  | Date and time when resource was deleted |
| 13 | urn | string |  | Urn of resource |
| 14 | oss_urn | string |  | Oss urn of resource |
| 15 | upload_status | enum: string | Possible Values: Not Completed Completed | Upload status of signature |
| 16 | bim360_project_id | string: UUID |  | BIM 360 HQ Account ID. |
| 17 | bim360_account_id | string: UUID |  | BIM 360 HQ Project ID. |

## checklist_signatures

The signatures of a template

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID of the signature |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | instance_id | number |  | The ID of the checklist |
| 5 | required_by | string |  | The name of the person/role that supposed to sign |
| 6 | is_required | boolean |  | Weather the signature is required to be signed in order to complete the checklist or not |
| 7 | defined_at | enum: string | Templates/Checklist | Where the signature is defined |
| 8 | required_name | string |  | The name of the person that supposed to sign |
| 9 | required_company | string |  | The company of the person that supposed to sign |
| 10 | signed_name | string |  | The name of the signed person |
| 11 | signed_company | string |  | The company of the signed person |
| 12 | submitted_by | string |  | The oxygen Id of the user that signed |
| 13 | signed_at | timestamp: SQL |  | The date of the signing |
| 14 | created_at | timestamp: SQL |  | Date and time the resource was created. |
| 15 | updated_at | timestamp: SQL |  | Date and time the resource was last updated. |
| 16 | deleted_at | timestamp: SQL |  | Date and time the resource was deleted. |
| 17 | type | enum: string | SVG/Attachment | The type of the signature file |
| 18 | is_signed | boolean |  | Weather the required signature signed or not |

## checklists

Information about all the BIM 360 Field Management checklists in a project, including details about their statuses, priorities, and assignees.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | The unique identifier of the checklist |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | scheduled_date | timestamp: SQL |  | Scheduled date in ISO8601 format |
| 5 | location | string |  | Location for the checklist activity |
| 6 | title | string |  | Name of the checklist. |
| 7 | template_id | number |  | ID of the Template |
| 8 | template_version_id | number |  | Version ID of the template associated with the checklist. Every time you update a template it updates the version ID. |
| 9 | created_by | string |  | Autodesk ID of the user who created the checklist. |
| 10 | modified_by | string |  | Autodesk ID of the user who last modified the checklist. |
| 11 | updated_at | timestamp: SQL |  | Date and time the resource was last updated in ISO8601 format. |
| 12 | created_at | timestamp: SQL |  | Date and time the resource was last created in ISO8601 format. |
| 13 | deleted_at | timestamp: SQL |  | Date and time the resource was deleted - used for offline mobile DB management in ISO8601 format. |
| 14 | instructions | string |  | Description of the template. |
| 15 | template_type | enum: string | Possible Values: Quality Punch List Safety Commissioning | Template Type Name |
| 16 | status | enum: string | Possible Values: Not Scheduled Scheduled In Progress Completed Signed Of Pending Signature Not Started | Status Name for the checlist |
| 17 | progress | number |  | Percentage of completed checklist items; calculated using |
| 18 | completed_items_count | number |  | Number of completed checklist items. |
| 19 | items_count | number |  | Number of checklist items. |
| 20 | sections_count | number |  | Number of checklist sections. |
| 21 | created_by_company | string |  | oxygenId of the company |
| 22 | required_signatures_count | number |  | total number of signatures |
| 23 | unsigned_signatures_count | number |  | total number of unssignatures |
| 24 | allow_section_assignee | boolean |  | true if a user can be assigned to the a checklist sections. false if a user cannot be assigned to the a checklist sections. |
| 25 | checklist_id | number |  | Sequential id in which checklist is created in the project. |
| 26 | completed_on | timestamp: SQL |  | Date and time the resource was completed in ISO8601 format. |
| 27 | started_on | timestamp: SQL |  | Date and time the resource status changed from Not Started to In Progress in ISO8601 format. |
| 28 | is_archived | boolean |  | true if resource is archived. |
| 29 | archived_on | timestamp: SQL |  | Date and time the resource was last archived/unarchived in ISO8601 format. |
| 30 | archived_by | string |  | oxygenId of the last user that archived/unarchived the checklist. |

## template_item_instructions

The item instructions for BIM 360 Field Management checklists.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | template_id | number |  | ID of the Template Foreign Key: Table: templates Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | template_version_id | number |  | Version ID of the template. Every time you update a template it updates the version ID. Foreign Key: Table: templates Column: id |
| 5 | section_id | number |  | ID of the Template Section Foreign Key: Table: template_sections Column: id |
| 6 | item_id | number |  | ID of the Template Item Foreign Key: Table: template_items Column: id |
| 7 | item_version_id | number |  | Identifier for item version. if not given the lastest version is selected of the item. |
| 8 | id | number |  | ID of the description of the instruction. |
| 9 | instructions_type | string |  | The instructions type |
| 10 | data | string |  | Description of the item. |
| 11 | updated_at | timestamp: SQL |  | Date and time the resource was last updated. |
| 12 | created_at | timestamp: SQL |  | Date and time the resource was created. |

## template_items

The items for BIM 360 Field Management checklists.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | template_version_id | number |  | Version ID of the template. Every time you update a template it updates the version ID. Foreign Key: Table: templates Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | template_id | number |  | ID of the Template |
| 5 | template_section_id | number |  | ID of the Template Section Foreign Key: Table: template_sections Column: id |
| 6 | item_id | number |  | The ID of the item |
| 7 | item_version_id | number |  | Identifier for item version. if not given the lastest version is selected of the item. |
| 8 | number | number |  | Item number according to the order the item was created in the template. |
| 9 | index | number |  | Order the items appear in the UI. |
| 10 | is_required | boolean | true - it is required to answer this question, false - it is optional to answer this question. | Is the answer required for this question |
| 11 | title | string |  | Title of the item |
| 12 | section_id | number |  | ID of the section. Foreign Key: Table: sections Column: id |
| 13 | updated_at | timestamp: SQL |  | Date and time the resource was last updated. |
| 14 | created_at | timestamp: SQL |  | Date and time the resource was created. |
| 15 | response_type | string |  | The response type name |
| 16 | possible_answers | string | comma separated list of answers | The possible answers of the item |

## template_items_all

The items for BIM 360 Field Management checklists. (NOTE: THIS TABLE IS ONLY AVAILABLE IN PROJECT LEVEL EXTRACTS DUE TO SIZE CONSTRAINTS)

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | template_version_id | number |  | Version ID of the template. Every time you update a template it updates the version ID. Foreign Key: Table: templates Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | template_id | number |  | ID of the Template |
| 5 | template_section_id | number |  | ID of the Template Section Foreign Key: Table: template_sections Column: id |
| 6 | item_id | number |  | The ID of the item |
| 7 | item_version_id | number |  | Identifier for item version. if not given the lastest version is selected of the item. |
| 8 | number | number |  | Item number according to the order the item was created in the template. |
| 9 | index | number |  | Order the items appear in the UI. |
| 10 | is_required | boolean | true - it is required to answer this question, false - it is optional to answer this question. | Is the answer required for this question |
| 11 | title | string |  | Title of the item |
| 12 | section_id | number |  | ID of the section. Foreign Key: Table: sections Column: id |
| 13 | updated_at | timestamp: SQL |  | Date and time the resource was last updated. |
| 14 | created_at | timestamp: SQL |  | Date and time the resource was created. |
| 15 | response_type | string |  | The response type name |
| 16 | possible_answers | string | comma separated list of answers | The possible answers of the item |

## template_items_answers

Possible Template Item Answers

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | Added for project scoping of checklist data |
| 3 | list_response_id | string: UUID |  | ID of the type of answer. |
| 4 | possible_answers | string |  | The possible answers of the item |

## template_sections

The section information for BIM 360 Field Management checklists.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | ID of the section. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | template_id | number |  | ID of the Template |
| 5 | template_version_id | number |  | Version ID of the template. Every time you update a template it updates the version ID. Foreign Key: Table: templates Column: id |
| 6 | title | string |  | Name of the section. |
| 7 | number | number |  | Section number according to the order the section was created in the template. The number is displayed in the format that is defined in included.sections.attributes.sectionNumbering.id |
| 8 | index | number |  | Number of the section according to the order that it appears in the UI. |
| 9 | instructions | string |  | Description of the section. |
| 10 | updated_at | timestamp: SQL |  | Date and time the resource was last updated. |
| 11 | created_at | timestamp: SQL |  | Date and time the resource was created. |

## template_sections_all

The section information for BIM 360 Field Management checklists. (NOTE: THIS TABLE IS ONLY AVAILABLE IN PROJECT LEVEL EXTRACTS DUE TO SIZE CONSTRAINTS)

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | ID of the section. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | template_id | number |  | ID of the Template |
| 5 | template_version_id | number |  | Version ID of the template. Every time you update a template it updates the version ID. Foreign Key: Table: templates Column: id |
| 6 | title | string |  | Name of the section. |
| 7 | number | number |  | Section number according to the order the section was created in the template. The number is displayed in the format that is defined in included.sections.attributes.sectionNumbering.id |
| 8 | index | number |  | Number of the section according to the order that it appears in the UI. |
| 9 | instructions | string |  | Description of the section. |
| 10 | updated_at | timestamp: SQL |  | Date and time the resource was last updated. |
| 11 | created_at | timestamp: SQL |  | Date and time the resource was created. |

## template_signatures

The signatures of a template

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | id of the template signatures |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | template_version_id | number |  | Template signature version ID |
| 5 | template_id | number |  | Template signature ID |
| 6 | required_by | string |  | Who is required to sign |
| 7 | is_required | boolean |  | Is the template signature required |
| 8 | updated_at | timestamp: SQL |  | Date and time the resource was last updated. |
| 9 | created_at | timestamp: SQL |  | Date and time the resource was created. |

## template_signatures_all

The signatures of a template (NOTE: THIS TABLE IS ONLY AVAILABLE IN PROJECT LEVEL EXTRACTS DUE TO SIZE CONSTRAINTS)

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID of the signature |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | template_version_id | number |  | Template version ID for the signature |
| 5 | template_id | number |  | Template ID for the signature |
| 6 | required_by | string |  | Required by |
| 7 | is_required | boolean |  | Is the signature required for this question |
| 8 | updated_at | timestamp: SQL |  | Date and time the resource was last updated. |
| 9 | created_at | timestamp: SQL |  | Date and time the resource was created. |

## templates

Information about a specific BIM 360 Field Management templates, including details about the items, sections, and attachments in the template.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | template_id | number |  | ID of the template |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | title | string |  | Name of the template. |
| 5 | template_version_id | number |  | Version ID of the template. Every time you update a template it updates the version ID. |
| 6 | created_by | string |  | Autodesk ID of the user who created the template. |
| 7 | updated_at | timestamp: SQL |  | Date and time the resource was last updated. |
| 8 | created_at | timestamp: SQL |  | Date and time the resource was created. |
| 9 | instructions | string |  | Description of the template. |
| 10 | template_type | enum: string | Possible Values: Quality Punch List Safety Commissioning | Name for the template type |
| 11 | allow_section_assignee | boolean |  | true if you can add a section assignee to the template. false if you cannot add a section assignee to the template. |
| 12 | items_count | number |  | Number of items |
| 13 | sections_count | number |  | Number of sections |
| 14 | modified_by | string |  | oxygenId of the last user that updated the checklist |
| 15 | version_number | number |  | Version Number for the template |
| 16 | share_status | enum: string | Possible Values: active detached deleted | Status of account level template in project. Possible values are active/detached/deleted. |
| 17 | deleted_at | timestamp: SQL |  | Date and time the resource was deleted. |

## templates_versions

Information about BIM 360 Field Management templates (all versions), including details about the items, sections, and attachments in the template.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | template_id | number |  | ID of the template |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | title | string |  | Name of the template. |
| 5 | template_version_id | number |  | Version ID of the template. Every time you update a template it updates the version ID. |
| 6 | created_by | string |  | Autodesk ID of the user who created the template. |
| 7 | updated_at | timestamp: SQL |  | Date and time the resource was last updated. |
| 8 | created_at | timestamp: SQL |  | Date and time the resource was created. |
| 9 | instructions | string |  | Description of the template. |
| 10 | template_type | enum: string | Possible Values: Quality Punch List Safety Commissioning | Name for the template type |
| 11 | allow_section_assignee | boolean |  | true if you can add a section assignee to the template. false if you cannot add a section assignee to the template. |
| 12 | items_count | number |  | Number of items |
| 13 | sections_count | number |  | Number of sections |
| 14 | modified_by | string |  | oxygenId of the last user that updated the checklist |
| 15 | version_number | number |  | Version Number for the template |
| 16 | share_status | enum: string | Possible Values: active detached deleted | Status of account level template in project. Possible values are active/detached/deleted. |
| 17 | deleted_at | timestamp: SQL |  | Date and time the resource was deleted. |

© Copyright 2026 Autodesk Inc. | [Autodesk Construction Cloud](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
