# takeoff Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=takeoff&format=html

---

# takeoff Schema Description

**Documentation Updated:** 2025-09-04  

- [carbon_definitions](#carbon_definitions)
- [classification_systems](#classification_systems)
- [classifications](#classifications)
- [content_lineages](#content_lineages)
- [packages](#packages)
- [quantities](#quantities)
- [quantity_definitions](#quantity_definitions)
- [settings](#settings)
- [takeoff_items](#takeoff_items)
- [takeoff_types](#takeoff_types)

**Beta Release**  
This is a Beta release of the takeoff data set and schema definitions are subject to change or even possibly be removed from the final data set release. Thank you for your understanding with any future schema updates.

## carbon_definitions

Carbon definitions

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource Id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | declared_unit | enum: string | Possible Values: EA IN LF YD SI SF SY CI CF CY LBS TON MM M M2 M3 KG T | Unit of measure used to calculate the embodied carbon for a given material. |
| 5 | unit_of_measure | enum: string | Possible Values: KGCO2E TCO2E | Unit of measure for the embodied carbon amount |
| 6 | a1_a2_a3_achievable | number | nullable | Embodied carbon statistics for the product stages A1, A2, and A3 for the material or EPD. Achievable embodied carbon quantity for the scope (20th percentile). |
| 7 | a1_a2_a3_conservative | number | nullable | Embodied carbon statistics for the product stages A1, A2, and A3 for the material or EPD. Conservative embodied carbon quantity for the scope (80th percentile). |
| 8 | a1_a2_a3_mean | number | nullable | Embodied carbon statistics for the product stages A1, A2, and A3 for the material or EPD. Mean of the embodied carbon results. |
| 9 | a1_a2_a3_standard_deviation | number | nullable | Embodied carbon statistics for the product stages A1, A2, and A3 for the material or EPD. Standard deviation of the embodied carbon results. |

## classification_systems

Classification systems associated with each project. A classification system is used for the process of categorizing and organizing information for construction projects.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource Id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | name | string | Max length: 200 | The classification system name. |
| 5 | type | enum: string | Possible Values: CLASSIFICATION_SYSTEM_1 CLASSIFICATION_SYSTEM_2 | The type of classification system. |
| 6 | created_at | timestamp: SQL |  | Date the resource was created |
| 7 | updated_at | timestamp: SQL |  | Date the resource was updated |

## classifications

Classification hierarchy for a classification system.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource Id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | system_id | string: UUID |  | Foreign Key: Table: classification_systems Column: id |
| 5 | code | string | Max length: 256 | The classification code. |
| 6 | parent_code | string: null | Max length: 256 | Parent classification code. Null if the current classification is the root. |
| 7 | description | string | Max length: 256 | A description of the classification. |
| 8 | parent_id | string: UUID | nullable | Parent classification ID, references the classification id. Null if the current classification is the root. |

## content_lineages

List of 2D sheets and BIM models that are used in a Takeoff project.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource Id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | sheet_name | string: null | nullable Max length: 256 | Name of the sheet. This is set to NULL if the content lineage points to a 3D model. |
| 5 | lineage_urn | string: null | Max length: 256 | The URN of the 3D model. This is set to NULL for a sheet. |
| 6 | view_name | string: null | Max length: 256 | The name of the 3D model view. |
| 7 | type | enum: string | Possible Values: SHEET FILE_MODEL | The content view type. |
| 8 | created_at | timestamp: SQL |  | Date the resource was created |
| 9 | updated_at | timestamp: SQL |  | Date the resource was updated |

## packages

Takeoff packages are used to organize and contain all takeoff data related to a scope of work in a project.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource Id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | name | string | Max length: 64 | The package name (user defined). |
| 5 | created_at | timestamp: SQL |  | Date the resource was created |
| 6 | updated_at | timestamp: SQL |  | Date the resource was updated |

## quantities

Quantities associated with Takeoff items

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource Id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | quantity | number | nullable | The quantity of the takeoff. |
| 5 | output_name | string | nullable. Max length: 256 | A custom output name from the user. |
| 6 | unit_of_measure | enum: string | Possible Values: EA IN LF YD SI SF SY CI CF CY LBS TON MM M M2 M3 KG T | The unit of measurement. |
| 7 | quantity_order | number |  | The order for which the quantities are sorted. This value will be 0 for the Primary quantity and will be greater or equal to 1 for Secondary quantities. |
| 8 | item_id | string: UUID |  | Foreign Key: Table: takeoff_items Column: id |
| 9 | classification1_id | string: UUID | nullable | Foreign Key: Table: classifications Column: id |
| 10 | classification2_id | string: UUID | nullable | Foreign Key: Table: classifications Column: id |
| 11 | carbon_definition_id | string: UUID | nullable | Foreign Key: Table: carbon_definitions Column: id |
| 12 | unit_cost | number | nullable | Unit cost for the quantity |
| 13 | total_cost | number | nullable | Total cost = quantity * unit_cost |

## quantity_definitions

Quantity definitions associated with a Takeoff type

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | output_name | string: null | Max length: 256 | A custom output name from the user. |
| 5 | expression | string: null | Max length: 4096 | The formula to calculate the quantity. |
| 6 | unit_of_measure | enum: string | Possible Values: EA IN LF YD SI SF SY CI CF CY LBS TON MM M M2 M3 KG T | The unit of measurement. |
| 7 | quantity_order | number |  | The order for which the quantities are sorted. |
| 8 | type_id | string: UUID |  | Foreign Key: Table: takeoff_types Column: id |
| 9 | classification1_id | string: UUID |  | Foreign Key: Table: classifications Column: id. |
| 10 | classification2_id | string: UUID |  | Foreign Key: Table: classifications Column: id. |
| 11 | unit_cost | number | nullable | Unit cost for quantity |
| 12 | carbon_definition_id | string: UUID | nullable | Foreign Key: Table: carbon_definitions Column: id |

## settings

Takeoff settings for each project

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Same as Project id. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | measurement_system | enum: string | nullable ENUM_VALUES: IMPERIAL, METRIC | The project measurement system. Possible values: IMPERIAL, METRIC. |
| 5 | created_at | timestamp: SQL |  | Date the resource was created |
| 6 | updated_at | timestamp: SQL |  | Date the resource was updated |

## takeoff_items

Takeoff items in a project. Each item belongs to a Takeoff package.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | content_lineage_id | string: UUID |  | Foreign Key: Table: content_lineages Column: id |
| 5 | content_version | string | Max length: 256 | The content view version. |
| 6 | package_id | string: UUID |  | Foreign Key: Table: packages Column: id |
| 7 | type_id | string: UUID |  | Foreign Key: Table: takeoff_types Column: id |
| 8 | object_name | string: null | Max length: 256 | The name of the takeoff type that the item is derived from. |
| 9 | location_id | string: UUID | nullable | Reference to Locations node id |
| 10 | created_at | timestamp: SQL |  | Date the resource was created |
| 11 | updated_at | timestamp: SQL |  | Date the resource was updated |

## takeoff_types

Takeoff types are used to organize and describe groups of takeoff items with shared properties

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource Id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | name | string | Max length: 64 | The takeoff type name. |
| 5 | description | string: null | Max length: 256 | A description of the takeoff type. |
| 6 | tool | enum: string | Possible Values: COUNT DISTANCE AREA SELECT | The type of tool used to create takeoff items of this takeoff type. |
| 7 | created_at | timestamp: SQL |  | Date the resource was created |
| 8 | updated_at | timestamp: SQL |  | Date the resource was updated |
| 9 | package_id | string: UUID |  | Foreign Key: Table: packages Column: id |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
