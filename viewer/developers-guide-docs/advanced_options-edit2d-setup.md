# Setting up Edit2D in Your Application

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/advanced_options/edit2d-setup/

---

# Setting up Edit2D in Your Application

The Edit2D extension provides tools for displaying and editing 2D shapes in Viewer SDK. This tutorial demonstrates how the Edit2D extension works. Tutorials that demonstrate how to use Edit2D, customize Edit2D, and how to manually draw Edit2D shapes with JavaScript are linked at the end of this tutorial.

This tutorial covers:

- How to load the Edit2D extension
- How to connect your app with Edit2D

## [Step 1: Load the Extension](#step-1-load-the-extension)

To start using Edit2D, you first need to load the extension. In this example, we will register Edit2Dâs default toolset. You can learn how to create your own toolset, along with other customizations, in the [Customizing Edit2D](advanced_options-edit2d-customize.md) tutorial.

```
// Load Edit2D extension
const options = {
    // If true, PolygonTool creates Paths instead of just Polygons. This lets you change segments to arcs.
    enableArcs: true
};

const edit2d = await viewer.loadExtension('Autodesk.Edit2D');

// Register all standard tools in default configuration
edit2d.registerDefaultTools();

```

Show More

## [Step 2: Connect Your App with Edit2D](#step-2-connect-your-app-with-edit2d)

After youâve loaded the extension, make sure that the Edit2D toolset responds to your Viewer SDK application. Do this by setting up the Edit2D Context and configuring event handling.

### 2.1 Set Edit2D Context

Registering the default tools sets up an `Edit2DContext` that contains an edit layer, tools, and everything the tools need to work.

```
// Code follows example above

const ctx = edit2d.defaultContext;

// {EditLayer} Edit layer containing your shapes
ctx.layer

// {EditLayer} An additional layer used by tools to display temporary shapes (e.g. dashed lines for snapping etc.)
ctx.gizmoLayer

// {UndoStack} Manages all modifications and tracks undo/redo history
ctx.undoStack

// {Selection} Controls selection and hovering highlight
ctx.selection

// {Edit2DSnapper} Edit2D snapper
ctx.snapper

```

Show More

### 2.2 Configure Event Handling

Most Edit2D classes support the Viewer SDK EventListener interface. There are a few different ways you can connect your application UI and data model with Edit2D. This step shows two examples:

- Synchronizing your data model
- Synchronizing selection

**Synchronizing your data model**

Within your application, shapes may have an application-specific meaning unknown to Edit2D. This means that when you modify the layer with Edit2D tools or undo/redo, your application-specific data model remains unchanged. To keep your data model in sync with changes made to the layer, you can register an event listener with `UndoStack`. Doing this allows you to be notified consistently, regardless of whether a modification is caused by a tool, Undo, or Redo. Add one of the following lines to your code to notify you before or after the action is taken.

```
// Before action
ctx.undoStack.addEventListener(Autodesk.Edit2D.UndoStack.BEFORE_ACTION, beforeAction);

// After action
ctx.undoStack.addEventListener(Autodesk.Edit2D.UndoStack.BEFORE_ACTION, afterAction);

```

**Synchronizing selection**

You can also synchronize selection with Edit2D for certain items in your UI using `edit2d.context.selection`.

One way to do this is to register a handler. The handler ensures the application is notified if selection changes.

In the following example, weâve set the handler to listen for mouse clicks.

```
// Register your handler
ctx.selection.addEventListener(Autodesk.Edit2D.Selection.Events.SELECTION_CHANGED, onSelectionChanged);

```

Similarly, you can set the handler to synchronize mouse hovering:

```
// Update UI state on hover changes
ctx.selection.addEventListener(Autodesk.Edit2D.Selection.Events.SELECTION_HOVER_CHANGED, onHoverChanged);

```

By default, selection and mouse-over highlighting are automatically controlled by Edit2D tools. However, you can also modify selection and hover-highlighting from your application by accessing ctx.selection directly:

```
// Apply your selection from UI
ctx.selection.selectOnly(myItem.shape);

// Sync Edit2D state on UI-hover events
ctx.selection.setHoverID(shape.id);

```

## [Whatâs Next?](#what-s-next)

Now that youâve set up Edit2D, check out these tutorials:

- [Using the Edit2D Toolset](advanced_options-edit2d-use.md)
- [Drawing Edit2D Shapes Manually](advanced_options-edit2d-manual.md)
- [Customizing Edit2D](advanced_options-edit2d-customize.md)
