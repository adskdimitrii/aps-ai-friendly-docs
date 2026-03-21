# ElementFilterInput

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/elementfilterinput/

---

Inputs

# ElementFilterInput

[](#)

Query input for filtering Elements.

## [Fields](#fields)

| query   [String](scalars.md) | Filter query in RSQL format for searching elements. For more details, please refer to: [Advanced Filtering](https://aps.autodesk.com/en/docs/aecdatamodel/v1/developers_guide/API%20Essentials/aecdatamodel/v1/) |
| --- | --- |
| name   [[String!]](/en/docs/aecdatamodel/v1/reference/scalars) | Filter for elements with a specified name |
| nameWithComparator   [[ValueComparatorInput!]](/en/docs/aecdatamodel/v1/reference/inputs/valuecomparatorinput) | Filter for elements with a specified name and comparator to apply |
| properties   [[ElementPropertyFilterInput!]](/en/docs/aecdatamodel/v1/reference/inputs/elementpropertyfilterinput) | Filter for elements with specified property values |
| references   [[ElementReferenceFilterInput!]](/en/docs/aecdatamodel/v1/reference/inputs/elementreferencefilterinput) | Filter for elements with specified reference properties |
| createdBy   [[String!]](/en/docs/aecdatamodel/v1/reference/scalars) | Filter for elements created by a specified user (email) |
| lastModifiedBy   [[String!]](/en/docs/aecdatamodel/v1/reference/scalars) | Filter for elements last modified by a specified user (email) |
| elementId   [[String!]](/en/docs/aecdatamodel-beta/v1/reference/scalars) | Filter for elements by their ids |
| revitElementId   [[String!]](/en/docs/aecdatamodel-beta/v1/reference/scalars) | Filter for elements by their revit element ids |

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Argument for Query | [elementsByHub](queries-elementsbyhub.md) | Retrieves elements from given hub, using additional RSQL filters if provided. |
| Argument for Query | [elementsByProject](queries-elementsbyproject.md) | Retrieves elements from given project, using additional RSQL filters if provided. |
| Argument for Query | [elementsByFolder](queries-elementsbyfolder.md) | Retrieves elements from given folder, using additional RSQL filters if provided. |
| Argument for Query | [elementsByElementGroup](queries-elementsbyelementgroup.md) | Retrieves elements from given elementGroup, using additional RSQL filters if provided. |
| Argument for Query | [elementsByElementGroups](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elementsbyelementgroups/) | Retrieves elements from a given set of elementGroups, using additional RSQL filters if provided. |
| Argument for Query | [elementsByElementGroupAtVersion](queries-elementsbyelementgroupatversion.md) | Retrieves elements from given elementGroup at given elementGroup version, using additional RSQL filters if provided. |
| Argument for Field | [Element](objects-element.md) | Represents an element type. |
| Argument for Field | [ElementGroup](objects-elementgroup.md) | Represents a Revit model. |
