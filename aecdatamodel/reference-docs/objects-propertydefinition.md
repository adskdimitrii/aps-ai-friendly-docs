# PropertyDefinition

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/propertydefinition/

---

Objects

# PropertyDefinition

[](#)

Data object that represents property definition.

Property definition is an object that acts as a template to create properties on an entity.

## [Fields](#fields)

| name*   [String!](scalars.md) `non-null` | Name for this property definition. |
| --- | --- |
| specification   [String](scalars.md) | Specification of the property definition. It represents the data type of a property definition. |
| units   [Units](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/units/) | Unit of a property definition. |
| id*   [ID!](scalars.md) `non-null` | The ID of property definition. |
| description   [String](scalars.md) | A short description of the property definition. |
| isHidden   [Boolean](scalars.md) | Indicates if the parameter is hidden or not in the application |
| isArchived   [Boolean](scalars.md) | Indicates if the parameter is archived or not. |
| isReadOnly   [Boolean](scalars.md) | Indicates if the parameter is read-only or not in the application |
| shouldCopy   [Boolean](scalars.md) | Specifies expected behavior for the property on document data management operation like ‘copy’ in Autodesk authoring apps. A value of ‘true’ means the property will be copied along to the new document on such operations. |
| collection   [PropertyDefinitionCollection](objects-propertydefinitioncollection.md) | Property definition collection in which this property definition is present |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Property](objects-property.md) | Data object that represents property. |
| Field Of | [Referenceproperty](objects-referenceproperty.md) | A reference property which describes relationship between elements. |
