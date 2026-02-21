# ControlGroup

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/UI/ControlGroup/

---

Autodesk.Viewing.UI

# ControlGroup
> Extends [`Autodesk.Viewing.UI.Control`_](#id36)

## [new ControlGroup(id, options)](#new-controlgroup-id-options)

Class for grouping controls.

### Parameters

Expand all

| id   string | The id for this control group. |
| --- | --- |
| options   object | An optional dictionary of options. |
| collapsible   boolean | Whether this control group is collapsible. |

# Methods

## [addControl(control, options)](#addcontrol-control-options)

Adds a control to this control group.

### Parameters

Expand all

| control*   [Autodesk.Viewing.UI.Control](/en/docs/viewer/v7/reference/UI/Control/) | The control to add. |
| --- | --- |
| options   object | An option dictionary of options. |
| index   object | The index to insert the control at. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the control was successfully added. |

## [indexOf(control)](#indexof-control)

Returns the index of a control in this group. -1 if the item isnât found.

### Parameters

| control*   string, [Autodesk.Viewing.UI.Control](/en/docs/viewer/v7/reference/UI/Control/) | The control ID or control instance to find. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| number | Index of a successfully removed control, otherwise -1. |

## [removeControl(control)](#removecontrol-control)

Removes a control from this control group.

### Parameters

| control*   string, [Autodesk.Viewing.UI.Control](/en/docs/viewer/v7/reference/UI/Control/) | The control ID or control instance to remove. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the control was successfully removed. |

## [getControl(controlId)](#getcontrol-controlid)

Returns the control with the corresponding ID if it is in this control group.

### Parameters

| controlId*   string | The ID of the control. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.UI.Control](/en/docs/viewer/v7/reference/UI/Control/) | The control or null if it doesnât exist. |

## [getControlId(index)](#getcontrolid-index)

Returns the control ID with for corresponding index if it is in this control group.

### Parameters

| index*   number | Index of the control. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| string | The ID of the control or null if it doesnât exist. |

## [getNumberOfControls()](#getnumberofcontrols)

Returns the number of controls in this control group.

### Returns

| type | description |
| --- | --- |
| number | The number of controls. |

## [setCollapsed(collapsed)](#setcollapsed-collapsed)

Sets the collapsed state of this control group. Iterates over the child controls and calls child.setCollapsed(collapsed).

### Parameters

| collapsed*   boolean | The collapsed value to set. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if at least one collapsible childâs state changes. |

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

## [CONTROL_ADDED](#control-added)

Event fired a control is added to the control group.

### Properties

| control   string | The control that was added. |
| --- | --- |
| index   number | The index at which the control was added. |

## [CONTROL_REMOVED](#control-removed)

Event fired when a control is removed from the control group.

### Properties

| control   string | The control that was removed. |
| --- | --- |
| index   number | The index at which the control was removed. |

## [SIZE_CHANGED](#size-changed)

Event fired when the size of the control group changes.

### Properties

| childEvent   object | The event that the child fired. |
| --- | --- |

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
