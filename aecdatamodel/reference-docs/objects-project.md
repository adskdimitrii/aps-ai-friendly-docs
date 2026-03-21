# Project

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/project/

---

Objects

# Project

[](#)

Represents a project.

A project is a shared workspace for teams of people working together on a project, to store, organize, and manage all related entity data.

## [Fields](#fields)

Expand all

| id*   [ID!](scalars.md) `non-null` | The ID that uniquely identifies the project. |
| --- | --- |
| hub   [Hub](objects-hub.md) | An object representing the hub that contains this project. |
| elementGroups*   [ElementGroups!](objects-elementgroups.md) `non-null` | The ElementGroups within the project |
| filter   [ElementGroupFilterInput](inputs-elementgroupfilterinput.md) | Specifies how to filter |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |
| name   [String](scalars.md) | The name of the project. |
| alternativeIdentifiers   [ProjectAlternativeIdentifiers](objects-projectalternativeidentifiers.md) | Alternative identifiers for this project |
| folders   [Folders](objects-folders.md) | The top-level folders within the project. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |
| filter   [FolderFilterInput](inputs-folderfilterinput.md) | Specifies how to filter on folders. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Folder](objects-folder.md) | Represents a folder. A folder is a location for storing files, data, and other folders (sub-folders). |
| Query By | [project](queries-project.md) | Retrieves an object representing a project from a specified hub. A project is a shared workspace for teams of people to store, organize, and manage all related design data. |
| Query By | [projectByDataManagementAPIId](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/projectbydatamanagementapiid/) | Retrieves an object representing a project by its external id. A project is a shared workspace for teams of people to store, organize, and manage all related design data. |
