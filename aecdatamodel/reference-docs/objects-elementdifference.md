# ElementDifference

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/elementdifference/

---

Objects

# ElementDifference

[](#)

Represents an Element Difference type

## [Fields](#fields)

Expand all

| type   [DifferenceType](objects-differencetype.md) | The type of the difference in the element between versions |
| --- | --- |
| element   [Element](objects-element.md) | Represents the element the difference belongs to |
| differences   [ComponentDifferences](objects-componentdifferences.md) | Contains the Component Differences for the element |
| pagination   [PaginationInput](inputs-paginationinput.md) | Pagination for property-level differences within the element. |

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Query By | [diffElementByVersionWithLatest](queries-diffelementbyversionwithlatest.md) | Returns the element difference from target element. |
