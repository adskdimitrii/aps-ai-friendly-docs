# ProjectFilterInput

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/projectfilterinput/

---

Inputs

# ProjectFilterInput

[](#)

Specifies how to filter projects.

## [Fields](#fields)

| name   [String](scalars.md) | The name of the project you want to match. Currently, only exact matches are supported. |
| --- | --- |

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Argument for Query | [projects](queries-projects.md) | Retrieves all projects that match the specified filter criteria from a specified hub. |
| Argument for Field | [Hub](objects-hub.md) | Represents a hub. A hub is a container of projects, shared resources, and users with a common context. |
