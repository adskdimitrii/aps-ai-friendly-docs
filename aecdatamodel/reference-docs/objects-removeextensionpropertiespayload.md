# RemoveExtensionPropertiesPayload

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/removeextensionpropertiespayload/

---

Objects

# RemoveExtensionPropertiesPayload

[](#)

Payload for removing extension properties from elements.

## [Fields](#fields)

| elements*   [[Element!]](/en/docs/aecdatamodel/v1/reference/objects/element) `non-null` | Extension elements that were changed. |
| --- | --- |
| totalResults   [Int](scalars.md) | Total number of mutated extension elements. |
| message   [String](scalars.md) | Additional response details for categoryFilter-based mutations. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Mutated By | [removeExtensionPropertiesFromElements](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/mutations/removeextensionpropertiesfromelements/) | Removes extension properties from elements. |
