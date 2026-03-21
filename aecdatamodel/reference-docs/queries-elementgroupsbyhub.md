# elementGroupsByHub

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/elementgroupsbyhub/

---

Queries

# elementGroupsByHub

[](#)

Retrieves elementGroups in the given hub, using additional RSQL filters if provided.

**Template for Query:**

```
query GetElementGroupsByHub($hubId: ID!, $filter: ElementGroupFilterInput, $pagination: PaginationInput) {
  elementGroupsByHub(hubId: $hubId, filter: $filter, pagination: $pagination) {
    # ElementGroupsByHub Fields
  }
}

```

**Template for Query Variables:**

```
{
  "hubId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "filter" : "<SOME-ELEMENTGROUPFILTER-INPUT-TYPE-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| hubId*   [ID!](scalars.md) `non-null` | Hub to retrieve elementGroups from. |
| --- | --- |
| filter   [ElementGroupFilterInput](inputs-elementgroupfilterinput.md) | RSQL filter to use for searching elementGroups. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [ElementGroups!](objects-elementgroups.md) `non-null` | Contains a list of ElementGroups returned in response to a query. |

## [Examples](#examples)
