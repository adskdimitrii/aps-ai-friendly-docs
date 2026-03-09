# Reacting to Events

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/viewer_basics/events/

---

# Reacting to Events

Events are a mechanism to notify 3rd party code about changes in the Viewer.
The Viewer actually listens to its own events in order to update the UI state.
See the [Viewing Namespace](https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/#escape-event) topic of the API Reference for a list of available events.

This topic demonstrates adding listeners for the `Autodesk.Viewing.SELECTION_CHANGED_EVENT` and `Autodesk.Viewing.NAVIGATION_MODE_CHANGED_EVENT`. We will change the HTML content to
display how many elements are currently selected and what navigation tool is currently set.



## [Before You Begin](#before-you-begin)

We recommend the code in this example to be encapsulated in an [extension](viewer_basics-extensions.md).

## [Step 1: Add Selection Counter to HTML](#step-1-add-selection-counter-to-html)

Letâs begin by adding an HTML element that displays how many nodes are currently selected.
Add the HTML block after the Viewerâs `div`.

```
<div class="my-custom-ui">
    <div>Items selected: <span id="MySelectionValue">0</span></div>
<div>

```

Add the following style.

```
<style>
   .my-custom-ui {
        position: absolute;
        top: 0;
        left: 0;
        z-index: 5;
        margin: .3em;
        padding: .3em;
        font-size: 3em;
        font-family: sans-serif;
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 8px;
    }
    .my-custom-ui span {
        color: red;
    }
</style>

```

Show More

The content of `#MySelectionValue` changes whenever `Autodesk.Viewing.SELECTION_CHANGED_EVENT` gets fired.

## [Step 2: Listen and react to an event](#step-2-listen-and-react-to-an-event)

Events are dispatched through the [Viewer3D](../reference-docs/Viewing-Viewer3D.md) instance.
Letâs now add a function to handle selection change events.
We will also call `addEventListener()` on the extensionâs `load()` function and call `removeEventListener()` on the extensionsâs `unload()` function.

```
// Event handler for Autodesk.Viewing.SELECTION_CHANGED_EVENT
EventsTutorial.prototype.onSelectionEvent = function(event) {
    var currSelection = this.viewer.getSelection();
    var domElem = document.getElementById('MySelectionValue');
    domElem.innerText = currSelection.length;
};

EventsTutorial.prototype.load = function() {
    this.onSelectionBinded = this.onSelectionEvent.bind(this);
    this.viewer.addEventListener(Autodesk.Viewing.SELECTION_CHANGED_EVENT, this.onSelectionBinded);
    return true;
};

EventsTutorial.prototype.unload = function() {
    this.viewer.removeEventListener(Autodesk.Viewing.SELECTION_CHANGED_EVENT, this.onSelectionBinded);
    this.onSelectionBinded = null;
    return true;
};

```

Show More

We use `bind()` to keep a reference to `this` within `onSelectionEvent()`.

At this point, every time a node gets selected the counter will change to that number.
Remove the selection by using `ESC` on your keyboard. You select additional nodes by using `Shift-Click` or `Ctrl-Click`.
Notice that you can also toggle the selection with those commands.

## [Step 3: Another event](#step-3-another-event)

The Viewerâs toolbar features buttons that change the current navigation tool. Tools are responsible for converting user input into actions.
The Navigation tools in particular deal with navigating the camera around the scene.



Letâs now listen to `Autodesk.Viewing.NAVIGATION_MODE_CHANGED_EVENT` and display the toolâs name onscreen.
Start by modifying the initially added HTML as follows.

```
<div class="my-custom-ui">
  <div>Items selected: <span id="MySelectionValue">0</span></div>
  <div>Navigation tool: <span id="MyToolValue">Unknown</span></div>
<div>

```

We also need to add the event handler and modify `load()` and `unload()` methods.

```
// New event for handling Autodesk.Viewing.NAVIGATION_MODE_CHANGED_EVENT
// Follows a similar pattern
EventsTutorial.prototype.onNavigationModeEvent = function(event) {
    var domElem = document.getElementById('MyToolValue');
    domElem.innerText = event.id;
};

EventsTutorial.prototype.load = function() {
    this.onSelectionBinded = this.onSelectionEvent.bind(this);
    this.onNavigationModeBinded = this.onNavigationModeEvent.bind(this);
    this.viewer.addEventListener(Autodesk.Viewing.SELECTION_CHANGED_EVENT, this.onSelectionBinded);
    this.viewer.addEventListener(Autodesk.Viewing.NAVIGATION_MODE_CHANGED_EVENT, this.onNavigationModeBinded);
    return true;
};

EventsTutorial.prototype.unload = function() {
    this.viewer.removeEventListener(Autodesk.Viewing.SELECTION_CHANGED_EVENT, this.onSelectionBinded);
    this.viewer.removeEventListener(Autodesk.Viewing.NAVIGATION_MODE_CHANGED_EVENT, this.onNavigationModeBinded);
    this.onSelectionBinded = null;
    this.onNavigationModeBinded = null;
    return true;
};

```

Show More

Notice that for this new event, we are actually consuming the `id` property and assigning it as the `innerText`.
Most of the events dispatched have associated data with them. The same data can be pulled from the `Viewer` instance as well.
The same `id` value can be fetched from the viewer by calling `this.viewer.getActiveNavigationTool()`.

```
// Alternative handler for Autodesk.Viewing.NAVIGATION_MODE_CHANGED_EVENT
EventsTutorial.prototype.onNavigationModeEvent = function(event) {
    var domElem = document.getElementById('MyToolValue');
    domElem.innerText = this.viewer.getActiveNavigationTool(); // same value as event.id
};

```

Now that the event is hooked, try clicking through the navigation buttons in the Viewerâs toolbar. Youâll find that the
event handler will pick up the tool change event!
