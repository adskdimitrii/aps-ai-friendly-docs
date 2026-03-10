# PropertySet

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/PropertySet/

---

Autodesk.Viewing

# PropertySet

The PropertySet class allows for aggregation of properties with the same names and categories. To get an instance of this class use [Autodesk.Viewing.Model#getPropertySet](Viewing-Model.md#getPropertySet/).

## [new PropertySet(result)](#new-propertyset-result)

### Parameters

| result*   Object |  |
| --- | --- |

* Required

### Examples

```
const dbIds = viewer.getSelection();
// Use the model's getPropertySet to get the PropertySet instance for the specified dbIds
viewer.model.getPropertySet(dbIds).then((propSet) => {
   // iterate, aggregate, etc
});

```

---

# Methods

## [forEach(callback)](#foreach-callback)

Iterates over all of the common properties. The callback is invoked on each key in the property map.

### Parameters

| callback*   [forEachCallback](globals-TypeDefs-forEachCallback.md) | Called for each entry in the map |
| --- | --- |

* Required

## [getAggregation(properties)](#getaggregation-properties)

Returns an object containing aggregated values. see [Autodesk.Viewing.PropertySet#forEach](Viewing-PropertySet.md#forEach/)

### Parameters

| properties*   Array.<Object>, String | either the key in the object or an array of properties |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| [AggregatedResult](globals-TypeDefs-AggregatedResult.md) | Object with all aggregated values |

### Examples

```
propertySet.forEach((key, properties) => {
  const aggregation = propertySet.getAggregation(key);
});

```

---

## [getValue2PropertiesMap(properties)](#getvalue2propertiesmap-properties)

Returns an object with a key representing the property’s displayValue and the value being all of the property names associated with it.

see [Autodesk.Viewing.PropertySet#forEach](Viewing-PropertySet.md#forEach/) see [PropertyResult](globals-TypeDefs-PropertyResult.md)

### Parameters

| properties*   Array.<Object>, String | either the key in the object or an array of properties |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Object | The key representing a common displayValue and the value representing all of the PropertyResult sharing that displaValue |

### Examples

```
propertySet.forEach((name, properties) => {
  const commonValues = propertySet.getValue2PropertiesMap(key);
});

```

---

## [getValidIds(displayName, displayCategory)](#getvalidids-displayname-displaycategory)

Searches all of the keys in the map object and returns all valid keys that either match the displayName or categoryName.

### Parameters

| displayName*   String | the display name |
| --- | --- |
| displayCategory*   String | the category name |

* Required

### Returns

| type | description |
| --- | --- |
| Array.<String> | an array of valid map ids |

## [getDbIds()](#getdbids)

Get the dbIds that are associated with the propertySet

### Returns

| type | description |
| --- | --- |
| Array.<number> | an array of dbids associated with the PropertySet |

## [getVisibleKeys()](#getvisiblekeys)

Returns an array of keys that contain visible properties

### Returns

| type | description |
| --- | --- |
| Array.<string> | array of keys |

## [getKeysWithCategories()](#getkeyswithcategories)

Returns an array of keys that have properties with displayCategories

### Returns

| type | description |
| --- | --- |
| Array.<string> | array of keys |

## [merge(propertySet)](#merge-propertyset)

Merges the passed in PropertySet map with the current PropertySet’s map.

### Parameters

| propertySet*   [Autodesk.Viewing.PropertySet](Viewing-PropertySet.md) | A PropertySet instance |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.PropertySet](Viewing-PropertySet.md) | returns from the passed in propertySet merged |
