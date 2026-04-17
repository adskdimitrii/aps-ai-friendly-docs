# reviews Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=reviews&format=html

---

# reviews Schema Description

**Documentation Updated:** 2025-07-16  

- [review_candidates](#review_candidates)
- [review_comments](#review_comments)
- [review_documents](#review_documents)
- [review_steps](#review_steps)
- [review_tasks](#review_tasks)
- [review_workflow_templates](#review_workflow_templates)
- [review_workflows](#review_workflows)
- [reviews](#reviews)
- [workflow_notes](#workflow_notes)

## review_candidates

Describes the basic information of created review steps.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The UUID of the review the step belongs to. |
| 2 | sequence_id | number |  | The sequence id of the review the step belongs to. |
| 3 | instance_id | string: UUID |  | The instance id in the workflow service. |
| 4 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 5 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 6 | step_id | string |  | The step id(every step in a review has a fixed id). |
| 7 | step_name | string |  | The step name. |
| 8 | candidate_type | enum: string | Possible Values: user role company | The candidate type. Could be a user, role or company. |
| 9 | candidate_oxygen_id | string |  | The oxygen id of the candidate. |

## review_comments

Describes the basic information of created review comments.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | PK: UUID of a review comment. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | review_document_id | string: UUID |  | Id for the review document the comment belongs to |
| 5 | created_by | string |  | Id of the user who created comment. |
| 6 | status | enum: string | Possible Values: draft submitted | The current status of the comment. |
| 7 | text | string |  | The comment text. |
| 8 | created_at | timestamp: SQL |  | Creation time of the comment. |
| 9 | updated_at | timestamp: SQL |  | Update time of the comment. |
| 10 | deleted_at | timestamp: SQL |  | Deletion time of the comment. |
| 11 | round_num | number |  | Which round the comment belongs to |

## review_documents

Describes the basic information of created review documents.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | PK: UUID of a review document. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | review_id | string: UUID |  | Id for the review the document belongs to |
| 5 | versioned_urn | string |  | The version urn of the document. |
| 6 | status | enum: string | Possible Values: approved rejected | The review status of the document. |
| 7 | created_at | timestamp: SQL |  | Creation time of the document. |
| 8 | updated_at | timestamp: SQL |  | Update time of the document. |
| 9 | round_num | number |  | Which round the document version belongs to |

## review_steps

Describes the basic information of created review steps.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The UUID of the review the step belongs to. |
| 2 | sequence_id | number |  | The sequence id of the review the step belongs to. |
| 3 | instance_id | string: UUID |  | The instance id in the workflow service. |
| 4 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 5 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 6 | workflow_id | string: UUID |  | The workflow id of a review. |
| 7 | step_id | string |  | The step id(every step in a review has a fixed id). |
| 8 | step_name | string |  | The step default name (deprecated). |
| 9 | step_display_name | string |  | The step name which is shown for users. |

## review_tasks

Describes the basic information of created review tasks.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | PK: UUID of a review task. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | review_id | string: UUID |  | Id for the review the task belongs to |
| 5 | task_id | string: UUID |  | Id of the task in the workflow service. |
| 6 | task_key | string |  | Key of the task in the workflow service. |
| 7 | name | string |  | Name of the task in the workflow service. |
| 8 | assignee | string |  | Id of the current task assignee |
| 9 | next_task_key | string |  | The next task key in the workflow service. |
| 10 | state | enum: string | Possible Values: claimed unclaimed submitted viod | The current state of the task. |
| 11 | due_date | timestamp: SQL |  | The due date of the task. |
| 12 | created_at | timestamp: SQL |  | Creation time of the task. |
| 13 | updated_at | timestamp: SQL |  | Update time of the task. |
| 14 | step_id | string |  | Id for the step the task belongs to |

## review_workflow_templates

Describes the basic information of created workflow templates.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | PK: UUID of a workflow template |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | template_id | string: UUID |  | Id to identify the template in the workflow service. |
| 5 | created_at | timestamp: SQL |  | Creation time of the template. |
| 6 | updated_at | timestamp: SQL |  | Update time of the template. |

## review_workflows

Describes the basic information of created workflows.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | PK: UUID of a review workflow |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | workflow_template_id | string: UUID |  | Id of the workflow template. |
| 5 | form_id | string: UUID |  | The form id in the workflow service. |
| 6 | name | string |  | The name of the workflow. |
| 7 | description | string |  | The description of the workflow. |
| 8 | status | enum: string | Possible Values: initiating active archived locked | The status of the workflow. |
| 9 | bpmn_urn | string |  | The urn of bpmn in the workflow serivce. |
| 10 | memo | string |  | The note of the workflow. |
| 11 | created_at | timestamp: SQL |  | Creation time of the workflow. |
| 12 | updated_at | timestamp: SQL |  | Update time of the workflow. |

## reviews

Describes the basic information of created reviews.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | PK: UUID of a review. |
| 2 | sequence_id | number |  | The sequence id of a review. |
| 3 | instance_id | string: UUID |  | The instance id in the workflow service. |
| 4 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 5 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 6 | workflow_id | string: UUID |  | The workflow id of a review. |
| 7 | status | enum: string | Possible Values: initiating open closed void failed closing processing | The status of a review. |
| 8 | review_name | string |  | The name of a review. |
| 9 | memo | string |  | The note of a review. |
| 10 | created_by | string |  | Id of user who create the review |
| 11 | next_due_date | timestamp: SQL |  | The next due date of a review. |
| 12 | created_at | timestamp: SQL |  | Creation time of the reivew. |
| 13 | updated_at | timestamp: SQL |  | Update time of the review. |
| 14 | docs_count | number |  | The count of reviewing documents of a review. |
| 15 | approved_count | number |  | The count of approved documents of a review. |
| 16 | rejected_count | number |  | The count of rejected documents of a review. |
| 17 | workflow_name | string |  | The name of a workflow. |
| 18 | started_at | timestamp: SQL |  | The time of the review started. |
| 19 | finished_at | timestamp: SQL |  | The time of the review finished. |
| 20 | next_action_candidates_users | string: null |  | List of candidate users in the next action. |
| 21 | next_action_candidates_roles | string: null |  | List of candidate roles in the next action. |
| 22 | next_action_candidates_companies | string: null |  | List of candidate companies in the next action. |
| 23 | next_action_claimed_by | string: null |  | List of users claimed the next action. |
| 24 | current_round_num | number |  | The current round number of this review |
| 25 | current_step | number |  | The current step of this review |
| 26 | total_steps | number |  | The total step of this review |
| 27 | is_archived | boolean |  | The archive status of the review |

## workflow_notes

Describes the basic information of created review notes.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | PK: UUID of a review note. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | review_id | string: UUID |  | Id for the review the note belongs to |
| 5 | created_by | string |  | Id of the user who created comment. |
| 6 | note | string |  | The comment text. |
| 7 | created_at | timestamp: SQL |  | Creation time of the comment. |
| 8 | updated_at | timestamp: SQL |  | Update time of the comment. |
| 9 | round_num | number |  | Which round the note belongs to |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
