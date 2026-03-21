# ElementGroupFilterInput

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/elementgroupfilterinput/

---

Inputs

# ElementGroupFilterInput

[](#)

Query input for filtering ElementGroups.

## [Fields](#fields)

| query   [String](scalars.md) | Query filter in RSQL format to search for elementGroups. For more details, please refer to: [Advanced Filtering](https://aps.autodesk.com/en/docs/aecdatamodel/v1/developers_guide/filtering/advanced-filtering/) |
| --- | --- |
| name   [[String!]](/en/docs/aecdatamodel/v1/reference/scalars) | Filter for elementGroups with a specified name |
| createdBy   [[String!]](/en/docs/aecdatamodel/v1/reference/scalars) | Filter for elementGroups created by a specified user (email) |
| lastModifiedBy   [[String!]](/en/docs/aecdatamodel/v1/reference/scalars) | Filter for elementGroups last modified by a specified user (email) |
| fileUrn   [[String!]](/en/docs/aecdatamodel/v1/reference/scalars) | Filter for elementGroups with a specified file URN |

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Argument for Query | [elementGroupsByHub](queries-elementgroupsbyhub.md) | Retrieves elementGroups in the given hub, using additional RSQL filters if provided. |
| Argument for Query | [elementGroupsByProject](queries-elementgroupsbyproject.md) | Retrieves elementGroups in the given project, using additional RSQL filters if provided. |
| Argument for Query | [elementGroupsByFolder](queries-elementgroupsbyfolder.md) | Retrieves elementGroups in the given folder, using additional RSQL filters if provided. |
| Argument for Query | [elementGroupsByFolderAndSubFolders](queries-elementgroupsbyfolderandsubfolders.md) | Retrieves elementGroups in the given folder and it’s sub-folders recursively, using additional RSQL filters if provided. |
| Argument for Field | [Project](objects-project.md) | Represents a project. A project is a shared workspace for teams of people working together on a project, to store, organize, and manage all related entity data. |
