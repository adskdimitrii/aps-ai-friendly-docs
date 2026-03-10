# Writing an Extension

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/viewer_basics/extensions/

---

# Writing an Extension

## [What is an Extension?](#what-is-an-extension)

An extension is JavaScript code that extends or modifies the Viewer’s behavior. You can use extensions to add specialized functionality to the Viewer SDK.

Many extensions are bundled with the Viewer. For a complete list of included extensions, see the API Reference section for [Extensions](https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/). If the functionality you need is not included, you can write your own extensions.

Writing extensions is best explained with an example. The following example creates a Viewer extension named `MyAwesomeExtension`.

There will be two HTML buttons that interact with the added extension. They will be placed below and outside the Viewer canvas.

One of the buttons will be used to lock the camera. Once locked you will not be able to orbit (rotate), pan, or zoom.
The next button will be used to unlock the camera, re-enabling mouse and touch interactions.

## [Step 1: Include extension file](#step-1-include-extension-file)

Extensions must be defined after all core classes for the Viewer have been defined.
This example uses a file named `my-awesome-extension.js` and the following snippet shows how to include it in the HTML.

```
<script src="https://developer.api.autodesk.com/modelderivative/v2/viewers/7.*/viewer3D.min.js"></script>
<script src="my-awesome-extension.js"></script>

```

## [Step 2: Write the extension code](#step-2-write-the-extension-code)

An extension consists of the following interface points:

1. Inherits from `Autodesk.Viewing.Extension`.
2. Defines method `load()` that returns a `boolean`.
3. Defines method `unload()` that also returns a `boolean`.
4. Registers itself with a unique `string id`.

```
// Content for 'my-awesome-extension.js'

function MyAwesomeExtension(viewer, options) {
  Autodesk.Viewing.Extension.call(this, viewer, options);
}

MyAwesomeExtension.prototype = Object.create(Autodesk.Viewing.Extension.prototype);
MyAwesomeExtension.prototype.constructor = MyAwesomeExtension;

MyAwesomeExtension.prototype.load = function() {
  alert('MyAwesomeExtension is loaded!');
  return true;
};

MyAwesomeExtension.prototype.unload = function() {
  alert('MyAwesomeExtension is now unloaded!');
  return true;
};

Autodesk.Viewing.theExtensionManager.registerExtension('MyAwesomeExtension', MyAwesomeExtension);

```

Show More

An extension will successfully get loaded into The Viewer’s lifecycle only if `load()` returns `true`.
Likewise, an extension will get successfully unloaded if `unload()` returns `true`.

Notice that the string `'MyAwesomeExtension'` used in `registerExtension()` doesn’t need to match the
function name declaration.

**Note:** The extension does not get loaded when refreshing the HTML page.

## [Step 3: Load the extension](#step-3-load-the-extension)

To instruct the Viewer instance to load the extension:

```
var config3d = {
  ...
  extensions: ['MyAwesomeExtension'],
  ...
};
var htmlDiv = document.getElementById('forgeViewer')
viewer = new Autodesk.Viewing.GuiViewer3D(htmlDiv, config3d);
viewer.start();
...
viewer.loadModel(...);

```

Show More

Refreshing the HTML page displays the `alert()` message found in the extension’s `load()` method.

## [Step 4: Add HTML buttons](#step-4-add-html-buttons)

Add two simple HTML buttons after the Viewer div:

```
<div id="forgeViewer"></div>
<button id="MyAwesomeLockButton">Lock it!</button>
<button id="MyAwesomeUnlockButton">Unlock it!</button>

```

## [Step 5: Add button handlers](#step-5-add-button-handlers)

To enhance the extension’s `load()` method to handle the HTML buttons’ click events:
Notice our extension has property `this.viewer`, the main access point for most of The Viewer’s features and customizations.

```
MyAwesomeExtension.prototype.load = function() {
  // alert('MyAwesomeExtension is loaded!');

  var viewer = this.viewer;

  var lockBtn = document.getElementById('MyAwesomeLockButton');
  lockBtn.addEventListener('click', function() {
    viewer.setNavigationLock(true);
  });

  var unlockBtn = document.getElementById('MyAwesomeUnlockButton');
  unlockBtn.addEventListener('click', function() {
    viewer.setNavigationLock(false);
  });

  return true;
};

```

Show More

**Note:** The extension property `this.viewer` is the main access point for most of the Viewer’s features and customizations.

Reload the HTML and use the mouse to move the camera around. Then click `Lock it!` and notice how you can
no longer modify the camera with the mouse. You will notice that some UI buttons get hidden as well.

Now click the `Unlock it!` button to enable camera interactions once again.

## [Step 6: Cleanup on unload](#step-6-cleanup-on-unload)

It’s a good practice to remove added event listeners to DOM elements when the extension is unloaded.

To perform all cleanup operations in the unload method:

```
function MyAwesomeExtension(viewer, options) {
  Autodesk.Viewing.Extension.call(this, viewer, options);

  // Preserve "this" reference when methods are invoked by event handlers.
  this.lockViewport = this.lockViewport.bind(this);
  this.unlockViewport = this.unlockViewport.bind(this);
}

MyAwesomeExtension.prototype = Object.create(Autodesk.Viewing.Extension.prototype);
MyAwesomeExtension.prototype.constructor = MyAwesomeExtension;

MyAwesomeExtension.prototype.lockViewport = function() {
  this.viewer.setNavigationLock(true);
};

MyAwesomeExtension.prototype.unlockViewport = function() {
  this.viewer.setNavigationLock(false);
};

MyAwesomeExtension.prototype.load = function() {
  // alert('MyAwesomeExtension is loaded!');

  this._lockBtn = document.getElementById('MyAwesomeLockButton');
  this._lockBtn.addEventListener('click', this.lockViewport);

  this._unlockBtn = document.getElementById('MyAwesomeUnlockButton');
  this._unlockBtn.addEventListener('click', this.unlockViewport);

  return true;
};

 MyAwesomeExtension.prototype.unload = function() {
  // alert('MyAwesomeExtension is now unloaded!');

  if (this._lockBtn) {
    this._lockBtn.removeEventListener('click', this.lockViewport);
    this._lockBtn = null;
  }

  if (this._unlockBtn) {
      this._unlockBtn.removeEventListener('click', this.unlockViewport);
      this._unlockBtn = null;
  }

  return true;
};

```

Show More

## [Step 7: Test the Extension](#step-7-test-the-extension)

To fully test that the extension is working as expected, you can manually force the
extension to be loaded and unloaded.

From the browser’s console type the following to check whether your extension is loaded or not.
At this point, the extension should be loaded and the function call should return `true`:

```
NOP_VIEWER.isExtensionLoaded('MyAwesomeExtension');

```

Note the use of the global variable `NOP_VIEWER`, defined by the Viewer SDK after developers create a Viewer instance.

Now type the following to `unload` the extension:

```
NOP_VIEWER.unloadExtension('MyAwesomeExtension');

```

If all goes as expected, the added buttons should no longer work. Click on them to validate.

You can then load the extension again by calling

```
NOP_VIEWER.loadExtension('MyAwesomeExtension');

```

Now the added buttons will again work as expected.
