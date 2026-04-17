# ElementGroupDifference

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/elementgroupdifference/

---

Objects

# ElementGroupDifference

[](#)

Contains a list of ElementDifferences returned in response to a query.

## [Fields](#fields)

| result   [[ElementDifference]](/en/docs/aecdatamodel/v1/reference/objects/elementdifference) | An array containing ElementDifferences |
| --- | --- |
| pagination   [Pagination](objects-pagination.md) | Contains information about the current page when results are split into multiple pages. |

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Query By | [diffElementGroupByVersionWithLatest](queries-diffelementgroupbyversionwithlatest.md) | Returns a list of element differences and their difference type from target elementGroup. |
