# schedule Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=schedule&format=html

---

# schedule Schema Description

**Documentation Updated:** 2026-03-10  

- [activities](#activities)
- [activity_codes](#activity_codes)
- [comments](#comments)
- [dependencies](#dependencies)
- [plan_commitments](#plan_commitments)
- [plan_handoffs](#plan_handoffs)
- [plan_plans](#plan_plans)
- [plan_project_settings](#plan_project_settings)
- [plan_task_comments](#plan_task_comments)
- [plan_tasks](#plan_tasks)
- [resources](#resources)
- [schedules](#schedules)

## activities

Schedule activities belonging to the latest schedule revision

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
| 29 | created_at | timestamp: SQL |  | Creation time of the activity |
| 30 | updated_at | timestamp: SQL |  | Update time of the activity |
| 31 | wbs_path_text | string: null |  | The WBS Path of the activity, constracted from names, string array |

## activity_codes

Activity codes (Custom attributes) assignments to Activities belonging to the latest schedule revision

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
| 9 | created_at | timestamp: SQL |  | Creation time of the activity code |
| 10 | updated_at | timestamp: SQL |  | Update time of the activity code |

## comments

Schedule update requests status changes

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The comment ID |
| 2 | schedule_id | string: UUID |  | The update request id for the status change request Foreign Key: Table: schedules Column: id |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 5 | activity_unique_id | number |  | The activity unique id in the User's scheduling software |
| 6 | body | string | Max length: 10000 | The comment text |
| 7 | created_by | string |  | User who created the comment |
| 8 | created_at | timestamp: SQL |  | Creation time of the comment |

## dependencies

Activity dependencies (links) belonging to the latest schedule revision

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The dependency ID |
| 2 | schedule_id | string: UUID |  | The schedules ID for the revision Foreign Key: Table: schedules Column: id |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 5 | source_unique_id | number |  | The source activity unique id of the dependency |
| 6 | target_unique_id | number |  | The target activity unique id of the dependency |
| 7 | type | enum: string | ENUM VALUES: FINISH_FINISH, FINISH_START, START_FINISH, START_START | The type of dependency link |
| 8 | created_at | timestamp: SQL |  | Creation time of the dependency |
| 9 | updated_at | timestamp: SQL |  | Update time of the dependency |

## plan_commitments

The Workplan commitments in ACC Build

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The commitment ID |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | plan_id | string: UUID |  | The plan ID derived from the linked task Foreign Key: Table: plans Column: id |
| 5 | task_id | string: UUID |  | The task ID this commitment is made against Foreign Key: Table: tasks Column: id |
| 6 | replanned_commitment_id | string: UUID |  | The ID of the commitment this one replans Foreign Key: Table: commitments Column: id |
| 7 | root_cause_id | string: UUID |  | The root cause ID when commitment is incomplete |
| 8 | task_type | string |  | The task type of the commitment |
| 9 | work_type | string |  | The work type of the commitment |
| 10 | status | string |  | The current status of the commitment |
| 11 | start_date | date: string |  | The start date of the commitment |
| 12 | finish_date | date: string |  | The finish date of the commitment |
| 13 | duration | number |  | The duration value when the task was committed |
| 14 | assigned_member_id | string: null |  | The member ID assigned to the commitment |
| 15 | assigned_company_id | string: null |  | The company ID assigned to the commitment |
| 16 | assigned_role_id | string: null |  | The role ID assigned to the commitment |
| 17 | location_id | string: UUID |  | The location ID associated with the commitment |
| 18 | wbs_id | string: UUID |  | The WBS ID associated with the commitment |
| 19 | crew_size | number |  | The crew size committed to the task |
| 20 | was_start_changed | boolean |  | Whether the start date was changed from the original task |
| 21 | was_duration_changed | boolean |  | Whether the duration was changed from the original task |
| 22 | was_finish_changed | boolean |  | Whether the finish date was changed from the original task |
| 23 | created_by | string |  | The user who created the commitment |
| 24 | created_at | timestamp: SQL |  | Creation time of the commitment |
| 25 | updated_by | string |  | The user who last updated the commitment |
| 26 | updated_at | timestamp: SQL |  | Last update time of the commitment |

## plan_handoffs

The Workplan task handoffs in ACC Build

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The handoff ID |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | plan_id | string: UUID |  | The plan ID this handoff belongs to Foreign Key: Table: plans Column: id |
| 5 | source_task | string: UUID |  | The source task ID of the handoff Foreign Key: Table: tasks Column: id |
| 6 | target_task | string: UUID |  | The target task ID of the handoff Foreign Key: Table: tasks Column: id |
| 7 | created_by | string |  | The user who created the handoff |
| 8 | created_at | timestamp: SQL |  | Creation time of the handoff |
| 9 | updated_by | string |  | The user who last updated the handoff |
| 10 | updated_at | timestamp: SQL |  | Last update time of the handoff |

## plan_plans

The Workplan plans in ACC Build

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The plan ID |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | name | string |  | The plan name |
| 5 | schedule_id | string: UUID |  | The connected schedule ID for the plan Foreign Key: Table: schedules Column: id |
| 6 | created_by | string |  | The user who created the plan |
| 7 | updated_by | string |  | The user who last updated the plan |
| 8 | created_at | timestamp: SQL |  | Creation time of the plan |
| 9 | updated_at | timestamp: SQL |  | Last update time of the plan |

## plan_project_settings

The Workplan project settings in ACC Build

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | non_working_dates | string |  | Non-working dates configured for the project (JSON array) |
| 4 | first_day_of_the_week | string: null |  | The first day of the project working week |
| 5 | working_days | string: null |  | The project working days configuration |
| 6 | wbs_tree | string |  | The WBS tree structure for the project (JSON) |
| 7 | created_by | string |  | The user who created the project settings |
| 8 | created_at | timestamp: SQL |  | Creation time of the project settings |
| 9 | updated_by | string |  | The user who last updated the project settings |
| 10 | updated_at | timestamp: SQL |  | Last update time of the project settings |

## plan_task_comments

The Workplan tasks comments in ACC Build

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The task comments ID |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | task_id | string: UUID |  | The task ID for the task comment Foreign Key: Table: tasks Column: id |
| 5 | plan_id | string: UUID |  | The plan ID for the task comment Foreign Key: Table: plans Column: id |
| 6 | body | string |  | The body of the task comment |
| 7 | created_at | timestamp: SQL |  | Creation time of the task comment |
| 8 | created_by | string |  | The user who created the task comment |

## plan_tasks

The Workplan tasks in ACC Build

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The task ID |
| 2 | plan_id | string: UUID |  | The plan ID this task belongs to Foreign Key: Table: plans Column: id |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 5 | parent_task_id | string: UUID |  | The parent task ID for hierarchical task structures Foreign Key: Table: tasks Column: id |
| 6 | activity_unique_id | number |  | The task's connected schedule activity id Foreign Key: Table: schedule_activities Column: unique_id |
| 7 | unique_id | number |  | The unique sequential identifier of the task within the plan |
| 8 | task_type | string |  | The task type (e.g. task, milestone) |
| 9 | work_type | string |  | The work type of the task |
| 10 | status | string |  | The current status of the task |
| 11 | title | string |  | the task title |
| 12 | description | string |  | The task description |
| 13 | start_date | date: string |  | The start date of the task |
| 14 | finish_date | date: string |  | The finish date of the task |
| 15 | duration | number |  | The duration of the task in working days |
| 16 | location_id | string: UUID |  | The location ID associated with the task |
| 17 | assigned_member_id | string: null |  | The member ID assigned to the task |
| 18 | assigned_company_id | string: null |  | The company ID assigned to the task |
| 19 | assigned_role_id | string: null |  | The role ID assigned to the task |
| 20 | wbs_id | string: UUID |  | The WBS ID associated with the task |
| 21 | completion_percentage | number |  | The completion percentage of the task (0-100) |
| 22 | crew_size | number |  | The crew size assigned to the task |
| 23 | priority | number |  | The priority of the task |
| 24 | comments_count | number |  | The number of comments on the task |
| 25 | commitments_count | number |  | The total number of commitments and replans of the task |
| 26 | task_imports_id | string |  | The import ID if the task was imported from Excel |
| 27 | created_by | string |  | The user who created the task |
| 28 | created_at | timestamp: SQL |  | Creation time of the task |
| 29 | updated_by | string |  | The user who last updated the task |
| 30 | updated_at | timestamp: SQL |  | Last update time of the task |

## resources

Resource (Assignees) assignments to Activities belonging to the latest schedule revision

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
| 10 | created_at | timestamp: SQL |  | Creation time of the resource |
| 11 | updated_at | timestamp: SQL |  | Update time of the resource |

## schedules

Schedules in ACC Build

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
| 10 | created_at | timestamp: SQL |  | Creation time of the schedule |
| 11 | updated_at | timestamp: SQL |  | Update time of the schedule |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
