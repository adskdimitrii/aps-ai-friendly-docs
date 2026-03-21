# PaginationInput

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/paginationinput/

---

Inputs

# PaginationInput

[](#)

Specifies how to split the response into multiple pages.

## [Fields](#fields)

| cursor   [String](scalars.md) | Specifies what page to fetch. If you don’t specify `cursor`, fetches the first page. |
| --- | --- |
| limit   [Int](scalars.md) | The maximum number of items to return in a page. The default value for `limit` varies from query to query. |

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Argument for Query | [elementGroupsByHub](queries-elementgroupsbyhub.md) | Retrieves elementGroups in the given hub, using additional RSQL filters if provided. |
| Argument for Query | [elementGroupsByProject](queries-elementgroupsbyproject.md) | Retrieves elementGroups in the given project, using additional RSQL filters if provided. |
| Argument for Query | [elementGroupsByFolder](queries-elementgroupsbyfolder.md) | Retrieves elementGroups in the given folder, using additional RSQL filters if provided. |
| Argument for Query | [elementGroupsByFolderAndSubFolders](queries-elementgroupsbyfolderandsubfolders.md) | Retrieves elementGroups in the given folder and it’s sub-folders recursively, using additional RSQL filters if provided. |
| Argument for Query | [elementsByHub](queries-elementsbyhub.md) | Retrieves elements from given hub, using additional RSQL filters if provided. |
| Argument for Query | [elementsByProject](queries-elementsbyproject.md) | Retrieves elements from given project, using additional RSQL filters if provided. |
| Argument for Query | [elementsByFolder](queries-elementsbyfolder.md) | Retrieves elements from given folder, using additional RSQL filters if provided. |
| Argument for Query | [elementsByElementGroup](queries-elementsbyelementgroup.md) | Retrieves elements from given elementGroup, using additional RSQL filters if provided. |
| Argument for Query | [elementsByElementGroups](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elementsbyelementgroups/) | Retrieves elements from a given set of elementGroups, using additional RSQL filters if provided. |
| Argument for Query | [elementsByElementGroupAtVersion](queries-elementsbyelementgroupatversion.md) | Retrieves elements from given elementGroup at given elementGroup version, using additional RSQL filters if provided. |
| Argument for Query | [hubs](queries-hubs.md) | Retrieves all hubs that match the specified criteria. A Hub is a container of projects, shared resources, and users with a common context. |
| Argument for Query | [projects](queries-projects.md) | Retrieves all projects that match the specified filter criteria from a specified hub. |
| Argument for Query | [foldersByFolder](queries-foldersbyfolder.md) | Retrieves all subfolders within a specified folder that meet the filter criteria specified by the `filter` argument. |
| Argument for Query | [foldersByProject](queries-foldersbyproject.md) | Retrieves all top level folders under a specified project that meet the filter criteria specified by the `filter` argument. |
| Argument for Field | [Element](objects-element.md) | Represents an element type. |
| Argument for Field | [ElementGroup](objects-elementgroup.md) | Represents a Revit model. |
| Argument for Field | [ElementGroupVersionHistory](objects-elementgroupversionhistory.md) | Information related to versions of an elementGroup. |
| Argument for Field | [Folder](objects-folder.md) | Represents a folder. A folder is a location for storing files, data, and other folders (sub-folders). |
| Argument for Field | [Hub](objects-hub.md) | Represents a hub. A hub is a container of projects, shared resources, and users with a common context. |
| Argument for Field | [Project](objects-project.md) | Represents a project. A project is a shared workspace for teams of people working together on a project, to store, organize, and manage all related entity data. |
| Argument for Field | [PropertyDefinitionCollection](objects-propertydefinitioncollection.md) | Data object that represents property definition collection. |
