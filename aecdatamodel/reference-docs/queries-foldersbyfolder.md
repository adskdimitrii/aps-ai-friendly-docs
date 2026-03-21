# foldersByFolder

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/foldersbyfolder/

---

Queries

# foldersByFolder

[](#)

Retrieves all subfolders within a specified folder that meet the filter criteria specified by the `filter` argument.

**Template for Query:**

```
query GetFoldersByFolder($projectId: ID!, $folderId: ID!, $filter: FolderFilterInput, $pagination: PaginationInput) {
  foldersByFolder(projectId: $projectId, folderId: $folderId, filter: $filter, pagination: $pagination) {
    # FoldersByFolder Fields
  }
}

```

**Template for Query Variables:**

```
{
  "projectId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "folderId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "filter" : "<SOME-FOLDERFILTER-INPUT-TYPE-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| projectId*   [ID!](scalars.md) `non-null` | The ID of the project that contains the items. |
| --- | --- |
| folderId*   [ID!](scalars.md) `non-null` | The ID of the folder that contains the subfolders. |
| filter   [FolderFilterInput](inputs-folderfilterinput.md) | Specifies how to filter on folders. You can filter by name. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [Folders](objects-folders.md) | A list of Folders returned in response to a query. A folder contains items, such as designs and sub-folders. |

## [Examples](#examples)
