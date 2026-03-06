# meetingminutes Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=meetingminutes&format=html

---

# meetingminutes Schema Description

**Documentation Updated:** 2023-12-04  

- [assignees](#assignees)
- [attachments](#attachments)
- [items](#items)
- [meetings](#meetings)
- [non_member_participants](#non_member_participants)
- [participants](#participants)
- [topics](#topics)

## assignees

Item Assignments

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | id |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 3 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | item_id | string: UUID |  | Item id which this assignment refer to Foreign Key: Table: items Column: id |
| 5 | participant_id | string: UUID |  | Assigned participant id Foreign Key: Table: participants Column: id |
| 6 | non_member_participant_id | string: UUID |  | Assigned non-membmer-participant id Foreign Key: Table: non_member_participants Column: id |
| 7 | created_at | timestamp: SQL |  | Creation time |
| 8 | updated_at | timestamp: SQL |  | Update time |
| 9 | deleted_at | timestamp: SQL |  | Deletion time |

## attachments

BIM 360 only - Meeting/item Attachments

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
| 11 | created_at | timestamp: SQL |  | Creation time |
| 12 | updated_at | timestamp: SQL |  | Update time |
| 13 | deleted_at | timestamp: SQL |  | Deletion time |

## items

Meeting items

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
| 12 | created_at | timestamp: SQL |  | Creation time |
| 13 | updated_at | timestamp: SQL |  | Update time |
| 14 | deleted_at | timestamp: SQL |  | Deletion time |

## meetings

Meetings

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
| 16 | created_at | timestamp: SQL |  | Creation time |
| 17 | updated_at | timestamp: SQL |  | Update time |
| 18 | deleted_at | timestamp: SQL |  | Deletion time |

## non_member_participants

Meeting non-membmer-participants - participants that doen't have oxygen id

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
| 12 | created_at | timestamp: SQL |  | Creation time |
| 13 | updated_at | timestamp: SQL |  | Update time |
| 14 | deleted_at | timestamp: SQL |  | Deletion time |

## participants

Meeting participants

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
| 10 | created_at | timestamp: SQL |  | Creation time |
| 11 | updated_at | timestamp: SQL |  | Update time |
| 12 | deleted_at | timestamp: SQL |  | Deletion time |

## topics

Meeting topics

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
| 9 | created_at | timestamp: SQL |  | Creation time |
| 10 | updated_at | timestamp: SQL |  | Update time |
| 11 | deleted_at | timestamp: SQL |  | Deletion time |

© Copyright 2026 Autodesk Inc. | [Autodesk Construction Cloud](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
