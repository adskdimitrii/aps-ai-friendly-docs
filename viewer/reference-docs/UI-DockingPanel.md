# DockingPanel

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/UI/DockingPanel/

---

Autodesk.Viewing.UI

# DockingPanel

## [new DockingPanel(parentContainer, id, title, options)](#new-dockingpanel-parentcontainer-id-title-options)

UI panel that is movable and resizable within the bounds of its parent container.

### Parameters

Expand all

| parentContainer*   HTMLElement | The container for this panel. |
| --- | --- |
| id*   string | The id to assign this panel. |
| title*   string | The title of this panel. |
| options   object | An optional dictionary of options. |
| localizeTitle   boolean | When true, localization is attempted for the given title. |
| addFooter   boolean | When true, adds a footer to the panel with resizing handler. |

* Required

### Examples

```
// Example of a simple DockingPanel that displays the given content.
// The titlebar and move behavior are overridden in initialize(), which also
// creates a custom close button.
//
SimplePanel = function(parentContainer, id, title, content, x, y)
{
    this.content = content;
    Autodesk.Viewing.UI.DockingPanel.call(this, parentContainer, id, '');

    // Auto-fit to the content and don't allow resize.  Position at the coordinates given.
    //
    this.container.style.height = "auto";
    this.container.style.width = "auto";
    this.container.style.resize = "none";
    this.container.style.left = x + "px";
    this.container.style.top = y + "px";
};

SimplePanel.prototype = Object.create(Autodesk.Viewing.UI.DockingPanel.prototype);
SimplePanel.prototype.constructor = SimplePanel;

SimplePanel.prototype.initialize = function()
{
    // Override DockingPanel initialize() to:
    // - create a standard title bar
    // - click anywhere on the panel to move
    // - create a close element at the bottom right
    //
    this.title = this.createTitleBar(this.titleLabel || this.container.id);
    this.container.appendChild(this.title);

    this.container.appendChild(this.content);
    this.initializeMoveHandlers(this.container);

    this.closer = this.getDocument().createElement("div");
    this.closer.className = "simplePanelClose";
    this.closer.textContent = "Close";
    this.initializeCloseHandler(this.closer);
    this.container.appendChild(this.closer);
};

```

Show More

---
