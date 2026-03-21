# elementGroupExtractionStatus

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/elementgroupextractionstatus/

---

Queries

# elementGroupExtractionStatus

[](#)

Retrieves the extraction status of the given elementGroup.

**Template for Query:**

```
query GetElementGroupExtractionStatus($fileUrn: ID!, $versionNumber: Int) {
  elementGroupExtractionStatus(fileUrn: $fileUrn, versionNumber: $versionNumber) {
    # ElementGroupExtractionStatus Fields
  }
}

```

**Template for Query Variables:**

```
{
  "fileUrn" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "versionNumber" : "<SOME-INT-TYPE-SCALAR-VALUE>"
}

```

## [Arguments](#arguments)

| fileUrn*   [ID!](scalars.md) `non-null` | File to retrieve elementGroup extraction status from. |
| --- | --- |
| versionNumber   [Int](scalars.md) | File version to retrieve elementGroup extraction status from. Default value is 1. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [ElementGroupExtractionStatus](objects-elementgroupextractionstatus.md) | Information about elementGroup extraction status. |

## [Examples](#examples)
