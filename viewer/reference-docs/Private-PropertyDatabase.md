# PropertyDatabase

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Private/PropertyDatabase/

---

Autodesk.Viewing.Private

# PropertyDatabase

The Property Database contains property information for each part of a model. The data is read-only, since it has been packed to optimize memory footprint. Itâs implemented as an Entity-Atribute-Value (EAV) set of tables. LMV keeps the PropertyDatabase in a browser worker thread to prevent compute-intensive methods to block the main browser UI thread. Words âAttributeâ and âPropertyâ are use interchangeably.

## [new PropertyDatabase(dbjsons, fileType)](#new-propertydatabase-dbjsons-filetype)

### Parameters

| dbjsons*   object | is expected to be of the form {{ attrs: {filename1:x, filename2:y}, ids: {filename1:xâ¦ }, values: {â¦ }, offsets: {â¦ }, avs: {â¦ } } where each of the elements of each array is a pair of the original name and the unzipped raw byte array buffer corresponding to the respective property database constituent. In the current implementation each array is expected to only have one name-value element. |
| --- | --- |
| fileType*   string | Optional file type (ârvtâ, âdwgâ, etc.) for applying file-specific naming logic |

* Required

# Methods

## [getObjectCount()](#getobjectcount)

Obtains the number of database ids (dbIds) available. These ids range betwee 1 (inclusive) up to getObjectCount() (exclusive).

### Returns

| type | description |
| --- | --- |
| number |  |

## [getAttrValue(attrId, valId, integerHint)](#getattrvalue-attrid-valid-integerhint)

Obtains the actual value of a property.

### Parameters

| attrId*   number | The attribute id |
| --- | --- |
| valId*   number | The value id |
| integerHint   boolean | If true the return value will be casted to integer. |

* Required

### Returns

| type | description |
| --- | --- |
|  |  |

## [getObjectProperties(dbId, propFilter, ignoreHidden, propIgnored)](#getobjectproperties-dbid-propfilter-ignorehidden-propignored)

Obtains all properties for a given database id.

### Parameters

| dbId*   number | The database id |
| --- | --- |
| propFilter   Array.<string> | Array of property names to return values for. Use null for no filtering. |
| ignoreHidden   boolean | true to ignore hidden properties. |
| propIgnored   Array.<string> | Array of property names to not include in the return value. |

* Required

### Returns

| type | description |
| --- | --- |
| object | consisting of attributes `name`, `dbId`, `properties` and `externalId`. |

## [getExternalIdMapping(extIdFilter)](#getexternalidmapping-extidfilter)

Obtains a map between each database id (dbId) and their corresponding external-id. The external-id is the identifier used by the source file. Example: A translated Revit file has a wall with dbId=1, but in Revit (desktop application) the identifier of that wall is âWall-06-some-guid-hereâ.

### Parameters

| extIdFilter   Array.<number> | Limits the result to only contain the ids in this array. |
| --- | --- |

### Returns

| type | description |
| --- | --- |
| object | map from dbId into external-id. |

## [getSearchTerms(searchText)](#getsearchterms-searchtext)

Given a text string, returns an array of individual words separated by white spaces. Will preserve white spacing within double quotes.

### Parameters

| searchText*   string | Text to search |
| --- | --- |

* Required

## [bruteForceFind(propertyName)](#bruteforcefind-propertyname)

Given a property name, it returns an array of ids that contain it.

### Parameters

| propertyName*   string | Property name |
| --- | --- |

* Required

## [getLayerToNodeIdMapping()](#getlayertonodeidmapping)

Specialized function that returns: { âlayer-name-1â: [id1, id2, â¦, idN], âlayer-name-2â: [idX, idY, â¦, idZ], â¦ }

## [getAttributeDef(attrId)](#getattributedef-attrid)

Unpacks an attribute value into all available components.

### Parameters

| attrId*   number | The attribute id. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| object | containing `name`, `category`, `dataType`, `dataTypeContext`, `description`, `displayName` and `flags`. |

## [enumAttributes(cb)](#enumattributes-cb)

Invokes a callback function for each attribute-id in the model.

### Parameters

| cb*   function | Callback invoked |
| --- | --- |

* Required

### Examples

```
pdb.enumAttributes(function(attrId, attrDef) {
        // attrDef is an object
        if (attrDef.name === 'name') {
            return true; // return true to stop iteration.
        }
   })

```

---

## [enumObjectProperties(dbId, cb)](#enumobjectproperties-dbid-cb)

Iterates over all properties for a given database id and invokes the supplied callback function.

### Parameters

| dbId*   number | The attribute id. |
| --- | --- |
| cb*   function | callback function, that receives 2 arguments: attribute-id (`attrId`) and value-id (`valId`). Have the function return `true` to abort iteration. |

* Required

## [getPropertiesSubsetWithInheritance(dbId, desiredAttrIds, dstValIds)](#getpropertiessubsetwithinheritance-dbid-desiredattrids-dstvalids)

Given an object ID, returns the corresponding value IDs for the given list of attribute Ids. Takes into account instance_of inheritance of properties.

### Parameters

| dbId*   number | Integer input object ID |
| --- | --- |
| desiredAttrIds*   object | An optional map of the requested attribute Ids, where desiredAttrIds[attrId] is âtruthyâ. If not provided, all properties will be returned. |
| dstValIds*   object | A storage target map, such that dstValIds[attrId] will be the resulting value ID. It is the responsibility of the caller to zero initialize this map. |

* Required

### Returns

| type | description |
| --- | --- |
| Array.<number> | A flat list of integers attributeId - valueId pairs. This is in addition to the dstValIds, for cases where the object has mutliple properties of the same type, e.g. children, **viewable_in**, etc. |

## [findLayers()](#findlayers)

Iterates over the property database and finds all layers.

### Returns

| type | description |
| --- | --- |
| object |  |

## [enumObjects(cb, fromId, toId)](#enumobjects-cb-fromid-toid)

Iterates over all database ids and invokes a callback function.

### Parameters

| cb*   function | callback function. Receives a single parameter: the database-id. Have the function return true to abort iteration. |
| --- | --- |
| fromId*   number | starting id (inclusive) |
| toId*   number | end id (exclusive) |

* Required

## [attributeHidden(attrId)](#attributehidden-attrid)

Checks whether an attribute is hidden or not.

### Parameters

| attrId*   number | The attribute id. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the attribute is a hidden one. |

## [numberOfAttributes()](#numberofattributes)

Returns count of the number of attributes

### Returns

| type | description |
| --- | --- |
| number |  |

## [numberOfValues()](#numberofvalues)

Returns count of the number of values

### Returns

| type | description |
| --- | --- |
| number |  |
