# foldersByProject

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/foldersbyproject/

---

Queries

# foldersByProject

[](#)

Retrieves all top level folders under a specified project that meet the filter criteria specified by the `filter` argument.

**Template for Query:**

```
query GetFoldersByProject($projectId: ID!, $filter: FolderFilterInput, $pagination: PaginationInput) {
  foldersByProject(projectId: $projectId, filter: $filter, pagination: $pagination) {
    # FoldersByProject Fields
  }
}

```

**Template for Query Variables:**

```
{
  "projectId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "filter" : "<SOME-FOLDERFILTER-INPUT-TYPE-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| projectId*   [ID!](scalars.md) `non-null` | The ID of the project that contains the items. |
| --- | --- |
| filter   [FolderFilterInput](inputs-folderfilterinput.md) | Specifies how to filter on folders. You can filter by name. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [Folders](objects-folders.md) | A list of Folders returned in response to a query. A folder contains items, such as designs and sub-folders. |

## [Examples](#examples)
