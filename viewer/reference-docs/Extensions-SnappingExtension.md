# SnappingExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/SnappingExtension/

---

Autodesk.Viewing.Extensions

# SnappingExtension

Utility extension that provides access to the [Autodesk.Viewing.Extensions.Snapping.Snapper](/en/docs/viewer/v7/reference/Snapping/Snapper/) tool.

The extension id is: `Autodesk.Snapping`

## [new SnappingExtension(viewer, options)](#new-snappingextension-viewer-options)

### Parameters

| viewer*   [Viewer3D](/en/docs/viewer/v7/reference/Viewing/Viewer3D/) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

### Examples

```
viewer.loadExtension('Autodesk.Snapping')

```

---

# Methods

## [load()](#load)

Load the extension.

### Returns

| type | description |
| --- | --- |
| Promise | that resolves when dependent extension finishes loading. |

## [unload()](#unload)

Unloads the extension. It does not unload dependent extensions.

### Returns

| type | description |
| --- | --- |
| boolean | Always returns true |

## [activate()](#activate)

Unused method.

### Returns

| type | description |
| --- | --- |
| boolean | Always returns true |

## [deactivate()](#deactivate)

Unused method.

### Returns

| type | description |
| --- | --- |
| boolean | Always returns false |
