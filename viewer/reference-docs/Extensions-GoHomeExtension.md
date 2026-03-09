# GoHomeExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/GoHomeExtension/

---

Autodesk.Viewing.Extensions

# GoHomeExtension

## [new GoHomeExtension(viewer, options)](#new-gohomeextension-viewer-options)

Use its `activate()` method to animate the camera back to its default, home view. The extension doesnât provide any UI.

The extension id is: `Autodesk.GoHome`

### Parameters

| viewer*   [Viewer3D](Viewing-Viewer3D.md) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

### Examples

```
viewer.loadExtension('Autodesk.GoHome')

```

---

# Methods

## [activate()](#activate)

Animates the camera back to its home location.

## [activate()](#id1)

It doesnât do anything.
