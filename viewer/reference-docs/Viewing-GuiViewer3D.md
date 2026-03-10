# GuiViewer3D

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/GuiViewer3D/

---

Autodesk.Viewing

# GuiViewer3D
> Extends [`Autodesk.Viewing.Viewer3D`_](#id232)

## [new GuiViewer3D(container, config)](#new-guiviewer3d-container-config)

Viewer component based on [Autodesk.Viewing.Viewer3D](Viewing-Viewer3D.md) with added UI.

### Parameters

| container*   HTMLElement | The viewer container. |
| --- | --- |
| config*   object | The initial settings object. See base class for details. |

* Required

# Properties

| ViewerCount | Need to keep track of viewers in document so we know when it is safe to call clearPropertyWorkerCache() |
| --- | --- |
| kDefaultCanvasConfig | Default values passed into [#setCanvasClickBehavior](#setCanvasClickBehavior/) specifying how the viewer canvas will react to user input as well as other 3d-canvas related options. |

# Methods

## [loadExtension(extensionId, options)](#loadextension-extensionid-options)

Loads the extension with the given id and options.

### Parameters

| extensionId*   string | The string id of the extension. |
| --- | --- |
| options*   Object | An optional dictionary of options. |

* Required

### Returns

| type | description |
| --- | --- |
| Promise | Resolves with the extension requested. |

## [getExtension(extensionId, callback)](#getextension-extensionid-callback)

Returns the loaded extension.

### Parameters

| extensionId*   string | The string id of the extension. |
| --- | --- |
| callback   function | That receives an extension instance as argument. |

* Required

### Returns

| type | description |
| --- | --- |
| Object | Extension. |

## [getExtensionAsync(extensionId)](#getextensionasync-extensionid)

Returns a promise with the loaded extension.

### Parameters

| extensionId*   string | The string id of the extension. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Promise | Resolves with the loaded extension. |

## [unloadExtension(extensionId)](#unloadextension-extensionid)

Unloads the extension with the given id.

### Parameters

| extensionId*   string | The string id of the extension. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the extension was successfully unloaded. |

## [loadExtensionLocal(extensionId, options)](#loadextensionlocal-extensionid-options)

Loads the extension with the given id and options. For internal use only.

### Parameters

| extensionId*   string | The string id of the extension. |
| --- | --- |
| options*   Object | An optional dictionary of options. |

* Required

### Returns

| type | description |
| --- | --- |
| Promise | Resolves with the extension requested. |

## [forEachExtension(callback)](#foreachextension-callback)

Iterate over each extension that has been successfully loaded and invokes a callback function for them.

### Parameters

| callback*   function | That receives an extension instance as argument. |
| --- | --- |

* Required

### Examples

```
forEachExtension(function(ext){
    console.log(ext.id);
 })

```

---

## [start(url, options, onSuccessCallback, onErrorCallback, initOptions)](#start-url-options-onsuccesscallback-onerrorcallback-initoptions)

Initializes the viewer and loads any extensions specified in the constructor’s config parameter. If the optional parameters are specified, the start() function will use an optimized initialization sequence that results in faster model load. The parameters are the same as the ones for Viewer3D.loadModel and you do not need to call loadModel subsequently if the model is loaded via the call to start().

### Parameters

| url   string | Optional URN or filepath to load on start. |
| --- | --- |
| options   object | Optional path to shared property database. |
| onSuccessCallback   Autodesk.Viewing.Viewer3D~onLoadModelSuccess | Method that gets called when initial loading is done and streaming starts. |
| onErrorCallback   Autodesk.Viewing.Viewer3D~onLoadModelFailure | Method that gets called when initial loading ends with an error. |
| initOptions   object | Optional: Options forwarded to viewer.initialize() |

### Returns

| type | description |
| --- | --- |
| number | 0 if the viewer has started, an error code (same as that returned by initialize()) otherwise. |

## [setUp(config)](#setup-config)

Loading extensions and initializing canvas interactions. Invoked automatically by [Autodesk.Viewing.Viewer3D#start](Viewing-Viewer3D.md#start/) method.

### Parameters

Expand all

| config   object | configuration values |
| --- | --- |
| extensions   Array.<string> | List of extension ids to load with the model. |
| canvasConfig   object | Overrides for click/tap events on the 3D canvas. Refer to [#setCanvasClickBehavior](#setCanvasClickBehavior/) for details. |

## [tearDown(isUnloadModelsWanted)](#teardown-isunloadmodelswanted)

Unloads extensions and the loaded models. Invoked automatically by [Autodesk.Viewing.Viewer3D#finish](Viewing-Viewer3D.md#finish/) method.

### Parameters

| isUnloadModelsWanted   boolean | Whether to unload models at the end. Default is true. |
| --- | --- |

## [_onAggregatedSelectionChanged()](#onaggregatedselectionchanged)

When selection has changed set the pivot point to be in the middle, if Autodesk.Viewing.Private.Prefs3D.SELECTION_SETS_PIVOT is true

## [run()](#run)

Triggers the Viewer’s render loop. Invoked automatically by [Autodesk.Viewing.Viewer3D#start](Viewing-Viewer3D.md#start/) method. Refer to [ViewerConfig.startOnInitialize](#fixMe/) to change start’s method behavior.

## [localize()](#localize)

Localize the viewer. This method can be overwritten so that the subclasses can localize any additional elements. Invoked internally during initialization.

## [uninitialize()](#uninitialize)

Removes all created DOM elements, performs GL uninitialization that is needed and removes event listeners.

## [finish()](#finish)

Unloads any loaded extensions and then uninitializes the viewer.

## [loadModel(url, options, onSuccessCallback, onErrorCallback)](#loadmodel-url-options-onsuccesscallback-onerrorcallback)

Loads a model into the viewer. Can be used sequentially to load multiple 3D models into the same scene.

### Parameters

Expand all

| url*   string | The url to the model. |
| --- | --- |
| options   object | Dictionary of options. |
| fileLoader   [Autodesk.Viewing.FileLoader](Viewing-FileLoader.md) | The file loader to use for this url. Required for unsupported file types. |
| keepCurrentModels   boolean | Flag indicating whether viewer should keep or unload all other models. |
| loadOptions   object | May contain params that are specific for certain loaders/filetypes. |
| sharedPropertyDbPath   string | Optional path to shared property database. |
| ids   string | A list of object IDs to load. |
| loadAsHidden   boolean | By default, a new model is instantly shown and triggers viewer refreshes during loading. Setting this option avoids that. The model can then be shown later by calling showModel(). |
| modelNameOverride   string | Allows host application to override model name used in UI. |
| placementTransform   LmvMatrix4 | Applied to the model during loading. |
| applyScaling   string, Object | Unit-Scaling that is applied to the model on load, e.g. { from: ‘ft’, to: ‘m’ }. If ‘from’ is not set, it is determined from model metadata (if provided). If only ‘to’ is set, you can just assign a string directly, e.g. applyScaling = ‘m’ is the same as applyScaling = { to: ‘m’ }. |
| applyPlacementInModelUnits   boolean | Only relevant if options.placementTransform and options.applyScaling are both used at once. In this way, it controls the order in which placement and scaling happen: - False: Placement happens in viewer world-units. That is, applyScaling is done first, then the custom placementMatrix is applied. (Default behavior) - True: Placement happens in model units. That is, custom placementMatrix is applied first, then the unit scaling. |
| onSuccessCallback   Autodesk.Viewing.Viewer3D~onLoadModelSuccess | A method that gets called when model’s metadata loading is done and geometry streaming starts. |
| onErrorCallback   Autodesk.Viewing.Viewer3D~onLoadModelFailure | A method that gets called when loading fails. |

* Required

## [isLoadDone(include)](#isloaddone-include)

Check whether models are completely loaded This method checks all models in the model queue and load requests that haven’t loaded the root model yet. A model is completely loaded when the root model is loaded, all of the geometry is loaded, the property database, if present is loaded and no textures are being loaded.

### Parameters

Expand all

| include   Object | Optional object to set the scope of the wait |
| --- | --- |
| geometry   Boolean | Set to false to exclude the geometry loading from consideration. Because textures are loaded with geometry, include.textures must also be set to false to prevent geometry from being considered. Defaults to true. |
| propDb   Boolean | Set to false to exclude the property data base loading from consideration. Defaults to true. |
| textures   Boolean | Set to false to exclude the texture loading from consideration. Defaults to true. |
| hidden   Boolean | Set to true to include hidden models for consideration. Defaults to false. |
| onlyModels   [Model](Viewing-Model.md), Array.<Model> | Limits the check to the model or models in this property. Note that checking for textures loaded cannot be limited to models. |

### Returns

| type | description |
| --- | --- |
| Boolean | True if all models are completely loaded, otherwise false |

## [waitForLoadDone(include)](#waitforloaddone-include)

Wait for models to be completely loaded This method checks all models in the model queue and load requests that haven’t loaded the root model yet. A model is completely loaded when the root model is loaded, all of the geometry is loaded, the property database, if there is one, is loaded and no textures are being loaded. If this method is called before the viewer is started, then it will wait until the viewer starts and at least one model start loading to check for the load completing

### Parameters

Expand all

| include   Object | Optional object to set the scope of the wait |
| --- | --- |
| geometry   Boolean | Set to false to exclude the geometry loading from consideration. Because textures are loaded with geometry, include.textures must also be set to false to prevent waiting for geometry to load. Defaults to true. |
| propDb   Boolean | Set to false to exclude the property data base loading from consideration. Defaults to true. |
| textures   Boolean | Set to false to exclude the texture loading from consideration. Defaults to true. |
| hidden   Boolean | Set to true to include hidden models for consideration. Defaults to false. |
| onlyModels   [Model](Viewing-Model.md), Array.<Model> | Limits the wait to the model or models in this property. Note that waiting for textures loaded cannot be limited to models. |

### Returns

| type | description |
| --- | --- |
| Promise | resolves when all models are loaded. This promise can be rejected by a LOADER_LOAD_ERROR_EVENT event. |

## [unloadModel(model)](#unloadmodel-model)

Unloads the specified model. Reference [Autodesk.Viewing.Viewer3D#hideModel](Viewing-Viewer3D.md#hideModel/) to hide the model.

### Parameters

| model*   [Autodesk.Viewing.Model](Viewing-Model.md) | The model to unload. |
| --- | --- |

* Required

## [loadDocumentNode(avDocument, manifestNode, options)](#loaddocumentnode-avdocument-manifestnode-options)

### Parameters

| avDocument*   [Autodesk.Viewing.Document](Viewing-Document.md) | The Document instance, which owns the model being loaded |
| --- | --- |
| manifestNode*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | The specific manifest node to load (within the Document) |
| options   ViewerConfig | Options to pass to [Autodesk.Viewing.Viewer3D#loadModel](Viewing-Viewer3D.md#loadModel/). Will be initialized internally if not specified. The options object will be augmented by automatically determined load parameters. |

* Required

### Returns

| type | description |
| --- | --- |
| Promise | Resolves with an object representing the model. |

## [unloadDocumentNode(manifestNode)](#unloaddocumentnode-manifestnode)

Unloads a model previously loaded by loadDocumentNode().

Reference [Autodesk.Viewing.Viewer3D#loadDocumentNode](Viewing-Viewer3D.md#loadDocumentNode/)

### Parameters

| manifestNode*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | The specific manifest node to unload (within the Document) |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true on success |

## [getDimensions()](#getdimensions)

Returns the dimensions of the WebGL canvas.

### Returns

| type | description |
| --- | --- |
| object | Client rectangle bounds object { width:Number, height: Number } |

## [resize()](#resize)

Resizes the viewer. Required when wrapping div changes dimensions due to CSS changes.

## [getHotkeyManager()](#gethotkeymanager)

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.HotkeyManager](Viewing-HotkeyManager.md) | The hotkey manager. |

## [getCamera()](#getcamera)

Gets the camera so it can be modified by the client.

### Returns

| type | description |
| --- | --- |
| THREE.Camera | The active camera. |

## [getState(filter)](#getstate-filter)

Gets the view state as a plain object. A viewer state contains data for the viewport, selection and isolation.

Reference [Autodesk.Viewing.Viewer3D#restoreState](Viewing-Viewer3D.md#restoreState/)

### Parameters

| filter   object | Specifies which viewer values to get. |
| --- | --- |

### Returns

| type | description |
| --- | --- |
| object | Viewer state. |

## [restoreState(viewerState, filter, immediate)](#restorestate-viewerstate-filter-immediate)

Restores the viewer state from a given object.

Reference [Autodesk.Viewing.Viewer3D#getState](Viewing-Viewer3D.md#getState/)

### Parameters

| viewerState*   Object |  |
| --- | --- |
| filter   Object | Similar in structure to viewerState used to filter out values that should not be restored. |
| immediate   boolean | Whether the new view is applied with (true) or without transition (false). |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if restore operation was successful. |

## [setView(viewNode, options)](#setview-viewnode-options)

Loads a view specified in the Manifest JSON. For 3D models it will use the camera values. For 2D models it will use the viewBox values.

Notice that in order that the view will be properly set according to the model’s transformation, the model has to be loaded first.

### Parameters

Expand all

| viewNode*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) | bubble node representing the view |
| --- | --- |
| options   Object |  |
| skipTransition   boolean | true to apply instanstly instead of lerping. |
| useExactCamera   boolean | whether any up vector adjustment is to be done (to keep head up view) |
| skipViewpointExtra   boolean | true to skip using extra viewpoint information |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true, if the view is applied. |

## [setViewFromArray(params)](#setviewfromarray-params)

Sets the view from an array of parameters.

To get the view array of the current camera use: [Autodesk.Viewing.Viewer3D#getViewArrayFromCamera](Viewing-Viewer3D.md#getViewArrayFromCamera/). To get the camera object from the view array use [Autodesk.Viewing.Viewer3D#getCameraFromViewArray](Viewing-Viewer3D.md#getCameraFromViewArray/).

### Parameters

| params*   Array.<Number> | View parameters: [position-x, position-y, position-z, target-x, target-y, target-z, up-x, up-y, up-z, aspect, fov (radians), orthoScale, isPerspective (0=perspective, 1=ortho)] |
| --- | --- |

* Required

## [getCameraFromViewArray(params, model)](#getcamerafromviewarray-params-model)

Returns an object representing a Camera from an unintuitive array of number. Note: To use this function in multi-model scenarios, you must pass the model parameter.

To get the view array of the current camera use: [Autodesk.Viewing.Viewer3D#getViewArrayFromCamera](Viewing-Viewer3D.md#getViewArrayFromCamera/).

### Parameters

| params*   Array.<Number> | Array with 13 elements describing different aspects of a camera. |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | Camera is transformed in the same way as the model. Default is this.model (only sufficient for single-view scenarios). |

* Required

### Returns

| type | description |
| --- | --- |
| Object, null | Camera object, or null if argument is invalid or missing. |

## [getViewArrayFromCamera()](#getviewarrayfromcamera)

Returns an Array of values that could be inserted back into a manifest to represent a view. To get the camera object from the view array use [Autodesk.Viewing.Viewer3D#getCameraFromViewArray](Viewing-Viewer3D.md#getCameraFromViewArray/).

### Returns

| type | description |
| --- | --- |
| Array.<Number> | Array with 13 elements describing different aspects of the current camera. |

## [setViewFromViewBox(viewbox, name, skipTransition)](#setviewfromviewbox-viewbox-name-skiptransition)

Sets the view from an array representing a view box.

Not applicable to 3D.

### Parameters

| viewbox*   Array.<Number> | View parameters: [min-x, min-y, max-x, max-y] |
| --- | --- |
| name   string | Optional named view name to also set the layer visibility state associated with this view. |
| skipTransition   boolean | true to apply instanstly instead of lerping. |

* Required

## [activateLayerState(stateName)](#activatelayerstate-statename)

Changes the active layer state. Layers is a feature usually available on 2D models and some 3D models.

Reference [Autodesk.Viewing.Viewer3D#getLayerStates](Viewing-Viewer3D.md#getLayerStates/)

### Parameters

| stateName*   string | Name of the layer state to activate. |
| --- | --- |

* Required

## [getLayerStates()](#getlayerstates)

Returns information for each layer state: name, description, active. Activate a state through [Autodesk.Viewing.Viewer3D#activateLayerState](Viewing-Viewer3D.md#activateLayerState/).

### Returns

| type | description |
| --- | --- |
| Array.<Object>, null | Array of layer states. If layers don’t exist or are hidden, this methods returns null. |

## [setViewFromFile(model)](#setviewfromfile-model)

Sets the view using the default view in the source file.

### Parameters

| model   [Autodesk.Viewing.Model](Viewing-Model.md) | The model, defaults to the loaded model. |
| --- | --- |

## [getProperties(dbid, onSuccessCallback, onErrorCallback)](#getproperties-dbid-onsuccesscallback-onerrorcallback)

Gets the properties for an ID.

### Parameters

| dbid*   number | The database identifier. |
| --- | --- |
| onSuccessCallback   [Callbacks#onPropertiesSuccess](https://aps.autodesk.com/en/docs/viewer/v7/reference/Callbacks/onPropertiesSuccess/) | Callback for when the properties are fetched. |
| onErrorCallback   [Callbacks#onGenericError](https://aps.autodesk.com/en/docs/viewer/v7/reference/Callbacks/onGenericError/) | Callback for when the properties are not found or another error occurs. |

* Required

## [getObjectTree(onSuccessCallback, onErrorCallback)](#getobjecttree-onsuccesscallback-onerrorcallback)

Gets the viewer model object tree. Once the tree is received it will invoke the specified callback function.

You can use the model object tree to get information about items in the model. The tree is made up of nodes, which correspond to model components such as assemblies or parts.

### Parameters

| onSuccessCallback   [Callbacks#onObjectTreeSuccess](https://aps.autodesk.com/en/docs/viewer/v7/reference/Callbacks/onObjectTreeSuccess/) | Success callback invoked once the object tree is available. |
| --- | --- |
| onErrorCallback   [Callbacks#onGenericError](https://aps.autodesk.com/en/docs/viewer/v7/reference/Callbacks/onGenericError/) | Error callback invoked when the object tree is not found available. |

## [setCanvasClickBehavior(config)](#setcanvasclickbehavior-config)

Sets the click behavior on the canvas to follow config. This is used to change the behavior of events such as selection or Center-of-Interest changed.

### Parameters

| config*   object | Parameter object that meets the above layout. |
| --- | --- |

* Required

### Examples

```
 {
     "click": {
         "onObject": [ACTIONS],
         "offObject": [ACTIONS]
     },
     "clickCtrl": {
         "onObject": [ACTIONS],
         "offObject": [ACTIONS]
     },
     "clickShift": {
         ...
     },
     "clickCtrlShift": {
         ...
     },
     "disableSpinner": BOOLEAN
     "disableMouseWheel": BOOLEAN,
     "disableTwoFingerSwipe": BOOLEAN
}

```

Show More

Actions can be any of the following: “selectOnly”, “selectToggle”, “deselectAll”, “isolate”, “showAll”, “setCOI”, “focus”, “hide”

---

## [search(text, onSuccessCallback, onErrorCallback, attributeNames, options)](#search-text-onsuccesscallback-onerrorcallback-attributenames-options)

Searches the elements for the given text. When the search is complete, the callback onResultsReturned(idArray) is invoked.

### Parameters

Expand all

| text*   string | The search term (not case sensitive). |
| --- | --- |
| onSuccessCallback*   [Callbacks#onSearchSuccess](https://aps.autodesk.com/en/docs/viewer/v7/reference/Callbacks/onSearchSuccess/) | Invoked when the search results are ready. |
| onErrorCallback*   [Callbacks#onGenericError](https://aps.autodesk.com/en/docs/viewer/v7/reference/Callbacks/onGenericError/) | Invoke when an error occured during search. |
| attributeNames   Array.<string> | Restricts search to specific attribute names. |
| options   Object | Search options. |
| searchHidden   boolean | Set to true to also search hidden properties |
| includeInherited   boolean | Set to true to include nodes that inherit the property |

* Required

## [getHiddenNodes(model)](#gethiddennodes-model)

Returns an array of the IDs of the currently hidden nodes. When isolation is in place, there are no hidden nodes returned because all nodes that are not isolated are considered hidden.

### Parameters

| model   [Autodesk.Viewing.Model](Viewing-Model.md) | Model object, if passed in the hidden nodes of the model are returned |
| --- | --- |

### Returns

| type | description |
| --- | --- |
| Array.<number> | Array of nodes that are currently hidden, when no isolation is in place. |

## [getIsolatedNodes(model)](#getisolatednodes-model)

Returns an array of the IDs of the currently isolated nodes.

Not yet implemented for 2D.

### Parameters

| model   [Autodesk.Viewing.Model](Viewing-Model.md) | Model object, if passed in the isolated nodes of the model are returned |
| --- | --- |

### Returns

| type | description |
| --- | --- |
| Array.<number> | Array of nodes that are currently isolated. |

## [isolate(node, model)](#isolate-node-model)

Isolates one of many sub-elements. You can pass in a node or an array of nodes to isolate. Pass in null to reset isolation.

### Parameters

| node*   Array.<number>, number | A node ID or array of node IDs from the model tree [BaseViewer#getObjectTree](#fixMe/). |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | the model that contains the node id. Defaults to the first loaded model. |

* Required

## [setBackgroundColor(red, green, blue, red2, green2, blue2)](#setbackgroundcolor-red-green-blue-red2-green2-blue2)

Sets the background colors, which will be used to create a gradient. Values are in the range [0..255]

### Parameters

| red*   number |  |
| --- | --- |
| green*   number |  |
| blue*   number |  |
| red2*   number |  |
| green2*   number |  |
| blue2*   number |  |

* Required

## [setBackgroundOpacity(opacity)](#setbackgroundopacity-opacity)

Sets the background opacity.

### Parameters

| opacity*   number | Value is in the range [0.0..1.0] |
| --- | --- |

* Required

## [toggleSelect(dbid, model, selectionType)](#toggleselect-dbid-model-selectiontype)

Toggles the selection for a given dbid. If it was unselected, it is selected. If it was selected, it is unselected.

Currently three ways of node selection are supported:

- Autodesk.Viewing.SelectionType.MIXED

> * Leaf nodes are selected using the overlayed selection type, and inner nodes are selected using regular selection type.

- Autodesk.Viewing.SelectionType.REGULAR

> * Nodes are tinted with the selection color.

- Autodesk.Viewing.SelectionType.OVERLAYED

> * Nodes are tinted with the selection color and shown on top of the not selected geometry.

Not yet implemented for 2D.

### Parameters

| dbid*   number |  |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | the model that contains the dbId. Uses the initial model loaded by default. |
| selectionType*   number | a member of Autodesk.Viewing.SelectionMode. |

* Required

## [select(dbids, model, selectionType)](#select-dbids-model-selectiontype)

Selects the array of ids. You can also pass in a single id instead of an array.

Currently three ways of node selection are supported:

- Autodesk.Viewing.SelectionType.MIXED

> * Leaf nodes are selected using the overlayed selection type, and inner nodes are selected using regular selection type.

- Autodesk.Viewing.SelectionType.REGULAR

> * Nodes are tinted with the selection color.

- Autodesk.Viewing.SelectionType.OVERLAYED

> * Nodes are tinted with the selection color and shown on top of the not selected geometry.

### Parameters

| dbids*   Array.<number>, number | element or array of elements to select. |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | the model instance containing the ids. |
| selectionType   number | a member of `Autodesk.Viewing.SelectionType`. |

* Required

## [clearSelection()](#clearselection)

Clears the selection. See [Autodesk.Viewing.Viewer3D#select](Viewing-Viewer3D.md#select/)

## [getSelectionVisibility()](#getselectionvisibility)

Returns information about the visibility of the current selection.

### Returns

| type | description |
| --- | --- |
| object | `{hasVisible:boolean, hasHidden:boolean}` |

## [getSelectionCount()](#getselectioncount)

Returns the number of nodes (dbIds) in the current selection.

### Returns

| type | description |
| --- | --- |
| number | number of selected nodes |

## [setSelectionMode(mode)](#setselectionmode-mode)

Sets selection granularity mode. Supported values are:

- Autodesk.Viewing.SelectionMode.LEAF_OBJECT: Always select the leaf objects in the hierarchy.
- Autodesk.Viewing.SelectionMode.FIRST_OBJECT: For a given node, selects the first non-composite (layer, collection, model) on the path from the root to the given node, and all children.
- Autodesk.Viewing.SelectionMode.LAST_OBJECT: For a given node, selects the nearest ancestor composite node and all children. Selects the input node itself in case there is no composite node in the path to the root node.

### Parameters

| mode*   number | The selection mode. |
| --- | --- |

* Required

## [getSelection()](#getselection)

Returns the current selection.

### Returns

| type | description |
| --- | --- |
| Array.<number> | Array of the nodes (dbIds) of the currently selected nodes. |

## [lockSelection(dbIds, lock, model)](#lockselection-dbids-lock-model)

Locks the selection of specific `nodes` (dbIds) in a given model. The `nodes` will be unselected if the `lock` is set to true and the nodes are already selected. The locked nodes will not be selectable.

### Parameters

| dbIds*   Number, Array.<Number> | dbIds to lock |
| --- | --- |
| lock*   Boolean | true to lock, false otherwise |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | The model that contains the dbId. By default uses the initial model loaded into the scene. |

* Required

## [unlockSelection(dbIds, model)](#unlockselection-dbids-model)

This function will unlock the specified `nodes` (dbIds) for a specific `model`. If the `nodes` parameter is omitted then the specified `model`’s locked nodes will be unlocked. If the `model` parameter is omitted then the specified `nodes` will be unlocked for the viewer.model. If both parameters are omitted then all of the models in the viewer will release their locked nodes.

### Parameters

| dbIds   Array.<Number> | dbIds to unlock |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | The model associated to the nodes parameters |

## [isSelectionLocked(dbId, model)](#isselectionlocked-dbid-model)

Checks whether selection is locked for a node

### Parameters

| dbId*   number | the object’s identifier. |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | the model that contains the dbId. By default uses the initial model loaded into the scene. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True is the visibility is locked |

## [getAggregateSelection(callback)](#getaggregateselection-callback)

Returns the selected items from all loaded models.

### Parameters

| callback   function | Optional callback to receive enumerated pairs of model and dbId for each selected object. If no callback is given, an array of objects is returned. |
| --- | --- |

### Returns

| type | description |
| --- | --- |
| Array.<object> | An array of objects with a model and selectionSet properties for each model that has selected items in the scene. |

## [setAggregateSelection(selection, fireEvent)](#setaggregateselection-selection-fireevent)

Selects ids from different models. Choose this api instead of select() when selecting across many models

### Parameters

| selection*   Array.<SelectionDef> | Array of selection objects defining what to select |
| --- | --- |
| fireEvent   Boolean | Whether an event is fired at the end |

* Required

## [getAggregateIsolation()](#getaggregateisolation)

Returns the isolated items from all loaded models.

### Returns

| type | description |
| --- | --- |
| Array.<{model: Autodesk.Viewing.Model, ids: Array.<number>}> | An array of objects with a `model` and the isolated `ids` in that model. |

## [setAggregateIsolation(isolation)](#setaggregateisolation-isolation)

Isolate ids from different models. Choose this api instead of isolate() when isolating across many models. It will hide all other models.

### Parameters

| isolation*   Array.<{model: Autodesk.Viewing.Model, ids: (Array.<number>\|number)}> | An array of objects with a `model` and the `ids` to isolate in that model |
| --- | --- |

* Required

## [getAggregateHiddenNodes()](#getaggregatehiddennodes)

Returns the hidden nodes for all loaded models.

### Returns

| type | description |
| --- | --- |
| Array.<{model: Autodesk.Viewing.Model, ids: Array.<number>}> | An array of objects with a `model` and the hidden `ids` in that model. |

## [hide(node, model)](#hide-node-model)

Ensures the passed in nodes (dbIds) are hidden.

### Parameters

| node*   Array.<number>, number | An array of nodes (dbids) or just a single node. |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | The model that contains the dbId. By default uses the initial model loaded into the scene. |

* Required

## [show(node, model)](#show-node-model)

Ensures the passed in nodes (dbIds) are shown.

### Parameters

| node*   Array.<number>, number | An array of nodes (dbids) or just a single node. |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | The model that contains the dbId. By default uses the initial model loaded into the scene. |

* Required

## [showAll()](#showall)

Ensures everything is visible. Clears all node isolation (3D) and turns on all layers (2D).

## [hideAll()](#hideall)

Ensures all objects are hidden. Clears all nodes.

## [toggleVisibility(dbId, model)](#togglevisibility-dbid-model)

Toggles the visibility of the given node (dbId).

Not yet implemented for 2D.

### Parameters

| dbId*   number | the object’s identifier. |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | the model that contains the dbId. By default uses the initial model loaded into the scene. |

* Required

## [areAllVisible()](#areallvisible)

Returns true if every node (dbId) is visible.

### Returns

| type | description |
| --- | --- |
| boolean | True if every node is visible, false otherwise. |

## [isNodeVisible(nodeId, model)](#isnodevisible-nodeid-model)

Returns true if the specified node is visible. The model argument is required only when in multi-model scenarios.

### Parameters

| nodeId*   number | Geometry node to check if visible. |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | The model that contains the specified `nodeId`. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean |  |

## [lockVisible(dbId, locked, model)](#lockvisible-dbid-locked-model)

Ensures the passed in nodes (dbIds) are shown.

### Parameters

| dbId*   Array.<number>, number | array of nodes or a single node |
| --- | --- |
| locked*   boolean | Set to true to lock the nodes visible. Set to false to allow the nodes to be hidden. |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | The model that contains the dbId. By default uses the initial model loaded into the scene. |

* Required

## [toggleLockVisible(dbId, model)](#togglelockvisible-dbid-model)

Toggles the visibility lock of the given node (dbId).

Not yet implemented for 2D.

### Parameters

| dbId*   number | the object’s identifier. |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | the model that contains the dbId. By default uses the initial model loaded into the scene. |

* Required

## [isVisibleLocked(dbId, model)](#isvisiblelocked-dbid-model)

Checks whether visibility is locked for a node (dbId).

Not yet implemented for 2D.

### Parameters

| dbId*   number | the object’s identifier. |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | the model that contains the dbId. By default uses the initial model loaded into the scene. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True is the visibility is locked |

## [explode(scale, options)](#explode-scale-options)

Explodes the model from the center of gravity.

Not applicable to 2D.

### Parameters

Expand all

| scale*   number | A value from 0.0-1.0 to indicate how much to explode. |
| --- | --- |
| options*   Object | Additional setting for STRATEGY_HIERARCHY. |
| magnitude*   Number | Controls the spread of explode. |
| depthDampening*   Number | Controls the reduction of the explode effect with depth of the object in the hierarchy. |

* Required

## [getExplodeScale()](#getexplodescale)

Returns the explode scale.

Not applicable to 2D.

### Returns

| type | description |
| --- | --- |
| number | A value from 0.0-1.0 indicating how exploded the model is. |

## [getExplodeOptions()](#getexplodeoptions)

Returns the explode options.

Not applicable to 2D.

### Returns

| type | description |
| --- | --- |
| object | `{magnitude:Number, depthDampening:Number}` |

## [lockExplode(dbids, lock, model)](#lockexplode-dbids-lock-model)

Lock node (dbid) so that it doesn’t explode

Not applicable to 2D.

### Parameters

| dbids*   Array.<number>, number | The dbids to lock or unlock |
| --- | --- |
| lock*   boolean | Set to true to prevent dbids from exploding. Set to false to allow dbids to explode. |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | The model containing the dbids. Defaults to this.model |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if any dbids were changed. |

## [isExplodeLocked(dbid, model)](#isexplodelocked-dbid-model)

Check whether a dbid is locked so it doesn’t explode.

Not applicable to 2D.

### Parameters

| dbid*   number | The dbid to check |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | The model containing the dbids. Defaults to this.model |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if dbid is locked to prevent explode |

## [toggleLockExplode(dbid, model)](#togglelockexplode-dbid-model)

Toggle dbid lock so it doesn’t explode

Not applicable to 2D.

### Parameters

| dbid*   number | The dbid to lock or unlock |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | The model containing the dbids. Defaults to this.model |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if any dbids were changed. |

## [setQualityLevel(useSAO, useFXAA)](#setqualitylevel-usesao-usefxaa)

Enables or disables the high quality rendering settings.

Not applicable to 2D.

### Parameters

| useSAO*   boolean | True or false to enable screen space ambient occlusion. |
| --- | --- |
| useFXAA*   boolean | True or false to enable fast approximate anti-aliasing. |

* Required

## [setGhosting(value)](#setghosting-value)

Toggles ghosting during search and isolate.

Not applicable to 2D.

### Parameters

| value*   boolean | Indicates whether ghosting is on or off. |
| --- | --- |

* Required

## [setGroundShadow(value)](#setgroundshadow-value)

Toggles ground shadow.

Not applicable to 2D.

### Parameters

| value*   boolean | Indicates whether shadow is on or off. |
| --- | --- |

* Required

## [setGroundReflection(value)](#setgroundreflection-value)

Toggles ground reflection.

Not applicable to 2D.

### Parameters

| value*   boolean | Indicates whether reflection is on or off. |
| --- | --- |

* Required

## [setEnvMapBackground(value)](#setenvmapbackground-value)

Toggles environment map for background.

Not applicable to 2D.

### Parameters

| value*   boolean | Indicates whether environment map for background is on or off. |
| --- | --- |

* Required

## [setBimWalkToolPopup(value)](#setbimwalktoolpopup-value)

Toggles the bimwalk tool popup.

Not applicable to 2D.

### Parameters

| value*   boolean | Indicates whether first person tool popup is showed or not. |
| --- | --- |

* Required

## [getBimWalkToolPopup()](#getbimwalktoolpopup)

Returns the state of First Person Walk tool popup

Not applicable to 2D.

### Returns

| type | description |
| --- | --- |
| boolean | true if the First Person Walk tool popup appears, false if the First Person Walk tool popup does not appear. |

## [setProgressiveRendering(value)](#setprogressiverendering-value)

Toggles whether progressive rendering is used. Warning: turning progressive rendering off will have serious performance implications.

### Parameters

| value*   boolean | whether it is on or off |
| --- | --- |

* Required

## [setGrayscale(value)](#setgrayscale-value)

Overrides line colors in 2D models to render in shades of gray. Applies only to 2D models.

### Parameters

| value*   boolean | whether it is on or off |
| --- | --- |

* Required

## [setSwapBlackAndWhite(value)](#setswapblackandwhite-value)

AutoCAD drawings are commonly displayed with white lines on a black background. Setting reverse swaps (just) these two colors.

### Parameters

| value*   boolean | whether it is on or off |
| --- | --- |

* Required

## [setOptimizeNavigation(value)](#setoptimizenavigation-value)

Toggles whether the navigation should be optimized for performance. If set to true, anti-aliasing and ambient shadows will be off while navigating.

Not applicable to 2D.

### Parameters

| value*   boolean | whether it is on or off |
| --- | --- |

* Required

## [setNavigationLock(value)](#setnavigationlock-value)

Locks or unlocks navigation controls.

When navigation is locked, certain operations (for example, orbit, pan, or fit-to-view) are disabled.

Reference [Autodesk.Viewing.Viewer3D#setNavigationLockSettings](Viewing-Viewer3D.md#setNavigationLockSettings/)

### Parameters

| value*   boolean | True if the navigation should be locked. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | The previous state of the lock (this may be used to restore the lock to it’s previous state). |

## [getNavigationLock()](#getnavigationlock)

Gets the current state of the navigation lock.

### Returns

| type | description |
| --- | --- |
| boolean | True if the navigation controls are currently locked. |

## [setNavigationLockSettings(settings)](#setnavigationlocksettings-settings)

Updates the configuration of the navigation lock, i.e., which actions are available when navigation is locked.

The configurable actions are ‘orbit’, ‘pan’, ‘zoom’, ‘roll’, ‘fov’, ‘walk’, or ‘gotoview’. By default, none of the actions are enabled when the navigation is locked.

Reference [Autodesk.Viewing.Viewer3D#setNavigationLock](Viewing-Viewer3D.md#setNavigationLock/)

### Parameters

| settings*   object | Map of : pairs specifying whether the given action is enabled even when the navigation is locked. |
| --- | --- |

* Required

## [getNavigationLockSettings()](#getnavigationlocksettings)

Gets the current configuration of the navigation lock.

### Returns

| type | description |
| --- | --- |
| object | Map of : pairs specifying whether the given action is enabled even when the navigation is locked. |

## [setActiveNavigationTool(toolName)](#setactivenavigationtool-toolname)

Swaps the current navigation tool for the tool with the provided name. Will trigger NAVIGATION_MODE_CHANGED event if the mode actually changes.

Reference [Viewer3D#getActiveNavigationTool](Viewing-Viewer3D.md#getActiveNavigationTool/)

### Parameters

| toolName   string | The name of the tool to activate. By default it will switch to the default tool. |
| --- | --- |

### Returns

| type | description |
| --- | --- |
| boolean | True if the tool was set successfully. False otherwise. |

## [getActiveNavigationTool()](#getactivenavigationtool)

Returns the name of the active navigation tool.

Reference [Viewer3D#setActiveNavigationTool](Viewing-Viewer3D.md#setActiveNavigationTool/)

### Returns

| type | description |
| --- | --- |
| string | The tool’s name. |

## [setDefaultNavigationTool(toolName)](#setdefaultnavigationtool-toolname)

Sets the default navigation tool. This tool will always sit beneath the navigation tool on the tool stack.

### Parameters

| toolName*   string | The name of the new default navigation tool. |
| --- | --- |

* Required

## [getDefaultNavigationToolName()](#getdefaultnavigationtoolname)

Returns the default navigation tool

### Returns

| type | description |
| --- | --- |
| Object | The default navigation tool. |

## [getFOV()](#getfov)

Gets the current camera vertical field of view.

### Returns

| type | description |
| --- | --- |
| number | the field of view in degrees. |

## [setFOV(degrees)](#setfov-degrees)

Sets the current cameras vertical field of view.

### Parameters

| degrees*   number | Field of view in degrees. |
| --- | --- |

* Required

## [getFocalLength()](#getfocallength)

Gets the current camera focal length.

### Returns

| type | description |
| --- | --- |
| number | the focal length in millimetres. |

## [setFocalLength(mm)](#setfocallength-mm)

Sets the current cameras focal length.

### Parameters

| mm*   number | Focal length in millimetres |
| --- | --- |

* Required

## [hideLines(hide)](#hidelines-hide)

Hides all lines in the scene.

### Parameters

| hide*   boolean |  |
| --- | --- |

* Required

## [hidePoints(hide)](#hidepoints-hide)

Hides all points in the scene.

### Parameters

| hide*   boolean |  |
| --- | --- |

* Required

## [setDisplayEdges(show)](#setdisplayedges-show)

Turns edge topology display on/off (where available).

### Parameters

| show*   boolean | true to turn edge topology display on, false to turn edge topology display off. |
| --- | --- |

* Required

## [applyCamera(camera, fit)](#applycamera-camera-fit)

### Parameters

| camera*   THREE.Camera | the camera to apply. |
| --- | --- |
| fit   boolean | Do a fit to view after transition. |

* Required

## [fitToView(objectIds, model, immediate)](#fittoview-objectids-model-immediate)

Fits camera to objects by ID. It fits the entire model if no ID is provided. Operation will fit to the model’s bounding box when its object tree is not available.

### Parameters

| objectIds   Array.<number>, null | array of Ids to fit into the view. Avoid passing this value to fit the entire model. |
| --- | --- |
| model   [Autodesk.Viewing.Model](Viewing-Model.md), null | The model containing the `objectIds`. If falsey, the viewer’s current model will be used. |
| immediate   boolean | true to avoid the default transition. |

## [setClickConfig(what, where, newAction)](#setclickconfig-what-where-newaction)

Modifies a click action configuration entry.

### Parameters

| what*   string | which click config to modify (one of “click”, “clickAlt”, “clickCtrl”, “clickShift”, “clickCtrlShift”). |
| --- | --- |
| where*   string | hit location selector (one of “onObject”, “offObject”). |
| newAction*   Array.<string> | action list (containing any of “setCOI”, “selectOnly”, “selectToggle”, “deselectAll”, “deselectAll”, “isolate”, “showAll”, “hide”, “focus”). |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | False if specified entry is not found, otherwise true. |

## [getClickConfig(what, where)](#getclickconfig-what-where)

Fetch a click action configuration entry.

### Parameters

| what*   string | which click config to fetch (one of “click”, “clickAlt”, “clickCtrl”, “clickShift”, “clickCtrlShift”). |
| --- | --- |
| where*   string | hit location selector (one of “onObject”, “offObject”). |

* Required

### Returns

| type | description |
| --- | --- |
| array | action list for the given entry or null if not found. |

## [setClickToSetCOI(state, updatePrefs)](#setclicktosetcoi-state-updateprefs)

Modify the default click behaviour for the viewer. COI is Center of Interest.

### Parameters

| state*   boolean | If true the default is to set the center of interest. If false the default is single select. |
| --- | --- |
| updatePrefs   boolean | Whether to update user preferences. Defaults to true unless explicitly set to false. |

* Required

## [setProfile(profile, override)](#setprofile-profile-override)

Updates viewer settings encapsulated witihn a Profile. This method will also load and unload extensions referenced by the Profile.

### Parameters

| profile*   [Autodesk.Viewing.Profile](Viewing-Profile.md) | profile containing settings. |
| --- | --- |
| override   boolean | If set to true this will override all existing preference with the new profile preference. Default: true |

* Required

### Examples

```
const profileSettings = {
   name: "mySettings",
   settings: {
       ambientShadows: false,
       groundShadows: true
   }
   extensions: {
       load: [],   // Extension IDs
       unload: []  // Extension IDs
   }
}
const profile = new Autodesk.Viewing.Profile(profileSettings);
viewer.setProfile(profile);

```

Show More

---

## [setLightPreset(index)](#setlightpreset-index)

Sets the Light Presets (Environments) for the Viewer.

Not applicable to 2D.

Sets the preference in the UI

### Parameters

| index*   Number | The index mapping looks like this: 0 -> Simple Grey, 1 -> Sharp Highlights, 2 -> Dark Sky, 3 -> Grey Room, 4 -> Photo Booth, 5 -> Tranquility, 6 -> Infinity Pool, 7 -> Simple White, 8 -> Riverbank, 9 -> Contrast, 1 ->0 Rim Highlights, 1 ->1 Cool Light, 1 ->2 Warm Light, 1 ->3 Soft Light, 1 ->4 Grid Light, 1 ->5 Plaza, 1 ->6 Snow Field |
| --- | --- |

* Required

## [setUsePivotAlways(value)](#setusepivotalways-value)

Set or unset a view navigation option which requests that orbit controls always orbit around the currently set pivot point.

Sets the preference in the UI

### Parameters

| value*   boolean | value of the option, true to request use of the pivot point. When false some controls may pivot around the center of the view. (Currently applies only to the view-cube orbit controls.) |
| --- | --- |

* Required

## [setReverseZoomDirection(value)](#setreversezoomdirection-value)

Set or unset a view navigation option to reverse the default direction for camera dolly (zoom) operations.

Sets the preference in the UI

### Parameters

| value*   boolean | value of the option, true for reverse, false for default |
| --- | --- |

* Required

## [setReverseHorizontalLookDirection(value)](#setreversehorizontallookdirection-value)

Set or unset a view navigation option to reverse the default direction for horizontal look operations.

Not applicable to 2D.

Sets the preference in the UI

### Parameters

| value*   boolean | value of the option, true for reverse, false for default |
| --- | --- |

* Required

## [setReverseVerticalLookDirection(value)](#setreverseverticallookdirection-value)

Set or unset a view navigation option to reverse the default direction for vertical look operations.

Not applicable to 2D.

Sets the preference in the UI

### Parameters

| value*   boolean | value of the option, true for reverse, false for default |
| --- | --- |

* Required

## [setZoomTowardsPivot(value)](#setzoomtowardspivot-value)

Get the state of the view navigation option that requests the default direction for camera dolly (zoom) operations to be towards the camera pivot point.

Sets the preference in the UI

### Parameters

| value*   boolean | value of the option, true for towards the pivot, false for default |
| --- | --- |

* Required

## [setOrbitPastWorldPoles(value)](#setorbitpastworldpoles-value)

Set or unset a view navigation option to allow the orbit controls to move the camera beyond the north and south poles (world up/down direction). In other words, when set the orbit control will allow the camera to rotate into an upside down orientation. When unset orbit navigation should stop when the camera view direction reaches the up/down direction.

Not applicable to 2D.

Sets the preference in the UI

### Parameters

| value*   boolean | value of the option, true to allow orbiting past the poles. |
| --- | --- |

* Required

## [setUseLeftHandedInput(value)](#setuselefthandedinput-value)

Set or unset a view navigation option which requests that mouse buttons be reversed from their default assignment (i.e. Left mouse operation becomes right mouse and vice versa).

Sets the preference in the UI

### Parameters

| value*   boolean | value of the option, true to request reversal of mouse button assignments. |
| --- | --- |

* Required

## [setZoomDragSpeed(value)](#setzoomdragspeed-value)

Set a sensitivity of mouse movement with the zoom tool

Sets the preference in the UI

### Parameters

| value*   number | value of the option, can be between 5 and 300. Default is 100. |
| --- | --- |

* Required

## [setZoomScrollSpeed(value)](#setzoomscrollspeed-value)

Set a sensitivity of the mouse scroll wheel when zooming

Sets the preference in the UI

### Parameters

| value*   number | value of the option, can be between 0.1 and 3.0. Default is 0.6. |
| --- | --- |

* Required

## [setDisplayUnits(value)](#setdisplayunits-value)

Set units for quantities displayed in the property panel. Only setting linear (distance) quantity units are supported

### Parameters

| value*   string | display units to set. The units can be “” (file units), “mm”, “cm”, “m”, “in”, “ft”, “ft-and-fractional-in”, “ft-and-decimal-in”, “decimal-in”, “decimal-ft”, “fractional-in”, “m-and-cm”, |
| --- | --- |

* Required

## [setDisplayUnitsPrecision(value)](#setdisplayunitsprecision-value)

Set the precision for quantities displayed in the property panel.

### Parameters

| value*   number | precision for the units The value is the number of decimal values after the “.”. For e.g., a value of 5 would be either 0.12345 or 1/32 (2^5) for fraction type units Values greater than 6 is not supported If value is not specified, it defaults to the precision in the file |
| --- | --- |

* Required

## [setLayerVisible(nodes, visible, isolate)](#setlayervisible-nodes-visible-isolate)

Set visibility for a single layer, or for all layers.

### Parameters

| nodes*   Array | An array of layer nodes, or a single layer node, or null for all layers |
| --- | --- |
| visible*   boolean | true to show the layer, false to hide it |
| isolate   boolean | true to isolate the layer |

* Required

## [isLayerVisible(node)](#islayervisible-node)

Returns true if the layer is visible.

### Parameters

| node*   Object | Layer node |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the layer is visible |

## [anyLayerHidden()](#anylayerhidden)

Returns true if any layer is hidden.

### Returns

| type | description |
| --- | --- |
| boolean | true if any layer is hidden |

## [allLayersHidden()](#alllayershidden)

Returns true if all layers are hiden.

### Returns

| type | description |
| --- | --- |
| boolean | true if all layers are hidden |

## [hideHiddenObjects()](#hidehiddenobjects)

## [setGroundShadowColor(color)](#setgroundshadowcolor-color)

If enabled, set ground shadow color

Not applicable to 2D

### Parameters

| color*   THREE.Color |  |
| --- | --- |

* Required

## [setGroundShadowAlpha(alpha)](#setgroundshadowalpha-alpha)

If enabled, set ground shadow alpha

Not applicable to 2D

### Parameters

| alpha*   float |  |
| --- | --- |

* Required

## [setGroundReflectionColor(color)](#setgroundreflectioncolor-color)

If enabled, set ground reflection color. This is reset to default when reflections toggled off.

Not applicable to 2D

### Parameters

| color*   THREE.Color |  |
| --- | --- |

* Required

## [setGroundReflectionAlpha(alpha)](#setgroundreflectionalpha-alpha)

If enabled, set ground reflection alpha. This is reset to default when reflections toggled off.

Not applicable to 2D

### Parameters

| alpha*   number |  |
| --- | --- |

* Required

## [getCutPlanes()](#getcutplanes)

Returns a list of active cut planes

Not applicable to 2D

### Returns

| type | description |
| --- | --- |
| Array.<THREE.Vector4> | List of Vector4 plane representation {x:a, y:b, z:c, w:d} |

## [setCutPlanes(planes)](#setcutplanes-planes)

Apply a list of cut planes

Not applicable to 2D

### Parameters

| planes*   Array.<THREE.Vector4> | List of Vector4 plane representation: {x:a, y:b, z:c, w:d} Plane general equation: ax + by + cz + d = 0 where a, b, and c are not all zero Passing an empty list or null is equivalent to setting zero cut planes |
| --- | --- |

* Required

## [getScreenShot(w, h, cb, overlayRenderer)](#getscreenshot-w-h-cb-overlayrenderer)

Captures the current screen image as Blob URL Blob URL can be used like a regular image url (e.g., window.open, img.src, etc) If width and height are 0, returns asynchronously and calls the callback with an image as Blob URL with dimensions equal to current canvas dimensions If width and height are given, returns asynchronously and calls the callback with the resized image as Blob URL If no callback is given, displays the image in a new window. Optional overlayRenderer can be supplied, in order to render an overlay on top of the renderer image.

### Parameters

| w   number | width of the requested image |
| --- | --- |
| h   number | height of the requested image |
| cb   function | callback |
| overlayRenderer   function | overlayRenderer |

### Returns

| type | description |
| --- | --- |
| DOMString | screenshot image Blob URL, if no parameters are given |

## [worldToClient(point, camera)](#worldtoclient-point-camera)

Calculates the pixel position in client space coordinates of a point in world space.
See also [Autodesk.Viewing.Viewer3D#clientToWorld](Viewing-Viewer3D.md#clientToWorld/).

### Parameters

| point*   THREE.Vector3 | Point in world space coordinates. |
| --- | --- |
| camera*   THREE.Camera | Optional camera to use - default is the viewer’s native camera. |

* Required

### Returns

| type | description |
| --- | --- |
| THREE.Vector3 | Point transformed and projected into client space coordinates. Z value is 0. |

## [clientToWorld(clientX, clientY, ignoreTransparent, ignore2dModelBounds, ignore2dModelsOn3d)](#clienttoworld-clientx-clienty-ignoretransparent-ignore2dmodelbounds-ignore2dmodelson3d)

Given coordinates in pixel screen space it returns information of the underlying geometry node. Hidden nodes will not be taken into account. Returns null if there is no geometry in the specified location. For 2d models, it will return null outside the paper, unless ignore2dModelBounds is true.
See also [Autodesk.Viewing.Viewer3D#worldToClient](Viewing-Viewer3D.md#worldToClient/).

- Activate a state through [Autodesk.Viewing.Viewer3D#activateLayerState](Viewing-Viewer3D.md#activateLayerState/).

### Parameters

| clientX*   Number | X coordinate where 0 is left |
| --- | --- |
| clientY*   Number | Y coordinate where 0 is top |
| ignoreTransparent   Boolean | Ignores transparent materials |
| ignore2dModelBounds   boolean | For 2d models - whether to return a result outside of the model’s bounds. |
| ignore2dModelsOn3d   boolean | Whether to ignore 2d models when in 3d mode. |

* Required

### Returns

| type | description |
| --- | --- |
| Object, null | contains point attribute. 3d models have additional attributes. |

## [modelHasTopology()](#modelhastopology)

Expose if the model has topology information downloaded. Only applicable to 3D models.

### Returns

| type | description |
| --- | --- |
| boolean | value - Indicates whether the model has topology information. |

## [setSelectionColor(color, selectionType)](#setselectioncolor-color-selectiontype)

Changes the color of the selection for a particular selection type.

- Autodesk.Viewing.SelectionType.MIXED

> * Sets the same color for regular and overlayed selection.

- Autodesk.Viewing.SelectionType.REGULAR

> * Sets the color of regular selection.

- Autodesk.Viewing.SelectionType.OVERLAYED

> * Sets the color of overlayed selection.

### Parameters

| color*   THREE.Color |  |
| --- | --- |
| selectionType*   number | a member of Autodesk.Viewing.SelectionMode. |

* Required

### Examples

```
viewer.setSelectionColor(new THREE.Color(0xFF0000), Autodesk.Viewing.SelectionType.MIXED); // red color

```

---

## [set2dSelectionColor(color, opacity)](#set2dselectioncolor-color-opacity)

Changes the color of the selection for 2D drawings.

### Parameters

| color*   THREE.Color |  |
| --- | --- |
| opacity*   number |  |

* Required

### Examples

```
viewer.set2dSelectionColor(new THREE.Color(0xFF0000), 0.1); // red color, opacity of 0.1

```

---

## [setTheme(name)](#settheme-name)

Sets the current UI theme of the viewer. Supported values are “light-theme” and “dark-theme”, which is the default.

### Parameters

| name*   string | Name of the theme, it will be added to the viewer’s container class list. |
| --- | --- |

* Required

## [setThemingColor(dbId, color, model, recursive)](#setthemingcolor-dbid-color-model-recursive)

Highlight an object with a theming color that is blended with the original object’s material.

### Parameters

| dbId*   number |  |
| --- | --- |
| color*   THREE.Vector4 | (r, g, b, intensity), all in [0,1]. |
| model   [Autodesk.Viewing.Model](Viewing-Model.md) | For multi-model support. |
| recursive   boolean | Should apply theming color recursively to all child nodes. |

* Required

## [clearThemingColors(model)](#clearthemingcolors-model)

Restore original colors for all themed shapes.

### Parameters

| model   [Autodesk.Viewing.Model](Viewing-Model.md) | For multi-model support. |
| --- | --- |

## [setMaterialsToDefaults(model)](#setmaterialstodefaults-model)

Restore original materials of a model if they were overwritten, e.g. by Autodesk.Viewing.Viewer3D#setView.”

### Parameters

| model   [Autodesk.Viewing.Model](Viewing-Model.md) | For multi-model support. |
| --- | --- |

## [hideModel(model)](#hidemodel-model)

Temporarily remove a model from the Viewer, but keep loaders, materials, and geometry alive.

Reference [Autodesk.Viewing.Viewer3D#showModel](Viewing-Viewer3D.md#showModel/)

### Parameters

| model*   number, [Autodesk.Viewing.Model](Viewing-Model.md) | model id or Model object |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true indicates success, i.e., modelId referred to a visible model that is now hidden |

## [showModel(model, preserveTools)](#showmodel-model-preservetools)

Make a previously hidden model visible again.

Reference [Autodesk.Viewing.Viewer3D#hideModel](Viewing-Viewer3D.md#hideModel/)

### Parameters

| model*   number, [Autodesk.Viewing.Model](Viewing-Model.md) | model id or Model object |
| --- | --- |
| preserveTools*   boolean | disable automatic activation of default tool |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true indicates success, i.e., `model` referred to a hidden model that is now visible |

## [getVisibleModels()](#getvisiblemodels)

### Returns

| type | description |
| --- | --- |
| Array.<Autodesk.Viewing.Model> |  |

## [getHiddenModels()](#gethiddenmodels)

### Returns

| type | description |
| --- | --- |
| Array.<Autodesk.Viewing.Model> |  |

## [getAllModels()](#getallmodels)

Returns all models loaded in the viewer.

### Returns

| type | description |
| --- | --- |
| Array.<Autodesk.Viewing.Model> | An array of visible and hidden models |

## [getFirstModel()](#getfirstmodel)

Returns the first model, according to the environment. If we are in 2D, returns the first sheet. If we are in 3D, returns the first 3D model, regardless if a 2D sheet was loaded before. Note: If there’s only 2D models in a 3D environment it will return null.

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.Model](Viewing-Model.md) | A model |

## [getUnderlayRaster(bubbleNode)](#getunderlayraster-bubblenode)

When loading a PDF document we optionally add a raster preview. This function returns the preview corresponding to the passed bubbleNode.

### Parameters

| bubbleNode*   [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) |  |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Array.<Autodesk.Viewing.Model> |  |

## [disableHighlight(disable)](#disablehighlight-disable)

Disables roll-over highlighting.

### Parameters

| disable*   boolean | Indicates whether highlighting should be on or off. True to disable highlights, false to enable them. |
| --- | --- |

* Required

## [disableSelection(disable)](#disableselection-disable)

disable the selection of a loaded model.

### Parameters

| disable*   boolean | true to disable selection, false to enable selection. |
| --- | --- |

* Required

## [isHighlightDisabled()](#ishighlightdisabled)

check if the mouse-over highlight is disabled or not

## [isHighlightPaused()](#ishighlightpaused)

check if the mouse-over highlight is paused or not

## [isHighlightActive()](#ishighlightactive)

check if the mouse-over highlight is active or not

## [isSelectionDisabled()](#isselectiondisabled)

check if the selection of the loaded model is disabled or not

## [activateExtension(extensionID, mode)](#activateextension-extensionid-mode)

Activates the extension based on the extensionID and mode given. By default it takes the first available mode in getmodes();

### Parameters

| extensionID*   string | The extension id. |
| --- | --- |
| mode   string |  |

* Required

## [deactivateExtension(extensionID)](#deactivateextension-extensionid)

Dectivates the extension based on the extensionID specified.

### Parameters

| extensionID*   string | the extension ID |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the extension was deactivated false otherwise |

## [isExtensionActive(extensionID, mode)](#isextensionactive-extensionid-mode)

Check if the extension is active or not by passing the extensionID.

### Parameters

| extensionID*   string | the extension ID |
| --- | --- |
| mode*   string | The model of the extension |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the extension is active, false otherwise |

## [isExtensionLoaded(extensionID)](#isextensionloaded-extensionid)

Check if the extension is loaded or not by passing the extensionID.

### Parameters

| extensionID*   string | the extension ID |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | returns true if the extension was loaded, false otherwise |

## [getLoadedExtensions()](#getloadedextensions)

Get a list of all the extensions that are currently loaded.

### Returns

| type | description |
| --- | --- |
| Array.<string> | returns the IDs of all of the loaded extensions |

## [getExtensionModes(extensionID)](#getextensionmodes-extensionid)

Get a list of all the modes that are available for the given extensionID.

### Parameters

| extensionID*   string | the extension ID |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Array.<string> | array of the extension’s modes. |

## [hitTest(x, y, ignoreTransparent)](#hittest-x-y-ignoretransparent)

Returns the intersection information for point x,y. If no intersection is found this function will return null.

### Parameters

| x*   number | X-coordinate, i.e., horizontal distance (in pixels) from the left border of the canvas. |
| --- | --- |
| y*   number | Y-coordinate, i.e., vertical distance (in pixels) from the top border of the canvas. |
| ignoreTransparent   boolean | ignores any transparent objects that might intersect x,y |

* Required

### Returns

| type | description |
| --- | --- |
| [Intersection](globals-TypeDefs-Intersection.md), null | Intersection information about closest hit point. |

## [refresh(clear)](#refresh-clear)

Clears the screen and redraws the overlays if clear is set to true. Only the overlays will be redrawn if clear is set to false. Should only be called when absolutely needed.

### Parameters

| clear*   boolean | clears the screen and redraws the overlays. |
| --- | --- |

* Required

## [chooseProfile()](#chooseprofile)

Function that decides which [Autodesk.Viewing.Profile](Viewing-Profile.md) to use when a model is loaded for the first time.

Override this method to implement a different logic.

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.Profile](Viewing-Profile.md), null | a Profile |
