# PropertyResult

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/globals/TypeDefs/PropertyResult/

---

Type Definitions

# PropertyResult

Element type for [GetPropertiesResult.properties](/en/docs/viewer/v7/reference/globals/TypeDefs/GetPropertiesResult/).

# Properties

| attributeName   string | The property identifying name. |
| --- | --- |
| displayCategory   string, null | Category the attribute belongs into. |
| displayName   string | A user facing label for the property. It could contain the same value as attributeName. |
| displayValue   string, number, boolean | The value for the property. |
| hidden   boolean | Whether the property is meant to be user facing or not. |
| precision   number | Applies only to numerical displayValues. |
| type   object | An enumeration value of type AttributeType indicating how to interpret displayValue. |
| units   string, null | The units associated with displayValue. |
