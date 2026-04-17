# elementGroupExtractionStatusAtTip

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/elementgroupextractionstatusattip/

---

Queries

# elementGroupExtractionStatusAtTip

[](#)

Retrieves the extraction status of the given elementGroup for the latest version.

**Template for Query:**

```
query GetElementGroupExtractionStatusAtTip($fileUrn: ID!, $accProjectId: ID!) {
  elementGroupExtractionStatusAtTip(fileUrn: $fileUrn, accProjectId: $accProjectId) {
    # ElementGroupExtractionStatusAtTip Fields
  }
}

```

**Template for Query Variables:**

```
{
  "fileUrn" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "accProjectId" : "<SOME-ID-TYPE-SCALAR-VALUE>"
}

```

## [Arguments](#arguments)

| fileUrn*   [ID!](scalars.md) `non-null` | File to retrieve elementGroup extraction status from. |
| --- | --- |
| accProjectId*   [ID!](scalars.md) `non-null` | Forma Project Id of the elementGroup. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [ElementGroupExtractionStatus](objects-elementgroupextractionstatus.md) | Information about elementGroup extraction status. |
