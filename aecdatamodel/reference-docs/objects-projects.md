# Projects

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/projects/

---

Objects

# Projects

[](#)

Contains a list of projects returned in response to a query.

## [Fields](#fields)

| pagination   [Pagination](objects-pagination.md) | Contains information about the current page, when results are split into multiple pages. |
| --- | --- |
| results*   [[Project]!](/en/docs/aecdatamodel/v1/reference/objects/project) `non-null` | An array that contains objects representing projects. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Hub](objects-hub.md) | Represents a hub. A hub is a container of projects, shared resources, and users with a common context. |
| Query By | [projects](queries-projects.md) | Retrieves all projects that match the specified filter criteria from a specified hub. |
