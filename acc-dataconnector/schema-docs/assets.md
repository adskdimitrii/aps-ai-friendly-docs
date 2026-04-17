# assets Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=assets&format=html

---

# assets Schema Description

**Documentation Updated:** 2024-07-23  

- [asset_custom_attribute_values](#asset_custom_attribute_values)
- [asset_model_sync_records](#asset_model_sync_records)
- [asset_permissions](#asset_permissions)
- [asset_stages](#asset_stages)
- [asset_statuses](#asset_statuses)
- [assets](#assets)
- [categories](#categories)
- [category_custom_attribute_assignments](#category_custom_attribute_assignments)
- [category_status_set_assignments](#category_status_set_assignments)
- [custom_attribute_default_values](#custom_attribute_default_values)
- [custom_attribute_selection_values](#custom_attribute_selection_values)
- [custom_attributes](#custom_attributes)
- [model_sync_containers](#model_sync_containers)
- [status_sets](#status_sets)
- [system_memberships](#system_memberships)
- [systems](#systems)

## asset_custom_attribute_values

The value of a Custom Attribute for a given Asset

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | asset_id | string: UUID |  | Identifier of the Asset this value is for Foreign Key: Table: assets Column: id |
| 2 | custom_attribute_id | string: UUID |  | Identifier of the Custom Attribute that defines the context of this value Foreign Key: Table: custom_attributes Column: id |
| 3 | value_boolean | boolean | Nullable | The value of the Custom Attribute for 'boolean' Custom Attribute data_types. One, and only one, of value_boolean or value_string will be populated. |
| 4 | value_string | string: null |  | The value of the Custom Attribute for 'text', 'numeric', 'date', 'select' and 'multi_select' Custom Attribute data_types. One, and only one, of value_boolean or value_string will be populated. For 'numeric' data_types, the value will be a string that parses to a floating point number, e.g. "46.2" For 'date' data_types, the value will be an ISO8601 date string with no time, e.g. "2020-04-10" For 'select' and 'multi_select` data_types, the value will be a FOREIGN_KEY: custom_attribute_selection_values,id. The custom_attribute_selection_values,id key will be one of the custom_attribute_selection_values for the Custom Attribute described by custom_attribute_id. Note: 'multi_select' data_types can have more than one value per Asset. All other types have a maximum of a single value per Asset. |
| 5 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 6 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |

## asset_model_sync_records

Record of syncing a model object to an asset

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Internal Identifier |
| 2 | version | number |  | Sequential version. Incremented each time the item is modified in any way. |
| 3 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 5 | asset_id | string: UUID |  | The ID of the Asset the model object has been synced to Foreign Key: Table: assets Column: id |
| 6 | model_lineage_urn | string |  | The URN of the model file's versioned lineage |
| 7 | model_object_guid | string |  | A globally unique identifier for a model object set by ACS Assets service |
| 8 | model_external_id | string |  | An ID for externally identifying a model object that comes directly from the model file. This is ofen a GUID (e.g. for Revit files), but not always. |
| 9 | synced_model_version_urn | string |  | The versioned URN of the model file's lineage that was actually synced to the Asset |
| 10 | synced_model_version_number | number |  | The version of the URN of the model file's lineage that was actually synced to the Asset |
| 11 | model_svf2_id | number |  | An integer ID commonly used internally in model files that is stable across versions of the model file |
| 12 | model_lmv_id | number |  | An integer ID commonly used internally in model files for older file types that do not support SVF2 |
| 13 | created_at | timestamp: SQL |  | Creation time |
| 14 | created_by | string |  | User (Oxygen) ID of the create actor |
| 15 | updated_at | timestamp: SQL |  | Most recent update time |
| 16 | updated_by | string |  | User (Oxygen) ID of the most recent update actor |
| 17 | deleted_at | timestamp: SQL | Nullable | Deletion time. If deleted_at === null, the entity is considered active. |
| 18 | deleted_by | string: null |  | User (Oxygen) ID of the delete actor |

## asset_permissions

Permission Definitions for V3 Permissions API

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Internal Identifier |
| 2 | version | number |  | Sequential version. Incremented each time the item is modified in any way. |
| 3 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 5 | permission_policy_type | enum: string | view, edit, create, create_only, manage, inherited_permissions | The type of the permission assigned to the subject and resource |
| 6 | subject_type | enum: string | user, company, role, project_admins | Indicates the type of the subject to which the permission applies |
| 7 | subject_oxygen_id | string |  | The Oxygen ID of the user or user group to which the permission applies |
| 8 | subject_acs_admin_id | string: UUID |  | The UUID identifier of a user or user group, as defined in the ACC Admin APIs, to which the permission applies |
| 9 | resource_type | enum: string | project, category, system_category | The type of the resource associated with a permission |
| 10 | resource_id | string: UUID |  | The identifier of the resource to which this permission is assigned |
| 11 | effect | enum: string | allow, deny | The effect of the permission |
| 12 | created_at | timestamp: SQL |  | Creation time |
| 13 | created_by | string |  | User (Oxygen) ID of the create actor |
| 14 | updated_at | timestamp: SQL |  | Most recent update time |
| 15 | updated_by | string |  | User (Oxygen) ID of the most recent update actor |
| 16 | deleted_at | timestamp: SQL | Nullable | Deletion time. If deleted_at === null, the entity is considered active. |
| 17 | deleted_by | string: null |  | User (Oxygen) ID of the delete actor |

## asset_stages

Asset Stage Definitions

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Internal Identifier |
| 2 | version | number |  | Sequential version. Incremented each time the item is modified in any way. |
| 3 | asset_id | string: UUID |  | The ID of the Asset this Asset Stage belongs to Foreign Key: Table: assets Column: id |
| 4 | bound_type | enum: string | asset_status | The type of joined object this stage belongs to |
| 5 | bound_id | string: UUID |  | The joined object this stage belongs to |
| 6 | completed_work | number |  | The completed amount of work |
| 7 | max_work | number |  | The total amount of work to be completed |
| 8 | unit_of_work | enum: string | SF, LF, SM, LM, N/A | The unit of work |
| 9 | started_at | timestamp: SQL |  | Start time |
| 10 | started_by | string |  | User (Oxygen) ID of the start actor |
| 11 | completed_at | timestamp: SQL |  | Completion time |
| 12 | completed_by | string |  | User (Oxygen) ID of the complete actor |
| 13 | completion_status | enum: string | in_progress, completed, skipped | Completion status of the asset stages |
| 14 | is_current | boolean |  | Whether this stage is the current |
| 15 | category_id | string: UUID |  | The category id of the stage Foreign Key: Table: categories Column: id |
| 16 | location_id | string: UUID |  | BIM 360 Locations ID of the Location of this Asset Stage |
| 17 | created_at | timestamp: SQL |  | Creation time |
| 18 | created_by | string |  | User (Oxygen) ID of the create actor |
| 19 | updated_at | timestamp: SQL |  | Most recent update time |
| 20 | updated_by | string |  | User (Oxygen) ID of the most recent update actor |
| 21 | deleted_at | timestamp: SQL | Nullable | Deletion time. If deleted_at === null, the entity is considered active. |
| 22 | deleted_by | string: null |  | User (Oxygen) ID of the delete actor |
| 23 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 24 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |

## asset_statuses

Statuses available for Assets

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Internal Identifier |
| 2 | version | number |  | Sequential version. Incremented each time the item is modified in any way. |
| 3 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 5 | label | string | Max length: 100 | Displayable name |
| 6 | description | string: null | Max length: 500 | Description of the asset status |
| 7 | status_set_id | string: UUID |  | Identifier of the Status Set the Asset Status is assigned to Foreign Key: Table: status_sets Column: id |
| 8 | created_at | timestamp: SQL |  | Creation time |
| 9 | created_by | string |  | User (Oxygen) ID of the create actor |
| 10 | updated_at | timestamp: SQL |  | Most recent update time |
| 11 | updated_by | string |  | User (Oxygen) ID of the most recent update actor |
| 12 | deleted_at | timestamp: SQL | Nullable | Deletion time. If deleted_at === null, the entity is considered active. |
| 13 | deleted_by | string: null |  | User (Oxygen) ID of the delete actor |
| 14 | sort_order | number |  | Sort order of the Asset Status within the Status Set |

## assets

A Physical Asset

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Internal Identifier |
| 2 | version | number |  | Sequential version. Incremented each time the item is modified in any way. |
| 3 | client_asset_id | string | Max length: 100 | Client generated Identifier |
| 4 | description | string: null | Max length: 1000 | Description of the asset |
| 5 | category_id | string |  | Identifier of the Category this Asset is assigned to Foreign Key: Table: categories Column: id |
| 6 | status_id | string: UUID |  | Identifier of the Assets Status this Asset is assigned to Foreign Key: Table: asset_statuses Column: id |
| 7 | location_id | string: UUID | Nullable | BIM 360 Locations ID or the Location this Asset is assigned |
| 8 | company_id | string: UUID |  | BIM 360 HQ Company Identifier |
| 9 | barcode | string: null | Max length: 100 | Barcode for the asset |
| 10 | created_at | timestamp: SQL |  | Creation time |
| 11 | created_by | string |  | User (Oxygen) ID of the create actor |
| 12 | updated_at | timestamp: SQL |  | Most recent update time |
| 13 | updated_by | string |  | User (Oxygen) ID of the most recent update actor |
| 14 | deleted_at | timestamp: SQL | Nullable | Deletion time. If deleted_at === null, the entity is considered active. |
| 15 | deleted_by | string: null |  | User (Oxygen) ID of the delete actor |
| 16 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 17 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |

## categories

Hierarchical Tree for Categorizing Systems and Assets

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string |  | Internal Identifier (Legacy) |
| 2 | version | number |  | Sequential version. Incremented each time the item is modified in any way. |
| 3 | name | string | Max length: 100 | Displayable name |
| 4 | description | string: null | Max length: 1000 | Description of the category |
| 5 | parent_id | string | Nullable | Identifier (Legacy) of the Parent Category. If not present, Category is ROOT. Foreign Key: Table: categories Column: id |
| 6 | created_at | timestamp: SQL |  | Creation time |
| 7 | created_by | string |  | User (Oxygen) ID of the create actor |
| 8 | updated_at | timestamp: SQL |  | Most recent update time |
| 9 | updated_by | string |  | User (Oxygen) ID of the most recent update actor |
| 10 | deleted_at | timestamp: SQL | Nullable | Deletion time. If deleted_at === null, the entity is considered active. |
| 11 | deleted_by | string: null |  | User (Oxygen) ID of the delete actor |
| 12 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 13 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 14 | uid | string: UUID |  | Internal identifier (Globally Unique) |
| 15 | category_type | enum: string | asset, system | Type of category. Systems and assets have distinct category trees. |
| 16 | parent_uid | string: UUID | Nullable | Identifier (Globally Unique) of the Parent Category. If not present, Category is ROOT. Foreign Key: Table: categories Column: uid |

## category_custom_attribute_assignments

Assignments of Custom Attributes to Categories

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Internal Identifier |
| 2 | version | number |  | Sequential version. Incremented each time the item is modified in any way. |
| 3 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 5 | category_id | string |  | Identifier of the Category the Custom Attribute is being assigned to Foreign Key: Table: categories Column: id |
| 6 | custom_attribute_id | string: UUID |  | Identifier of the Custom Attribute being assigned to a Category Foreign Key: Table: custom_attributes Column: id |
| 7 | created_at | timestamp: SQL |  | Creation time |
| 8 | created_by | string |  | User (Oxygen) ID of the create actor |
| 9 | updated_at | timestamp: SQL |  | Most recent update time |
| 10 | updated_by | string |  | User (Oxygen) ID of the most recent update actor |
| 11 | deleted_at | timestamp: SQL | Nullable | Deletion time. If deleted_at === null, the entity is considered active. |
| 12 | deleted_by | string: null |  | User (Oxygen) ID of the delete actor |

## category_status_set_assignments

Assignments of Status Sets to Categories

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Internal Identifier |
| 2 | version | number |  | Sequential version. Incremented each time the item is modified in any way. |
| 3 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 5 | category_id | string |  | Identifier (Legacy) of the Category the Status Set is being assigned to Foreign Key: Table: categories Column: id |
| 6 | status_set_id | string: UUID |  | Identifier of the Status Set being assigned to a Category Foreign Key: Table: status_sets Column: id |
| 7 | created_at | timestamp: SQL |  | Creation time |
| 8 | created_by | string |  | User (Oxygen) ID of the create actor |
| 9 | updated_at | timestamp: SQL |  | Most recent update time |
| 10 | updated_by | string |  | User (Oxygen) ID of the most recent update actor |
| 11 | deleted_at | timestamp: SQL | Nullable | Deletion time. If deleted_at === null, the entity is considered active. |
| 12 | deleted_by | string: null |  | User (Oxygen) ID of the delete actor |
| 13 | category_type | enum: string | asset, system | Type of category. Systems and assets have distinct category trees. |
| 14 | category_uid | string: UUID |  | Identifier (Globally Unique) of the Category the Status Set is being assigned to Foreign Key: Table: categories Column: uid |

## custom_attribute_default_values

Default Values for the Custom Attributes

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 2 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 3 | custom_attribute_id | string: UUID |  | Foreign Key: Table: custom_attributes Column: id |
| 4 | default_value_boolean | boolean | Nullable | Default value for the Custom Attribute for an Asset for 'boolean' data_types. One, and only one, of default_value_boolean or default_value_string will be populated. |
| 5 | default_value_string | string: null |  | Default value for the Custom Attribute for an Asset for 'text', 'numeric', 'date', 'select', and 'multi_select' data_types. One, and only one, of default_value_boolean or default_value_string will be populated. For 'select' and 'multi_select` data_types, the value will be a FOREIGN_KEY: custom_attribute_selection_values,id. The custom_attribute_selection_values,id key will be one of the custom_attribute_selection_values for the Custom Attribute described by custom_attribute_id. Note: 'multi_select' data_types can have more than one default value per Custom Attribute. All other types have a maximum of a single default value per Custom Attribute. |

## custom_attribute_selection_values

Available Selection values for 'select' and 'multi_select' data_type Custom Attributes

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Internal Identifier |
| 2 | version | number |  | Sequential version. Incremented each time the item is modified in any way. |
| 3 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 5 | display_name | string | Max length: 100 | Displayable name |
| 6 | custom_attribute_id | string: UUID |  | Foreign Key: Table: custom_attributes Column: id |
| 7 | created_at | timestamp: SQL |  | Creation time |
| 8 | created_by | string |  | User (Oxygen) ID of the create actor |
| 9 | updated_at | timestamp: SQL |  | Most recent update time |
| 10 | updated_by | string |  | User (Oxygen) ID of the most recent update actor |
| 11 | deleted_at | timestamp: SQL | Nullable | Deletion time. If deleted_at === null, the entity is considered active. |
| 12 | deleted_by | string: null |  | User (Oxygen) ID of the delete actor |

## custom_attributes

User-Defined Attributes for available for Assets in a given Category

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Internal Identifier |
| 2 | version | number |  | Sequential version. Incremented each time the item is modified in any way. |
| 3 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 5 | name | string |  | Internal name of the Custom Attribute |
| 6 | display_name | string | Max length: 100 | Displayable name |
| 7 | description | string: null | Max length: 1000 | Description of the custom attribute |
| 8 | data_type | enum: string | boolean, text, numeric, date, select, multi_select | The Data Type of the Custom Attribute. Used to determine which additional columns will be applicable, and what their data_type will be for the Custom Attribute. Used to determine the populated value field of the value for this Custom Attribute on an Asset (i.e. value_boolean, value_string, or value_array) |
| 9 | required_on_ingress | boolean |  | Does NOT guarantee the presence of a value for the Custom Attribute on an Asset if True |
| 10 | max_length_on_ingress | number | Only present for 'text' data_type | Defines a max length that can be set for the Custom Attribute when editing an Asset. Does not guarantee that all existing Assets values for the Custom Attribute will meet this max length. |
| 11 | created_at | timestamp: SQL |  | Creation time |
| 12 | created_by | string |  | User (Oxygen) ID of the create actor |
| 13 | updated_at | timestamp: SQL |  | Most recent update time |
| 14 | updated_by | string |  | User (Oxygen) ID of the most recent update actor |
| 15 | deleted_at | timestamp: SQL | Nullable | Deletion time. If deleted_at === null, the entity is considered active. |
| 16 | deleted_by | string: null |  | User (Oxygen) ID of the delete actor |

## model_sync_containers

Container for a model file to extract assets from

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Internal Identifier |
| 2 | version | number |  | Sequential version. Incremented each time the item is modified in any way. |
| 3 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 5 | model_lineage_urn | string |  | The URN of the model file's versioned lineage |
| 6 | created_at | timestamp: SQL |  | Creation time |
| 7 | created_by | string |  | User (Oxygen) ID of the create actor |
| 8 | updated_at | timestamp: SQL |  | Most recent update time |
| 9 | updated_by | string |  | User (Oxygen) ID of the most recent update actor |
| 10 | deleted_at | timestamp: SQL | Nullable | Deletion time. If deleted_at === null, the entity is considered active. |
| 11 | deleted_by | string: null |  | User (Oxygen) ID of the delete actor |

## status_sets

Set of Statuses available for Assets in a given Category

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Internal Identifier |
| 2 | version | number |  | Sequential version. Incremented each time the item is modified in any way. |
| 3 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 5 | name | string | Max length: 100 | Displayable name |
| 6 | description | string: null | Max length: 500 | Description of the status set |
| 7 | is_default | boolean |  | A Project will always have a single "Default" Status Set created for the Project upon initialization. All other Status Sets will be user created and is_default = false |
| 8 | created_at | timestamp: SQL |  | Creation time |
| 9 | created_by | string |  | User (Oxygen) ID of the create actor |
| 10 | updated_at | timestamp: SQL |  | Most recent update time |
| 11 | updated_by | string |  | User (Oxygen) ID of the most recent update actor |
| 12 | deleted_at | timestamp: SQL | Nullable | Deletion time. If deleted_at === null, the entity is considered active. |
| 13 | deleted_by | string: null |  | User (Oxygen) ID of the delete actor |

## system_memberships

Membership of a System

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 2 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 3 | system_id | string: UUID |  | Identifier of the Parent System Foreign Key: Table: systems Column: id |
| 4 | member_type | enum: string | asset, system | Type of the System member. Systems can contain Assets or other Systems. |
| 5 | member_id | string: UUID |  | Identifier of the Member System Foreign Key: Table: systems Column: id |

## systems

System Definitions

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Internal Identifier |
| 2 | version | number |  | Sequential version. Incremented each time the item is modified in any way. |
| 3 | bim360_account_id | string: UUID |  | Added for account scoping of Assets data |
| 4 | bim360_project_id | string: UUID |  | Added for account scoping of Assets data |
| 5 | name | string | Max length: 500 | Displayable name |
| 6 | description | string: null | Max length: 1000 | Description of the system |
| 7 | category_uid | string: UUID |  | Identifier (Globally Unique) of the Category this System is assigned to Foreign Key: Table: categories Column: uid |
| 8 | status_id | string: UUID |  | Identifier of the Assets Status this System is assigned to Foreign Key: Table: asset_statuses Column: id |
| 9 | created_at | timestamp: SQL |  | Creation time |
| 10 | created_by | string |  | User (Oxygen) ID of the create actor |
| 11 | updated_at | timestamp: SQL |  | Most recent update time |
| 12 | updated_by | string |  | User (Oxygen) ID of the most recent update actor |
| 13 | deleted_at | timestamp: SQL | Nullable | Deletion time. If deleted_at === null, the entity is considered active. |
| 14 | deleted_by | string: null |  | User (Oxygen) ID of the delete actor |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
