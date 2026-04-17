# ExtensionComponent

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/extensioncomponent/

---

Objects

# ExtensionComponent

[](#)

Component that links an extension to the entity it is extending.

## [Fields](#fields)

| componentType*   [ComponentType!](objects-componenttype.md) `non-null` | Type of the component |
| --- | --- |
| element   [Element](objects-element.md) | Element being extended |
| elementGroup   [ElementGroup](objects-elementgroup.md) | ElementGroup being extended |

* Required

## [Implements](#implements)

| Usage | Used By | Description |
| --- | --- | --- |
| Interface | [ECSComponent](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/interfaces/ecscomponent/) | Represents a component |
