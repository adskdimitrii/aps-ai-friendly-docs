# Folders

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/folders/

---

Objects

# Folders

[](#)

A list of Folders returned in response to a query.

A folder contains items, such as designs and sub-folders.

## [Fields](#fields)

| pagination   [Pagination](objects-pagination.md) | Contains information about the current page, when results are split into multiple pages. |
| --- | --- |
| results*   [[Folder!]](/en/docs/aecdatamodel/v1/reference/objects/folder) `non-null` | An array that contains objects representing items. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Folder](objects-folder.md) | Represents a folder. A folder is a location for storing files, data, and other folders (sub-folders). |
| Field Of | [Project](objects-project.md) | Represents a project. A project is a shared workspace for teams of people working together on a project, to store, organize, and manage all related entity data. |
| Query By | [foldersByFolder](queries-foldersbyfolder.md) | Retrieves all subfolders within a specified folder that meet the filter criteria specified by the `filter` argument. |
| Query By | [foldersByProject](queries-foldersbyproject.md) | Retrieves all top level folders under a specified project that meet the filter criteria specified by the `filter` argument. |
