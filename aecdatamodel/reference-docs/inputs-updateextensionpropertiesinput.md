# UpdateExtensionPropertiesInput

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/updateextensionpropertiesinput/

---

Inputs

# UpdateExtensionPropertiesInput

[](#)

Input for updating extension properties on elements.

## [Fields](#fields)

| targets*   [[ExtensionPropertyTarget!]!](/en/docs/aecdatamodel/v1/reference/inputs/extensionpropertytarget) `non-null` | Ids of targets to update extension properties on. |
| --- | --- |
| properties*   [[ExtensionPropertyInput!]!](/en/docs/aecdatamodel/v1/reference/inputs/extensionpropertyinput) `non-null` | Extension properties to update. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Input for Mutation | [updateExtensionPropertiesOnElements](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/mutations/updateextensionpropertiesonelements/) | Updates extension properties on elements. |
