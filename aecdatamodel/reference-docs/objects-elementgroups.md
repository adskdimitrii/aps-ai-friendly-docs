# ElementGroups

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/elementgroups/

---

Objects

# ElementGroups

[](#)

Contains a list of ElementGroups returned in response to a query.

## [Fields](#fields)

| pagination   [Pagination](objects-pagination.md) | Contains information about the current page when results are split into multiple pages. |
| --- | --- |
| results*   [[ElementGroup]!](/en/docs/aecdatamodel/v1/reference/objects/elementgroup) `non-null` | An array containing ElementGroups |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Project](objects-project.md) | Represents a project. A project is a shared workspace for teams of people working together on a project, to store, organize, and manage all related entity data. |
| Query By | [elementGroupsByHub](queries-elementgroupsbyhub.md) | Retrieves elementGroups in the given hub, using additional RSQL filters if provided. |
| Query By | [elementGroupsByProject](queries-elementgroupsbyproject.md) | Retrieves elementGroups in the given project, using additional RSQL filters if provided. |
| Query By | [elementGroupsByFolder](queries-elementgroupsbyfolder.md) | Retrieves elementGroups in the given folder, using additional RSQL filters if provided. |
| Query By | [elementGroupsByFolderAndSubFolders](queries-elementgroupsbyfolderandsubfolders.md) | Retrieves elementGroups in the given folder and it’s sub-folders recursively, using additional RSQL filters if provided. |
