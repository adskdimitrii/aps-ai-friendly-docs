# ComboButton

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/UI/ComboButton/

---

Autodesk.Viewing.UI

# ComboButton
> Extends [`Autodesk.Viewing.UI.Button`_](#id33)

## [new ComboButton(id, options)](#new-combobutton-id-options)

ComboButton with submenu that can be added to toolbars.

### Parameters

| id   string | The id for this comboButton. Optional. |
| --- | --- |
| options   object | An optional dictionary of options. |

# Methods

## [addControl(button)](#addcontrol-button)

Adds a new control to the combo fly-out.

### Parameters

| button*   [Autodesk.Viewing.UI.Button](UI-Button.md) |  |
| --- | --- |

* Required

## [removeControl(button)](#removecontrol-button)

Removes a control from the combo fly-out.

### Parameters

| button*   [Autodesk.Viewing.UI.Button](UI-Button.md) |  |
| --- | --- |

* Required

## [setState(state)](#setstate-state)

Sets the state of this combo button.

### Parameters

| state*   [Autodesk.Viewing.UI.Button.State](UI-Button.md#State/) | The state. |
| --- | --- |

* Required

## [saveAsDefault()](#saveasdefault)

Copies tooltip (if any), icon and click handler into an internal attribute. Can be restored through [#restoreDefault](#restoreDefault/).

## [restoreDefault()](#id5)

Restores visual settings previously stored through [#saveAsDefault](#saveAsDefault/).

## [setIcon(iconClass)](#seticon-iconclass)

Sets the icon for the button.

### Parameters

| iconClass*   string | The CSS class defining the appearance of the button icon (e.g. image background). |
| --- | --- |

* Required

## [getState()](#getstate)

Returns the state of this button.

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.UI.Button.State](UI-Button.md#State/) | The state of the button. |

## [onClick(event)](#onclick-event)

Override this method to be notified when the user clicks on the button.

### Parameters

| event*   MouseEvent |  |
| --- | --- |

* Required

## [onMouseOver(event)](#onmouseover-event)

Override this method to be notified when the mouse enters the button.

### Parameters

| event*   MouseEvent |  |
| --- | --- |

* Required

## [onMouseOut(event)](#onmouseout-event)

Override this method to be notified when the mouse leaves the button.

### Parameters

| event*   MouseEvent |  |
| --- | --- |

* Required

## [getId()](#getid)

Gets this control’s ID.

### Returns

| type | description |
| --- | --- |
| string | The control’s ID. |

## [setVisible(visible)](#setvisible-visible)

Sets the visibility of this control.

### Parameters

| visible*   boolean | The visibility value to set. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the control’s visibility changed. |

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
| string | The tooltip text. Null if it’s not set. |

## [setCollapsed(collapsed)](#setcollapsed-collapsed)

Sets the collapsed state of this control.

### Parameters

| collapsed*   boolean | The collapsed value to set. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the control’s collapsed state changes. |

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

## [STATE_CHANGED](#state-changed)

Event fired when state of the button changes.

### Properties

| buttonId   string | The ID of the button that fired this event. |
| --- | --- |
| state   [Autodesk.Viewing.UI.Button.State](UI-Button.md#State/) | The new state of the button. |

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
