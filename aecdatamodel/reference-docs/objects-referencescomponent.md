# ReferencesComponent

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/referencescomponent/

---

Objects

# ReferencesComponent

[](#)

Component that contains references of an entity

## [Fields](#fields)

Expand all

| componentType*   [ComponentType!](objects-componenttype.md) `non-null` | Type of the component |
| --- | --- |
| references   [ReferenceProperties](objects-referenceproperties.md) | Represents information that further defines the Element (e.g. Type data) |
| filter   [ReferencePropertyFilterInput](inputs-referencepropertyfilterinput.md) | Specifies which reference properties to return. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Implements](#implements)

| Usage | Used By | Description |
| --- | --- | --- |
| Interface | [ECSComponent](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/interfaces/ecscomponent/) | Represents a component |
