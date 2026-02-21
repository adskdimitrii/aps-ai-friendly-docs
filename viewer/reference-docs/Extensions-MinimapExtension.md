# MinimapExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/MinimapExtension/

---

Autodesk.Viewing.Extensions

# MinimapExtension

Provides a 2d Minimap to show the view of the current document.

The extension id is: `Autodesk.BIM360.Minimap`

## [new MinimapExtension()](#new-minimapextension)

### Examples

```
viewer.loadExtension('Autodesk.BIM360.Minimap')

```

---

# Methods

## [load()](#load)

Load the minimap extension.

### Returns

| type | description |
| --- | --- |
| boolean | True if minimap extension is loaded successfully. |

## [unload()](#unload)

Unload the minimap extension.

### Returns

| type | description |
| --- | --- |
| boolean | True if minimap extension is unloaded successfully. |

## [onCameraChange(withTransition)](#oncamerachange-withtransition)

Occurs when camera changes

### Parameters

| withTransition*   boolean | True if cameara changed with a transition. |
| --- | --- |

* Required

## [destroyUI()](#destroyui)

Destroys minimapâs UI
