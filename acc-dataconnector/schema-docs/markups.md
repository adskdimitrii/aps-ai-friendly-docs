# markups Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=markups&format=html

---

# markups Schema Description

**Documentation Updated:** 2024-03-14  

- [layer](#layer)
- [link](#link)
- [markup](#markup)
- [placement](#placement)

## layer

Markups are placed on layers. which are placed on surfaces.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 2 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 3 | uid | string: UUID |  | Unique identifier for the layer. |
| 4 | surface_uid | string: UUID |  | Parent Surface ID for this Layer. Foreign Key: Table: surface Column: uid |
| 5 | name | string: null |  | Name of layer, null is default layer. |
| 6 | promotable | boolean |  | Indicates whether or not this layer's markups are copied when a new version of a sheet is uploaded. |
| 7 | surface_type | string | Possible Values: document sheet photo job_output acc_sheet acc_document acc_model | The type of surface |
| 8 | base_entity_urn | string |  | The document version urn |
| 9 | base_entity_uid | string: UUID |  | The UUID of the root entity of the surface (sheet id, doc id, etc) |

## link

Indicates if a markup is linked to another feature entity.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 2 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 3 | uid | string: UUID |  | The unique identifier for this link. |
| 4 | markup_id | number |  | markup ID associated with this placement. Foreign Key: Table: markup Column: id |
| 5 | type | string | Possible Values: document sheet acc_document acc_sheet acc_sheet_history photo rfi progress-tracking form submittal | Type of link |
| 6 | destination | string: UUID |  | The unique identifier of the entity linked to. Mutually exclusive with uri. |
| 7 | uri | string: null |  | The uniform resource identifier being linked to. Mutually exclusive with destination. |
| 8 | created_by | string |  | Autodesk User ID of the user who created the link. |
| 9 | created_at | timestamp: SQL |  | Date and time the link was created in ISO8601 format |
| 10 | deleted | boolean |  | Indicates if the link has been deleted |
| 11 | deleted_by | string |  | Autodesk User ID of the user who deleted the link. |
| 12 | deleted_at | timestamp: SQL |  | Date and time the link was deleted in ISO8601 format |

## markup

Main table for all our markup data.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | number |  | Unique identifier of markup. |
| 2 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | uid | string: UUID |  | Unique identifier of markup. |
| 5 | feature_bound_uid | string: UUID |  | Unique identifier of feature entity this markup is linked to. |
| 6 | feature_bound_type | string: null | Possible Values: issue progress-tracking photo calibration | Type of feature entity this markup is linked to. |
| 7 | type | string: null |  | Stencil schema used for markup |
| 8 | created_by | string |  | Autodesk User ID of the user who created the markup. |
| 9 | created_at | timestamp: SQL |  | Date and time the markup was created in ISO8601 format |
| 10 | updated_by | string |  | Autodesk User ID of the user who updated the markup. |
| 11 | updated_at | timestamp: SQL |  | Date and time the markup was updated in ISO8601 format |
| 12 | deleted | boolean |  | Indicates if the markup has been deleted |
| 13 | deleted_by | string |  | Autodesk User ID of the user who deleted the markup. |
| 14 | deleted_at | timestamp: SQL |  | Date and time the markup was deleted in ISO8601 format |
| 15 | markup_text | string |  | Text content for the given markup. This is the initial text that the markup was created with, THIS MAY BE OVERRIDDEN BY TEXT ON THE PLACEMENT OF THIS MARKUP. Merge with the "placement" table and check "placement_text" to identify the text of a given placement of this markup. if "placement_text" is blank, then "markup_text" holds the current text content. NOTE: if the markup is a feature bound markup (feature_bound_type is present), the text here is inaccurate and should be ignored. |

## placement

Combined with markup table to place markups on layers and surfaces.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | Added for account scoping of issues data |
| 2 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 3 | markup_uid | string: UUID |  | markup ID associated with this placement. Foreign Key: Table: markup Column: uid |
| 4 | surface_uid | string: UUID |  | Surface ID this markup is placed on. Foreign Key: Table: surface Column: uid |
| 5 | published | boolean |  | Indicates if the markup is visible to all users or not. |
| 6 | layer_uid | string: UUID |  | Layer ID this markup is placed on. Foreign Key: Table: layer Column: uid |
| 7 | id | number |  | Unique identifier for the placement. |
| 8 | uid | string: UUID |  | Unique identifier for the placement. |
| 9 | created_by | string |  | Autodesk User ID of the user who created the placement. |
| 10 | created_at | timestamp: SQL |  | Date and time the placement was created in ISO8601 format |
| 11 | updated_by | string |  | Autodesk User ID of the user who updated the placement. |
| 12 | updated_at | timestamp: SQL |  | Date and time the placement was updated in ISO8601 format |
| 13 | deleted | boolean |  | Indicates if the placement has been deleted |
| 14 | deleted_by | string |  | Autodesk User ID of the user who deleted the placement. |
| 15 | deleted_at | timestamp: SQL |  | Date and time the placement was deleted in ISO8601 format |
| 16 | placement_text | string |  | Text content for the given markup-placement. THIS WILL OVERRIDE TEXT IN MARKUP.MARKUP_TEXT. If there is text present in this column, it is the current text of the given placement. If this field is blank, check the "markup_text" column by merging with the "markup" table to get text (if there is any for this placement). NOTE: if the markup is a feature bound markup (feature_bound_type is present), the text here is inaccurate and should be ignored. |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
