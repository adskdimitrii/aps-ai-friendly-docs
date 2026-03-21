# DistinctPropertyValuesCollection

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/distinctpropertyvaluescollection/

---

Objects

# DistinctPropertyValuesCollection

[](#)

A collection of distinct properties matching the name given.

## [Fields](#fields)

| pagination   [Pagination](objects-pagination.md) | Contains information about the current page when results are split into multiple pages. |
| --- | --- |
| results*   [[DistinctPropertyValues]!](/en/docs/aecdatamodel/v1/reference/objects/distinctpropertyvalues) `non-null` | An array of distinct property values matching the name given. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Query By | [distinctPropertyValuesInElementGroupByName](queries-distinctpropertyvaluesinelementgroupbyname.md) | Retrieves distinct values in an ElementGroup given a property name. |
