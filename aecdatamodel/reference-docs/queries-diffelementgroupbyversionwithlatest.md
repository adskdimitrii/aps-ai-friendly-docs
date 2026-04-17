# diffElementGroupByVersionWithLatest

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/diffelementgroupbyversionwithlatest/

---

Queries

# diffElementGroupByVersionWithLatest

[](#)

Returns a list of element differences and their difference type from target elementGroup. No support with extension element groups currently.

**Template for Query:**

```
query GetDiffElementGroupByVersionWithLatest($elementGroupId: ID!, $startVersion: Int, $versionFilter: VersionFilterInput, $changeFilter: [DifferenceType], $pagination: PaginationInput) {
  diffElementGroupByVersionWithLatest(elementGroupId: $elementGroupId, startVersion: $startVersion, versionFilter: $versionFilter, changeFilter: $changeFilter, pagination: $pagination) {
    # DiffElementGroupByVersionWithLatest Fields
  }
}

```

**Template for Query Variables:**

```
{
  "elementGroupId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "startVersion" : "<SOME-INT-TYPE-SCALAR-VALUE>",
  "versionFilter" : "<SOME-VERSIONFILTER-INPUT-TYPE-VALUE>",
  "changeFilter" : "<SOME-[DIFFERENCETYPE]-TYPE-SCALAR-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| elementGroupId*   [ID!](scalars.md) `non-null` | ElementGroup to retrieve element differences of. |
| --- | --- |
| startVersion   [Int](scalars.md) | The version to get the element differences from against the latest. |
| versionFilter   [VersionFilterInput](inputs-versionfilterinput.md) | Optional. Specifies version resolution behavior (e.g. whether startVersion refers to a PUBLISHED or WIP version). Defaults to PUBLISHED if not provided. |
| changeFilter   [[DifferenceType]](/en/docs/aecdatamodel/v1/reference/objects/differencetype) | The type of change to filter the element differences by. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [ElementGroupDifference](objects-elementgroupdifference.md) | Contains a list of ElementDifferences returned in response to a query. |
