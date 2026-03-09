# ViewerSettingsExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/ViewerSettingsExtension/

---

Autodesk.Viewing.Extensions

# ViewerSettingsExtension

## [new ViewerSettingsExtension(viewer, options)](#new-viewersettingsextension-viewer-options)

Use its `activate()` method to open the Settings UI.

The extension id is: `Autodesk.ViewerSettings`

### Parameters

| viewer*   [Viewer3D](Viewing-Viewer3D.md) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

### Examples

```
viewer.loadExtension('Autodesk.ViewerSettings')

```

---

# Methods

## [activate()](#activate)

Opens the Settings UI.

## [deactivate()](#deactivate)

Closes the Settings UI.
