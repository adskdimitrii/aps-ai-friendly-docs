# Extension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/Extension/

---

Autodesk.Viewing

# Extension

## [new Extension(viewer, options)](#new-extension-viewer-options)

Base class for extending the functionality of the viewer.

Derive from this class and implement methods `load()` and `unload()`.

Register this extension by calling: [``](#id1)Autodesk.Viewing.theExtensionManager.registerExtension(âyour_extension_idâ, YOUR_EXTENSION_CLASS); ``

Extensions are registered and loaded automatically by adding the Extension ID to the config object passed to the viewer constructor.

### Parameters

| viewer*   [Autodesk.Viewing.Viewer3D](Viewing-Viewer3D.md) | The viewer to be extended. |
| --- | --- |
| options*   object | An optional dictionary of options for this extension. |

* Required

# Methods

## [load()](#load)

Override the load method to add functionality to the viewer. Use the Viewerâs APIs to add/modify/replace/delete UI, register event listeners, etc.

### Returns

| type | description |
| --- | --- |
| boolean, Promise | True if the load was successful. Optionally, the function can return a Promise which resolves when load succeeds and rejects in case of failure. |

## [unload()](#unload)

Override the unload method to perform some cleanup of operations that were done in load.

### Returns

| type | description |
| --- | --- |
| boolean | True if the unload was successful. |

## [activate(mode)](#activate-mode)

Override the activate method to enable the functionality of the extension.

### Parameters

| mode   string | An optional mode that indicates a different way the extension can function. |
| --- | --- |

### Returns

| type | description |
| --- | --- |
| boolean | True if the extension activation was successful. |

## [deactivate()](#deactivate)

Override the deactivate method to disable the functionality of the extension.

### Returns

| type | description |
| --- | --- |
| boolean | True if the extension deactivation was successful. |

## [setActive(enable, mode)](#setactive-enable-mode)

Activates the extension if the enable parameter is set to true. Deactivates the extension if the enable parameter is set to true.

### Parameters

| enable*   boolean | flag to activate or deactivate the extension. |
| --- | --- |
| mode   string | An optional mode that indicates a different way the extension can function. |

* Required

## [getName()](#getname)

Gets the name of the extension.

### Returns

| type | description |
| --- | --- |
| string | Returns the name of the extension. |

## [getModes()](#getmodes)

Gets an array of modes available for the extension.

### Returns

| type | description |
| --- | --- |
| Array | Returns an array of modes. |

## [isActive(mode)](#isactive-mode)

Check if the extension is active and optionally check if the specified mode is active for that extension.

### Parameters

| mode* | An optional mode that indicates a different way the extension can function. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | Default - True if the extension is active. When optional argument mode is specified, returns true if both extension and the mode are active, false otherwise. |

## [getState(viewerState)](#getstate-viewerstate)

Gets the extension state as a plain object. Intended to be called when viewer state is requested.

### Parameters

| viewerState*   object | Object to inject extension values. |
| --- | --- |

* Required

## [restoreState(viewerState, immediate)](#restorestate-viewerstate-immediate)

Restores the extension state from a given object.

### Parameters

| viewerState*   object | Viewer state. |
| --- | --- |
| immediate*   boolean | Whether the new view is applied with (true) or without transition (false). |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if restore operation was successful. |

## [extendLocalization(locales)](#extendlocalization-locales)

Add localization strings to the viewer. This method can override localization keys already loaded. There is no API method to remove localization strings added with this method.

### Parameters

| locales*   object | The set of localized strings keyed by language |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if localization was successfully updated |

### Examples

```
var locales = {
      en: { my_tooltip: "CUSTOM_TOOLTIP" },
      de: { my_tooltip: "BENUTZERDEFINIERTE_TOOLTIP" }
 };
 ext.extendLocalization(locales);

```

---

## [getCache()](#getcache)

Returns an object that persists throughout an extensionâs unload->load operation sequence. Cache object is kept by the [Autodesk.Viewing.Viewer3D](Viewing-Viewer3D.md) instance. Cache object lives only in RAM, there is no localStorage persistence.

### Returns

| type | description |
| --- | --- |
| object | The cache object for a given extension. |

## [onToolbarCreated(toolbar)](#ontoolbarcreated-toolbar)

Invoked after the Toolbar UI gets created. Extensions can extend (or remove) its content from this point forward. The method is invoked after [TOOLBAR_CREATED_EVENT](https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/#TOOLBAR_CREATED_EVENT/) gets fired. It is also invoked right after [Autodesk.Viewing.Extension#load](Viewing-Extension.md#load/) if the toolbar was already created.

Must be overriden by subclasses.

### Parameters

| toolbar*   [Autodesk.Viewing.UI.ToolBar](UI-ToolBar.md) | toolbar instance. |
| --- | --- |

* Required
