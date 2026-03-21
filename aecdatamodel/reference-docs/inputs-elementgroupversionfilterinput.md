# ElementGroupVersionFilterInput

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/elementgroupversionfilterinput/

---

Inputs

# ElementGroupVersionFilterInput

[](#)

Input to filter using version criteria.

## [Fields](#fields)

| number   [Int](scalars.md) | version number to use for filtering |
| --- | --- |
| createdAfter   [DateTime](scalars.md) | createdAfter datetime filter |
| createdBefore   [DateTime](scalars.md) | createdBefore datetime filter |
| createdOn   [DateTime](scalars.md) | createdOn datetime filter |
| createdBy   [ID](scalars.md) | filter based on user who created the version |

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Argument for Field | [ElementGroupVersionHistory](objects-elementgroupversionhistory.md) | Information related to versions of an elementGroup. |
