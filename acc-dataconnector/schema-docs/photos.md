# photos Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=photos&format=html

---

# photos Schema Description

**Documentation Updated:** 2024-09-10  

- [photo_tags](#photo_tags)
- [photos](#photos)
- [referencer_participants](#referencer_participants)
- [referencer_photos](#referencer_photos)

## photo_tags

Photo tags data

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | ID of the photo tag |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | seq_id | number |  | Used for sync token, the order in which columns were updated. |
| 5 | project_id | string | Max Length: 36 | The Project UID this tag applies to. |
| 6 | photo_id | string | Max Length: 36 | The Photo UID this tag applies to. |
| 7 | tag_name | string | Max Length: 64 | String that represents the tag. (EX: "stairs", "drywall", etc) |
| 8 | tag_type | string | Max Length: 255 | Type of tag, "user", "ml" (autotag), etc |
| 9 | created_at | timestamp: SQL |  | The datetime the tag was created on the server. |
| 10 | creator_id | string | Max Length: 8000 | The UID of the user who created the tag. |
| 11 | deleted_at | timestamp: SQL |  | The datetime the row was deleted, if applicable. |
| 12 | deleter_id | string | Max Length: 8000 | The UID of the user who deleted the photo, if deleted. |
| 13 | model_version | number |  | Model version for the photo |

## photos

All the photo models (Original table name is gg_photos)

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | ID of the photo |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | title | string | Max Length: 8000 | The title of the photo, which can be changed to a custom string |
| 5 | size | number |  | N/A |
| 6 | status | string | Max Length: 255 | N/A |
| 7 | annotation | string | Max Length: 36 | N/A |
| 8 | punch | string | Max Length: 36 | N/A |
| 9 | creator_id | string | Max Length: 8000 | The UID of the user who created the photo |
| 10 | deleter_id | string | Max Length: 8000 | The UID of the user who deleted the photo, if deleted. |
| 11 | updater_id | string | Max Length: 8000 | The UID of the user who most recently updated the photo. |
| 12 | lat | number |  | Latitude of the photo, if applicable. |
| 13 | lng | number |  | Longitude of the photo, if applicable. |
| 14 | uid | string | Max Length: 36 | Photo UID |
| 15 | description | string | Max Length: 512 | N/A |
| 16 | image_type | string | Max Length: 255 | N/A |
| 17 | type | string | Max Length: 8000 | N/A |
| 18 | taken_on | timestamp: SQL |  | The datetime the photo was taken at, parsed from the photo's metadata, if available. |
| 19 | locked_at | timestamp: SQL |  | N/A |
| 20 | is_public | boolean |  | Whether the photo is public to all users on a project, or uses permissions. |
| 21 | created_at | timestamp: SQL |  | The datetime the photo was uploaded to the server. |
| 22 | user_created_at | timestamp: SQL |  | The datetime the photo was added to the project locally (on mobile devices, before uploading to the cloud). |
| 23 | updated_on | timestamp: SQL |  | The datetime the row was last updated. |
| 24 | deleted_at | timestamp: SQL |  | The datetime the row was deleted, if applicable. |
| 25 | project | string | Max Length: 36 | The Project UID this tag applies to. |
| 26 | seq_id | number |  | Used for sync token, the order in which columns were updated. |
| 27 | sheet | string | Max Length: 36 | N/A |

## referencer_participants

Users/Groups associated to a Photo referencer

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | ID of the referencer participant |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | project_id | string | Max Length: 36 | The Project UID this row applies to. |
| 5 | referencer_urn | string | Max Length: 250 | Unique URN of the resource referencing the photo |
| 6 | participant_id | string | Max Length: 36 | The UID of the entity (user, group, role, etc...) referencing the photo |
| 7 | participant_type | string | Max Length: 36 | The type of the entity referencing the photo (for debugging purposes) |
| 8 | created_at | timestamp: SQL |  | The datetime the row was created on the server. |

## referencer_photos

Photo Referencers such as RFI, Issues

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | ID of the referencer photo |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | project_id | string | Max Length: 36 | The Project UID this row applies to. |
| 5 | referencer_urn | string | Max Length: 255 | Unique URN of the resource referencing the photo |
| 6 | photo_id | string | Max Length: 36 | The Photo UID this row applies to. |
| 7 | created_at | timestamp: SQL |  | The datetime the row was created on the server. |
| 8 | edge_urn | string | Max Length: 255 | This column was created to account for Form's complex visibility rules that depend on the state of the Form. Instead of having the Form as the Referencer, the Form Template becomes the Referencer, and the Form URN becomes the edge that moves between various Form Template URNs (for example, each Form Template will have multiple URNs that correspond to the various states that the Form can be in: DRAFT, PUBLISHED, etc..). |

© Copyright 2026 Autodesk Inc. | [Autodesk Construction Cloud](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
