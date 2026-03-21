# DistinctPropertyValues

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/distinctpropertyvalues/

---

Objects

# DistinctPropertyValues

[](#)

Contains a list of DistinctPropertyValue returned in response to a query.

## [Fields](#fields)

Expand all

| definition   [PropertyDefinition](objects-propertydefinition.md) | Information about the Property of the distinct values returned. |
| --- | --- |
| values*   [[DistinctPropertyValue!]](/en/docs/aecdatamodel/v1/reference/objects/distinctpropertyvalue) `non-null` | An array of distinct property values. |
| limit   [Int](scalars.md) | Limit the number of distinct values returned. Does not support pagination. Default = 200, maximum = 2000. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Query By | [distinctPropertyValuesInElementGroupById](queries-distinctpropertyvaluesinelementgroupbyid.md) | Retrieves distinct values in an ElementGroup given a property definition ID. |
