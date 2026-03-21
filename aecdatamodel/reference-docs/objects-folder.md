# Folder

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/folder/

---

Objects

# Folder

[](#)

Represents a folder.

A folder is a location for storing files, data, and other folders (sub-folders).

## [Fields](#fields)

Expand all

| id*   [ID!](scalars.md) `non-null` | The ID that uniquely identifies the folder. |
| --- | --- |
| project   [Project](objects-project.md) | An object representing the project that contains this folder. |
| hub   [Hub](objects-hub.md) | An object representing the hub that contains this folder. |
| parentFolder   [Folder](objects-folder.md) | The folder that contains this folder. |
| name   [String](scalars.md) | A human-readable name to identify this folder. |
| createdOn   [DateTime](scalars.md) | Indicates when this folder was created. |
| createdBy   [User](objects-user.md) | An object representing the user who created this folder. |
| lastModifiedOn   [DateTime](scalars.md) | Indicates when this folder was most recently modified. |
| lastModifiedBy   [User](objects-user.md) | An object representing the user who made the most recent modification. |
| objectCount   [Int](scalars.md) | Indicates the number items (folders and files) contained in this folder. |
| folders   [Folders](objects-folders.md) | Contains a list of folders that meet the specified filter criteria. You specify the filter criteria as an input to this field. Expand to see the inputs for this field. |
| filter   [FolderFilterInput](inputs-folderfilterinput.md) | Specifies how to filter on folders. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Elementgroup](objects-elementgroup.md) | Represents a Revit model. |
| Field Of | [Folder](objects-folder.md) | Represents a folder. A folder is a location for storing files, data, and other folders (sub-folders). |
| Field Of | [Folders](objects-folders.md) | A list of Folders returned in response to a query. A folder contains items, such as designs and sub-folders. |
| Query By | [folder](queries-folder.md) | Retrieve folder specified by the provided Id |
