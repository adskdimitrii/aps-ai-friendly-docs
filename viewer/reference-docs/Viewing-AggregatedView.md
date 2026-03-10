# AggregatedView

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/AggregatedView/

---

Autodesk.Viewing

# AggregatedView

AggregatedView implements a viewing application based on Viewer3D. Its purpose is to provide functionality around Viewer3D to facilitate implementation of viewer application workflows like switching between different views or toggling models on/off dynamically.

Examples of AggregatedView functionality include:

1. **Facilitate use in react**: Just set an array of nodes from React property and AggregatedView takes care to make sure that models are loaded and shown/hidden as needed.
2. **LRU-Caching of models**: Keep models in memory for fast switches, but unload unused models if memory is critical
3. **Extensions**: Setting up a couple of useful default extensions (can be customized or switched off where wanted)
4. **Home camera**: Setting a home view camera that considers multiple models.
5. **Application State management**: Facilitates some state management, e.g.
  1. Setting a camera without having to care whether the model is already loaded or not.
  2. Starting Walk-mode without having to care whether BIMWalk extension is already loaded.
  3. Allow toggling visibility of a model without having to care about the loading state of the model.
6. **GlobalOffsets**: Choose globalOffset automatically, but identically for all models to make sure that they are placed consistently.
7. **View Switches**: Allow visibility toggling (`hide`/`show`) versus full view switches (`switchView(nodes)`), the latter including proper reset of camera, UI, and extensions
8. **Diff Setups**: Just set diffOptions to setup change visualization of aggregated views.

## [new AggregatedView()](#new-aggregatedview)

### Examples

```
const view = new Autodesk.Viewing.AggregatedView();
// Initialize the aggregatedView with the HTML element and the options object
await view.init(viewerElement, options);

```

---

# Methods

## [init(parentDiv, options)](#init-parentdiv-options)

Initializes the AggregatedView and loads the following predefined extensions: `Autodesk.CrossFadeEffects`, `Autodesk.AEC.LevelsExtension`, `Autodesk.ModelStructure`, `Autodesk.AEC.HyperlinkExtension`, `Autodesk.AEC.Minimap3DExtension`, `Autodesk.AEC.CanvasBookmarkExtension` and `Autodesk.AEC.DropMeExtension` The initialization can also be customized with the options object.

To initialize the viewer without loading the specified extension please reference [initViewerInstance](Viewing-AggregatedView.md#initViewerInstance/).

### Parameters

Expand all

| parentDiv*   HTMLDivElement | The div element in which the viewer will be initialized |
| --- | --- |
| options   Object | Configuration options for aggregated view |
| viewerConfig   Object | Used for initializing GuiViewer3D. This is the options object that is passed into either av.Viewer3D or av.GuiViewer3D |
| disableBookmarks   boolean | Disable display of visual bookmarks |
| clusterfck   Object | Dependency-Injection of clusterfck library (enables clustering of Bookmark icons) |
| viewerStartOptions   Object | Options passed to the viewer initialization process |
| ignoreGlobalOffset   boolean | Forces globalOffset to undefined for all loaded models. Effect of this is that all models are auto-centered using the model bbox. Note that this does only work if you never show more than one 3D viewable at once |
| unloadUnfinishedModels   boolean | By setting unloadUnfinishedModels, when calling hide(bubbleNode), it will unload models that haven’t been fully loaded. Used in order to reduce amount of file loaders when switching between models |
| useDynamicGlobalOffset   boolean | If true, the globalOffset is applied dynamically after loading |
| cameraValidator   boolean | Called with a (camera, model) when using a model camera as start or home camera. This allows for clients to apply optional custom repairs for models with messy camera data |
| propagateInputEventTypes   Array.<string> | By default, LMV ToolController “eats” all handled events so that they don’t reach any other widgets. Specify an array of event types that you want this behaviour disabled for. For example [‘mouseup’, ‘mousedown’] allows alloy to detect mouse outside clicks to close pending dropdown menus |
| createModelAlignmentService*   function | Factory function to create AlignmentService implementation for loading/saving model transforms. See AlignmentServices above for details |
| getCustomLoadOptions   function | Allows for applying custom options to be used for all model loading. The callback returns an options object that is applied by default in all model-load calls. The signature should look like: function(av.BubbleNode)=>Object |
| viewerUnits   string | If specified, all models are re-scaled from model units to this unit. Must be a GNU unit format string, e.g. “m”. |
| forceWorldUpDirection   Array.<number> | If specified, the world up direction is forced to the given vector. Models with different world up directions in the manifest are rotated to align with the given vector. Must be an array of three numbers, e.g. [0, 1, 0]. |
| multiViewerFactory   Autodesk.Viewing.MultiViewerFactory | Optional multi viewer factory. Used to create multiple viewers with shared resources |
| useConsolidation   boolean | Optional flag to enable / disable mesh consolidation. Defaults to true. |

* Required

### Returns

| type | description |
| --- | --- |
| Promise | returns a promise once all of the specified extensions are loaded. |

## [initViewerInstance(parentDiv, options)](#initviewerinstance-parentdiv-options)

Initialize a new viewer instance.

To initialize the viewer and load the default extensions please see [init](Viewing-AggregatedView.md#init/).

### Parameters

| parentDiv*   HTMLDivElement | The div element in which the viewer will be initialized |
| --- | --- |
| options   Object | The same options object that is passed into the init method |

* Required

## [reset()](#reset)

Resets tools, UI, camera, and refPoint. This method should be called when an explicit view switch occurred instead of just toggling visibility of models.

## [getModel(node)](#getmodel-node)

Finds a model for the given bubbleNode or key. To get multiple models reference [getModels](#fixMe/). To make sure that the model is loaded reference [getModelAndWait](Viewing-AggregatedView.md#getModelAndWait/).

### Parameters

| node*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | The Bubble node to use to get the model |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.Model](Viewing-Model.md) | The model that corresponds to the bubbleNode |

### Examples

```
const nodes = view.getVisibleNodes();
// Get the model of the first bubble node.
const model = view.getModel(nodes[0]);

```

---

## [getModelAndWait(node, checkIfVisible)](#getmodelandwait-node-checkifvisible)

Find a model for given bubbleNode or key. If the model is not available yet, wait until it’s ready.

### Parameters

| node*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | The Bubble node to use to get the model |
| --- | --- |
| checkIfVisible   Boolean | If true, will wait until model is also visible |

* Required

### Returns

| type | description |
| --- | --- |
| Promise | the promise resolves once the model is loaded with the model instance |

### Examples

```
const model = await view.getModelAndWait(node);

```

---

## [isEmpty()](#isempty)

Returns true if there are no visible bubble nodes.

### Returns

| type | description |
| --- | --- |
| Boolean | returns true if all nodes are invisible |

## [show(bubbleNode, customLoadOptions)](#show-bubblenode-customloadoptions)

Makes sure that a model is loaded and shown

To get the bubbleNode from a URN please reference [Document#load](#fixMe/).

### Parameters

| bubbleNode*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | The node to load and show in the viewer |
| --- | --- |
| customLoadOptions   Object | Optional extra loadOptions to override/extend the default ones |

* Required

### Returns

| type | description |
| --- | --- |
| Promise | Returns a promise which resolves with the model |

### Examples

```
// Load a document from a documentId/URN
Autodesk.Viewing.Document.load(documentId, (doc) => {
  // Find all of the 3D bubble nodes
  var nodes3D = doc.docRoot.search({ role: '3d', type: "geometry" });

  // Using aggregated view load and show the model.
  const model = await view.show(nodes3D[0]);
});

```

Show More

---

## [hide(bubbleNode)](#hide-bubblenode)

Hides the model associated from the supplied bubble node.

To show the model reference [show](Viewing-AggregatedView.md#show/).

### Parameters

| bubbleNode*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | The node to hide in the viewer |
| --- | --- |

* Required

### Examples

```
view.hide(node);

```

---

## [isVisible(bubbleNode)](#isvisible-bubblenode)

Returns true if the supplied bubble node is currently visible.

### Parameters

| bubbleNode*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | The BubbleNode to check the visibility of |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Boolean | true if the specified node is visible, false otherwise |

## [hideAll()](#hideall)

Hide all of the models in the viewer.

## [getVisibleNodes()](#getvisiblenodes)

Returns all of the visible bubble nodes.

### Returns

| type | description |
| --- | --- |
| Array.<Autodesk.Viewing.BubbleNode> | An array of all of the visible nodes |

## [areAllNodes2D()](#areallnodes2d)

Returns true if all of the nodes are 2D.

### Returns

| type | description |
| --- | --- |
| Boolean | returns true if all nodes are 2D, false otherwise. |

## [isOtgManifestMissing(bubbleNode)](#isotgmanifestmissing-bubblenode)

Checks if the Otg manifest for a 3D viewable is available and complete. If not, it reports an error and returns false.

### Parameters

| bubbleNode*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | The BubbleNode |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Boolean | true if the OTG manifest is missing. |

## [load(bubbleNode, customLoadOptions)](#load-bubblenode-customloadoptions)

Loads the model that is specified by the passed in bubbleNode parameter. Note this function will not show the model once it is loaded. To load and show the model reference the [show](Viewing-AggregatedView.md#show/) method.

### Parameters

| bubbleNode*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | The BubbleNode |
| --- | --- |
| customLoadOptions   Object | Optional extra loadOptions to override/extend the default ones |

* Required

### Returns

| type | description |
| --- | --- |
| Promise | The promise resolves with the loaded model |

## [unload(bubbleNode)](#unload-bubblenode)

Unload the model that corresponds with the passed in bubbleNode.

### Parameters

| bubbleNode*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | The BubbleNode to unload |
| --- | --- |

* Required

### Examples

```
const nodes = view.getVisibleNodes();
// Unload the first model
view.unload(nodes[0]);

```

---

## [unloadAll(itemFilter)](#unloadall-itemfilter)

Unload all of the models that are currently in the view.

### Parameters

| itemFilter   function | This callback is used to check if a model needs to be unloaded. This callback recieves an object describing the current view item and it should return a boolean |
| --- | --- |

### Examples

```
// This example will unload all invisible models.
view.unloadAll((item) => {
  return !item.visible
});

```

---

## [setCameraGlobal(camera)](#setcameraglobal-camera)

Set camera in global coords.

- The current global offset is automatically subtracted
- You don’t have to specify all members, e.g., can leave out up or fov. Only defined values are replaced.
- You can call it independent of loading state: If no model is loaded yet, the camera change is applied after first model add
- Note that the call only has effect on current view, i.e., is discarded on reset/viewSwitch calls.

### Parameters

| camera*   THREE.Camera | Camera instance that will be used to apply to global camera |
| --- | --- |

* Required

## [setCamera(camera)](#setcamera-camera)

Set the view from the passed in camera.

### Parameters

| camera*   THREE.Camera | Camera instance |
| --- | --- |

* Required

## [startBimWalk()](#startbimwalk)

Starts the BIM walk tool. Under the hood this method will activate the BimWalk extension.

## [stopBimWalk()](#stopbimwalk)

Stop the BIM walk tool. Under the hood this method will deactivate the BimWalk extension.

## [isBimWalkActive()](#isbimwalkactive)

Returns true if the BimWalk tool is active.

### Returns

| type | description |
| --- | --- |
| Boolean | true if the tool is active, false otherwise. |

## [switchView(bubbleNodes, diffConfig)](#switchview-bubblenodes-diffconfig)

Switches between bubble node models. This method will reset the view and then set the passed in nodes.

Use this for explicit view switches. See [setNodes()](Viewing-AggregatedView.md#setNodes/) for params.

### Parameters

| bubbleNodes*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md), Array.<Autodesk.Viewing.BubbleNode> | The nodes to be shown |
| --- | --- |
| diffConfig   Object | see the setNodes method for the diffConfig parameter |

* Required

### Returns

| type | description |
| --- | --- |
| Promise | The promise resolves with the loaded models |

## [setNodes(bubbleNodes, diffConfig)](#setnodes-bubblenodes-diffconfig)

Load/Unload models so that the currently loaded models matches with the given list of svfs.

Note: Use [switchView()](Viewing-AggregatedView.md#switchView/) to do an explicit view switch (including resetting tools/camera). Use [setModels()](#fixMe/) to reconfiguring which models are visible in the current view.

### Parameters

Expand all

| bubbleNodes*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md), Array.<Autodesk.Viewing.BubbleNode> | The nodes to be shown |
| --- | --- |
| diffConfig   Object | Options to activate diff views. |
| primaryBubbles   Array.<Autodesk.Viewing.BubbleNode> | A subset of ‘bubbleNodes’ that participates in the diff. If ‘bubbleNodes’ contains more, these will be ghosted. These nodes represent the current/as-is state |
| diffBubbles   Array.<Autodesk.Viewing.BubbleNode> | Length must match primaryBubbles. For each node primaryBubbles[i], diffBubbles[i] provides the corresponding “before” state to compare against |
| diff   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | If svfs are sheet nodes, diff.supportModels must provide the bubbleNodes for the corresponding 3D support models. { diff, primary } |
| primary   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | Primary bubble node to do the diff comparison on |
| autoDetect   boolean | If true, support models are automatically found - works for Revit models with master views |

* Required

### Returns

| type | description |
| --- | --- |
| Promise | The promise resolves with the loaded models |

## [isLoadDone()](#isloaddone)

Returns true if all pending loading is finished. More concrete, it means that there is no…

- model-root loading
- geometry loading, or
- propDbLoading pending or in progress.

Reference [waitForLoadDone](Viewing-AggregatedView.md#waitForLoadDone/).

### Returns

| type | description |
| --- | --- |
| Boolean | Returns true if all of the models in the view are fully loaded, false otherwise. |

## [waitForLoadDone()](#id46)

Returns a promise that resolves when [isLoadDone()](Viewing-AggregatedView.md#isLoadDone/) returns true.

### Returns

| type | description |
| --- | --- |
| Promise | resolves when all isLoadDone returns true. |

## [findDiffSupportModel(sheetNode)](#finddiffsupportmodel-sheetnode)

“Support models” are 3D models that augment 2D diffs for better results: Instead of comparing the 2D objects directly, the correspodning 3D counterparts are compared. This is more reliable and avoids false positives due to irrelevant plotting differences. We use master views as support models, because they contain all objects of a given phase.

Given a bubble node referring to a 2D sheet node, this function returns the bubbleNode of the corresponding 3D master view that belongs to the same phase. This can be used as “support model” to obtain better results for 2D diff.

### Parameters

| sheetNode*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | A 2d bubble node |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | the coresponding 3d bubble node |

## [findDiffSupportModels(diffConfig)](#finddiffsupportmodels-diffconfig)

Find corresponding 3D model for each diff/primary The result will be stored in the passed in diffConfig. The results will be in diffConfig.supportBubbles.diff and diffConfig.supportBubbles.primary.

For the diffConfig parameter reference [setNodes](Viewing-AggregatedView.md#setNodes/).

### Parameters

| diffConfig*   Object | see the setNodes method for the diffConfig parameter |
| --- | --- |

* Required
