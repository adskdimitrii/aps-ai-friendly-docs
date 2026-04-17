# elementsByElementGroupParallelCursors

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/elementsbyelementgroupparallelcursors/

---

Queries

# elementsByElementGroupParallelCursors

[](#)

Returns a list of cursors which can be used to get all elements of an ElementGroup rapidely in parallel.

**Template for Query:**

```
query GetElementsByElementGroupParallelCursors($elementGroupId: ID!, $amount: Int) {
  elementsByElementGroupParallelCursors(elementGroupId: $elementGroupId, amount: $amount) {
    # ElementsByElementGroupParallelCursors Fields
  }
}

```

**Template for Query Variables:**

```
{
  "elementGroupId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "amount" : "<SOME-INT-TYPE-SCALAR-VALUE>"
}

```

## [Arguments](#arguments)

| elementGroupId*   [ID!](scalars.md) `non-null` | ElementGroup to generate cursors for. |
| --- | --- |
| amount   [Int](scalars.md) |  |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [ElementCursors](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/elementcursors/) | Contains a list of Cusors returned in response to a query. |

## [Examples](#examples)
