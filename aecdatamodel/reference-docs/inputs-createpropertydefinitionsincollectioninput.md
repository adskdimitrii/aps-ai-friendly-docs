# CreatePropertyDefinitionsInCollectionInput

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/createpropertydefinitionsincollectioninput/

---

Inputs

# CreatePropertyDefinitionsInCollectionInput

[](#)

Input required for creating property definitions

## [Fields](#fields)

| propertyDefinitionCollectionId*   [ID!](scalars.md) `non-null` | The ID of property definition collection. |
| --- | --- |
| propertyDefinitionsInput*   [[PropertyDefinitionInCollectionInput!]!](/en/docs/aecdatamodel/v1/reference/inputs/propertydefinitionincollectioninput) `non-null` | List of property definitions to be created. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Input for Mutation | [createPropertyDefinitionsInCollection](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/mutations/createpropertydefinitionsincollection/) | Creates multiple property definitions in a property definition collection. |
