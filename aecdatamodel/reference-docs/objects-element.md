# Element

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/element/

---

Objects

# Element

[](#)

Represents an element type.

## [Fields](#fields)

Expand all

| id*   [ID!](scalars.md) `non-null` | Globally unique identifier for an Element. |
| --- | --- |
| name*   [String!](scalars.md) `non-null` | The human-readable name of the Element |
| properties*   [Properties!](objects-properties.md) `non-null` | Query for specific Properties |
| filter   [PropertyFilterInput](inputs-propertyfilterinput.md) | Specifies which properties to return. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |
| includeReferencesProperties   [String](scalars.md) | Must be set to the reference name. |
| references   [ReferenceProperties](objects-referenceproperties.md) | Represents information that further defines the Element (e.g. Type data) |
| filter   [ReferencePropertyFilterInput](inputs-referencepropertyfilterinput.md) | Specifies which reference properties to return. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |
| createdBy   [User](objects-user.md) | User responsible for creating this element |
| createdOn   [DateTime](scalars.md) | Timestamp of element creation |
| lastModifiedBy   [User](objects-user.md) | Latest user who modified the data |
| lastModifiedOn   [DateTime](scalars.md) | Latest timestamp when the element was modified |
| referencedBy   [Elements](objects-elements.md) | Elements which have references to the current element |
| name*   [String!](scalars.md) `non-null` | The name of relationship to find references for. |
| filter   [ElementFilterInput](inputs-elementfilterinput.md) | Specifies how to filter elements with references to current element. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |
| alternativeIdentifiers   [ElementAlternativeIdentifiers](objects-elementalternativeidentifiers.md) | Alternative identifiers for this element |
| elementGroup   [ElementGroup](objects-elementgroup.md) | The elementGroup which this element belongs to. |
| components*   [ECSComponents!](objects-ecscomponents.md) `non-null` | General data about the element |
| filter   [ComponentsFilterInput](inputs-componentsfilterinput.md) |  |
| pagination   [PaginationInput](inputs-paginationinput.md) |  |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Addextensionpropertiespayload](objects-addextensionpropertiespayload.md) | Payload for adding extension properties to elements. |
| Field Of | [Extensioncomponent](objects-extensioncomponent.md) | Component that links an extension to the entity it is extending. |
| Field Of | [Referenceproperty](objects-referenceproperty.md) | A reference property which describes relationship between elements. |
| Field Of | [Removeextensionpropertiespayload](objects-removeextensionpropertiespayload.md) | Payload for removing extension properties from elements. |
| Field Of | [Updateextensionpropertiespayload](objects-updateextensionpropertiespayload.md) | Payload for updating extension properties on elements. |
| Query By | [elementAtTip](queries-elementattip.md) | Retrieves element using given ID. |
