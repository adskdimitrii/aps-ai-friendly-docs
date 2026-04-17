# cdcsheets Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=cdcsheets&format=html

---

# cdcsheets Schema Description

**Documentation Updated:** 2025-12-08  

- [disciplines](#disciplines)
- [lineages](#lineages)
- [sets](#sets)
- [sheet_bubbles](#sheet_bubbles)
- [sheet_tags](#sheet_tags)
- [sheets](#sheets)

**Beta Release**  
This is a Beta release of the cdcsheets data set and schema definitions are subject to change or even possibly be removed from the final data set release. Thank you for your understanding with any future schema updates.

## disciplines

A discipline definition in a container - This is the Change Data Capture (CDC) enabled version of the sheets.disciplines table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | container_type | string |  | Type of the contain to which this tag belongs |
| 4 | index | number |  | Discipline index |
| 5 | name | string |  | Discipline name |
| 6 | designator | string |  | Short charcators as a discipline designator |
| 7 | created_at | timestamp: SQL |  | Timestamp when the discipline was created Column used for filtering Date Range Extraction requests |
| 8 | updated_at | timestamp: SQL |  | Timestamp when the discipline was updated Column used for filtering Date Range Extraction requests |
| 9 | deleted_at | timestamp: SQL |  | Timestamp when the discipline was deleted Column used for filtering Date Range Extraction requests |
| 10 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## lineages

Object to define sheets collection with a unique name - This is the Change Data Capture (CDC) enabled version of the sheets.lineages table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique id for the sheet_history |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | container_type | string |  | Typ of the contain to which the sheet_history belongs |
| 5 | name | string |  | Name of the sheet_history |
| 6 | created_at | timestamp: SQL |  | Timestamp when the lineage was created Column used for filtering Date Range Extraction requests |
| 7 | updated_at | timestamp: SQL |  | Timestamp when the lineage was updated Column used for filtering Date Range Extraction requests |
| 8 | deleted_at | timestamp: SQL |  | Timestamp when the lineage was deleted Column used for filtering Date Range Extraction requests |
| 9 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## sets

Object to define a milestone with name and time - This is the Change Data Capture (CDC) enabled version of the sheets.sets table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique id for the version_set |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | container_type | string |  | Typ of the contain to which the version set belongs |
| 5 | name | string |  | Name of the version_set |
| 6 | issuance_date | timestamp: SQL |  | Issuance time of the version_set |
| 7 | created_at | timestamp: SQL |  | Creation time of the version_set Column used for filtering Date Range Extraction requests |
| 8 | created_by | string |  | Id of user who create the version_set |
| 9 | created_by_name | string |  | Name of user who create the version_set |
| 10 | updated_at | timestamp: SQL |  | Update time of the version_set Column used for filtering Date Range Extraction requests |
| 11 | updated_by | string |  | Id of user who update the version_set |
| 12 | updated_by_name | string |  | Name of user who update the version_set |
| 13 | deleted | boolean |  | Sheet is deleted |
| 14 | deleted_at | timestamp: SQL |  | Timestamp when the set was deleted Column used for filtering Date Range Extraction requests |
| 15 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## sheet_bubbles

Bubble resources of a sheet - This is the Change Data Capture (CDC) enabled version of the sheets.sheet_bubbles table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | container_type | string |  | Typ of the contain to which this bubble object belongs |
| 4 | sheet_id | string: UUID |  | Id of a sheet |
| 5 | urn | string |  | Urn of the bubble related to the sheet |
| 6 | viewable_guid | string |  | Id to identify the given resource in the bubble related to the sheet |
| 7 | paper_width | number |  | Physical paper height of the sheet |
| 8 | paper_height | number |  | Physical paper height of the sheet |
| 9 | viewable_order | number |  | Page number in the bubble related to the sheet |
| 10 | pug_urn | string |  | Urn of the viewable pug object for the sheet |
| 11 | pug_width | number |  | Width of the viewable pug object for the sheet |
| 12 | pug_height | number |  | Height of the viewable pug object for the sheet |
| 13 | large_thumbnail_width | number |  | Width of the large thumbnaill for the sheet |
| 14 | large_thumbnail_height | number |  | Height of the large thumbnaill for the sheet |
| 15 | small_thumbnail_width | number |  | Width of the small thumbnaill for the sheet |
| 16 | small_thumbnail_height | number |  | Height of the small thumbnaill for the sheet |
| 17 | storage_urn | string |  | The storage urn of the pdf page for the sheet |
| 18 | storage_size | number |  | Storage size of the sheet |
| 19 | viewable_urn | string |  | Urn of the viewable leaflet object for the sheet |
| 20 | viewable_width | number |  | Width of the viewable leaflet object for the sheet |
| 21 | viewable_height | number |  | Height of the viewable leaflet object for the sheet |
| 22 | created_at | timestamp: SQL |  | Timestamp when the sheet_bubble was created Column used for filtering Date Range Extraction requests |
| 23 | updated_at | timestamp: SQL |  | Timestamp when the sheet_bubble was updated Column used for filtering Date Range Extraction requests |
| 24 | deleted_at | timestamp: SQL |  | Timestamp when the sheet_bubble was deleted Column used for filtering Date Range Extraction requests |
| 25 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## sheet_tags

Text label on a sheet - This is the Change Data Capture (CDC) enabled version of the sheets.sheet_tags table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | container_type | string |  | Typ of the contain to which this tag belongs |
| 4 | sheet_id | string: UUID |  | Id of a sheet |
| 5 | value | string |  | Text value of a tag |
| 6 | created_at | timestamp: SQL |  | Timestamp when the sheet_tag was created Column used for filtering Date Range Extraction requests |
| 7 | updated_at | timestamp: SQL |  | Timestamp when the sheet_tag was updated Column used for filtering Date Range Extraction requests |
| 8 | deleted_at | timestamp: SQL |  | Timestamp when the sheet_tag was deleted Column used for filtering Date Range Extraction requests |
| 9 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## sheets

Object created from a single pdf page with name and version set - This is the Change Data Capture (CDC) enabled version of the sheets.sheets table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique id for the sheet |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | container_type | string |  | Typ of the contain to which the sheet belongs |
| 5 | name | string |  | Name of the sheet |
| 6 | nat_sort_name | string |  | Name variety based on natural sorting |
| 7 | history_id | string: UUID |  | Id for the history the sheet belongs to |
| 8 | version_set_id | string: UUID |  | Id for the version set the sheet belongs to |
| 9 | created_at | timestamp: SQL |  | Creation time of the sheet Column used for filtering Date Range Extraction requests |
| 10 | created_by | string |  | Id of user who create the sheet |
| 11 | created_by_name | string |  | Name of user who create the sheet |
| 12 | updated_at | timestamp: SQL |  | Update time of the sheet Column used for filtering Date Range Extraction requests |
| 13 | updated_by | string |  | Id of user who update the sheet |
| 14 | updated_by_name | string |  | Name of user who update the sheet |
| 15 | title | string |  | Description for the sheet |
| 16 | upload_file_name | string |  | The name of the upload file, from which the sheet created |
| 17 | upload_id | string: UUID |  | The id of the upload command that creates the sheet |
| 18 | processing_state | string |  | The processing state of the sheet |
| 19 | is_current | boolean |  | Indicate whether this is the current version among sheets with same name |
| 20 | discipline_index | number |  | Index of the relevant discipline |
| 21 | deleted | boolean |  | Whether this is a deleted sheet |
| 22 | deleted_at | timestamp: SQL |  | Deletion time of the sheet Column used for filtering Date Range Extraction requests |
| 23 | deleted_by | string |  | Id of user who delete the sheet |
| 24 | deleted_by_name | string |  | Name of user who delete the sheet |
| 25 | original_set_name | string |  | Snapshot of the set name when the sheet is deleted |
| 26 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
