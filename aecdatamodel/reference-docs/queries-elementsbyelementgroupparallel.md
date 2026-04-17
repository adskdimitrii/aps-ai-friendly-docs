# elementsByElementGroupParallel

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/elementsbyelementgroupparallel/

---

Queries

# elementsByElementGroupParallel

[](#)

Retrieves elements from given elementGroup, use elementsByElementGroupParallelCursors to generate the innitial cursors.

**Template for Query:**

```
query GetElementsByElementGroupParallel($elementGroupId: ID!, $pagination: PaginationInput!) {
  elementsByElementGroupParallel(elementGroupId: $elementGroupId, pagination: $pagination) {
    # ElementsByElementGroupParallel Fields
  }
}

```

**Template for Query Variables:**

```
{
  "elementGroupId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT>"
}

```

## [Arguments](#arguments)

| elementGroupId*   [ID!](scalars.md) `non-null` | ElementGroup to retrieve elements from. |
| --- | --- |
| pagination*   [PaginationInput!](inputs-paginationinput.md) `non-null` | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [Elements](objects-elements.md) | Contains a list of Elements returned in response to a query. |

## [Examples](#examples)
