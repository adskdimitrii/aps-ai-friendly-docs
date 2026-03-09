# LayerManagerExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/LayerManagerExtension/

---

Autodesk.Viewing.Extensions

# LayerManagerExtension

## [new LayerManagerExtension(viewer, options)](#new-layermanagerextension-viewer-options)

Use its `activate()` method to open the LayersPanel UI. Layers are usually present in 2D models, but some 3D models may support layers as well, for example: AutoCAD.

The extension id is: `Autodesk.LayerManager`

### Parameters

| viewer*   [Viewer3D](Viewing-Viewer3D.md) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

### Examples

```
viewer.loadExtension('Autodesk.LayerManager')

```

---

# Methods

## [activate()](#activate)

Opens the Layers Panel UI.

## [deactivate()](#deactivate)

Closes the Layers Panel UI.

## [isActive()](#isactive)

Checks whether the Layers Panel UI is opened.

### Returns

| type | description |
| --- | --- |
| boolean | true if the Layers Panel UI is currently opened. |
