# Hub

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/hub/

---

Objects

# Hub

[](#)

Represents a hub.

A hub is a container of projects, shared resources, and users with a common context.

## [Fields](#fields)

Expand all

| id*   [ID!](scalars.md) `non-null` | The ID that uniquely identifies the hub. |
| --- | --- |
| name   [String](scalars.md) | A human-readable name to identify the hub. |
| projects   [Projects](objects-projects.md) | Contains a list of projects within the specified hub. Expand to see the inputs for this field. |
| filter   [ProjectFilterInput](inputs-projectfilterinput.md) | Specifies how to filter a list of projects. You can filter by name. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |
| alternativeIdentifiers   [HubAlternativeIdentifiers](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/hubalternativeidentifiers/) | Alternative identifiers for this hub |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Folder](objects-folder.md) | Represents a folder. A folder is a location for storing files, data, and other folders (sub-folders). |
| Field Of | [Project](objects-project.md) | Represents a project. A project is a shared workspace for teams of people working together on a project, to store, organize, and manage all related entity data. |
| Query By | [hub](queries-hub.md) | Retrieves an object representing a hub. A Hub is a container of projects, shared resources, and users with a common context. |
| Query By | [hubByDataManagementAPIId](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/hubbydatamanagementapiid/) | Retrieves an object representing a hub by its external id. A Hub is a container of projects, shared resources, and users with a common context. |
