# clashes Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=clashes&format=html

---

# clashes Schema Description

**Documentation Updated:** 2024-11-20  

- [assigned_clash_group](#assigned_clash_group)
- [clash_group_to_clash_id](#clash_group_to_clash_id)
- [clash_test](#clash_test)
- [closed_clash_group](#closed_clash_group)

## assigned_clash_group

Group of clashes, manually classified as an issue

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | clash_group_id | string: UUID |  | Unique ID of the assigned clash group |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | issue_id | string: UUID |  | Issue Id associated with the clash clash group |
| 5 | title | string: null |  | Name of the issue |
| 6 | description | string: null |  | Description of the purpose of the issue |
| 7 | status | string: null | Possible Values: open work_completed ready_to_inspect not_approved in_dispute closed void answered draft pending in_progress completed in_review | Unique identifier of the current status of the issue |
| 8 | clash_test_id | string: UUID |  | Unique id of the clash test |
| 9 | model_set_id | string: UUID |  | A coordination space ID uniquely identifies combinations of models in a clash group, like 'scope 1' for models A & B, and 'scope 2' for models A & C. |
| 10 | created_at_model_set_version | number |  | A coordination space version number uniquely identifies varying model combinations in a clash group. For instance, 'scope version 1' could represent models A v1 & B v1, while 'scope version 2' may denote models A v1 & B v2. |
| 11 | created_at | timestamp: SQL |  | Date and time the clash group was marked as an issue |
| 12 | created_by | string |  | Autodesk ID of the user who marked the clash group as an issue. |

## clash_group_to_clash_id

List of clash ids, associated with a clash group

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | clash_group_id | string: UUID |  | Id of the issue clash group |
| 2 | clash_id | number |  | Id of the clash associated with the clash group, corresponding with the clash ID field in the clash result resources available via the API (see API documentation for more details). |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |

## clash_test

Clash Tests run by the user

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | clash_test_id | string: UUID |  | Id of the clash test |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | model_set_id | string: UUID |  | A coordination space ID uniquely identifies combinations of models in a clash test, like 'scope 1' for models A & B, and 'scope 2' for models A & C. |
| 5 | model_set_version | number |  | A coordination space version ID uniquely identifies varying model combinations in a clash test. For instance, 'scope version 1' could represent models A v1 & B v1, while 'scope version 2' may denote models A v1 & B v2. |
| 6 | root_folder_urn | string |  | Unique Resource Name of the clash test root folder |
| 7 | started_at | timestamp: SQL |  | Date and time the clash job started (UTC) |
| 8 | completed_at | timestamp: SQL |  | Date and time the clash job finished (UTC) |
| 9 | status | string | Possible Values: Pending Processing Successful Failed | The status of the clash test; Pending, Processing, Successful, Failed |
| 10 | backend_type | number | Possible Values: 0 (V1) 1 (V2) | The type of the coordination space; Projects created before November 2022 will be 0 = V1, after will be 1 = V2. Refer to Coordination Space Versions in Model Coordination help files for further information. |

## closed_clash_group

Group of clashes, manually classified as not-an-issue

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | clash_group_id | string: UUID |  | Unique ID of the clash group classified as not-an-issue |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | reason | string |  | Reason why the clash group was marked as not-an-issue |
| 5 | title | string |  | Title of the closed clash group classified as not-an-issue |
| 6 | description | string |  | Description of the closed clash group |
| 7 | clash_test_id | string: UUID |  | Unique id of the clash test |
| 8 | model_set_id | string: UUID |  | A coordination space ID uniquely identifies combinations of models in a clash group classified as not-an-issue, like 'scope 1' for models A & B, and 'scope 2' for models A & C. |
| 9 | created_at_model_set_version | number |  | A coordination space version number uniquely identifies varying model combinations in a classified as not-an-issue. For instance, 'scope version 1' could represent models A v1 & B v1, while 'scope version 2' may denote models A v1 & B v2. |
| 10 | created_at | timestamp: SQL |  | Date and time the clash group was marked as not-an-issue |
| 11 | created_by | string |  | Autodesk ID of the user who marked the clash group as not-an-issue. |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
