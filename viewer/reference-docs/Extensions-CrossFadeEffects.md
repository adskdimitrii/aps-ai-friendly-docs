# CrossFadeEffects

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/CrossFadeEffects/

---

Autodesk.Viewing.Extensions

# CrossFadeEffects

CrossFadeEffects extension provides API for implementing smooth fading effects in LMV, e.g.

- CrossFading between models or model configurations (e.g. color theming, hiding objects etc.)
- Image-based “ghosting” effect, i.e. showing a semitransparent snapshot of a model on top of another one.

The extension id is: `Autodesk.CrossFadeEffects`

Note:

- Note that CrossFadeEffects require 2 extra RenderTargets. So, they should only be used for optional effects that can be skipped on weak devices.
- CrossFade effects can only be used for one purpose at a time. When using them for a new feature, you have to make sure that they don’t conflict with existing features.

## [new CrossFadeEffects()](#new-crossfadeeffects)

### Examples

```
viewer.loadExtension('Autodesk.CrossFadeEffects')

```

---

# Methods

## [load()](#load)

Enables cross frade effects.

## [unload()](#unload)

Disables cross frade effects.

## [acquireControl(clientId, onClientChanged)](#acquirecontrol-clientid-onclientchanged)

Fading targets may be used by different clients for different purposes. That’s okay as long as it does not happen concurrently.

In case of conflicts, the last caller takes precedence.

If you start an effect using this extension, always call this function to notify client code that was using it before. Vice versa, provide an onClientChanged() callback to handle the case that someone else overtakes.

Example: If start a fading effect while the ghost floors of the LevelsExtension are fading out, the LevelsExtension will be notified to skip the fade-out anim to avoid conflicts.

### Parameters

| clientId*   string | Some identifier unique for the code component using the effect, e.g. the name of an extension. |
| --- | --- |
| onClientChanged   function | Will be called if another client called acquireControl. |

* Required

## [setModelTargetIndex(modelId, targetIndex)](#setmodeltargetindex-modelid-targetindex)

Only allowed if modelCrossFade is enabled. Determines to which target a RenderModel will be rendered.

### Parameters

| modelId*   number | The model id |
| --- | --- |
| targetIndex*   undefined, 0, 1 | index of the crossFade target or undefined (default) to use default color buffer |

* Required

## [setModelTargetIndexForAll(index)](#setmodeltargetindexforall-index)

Only allowed if modelCrossFade is enabled. Determines to which target a RenderModel will be rendered.

### Parameters

| index*   undefined, 0, 1 | index of the crossFade target or undefined (default) to use default color buffer |
| --- | --- |

* Required

## [setCrossFadeOpacity(targetIndex, opacity)](#setcrossfadeopacity-targetindex-opacity)

Only allowed if modelCrossFade is enabled. Assigns a blending opacity to a cross-fading extra target.

### Parameters

| targetIndex*   number | must be >0 |
| --- | --- |
| opacity*   number | in [0,1] |

* Required

## [setCrossFadeEnabled(enable)](#setcrossfadeenabled-enable)

Enable/Disable model cross-fading. Must be enabled in order to render models to different render targets for cross-fading effects (see below). If no cross-fading effects are used, it should be disabled to save GPU memory and performance.

### Parameters

| enable*   boolean | Whether to enable(true) or disable(false) cross fade effects. |
| --- | --- |

* Required

## [fadeTarget(targetIndex, startOpacity, endOpacity, duration, onFinished)](#fadetarget-targetindex-startopacity-endopacity-duration-onfinished)

Runs a fading-animation on a cross-fading target.

### Parameters

| targetIndex*   number | see setModelTargetIndex() |
| --- | --- |
| startOpacity*   number | in [0,1] |
| endOpacity*   number | in [0,1] |
| duration   number | in seconds |
| onFinished   function | optional callback triggered when animation is finished |

* Required

### Returns

| type | description |
| --- | --- |
| object | AnimControl instance |

## [fadeToViewerState(applyState, duration)](#fadetoviewerstate-applystate-duration)

Runs a static image fade between the current view and a modified view. (e.g. with changed model/fragment visiblity, ghosting etc.) The modified view is specified via function applyState.

### Parameters

| applyState*   function | applied after rendering the fading start image. |
| --- | --- |
| duration*   number | in seconds |

* Required
