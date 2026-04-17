# AddExtensionPropertiesInput

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/addextensionpropertiesinput/

---

Inputs

# AddExtensionPropertiesInput

[](#)

Input for adding extension properties to elements.

## [Fields](#fields)

| targets*   [[ExtensionPropertyTarget!]!](/en/docs/aecdatamodel/v1/reference/inputs/extensionpropertytarget) `non-null` | Ids of targets to add extension properties on. |
| --- | --- |
| properties*   [[ExtensionPropertyInput!]!](/en/docs/aecdatamodel/v1/reference/inputs/extensionpropertyinput) `non-null` | Extension properties to add. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Input for Mutation | [addExtensionPropertiesToElements](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/mutations/addextensionpropertiestoelements/) | Adds extension properties to elements. |
