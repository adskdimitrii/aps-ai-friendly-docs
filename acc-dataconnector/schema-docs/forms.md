# forms Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=forms&format=html

---

# forms Schema Description

**Documentation Updated:** 2026-02-04  

- [form_attachments](#form_attachments)
- [form_files](#form_files)
- [form_sections](#form_sections)
- [form_templates](#form_templates)
- [forms](#forms)
- [layout_section_items](#layout_section_items)
- [layout_sections](#layout_sections)
- [layout_table_columns](#layout_table_columns)
- [layouts](#layouts)
- [native_form_section_item_attachments](#native_form_section_item_attachments)
- [native_form_tabular_values](#native_form_tabular_values)
- [native_form_values](#native_form_values)
- [native_forms](#native_forms)
- [weather](#weather)
- [weather_hours](#weather_hours)

## form_attachments

Defines the relation between a form and an attachment stored in the Docs service

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID of this form attachment record |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | form_id | string: UUID |  | Foreign Key: Table: forms.id The form this attachment is on Column: |
| 5 | attachment_id | string: UUID |  | Unique ID for the attachment |
| 6 | attachment_type | string |  | A Form specified type describing the attachment, e.g. form |
| 7 | item_urn | string |  | The URN for the attachment lineage in Docs. This is the attachment's unique identifier as far as Docs is concerned. |
| 8 | is_deleted | boolean |  | Indicates whether or not the attachment has been deleted. |
| 9 | updated_by | string |  | The user that last updated the attachment. |
| 10 | created_by | string |  | The user that created the attachment. |
| 11 | created_at | timestamp: SQL |  | The date the form attachment was created. |
| 12 | updated_at | timestamp: SQL |  | The date the form attachment was updated. |

## form_files

For PDF based forms, information about the PDF files

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique id for this file |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | form_id | string: UUID |  | Foreign Key: Table: forms.id Id of the form this file is associated with Column: |
| 5 | extracted_form_data | string: null |  | Data extracted from the filled PDF in JSON format |

## form_sections

The sections of a form with section assignment

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | id of this form section |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | form_uid | string: UUID |  | The uid for the form this section belongs to |
| 5 | status | string |  | The status of the form section |
| 6 | assignee_id | string |  | The assignee id the section is assigned to |
| 7 | assignee_type | string |  | The type of assignee the section is assigned to |
| 8 | created_at | timestamp: SQL |  | The date the form section as created |
| 9 | created_by | string |  | The creator of the form section |
| 10 | updated_at | timestamp: SQL |  | The date the form section was updated at |
| 11 | updated_by | string |  | The user that updated the form section |
| 12 | user_created_at | timestamp: SQL |  | The date the form section was created by the user (in the case of creating the form section offline, and using mobile sync) |
| 13 | last_completed_by | string |  | The last completed user of this form section |
| 14 | last_completed_at | timestamp: SQL |  | The last completed date of this form section |
| 15 | last_reopened_by | string |  | The last reopened user of this form section |
| 16 | last_reopened_at | timestamp: SQL |  | The last reopened date of this form section |

## form_templates

Form templates define the forms a user can fill out. These can either be smart PDFs or native.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | created_by | string |  | Who created the template |
| 2 | updated_at | timestamp: SQL |  | When the template was last updated |
| 3 | id | string: UUID |  | Unique id for this template |
| 4 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 5 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 6 | name | string |  | The name of the template |
| 7 | status | enum: string | Possible Values: active inactive deleted | The status of the template |
| 8 | file_id | string: UUID |  | Foreign Key: Table: form_files.id If this is a PDF form Column: the id of the file |
| 9 | native_form_id | string: UUID |  | Foreign Key: Table: native_forms.id Column: |
| 10 | template_type | string: null | A semi-colon separated list of these possible values: SEMI_COLON_LIST: null; pg.template_type.safety; pg.template_type.punchlist; pg.template_type.other; pg.template_type.other; pg.template_type.quality; pg.template_type.commissioning; pg.template_type.daily_report; pg.template_type.time_sheet | Template type for the form |

## forms

Instances of forms created by users. The type (pdf/native) and content is determined by the template.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique id for this form |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | template_id | string: UUID |  | Foreign Key: Table: form_templates.id The template this form is an instance of Column: |
| 5 | status | string | Possible Values: in_progress discarded closed archived in_review | The status of the form |
| 6 | assignee_id | string |  | Who the form is assigned to - this field is deprecated and you should use assignee_type and assignee_type_id |
| 7 | number | number |  | User facing report number |
| 8 | form_date | date: string |  | The date set on the form |
| 9 | notes | string: null |  | User filled notes |
| 10 | description | string: null |  | User filled description |
| 11 | weather_id | number |  | Foreign Key: Table: weather.id Weather associated with form Column: |
| 12 | native_form_id | string: UUID |  | For native forms, FK to form data |
| 13 | file_id | string: UUID |  | Foreign Key: Table: form_files.id For PDF forms Column: information about the PDF file |
| 14 | created_by | string |  | Who created the form |
| 15 | updated_at | timestamp: SQL |  | When was the form last updated |
| 16 | location_id | string: UUID |  | Foreign Key: Table: locations.nodes.external_id Reference to the location associated with the form. Column: |
| 17 | last_reopened_by | string: UUID |  | Who last reopened a form |
| 18 | last_submitter_signature | string: null |  | User filled signature |
| 19 | due_date | date: string |  | The date the form is due, may be null. |
| 20 | created_at | timestamp: SQL |  | The date the form was created |
| 21 | last_submitted_at | timestamp: SQL |  | The date the form was submitted on |
| 22 | assignee_type_id | string |  | Who the form is assigned to - this value is the uuid of a user, company or role. The assignee_type field will indicate which. The value can then be joined on the admin.users, admin.companies or admin.roles tables respectively to retrieve information about the assignee. |
| 23 | assignee_type | string: null |  | The type of assignee - NULL is a user, 'company' is a company, 'role' is a role |
| 24 | name | string: null |  | The name of the form - nullable value - a backfill is being completed to default the value of this field to the template name |
| 25 | last_submitted_by | string |  | Who last submitted the form |

## layout_section_items

Defines the items in a layout section

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | uid | string: UUID |  | The Id of this layout section item |
| 2 | layout_uid | string: UUID |  | Foreign Key: Table: layouts.uid Foreign key to layout that this section item is a part of Column: |
| 3 | section_uid | string: UUID |  | Foreign Key: Table: layout_sections.uid Foreign key to layout section that this item is a part of Column: |
| 4 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 5 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 6 | sort_index | number |  | The index of this section item starting from 0 |
| 7 | label | string |  | The label of this section item |
| 8 | schema | string |  | Foreign Key: Table: native_form_values.field_id The schema id for this section item Column: |
| 9 | value_name | string |  | Determines the question type, also the value name that should be used to answer the field. |
| 10 | description | string |  | The text to use to describe this value. |
| 11 | is_required | boolean |  | Determines if the question must be filled before a form can be submitted. |
| 12 | modifier | string |  | For toggle_val fields, determines the display words used for the question (Yes/No/NA vs True/False/NA vs ...)\nFor choice_val fields, determines if it displays as a dropdown (default radio buttons) |
| 13 | presets | string |  | For array_val / choice_val |
| 14 | type | string |  | What type of UI component should be generated for this Element. One of `field` or `table`. |
| 15 | display_index | number |  | The section item number, if it exists |
| 16 | field_id_v2 | string: UUID |  | Foreign Key: Table: native_form_values.field_id The schema id for this section item. (Historically named schema or field_id Column: but now renamed to field_id_v2 to be consistent across tables.) |

## layout_sections

Defines the sections of a layout

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | uid | string: UUID |  | Id of this layout section record |
| 2 | layout_uid | string: UUID |  | Foreign Key: Table: layouts.uid Foreign key to layout that this section is a part of Column: |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 5 | sort_index | number |  | The index of this section starting from 0 |
| 6 | label | string |  | The label for this section |
| 7 | description | string |  | The description of this section |
| 8 | form_section_id | string: UUID |  | Foreign Key: Table: form_sections.id Foreign key to layout that these sections are a part of Column: |
| 9 | assignee_id | string |  | The assignee id the section is assigned to |
| 10 | assignee_type | string |  | The type of assignee the section is assigned to |
| 11 | display_index | number |  | the section number, if it exists |

## layout_table_columns

Defines the items in a layotu section

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | uid | string: UUID |  | The Id of this layout table column |
| 2 | layout_uid | string: UUID |  | Foreign Key: Table: layouts.uid Foreign key to layout that this table column are a part of Column: |
| 3 | section_item_uid | string: UUID |  | Foreign Key: Table: layout_section_items.uid Foreign key to layout section that this column is a part of Column: |
| 4 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 5 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 6 | sort_index | number |  | The index of this table column starting from 0 |
| 7 | presets | string |  | Autocomplete or drop-down options |
| 8 | value_name | string |  | If an Element has a value_name attribute, the value displayed is to be bound to the corresponding value in the values segment. |
| 9 | values_provider | string |  | If set, only data from the indicated source will be allowed (companies: project companies, roles: account roles, presets: the presets field list) |
| 10 | label | string |  | The text to use to describe this value. |
| 11 | column_key | string |  | A string that is unique to the table. Must be alpha-numeric characters only and starts with a lower case non-numeric character. The column_key can be referred to in expressions for calculations. |
| 12 | column_type | string |  | The data type of the column. ("text_val", "number_val", "integer_val", "array_val", "uid_val", "svg_val", "date_val", "time_val", "timespan_val") |
| 13 | expression | string |  | The expression string of the column, if the column is a calculated field. |

## layouts

Defines the layout of a native form template

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | uid | string: UUID |  | Id of this layout record |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | description | string |  | Description of the layout |
| 5 | has_section_assignees | boolean |  | Indicates that this layout has section assignees |
| 6 | created_at | timestamp: SQL |  | The date the layout was created |
| 7 | created_by | string |  | The creator of the layout |
| 8 | updated_at | timestamp: SQL |  | The date the layout was updated |
| 9 | updated_by | string |  | The user that updated the layout |
| 10 | user_created_at | timestamp: SQL |  | The date the form section was created by the user (in the case of creating the form section offline, and using mobile sync) |
| 11 | sequential_section_completion | boolean |  | Indicates that this layout has sequential section completion enabled |

## native_form_section_item_attachments

Defines the relation between a Form and an attachment stored in the Docs service

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | ID of this form field attachment record |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | native_form_id | string: UUID |  | Foreign Key: Table: native_forms.id The native form this attachment is on Column: |
| 5 | section_item_uid | string: UUID |  | Foreign Key: Table: layout_section_items.uid The section item this attachment is on Column: |
| 6 | attachment_id | string: UUID |  | Unique ID for the attachment |
| 7 | attachment_type | string |  | A Form specified type describing the attachment, e.g. form-field |
| 8 | item_urn | string |  | The URN for the attachment lineage in Docs. This is the attachment's unique identifier as far as Docs is concerned. |
| 9 | is_deleted | boolean |  | Indicates whether or not the attachment has been deleted. |
| 10 | updated_by | string |  | The user that last updated the attachment. |
| 11 | created_by | string |  | The user that created the attachment. |
| 12 | created_at | timestamp: SQL |  | The date the form attachment was created. |
| 13 | updated_at | timestamp: SQL |  | The date the form attachment was updated. |

## native_form_tabular_values

Stores user answers to tables

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | native_form_id | string: UUID |  | Foreign Key: Table: forms.native_form_id Foreign key to the id of the native form Column: |
| 2 | layout_table_column_id | string: UUID |  | Foreign Key: Table: layout_table_columns.uid Foreign key to the column uid Column: |
| 3 | layout_section_item_id | string: UUID |  | Foreign Key: Table: layout_section_items.uid Foreign key to the section item Column: |
| 4 | native_form_value_id | string: UUID |  | Foreign Key: Table: native_form_values.id Foreign key to unique id for value Column: |
| 5 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. This column is added to enable simple data extraction by the Data |
| 6 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 7 | field_id | string |  | The schema id for this section item |
| 8 | text_val | string: null |  | The text value for the table cell |
| 9 | number_val | number |  | The number (decimal) value of for the table cell |
| 10 | integer_val | number |  | The integer value for the table cell |
| 11 | array_val | string: null |  | The array (multi-select) value for the table cell |
| 12 | uid_val | string: UUID |  | The uid (UserIds, RoleIds, GroupIds) value for the table cell |
| 13 | svg_val | string: null |  | The svg (signature) value for the table cell |
| 14 | timespan_val | string |  | The timespan value for the table cell |
| 15 | datetime_local_val | timestamp: SQL |  | The datetime (local) value for the table cell |
| 16 | datetime_utc_val | timestamp: SQL |  | The datetime (utc) value for the table cell |
| 17 | timezone_val | string: null |  | The timezone value for the table cell |
| 18 | lat_val | number |  | The latitude value for the table cell |
| 19 | lng_val | number |  | The longitude value for the table cell |
| 20 | created_at | timestamp: SQL |  | The date the tabular value was created |
| 21 | created_by | string |  | The creator of the tabular value |
| 22 | updated_at | timestamp: SQL |  | The date the tabular value was updated |
| 23 | updated_by | string |  | The user that updated the tabular value |
| 24 | date_val | date: string |  | The date value (without timezone) for the table cell |
| 25 | time_val | time |  | The time value for the table cell |
| 26 | field_id_v2 | string: UUID |  | The schema id for this section item. (Historically named schema or field_id, but is now field_id_v2 to be consistent across tables.) |

## native_form_values

Stores users answers to native form questions

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique id for the value |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | native_form_id | string: UUID |  | Foreign Key: Table: native_forms.id Id of the native form the value belongs to Column: |
| 5 | rank | number |  | The display order of this row. Rows are displayed sorted by rank Integer. Not guaranteed to be gapless (e.g. if we have 2 rows with ranks 5 , 7, clients should display only 2 rows with no gaps). Also, not guarenteed to be unique. This allows for a row to be deleted without updating the rank of all subsequent rows. |
| 6 | field_id | string |  | Identifier for an item in a form (not necessairly a UID) may refer to a table or individual question, depending on the case there may be multiple value rows. These ids can be used to aggregate results, some ids may be consistant between different templates. |
| 7 | notes | string: null |  | Notes added to a response |
| 8 | name | string: null |  | For signatures, the text name of the signer; For tables, the "fallback" company name of the associated company_id |
| 9 | svg_val | string: null |  | For signatures: SVG image of signature |
| 10 | array_val | string: null |  | For multi-select answers: array of selected answer values |
| 11 | number_val | number |  | For numeric answers: number value |
| 12 | text_val | string: null |  | For text answers: answer value |
| 13 | choice_val | string: null |  | For single-select answers: answer value |
| 14 | toggle_val | number |  | For toggle answers: 0 - false/no/minus, 1 - true/yes/plus, 2 - NA |
| 15 | date_val | date: string |  | For date answers: date value |
| 16 | description | string: null |  | For tables: description of the row |
| 17 | item | string: null |  | For material and equipment logs: name of the thing |
| 18 | quantity | number |  | For material and equipment logs: how many things |
| 19 | unit | string: null |  | For material logs: what measurement unit is quantity in |
| 20 | timespan | string |  | For work and equipment logs: the amount of time |
| 21 | trade | string: null |  | For worklogs: the name of the trade or crew |
| 22 | headcount | number |  | For work logs: how many people |
| 23 | company_id | string: UUID |  | For tables: company to which the crew members performing the logged work belong |
| 24 | role_id | string: UUID |  | For tables: role of the crew members performing the logged work |
| 25 | ot_timespan | string: null |  | For work and equipment logs: the amount of overtime |
| 26 | role_name | string: null |  | For tables: the "fallback" role name of the associated role_id |
| 27 | updated_at | timestamp: SQL |  | For tables: The date the form value was updated. |
| 28 | updated_by | string |  | For tables: The user that updated the form value |
| 29 | field_id_v2 | string: UUID |  | Identifier for an item in a form may refer to a table or individual question, depending on the case there may be multiple value rows. These ids can be used to aggregate results, some ids may be consistant between different templates. (Historically named schema or field_id, but is now field_id_v2 to be consistent across tables.) |

## native_forms

Defines a native form e.g. the layout specifies the sections, questions, and other metadata.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | updated_at | timestamp: SQL |  | When the form was last updated |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | id | string: UUID |  | Unique id for this native form |
| 5 | template_id | string: UUID |  | Foreign Key: Table: native_forms.id For native_forms of form instances (not templates) this is a foreign key to the native_form that defined the template when the form instance was created. This may be different from the current native form that defines the template Column: if the template has been edited. |
| 6 | layout_uid | string: UUID |  | Foreign Key: Table: layouts.uid For native_forms of form templates (not instances) this is a foreign key to the layout that defines the template. Column: |

## weather

The daily weather information for forms with weather enabled

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | Id of this weather record |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | date | date: string |  | Date of the weather event |
| 5 | summary_key | string: null | A semi-colon separated list of these possible values: SEMI_COLON_LIST: null;snow;cloudy;sleet;clear;partly-cloudy;rain;wind;fog | Summary of the weather |
| 6 | temperature_min | number |  | Minimum temperature of day in fahrenheit |
| 7 | temperature_max | number |  | Maximum temperature of the day in fahrenheit |
| 8 | humidity | number |  | A percentage value indicating the humidity over the course of the day. |
| 9 | wind_speed | number |  | The average wind speed observed throughout the day in miles per hour |
| 10 | wind_gust | number |  | The maximum wind speed observed throughout the day in miles per hour |
| 11 | wind_bearing | number |  | The direction the wind is coming from - north is 0 degrees, progressing clockwise |
| 12 | fetched_at | timestamp: SQL |  | When the weather was fetched from weather service provider |
| 13 | precipitation_accumulation | number |  | The amount of precipitation accumulated throughout the day in inches |

## weather_hours

The hourly weather information for forms with weather enabled

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | weather_id | number |  | Foreign Key: Table: weather.id Foreign key to weather of the day these hours are part of Column: |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | hour | time |  | Time of day this weather row is for |
| 5 | summary_key | string: null | A semi-colon separated list of these possible values: SEMI_COLON_LIST: null;snow;cloudy;sleet;clear;partly-cloudy;rain;wind;fog | Summary of the weather |
| 6 | temp | number |  | Temperature in fahrenheit |
| 7 | wind_speed | number |  | The average wind speed observed throughout the day in miles per hour |
| 8 | wind_bearing | number |  | The direction the wind is coming from - north is 0 degrees, progressing clockwise |
| 9 | humidity | number |  | A percentage value indicating the humidity |
| 10 | fetched_at | timestamp: SQL |  | When the weather was fetched from weather service provider |
| 11 | created_at | timestamp: SQL |  | When the row was created |
| 12 | updated_at | timestamp: SQL |  | When the row was updated |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
