# ExplodeExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/ExplodeExtension/

---

Autodesk.Viewing.Extensions

# ExplodeExtension

Use its `activate()` method to enable the explode UI.

The extension id is: `Autodesk.Explode`

## [new ExplodeExtension(viewer, options)](#new-explodeextension-viewer-options)

### Parameters

| viewer*   [Viewer3D](/en/docs/viewer/v7/reference/Viewing/Viewer3D/) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

### Examples

```
viewer.loadExtension('Autodesk.Explode')

```

---

# Methods

## [load()](#load)

Initializes and registers the ExplodeTool.

## [unload()](#unload)

Deactivate the extension, deregister the ExplodeTool, and remove the UI from the toolbar.

## [onToolbarCreated(toolbar)](#ontoolbarcreated-toolbar)

Invoked by the viewer when the toolbar UI is available.

### Parameters

| toolbar*   [Autodesk.Viewing.UI.ToolBar](/en/docs/viewer/v7/reference/UI/ToolBar/) | toolbar instance. |
| --- | --- |

* Required

## [activate()](#activate)

Activates the tool and UI.

## [deactivate()](#deactivate)

Hides the explode UI and deactivates the ExplodeTool (resets the explode scale).

## [isActive()](#isactive)

### Returns

| type | description |
| --- | --- |
| boolean | true if the ExplodeTool is active. |

## [getScale()](#getscale)

### Returns

| type | description |
| --- | --- |
| number | Between 0 and 1. |

## [setScale(value)](#setscale-value)

Sets scale of the explode and applies an explode operation.

### Parameters

| value*   number | Between 0 and 1. |
| --- | --- |

* Required

## [getMagnitude()](#getmagnitude)

### Returns

| type | description |
| --- | --- |
| number | 0 - +inf. |

## [setMagnitude(value)](#setmagnitude-value)

Sets magnitude of the explode and applies an explode operation.

### Parameters

| value*   number | 0 - +inf. |
| --- | --- |

* Required

## [getDepthDampening()](#getdepthdampening)

### Returns

| type | description |
| --- | --- |
| number | 1 - +inf. |

## [setDepthDampening(value)](#setdepthdampening-value)

Sets depth dampening of the explode and applies an explode operation.

### Parameters

| value*   number | 0 - +inf. |
| --- | --- |

* Required

## [setStrategy(strategy)](#setstrategy-strategy)

Specifies the algorithm used for exploding models.

### Parameters

| strategy*   string | Either âhierarchyâ or âradialâ. |
| --- | --- |

* Required

## [getStrategy()](#getstrategy)

Returns an identifier for the algorithm used for exploding models.

### Returns

| type | description |
| --- | --- |
| string |  |

## [setUIEnabled(enable)](#setuienabled-enable)

Enable / Disable the explode button & slider. Doesnât affect the state of the explode scale itself.

### Parameters

| enable*   boolean | enable / disable the UI. |
| --- | --- |

* Required
