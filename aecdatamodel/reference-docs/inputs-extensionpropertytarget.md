# ExtensionPropertyTarget

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/extensionpropertytarget/

---

Inputs

# ExtensionPropertyTarget

[](#)

Input specifying target elements and their extensionGroup to add properties in. You can target elements in one of two ways:
> - **By explicit IDs**: Provide specific element IDs using the `elementIds` field
> - **By category**: Filter elements by category name using the `categoryFilter` field
> These options are mutually exclusive - use either `elementIds` OR `categoryFilter`, not both.

## [Fields](#fields)

| elementIds   [[String!]](/en/docs/aecdatamodel/v1/reference/scalars) | Ids of target elements |
| --- | --- |
| extensionGroupId*   [ID!](scalars.md) `non-null` | Id of extensionGroup which should contain extension elements |
| categoryFilter   [CategoryFilterInput](inputs-categoryfilterinput.md) | Target element categories |

* Required

## [Where Used](#where-used)
