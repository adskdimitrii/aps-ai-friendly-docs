# Hubs

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/hubs/

---

Objects

# Hubs

[](#)

Contains a list of hubs returned in response to a query.

A hub is a container of projects, shared resources, and users with a common context.

## [Fields](#fields)

| pagination   [Pagination](objects-pagination.md) | Contains information about the current page, when results are split into multiple pages. |
| --- | --- |
| results*   [[Hub]!](/en/docs/aecdatamodel/v1/reference/objects/hub) `non-null` | An array that contains objects representing hubs. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Query By | [hubs](queries-hubs.md) | Retrieves all hubs that match the specified criteria. A Hub is a container of projects, shared resources, and users with a common context. |
