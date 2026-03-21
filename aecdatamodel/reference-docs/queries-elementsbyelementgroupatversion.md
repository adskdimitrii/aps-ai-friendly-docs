# elementsByElementGroupAtVersion

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/elementsbyelementgroupatversion/

---

Queries

# elementsByElementGroupAtVersion

[](#)

Retrieves elements from given elementGroup at given elementGroup version, using additional RSQL filters if provided.

**Template for Query:**

```
query GetElementsByElementGroupAtVersion($elementGroupId: ID!, $versionNumber: Int!, $filter: ElementFilterInput, $pagination: PaginationInput) {
  elementsByElementGroupAtVersion(elementGroupId: $elementGroupId, versionNumber: $versionNumber, filter: $filter, pagination: $pagination) {
    # ElementsByElementGroupAtVersion Fields
  }
}

```

**Template for Query Variables:**

```
{
  "elementGroupId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "versionNumber" : "<SOME-INT-TYPE-SCALAR-VALUE>",
  "filter" : "<SOME-ELEMENTFILTER-INPUT-TYPE-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| elementGroupId*   [ID!](scalars.md) `non-null` | ElementGroup to retrieve elements from. |
| --- | --- |
| versionNumber*   [Int!](scalars.md) `non-null` | ElementGroup version to retrieve elements from. |
| filter   [ElementFilterInput](inputs-elementfilterinput.md) | RSQL filter to use for searching elements. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [Elements](objects-elements.md) | Contains a list of Elements returned in response to a query. |

## [Examples](#examples)
