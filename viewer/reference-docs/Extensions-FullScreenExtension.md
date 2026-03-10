# FullScreenExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/FullScreenExtension/

---

Autodesk.Viewing.Extensions

# FullScreenExtension

## [new FullScreenExtension(viewer, options)](#new-fullscreenextension-viewer-options)

Use its `activate()` method to enter fullscreen mode. It performs the same action as the toolbar’s fullscreen button.

The extension id is: `Autodesk.FullScreen`

### Parameters

| viewer*   [Viewer3D](Viewing-Viewer3D.md) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

### Examples

```
viewer.loadExtension('Autodesk.FullScreen')

```

---

# Methods

## [activate()](#activate)

Enters fullscreen mode.

## [deactivate()](#deactivate)

Exits fullscreen mode.
