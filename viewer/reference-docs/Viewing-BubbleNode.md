# BubbleNode

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/BubbleNode/

---

Autodesk.Viewing

# BubbleNode

Wrapper and helper for âbubbleâ data.

Bubble is a container of various 2D or 3D viewables (and additional data) that may be generated from a single seed file. The bubble is a JSON structure of nodes that have different roles, for example, they may represent sheets, nested 2D/3D geometry, etc.

This class wraps the internal representation of the bubble and adds a couple of helper methods.

## [new BubbleNode(data, parent)](#new-bubblenode-data-parent)

### Parameters

| data*   object | Raw node from the bubble JSON. |
| --- | --- |
| parent   object | Parent node from the bubble JSON. |

* Required

# Methods

## [isSVF2()](#issvf2)

### Returns

| type | description |
| --- | --- |
| boolean | True if the bubble is from MD API. |

## [getOtgGraphicsNode()](#getotggraphicsnode)

Returns the OTG viewable from an otg manifest (if available, otherwise undefined)

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.BubbleNode](/en/docs/viewer/v7/reference/Viewing/BubbleNode/), undefined |  |

## [getPropertyDbManifest(viewableID)](#getpropertydbmanifest-viewableid)

Returns a list of property database files. Previously, for v1, this list was hardcoded in PropWorker/ This function knows about v2 and cross-version sharing of OTG property databases

### Parameters

| viewableID   string | The viewable ID to get the property DB manifest for, defaults to this nodeâs GUID |
| --- | --- |

## [getRootNode()](#getrootnode)

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.BubbleNode](/en/docs/viewer/v7/reference/Viewing/BubbleNode/) | Top-most bubble node. |

## [isForgeManifest()](#isforgemanifest)

Whether the manifest comes from APS (modelDerivativeV2) or not (derivativeV2). Applies only to the root node. Used internally.

## [findPropertyDbPath(viewableID)](#findpropertydbpath-viewableid)

Finds shared property DB if there is one.

### Parameters

| viewableID   string | The viewable ID to use for looking up the property DB, defaults to this nodeâs GUID |
| --- | --- |

### Returns

| type | description |
| --- | --- |
| string, null | Shared property DB path, or null. |

## [name()](#name)

### Returns

| type | description |
| --- | --- |
| string | The nodeâs name. |

## [guid()](#guid)

### Returns

| type | description |
| --- | --- |
| string | The nodeâs GUID. |

## [type()](#type)

### Returns

| type | description |
| --- | --- |
| string | The nodeâs type. |

## [extensions()](#extensions)

### Returns

| type | description |
| --- | --- |
| Array.<string> | Either an Array of extension ids, or undefined. |

## [urn(searchParent)](#urn-searchparent)

Retrieves the URN of the node or its closest ancestor.

### Parameters

| searchParent*   boolean | If URN is not available for this node, search through its ancestors, too. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| string | Viewable URN. |

## [lineageUrn(encode)](#lineageurn-encode)

Retrieves the lineageUrn of the node. Note that models uploaded to OSS directly (not through WipDM) do not have a lineageUrn.

### Parameters

| encode   boolean | Whether to return the result base64 encoded or not. |
| --- | --- |

### Returns

| type | description |
| --- | --- |
| string | Viewable lineageUrn, or null in case of an error. |

## [isGeomLeaf()](#isgeomleaf)

### Returns

| type | description |
| --- | --- |
| boolean | True if this is a geometry leaf node. |

## [isViewable()](#isviewable)

### Returns

| type | description |
| --- | --- |
| boolean | True if this is a viewable node. |

## [getLodNode()](#getlodnode)

### Returns

| type | description |
| --- | --- |
| [BubbleNode](/en/docs/viewer/v7/reference/Viewing/BubbleNode/) | The LOD node. |

## [isGeometry()](#isgeometry)

### Returns

| type | description |
| --- | --- |
| boolean | True if this is a geometry node. |

## [isViewPreset()](#isviewpreset)

### Returns

| type | description |
| --- | --- |
| boolean | True if this is a view preset/camera definition node. |

## [is2D()](#is2d)

### Returns

| type | description |
| --- | --- |
| boolean | True if this is a 2D node. |

## [is3D()](#is3d)

### Returns

| type | description |
| --- | --- |
| boolean | True if this is a 3D node. |

## [is2DGeom()](#is2dgeom)

### Returns

| type | description |
| --- | --- |
| boolean | True if this is a 2D geometry node. |

## [is3DGeom()](#is3dgeom)

### Returns

| type | description |
| --- | --- |
| boolean | True if this is a 3D geometry node. |

## [useAsDefault()](#useasdefault)

### Returns

| type | description |
| --- | --- |
| boolean | True if the node is meant to be loaded initially. |

## [getDefaultGeometry(searchMasterview, loadLargestView)](#getdefaultgeometry-searchmasterview-loadlargestview)

### Parameters

| searchMasterview   boolean | Search for master view |
| --- | --- |
| loadLargestView   boolean | Sort by geometry size |

### Returns

| type | description |
| --- | --- |
| [BubbleNode](/en/docs/viewer/v7/reference/Viewing/BubbleNode/) | The default geometry if any, and otherwise the full data set. For SVF: A geometry node marked as being the default (for SVF: `useAsDefault=true`). When none is found, it returns the first element from `this.search({'type': 'geometry'})`. |

## [getPlacementTransform()](#getplacementtransform)

### Returns

| type | description |
| --- | --- |
| object | Placement transform of the node. |

## [isMetadata()](#ismetadata)

### Returns

| type | description |
| --- | --- |
| boolean | True if this is a metadata node. |

## [findViewableParent()](#findviewableparent)

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.BubbleNode](/en/docs/viewer/v7/reference/Viewing/BubbleNode/) | First parent in the hierarchy that is a viewable. If called on the top level design node, returns the first child of the design node that is a viewable. |

## [findParentGeom2Dor3D(options)](#findparentgeom2dor3d-options)

### Parameters

Expand all

| options   object | Advance usage options |
| --- | --- |
| fallbackParent   [Autodesk.Viewing.BubbleNode](/en/docs/viewer/v7/reference/Viewing/BubbleNode/) | Gets returned when no geometry node is available after iterating through the parent chain. |

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.BubbleNode](/en/docs/viewer/v7/reference/Viewing/BubbleNode/) | First parent in the hierarchy that is a 2D or 3D geometry. |

## [findAllViewables()](#findallviewables)

### Returns

| type | description |
| --- | --- |
| Array.<Autodesk.Viewing.BubbleNode> | Array with all of the viewables under this node. |

## [getViewableRootPath(ignoreLeaflet)](#getviewablerootpath-ignoreleaflet)

Looks for the viewable root path in this node and all its children.

### Parameters

| ignoreLeaflet*   boolean | If set, it will skip any image pyramid sub-nodes and return a path to F2D file if available. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| string | Viewable root path, or null. |

## [getNamedViews()](#getnamedviews)

Returns all the named view in the viewable. Named views are obtained from the documentâs manifest which contains camera information and a string identifier.

### Returns

| type | description |
| --- | --- |
| array | All named views. Returns empty array if none are found. |

## [findByGuid(guid)](#findbyguid-guid)

Returns first node from the bubble matching a GUID.

Note that some GUIDs in the bubble are not unique, you have to be sure you are looking for a GUID that is unique if you want correct result from this function. Otherwise use the generic search.

### Parameters

| guid*   string | Node GUID. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.BubbleNode](/en/docs/viewer/v7/reference/Viewing/BubbleNode/) | Matching bubble node, or null. |

## [search(propsToMatch)](#search-propstomatch)

Finds nodes from the bubble matching one or more properties.

### Parameters

| propsToMatch*   object | Filter criteria: To match, nodes must have the specified properties and values. Use comma-separated property:value pairs or named preset object. (See comments in examples below.) |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Array.<BubbleNode> | Matching nodes, or null. |

### Examples

```
// Filter criteria syntax:

```

// { âpropertyâ:âvalueâ [, âpropertyâ:âvalueâ, â¦] }
// or use named preset objects:
// BubbleNode.MODEL_NODE { âroleâ:â3dâ, âtypeâ:âgeometryâ }
// BubbleNode.GEOMETRY_SVF_NODE { âroleâ:âgraphicsâ, âmimeâ: âapplication/autodesk-svfâ }
// BubbleNode.SHEET_NODE { âroleâ:â2dâ, âtypeâ:âgeometryâ }
// BubbleNode.LEAFLET_NODE { âroleâ:âleafletâ }
// BubbleNode.IMAGE_NODE { âroleâ:âimageâ }
// BubbleNode.GEOMETRY_F2D_NODE { âroleâ:âgraphicsâ, âmimeâ: âapplication/autodesk-f2dâ }
// BubbleNode.VIEWABLE_NODE { âroleâ:âviewableâ }
// BubbleNode.AEC_MODEL_DATA { âroleâ:âAutodesk.AEC.ModelDataâ}

var singleProps = myBubbleNode.search({ âtypeâ:âgeometryâ });
var multiProps = myBubbleNode.search({ âroleâ:â3dâ, âtypeâ:âgeometryâ });
var presetProps = myBubbleNode.search( myBubbleNode.SHEET_NODE );

---

## [traverse(cb)](#traverse-cb)

Recursively traverses the bubble, calling a callback function for each node, for as long as the callback function keeps returning false.

### Parameters

| cb*   function | Callback function, accepts a bubble node as an argument, and returns true if the traversal should be terminated. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | Result of the last callback invocation. |

## [getLevel()](#getlevel)

Returns the Revit Level/Floor of this bubble node. Only relevant for 2d sheets coming from Revit at the moment.

## [getLevelName()](#getlevelname)

### Returns

| type | description |
| --- | --- |
| string | The Revit level/floor name of this bubble node. Only relevant for 2d sheets coming from Revit at the moment. |
