# NavToolsExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/NavToolsExtension/

---

Autodesk.Viewing.Extensions

# NavToolsExtension

## [new NavToolsExtension(viewer, options)](#new-navtoolsextension-viewer-options)

Adds toolbar buttons to Orbit, Pan and Dolly. It also adds camera interaction buttons for Fit to View, Focal Length and Roll

The extension id is: `Autodesk.DefaultTools.NavTools`

### Parameters

| viewer*   [Viewer3D](Viewing-Viewer3D.md) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

### Examples

```
viewer.loadExtension('Autodesk.DefaultTools.NavTools')

```

---

# Methods

## [activate(mode)](#activate-mode)

Performs the corresponding button action.

### Parameters

| mode*   string | one of the supported modes, see getModes(). |
| --- | --- |

* Required

## [deactivate()](#deactivate)

Deactivates the current mode and activates the default viewerâs navigation tool.

### Returns

| type | description |
| --- | --- |
| boolean | true when deactivation is successful. |

## [isActive(mode)](#isactive-mode)

Checks whether a specific supported mode is currently active.

### Parameters

| mode*   string | one of the supported modes. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true is the mode queried is currently active. |
