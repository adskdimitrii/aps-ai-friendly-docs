# Activities Data Set Verb Descriptions: RFIs

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=activities_rfis_verb_column_details&format=html

---

# Activities Data Set Verb Descriptions: RFIs

The Activities data set is more complex than the average ACC Data Schema data set due to the variable nature of payloads associated with the various "Activity Verbs" which define the particular activity
taken in the system. For the Activities schema, there are several tables defined (one for each service) and for each of these table definitions, there are common columns
and then many unique columns based on the particular service. The common columns included for all tables are:

- **activity_id:** Activity ID for this event
- **bim360_account_id:** BIM 360 HQ Account ID
- **bim360_project_id:** BIM 360 HQ Project ID
- **activity_verb:** Activity performed by the user
- **created_by:** Autodesk ID of the user performing the activity action
- **created_at:** The timestamp when the activity created
After these standard columns there are many service specific columns for the table definition. Columns may or many not contain data depending on the Activity Verb
in question. The following summary details the particular columns applicable for an Activity Verb. Also, for certain Activity Verbs there are Related Tables (in a SQL relational sense) that can be associated with the verb. These tables use the **activity_id** as
the foreign key for lookups and when there is an applicable foreign table, they are noted in the details below.

This description information is also made available programatically in the format of JSON files (one for each Activities table) in the **"schemas"** directory as part of every
extract archive. The naming convention for this file is:

-

```
activities_<service_group>_verb_column_details.json
```

The description file is an array of JSON objects with two primary fields:

- **columns:** Relevant columns for the verb
- **related_tables:** any tables with additional information on the verb in question
The following is an example JSON snippet from the Docs description file.

```
{
  "activate-approval-workflow" : {
     "columns" : [
        "activity_id",
        "bim360_account_id",
        "bim360_project_id",
        "created_by",
        "created_at",
        "activity_verb",
        "object_display_name",
        "object_id",
        "object_object_type"
     ]
  },
  "add-attribute-to-namingstandard" : {
     "columns" : [
        "activity_id",
        "bim360_account_id",
        "bim360_project_id",
        "created_by",
        "created_at",
        "activity_verb",
        "object_display_name",
        "object_id",
        "object_object_type"
     ],
     "related_tables" : [
        "docs_naming_standards"
     ]
  },
  ...

```

## Activity Verbs

Now that we have reviewed the data description for Activities data, the following is a detailed summary of 9 Activity Verbs for
 the RFIs Schema along with their relevant columns and any related tables.

| attachment-create attachment-delete comment-create | response-create response-update rfi-create | rfi-create-with-ai rfi-update rfi-view |  |
| --- | --- | --- | --- |
|  |

| activity_verb | relevant_columns | related_tables |
| --- | --- | --- |
| attachment-create | activity_id Activity ID for this event bim360_account_id BIM 360 HQ Account ID. bim360_project_id BIM 360 HQ Project ID. created_by Autodesk ID of the user performing the activity action created_at The timestamp when the activity created activity_verb Activity performed by the user object_display_name RFI display name object_id ID of the RFI | activity_id | Activity ID for this event | bim360_account_id | BIM 360 HQ Account ID. | bim360_project_id | BIM 360 HQ Project ID. | created_by | Autodesk ID of the user performing the activity action | created_at | The timestamp when the activity created | activity_verb | Activity performed by the user | object_display_name | RFI display name | object_id | ID of the RFI |  |
| attachment-delete |  |  |
| comment-create | activity_id Activity ID for this event bim360_account_id BIM 360 HQ Account ID. bim360_project_id BIM 360 HQ Project ID. created_by Autodesk ID of the user performing the activity action created_at The timestamp when the activity created activity_verb Activity performed by the user object_comment_body Comment body for the RFI Comment object_comment_id Comment ID for the RFI Comment object_comment_mentions Mentions for the RFI Comment object_comment_rfi_id ID of the RFI Comment object_comment_source Source client of the RFI Comment object_display_name RFI display name object_id ID of the RFI | activity_id | Activity ID for this event | bim360_account_id | BIM 360 HQ Account ID. | bim360_project_id | BIM 360 HQ Project ID. | created_by | Autodesk ID of the user performing the activity action | created_at | The timestamp when the activity created | activity_verb | Activity performed by the user | object_comment_body | Comment body for the RFI Comment | object_comment_id | Comment ID for the RFI Comment | object_comment_mentions | Mentions for the RFI Comment | object_comment_rfi_id | ID of the RFI Comment | object_comment_source | Source client of the RFI Comment | object_display_name | RFI display name | object_id | ID of the RFI |  |
| response-create | activity_id Activity ID for this event bim360_account_id BIM 360 HQ Account ID. bim360_project_id BIM 360 HQ Project ID. created_by Autodesk ID of the user performing the activity action created_at The timestamp when the activity created activity_verb Activity performed by the user object_display_name RFI display name object_id ID of the RFI | activity_id | Activity ID for this event | bim360_account_id | BIM 360 HQ Account ID. | bim360_project_id | BIM 360 HQ Project ID. | created_by | Autodesk ID of the user performing the activity action | created_at | The timestamp when the activity created | activity_verb | Activity performed by the user | object_display_name | RFI display name | object_id | ID of the RFI |  |
| response-update | activity_id Activity ID for this event bim360_account_id BIM 360 HQ Account ID. bim360_project_id BIM 360 HQ Project ID. created_by Autodesk ID of the user performing the activity action created_at The timestamp when the activity created activity_verb Activity performed by the user object_display_name RFI display name object_id ID of the RFI | activity_id | Activity ID for this event | bim360_account_id | BIM 360 HQ Account ID. | bim360_project_id | BIM 360 HQ Project ID. | created_by | Autodesk ID of the user performing the activity action | created_at | The timestamp when the activity created | activity_verb | Activity performed by the user | object_display_name | RFI display name | object_id | ID of the RFI |  |
| rfi-create | activity_id Activity ID for this event bim360_account_id BIM 360 HQ Account ID. bim360_project_id BIM 360 HQ Project ID. created_by Autodesk ID of the user performing the activity action created_at The timestamp when the activity created activity_verb Activity performed by the user object_display_name RFI display name object_id ID of the RFI | activity_id | Activity ID for this event | bim360_account_id | BIM 360 HQ Account ID. | bim360_project_id | BIM 360 HQ Project ID. | created_by | Autodesk ID of the user performing the activity action | created_at | The timestamp when the activity created | activity_verb | Activity performed by the user | object_display_name | RFI display name | object_id | ID of the RFI |  |
| rfi-create-with-ai | activity_id Activity ID for this event bim360_account_id BIM 360 HQ Account ID. bim360_project_id BIM 360 HQ Project ID. created_by Autodesk ID of the user performing the activity action created_at The timestamp when the activity created activity_verb Activity performed by the user object_display_name RFI display name object_id ID of the RFI | activity_id | Activity ID for this event | bim360_account_id | BIM 360 HQ Account ID. | bim360_project_id | BIM 360 HQ Project ID. | created_by | Autodesk ID of the user performing the activity action | created_at | The timestamp when the activity created | activity_verb | Activity performed by the user | object_display_name | RFI display name | object_id | ID of the RFI |  |
| rfi-update | activity_id Activity ID for this event bim360_account_id BIM 360 HQ Account ID. bim360_project_id BIM 360 HQ Project ID. created_by Autodesk ID of the user performing the activity action created_at The timestamp when the activity created activity_verb Activity performed by the user object_display_name RFI display name object_id ID of the RFI | activity_id | Activity ID for this event | bim360_account_id | BIM 360 HQ Account ID. | bim360_project_id | BIM 360 HQ Project ID. | created_by | Autodesk ID of the user performing the activity action | created_at | The timestamp when the activity created | activity_verb | Activity performed by the user | object_display_name | RFI display name | object_id | ID of the RFI | rfis_changes |
| rfi-view | activity_id Activity ID for this event bim360_account_id BIM 360 HQ Account ID. bim360_project_id BIM 360 HQ Project ID. created_by Autodesk ID of the user performing the activity action created_at The timestamp when the activity created activity_verb Activity performed by the user object_display_name RFI display name object_id ID of the RFI | activity_id | Activity ID for this event | bim360_account_id | BIM 360 HQ Account ID. | bim360_project_id | BIM 360 HQ Project ID. | created_by | Autodesk ID of the user performing the activity action | created_at | The timestamp when the activity created | activity_verb | Activity performed by the user | object_display_name | RFI display name | object_id | ID of the RFI |  |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
