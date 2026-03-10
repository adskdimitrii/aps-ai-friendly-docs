# FusionOrbitExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/FusionOrbitExtension/

---

Autodesk.Viewing.Extensions

# FusionOrbitExtension

## [new FusionOrbitExtension(viewer, options)](#new-fusionorbitextension-viewer-options)

Provides a customization to the orbit tool.

The extension id is: `Autodesk.Viewing.FusionOrbit`

### Parameters

| viewer*   [Viewer3D](Viewing-Viewer3D.md) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

### Examples

```
viewer.loadExtension('Autodesk.Viewing.FusionOrbit')

```

---

# Methods

## [activate(mode)](#activate-mode)

Activates the extension’s tool.

### Parameters

| mode   string | Either ‘fusionorbit’ (default) or ‘fusionfreeorbit’. |
| --- | --- |

## [deactivate()](#deactivate)

Deactivates the extension’s tool.
