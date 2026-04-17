# classifications Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=classifications&format=html

---

# classifications Schema Description

**Documentation Updated:** 2025-12-02  

- [nodes_account](#nodes_account)
- [nodes_library_used_in_project](#nodes_library_used_in_project)
- [nodes_project](#nodes_project)
- [structures_account](#structures_account)
- [structures_project](#structures_project)

**Beta Release**  
This is a Beta release of the classifications data set and schema definitions are subject to change or even possibly be removed from the final data set release. Thank you for your understanding with any future schema updates.

## nodes_account

List of nodes used in structures on account level

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | structure_id | string: UUID |  | ID of the structure |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | structure_name | string |  | Name of the structure |
| 5 | parent_node_id | number |  | ID of the parent node |
| 6 | node_id | number |  | Unique int4 representing the id of the node in the given structure version |
| 7 | node_code | string: null |  | Less user-friendly identifier of the node |
| 8 | node_name | string |  | User-friendly name of the node |
| 9 | order | number |  | Represents in which order the node will appear inside it's parent node branch |
| 10 | created_at | timestamp: SQL |  | Timestamp the node was created at |
| 11 | updated_at | timestamp: SQL |  | Timestamp the node was updated at |

## nodes_library_used_in_project

"List of nodes used in structures on project level, linked to account level structures"

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | structure_id | string: UUID |  | ID of the structure |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | structure_name | string |  | Name of the structure |
| 5 | parent_node_id | number |  | ID of the parent node |
| 6 | node_id | number |  | Unique int4 representing the id of the node in the given structure version |
| 7 | node_code | string: null |  | Less user-friendly identifier of the node |
| 8 | node_name | string |  | User-friendly name of the node |
| 9 | order | number |  | Represents in which order the node will appear inside it's parent node branch |
| 10 | created_at | timestamp: SQL |  | Timestamp the node was created at |
| 11 | updated_at | timestamp: SQL |  | Timestamp the node was updated at |

## nodes_project

List of nodes used in structures on project level, not linked to account level structures

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | structure_id | string: UUID |  | ID of the structure |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | structure_name | string |  | Name of the structure |
| 5 | parent_node_id | number |  | ID of the parent node |
| 6 | node_id | number |  | Unique int4 representing the id of the node in the given structure version |
| 7 | node_code | string: null |  | Less user-friendly identifier of the node |
| 8 | node_name | string |  | User-friendly name of the node |
| 9 | order | number |  | Represents in which order the node will appear inside it's parent node branch |
| 10 | created_at | timestamp: SQL |  | Timestamp the node was created at |
| 11 | updated_at | timestamp: SQL |  | Timestamp the node was updated at |

## structures_account

List of structures on account level

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | structure_id | string: UUID |  | ID of the structure |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | structure_name | string |  | Name of the structure |
| 5 | created_at | timestamp: SQL |  | Timestamp the structure was created at |
| 6 | updated_at | timestamp: SQL |  | Timestamp the structure was updated at |

## structures_project

List of structures on project level

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | structure_id | string: UUID |  | ID of the structure |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | structure_name | string |  | Name of the structure |
| 5 | created_at | timestamp: SQL |  | Timestamp the structure was created at |
| 6 | updated_at | timestamp: SQL |  | Timestamp the structure was updated at |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
