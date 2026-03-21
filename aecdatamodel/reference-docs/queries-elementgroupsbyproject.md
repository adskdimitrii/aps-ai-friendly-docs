# elementGroupsByProject

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/elementgroupsbyproject/

---

Queries

# elementGroupsByProject

[](#)

Retrieves elementGroups in the given project, using additional RSQL filters if provided.

**Template for Query:**

```
query GetElementGroupsByProject($projectId: ID!, $filter: ElementGroupFilterInput, $pagination: PaginationInput) {
  elementGroupsByProject(projectId: $projectId, filter: $filter, pagination: $pagination) {
    # ElementGroupsByProject Fields
  }
}

```

**Template for Query Variables:**

```
{
  "projectId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "filter" : "<SOME-ELEMENTGROUPFILTER-INPUT-TYPE-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| projectId*   [ID!](scalars.md) `non-null` | Project to retrieve elementGroups from. |
| --- | --- |
| filter   [ElementGroupFilterInput](inputs-elementgroupfilterinput.md) | RSQL filter to use for searching elementGroups. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [ElementGroups!](objects-elementgroups.md) `non-null` | Contains a list of ElementGroups returned in response to a query. |

## [Examples](#examples)
