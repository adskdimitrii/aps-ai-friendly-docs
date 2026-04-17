# cdclocations Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=cdclocations&format=html

---

# cdclocations Schema Description

**Documentation Updated:** 2025-11-21  

- [nodes](#nodes)
- [trees](#trees)

**Beta Release**  
This is a Beta release of the cdclocations data set and schema definitions are subject to change or even possibly be removed from the final data set release. Thank you for your understanding with any future schema updates.

## nodes

Nodes from a specified tree in BIM 360. - This is the Change Data Capture (CDC) enabled version of the locations.nodes table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | tree_id | string: UUID |  | The Tree ID for this node Foreign Key: Table: tree Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | parent_id | string: UUID |  | Parent Node ID |
| 5 | id | string: UUID |  | ID for the node |
| 6 | name | string |  | Name of the node |
| 7 | order | number |  | Relative order of the node under its parent |
| 8 | created_at | timestamp: SQL |  | Creation time for the node Column used for filtering Date Range Extraction requests |
| 9 | updated_at | timestamp: SQL |  | Update time for the node Column used for filtering Date Range Extraction requests |
| 10 | deleted_at | timestamp: SQL |  | Timestamp when the node was deleted Column used for filtering Date Range Extraction requests |
| 11 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## trees

The location trees for BIM 360. - This is the Change Data Capture (CDC) enabled version of the locations.trees table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Tree ID |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | name | string |  | Name of the tree |
| 5 | created_at | timestamp: SQL |  | Creation time of the tree Column used for filtering Date Range Extraction requests |
| 6 | updated_at | timestamp: SQL |  | Update time for the tree Column used for filtering Date Range Extraction requests |
| 7 | deleted_at | timestamp: SQL |  | Timestamp when the tree was deleted Column used for filtering Date Range Extraction requests |
| 8 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
