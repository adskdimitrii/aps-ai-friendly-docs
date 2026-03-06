# relationships Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=relationships&format=html

---

# relationships Schema Description

**Documentation Updated:** 2023-12-04  

- [entity_relationship](#entity_relationship)

## entity_relationship

Describes a relationship

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
| 10 | created_on | timestamp: SQL |  | Creation time for relationship |
| 11 | deleted_on | timestamp: SQL |  | Deletion time for relationship |
| 12 | is_deleted | boolean |  | Describes whether this relationship is deleted |
| 13 | is_service_owned | boolean |  | Is the relationships created by a ACC service |

© Copyright 2026 Autodesk Inc. | [Autodesk Construction Cloud](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
