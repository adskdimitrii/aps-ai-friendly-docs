# ElementGroupVersion

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/elementgroupversion/

---

Objects

# ElementGroupVersion

[](#)

Represents a single version of an ElementGroup.

## [Fields](#fields)

| versionNumber   [Int](scalars.md) | Published version number (lineage version). |
| --- | --- |
| wipVersionNumber   [Int](scalars.md) | WIP version number from the document timeline. Null when sync is not enabled. |
| createdOn   [DateTime](scalars.md) | Date and time of version creation. |
| createdBy   [User](objects-user.md) | User that created this specific version. |
| elementGroup   [ElementGroup](objects-elementgroup.md) | The ElementGroup at this version. |

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Elementgroup](objects-elementgroup.md) | Represents a Revit model. |
| Field Of | [Elementgroupversionhistory](objects-elementgroupversionhistory.md) | Information related to versions of an elementGroup. |
