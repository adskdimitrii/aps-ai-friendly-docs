# Pagination

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/pagination/

---

Objects

# Pagination

[](#)

Contains information about the current page, when results are split into multiple pages.

## [Fields](#fields)

| cursor   [String](scalars.md) | The address of the next page, if one exists. If the current page is the last page, `cursor` is `null`. |
| --- | --- |
| pageSize   [Int](scalars.md) | The number of items in the response page. |

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Elementgroups](objects-elementgroups.md) | Contains a list of ElementGroups returned in response to a query. |
| Field Of | [Elementgroupversions](objects-elementgroupversions.md) | An array of versions. |
| Field Of | [Elements](objects-elements.md) | Contains a list of Elements returned in response to a query. |
| Field Of | [Folders](objects-folders.md) | A list of Folders returned in response to a query. A folder contains items, such as designs and sub-folders. |
| Field Of | [Hubs](objects-hubs.md) | Contains a list of hubs returned in response to a query. A hub is a container of projects, shared resources, and users with a common context. |
| Field Of | [Projects](objects-projects.md) | Contains a list of projects returned in response to a query. |
| Field Of | [Properties](objects-properties.md) | Object representing list of Properties. |
| Field Of | [Propertydefinitioncollections](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/propertydefinitioncollections/) | Contains a list of Property Definition Collections returned in response to a query. |
| Field Of | [Propertydefinitions](objects-propertydefinitions.md) | List of property definitions. |
| Field Of | [Referenceproperties](objects-referenceproperties.md) | Reference properties. |
| Field Of | [Users](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/users/) | Represents pagination and result of list of users |
