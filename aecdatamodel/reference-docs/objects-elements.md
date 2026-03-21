# Elements

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/elements/

---

Objects

# Elements

[](#)

Contains a list of Elements returned in response to a query.

## [Fields](#fields)

| totalCount   [Int](scalars.md) | Total count of elements found for a given query. Will only be populated for the following fields: - ‘Query.elements’ - ‘Query.elementsByElementGroup’ - ‘ElementGroup.elements’ - ‘Element.referencedBy’ |
| --- | --- |
| pagination   [Pagination](objects-pagination.md) | Contains information about the current page, when results are split into multiple pages. |
| results*   [[Element]!](/en/docs/aecdatamodel/v1/reference/objects/element) `non-null` | An array representing elements |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Element](objects-element.md) | Represents an element type. |
| Field Of | [Elementgroup](objects-elementgroup.md) | Represents a Revit model. |
| Query By | [elementsByHub](queries-elementsbyhub.md) | Retrieves elements from given hub, using additional RSQL filters if provided. |
| Query By | [elementsByProject](queries-elementsbyproject.md) | Retrieves elements from given project, using additional RSQL filters if provided. |
| Query By | [elementsByFolder](queries-elementsbyfolder.md) | Retrieves elements from given folder, using additional RSQL filters if provided. |
| Query By | [elementsByElementGroup](queries-elementsbyelementgroup.md) | Retrieves elements from given elementGroup, using additional RSQL filters if provided. |
| Query By | [elementsByElementGroups](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elementsbyelementgroups/) | Retrieves elements from a given set of elementGroups, using additional RSQL filters if provided. |
| Query By | [elementsByElementGroupAtVersion](queries-elementsbyelementgroupatversion.md) | Retrieves elements from given elementGroup at given elementGroup version, using additional RSQL filters if provided. |
