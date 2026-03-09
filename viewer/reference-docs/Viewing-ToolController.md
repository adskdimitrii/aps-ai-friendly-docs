# ToolController

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/ToolController/

---

Autodesk.Viewing

# ToolController

Core interface to add and remove canvas interactions to the viewer.

## [new ToolController(viewerImpl, viewerApi, autocam, utilities, defaultHandler)](#new-toolcontroller-viewerimpl-viewerapi-autocam-utilities-defaulthandler)

This class is created internally by the Viewer api and is available via the âtoolControllerâ property of the Viewer3D api object. Client implementations should not normally instantiate this class directly.

### Parameters

| viewerImpl*   object | The viewer implementation object. |
| --- | --- |
| viewerApi*   object | The viewer api object. |
| autocam*   object | The Autocam interface object. |
| utilities*   object | The ViewingUtilities object. |
| defaultHandler*   object | The default event handling tool. |

* Required

# Methods

## [registerTool(tool, onStateChanged)](#registertool-tool-onstatechanged)

This method registers an event handling tool with the controller. This makes the tool available for activation and deactivation. Tools are registered under one or more names which must be provided via their âgetNamesâ method. The tools âgetNamesâ method must return an array of one or more names. Typically a tool will only have one name but if it wishes to operate in different modes it can use different names to activate the modes. Registered tools have the properties named âutilitiesâ and âcontrollerâ added to them which refer to the ViewingUtilities object and this controller respectively. Tools may not use the name âdefaultâ which is reserved.

### Parameters

| tool*   object | The tool to be registered. |
| --- | --- |
| onStateChanged*   function | callback to be called when disabling the tool through the modality map |

* Required

## [deregisterTool(tool)](#deregistertool-tool)

This method deregisters an event handling tool with the controller afterwhich it will no longer be available for activation and deactivation. All names that the tool is registered under will be deregistered. If any tool is active at the time of deregistration will first be deactivated and itâs âdeactivateâ method will be called.

### Parameters

| tool*   object | The tool to be deregistered. |
| --- | --- |

* Required

## [getTool(name)](#gettool-name)

This method returns the tool registered under the given name.

### Parameters

| name*   string | The tool name to look up. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| object | The tool registered under the given name or undefined if not found. |

## [getActiveToolName()](#getactivetoolname)

This method returns the name of the topmost tool on the tool stack. If no tools are active the name of the default tool is returned (which is âdefaultâ).

### Returns

| type | description |
| --- | --- |
| string | The tool name to look up. |

## [getActiveTool()](#getactivetool)

This method returns the name of the topmost tool on the tool stack. If no tools are active the name of the default tool is returned (which is âdefaultâ).

### Returns

| type | description |
| --- | --- |
| string | The tool name to look up. |

## [getActiveTools()](#getactivetools)

Return the current tool stack.

### Returns

| type | description |
| --- | --- |
| Array | list of tools in the tool stack |

## [rearrangeByPriorities()](#rearrangebypriorities)

Sorts the toolStack according to the toolsâ priority. Useful when a toolâs priority gets changed after activation.

## [activateToolModality(toolName)](#activatetoolmodality-toolname)

Disables or enables tools in the toolâs modality map

### Parameters

| toolName*   string | Name of the tool |
| --- | --- |

* Required

## [activateTool(toolName)](#activatetool-toolname)

Activates the tool registered under the given name. Activation implies pushing the tool on a stack of âactiveâ tools, each of which (starting from the top of the stack) is given the opportunity to handle incoming events. Tools may âconsumeâ events by returning true from their event handling methods, or they may allow events to be passed down to the next tool on the stack by returning false from the handling methods. Upon activation the tools âactivateâ method is called with the name under which it has been activated. Activation is not allowed while the controller is in a âlockedâ state (see the methods âsetIsLockedâ and âgetIsLockedâ). Tools must be registered prior to activation (see the methods âregisterToolâ and âderegisterToolâ). Each tool has its own priority property (default 0), such that a tool with higher priority will get events first.

### Parameters

| toolName*   string | The name of the tool to be activated. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if activation was successful. |

## [deactivateTool(toolName)](#deactivatetool-toolname)

The first tool found on the active stack with the given name is removed and its âdeactivateâ method is called. Once deactivated the tool will no longer receive events via its handler methods. Deactivation is not allowed while the controller is in a âlockedâ state (see the methods âsetIsLockedâ and âgetIsLockedâ).

### Parameters

| toolName*   string | The name of the tool to be deactivated. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if deactivation was successful. |

## [getToolNames()](#gettoolnames)

Obtain a list of all the currently registered tool names.

### Returns

| type | description |
| --- | --- |
| Array | List of all registered tool names. |

## [setDefaultTool(tool)](#setdefaulttool-tool)

Set the tool which will be requested to handle events if no other active tool handles them.

### Parameters

| tool*   object | The tool to be registered as the default. |
| --- | --- |

* Required

## [getDefaultTool()](#getdefaulttool)

Get the tool which handle events if no other active tool handles them.

### Returns

| type | description |
| --- | --- |
| object | The tool to be registered as the default. |

## [setIsLocked(state)](#setislocked-state)

Set the controller into a locked or unlocked state. While locked, tool activation and deactivation is not allowed. Locking the controller is sometimes necessary to force an interaction to remain active until it is fully completed.

### Parameters

| state*   boolean | The state of the controller lock. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | The previous state of the lock (this may be used to restore the lock to itâs previous state). |

## [getIsLocked()](#getislocked)

Get the current state of the controller lock.

### Returns

| type | description |
| --- | --- |
| boolean | The state of the lock. |

## [handleCmdKeyEvent(cmdEvent, eventType)](#handlecmdkeyevent-cmdevent-eventtype)

Catches a CMD event and generate a Control one instead.

### Parameters

| cmdEvent*   object | Event generated by CMD key |
| --- | --- |
| eventType*   string | Event type |

* Required

## [setMouseWheelInputEnabled(isEnabled)](#setmousewheelinputenabled-isenabled)

Whether mouse scroll wheel (and/or two-finger vertical swipe) will trigger a camera zoom operation.

### Parameters

| isEnabled*   boolean |  |
| --- | --- |

* Required

## [setModalityMap(map)](#setmodalitymap-map)

Set the modality map for each tool. This function will clear any existing modality map. The map object consists of a key which represents the tool name and a value which is an object that represents which tools to enable and disable. To get the tool names @see [Autodesk.Viewing.ToolController#getToolNames](Viewing-ToolController.md#getToolNames/)

### Parameters

| map*   object | Object describing each toolâs modality with other tools. |
| --- | --- |

* Required

### Examples

```
// When enabling the measure tool the explode, bimwalk and section tools will be disabled.
// When enabling the section tool the pan tool will be disabled.
toolController.setModalityMap({
    measure: { explode: false, bimwalk: false, section: false },
    section: { pan: false }
});

```

---

## [getModalityMap()](#getmodalitymap)

Get the modality map.

### Returns

| type | description |
| --- | --- |
| object | returns a copy of the tool modality. |

## [getToolModality(name)](#gettoolmodality-name)

Get a specific toolâs modality map.

### Parameters

| name*   string | tool name |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| object | an object describing the toolâs modality map. |

## [setToolModality(name, map)](#settoolmodality-name-map)

### Parameters

| name*   string | Tool name that is associated with the modality map. |
| --- | --- |
| map*   object | Object containing the name of the tool as the key and a boolean that describes if the tool can be enabled or disabled. |

* Required
