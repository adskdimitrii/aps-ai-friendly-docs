# PropertyDefinitionInCollectionInput

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/propertydefinitionincollectioninput/

---

Inputs

# PropertyDefinitionInCollectionInput

[](#)

Input required for creating property definition.

## [Fields](#fields)

| name*   [String!](scalars.md) `non-null` | Name for uniquely identifying a property definition. |
| --- | --- |
| specification*   [String!](scalars.md) `non-null` | Specification of property definition. It represents the data type of a property definition. |
| isReadOnly   [Boolean](scalars.md) | Indicates if the parameter is read-only or not in the application |
| isHidden   [Boolean](scalars.md) | Indicates if the parameter is hidden or not in the application |
| isArchived   [Boolean](scalars.md) | Indicates if the parameter is archived or not in the application |
| description   [String](scalars.md) | A short description of the property definition. |
| shouldCopy   [Boolean](scalars.md) | Specifies expected behavior for the property on document data management operation like ‘copy’ in Autodesk authoring apps. Setting it to ‘true’ will copy the property along to the new document on such operations. |

* Required

## [Where Used](#where-used)
