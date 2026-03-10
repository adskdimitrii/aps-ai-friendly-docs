# Customizing Your Edit2D Instance

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/advanced_options/edit2d-customize/

---

# Customizing Your Edit2D Instance

Edit2D defines several defaults when you run it. In the [Setting Up Edit2D](advanced_options-edit2d-setup.md) tutorial, you looked at an application that runs some of those defaults, including Edit2D’s default toolset and context. There are several ways to customize Edit2D behavior. This tutorial covers some of them.

This tutorial shows you ho to:

- Customize units
- Customize your toolset
- Customize context menu
- Add more layers
- Customize the appearance of selection and hover

Before completing this tutorial, you should be familiar with how to set up and use Edit2D in your application. Refer to the [Setting Up Edit2D](advanced_options-edit2d-setup.md) tutorial to familiarize yourself with these concepts. Tutorials about how to use Edit2D and how to manually draw Edit2D shapes with JavaScript are linked at the end of this tutorial.

## [Step 1: Customize Units](#step-1-customize-units)

By default, Edit2D’s unit handling is configured the same way as the `Measure` extension in Viewer SDK. If the `Measure` extension is not available, values are displayed 1:1 in layer coordinates without units.

Edit2D sets the default formatting for label text using `DefaultUnitHandler`. `Default Unit Handler` defines how to translate measurements in layers to the text displayed in labels. This includes:
- The name of the unit
- The way in which lengths and areas in layer-coords are translated to displayed values
- The number of digits displayed in labels.

You can define your own formatting by replacing the default unit handler. Note that you need to set `unitHandler` before specifying the tools.

```
const unitHandler = new Autodesk.Edit2D.SimpleUnitHandler(viewer);
unitHandler.layerUnit    = 'in';
unitHandler.displayUnits = 'cm';
unitHandler.digits       = 4;

// Register your tools after defining unitHandler

```

## [Step 2: Customize Your Toolset](#step-2-customize-your-toolset)

In the previous tutorial, we set up Edit2D with the default toolset, using the `registerDefaultTools()` method. This method completes a few steps for you in order to quickly set up Edit2D:

- Creates a single layer and gizmoLayer
- Creates all available tools
- Registers tools at ToolController

It is usually sufficient to use the default toolset, as long as you can be sure that you are the only one who is using Edit2D within your application. However, Edit2D can also be used by different software components within the same application. This may happen, for example, if Edit2D is used in another Viewer extension. In this case, it would produce conflicts if different components are all accessing the same tools and EditLayer.

You can avoid conflicts by registering your own toolset. First, you’ll want to register your tool, giving your toolset a name unique for your application.

```
edit2d.registerTools(MyToolSetName);

```

Once you’ve registered your tools, you need to define your toolset, context, and tools.

```
const toolSet = edit2d.getToolSet(MyToolSetName);
const context = toolSet.context;
const tools   = toolSet.tools;

```

## [Step 3: Customize Context Menu](#step-3-customize-context-menu)

When you load Edit2D’s default toolset, it automatically registers a context menu with features such `addVertex` and `removeVertex`. You can add application-specific items by registering a `contextMenuCallback`. You need to register the callback after updating the Edit2D context menu. This is because the Edit2D context menu replaces Viewer SDK’s default context menu when your user hits an an Edit2D shape.

```
const myItem = {
    title: 'My extra menu item',
    target : ()=> {console.log('Hello new item);}
};

const cb = (menu) => {
    menu.push(item);
}

//Let Viewer SDK trigger the callback when building the contextMenu
viewer.registerContextMenuCallback('MyOwnItems', cb);

```

Show More

You can also remove the Edit2D contextMenu altogether.

```
const toolset = edit2d.getToolSet(MyToolSetName);
toolset.contextMenu.unregister();

```

## [Step 4: Customize Appearance of Selection and Hover](#step-4-customize-appearance-of-selection-and-hover)

By default, displayed shape styles are slightly varied when users hover over or select them. For example, when a user selects a shape, the shape will display an increased line width and fill opacity. These responses do not alter the actual styles of the shapes you are editing. Instead, Edit2D uses style modifiers. A style modifier is a callback that temporarily overrides the display style of a shape with another one.

In the following example, we will replace the default style modification behavior with custom highlighting that affects all shapes that pass the filter function `(shapeId) => bool`.

```
// Switch-off default highlighting behavior
const selection = edit2d.defaultContext.selection;
layer.removeStyleModifier(selection.modifier);

// Define custom style modifier instead
const myModifier = (shape, style) => {

    // Leave style unaffected if shape does not pass the filter
    if (!myFilter(shape.id)) {
        return undefined;
    }

    // Return modified style copy
    const modified = style.clone();
    modified.fillColor = 'rgb(255, 0, 0)';
    return modified;
};

layer.addStyleModifier(myModifier);

```

Show More

A custom highlighting can, but does not have to, replace the default one. A layer supports multiple style modifiers that are applied in the order in which they were added.

Note: The style parameter may either be the original polygon style or the style returned by a previously applied style modifier. Make sure to create a modified copy, rather than change the style itself.

## [Step 5: Add More Layers](#step-5-add-more-layers)

When you register your tools, Edit2D creates a single `EditLayer` for your tools to work on–`context.layer`– and a second one for temporary overlays–`context.gizmoLayer`. You can add additional layers to the default setup.

```
// Create new layer
const anotherLayer = new Autodesk.Edit2d.EditLayer(viewer);

```

Once you’ve created the layer, you can choose how to display it. By default, additional layers are represented as overlays.

```
this.viewer.impl.addOverlay(OverlayName, layer.scene)

```

More generally, `layer.scene` is a `Three.Scene` with triangulated shapes that you can use in whatever way you want.

## [What’s Next?](#what-s-next)

Now that you’ve learned how to customize Edit2D, check out these tutorials:

- [Using the Edit2D Toolset](advanced_options-edit2d-use.md)
- [Drawing Edit2D Shapes Manually](advanced_options-edit2d-manual.md)
