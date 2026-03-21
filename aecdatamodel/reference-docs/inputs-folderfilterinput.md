# FolderFilterInput

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/folderfilterinput/

---

Inputs

# FolderFilterInput

[](#)

Specifies how to filter folders.

## [Fields](#fields)

| name   [String](scalars.md) | The name of the item you want to match. Currently, only exact matches are supported. |
| --- | --- |

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Argument for Query | [foldersByFolder](queries-foldersbyfolder.md) | Retrieves all subfolders within a specified folder that meet the filter criteria specified by the `filter` argument. |
| Argument for Query | [foldersByProject](queries-foldersbyproject.md) | Retrieves all top level folders under a specified project that meet the filter criteria specified by the `filter` argument. |
| Argument for Field | [Folder](objects-folder.md) | Represents a folder. A folder is a location for storing files, data, and other folders (sub-folders). |
| Argument for Field | [Project](objects-project.md) | Represents a project. A project is a shared workspace for teams of people working together on a project, to store, organize, and manage all related entity data. |
