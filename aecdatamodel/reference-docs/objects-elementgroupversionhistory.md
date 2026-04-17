# ElementGroupVersionHistory

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/elementgroupversionhistory/

---

Objects

# ElementGroupVersionHistory

[](#)

Information related to versions of an elementGroup.

## [Fields](#fields)

Expand all

| id*   [ID!](scalars.md) `non-null` | Globally unique identifier. |
| --- | --- |
| tipVersion   [ElementGroupVersion](objects-elementgroupversion.md) | Latest version. |
| versions*   [ElementGroupVersions!](objects-elementgroupversions.md) `non-null` | Query for a specific set of versions. |
| filter   [ElementGroupVersionFilterInput](inputs-elementgroupversionfilterinput.md) | Specifies how to filter using version specific criteria. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |
| versionByNumber   [ElementGroupVersion](objects-elementgroupversion.md) | Query for a specific version by its version number. |
| versionNumber   [Int](scalars.md) | Version number to use for fetching version. |
| versionFilter   [VersionFilterInput](inputs-versionfilterinput.md) | Optional. Specifies version resolution behavior (e.g. whether the versionNumber refers to a PUBLISHED or WIP version). Defaults to PUBLISHED if not provided. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Elementgroup](objects-elementgroup.md) | Represents a Revit model. |
