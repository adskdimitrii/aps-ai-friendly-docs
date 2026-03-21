# propertyDefinitionsByElementGroup

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/propertydefinitionsbyelementgroup/

---

Queries

# propertyDefinitionsByElementGroup

[](#)

Get all Property Definitions used in specified elementGroup

**Template for Query:**

```
query GetPropertyDefinitionsByElementGroup($elementGroupId: ID!, $filter: PropertyDefinitionFilterInput, $pagination: PaginationInput) {
  propertyDefinitionsByElementGroup(elementGroupId: $elementGroupId, filter: $filter, pagination: $pagination) {
    # PropertyDefinitionsByElementGroup Fields
  }
}

```

**Template for Query Variables:**

```
{
  "elementGroupId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "filter" : "<SOME-PROPERTYDEFINITIONFILTER-INPUT-TYPE-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| elementGroupId*   [ID!](https://aps.autodesk.com/en/docs/aecdatamodel-beta/v1/reference/scalars/) `non-null` | ElementGroup to retrieve property definitions of. |
| --- | --- |
| filter   [PropertyDefinitionFilterInput](https://aps.autodesk.com/en/docs/aecdatamodel-beta/v1/reference/inputs/propertydefinitionfilterinput/) | Specifies how to filter on property definitions. |
| pagination   [PaginationInput](https://aps.autodesk.com/en/docs/aecdatamodel-beta/v1/reference/inputs/paginationinput/) | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [PropertyDefinitions!](https://aps.autodesk.com/en/docs/aecdatamodel-beta/v1/reference/objects/propertydefinitions/) `non-null` | List of property definitions. |
