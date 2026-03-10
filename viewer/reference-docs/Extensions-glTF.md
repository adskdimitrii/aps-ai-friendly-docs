# glTF

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/glTF/

---

Autodesk.Viewing.Extensions

# glTF

Extension description

The glTF extension lets you view glTF 2.0 models in the Viewer. This extension lets you have efficient glTF 2.0 models in your application.

The extension id is: ‘Autodesk.glTF’

## [new glTF(viewer, options)](#new-gltf-viewer-options)

Autodesk.glTFExtension constructor

### Parameters

Expand all

| viewer*   [Autodesk.Viewing.Viewer3D](Viewing-Viewer3D.md) | Viewer instance. |
| --- | --- |
| options   Object | Options for the glTFExtension |
| someOption   boolean | This is how options should be documented |

* Required

### Examples

```
 // Use this viewer option to load the glTF extension
 var options = {
 env: 'AutodeskProduction',
 api: 'derivativeV2',
 documentId: 'tests/unittest/models/gltf/duck.gltf'
}

```

---

# Methods

## [activate(mode)](#activate-mode)

Override the activate method to enable the functionality of the extension.

### Parameters

| mode | An optional mode that indicates a different way the extension can function. |
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
