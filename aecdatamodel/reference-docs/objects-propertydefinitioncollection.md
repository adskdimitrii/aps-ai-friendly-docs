# PropertyDefinitionCollection

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/propertydefinitioncollection/

---

Objects

# PropertyDefinitionCollection

[](#)

Data object that represents property definition collection.

## [Fields](#fields)

Expand all

| id*   [ID!](scalars.md) `non-null` | The ID of this property definition collection. |
| --- | --- |
| name   [String](scalars.md) | Name for this property definition collection. |
| description   [String](scalars.md) | Description for this property definition collection. |
| definitions   [PropertyDefinitions](objects-propertydefinitions.md) | Get all Property Definitions of this Collection |
| filter   [PropertyDefinitionFilterInput](inputs-propertydefinitionfilterinput.md) | Specifies how to filter on property definitions. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Propertydefinition](objects-propertydefinition.md) | Data object that represents property definition. Property definition is an object that acts as a template to create properties on an entity. |
