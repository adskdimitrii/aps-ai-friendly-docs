# Tree

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/UI/Tree/

---

Autodesk.Viewing.UI

# Tree

## [new Tree(delegate, root, parentContainer, options)](#new-tree-delegate-root-parentcontainer-options)

Tree view control

### Parameters

| delegate*   object | TreeDelegate instance |
| --- | --- |
| root*   object | A node in the model Document |
| parentContainer*   HTMLElement |  |
| options*   object |  |

* Required

# Methods

## [destroy()](#destroy)

Remove tree from DOM.

## [show(show)](#show-show)

Show/hide the tree control

### Parameters

| show*   boolean | true to show the tree control, false to hide it |
| --- | --- |

* Required

## [getRootContainer()](#getrootcontainer)

Get the root container

### Returns

| type | description |
| --- | --- |
| string |  |

## [getElementForNode(node)](#getelementfornode-node)

Get DOM element for a given logical tree node (or its integer id)

### Parameters

| node*   object | Tree node element |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| HTMLElement |  |

## [delegate()](#delegate)

Get the tree delegate

### Returns

| type | description |
| --- | --- |
| object | TreeDelegate instance |

## [isCollapsed(group)](#iscollapsed-group)

Is the given group node in the tree collapsed?

### Parameters

| group*   object | The group node |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if group node is collapsed, false if expanded |

## [setCollapsed(group, collapsed, recursive)](#setcollapsed-group-collapsed-recursive)

Collapse/expand the given group node in the tree

### Parameters

| group*   object | the group node |
| --- | --- |
| collapsed*   boolean | Set to true to collapse the group node, false to expand it |
| recursive*   boolean | Set to true to make it recursive |

* Required

## [setAllCollapsed(collapsed)](#setallcollapsed-collapsed)

Collapse/expand all group nodes in the tree

### Parameters

| collapsed*   boolean | true to collapse tree, false to expand it |
| --- | --- |

* Required

## [addToSelection(nodes)](#addtoselection-nodes)

Add the given nodes to the current selection

### Parameters

| nodes*   Array.<object> | nodes to add to the current selection |
| --- | --- |

* Required

## [removeFromSelection(nodes)](#removefromselection-nodes)

Remove the given nodes from the current selection

### Parameters

| nodes*   Array.<object> | The nodes to remove from the current selection |
| --- | --- |

* Required

## [setSelection(nodes)](#setselection-nodes)

Set the current selection

### Parameters

| nodes*   Array.<object> | nodes to make currently selected |
| --- | --- |

* Required

## [getSelection()](#getselection)

Get the current selection

### Returns

| type | description |
| --- | --- |
| Array.<object> | selected nodes. |

## [clearSelection()](#clearselection)

Clear the current selection

## [isSelected(node)](#isselected-node)

Is the given node selected?

### Parameters

| node*   object | The tree node |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if node is selected, false otherwise |

## [scrollTo(node)](#scrollto-node)

Scrolls the container to reveal the node’s DOM element.

### Parameters

| node*   object | the Tree node |
| --- | --- |

* Required

## [addClass(node, className, recursive)](#addclass-node-classname-recursive)

Add a CSS class to a node

### Parameters

| node*   number, object | The tree node |
| --- | --- |
| className*   string |  |
| recursive* |  |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the class was added, false otherwise |

## [removeClass(node, className, recursive)](#removeclass-node-classname-recursive)

Remove a class from a node

### Parameters

| node*   number, object | The tree node or its dbId |
| --- | --- |
| className*   string | Class name |
| recursive*   boolean | Set to true to make it recursive |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the class was removed, false otherwise |

## [hasClass(node, className)](#hasclass-node-classname)

Does the node have the given class?

### Parameters

| node*   number, object | The node or its dbId |
| --- | --- |
| className*   string |  |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the node has the given class, false otherwise |

## [clear()](#clear)

Clears the contents of the tree

## [iterate(node, callback)](#iterate-node-callback)

Iterates through nodes in the tree in pre-order.

### Parameters

| node*   object, number | node at which to start the iteration. |
| --- | --- |
| callback*   function | invoked for each iterated node with (Object, HTMLElement) |

* Required
