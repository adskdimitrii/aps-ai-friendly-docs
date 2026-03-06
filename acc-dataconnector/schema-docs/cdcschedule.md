# cdcschedule Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=cdcschedule&format=html

---

# cdcschedule Schema Description

**Documentation Updated:** 2025-11-23  

- [activities](#activities)
- [activity_codes](#activity_codes)
- [comments](#comments)
- [dependencies](#dependencies)
- [resources](#resources)
- [schedules](#schedules)

**Beta Release**  
This is a Beta release of the cdcschedule data set and schema definitions are subject to change or even possibly be removed from the final data set release. Thank you for your understanding with any future schema updates.

## activities

Schedule activities belonging to the latest schedule revision - This is the Change Data Capture (CDC) enabled version of the schedule.activities table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The activity ID |
| 2 | schedule_id | string: UUID |  | The schedules ID for the activity Foreign Key: Table: schedules Column: id |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 5 | unique_id | number |  | The activity unique id in the User's scheduling software |
| 6 | sequential_id | number |  | The sequential ID of the activity |
| 7 | file_activity_id | string |  | The activity ID field in the Schedule file |
| 8 | parent_unique_id | number |  | The parent activity unique id in the User's scheduling software |
| 9 | type | enum: string | Possible Values: MILESTONE ACTIVITY | detailed column 7 description |
| 10 | name | string: null |  | The activity name |
| 11 | is_critical_path | boolean |  | Is the activity in the schedule's critical path |
| 12 | completion_percentage | number |  | The activity completion percentage |
| 13 | planned_start | timestamp: SQL |  | When the activity was planned to start |
| 14 | planned_finish | timestamp: SQL |  | When the activity was planned to finish |
| 15 | actual_start | timestamp: SQL |  | When the activity actually started |
| 16 | actual_finish | timestamp: SQL |  | When the activity actually finished |
| 17 | start | timestamp: SQL |  | A calculated field to determine the start display date of the activity |
| 18 | finish | timestamp: SQL |  | A calculated field to determine the finish display date of the activity |
| 19 | duration | number |  | The duration of the activity in days |
| 20 | actual_duration | number |  | The actual duration of the activity in days |
| 21 | remaining_duration | number |  | The remaining duration of the activity in days |
| 22 | free_slack_units | string |  | Units of the free (remaining) slack of the activity |
| 23 | free_slack_duration | number |  | The free (remaining) slack of the activity in the units in column free_slack_units |
| 24 | total_slack_units | string |  | Units of the total slack of the activity |
| 25 | total_slack_duration | number |  | The total slack of the activity in the units in column total_slack_units |
| 26 | is_wbs | boolean |  | Is the activity a WBS |
| 27 | wbs_path | string: null |  | The WBS Path of the activity, constracted from unique ids, string array // [1,2,3,4] -> "[1,2,3,4]" |
| 28 | wbs_code | string: null |  | The WBS code of the activity |
| 29 | created_at | timestamp: SQL |  | Creation time of the activity Column used for filtering Date Range Extraction requests |
| 30 | updated_at | timestamp: SQL |  | Update time of the activity Column used for filtering Date Range Extraction requests |
| 31 | wbs_path_text | string: null |  | The WBS Path of the activity, constracted from names, string array |
| 32 | deleted_at | timestamp: SQL |  | Timestamp when the activitie was deleted Column used for filtering Date Range Extraction requests |
| 33 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## activity_codes

Activity codes (Custom attributes) assignments to Activities belonging to the latest schedule revision - This is the Change Data Capture (CDC) enabled version of the schedule.activity_codes table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The activity code ID (Activity code assignment ID) |
| 2 | schedule_id | string: UUID |  | The schedule id of the activity code Foreign Key: Table: schedules Column: id |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 5 | activity_unique_id | number |  | The activity unique id in the User's scheduling software |
| 6 | name | string |  | The name of the activity code |
| 7 | value | string |  | The value code of the activity code assignment |
| 8 | value_description | string: null |  | The value free text of the activity code assignment |
| 9 | created_at | timestamp: SQL |  | Creation time of the activity code Column used for filtering Date Range Extraction requests |
| 10 | updated_at | timestamp: SQL |  | Update time of the activity code Column used for filtering Date Range Extraction requests |
| 11 | deleted_at | timestamp: SQL |  | Timestamp when the activity_code was deleted Column used for filtering Date Range Extraction requests |
| 12 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## comments

Schedule update requests status changes - This is the Change Data Capture (CDC) enabled version of the schedule.comments table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The comment ID |
| 2 | schedule_id | string: UUID |  | The update request id for the status change request Foreign Key: Table: schedules Column: id |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 5 | activity_unique_id | number |  | The activity unique id in the User's scheduling software |
| 6 | body | string | Max length: 10000 | The comment text |
| 7 | created_by | string |  | User who created the comment |
| 8 | created_at | timestamp: SQL |  | Creation time of the comment Column used for filtering Date Range Extraction requests |
| 9 | updated_at | timestamp: SQL |  | Timestamp when the comment was updated Column used for filtering Date Range Extraction requests |
| 10 | deleted_at | timestamp: SQL |  | Timestamp when the comment was deleted Column used for filtering Date Range Extraction requests |
| 11 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## dependencies

Activity dependencies (links) belonging to the latest schedule revision - This is the Change Data Capture (CDC) enabled version of the schedule.dependencies table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The dependency ID |
| 2 | schedule_id | string: UUID |  | The schedules ID for the revision Foreign Key: Table: schedules Column: id |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 5 | source_unique_id | number |  | The source activity unique id of the dependency |
| 6 | target_unique_id | number |  | The target activity unique id of the dependency |
| 7 | type | enum: string | ENUM VALUES: FINISH_FINISH, FINISH_START, START_FINISH, START_START | The type of dependency link |
| 8 | created_at | timestamp: SQL |  | Creation time of the dependency Column used for filtering Date Range Extraction requests |
| 9 | updated_at | timestamp: SQL |  | Update time of the dependency Column used for filtering Date Range Extraction requests |
| 10 | deleted_at | timestamp: SQL |  | Timestamp when the dependencie was deleted Column used for filtering Date Range Extraction requests |
| 11 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## resources

Resource (Assignees) assignments to Activities belonging to the latest schedule revision - This is the Change Data Capture (CDC) enabled version of the schedule.resources table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The resource ID (Resource assignment ID) |
| 2 | schedule_id | string: UUID |  | The schedule id of the activity code Foreign Key: Table: schedules Column: id |
| 3 | resource_unique_id | number |  | The resource unique id in the User's scheduling software |
| 4 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 5 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 6 | activity_unique_id | number |  | The activity unique id in the User's scheduling software |
| 7 | name | string |  | The name of the resource |
| 8 | type | enum: string | ENUM VALUES: WORK, COST, MATERIAL | The type of resource |
| 9 | email_address | string | Max length: 1000 | The email address of the resource |
| 10 | created_at | timestamp: SQL |  | Creation time of the resource Column used for filtering Date Range Extraction requests |
| 11 | updated_at | timestamp: SQL |  | Update time of the resource Column used for filtering Date Range Extraction requests |
| 12 | deleted_at | timestamp: SQL |  | Timestamp when the resource was deleted Column used for filtering Date Range Extraction requests |
| 13 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## schedules

Schedules in ACC Build - This is the Change Data Capture (CDC) enabled version of the schedule.schedules table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The schedule ID |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | name | string |  | The schedule name |
| 5 | type | enum: string | Possible Values: XER XML MPP PP | Schedule file type |
| 6 | version_number | number |  | The revision number of the schedule |
| 7 | is_public | boolean |  | Is the schedule available to all project members or to a restricted list of users |
| 8 | created_by | string |  | User who created the Schedule |
| 9 | updated_by | string |  | User who updated the Schedule |
| 10 | created_at | timestamp: SQL |  | Creation time of the schedule Column used for filtering Date Range Extraction requests |
| 11 | updated_at | timestamp: SQL |  | Update time of the schedule Column used for filtering Date Range Extraction requests |
| 12 | deleted_at | timestamp: SQL |  | Timestamp when the schedule was deleted Column used for filtering Date Range Extraction requests |
| 13 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

© Copyright 2026 Autodesk Inc. | [Autodesk Construction Cloud](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
