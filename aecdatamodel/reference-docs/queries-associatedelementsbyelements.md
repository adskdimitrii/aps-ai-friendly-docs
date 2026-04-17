# associatedElementsByElements

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/associatedelementsbyelements/

---

Queries

# associatedElementsByElements

[](#)

Returns a list of associated elements from target element Ids.

**Template for Query:**

```
query GetAssociatedElementsByElements($elementIds: [ID!]!, $pagination: PaginationInput) {
  associatedElementsByElements(elementIds: $elementIds, pagination: $pagination) {
    # AssociatedElementsByElements Fields
  }
}

```

**Template for Query Variables:**

```
{
  "elementIds" : "<SOME-[ID!]-TYPE-SCALAR-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| elementIds*   [[ID!]!](undefined/id!) `non-null` | target element ids for which to get the extension elements from. |
| --- | --- |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [Elements](objects-elements.md) | Contains a list of Elements returned in response to a query. |

## [Examples](#examples)
