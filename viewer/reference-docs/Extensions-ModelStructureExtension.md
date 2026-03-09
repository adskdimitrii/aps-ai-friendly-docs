# ModelStructureExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/ModelStructureExtension/

---

Autodesk.Viewing.Extensions

# ModelStructureExtension

## [new ModelStructureExtension(viewer, options)](#new-modelstructureextension-viewer-options)

Adds a toolbar button for accessing the Model Browser panel.

Use its `activate()` method to open the Model Browser panel. The Model Browser is only available to 3D models.

The extension id is: `Autodesk.ModelStructure`

[Autodesk.Viewing.GuiViewer3D](Viewing-GuiViewer3D.md) loads this extension by default.

### Parameters

| viewer*   [Viewer3D](Viewing-Viewer3D.md) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

### Examples

```
viewer.loadExtension('Autodesk.ModelStructure')

```

---

# Methods

## [load()](#load)

Invoked automatically when the extension is loaded.

## [unload()](#unload)

Invoked automatically when the extension is unloaded.

## [onToolbarCreated(toolbar)](#ontoolbarcreated-toolbar)

Invoked after the Toolbar UI gets created. Adds toolbar button.

### Parameters

| toolbar*   [Autodesk.Viewing.UI.ToolBar](UI-ToolBar.md) | toolbar instance. |
| --- | --- |

* Required

## [activate()](#activate)

Opens the Model Browser UI.

## [deactivate()](#deactivate)

Closes the Model Browser UI.

## [isActive()](#isactive)

### Returns

| type | description |
| --- | --- |
| boolean | true when the panel is visible. |

## [setModelStructurePanel(modelStructurePanel)](#setmodelstructurepanel-modelstructurepanel)

Sets the panel instance to open when clicking the toolbar button. Use the API to override the default panel with a custom one.

### Parameters

| modelStructurePanel*   [Autodesk.Viewing.UI.ModelStructurePanel](UI-ModelStructurePanel.md) | The model structure panel to use, or null. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the panel, or null, was set successfully; false otherwise. |

## [restoreDefaultPanel()](#restoredefaultpanel)

Removes custom panel and restores the default one.
