# BimWalkExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/BimWalkExtension/

---

Autodesk.Viewing.Extensions

# BimWalkExtension

## [new BimWalkExtension(viewer, options)](#new-bimwalkextension-viewer-options)

First Person navigation tool, similar to those found in videogames. Supports keyboard and mouse input.

The extension id is: `Autodesk.BimWalk`

### Parameters

| viewer*   [Viewer3D](Viewing-Viewer3D.md) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

### Examples

```
viewer.loadExtension('Autodesk.BimWalk')

```

---

# Methods

## [activate()](#activate)

Enables the walk tool.

## [deactivate()](#deactivate)

Deactivates the walk tool.
