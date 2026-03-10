# InstanceTree

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Private/InstanceTree/

---

Autodesk.Viewing.Private

# InstanceTree

## [new InstanceTree(nodeAccess, objectCount, maxDepth)](#new-instancetree-nodeaccess-objectcount-maxdepth)

### Parameters

| nodeAccess* |  |
| --- | --- |
| objectCount* |  |
| maxDepth* |  |

* Required

# Methods

## [isNodeHidden(dbId)](#isnodehidden-dbid)

Whether a node id is hidden.

### Parameters

| dbId*   number | The node’s database id |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean |  |

## [isNodeVisibleLocked(dbId)](#isnodevisiblelocked-dbid)

Whether a node id’s visiblitly is locked.

### Parameters

| dbId*   number | The node’s database id |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean |  |

## [isNodeExplodeLocked(dbId)](#isnodeexplodelocked-dbid)

Whether a node id’s explode is locked.

### Parameters

| dbId*   number | The node’s database id |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean |  |

## [getNodeType(dbId)](#getnodetype-dbid)

Gets the type associated with the node, such as assmebly, layer, model, geometry, etc.

### Parameters

| dbId*   number | The node’s database id |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| number | one of [NODE_TYPE](#fixMe/) |

## [isNodeSelectable(dbId)](#isnodeselectable-dbid)

Whether the node is a selectable entity.

### Parameters

| dbId*   number | The node’s database id |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean |  |

## [getNodeParentId(dbId)](#getnodeparentid-dbid)

Gets the database id of the node’s parent.

### Parameters

| dbId*   number | The node’s database id |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| number |  |

## [getRootId()](#getrootid)

Gets the model’s root database id.

### Returns

| type | description |
| --- | --- |
| number |  |

## [getNodeName(dbId, includeCount)](#getnodename-dbid-includecount)

Gets the name associated to the id.

### Parameters

| dbId*   number | The node’s database id |
| --- | --- |
| includeCount*   boolean | True if must include count |

* Required

### Returns

| type | description |
| --- | --- |
| string |  |

## [getChildCount(dbId)](#getchildcount-dbid)

Get number of children under the specified id.

### Parameters

| dbId*   number | The node’s database id |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| number |  |

## [getFragmentCount(dbId)](#getfragmentcount-dbid)

Get number of fragments under the specified id.

### Parameters

| dbId*   number | The node’s database id |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| number |  |

## [getNodeBox(dbId, dst)](#getnodebox-dbid-dst)

Sets the bounding box values for a particular id on the 2nd argument provided. There is no return value.

### Parameters

| dbId*   number | The node’s database id |
| --- | --- |
| dst*   Float32Array | An array holding 6 number values: (min-x, min-y, min-z, max-x, max-y, max-z) |

* Required

## [enumNodeFragments(node, callback, recursive)](#enumnodefragments-node-callback-recursive)

### Parameters

| node*   number | The id of a node. |
| --- | --- |
| callback*   Autodesk.Viewing.Private.InstanceTree~onEnumNodeFragments | The function that will be called for each fragment. Note that if the callback function returns a truthy value, a loop over the fragments and child nodes will be interrupted and the callback result will be forwarded back to the caller. |
| recursive   boolean | Whether the callback function gets called for child nodes, too. |

* Required

## [enumNodeChildren(node, callback, recursive)](#enumnodechildren-node-callback-recursive)

### Parameters

| node*   number | The id of a node. |
| --- | --- |
| callback*   Autodesk.Viewing.Private.InstanceTree~onEnumNodeChildren | The function that will be called for each child node. Note that if the callback function returns a truthy value, a loop over the child nodes will be interrupted and the callback result will be forwarded back to the caller. |
| recursive   boolean | Whether the callback function gets called for indirect child nodes, too. |

* Required

## [search(text)](#search-text)

Search the tree for nodes whose names match the given string.

### Parameters

| text*   string | The search term (not case sensitive). |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Array.<number> | The dbIds of all nodes in the tree matching the search text. |
