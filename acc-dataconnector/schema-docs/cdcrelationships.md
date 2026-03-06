# cdcrelationships Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=cdcrelationships&format=html

---

# cdcrelationships Schema Description

**Documentation Updated:** 2025-11-21  

- [entity_relationship](#entity_relationship)

**Beta Release**  
This is a Beta release of the cdcrelationships data set and schema definitions are subject to change or even possibly be removed from the final data set release. Thank you for your understanding with any future schema updates.

## entity_relationship

Describes a relationship - This is the Change Data Capture (CDC) enabled version of the relationships.entity_relationship table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | relationship_guid | string: UUID |  | External GUID for relationship (served by API) |
| 4 | item1_domain | string |  | Associated domain for Item 1 |
| 5 | item1_entitytype | string |  | Associated entity type for Item 1 |
| 6 | item1_id | string |  | Associated ID for Item 1 |
| 7 | item2_domain | string |  | Associated domain for Item 2 |
| 8 | item2_entitytype | string |  | Associated entity type for Item 2 |
| 9 | item2_id | string |  | Associated ID for Item 2 |
| 10 | created_at | timestamp: SQL |  | Timestamp when the entity_relationship was created Column used for filtering Date Range Extraction requests |
| 11 | deleted_at | timestamp: SQL |  | Timestamp when the entity_relationship was deleted Column used for filtering Date Range Extraction requests |
| 12 | is_deleted | boolean |  | Describes whether this relationship is deleted |
| 13 | is_service_owned | boolean |  | Is the relationships created by a ACC service |
| 14 | updated_at | timestamp: SQL |  | Timestamp when the entity_relationship was updated Column used for filtering Date Range Extraction requests |
| 15 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

© Copyright 2026 Autodesk Inc. | [Autodesk Construction Cloud](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
