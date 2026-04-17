# PropertiesComponent

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/propertiescomponent/

---

Objects

# PropertiesComponent

[](#)

Component that contains properties of an entity

## [Fields](#fields)

Expand all

| componentType*   [ComponentType!](objects-componenttype.md) `non-null` | Type of the component |
| --- | --- |
| properties   [Properties](objects-properties.md) | Query for specific Properties |
| filter   [PropertyFilterInput](inputs-propertyfilterinput.md) | Specifies which properties to return. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Implements](#implements)

| Usage | Used By | Description |
| --- | --- | --- |
| Interface | [ECSComponent](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/interfaces/ecscomponent/) | Represents a component |
