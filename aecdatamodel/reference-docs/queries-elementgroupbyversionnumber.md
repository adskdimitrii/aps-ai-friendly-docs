# elementGroupByVersionNumber

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/elementgroupbyversionnumber/

---

Queries

# elementGroupByVersionNumber

[](#)

Retrieves elementGroup by version number and ID.

**Template for Query:**

```
query GetElementGroupByVersionNumber($elementGroupId: ID!, $versionNumber: Int!, $versionFilter: VersionFilterInput) {
  elementGroupByVersionNumber(elementGroupId: $elementGroupId, versionNumber: $versionNumber, versionFilter: $versionFilter) {
    # ElementGroupByVersionNumber Fields
  }
}

```

**Template for Query Variables:**

```
{
  "elementGroupId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "versionNumber" : "<SOME-INT-TYPE-SCALAR-VALUE>",
  "versionFilter" : "<SOME-VERSIONFILTER-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| elementGroupId*   [ID!](scalars.md) `non-null` | The ID of the elementGroup. |
| --- | --- |
| versionNumber*   [Int!](scalars.md) `non-null` | Version number to be retrieved. |
| versionFilter   [VersionFilterInput](inputs-versionfilterinput.md) | Optional. Specifies version resolution behavior (e.g. whether the versionNumber refers to a PUBLISHED or WIP version). Defaults to PUBLISHED if not provided. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [ElementGroup](objects-elementgroup.md) | Represents a Revit model. |

## [Examples](#examples)
