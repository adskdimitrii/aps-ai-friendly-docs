# MarkupsCore

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/MarkupsCore/

---

Autodesk.Viewing.Extensions

# MarkupsCore

## [new MarkupsCore(viewer, options)](#new-markupscore-viewer-options)

Extension that allows end users to draw 2D markups on top of 2D and 3D models.

### Parameters

Expand all

| viewer*   [Autodesk.Viewing.Viewer3D](Viewing-Viewer3D.md) | Viewer instance used to operate on. |
| --- | --- |
| options*   object | Same Dictionary object passed into [Viewer3D](Viewing-Viewer3D.md)âs constructor. |
| markupDisableHotkeys   boolean | Disables hotkeys for copy, cut, paste, duplicate, undo, redo and deselect. |
| markupToolClass   [Autodesk.Viewing.ToolInterface](Viewing-ToolInterface.md) | Class override for input handling. Use it to override/extend default hotkeys and/or mouse/gesture input. |

* Required

# Methods

## [enterEditMode(layerId)](#entereditmode-layerid)

Enables mouse interactions and mobile device gestures over the Viewer canvas to create or draw markups.

Exit Edit mode by calling [leaveEditMode()](Extensions-MarkupsCore.md#leaveeditmode-1/).

See also [show()](Extensions-MarkupsCore.md#show/)

### Parameters

| layerId*   string | [optional] Identifier for the layer of markups to be edited. Example âLayer1â. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | Returns true if editMode is active |

## [leaveEditMode()](#id2)

Exits Edit mode.

See also [enterEditMode()](Extensions-MarkupsCore.md#entereditmode-layerid/).

### Returns

| type | description |
| --- | --- |
| boolean | Returns true if Edit mode has been deactivated |

## [toggle()](#toggle)

Toggle between visible markups, i.e., show() and hidden markups, i.e., hide().

## [show()](#id4)

Enables loading of previously saved markups. Exit Edit mode by calling [hide()](Extensions-MarkupsCore.md#hide/).

See also [enterEditMode()](Extensions-MarkupsCore.md#entereditmode-layerid/).

### Returns

| type | description |
| --- | --- |
| boolean | Whether it successfully entered view mode or not. |

## [hide()](#id7)

Removes any markup currently overlaid on the viewer. It exits Edit mode if it is active.

See also [show()](Extensions-MarkupsCore.md#show/)

### Returns

| type | description |
| --- | --- |
| boolean | Whether it successfully left view mode or not. |

## [clear()](#clear)

Removes newly created markups in the current editing layer. Markups that were created in a specific layer will not be removed.

Markups should have been added while in [enterEditMode()](Extensions-MarkupsCore.md#entereditmode-layerid/).

## [generateData()](#generatedata)

Returns an SVG string with the markups created so far. The SVG string can be reloaded using [loadMarkups()](Extensions-MarkupsCore.md#loadmarkups-markupstring-layerid/).

Markups should have been added while in [enterEditMode()](Extensions-MarkupsCore.md#entereditmode-layerid/).

### Returns

| type | description |
| --- | --- |
| string | Returns an SVG element with all of the created markups in a string format. |

## [changeEditMode(editMode)](#changeeditmode-editmode)

Changes the active drawing tool. For example, from the Arrow drawing tool to the Rectangle drawing tool. Only applicable while in [Edit Mode](Extensions-MarkupsCore.md#entereditmode-layerid/).

Supported values are:

- `new Autodesk.Viewing.Extensions.Markups.Core.EditModeArrow(MarkupsCoreInstance)`
- `new Autodesk.Viewing.Extensions.Markups.Core.EditModeRectangle(MarkupsCoreInstance)`
- `new Autodesk.Viewing.Extensions.Markups.Core.EditModeCircle(MarkupsCoreInstance)`
- `new Autodesk.Viewing.Extensions.Markups.Core.EditModeCloud(MarkupsCoreInstance)`
- `new Autodesk.Viewing.Extensions.Markups.Core.EditModeText(MarkupsCoreInstance)`
- `new Autodesk.Viewing.Extensions.Markups.Core.EditModeFreehand(MarkupsCoreInstance)`
- `new Autodesk.Viewing.Extensions.Markups.Core.EditModePolyline(MarkupsCoreInstance)`
- `new Autodesk.Viewing.Extensions.Markups.Core.EditModePolycloud(MarkupsCoreInstance)`

This function fires event `Autodesk.Viewing.Extensions.MarkupsCore.EVENT_EDITMODE_CHANGED`.

### Parameters

| editMode*   object | Object instance for the drawing tool |
| --- | --- |

* Required

## [isNavigationAllowed()](#isnavigationallowed)

Check whether a user can perform camera navigation operations on the current loaded model. While the extension is active, the user can still draw markups. Panning and zooming are only supported for orthographic cameras.

### Returns

| type | description |
| --- | --- |
| boolean | Whether [allowNavigation()](Extensions-MarkupsCore.md#allownavigation-allow/) can succeed. |

## [allowNavigation(allow)](#allownavigation-allow)

Enables click, tap, and swipe behavior to allow camera zoom and panning operations. It is only available in [Edit mode](Extensions-MarkupsCore.md#entereditmode-layerid/).

### Parameters

| allow*   boolean | Whether camera navigation interactions are active or not. |
| --- | --- |

* Required

## [disableMarkupInteractions(disable)](#disablemarkupinteractions-disable)

Sets mouse interactions and mobile device gestures with markups. Only applicable in [Edit mode](Extensions-MarkupsCore.md#entereditmode-layerid/).

### Parameters

| disable*   boolean | true to disable interactions with markups; false to enable interactions with markups; default false. |
| --- | --- |

* Required

## [copy()](#copy)

Standard copy operation. Applies to any selected markup.
See also [cut()](Extensions-MarkupsCore.md#cut-1/) and [paste()](Extensions-MarkupsCore.md#paste-2/).

## [cut()](#id19)

Standard cut operation. Applies to any selected markup, which gets removed from the screen at call time.
See also [copy()](Extensions-MarkupsCore.md#copy/) and [paste()](Extensions-MarkupsCore.md#paste-2/).

## [paste()](#id22)

Standard paste operation. This function will paste any previously copied or cut markup. Can be called repeatedly after a single copy or cut operation.
See also [copy()](Extensions-MarkupsCore.md#copy/) and [cut()](Extensions-MarkupsCore.md#cut-1/).

## [undo()](#undo)

Will undo the previous operation.
The Undo/Redo stacks will track any change done to the existing markups.
See also [redo()](Extensions-MarkupsCore.md#redo-1/) and [isUndoStackEmpty()](Extensions-MarkupsCore.md#isUndoStackEmpty/).

## [redo()](#id25)

Will redo any previously undo operation.
See also [undo()](Extensions-MarkupsCore.md#undo/), [isRedoStackEmpty()](Extensions-MarkupsCore.md#isRedoStackEmpty/).

## [isUndoStackEmpty()](#id27)

Returns true when [undo()](Extensions-MarkupsCore.md#undo/) produces no changes.

### Returns

| type | description |
| --- | --- |
| boolean | true if there are no changes to undo; false if there are changes to undo. |

## [isRedoStackEmpty()](#id30)

Returns true when [redo()](Extensions-MarkupsCore.md#redo-1/) produces no changes.

### Returns

| type | description |
| --- | --- |
| boolean | true if there are no changes to redo; false if there are changes to redo. |

## [getId()](#getid)

Helper function for generating unique markup ids.

### Returns

| type | description |
| --- | --- |
| number |  |

## [getMarkup(id)](#getmarkup-id)

Returns a markup with the specified ID. Returns null when not found. The ID can be retrieved from the return value of getSelection().
See also [getSelection()](Extensions-MarkupsCore.md#getselection-1/).

### Parameters

| id*   string | Markup identifier. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Autodesk.Viewing.Extensions.Markups.Core.Markup | Returns markup object. |

## [selectMarkup(markup)](#selectmarkup-markup)

Selects or deselects a markup. A selected markup gets an overlayed UI that allows you to perform transformations such as resizing, rotations, and translations. To deselect a markup, send a null value.
See also [getMarkup()](Extensions-MarkupsCore.md#getmarkup-id/).

### Parameters

| markup*   Autodesk.Viewing.Extensions.Markups.Core.Markup, null | The markup instance to select. Set the value to null to deselect a markup. |
| --- | --- |

* Required

## [getSelection()](#id37)

Returns the currently selected markup. A selected markup has a custom UI overlayed that allows you to perform resizing, rotations and translations.
See also [selectMarkup()](Extensions-MarkupsCore.md#selectmarkup-markup/).

### Returns

| type | description |
| --- | --- |
| Autodesk.Viewing.Extensions.Markups.Core.Markup, null | Returns selected markup object; null if no markup is selected. |

## [deleteMarkup(markup, dontAddToHistory)](#deletemarkup-markup-dontaddtohistory)

Deletes a markup from the canvas. Only applies while in [Edit mode](Extensions-MarkupsCore.md#entereditmode-layerid/).

### Parameters

| markup*   Autodesk.Viewing.Extensions.Markups.Core.Markup | Markup object. |
| --- | --- |
| dontAddToHistory   boolean | Whether delete action can be [undone](Extensions-MarkupsCore.md#undo/). |

* Required

## [loadMarkups(markupString, layerId)](#loadmarkups-markupstring-layerid)

Loads data (SVG string) for all markups in a specified layer (layerId) to the Viewerâs canvas.

See also [unloadMarkups()](Extensions-MarkupsCore.md#unloadmarkups-layerid/), and [hideMarkups()](Extensions-MarkupsCore.md#hidemarkups-layerid/).

### Parameters

| markupString*   string | SVG string with markups. See also [generateData()](Extensions-MarkupsCore.md#generatedata/). |
| --- | --- |
| layerId*   string | Identifier for the layer where the markup should be loaded to. Example âLayer1â. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | Whether the markup string was able to be loaded successfully |

## [revertLayer(layerId)](#revertlayer-layerid)

Revert any changes made to the specific layer.

See also [loadMarkups()](Extensions-MarkupsCore.md#loadmarkups-markupstring-layerid/) and [enterEditMode()](Extensions-MarkupsCore.md#entereditmode-layerid/).

### Parameters

| layerId*   string | ID of the layer to revert any changes that were made to it. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the layer was unloaded, false if the layer was not unloaded. |

## [unloadMarkups(layerId)](#unloadmarkups-layerid)

Removes markups from the DOM (Document Object Model). This is helpful for freeing up memory.

See also [loadMarkups()](Extensions-MarkupsCore.md#loadmarkups-markupstring-layerid/), [unloadMarkupsAllLayers()](Extensions-MarkupsCore.md#unloadmarkupsalllayers-1/), [clear()](Extensions-MarkupsCore.md#clear/), [hide()](Extensions-MarkupsCore.md#hide-1/), and [hideMarkups()](Extensions-MarkupsCore.md#hidemarkups-layerid/).

### Parameters

| layerId*   string | ID of the layer containing all markups to unload (from the DOM). |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | Whether the operation succeeded or not. |

## [unloadMarkupsAllLayers()](#id54)

Removes all markups loaded so far. Great for freeing up memory.

See also [loadMarkups()](Extensions-MarkupsCore.md#loadmarkups-markupstring-layerid/), [unloadMarkups()](Extensions-MarkupsCore.md#unloadmarkups-layerid/), [clear()](Extensions-MarkupsCore.md#clear/), [hide()](Extensions-MarkupsCore.md#hide-1/), and [hideMarkups()](Extensions-MarkupsCore.md#hidemarkups-layerid/).

## [hideMarkups(layerId)](#hidemarkups-layerid)

Hides all markups in a specified layer. Note that hidden markups will not be unloaded. Use the [showMarkups()](Extensions-MarkupsCore.md#showmarkups-layerid/) method to make them visible again; no additional parsing is required.

See also [showMarkups()](Extensions-MarkupsCore.md#showmarkups-layerid/), [unloadMarkups()](Extensions-MarkupsCore.md#unloadmarkups-layerid/), and [loadMarkups()](Extensions-MarkupsCore.md#loadmarkups-markupstring-layerid/).

### Parameters

| layerId*   string | ID of the layer containing all markups that should be hidden (in the DOM). |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | Whether the operation succeeded or not. |

## [showMarkups(layerId)](#showmarkups-layerid)

Unhides a layer of hidden markups ([hideMarkups()](#fixMe/)).

### Parameters

| layerId*   string | ID of the layer containing all markups to unload (from the DOM). |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | Whether the operation succeeded or not. |

# Events

## [EVENT_EDITMODE_CHANGED](#event-editmode-changed)

Fired whenever the drawing tool changes. For example, when the Arrow drawing tool changes into the Rectangle drawing tool.

## [EVENT_EDITMODE_ENTER](#event-editmode-enter)

Fired when Edit mode has been enabled, which allows the end user to start drawing markups over the Viewer canvas.

## [EVENT_EDITMODE_LEAVE](#event-editmode-leave)

Fired when Edit mode has been disabled, preventing the end user from drawing markups over the Viewer canvas.

## [EVENT_MARKUP_SELECTED](#event-markup-selected)

Fired when a drawn markup has been selected by the end user with a click command.

### Properties

| markup   Markup | The selected markup |
| --- | --- |

## [EVENT_MARKUP_DRAGGING](#event-markup-dragging)

Fired when a drawn markup is being dragged over the Viewer canvas.

## [EVENT_HISTORY_CHANGED](#event-history-changed)

Fired whenever a new undo or redo action is available.

### Properties

| data   [EventHistoryChangedData](globals-TypeDefs-EventHistoryChangedData.md) | The event data to identify the action and target |
| --- | --- |

## [EVENT_EDITMODE_CREATION_BEGIN](#event-editmode-creation-begin)

Fired when a markup creation begins. For example, as soon as the user starts dragging with the mouse to draw an arrow on the screen.

## [EVENT_EDITMODE_CREATION_END](#event-editmode-creation-end)

Fired when a markup has been created. For example, as soon as the user stops dragging and releases the mouse button to finish drawing an arrow on the screen

## [EVENT_MARKUP_DESELECT](#event-markup-deselect)

Fired when a markup is no longer selected.

### Properties

| markupId   number | The id of the selected markup |
| --- | --- |

## [EVENT_EDITFRAME_EDITION_START](#event-editframe-edition-start)

The selected markup is being modified, i.e, resizing, rotating, moving around

## [EVENT_EDITFRAME_EDITION_END](#event-editframe-edition-end)

The selected markup is no longer being modified
