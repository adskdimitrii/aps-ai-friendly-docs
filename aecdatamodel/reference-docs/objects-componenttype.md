# ComponentType

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/componenttype/

---

Objects

# ComponentType

[](#) Enum which represents the possible types of a component

## [Valid Values](#valid-values)

| Value | Description |
| --- | --- |
| IDENTITY | Identify component |
| PROPERTIES | Properties component |
| REFERENCES | References component |
| ELEMENT_ALTERNATIVE_REPRESENTATIONS | Element alternative representations component |
| BODY_REPRESENTATION | Body representation component |
| ORIGIN | Origin component |
| AXIS | Axis representation component |
| EXTENSION | Extension component |

## [Where Used](#where-used)

| Object/Input | Field | Description |
| --- | --- | --- |
| [AxisRepresentationComponent](objects-axisrepresentationcomponent.md) | `componentType`. | Represents the Axis Representation Component which contains a curve defining the axis. |
| [BodyRepresentationComponent](objects-bodyrepresentationcomponent.md) | `componentType`. | Component that contains body representation of an entity. |
| [ECSComponent](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/interfaces/ecscomponent/) | `componentType`. | Represents a component |
| [ElementAlternativeIdentifiersComponent](objects-elementalternativeidentifierscomponent.md) | `componentType`. | Component that contains alternative identifiers of an element |
| [ExtensionComponent](objects-extensioncomponent.md) | `componentType`. | Component that links an extension to the entity it is extending. |
| [IdentityComponent](objects-identitycomponent.md) | `componentType`. | Component that contains identity information of an entity |
| [OriginComponent](objects-origincomponent.md) | `componentType`. | Represents the Origin Component which contains the origin point of the element. |
| [PropertiesComponent](objects-propertiescomponent.md) | `componentType`. | Component that contains properties of an entity |
| [ReferencesComponent](objects-referencescomponent.md) | `componentType`. | Component that contains references of an entity |
| [componentsfilterinput](inputs-componentsfilterinput.md) | `types`. | Types of components |
