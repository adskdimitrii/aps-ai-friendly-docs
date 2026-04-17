# RemoveExtensionPropertiesInput

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/removeextensionpropertiesinput/

---

Inputs

# RemoveExtensionPropertiesInput

[](#)

Input for removing extension properties from elements.

## [Fields](#fields)

| targets*   [[ExtensionPropertyTarget!]!](/en/docs/aecdatamodel/v1/reference/inputs/extensionpropertytarget) `non-null` | Ids of targets to remove extension properties from. |
| --- | --- |
| propertyDefinitionIds*   [[String!]!](/en/docs/aecdatamodel/v1/reference/scalars) `non-null` | Extension properties to remove. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Input for Mutation | [removeExtensionPropertiesFromElements](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/mutations/removeextensionpropertiesfromelements/) | Removes extension properties from elements. |
