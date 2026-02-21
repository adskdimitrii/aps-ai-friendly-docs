# FusionOrbitExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/FusionOrbitExtension/

---

Autodesk.Viewing.Extensions

# FusionOrbitExtension

## [new FusionOrbitExtension(viewer, options)](#new-fusionorbitextension-viewer-options)

Provides a customization to the orbit tool.

The extension id is: `Autodesk.Viewing.FusionOrbit`

### Parameters

| viewer*   [Viewer3D](/en/docs/viewer/v7/reference/Viewing/Viewer3D/) | Viewer instance |
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

Activates the extensionâs tool.

### Parameters

| mode   string | Either âfusionorbitâ (default) or âfusionfreeorbitâ. |
| --- | --- |

## [deactivate()](#deactivate)

Deactivates the extensionâs tool.
