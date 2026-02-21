# HyperlinkExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/HyperlinkExtension/

---

Autodesk.Viewing.Extensions

# HyperlinkExtension

## [new HyperlinkExtension(viewer, options)](#new-hyperlinkextension-viewer-options)

Enhances 2D models by adding in-canvas tooltips that on click will navigate the user to another 2D or 3D model.

The extension id is: `Autodesk.Hyperlink`

### Parameters

| viewer*   [Viewer3D](/en/docs/viewer/v7/reference/Viewing/Viewer3D/) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

### Examples

```
viewer.loadExtension('Autodesk.Hyperlink')

```

---

# Methods

## [load()](#load)

Registers the hyperlink tool that will intercept pointer events to provide hyperlinks next to specific nodes in the model.

## [unload()](#unload)

Unregisters the hyperlink tool.
