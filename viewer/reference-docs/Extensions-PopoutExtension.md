# PopoutExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/PopoutExtension/

---

Autodesk.Viewing.Extensions

# PopoutExtension

Extension to popout the viewer into child windows

The extension id is: `Autodesk.Viewing.Popout`

## [new PopoutExtension(viewer, options)](#new-popoutextension-viewer-options)

### Parameters

| viewer*   [Autodesk.Viewing.Viewer3D](/en/docs/viewer/v7/reference/Viewing/Viewer3D/) | Viewer instance. |
| --- | --- |
| options*   object | Not used. |

* Required

### Examples

```
viewer.loadExtension('Autodesk.Viewing.Popout');

```

---

# Methods

## [load()](#load)

Extension interface method - loads the extension

### Returns

| type | description |
| --- | --- |
| boolean |  |

## [unload()](#unload)

Extension interface method - unloads the extension

### Returns

| type | description |
| --- | --- |
| boolean |  |

## [popoutToChild(child, elementid, copyStyles, setupStyleObserver)](#popouttochild-child-elementid-copystyles-setupstyleobserver)

Use this to pop the viewer out to an existing window

### Parameters

| child*   object | Already open window created with window.open() |
| --- | --- |
| elementid*   string | The dom element id in the child where the viewer will be moved to |
| copyStyles   boolean | Flag to copy the styles from the current window to the child. Set this to false if you intend to copy the styles yourself |
| setupStyleObserver   boolean | Style observers clone dynamically added (from extensions loading) into child. This is required for extensions to work. Set this to false if you intend to set up the cloning with mutation observers yourself |

* Required

## [popoutToBlank(options, onBeforeUnload, onClose, onBlocked)](#popouttoblank-options-onbeforeunload-onclose-onblocked)

Use this to pop the viewer out to a new blank window

### Parameters

| options   object | windowFeature options |
| --- | --- |
| onBeforeUnload   function | Called before the popout window is unloaded |
| onClose   function | Called when popout window is closed |
| onBlocked   function | Called when popup blockers block creating child window |

## [popin()](#popin)

Closes the popout window and moves the viewer back to the main window
