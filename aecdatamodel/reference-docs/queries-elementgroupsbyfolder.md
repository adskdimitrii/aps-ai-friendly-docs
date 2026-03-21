# elementGroupsByFolder

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/elementgroupsbyfolder/

---

Queries

# elementGroupsByFolder

[](#)

Retrieves elementGroups in the given folder, using additional RSQL filters if provided.

**Template for Query:**

```
query GetElementGroupsByFolder($projectId: ID!, $folderId: ID!, $filter: ElementGroupFilterInput, $pagination: PaginationInput) {
  elementGroupsByFolder(projectId: $projectId, folderId: $folderId, filter: $filter, pagination: $pagination) {
    # ElementGroupsByFolder Fields
  }
}

```

**Template for Query Variables:**

```
{
  "projectId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "folderId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "filter" : "<SOME-ELEMENTGROUPFILTER-INPUT-TYPE-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| projectId*   [ID!](scalars.md) `non-null` | Project to retrieve elementGroups from. |
| --- | --- |
| folderId*   [ID!](scalars.md) `non-null` | Folder to retrieve elementGroups from. |
| filter   [ElementGroupFilterInput](inputs-elementgroupfilterinput.md) | RSQL filter to use for searching elementGroups. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [ElementGroups!](objects-elementgroups.md) `non-null` | Contains a list of ElementGroups returned in response to a query. |

## [Examples](#examples)
