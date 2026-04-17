# diffElementByVersionWithLatest

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/diffelementbyversionwithlatest/

---

Queries

# diffElementByVersionWithLatest

[](#)

Returns the element difference from target element. No support with extension element groups currently.

**Template for Query:**

```
query GetDiffElementByVersionWithLatest($elementId: ID!, $versionFilter: VersionFilterInput, $startElementGroupVersion: Int) {
  diffElementByVersionWithLatest(elementId: $elementId, versionFilter: $versionFilter, startElementGroupVersion: $startElementGroupVersion) {
    # DiffElementByVersionWithLatest Fields
  }
}

```

**Template for Query Variables:**

```
{
  "elementId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "versionFilter" : "<SOME-VERSIONFILTER-INPUT-TYPE-VALUE>",
  "startElementGroupVersion" : "<SOME-INT-TYPE-SCALAR-VALUE>"
}

```

## [Arguments](#arguments)

| elementId*   [ID!](scalars.md) `non-null` | ElementId to retrieve element difference of. |
| --- | --- |
| versionFilter   [VersionFilterInput](inputs-versionfilterinput.md) | Optional. Specifies version resolution behavior (e.g. whether `startElementGroupVersion` refers to a PUBLISHED or WIP version). Defaults to PUBLISHED if not provided. |
| startElementGroupVersion   [Int](scalars.md) | The version to get the element differences from against the latest. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [ElementDifference](objects-elementdifference.md) | Represents an Element Difference type |
