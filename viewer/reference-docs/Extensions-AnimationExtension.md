# AnimationExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/AnimationExtension/

---

Autodesk.Viewing.Extensions

# AnimationExtension

## [new AnimationExtension(viewer, options)](#new-animationextension-viewer-options)

AnimationExtension adds a toolbar with buttons (play/pause/forward/backward/goto start/end) and timeline scrubber to control animation playback. The extension provides api methods that will be reflected by the animation toolbar.

The extension id is: `Autodesk.Fusion360.Animation`

### Parameters

| viewer*   [Viewer3D](Viewing-Viewer3D.md) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

### Examples

```
// When ANIMATION_READY_EVENT is fired, object tree has been created and animation data has been processed
viewer.addEventListener(Autodesk.Viewing.ANIMATION_READY_EVENT, function () {
  const animationExt = viewer.getExtension('Autodesk.Fusion360.Animation');
  animationExt.play();
});

```

---

# Methods

## [load()](#load)

Adds a toolbar button and hooks animation listeners.

## [unload()](#unload)

Removes toobar button and unhooks animation listeners.

## [play()](#play)

Plays the animation. Invoke pause() to stop the animation.

## [pause()](#pause)

Pauses an active animation. Can resume by invoking play()

## [isPlaying()](#isplaying)

Whether the animation is currently playing. Always returns the opposite of isPaused()

### Returns

| type | description |
| --- | --- |
| boolean |  |

## [isPaused()](#ispaused)

Whether the animation is currently paused. Always returns the opposite of isPlaying()

### Returns

| type | description |
| --- | --- |
| boolean |  |

## [rewind()](#rewind)

Rewinds and pauses the animation.

## [setTimelineValue(scale)](#settimelinevalue-scale)

Sets the animation at the very beginning (0), at the end(1) or anywhere in between. For example, use value 0.5 to set the animation half way through it’s completion. Will pause a playing animation.

### Parameters

| scale*   number | value between 0 and 1 |
| --- | --- |

* Required

## [prevKeyframe()](#prevkeyframe)

Sets animation onto the previous keyframe. Will pause the animation if playing.

## [nextKeyframe()](#nextkeyframe)

Sets animation onto the next keyframe. Will pause the animation if playing.

## [getDuration()](#getduration)

Returns how many seconds does the animation take to complete.

### Returns

| type | description |
| --- | --- |
| number |  |

## [getDurationLabel()](#getdurationlabel)

Returns duration as a formatted String h:mm:ss (hours:minutes:seconds)

### Returns

| type | description |
| --- | --- |
| string |  |

## [getCurrentTime()](#getcurrenttime)

Returns the elapsed time (in seconds) of the animation.

### Returns

| type | description |
| --- | --- |
| number |  |

## [getCurrentTimeLabel()](#getcurrenttimelabel)

Returns the current animation time as a formatted String h:mm:ss (hours:minutes:seconds)

### Returns

| type | description |
| --- | --- |
| string |  |

## [setFollowCamera(followCam)](#setfollowcamera-followcam)

Whether a playing animation updates the camera position.

### Parameters

| followCam*   boolean | true to allow animation to update camera position (default behavior). |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the operation was successful. |

## [isFollowingCamera()](#isfollowingcamera)

### Returns

| type | description |
| --- | --- |
| boolean | Whether animations will update the camera’s position (true) or not (false) |

## [setSpeedModifier(value)](#setspeedmodifier-value)

Changes the speed at which the animation is played. Use value 1 to run the animation at default speed, use value 2 to run it at double the speed, use value 0.5 to run it at half the speed.

### Parameters

| value*   number | A multiplier for the animation’s elapsed time. |
| --- | --- |

* Required

## [getSpeedModifier()](#getspeedmodifier)

### Returns

| type | description |
| --- | --- |
| number | The playback speed multiplier. |

## [setLooping(loop)](#setlooping-loop)

Sets whether the animation rewinds and plays as soon as the animation finishes playing.

### Parameters

| loop*   boolean | true to have the animation loop continuously. |
| --- | --- |

* Required

## [isLooping()](#islooping)

### Returns

| type | description |
| --- | --- |
| boolean | Whether the animation will loop continuously. |

## [onToolbarCreated(toolbar)](#ontoolbarcreated-toolbar)

Invoked by the viewer when the toolbar UI is available.

### Parameters

| toolbar*   [Autodesk.Viewing.UI.ToolBar](UI-ToolBar.md) | toolbar instance. |
| --- | --- |

* Required

## [openPanel()](#openpanel)

Opens a panel with options to configure the animation extension.

## [activate()](#activate)

Plays the animation.

## [deactivate()](#deactivate)

Pauses the animation.

## [isActive()](#isactive)

### Returns

| type | description |
| --- | --- |
| boolean | true when the animation is playing. |
