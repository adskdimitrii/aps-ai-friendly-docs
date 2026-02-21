# Control

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/UI/Control/

---

Autodesk.Viewing.UI

# Control

## [new Control(id, options)](#new-control-id-options)

Base class for UI controls.

It is abstract and should not be instantiated directly.

### Parameters

Expand all

| id   string | The id for this control. |
| --- | --- |
| options   object | Dictionary with options. |
| collapsible   boolean | Whether this control is collapsible. |

# Properties

| Event   String | Enum for control event IDs. |
| --- | --- |
| container   HTMLElement | The HTMLElement representing this control. |

# Methods

## [getId()](#getid)

Gets this controlâs ID.

### Returns

| type | description |
| --- | --- |
| string | The controlâs ID. |

## [setVisible(visible)](#setvisible-visible)

Sets the visibility of this control.

### Parameters

| visible*   boolean | The visibility value to set. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the controlâs visibility changed. |

## [isVisible()](#isvisible)

Gets the visibility of this control.

### Returns

| type | description |
| --- | --- |
| boolean | True if the this control is visible. |

## [setToolTip(toolTipText)](#settooltip-tooltiptext)

Sets the tooltip text for this control.

### Parameters

| toolTipText*   string | The text for the tooltip. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the tooltip was successfully set. |

## [getToolTip()](#gettooltip)

Returns the tooltip text for this control.

### Returns

| type | description |
| --- | --- |
| string | The tooltip text. Null if itâs not set. |

## [setCollapsed(collapsed)](#setcollapsed-collapsed)

Sets the collapsed state of this control.

### Parameters

| collapsed*   boolean | The collapsed value to set. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the controlâs collapsed state changes. |

## [isCollapsed()](#iscollapsed)

Gets the collapsed state of this control.

### Returns

| type | description |
| --- | --- |
| boolean | True if this control is collapsed. |

## [isCollapsible()](#iscollapsible)

Returns whether or not this control is collapsible.

### Returns

| type | description |
| --- | --- |
| boolean | True if this control can be collapsed. |

## [addClass(cssClass)](#addclass-cssclass)

Adds a CSS class to this control.

### Parameters

| cssClass*   string | The name of the CSS class. |
| --- | --- |

* Required

## [removeClass(cssClass)](#removeclass-cssclass)

Removes a CSS class from this control.

### Parameters

| cssClass*   string | The name of the CSS class. |
| --- | --- |

* Required

## [getPosition()](#getposition)

Returns the position of this control relative to the canvas.

### Returns

| type | description |
| --- | --- |
| object | The `top` and `left` values of the toolbar. |

## [getDimensions()](#getdimensions)

Returns the dimensions of this control.

### Returns

| type | description |
| --- | --- |
| object | The `width` and `height` of the toolbar. |

## [setDisplay(value)](#setdisplay-value)

Sets the CSS `display` style value.

### Parameters

| value*   string | CSS display value |
| --- | --- |

* Required

## [removeFromParent()](#removefromparent)

Removes current control from its parent container.

### Returns

| type | description |
| --- | --- |
| boolean | True if the control was successfully removed. |

# Events

## [VISIBILITY_CHANGED](#visibility-changed)

Event fired when the visibility of the control changes.

### Properties

| controlId   string | The ID of the control that fired this event. |
| --- | --- |
| isVisible   boolean | True if the control is now visible. |

## [COLLAPSED_CHANGED](#collapsed-changed)

Event fired when the collapsed state of the control changes.

### Properties

| controlId   string | The ID of the control that fired this event. |
| --- | --- |
| isCollapsed   boolean | True if the control is now collapsed. |
