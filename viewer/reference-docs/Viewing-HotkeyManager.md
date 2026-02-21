# HotkeyManager

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/HotkeyManager/

---

Autodesk.Viewing

# HotkeyManager

## [new HotkeyManager()](#new-hotkeymanager)

Management of hotkeys for the viewer.

# Methods

## [getNames()](#getnames)

Return name of the tool returned as an array

### Returns

| type | description |
| --- | --- |
| Array.<string> | [âhotkeysâ] |

## [getName()](#getname)

Return name of HotkeyManager tool

### Returns

| type | description |
| --- | --- |
| string | âhotkeysâ |

## [pushHotkeys(id, hotkeys, options)](#pushhotkeys-id-hotkeys-options)

Pushes new hotkeys onto the stack.

### Parameters

Expand all

| id*   string | The id for this hotkey set. |
| --- | --- |
| hotkeys*   Array.<Autodesk.Viewing.HotkeyManager~Hotkey> | The list of hotkeys. |
| options   object | An optional dictionary of options for this hotkey set. |
| tryUntilSuccess   boolean | When true, the onPress callback will be called until it returns true or the hotkey state changes. The onRelease callback will be called until it returns true or until the combination is reengaged. Stops propagation through the stack. Non-blocking. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the hotkeys were successfully pushed. |

## [popHotkeys(id)](#pophotkeys-id)

Removes hotkeys associated with an ID from the stack.

### Parameters

| id*   string | The id associated with the hotkeys. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the hotkeys were successfully popped. |

## [handleKeyDown(event, keyCode)](#handlekeydown-event-keycode)

### Parameters

| event* | Event to handle |
| --- | --- |
| keyCode* | Key code |

* Required

## [handleKeyUp(event, keyCode)](#handlekeyup-event-keycode)

### Parameters

| event* | Event to handle |
| --- | --- |
| keyCode* | Key code |

* Required

## [handleBlur()](#handleblur)

Handle blur by releasing all current keys

## [activate()](#activate)

No-op

## [deactivate()](#deactivate)

No-op
