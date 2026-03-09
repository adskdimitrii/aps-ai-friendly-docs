# PropertiesManagerExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/PropertiesManagerExtension/

---

Autodesk.Viewing.Extensions

# PropertiesManagerExtension

## [new PropertiesManagerExtension(viewer, options)](#new-propertiesmanagerextension-viewer-options)

Use its `activate()` method to open the Properties UI.

The extension id is: `Autodesk.PropertiesManager`

### Parameters

| viewer*   [Viewer3D](Viewing-Viewer3D.md) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

### Examples

```
viewer.loadExtension('Autodesk.PropertiesManager')

```

---

# Methods

## [load()](#load)

Invoked when the extension gets loaded.

### Returns

| type | description |
| --- | --- |
| boolean | true when the extension loaded successfully. |

## [unload()](#unload)

Invoked when the extension gets unloaded.

## [activate()](#activate)

Opens the Properties UI.

## [deactivate()](#deactivate)

Closes the Properties UI.

## [isActive()](#isactive)

### Returns

| type | description |
| --- | --- |
| boolean | true is the properties panel is open. |

## [setPanel(propertyPanel)](#setpanel-propertypanel)

Overrides the property panel instance.

### Parameters

| propertyPanel* |  |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the panel or null was set successfully, and false otherwise. |

## [setDefaultPanel()](#setdefaultpanel)

Resets the panel to its default instance.

## [getPanel()](#getpanel)

Gets the property panel instance.

### Returns

| type | description |
| --- | --- |
| object | The panel instance. |
