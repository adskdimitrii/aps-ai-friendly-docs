# ToolInterface

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/ToolInterface/

---

Autodesk.Viewing

# ToolInterface

## [new ToolInterface()](#new-toolinterface)

Base class for new interaction tools.

Can also be used simply as a template for creating a new tool.

# Methods

## [getNames()](#getnames)

This method should return an array containing the names of all tools implemented by this class. Often this would be a single name but it is possible to support multiple interactions with a single tool. When this tool is registered with the ToolController each name gets registered as an available tool.

### Returns

| type | description |
| --- | --- |
| Array | Array of strings. Should not be empty. |

## [getName()](#getname)

This is an optional convenience method to obtain the first name of this tool.

### Returns

| type | description |
| --- | --- |
| string | The tools default name. |

## [getPriority()](#getpriority)

This method should return the priority of the tool inside the tool stack. A tool with higher priority will get events first.

### Returns

| type | description |
| --- | --- |
| number | The toolâs priority. |

## [register()](#register)

This method is called by [Autodesk.Viewing.ToolController#registerTool](Viewing-ToolController.md#registerTool/). Use this for initialization.

## [deregister()](#deregister)

This method is called by [Autodesk.Viewing.ToolController#deregisterTool](Viewing-ToolController.md#deregisterTool/). Use this to clean up your tool.

## [activate(name, viewerApi)](#activate-name-viewerapi)

The activate method is called by the ToolController when it adds this tool to the list of those to receive event handling calls. Once activated, a toolâs âhandle*â methods may be called if no other higher priority tool handles the given event. Each active toolâs âupdateâ method also gets called once during each redraw loop.

### Parameters

| name*   string | The name under which the tool has been activated. |
| --- | --- |
| viewerApi*   [Autodesk.Viewing.Viewer3D](Viewing-Viewer3D.md) | Viewer instance. |

* Required

## [deactivate(name)](#deactivate-name)

The deactivate method is called by the ToolController when it removes this tool from the list of those to receive event handling calls. Once deactivated, a toolâs âhandle*â methods and âupdateâ method will no longer be called.

### Parameters

| name*   string | The name under which the tool has been deactivated. |
| --- | --- |

* Required

## [update(highResTimestamp)](#update-highrestimestamp)

The update method is called by the ToolController once per frame and provides each tool with the oportunity to make modifications to the scene or the view.

### Parameters

| highResTimestamp*   number | The process timestamp passed to requestAnimationFrame by the web browser. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | A state value indicating whether the tool has modified the view or the scene and a full refresh is required. |

## [handleSingleClick(event, button)](#handlesingleclick-event-button)

This method is called when a single mouse button click occurs.

### Parameters

| event*   MouseEvent | The event object that triggered this call. |
| --- | --- |
| button*   number | The button number that was clicked (0, 1, 2 for Left, Middle, Right respectively). Note that the button parameter value may be different that the button value indicated in the event object due to button re-mapping preferences that may be applied. This value should be respected over the value in the event object. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools. |

## [handleDoubleClick(event, button)](#handledoubleclick-event-button)

This method is called when a double mouse button click occurs.

### Parameters

| event*   MouseEvent | The event object that triggered this call. |
| --- | --- |
| button*   number | The button number that was clicked (0, 1, 2 for Left, Middle, Right respectively). Note that the button parameter value may be different that the button value indicated in the event object due to button re-mapping preferences that may be applied. This value should be respected over the value in the event object. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools. |

## [handleSingleTap(event)](#handlesingletap-event)

This method is called when a single tap on a touch device occurs.

### Parameters

| event*   [Event](UI-Control.md#Event/) | The triggering event. For tap events the canvasX, canvasY properties contain the canvas relative device coordinates of the tap and the normalizedX, normalizedY properties contain the tap coordinates in the normalized [-1, 1] range. The event.pointers array will contain either one or two touch events depending on whether the tap used one or two fingers. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools. |

## [handleDoubleTap(event)](#handledoubletap-event)

This method is called when a double tap on a touch device occurs.

### Parameters

| event*   [Event](UI-Control.md#Event/) | The triggering event. For tap events the canvasX, canvasY properties contain the canvas relative device coordinates of the tap and the normalizedX, normalizedY properties contain the tap coordinates in the normalized [-1, 1] range. The event.pointers array will contain either one or two touch events depending on whether the tap used one or two fingers. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools. |

## [handleKeyDown(event, keyCode)](#handlekeydown-event-keycode)

This method is called when a keyboard button is depressed.

### Parameters

| event*   KeyboardEvent | The event object that triggered this call. |
| --- | --- |
| keyCode*   number | The numerical key code identifying the key that was depressed. Note that the keyCode parameter value may be different that the value indicated in the event object due to key re-mapping preferences that may be applied. This value should be respected over the value in the event object. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools. |

## [handleKeyUp(event, keyCode)](#handlekeyup-event-keycode)

This method is called when a keyboard button is released.

### Parameters

| event*   KeyboardEvent | The event object that triggered this call. |
| --- | --- |
| keyCode*   number | The numerical key code identifying the key that was released. Note that the keyCode parameter value may be different that the value indicated in the event object due to key re-mapping preferences that may be applied. This value should be respected over the value in the event object. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools. |

## [handleWheelInput(delta)](#handlewheelinput-delta)

This method is called when a mouse wheel event occurs.

### Parameters

| delta*   number | A numerical value indicating the amount of wheel motion applied. Note that this value may be modified from the orignal event values so as to provide consistent results across browser families. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools. |

## [handleButtonDown(event, button)](#handlebuttondown-event-button)

This method is called when a mouse button is depressed.

### Parameters

| event*   MouseEvent | The event object that triggered this call. |
| --- | --- |
| button*   number | The button number that was depressed (0, 1, 2 for Left, Middle, Right respectively). Note that the button parameter value may be different that the button value indicated in the event object due to button re-mapping preferences that may be applied. This value should be respected over the value in the event object. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools. |

## [handleButtonUp(event, button)](#handlebuttonup-event-button)

This method is called when a mouse button is released.

### Parameters

| event*   MouseEvent | The event object that triggered this call. |
| --- | --- |
| button*   number | The button number that was released (0, 1, 2 for Left, Middle, Right respectively). Note that the button parameter value may be different that the button value indicated in the event object due to button re-mapping preferences that may be applied. This value should be respected over the value in the event object. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools. |

## [handleMouseMove(event)](#handlemousemove-event)

This method is called when a mouse motion event occurs.

### Parameters

| event*   MouseEvent | The event object that triggered this call. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools. |

## [handleGesture(event)](#handlegesture-event)

This method is called when a touch gesture event occurs.

### Parameters

| event*   [Event](UI-Control.md#Event/) | The event object that triggered this call. The event.type attribute will indicate the gesture event type. This will be one of: dragstart, dragmove, dragend, panstart, panmove, panend, pinchstart, pinchmove, pinchend, rotatestart, rotatemove, rotateend, drag3start, drag3move, drag3end. The event.canvas[XY] attributes will contain the coresponding touch position. The event.scale and event.rotation attributes contain pinch scaling and two finger rotation quantities respectively. The deltaX and deltaY attributes will contain drag offsets. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools. |

## [handleBlur(event)](#handleblur-event)

This method is called when the canvas area loses focus.

### Parameters

| event*   FocusEvent | The event object that triggered this call. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools. |

## [handleResize()](#handleresize)

This method is called on every active tool whenever the screen area changes. The new canvas area can be obtained from the Navigation interface via the getScreenViewport method.
