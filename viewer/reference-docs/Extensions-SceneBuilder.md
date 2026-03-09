# SceneBuilder

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/SceneBuilder/

---

Autodesk.Viewing.Extensions

# SceneBuilder

Scene Builder extension provides an API for building scenes without loading them from a URL.

The extension id is: `Autodesk.Viewing.SceneBuilder`

## [new SceneBuilder(viewer, options)](#new-scenebuilder-viewer-options)

### Parameters

Expand all

| viewer*   [Autodesk.Viewing.Viewer3D](Viewing-Viewer3D.md) | The viewer instance loading the extension |
| --- | --- |
| options   object | Default options used when calling addNewModel |
| conserveMemory   boolean | Set to true to turn on memory conservation mode. In this mode [addMesh()]`Autodesk.Viewing.Extensions.SceneBuilder#addMesh <#fixMe/>`_ is not available because a single mesh is shared among all of the fragments in the model. |

* Required

### Examples

```
viewer.loadExtension('Autodesk.Viewing.SceneBuilder');

```

---

# Methods

## [load()](#load)

Extension interface method - loads the extension

### Returns

| type | description |
| --- | --- |
| boolean |  |

## [unload()](#unload)

Extension interface method - unloads the extension Method [Autodesk.Viewing.Extensions.SceneBuilder#addNewModel](Extensions-SceneBuilder.md#addNewModel/) will fail if the extension is unloaded.

## [addNewModel(options)](#addnewmodel-options)

Add a new empty model into the scene. The model can be manipulated only by its associated ModelBuilder instance.

### Parameters

Expand all

| options   object | Options combined with the options used when the extension is loaded with loadExtension(). The combined options are put in the loadOptions property in the object returned by model.getData(). |
| --- | --- |
| conserveMemory   boolean | Set to true to turn on memory conservation mode. In this mode [addMesh()]`Autodesk.Viewing.Extensions.SceneBuilder#addMesh <#fixMe/>`_ is not available because a single mesh is shared among all of the fragments in the model. |
| createWireframe   boolean | Set to true to turn on edge generation for geometry. |

### Returns

| type | description |
| --- | --- |
| [Promise (ModelBuilder)](Extensions-ModelBuilder.md) | A Promise that resolves with a ModelBuilder instance for the new model. |
