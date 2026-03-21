# ElementGroup

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/elementgroup/

---

Objects

# ElementGroup

[](#)

Represents a Revit model.

## [Fields](#fields)

Expand all

| id*   [ID!](scalars.md) `non-null` | Globally unique identifier. |
| --- | --- |
| name   [String](scalars.md) | Name of the ElementGroup Container. |
| elements*   [Elements!](objects-elements.md) `non-null` | Get Elements |
| filter   [ElementFilterInput](inputs-elementfilterinput.md) | RSQL filter to use for searching elements. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |
| propertyDefinitions*   [PropertyDefinitions!](objects-propertydefinitions.md) `non-null` | Get all Property Definitions used in this elementGroup |
| filter   [PropertyDefinitionFilterInput](inputs-propertydefinitionfilterinput.md) | Specifies how to filter on property definitions. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |
| version   [ElementGroupVersion](objects-elementgroupversion.md) | Specific version of this ElementGroup. |
| versionHistory*   [ElementGroupVersionHistory!](objects-elementgroupversionhistory.md) `non-null` | Version history for this elementGroup |
| createdBy   [User](objects-user.md) | User responsible for creating this elementGroup |
| createdOn   [DateTime](scalars.md) | Timestamp of elementGroup creation |
| lastModifiedBy   [User](objects-user.md) | Latest user who modified this elementGroup |
| lastModifiedOn   [DateTime](scalars.md) | Latest timestamp when this elementGroup was modified |
| alternativeIdentifiers   [ElementGroupAlternativeIdentifiers](objects-elementgroupalternativeidentifiers.md) | Alternative identifiers for this elementGroup |
| parentFolder   [Folder](objects-folder.md) | Parent folder containing this elementGroup |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Element](objects-element.md) | Represents an element type. |
| Field Of | [Elementgroupextractionstatus](objects-elementgroupextractionstatus.md) | Information about elementGroup extraction status. |
| Field Of | [Elementgroupversion](objects-elementgroupversion.md) | Represents a single version of an ElementGroup. |
| Query By | [elementGroupAtTip](queries-elementgroupattip.md) | Retrieves latest elementGroup data based on given ID. |
| Query By | [elementGroupByVersionNumber](queries-elementgroupbyversionnumber.md) | Retrieves elementGroup by version number and ID. |
