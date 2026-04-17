# locations Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=locations&format=html

---

# locations Schema Description

**Documentation Updated:** 2023-12-04  

- [nodes](#nodes)
- [trees](#trees)

## nodes

Nodes from a specified tree in BIM 360.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | tree_id | string: UUID |  | The Tree ID for this node Foreign Key: Table: tree Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | parent_id | string: UUID |  | Parent Node ID |
| 5 | id | string: UUID |  | ID for the node |
| 6 | name | string |  | Name of the node |
| 7 | order | number |  | Relative order of the node under its parent |
| 8 | created_at | timestamp: SQL |  | Creation time for the node |
| 9 | updated_at | timestamp: SQL |  | Update time for the node |

## trees

The location trees for BIM 360.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Tree ID |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | name | string |  | Name of the tree |
| 5 | created_at | timestamp: SQL |  | Creation time of the tree |
| 6 | updated_at | timestamp: SQL |  | Update time for the tree |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
