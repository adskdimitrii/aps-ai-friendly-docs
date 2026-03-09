# Customizing the Toolbar

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/viewer_basics/toolbar-button/

---

# Customizing the Toolbar

Customizing a toolbar is best explained by looking at an example.

This example creates a custom toolbar with two buttons on the Viewer canvas.
Each button has its own tooltip and reacts to click events.
Clicking one button displays the environment background, while clicking the other hides it.

![../../../../_images/custom_toolbar.jpg](../../../../_images/custom_toolbar.jpg)

## [Before You Begin](#before-you-begin)

The customization logic is is implemented as an [extension](viewer_basics-extensions.md).

```
function ToolbarExtension(viewer, options) {
  Autodesk.Viewing.Extension.call(this, viewer, options);
}

ToolbarExtension.prototype = Object.create(Autodesk.Viewing.Extension.prototype);
ToolbarExtension.prototype.constructor = ToolbarExtension;

ToolbarExtension.prototype.load = function() {
  // Set background environment to "Infinity Pool"
  // and make sure the environment background texture is visible
  this.viewer.setLightPreset(6);
  this.viewer.setEnvMapBackground(true);

  // Ensure the model is centered
  this.viewer.fitToView();

  return true;
};

ToolbarExtension.prototype.unload = function() {
  // nothing yet
};

Autodesk.Viewing.theExtensionManager.registerExtension('ToolbarExtension', ToolbarExtension);

```

Show More

## [Step 1: Detect the Toolbar](#step-1-detect-the-toolbar)

In the custom extension, override base class method `onToolbarCreated`. The Viewer will invoke this method as soon as the toolbar is available to the extension.

```
ToolbarExtension.prototype.onToolbarCreated = function(toolbar) {

  alert('TODO: customize Viewer toolbar');
};

```

## [Step 2: Add Buttons](#step-2-add-buttons)

To create a sub-toolbar and add a couple of buttons:

```
ToolbarExtension.prototype.onToolbarCreated = function(toolbar) {
  // alert('TODO: customize Viewer toolbar');

  var viewer = this.viewer;

  // Button 1
  var button1 = new Autodesk.Viewing.UI.Button('show-env-bg-button');
  button1.onClick = function(e) {
      viewer.setEnvMapBackground(true);
  };
  button1.addClass('show-env-bg-button');
  button1.setToolTip('Show Environment');

  // Button 2
  var button2 = new Autodesk.Viewing.UI.Button('hide-env-bg-button');
  button2.onClick = function(e) {
      viewer.setEnvMapBackground(false);
  };
  button2.addClass('hide-env-bg-button');
  button2.setToolTip('Hide Environment');

  // SubToolbar
  this.subToolbar = new Autodesk.Viewing.UI.ControlGroup('my-custom-toolbar');
  this.subToolbar.addControl(button1);
  this.subToolbar.addControl(button2);

  toolbar.addControl(this.subToolbar);
};

```

Show More

Notice that the code above calls method `addClass()`, which adds a CSS class to
control the appearance of the custom buttons.

For this example, weâll add the style definitions in the HTML file:

```
<style>
  .show-env-bg-button {
    background: red;
  }
  .hide-env-bg-button {
    background: blue;
  }
</style>

```

Show More

When you refresh the HTML page the buttons display. Hovering over them displays tooltips. Click to trigger their actions.

## [Step 3: Cleanup](#step-3-cleanup)

Extensions should remove any DOM elements and events they add.
In this case, only `this.subToolbar` must be removed.

```
ToolbarExtension.prototype.unload = function() {
  if (this.subToolbar) {
      this.viewer.toolbar.removeControl(this.subToolbar);
      this.subToolbar = null;
  }
};

```

As explained in [Writing an Extension](viewer_basics-extensions.md), you can verify that the extension works as expected by manually
calling the `viewer.loadExtension('ToolbarExtension')` and `viewer.unload('ToolbarExtension')` methods.
