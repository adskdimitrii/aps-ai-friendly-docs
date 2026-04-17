# Model

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/Model/

---

Autodesk.Viewing

# Model

Core class representing the geometry.

## [new Model()](#new-model)

# Methods

## [getInstanceTree()](#getinstancetree)

### Returns

| type | description |
| --- | --- |
| [InstanceTree](Private-InstanceTree.md) | Instance tree of the model if available, otherwise null. |

## [getFuzzyBox(options)](#getfuzzybox-options)

Computes Bounding box of all fragments, but excluding outliers.

### Parameters

Expand all

| options   Object |  |
| --- | --- |
| quantil   float | in [0,1]. Relative amount of fragments that we consider computation. By default, we consider the 75% of fragments that are closest to the center. |
| center   float | Center from which we collect the closest shapes. By default, we use the center of mass. |
| ignoreTransforms   boolean | Ignore modelMatrix and animation transforms |
| allowlist   Array.<number> | Fragments to include in fuzzybox, by index. |

### Returns

| type | description |
| --- | --- |
| THREE.Box3 |  |

## [getBoundingBox(ignoreTransform, excludeShadow)](#getboundingbox-ignoretransform-excludeshadow)

### Parameters

| ignoreTransform   boolean | Set to true to return the original bounding box in model space coordinates. |
| --- | --- |
| excludeShadow   boolean | Remove shadow geometry (if exists) from model bounds. |

### Returns

| type | description |
| --- | --- |
| THREE.Box3 | Bounding box of the model if available, otherwise null. |

## [is2d()](#is2d)

### Returns

| type | description |
| --- | --- |
| boolean | Whether the model is 2D. |

## [is3d()](#is3d)

### Returns

| type | description |
| --- | --- |
| boolean | Whether the model is 3D. |

## [isSVF2()](#issvf2)

### Returns

| type | description |
| --- | --- |
| boolean | True if the model is an SVF2 file - which supports sharing of materials and geometry. |

## [isPdf(onlyPdfSource)](#ispdf-onlypdfsource)

### Parameters

| onlyPdfSource*   boolean | Set to true in order to verify that the source file of the model is PDF. Some design files can get extracted to PDFs for example, and in that case, when using the flag, we’ll get false as a result. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the model is created from a PDF file. |

## [isRevitPdf()](#isrevitpdf)

### Returns

| type | description |
| --- | --- |
| boolean | True if the model is a PDF that was created from a Revit source file. |

## [isSmartPdf()](#issmartpdf)

### Returns

| type | description |
| --- | --- |
| boolean | True if the model is a Smart PDF that was created by our translation pipeline. |

## [isLeaflet()](#isleaflet)

### Returns

| type | description |
| --- | --- |
| boolean | True if the model is created from an image file. |

## [isPageCoordinates()](#ispagecoordinates)

By default, Leaflet documents are being loaded in a normalized coordinate system. Only when using `fitPaperSize` load option, the model will be loaded in page coordinates, like every other 2D model.

### Returns

| type | description |
| --- | --- |
| boolean | True if the model is loaded in page coordinates. |

## [isSceneBuilder()](#isscenebuilder)

### Returns

| type | description |
| --- | --- |
| boolean | True if the model is created using Autodesk.Viewing.SceneBuilder extension |

## [getData()](#getdata)

Returns the geometry data.

### Returns

| type | description |
| --- | --- |
| Object | Data that represents the geometry. |

## [getDocumentNode()](#getdocumentnode)

Returns an object wrapping the bubble/manifest entry for the loaded geometry. Contains data such as the viewableID, guid, role…

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) |  |

## [getRoot()](#getroot)

Returns the root of the geometry node graph.

### Returns

| type | description |
| --- | --- |
| object | The root of the geometry node graph. Null if it doesn’t exist. |

## [getRootId()](#getrootid)

Returns the root of the geometry node graph.

### Returns

| type | description |
| --- | --- |
| number | The ID of the root or 0 if it doesn’t exist. |

## [getUnitData(unit)](#getunitdata-unit)

Returns an object that contains the standard unit string (unitString) and the scale value (unitScale).

### Parameters

| unit*   string | Unit name from the metadata |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| object | This object contains the standardized unit string (unitString) and a unit scaling value (unitScale) |

## [getUnitScale()](#getunitscale)

Returns the scale factor of model’s distance unit to meters.

### Returns

| type | description |
| --- | --- |
| number | The scale factor of the model’s distance unit to meters or unity if the units aren’t known. |

## [getUnitString()](#getunitstring)

Returns a standard string representation of the model’s distance unit.

### Returns

| type | description |
| --- | --- |
| string | Standard representation of model’s unit distance or null if it is not known. |

## [getDisplayUnit()](#getdisplayunit)

Returns a standard string representation of the model’s display unit.

### Returns

| type | description |
| --- | --- |
| string | Standard representation of model’s display unit or null if it is not known. |

## [getMetadata(itemName, subitemName, defaultValue)](#getmetadata-itemname-subitemname-defaultvalue)

Return metadata value.

### Parameters

| itemName*   string | Metadata item name. |
| --- | --- |
| subitemName   string | Metadata subitem name. |
| defaultValue   <br> | Default value. |

* Required

### Returns

| type | description |
| --- | --- |
|  | Metadata value, or defaultValue if no metadata or metadata item/subitem does not exist. |

## [getDefaultCamera()](#getdefaultcamera)

Returns the default camera.

## [isAEC()](#isaec)

### Returns

| type | description |
| --- | --- |
| boolean | True when the “AEC” loader settings were used when loading the model |

## [hasPageShadow()](#haspageshadow)

### Returns

| type | description |
| --- | --- |
| boolean | True when a 2D model has a page shadow |

## [getUpVector()](#getupvector)

Returns up vector as an array of 3.

Note: This returns the up vector as stored in the metadata (or the overridden up vector if specified), but does not take into account the world up rotation.

## [getNorthVector()](#getnorthvector)

Returns north vector as an array of 3.

## [getFrontVector()](#getfrontvector)

Returns front vector as an array of 3.

## [geomPolyCount()](#geompolycount)

Returns the polygon count.

### Returns

| type | description |
| --- | --- |
| number |  |

## [instancePolyCount()](#instancepolycount)

Returns the instanced polygon count.

### Returns

| type | description |
| --- | --- |
| number |  |

## [isLoadDone(checkTextures)](#isloaddone-checktextures)

Returns true if the model with all its geometries has loaded.

### Parameters

| checkTextures   boolean | Ensures that the model’s textures were completely loaded. |
| --- | --- |

### Returns

| type | description |
| --- | --- |
| boolean |  |

## [isObjectTreeCreated()](#isobjecttreecreated)

### Returns

| type | description |
| --- | --- |
| boolean | True if the frag to node id mapping is done. |

## [getPropertyDb()](#getpropertydb)

Returns an instance of [PropertyDatabase Loader](Private-PropDbLoader.md), responsible for communicating with the PropertyDatabase instance hosted in a browser worker thread.

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.Private.PropDbLoader](Private-PropDbLoader.md) |  |

## [getPropertyHashes(nameRE, categoryRE)](#getpropertyhashes-namere-categoryre)

Enumerates all attributes (types of properties) used for the given model. If the property database is available, for each property a triple with the property’s hash, name, and category is created and added to the result array. In addition, regular expression can be used to filter by name and/or category.

### Parameters

| nameRE*   RegExp | Regular expression to use for filtering properties by their name. |
| --- | --- |
| categoryRE*   RegExp | Regular expression to use for filtering properties by their category. |

* Required

### Returns

| type | description |
| --- | --- |
| Array | Array with triples of the properties’ hashes, names, and categories. |

### Examples

```
 const properties = await model.getPropertyHashes(/category/i);
// -> Array(8) [ (3) […], (3) […], (3) […], (3) […], (3) […], (3) […], (3) […], (3) […] ]
//     0: Array(3) [ "p5eddc473", "Category", "__category__" ]
//     1: Array(3) [ "pa7275c45", "CategoryId", "__categoryId__" ]
//     2: Array(3) [ "p3ed85946", "Subcategory", "Identity Data" ]
//     ...

```

---

## [getProperties(dbId, onSuccessCallback, onErrorCallback)](#getproperties-dbid-onsuccesscallback-onerrorcallback)

Asynchronous method that gets object properties

### Parameters

| dbId*   number | The database identifier. |
| --- | --- |
| onSuccessCallback   [Callbacks#onPropertiesSuccess](https://aps.autodesk.com/en/docs/viewer/v7/reference/Callbacks/onPropertiesSuccess/) | Callback for when the properties are fetched. |
| onErrorCallback   [Callbacks#onGenericError](https://aps.autodesk.com/en/docs/viewer/v7/reference/Callbacks/onGenericError/) | Callback for when the properties are not found or another error occurs. |

* Required

## [getProperties2(dbId, onSuccessCallback, onErrorCallback, options)](#getproperties2-dbid-onsuccesscallback-onerrorcallback-options)

Asynchronous method that gets object properties

### Parameters

Expand all

| dbId*   number | The database identifier. |
| --- | --- |
| onSuccessCallback   [Callbacks#onPropertiesSuccess](https://aps.autodesk.com/en/docs/viewer/v7/reference/Callbacks/onPropertiesSuccess/) | Callback for when the properties are fetched. |
| onErrorCallback   [Callbacks#onGenericError](https://aps.autodesk.com/en/docs/viewer/v7/reference/Callbacks/onGenericError/) | Callback for when the properties are not found or another error occurs. |
| options   Object |  |
| needsExternalId   boolean | Ensures loading of externalID table if necessary. This may consume a lot of memory. Only use if you really need externalIds. |

* Required

## [getBulkProperties(dbIds, options, onSuccessCallback, onErrorCallback)](#getbulkproperties-dbids-options-onsuccesscallback-onerrorcallback)

Returns properties for multiple objects with an optional filter on which properties to retrieve.

### Parameters

Expand all

| dbIds*   Array.<number> | IDs of the nodes to return the properties for. |
| --- | --- |
| options*   object, undefined | Dictionary with options. |
| propFilter   Array.<string> | Array of property names to return values for. Use null for no filtering. Filter applies to “name” and “externalId” fields also. |
| ignoreHidden   boolean | Ignore hidden properties |
| onSuccessCallback*   function | This method is called when request for property db succeeds. |
| onErrorCallback*   function | This method is called when request for property db fails. |

* Required

## [getBulkProperties2(dbIds, options, onSuccessCallback, onErrorCallback)](#getbulkproperties2-dbids-options-onsuccesscallback-onerrorcallback)

Returns properties for multiple objects with an optional filter on which properties to retrieve.

### Parameters

Expand all

| dbIds*   Array.<int> | IDs of the nodes to return the properties for. |
| --- | --- |
| options*   object, undefined | Dictionary with options. |
| propFilter   Array.<string> | Array of property names to return values for. Use null for no filtering. Filter applies to “name” and “externalId” fields also. |
| categoryFilter   Array.<string> | Array of category names to return values for. Use null for no filtering. |
| ignoreHidden   boolean | Ignore hidden properties |
| needsExternalId   boolean | Ensures loading of externalID table if necessary. This may consume a lot of memory. Only use if you really need externalIds. |
| onSuccessCallback*   function | This method is called when request for property db succeeds. |
| onErrorCallback*   function | This method is called when request for property db fails. |

* Required

## [getPropertySetAsync(dbIds, options)](#getpropertysetasync-dbids-options)

Returns a Promise that resolves with [PropertySet](Viewing-PropertySet.md) for multiple objects. An optional filter can be passed in to specify which properties to retrieve.

### Parameters

Expand all

| dbIds*   Array.<int> | IDs of the nodes to return the properties for. |
| --- | --- |
| options   Object | Dictionary with options. |
| propFilter   Array.<string> | Array of property names to return values for. Use null for no filtering. Filter applies to “name” and “externalId” fields also. |
| ignoreHidden   boolean | Ignore hidden properties |
| needsExternalId   boolean | Ensures loading of externalID table if necessary. This may consume a lot of memory. Only use if you really need externalIds. |

* Required

### Returns

| type | description |
| --- | --- |
| [Promise (PropertySet)](Viewing-PropertySet.md) | A promise that resolves with an instance of a Autodesk.Viewing.PropertySet |

## [getPropertySet(dbIds, onSuccessCallback, onErrorCallback, options)](#getpropertyset-dbids-onsuccesscallback-onerrorcallback-options)

Gets the property [PropertySet](Viewing-PropertySet.md) for multiple objects. An optional filter can be passed in to specify which properties to retrieve.

For the async version see [getPropertySetAsync](Viewing-Model.md#getPropertySetAsync/)

### Parameters

Expand all

| dbIds*   Array.<int> | IDs of the nodes to return the properties for. |
| --- | --- |
| onSuccessCallback*   function | This method is called when request for property db succeeds. |
| onErrorCallback*   function | This method is called when request for property db fails. |
| options   Object | Dictionary with options. |
| propFilter   Array.<string> | Array of property names to return values for. Use null for no filtering. Filter applies to “name” and “externalId” fields also. |
| ignoreHidden   boolean | Ignore hidden properties |
| needsExternalId   boolean | Ensures loading of externalID table if necessary. This may consume a lot of memory. Only use if you really need externalIds. |

* Required

### Returns

| type | description |
| --- | --- |
| [Promise (PropertySet)](Viewing-PropertySet.md) | Returns a promise that resolves with an instance of a Autodesk.Viewing.PropertySet |

## [getExternalIdMapping(onSuccessCallback, onErrorCallback)](#getexternalidmapping-onsuccesscallback-onerrorcallback)

Returns an object with key values being dbNodeIds and values externalIds. Useful to map LMV node ids to Fusion node ids.

### Parameters

| onSuccessCallback*   function | This method is called when request for property db succeeds. |
| --- | --- |
| onErrorCallback*   function | This method is called when request for property db fails. |

* Required

## [getLayerToNodeIdMapping(onSuccessCallback, onErrorCallback)](#getlayertonodeidmapping-onsuccesscallback-onerrorcallback)

Returns an object with key values being layer names, pointing to Arrays containing dbIds.

### Parameters

| onSuccessCallback*   function | This method is called when request for property db succeeds. |
| --- | --- |
| onErrorCallback*   function | This method is called when request for property db fails. |

* Required

## [getObjectTree(onSuccessCallback, onErrorCallback)](#getobjecttree-onsuccesscallback-onerrorcallback)

Asynchronous operation that gets a reference to the object tree.

You can use the model object tree to get information about items in the model. The tree is made up of nodes, which correspond to model components such as assemblies or parts.

### Parameters

| onSuccessCallback   [Callbacks#onObjectTreeSuccess](https://aps.autodesk.com/en/docs/viewer/v7/reference/Callbacks/onObjectTreeSuccess/) | Success callback invoked once the object tree is available. |
| --- | --- |
| onErrorCallback   [Callbacks#onGenericError](https://aps.autodesk.com/en/docs/viewer/v7/reference/Callbacks/onGenericError/) | Error callback invoked when the object tree is not found available. |

## [isObjectTreeLoaded()](#isobjecttreeloaded)

Returns `true` only when the object tree is loaded into memory. Will return `false` while the object tree is still loading, or when the object tree fails to load.

### Returns

| type | description |
| --- | --- |
| boolean |  |

## [search(text, onSuccessCallback, onErrorCallback, attributeNames, options)](#search-text-onsuccesscallback-onerrorcallback-attributenames-options)

Async operation to search the object property database.

### Parameters

Expand all

| text*   string | The search term (not case sensitive). |
| --- | --- |
| onSuccessCallback*   [Callbacks#onSearchSuccess](https://aps.autodesk.com/en/docs/viewer/v7/reference/Callbacks/onSearchSuccess/) | Invoked when the search results are ready. |
| onErrorCallback*   [Callbacks#onGenericError](https://aps.autodesk.com/en/docs/viewer/v7/reference/Callbacks/onGenericError/) | Invoke when an error occured during search. |
| attributeNames   Array.<string> | Restricts search to specific attribute names. |
| options   Object | Search options. Currently only supported option is searchHidden |
| searchHidden   boolean | Set to true to also search hidden properties |

* Required

## [findProperty(propertyName)](#findproperty-propertyname)

Searches the property database for all dbIds that contains a specific property name.

### Parameters

| propertyName*   string | The property name to search for (case sensitive). |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Promise (number[]) | The promise, which resolves with an array of dbIds containing the specified property. |

## [getTopology(index)](#gettopology-index)

Return topology data of one fragment.

Requires topology data to have been fetched with [fetchTopology()](Viewing-Model.md#fetchTopology/).

### Parameters

| index*   number | Topology index. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| object | Topology data. |

## [hasTopology()](#hastopology)

See also [fetchTopology()](Viewing-Model.md#fetchTopology/).

### Returns

| type | description |
| --- | --- |
| boolean | true if topology data has been downloaded and is available in memory |

## [fetchTopology(maxSizeMB)](#fetchtopology-maxsizemb)

Downloads the topology file, if one is available. The file may not get downloaded if the topology content size in memory is bigger than a specified limit (100 MB by default, 20 MB for mobile).

### Parameters

| maxSizeMB   number | Maximum uncompressed topology size allowed (in MegaBytes). |
| --- | --- |

### Returns

| type | description |
| --- | --- |
| Promise | A Promise that resolves with the topology object. |

## [hasGeometry()](#hasgeometry)

### Returns

| type | description |
| --- | --- |
| boolean | True if the model loaded contains at least 1 fragment. |

## [getFragmentPointer(fragId)](#getfragmentpointer-fragid)

Returns the FragmentPointer of the specified fragId in the model. This method returns null if the fragId is not passed in.

### Parameters

| fragId*   number | fragment id in the model |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Autodesk.Viewing.Private.FragmentPointer | The FragmentPointer |

## [clone()](#clone)

Returns a shallow copy of the model. All the inner state (Fragments, Geometries etc.) are shared.

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.Model](Viewing-Model.md) | A shallow copy of the model. |
