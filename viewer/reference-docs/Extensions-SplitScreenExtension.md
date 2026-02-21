# SplitScreenExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/SplitScreenExtension/

---

Autodesk.Viewing.Extensions

# SplitScreenExtension

## [new SplitScreenExtension(viewer, options)](#new-splitscreenextension-viewer-options)

This extension subdivides the LMV canvas into between 2 and 4 (inclusive) separate subcanvases.

The extension id is: `Autodesk.SplitScreen`

For each sub-canvas, you can specify a separate model filter function to control in which canvases each model shall appear. The canvases are numbered as follows: 0 1 2 3

By default (no modelFilter), all models are rendered to each subcanvas. Overlays are rendered into both canvases (unless selection highlighting proxies - which are associated with models)

Limitations: Most core features of LMV keep working (2D/3D render, mouse-over, selection, directional zoom etc.). However, there are currently some known limitations/tradeoffs:

- All canvases must use the same camera. Overcoming this requires to introduce a separate scene graph evaluation too.
- Subcanvas configuration is currently limited to subcanvases with the same aspect ratio. Extending that will (among others) require support for separate cameras.
- ZoomToolExtension, SectionTool, and Measure tool are disabled SplitScreen (we hide the UI)
- GroundShadow is supported, but doesnât apply model filter yet when refreshing the shadow
- GroundReflection in SplitScreen is not supported yet.
- We currently use only a single background for both. This is hardly noticeable for discreet backgrounds like the AEC default or fixed colors, but may disturb when using more detailed environments.

### Parameters

Expand all

| viewer*   [Viewer3D](/en/docs/viewer/v7/reference/Viewing/Viewer3D/) | Viewer instance |
| --- | --- |
| options   object |  |
| viewports   Array.<?Autodesk.Viewing.Extensions.SplitScreenExtension~modelFilterFunction> | Filter functions that returns true for models to be rendered for the viewport at that index. Falsy values render everything. |

* Required

### Examples

```
var options = {

```

viewports: [
function(id) { return id === 1; },
function(id) { return id !== 1; }
]
};
viewer.loadExtension(âAutodesk.SplitScreenâ, options);

---
