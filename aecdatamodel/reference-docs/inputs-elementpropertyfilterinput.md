# ElementPropertyFilterInput

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/elementpropertyfilterinput/

---

Inputs

# ElementPropertyFilterInput

[](#)

Query input for filtering Elements by their properties

## [Fields](#fields)

| name   [String](scalars.md) | Name of the property |
| --- | --- |
| id   [String](scalars.md) | ID of the property |
| value   [[String!]](/en/docs/aecdatamodel/v1/reference/scalars) | Value that the property should have |
| valueWithComparator   [[ValueComparatorInput!]](/en/docs/aecdatamodel/v1/reference/inputs/valuecomparatorinput) | Value that the property should have and comparator to apply |

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Argument for Input | [elementfilterinput](inputs-elementfilterinput.md) | Query input for filtering Elements. |
