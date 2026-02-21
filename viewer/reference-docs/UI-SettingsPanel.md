# SettingsPanel

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/UI/SettingsPanel/

---

Autodesk.Viewing.UI

# SettingsPanel
> Extends [Autodesk.Viewing.UI.SettingsPanel](/en/docs/viewer/v7/reference/UI/SettingsPanel)

## [new SettingsPanel(parentContainer, id, title, options)](#new-settingspanel-parentcontainer-id-title-options)

UI panel specifically designed for application settings.

The user can add new options to each of the tabs.

### Parameters

Expand all

| parentContainer*   HTMLElement | The container for this panel. |
| --- | --- |
| id*   string | The id to assign this panel. |
| title*   string | The title of this panel. |
| options   object | An optional dictionary of options. |
| width   number | Override panelâs minimum width |
| heightAdjustment   number | Override panelâs extra content height, to account for non-scrolling elements. |

* Required

# Methods

## [setVisible(show)](#setvisible-show)

Sets the new visibility state of this SettingsPanel.

### Parameters

| show*   boolean | The desired visibility state. |
| --- | --- |

* Required

## [addTab(tabId, tabTitle, options)](#addtab-tabid-tabtitle-options)

Adds a new tab to the panel.

### Parameters

| tabId*   string | id for the tab (DOM element will have an extended ID to ensure uniqueness). |
| --- | --- |
| tabTitle*   string |  |
| options   object | optional parameter that allows for additional options for the tab: * tabClassName - class name for the Dom elements* minWidth - min width for the tab* index - index if the tab should be inserted instead of added at the end. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the tab was added to the panel, false otherwise. |

## [removeTab(tabId)](#removetab-tabid)

Removes the given tab from the panel.

### Parameters

| tabId*   string | Tab to remove. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the tab was successfully removed, false otherwise. |

## [hasTab(tabId)](#hastab-tabid)

Returns true if a tab with given id exists.

### Parameters

| tabId*   string | Tab id. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the tab with given id exists, false otherwise. |

## [selectTab(tabId)](#selecttab-tabid)

Makes a given tab visible and hides the other ones.

### Parameters

| tabId*   string | Tab to select. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the tab was selected, false otherwise. |

## [isTabSelected(tabId)](#istabselected-tabid)

Returns true if the given tab is selected (visible).

### Parameters

| tabId*   string | Tab to check. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the tab is selected, false otherwise. |

## [addLabel(tabId, name)](#addlabel-tabid-name)

Adds a label to the panel.

### Parameters

| tabId*   string | Id of the tab that will contain the button. |
| --- | --- |
| name*   string | User facing text. |

* Required

### Returns

| type | description |
| --- | --- |
| object | the label control |

## [addButton(tabId, label)](#addbutton-tabid-label)

Adds a button to the panel.

### Parameters

| tabId*   string | Id of the tab that will contain the button. |
| --- | --- |
| label*   string | User facing text. |

* Required

### Returns

| type | description |
| --- | --- |
| string | ID of a new control. |

## [addCheckbox(tabId, caption, initialState, onchange, description, options)](#addcheckbox-tabid-caption-initialstate-onchange-description-options)

Creates a checkbox control and adds it to a given tab.

### Parameters

| tabId*   string | Tab to which to add a new checkbox. |
| --- | --- |
| caption*   string | The text associated with the checkbox. |
| initialState*   boolean | Initial value for the checkbox (checked or not). |
| onchange*   function | Callback that is called when the checkbox is changed. |
| description* |  |
| options*   object, undefined | Additional options: * insertAtIndex - index at which to insert a new checkbox* i18nOptions - additional translation options forwarded to i18n.t |

* Required

### Returns

| type | description |
| --- | --- |
| string | ID of a new control. |

## [addRow(tabId, caption, description, options)](#addrow-tabid-caption-description-options)

Creates a row control and adds it to a given tab. A row only contains a caption and a descriptions

### Parameters

| tabId*   string | Tab to which to add a new row. |
| --- | --- |
| caption*   string | The text associated with the row. |
| description*   string | Description |
| options*   object, undefined | Additional options: * insertAtIndex - index at which to insert a new row |

* Required

### Returns

| type | description |
| --- | --- |
| string | ID of a new control. |

## [addSlider(tabId, caption, min, max, initialValue, onchange, options)](#addslider-tabid-caption-min-max-initialvalue-onchange-options)

Creates a slider control and adds it to a given tab.

### Parameters

| tabId*   string | Tab to which to add a new slider. |
| --- | --- |
| caption*   string | The text associated with the slider |
| min*   number | Min value of the slider. |
| max*   number | Max value of the slider. |
| initialValue*   number | Initial value for the slider. |
| onchange*   function | Callback that is called when the slider value is changed. |
| options*   object, undefined | Additional options: * insertAtIndex - index at which to insert a new slider |

* Required

### Returns

| type | description |
| --- | --- |
| string | ID of a new control. |

## [addSliderV2(tabId, caption, description, min, max, initialValue, onchange, options)](#addsliderv2-tabid-caption-description-min-max-initialvalue-onchange-options)

Creates a row control and a slider control and adds it to a given tab. The slider does not contain the caption or the stepper.

### Parameters

| tabId*   string | Tab to which to add a new slider. |
| --- | --- |
| caption*   string | The text associated with the slider |
| description*   string | The description for the slider |
| min*   number | Min value of the slider. |
| max*   number | Max value of the slider. |
| initialValue*   number | Initial value for the slider. |
| onchange*   function | Callback that is called when the slider value is changed. |
| options*   object, undefined | Additional options: * insertAtIndex - index at which to insert a new slider |

* Required

### Returns

| type | description |
| --- | --- |
| Array.<string> | an array of control ids |

## [addDropDownMenu(tabId, caption, items, initialItemIndex, onchange, options)](#adddropdownmenu-tabid-caption-items-initialitemindex-onchange-options)

### Parameters

| tabId*   string | Tab to which to add a new slider. |
| --- | --- |
| caption*   string | The text associated with the slider. |
| items*   Array | List of items for the menu. |
| initialItemIndex*   number | Initial choice. |
| onchange*   function | Callback that is called when the menu selection is changed. |
| options*   object, undefined | Additional options: * insertAtIndex - index at which to insert a new drop down menu |

* Required

### Returns

| type | description |
| --- | --- |
| string | ID of a new control. |

## [addControl(tabId, control, options)](#addcontrol-tabid-control-options)

Adds a new control to a given tab.

### Parameters

| tabId*   string | Tab to which to add a new. |
| --- | --- |
| control*   object, HTMLElement | Control to add to the given tab. |
| options*   object, undefined | Additional parameters: * insertAtIndex - index at which to insert a new control* caption - caption for the control |

* Required

### Returns

| type | description |
| --- | --- |
| string | ID of the added control. |

## [removeButton(buttonId)](#removebutton-buttonid)

Removes a given button from the settings panel.

### Parameters

| buttonId*   string, [Autodesk.Viewing.UI.Control](/en/docs/viewer/v7/reference/UI/Control/) | button, or button id, to remove. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the button was removed, false otherwise. |

## [removeCheckbox(checkboxId)](#removecheckbox-checkboxid)

Removes a given checkbox from the settings panel.

### Parameters

| checkboxId*   string, [Autodesk.Viewing.UI.Control](/en/docs/viewer/v7/reference/UI/Control/) | Checkbox to remove. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the checkbox was removed, false otherwise. |

## [removeSlider(sliderId)](#removeslider-sliderid)

Removes a given slider from the settings panel.

### Parameters

| sliderId*   string, [Autodesk.Viewing.UI.Control](/en/docs/viewer/v7/reference/UI/Control/) | Slider control to remove. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the slider control was removed, false otherwise. |

## [removeDropdownMenu(dropdownMenuId)](#removedropdownmenu-dropdownmenuid)

Removes a given dropdown menu from the settings panel.

### Parameters

| dropdownMenuId*   string, [Autodesk.Viewing.UI.Control](/en/docs/viewer/v7/reference/UI/Control/) | Dropdown to remove. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the dropdown was removed, false if the dropdown was not removed. |

## [removeControl(controlId)](#removecontrol-controlid)

Removes a given control from the settings panel.

### Parameters

| controlId*   string, [Autodesk.Viewing.UI.Control](/en/docs/viewer/v7/reference/UI/Control/) | The control ID or control instance to remove. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the control was removed, false if the control was not removed. |

## [getControl(controlId)](#getcontrol-controlid)

Returns a control with a given id.

### Parameters

| controlId*   string | Checkbox id to return. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| object | Control object if found, null otherwise. |

## [getContentSize()](#getcontentsize)

Returns the width and height to be used when resizing the panel to the content.

### Returns

| type | description |
| --- | --- |
| object | `{height: number, width: number}`. |

## [sizeToContent(container)](#sizetocontent-container)

Resizes panel vertically to wrap around the content. It will always leave some room at the bottom to display the toolbar.

### Parameters

| container*   HTMLElement | parent container of settings panel |
| --- | --- |

* Required
