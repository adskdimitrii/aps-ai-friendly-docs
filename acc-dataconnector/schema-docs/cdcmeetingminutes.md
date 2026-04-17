# cdcmeetingminutes Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=cdcmeetingminutes&format=html

---

# cdcmeetingminutes Schema Description

**Documentation Updated:** 2025-12-08  

- [assignees](#assignees)
- [attachments](#attachments)
- [items](#items)
- [meetings](#meetings)
- [non_member_participants](#non_member_participants)
- [participants](#participants)
- [topics](#topics)

**Beta Release**  
This is a Beta release of the cdcmeetingminutes data set and schema definitions are subject to change or even possibly be removed from the final data set release. Thank you for your understanding with any future schema updates.

## assignees

Item Assignments - This is the Change Data Capture (CDC) enabled version of the meetingminutes.assignees table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | id |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 3 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | item_id | string: UUID |  | Item id which this assignment refer to Foreign Key: Table: items Column: id |
| 5 | participant_id | string: UUID |  | Assigned participant id Foreign Key: Table: participants Column: id |
| 6 | non_member_participant_id | string: UUID |  | Assigned non-membmer-participant id Foreign Key: Table: non_member_participants Column: id |
| 7 | created_at | timestamp: SQL |  | Creation time Column used for filtering Date Range Extraction requests |
| 8 | updated_at | timestamp: SQL |  | Update time Column used for filtering Date Range Extraction requests |
| 9 | deleted_at | timestamp: SQL |  | Deletion time Column used for filtering Date Range Extraction requests |
| 10 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## attachments

BIM 360 only - Meeting/item Attachments - This is the Change Data Capture (CDC) enabled version of the meetingminutes.attachments table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | id |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 3 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | item_id | string: UUID |  | Item id Foreign Key: Table: items Column: id |
| 5 | meeting_id | string: UUID |  | meeting id Foreign Key: Table: meetings Column: id |
| 6 | uri | string |  | uri of the attachment |
| 7 | origin | enum: string | Possible Values: docs | origin of the attachent (docs, photos, google photos, etc..) |
| 8 | name | string |  | attachment's name |
| 9 | created_by | string |  | user id which created this resource |
| 10 | updated_by | string |  | user id which last updated this resource |
| 11 | created_at | timestamp: SQL |  | Creation time Column used for filtering Date Range Extraction requests |
| 12 | updated_at | timestamp: SQL |  | Update time Column used for filtering Date Range Extraction requests |
| 13 | deleted_at | timestamp: SQL |  | Deletion time Column used for filtering Date Range Extraction requests |
| 14 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## items

Meeting items - This is the Change Data Capture (CDC) enabled version of the meetingminutes.items table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | id |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 3 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | topic_id | string: UUID |  | topic id Foreign Key: Table: topics Column: id |
| 5 | order_index | number |  | order index of the item in its topic |
| 6 | description | string |  | Item's content |
| 7 | status | enum: string | Possible Values: open closed | item's status |
| 8 | cross_series_id | string: UUID |  | item's series id, all followup items have same series id |
| 9 | due_date | timestamp: SQL |  | item's due date |
| 10 | created_by | string |  | user id which created this resource |
| 11 | updated_by | string |  | user id which last updated this resource |
| 12 | created_at | timestamp: SQL |  | Creation time Column used for filtering Date Range Extraction requests |
| 13 | updated_at | timestamp: SQL |  | Update time Column used for filtering Date Range Extraction requests |
| 14 | deleted_at | timestamp: SQL |  | Deletion time Column used for filtering Date Range Extraction requests |
| 15 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## meetings

Meetings - This is the Change Data Capture (CDC) enabled version of the meetingminutes.meetings table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | id |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 3 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | series_id | string: UUID |  | meeting's series id, all followup meetings have same series id |
| 5 | title | string |  | meeting's title |
| 6 | description | string |  | meeting's description/agenda |
| 7 | summary | string |  | meeting's summary |
| 8 | status | enum: string | Possible Values: open minutes | meeting's status |
| 9 | num_in_series | number |  | meeting's index in the series |
| 10 | meeting_location | string |  | meetings location, free text |
| 11 | starts_at | timestamp: SQL |  | meeting's beginning time |
| 12 | duration | number |  | meeting's duration |
| 13 | video_conference_link | string |  | link for the video conference |
| 14 | created_by | string |  | user id which created this resource |
| 15 | updated_by | string |  | user id which last updated this resource |
| 16 | created_at | timestamp: SQL |  | Creation time Column used for filtering Date Range Extraction requests |
| 17 | updated_at | timestamp: SQL |  | Update time Column used for filtering Date Range Extraction requests |
| 18 | deleted_at | timestamp: SQL |  | Deletion time Column used for filtering Date Range Extraction requests |
| 19 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## non_member_participants

Meeting non-membmer-participants - participants that doen't have oxygen id - This is the Change Data Capture (CDC) enabled version of the meetingminutes.non_member_participants table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | id |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 3 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | meeting_id | string: UUID | multi-column unquie | meeting id Foreign Key: Table: meetings Column: id |
| 5 | first_name | string |  | participant's first name |
| 6 | last_name | string |  | participant's last name |
| 7 | company | string |  | participant's company name |
| 8 | email | string |  | participant's email |
| 9 | status | enum: string | Possible Values: present missing | participant's status |
| 10 | created_by | string |  | user id which created this resource |
| 11 | updated_by | string |  | user id which last updated this resource |
| 12 | created_at | timestamp: SQL |  | Creation time Column used for filtering Date Range Extraction requests |
| 13 | updated_at | timestamp: SQL |  | Update time Column used for filtering Date Range Extraction requests |
| 14 | deleted_at | timestamp: SQL |  | Deletion time Column used for filtering Date Range Extraction requests |
| 15 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## participants

Meeting participants - This is the Change Data Capture (CDC) enabled version of the meetingminutes.participants table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | id |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 3 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | meeting_id | string: UUID |  | meeting id Foreign Key: Table: meetings Column: id |
| 5 | autodesk_id | string |  | user autodesk(oxygen) id |
| 6 | type | enum: string | Possible Values: organizer invitee | indicate if user is meeitng's organizer or invitee |
| 7 | status | enum: string | Possible Values: present missing | participant's status |
| 8 | created_by | string |  | user id which created this resource |
| 9 | updated_by | string |  | user id which last updated this resource |
| 10 | created_at | timestamp: SQL |  | Creation time Column used for filtering Date Range Extraction requests |
| 11 | updated_at | timestamp: SQL |  | Update time Column used for filtering Date Range Extraction requests |
| 12 | deleted_at | timestamp: SQL |  | Deletion time Column used for filtering Date Range Extraction requests |
| 13 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## topics

Meeting topics - This is the Change Data Capture (CDC) enabled version of the meetingminutes.topics table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | id |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 3 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | meeting_id | string: UUID |  | meeting id Foreign Key: Table: meetings Column: id |
| 5 | order_index | number |  | order index of the item in its meeting |
| 6 | name | string |  | topic's title/description |
| 7 | created_by | string |  | user id which created this resource |
| 8 | updated_by | string |  | user id which last updated this resource |
| 9 | created_at | timestamp: SQL |  | Creation time Column used for filtering Date Range Extraction requests |
| 10 | updated_at | timestamp: SQL |  | Update time Column used for filtering Date Range Extraction requests |
| 11 | deleted_at | timestamp: SQL |  | Deletion time Column used for filtering Date Range Extraction requests |
| 12 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
