# Using the Edit2D Toolset

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/advanced_options/edit2d-use/

---

# Using the Edit2D Toolset

Now that you have integrated Edit2D with your application, you can start using Edit2D tools to create shapes.

This tutorial shows you how to:

- Use various Edit2D tools
- Display and change labels
- Use snapping

Some code samples are provided in this tutorial, but most of the content demonstrates how Edit2D works for end users after being loaded in the Viewer SDK app. Google Chrome is required to complete this tutorial.

You should complete the [Setting Up Edit2D](advanced_options-edit2d-setup.md) tutorial before using this tutorial. Additional tutorials, which demonstrate how to customize Edit2D and how to manually draw Edit2D shapes using JavaScript, are linked at the end of this tutorial.

## [Step 1: Run the Edit2D Playground](#step-1-run-the-edit2d-playground)

For this tutorial, you need to set up the Edit2D playground. The Edit2D playground is useful for debugging Edit2D and testing its functionality. To set up the playground, copy this code snippet to your Chrome DevTools snippet collection and run it:

```
// Facilitate access to extension and layer
window.edit2d = NOP_VIEWER.getExtension('Autodesk.Edit2D');
window.layer  = edit2d.defaultContext.layer;
window.tools  = edit2d.defaultTools;

// Convenience function for tool switching per console. E.g. startTool(tools.polygonTool)
var startTool = function(tool) {

    var controller = NOP_VIEWER.toolController;

    // Check if currently active tool is from Edit2D
    var activeTool = controller.getActiveTool();
    var isEdit2D = activeTool && activeTool.getName().startsWith("Edit2");

    // deactivate any previous edit2d tool
    if (isEdit2D) {
        controller.deactivateTool(activeTool.getName());
        activeTool = null;
    }

    // stop editing tools
    if (!tool) {
        return;
    }

    controller.activateTool(tool.getName());
}

```

Show More

Setting up the Edit2D playground gives you quick access to some Edit2D functions. Note that because the functions are mechanisms for testing, they should not be used for production code or environment. Weâve used them in this tutorial to show you how the Edit2D extension works after loading it in your application.

## [Step 2: Use Edit2D Tools to Make Shapes](#step-2-use-edit2d-tools-to-make-shapes)

This step demonstrates how to use the following Edit2D tools:

- PolygonTool
- PolylineTool
- PolygonEditTool
- InsertSymbolTool

These tools become available when you call `registerDefaultTools()`. We did this when we loaded the extension in the [Set Up Edit2D](advanced_options-edit2d-setup.md) tutorial. Weâll load these tools in the console to demonstrate how each one works.

### 2.1 PolygonTool: Drawing Polygons and Rectangles

To start using the PolygonTool, enter the following in your console:

```
startTool(tools.polygonTool);

```

The mouse cursor will change to a cross.



With `PolygonTool` activated, you can:

1. Click to start a new polygon.
2. Click again to add vertices to the polygon.
3. `Backspace` to remove the most recently added vertex.
4. `Esc` to discard the new polygon.
5. Hold `Shift` to disable snapping. Snapping is active by default.
6. Double-click to add the final vertex of the polygon. Keyboard shortcuts for finishing the polygon are `Enter` and the `c` key.

With `PolygonTool`, you can also click and drag to draw a rectangle:

1. Press and hold your mouse to choose a starting point for your rectangle.
2. (Optionally) Hold the `Shift` key to force the rectangle into a square.
3. Drag mouse to determine the length and width of the rectangle.
4. Release the mouse to finish the rectangle.


### 2.2 PolylineTool: Drawing Polylines

To draw polylines, start the [``](#id1)PolylineTool:

```
startTool(tools.polylineTool)

```

`PolylineTool` is similar to `PolygonTool` and allows you to click point-by-point to draw polylines. You can draw simple lines using a single-drag interaction.



### 2.3 PolygonEditTool: Modify Polygons and Paths

To edit a polygon, start `PolygonEditTool`.

```
startTool(tools.polygonEditTool);

```

Shapes in the layer should now respond on mouse-hover with a slightly higher fill opacity. You can now click shapes that you want to edit.

With `PolygonEditTool`, you can do the following:

- **Move a shape** by dragging it.
- **Move vertices** by dragging vertex gizmos.


- Hold `Shift` key to **disable snapping**. Snapping is active by default.
- **Move edges** by dragging edge gizmos. When an edge is moved, neighboring edges get larger or smaller.


- **Create Protrusions** by dragging edges. If the moved edge is on the same line as its neighbor, the system adds an extra corner. This feature can be used to quickly edit protrusions for shapes with right angles.


- **Cancel dragging interaction** by using `Esc` key.
- **Insert new vertex** by right-clicking the edge. This displays the context menu.


- **Remove vertices** by clicking a vertex gizmo and pressing `Backspace`. You can also right-click the vertex gizmo to display the context menu.
- **Copy/Paste** a shape with `Ctrl-C/Ctrl-V`. Pasting multiple times will create multiple duplicates.


- **Change lines to Bezier arcs** by right-clicking an edge and choosing **Change to Arc Segment** in the context menu. As a shortcut, you can select the edge and press `a`.
- **Change arcs back to lines** by using the context menu of an arc segment. As a shortcut, you can select the edge and press `l`.


- **Edit tangents of curve segments** by dragging the tangent gizmos of a selected arc edge.


- **Change segments into ellipse arcs** using the context menu.


- **Edit ellipse arcs** by selecting an edge and dragging the purple gizmo at the center of the arc.


### 2.4 InsertSymbolTool

With `InsertSymbolTool`, you can click to insert shape instances at the mouse position.

```
startTool(tools.insertSymbolTool);

```

The default shape is a circle. You can replace the default by changing the symbol property of the tool. In the following example, weâll change `InsertSymbolTool` so that it creates horizontal lines of length 1 centered at the mouse position:

```
let line = new Autodesk.Edit2D.Polyline().makeLine(-1, -1, 1, 1);
tools.insertSymbolTool.symbol=line;

```

## [Step 3: Display Labels](#step-3-display-labels)

With some basic shapes in place, letâs add meaning to the shapes by creating labels. You can use Labels to display anything you want. For example, we will use a label to display the area and length of a shape.

### 3.1 Labels for Area and Length

`PolygonTool` and `PolygonEditTool` both have options to display area (polygons) and respective length (polylines).

To display the area of a polygon being edited, call the following:

```
tools.polygonTool.setAreaLabelVisible(true);

```



Similarly, you can display the length of new polylines:

```
tools.polygonTool.setLengthLabelVisible(true);

```



You can use the same functions in PolygonEditTools to display the area and length of a shape.

```
tools.polygonEditTool.setAreaLabelVisible(true);
tools.polygonEditTool.setLengthLabelVisible(true);

```

### 3.2 Units for Areas and Lengths

Edit 2D uses the same units and length calibration as the MeasureExtension. You can use MeasureExtensionâs calibration panel to specify units and calibration for your Edit2D shapes.



If you use Edit2D without the MeasureExtension, it will display all coordinates in model units. You can customize units by modifying or replacing `DefaultUnitHandler`. More information is available in the [Customize Edit2D](advanced_options-edit2d-customize.md) tutorial.

### 3.3 Creating Custom Labels

You can also give shapes custom text labels. The following example attaches a custom text label to the first shape in the layer.

```
var poly = layer.shapes[0];
var label = new Autodesk.Edit2D.ShapeLabel(poly, layer);
label.setText('MyLabel');

```

Similarly, you can attach a custom label to the edge of a shape.

```
var poly = layer.shapes[0];
var label = new Autodesk.Edit2D.EdgeLabel(layer);
label.attachToEdge(poly, 0);
label.setText('My Edge Label');

```

If you no longer want a label, you can remove it.

```
label.dtor();

```

### 3.4 Apply Labels to Multiple Shapes

You can easily apply labels to a whole group of shapes using a `ShapeLabelRule`. A `ShapeLabelRule` will define a rule for how to apply labels.

`ShapeLabelRule` has a few default settings. You can configure or replace any of these settings.

- Labels are created when shapes are added, and deleted when shapes are removed.
- Labels are created only for visible shapes larger than 5 pixels.
- Labels smoothly fade out when the shape becomes smaller than 5 pixels.

With `ShapeLabelRule`, you can also define a:

- *Filter*: Determines which shapes should be labeled.
- *Text rule*: Determines the text for each shape.
- *Style rule*: (Optional) Determines how to stylize a label.

A simple example is to create a `ShapeLabelRule` that displays the shape properties. In this example, we will label each shape with its class name.

```
// Label each shape with its className
var classRule = new Autodesk.Edit2D.ShapeLabelRule(layer, shape => shape.constructor.name);

```



## [Step 4: Snapping](#step-4-snapping)

When drawing new shapes or moving vertices, `PolygonTool` and `PolylgonEditTool` support many types of snapping.

- Snapping to a sheet geometry
- Snapping to edit layer geometry
- Snapping to angles
- Snapping to combinations of the previous types.

Snapping is active by default but can be suppressed by holding `Shift`. Geometry snapping and snapping indicators work the same way in Edit2D as with the Measure extension. Snapping to intersections and angles is only supported by Edit2D.

### 4.1 Geometry Snapping

There are two types of geometry snapping:

- **Point-Snap**: Snap to a unique point. This can be a line vertex, a circle midpoint, or a line intersection. Edit2D displays a square to indicate that you are creating a point-snap.


- **Segment-Snap**: Snap to a segment (for example, a line or circular arc). The position is not fully snapped, but constrained to a certain segment. Edit2D shows a crosshair of three lines to indicate that you are creating a segment-snap.


### 4.2 Angle Snapping

When using `PolygonTool` or moving vertices with `PolygonEditTool`, angle snapping is indicated by red dashed lines.



By default, we snap to angles that are multiples of 45Â°. You can change this behavior by changing the table of snapping angles in `AngleSnapper`.

```
edit2d.defaultContext.snapper.angleSnapper.snapAngles

```

Angle snapping always refers to a ânewâ edge that you are currently modifying.

- In `PolygonTool`, this refers to the new edge that you would get when adding the next vertex at the current mouse position.
- In `PolyEditTool`, when moving a vertex, it refers to the edges that start/end at the vertex being moved.

Angle snapping works if the new edge forms a snapping angle with any other edge in the shape. You can also snap to the perpendicular bisector of another edge.



### 4.3 Intersection Snapping

Snapping to an angle or line segment only constrains the snap position to one line segment. If there are multiple lines that a mouse position can snap to, the intersection of the closest two points is chosen.

The following cases are possible:

- Intersection between two geometry segments (each may be sheet geometry or edit layer geometry)
- Intersection between two angle snaplines
- Intersection between an angle snapline and line segment.

The following image shows an example of the third case. The intersection of a perpendicular bisector (angle snap) and a line segment on a sheet (geometry snap).



## [Whatâs Next?](#what-s-next)

To learn more about Edit2D, check out these tutorials:

- [Drawing Edit2D Shapes Manually](advanced_options-edit2d-manual.md)
- [Customizing Edit2D](advanced_options-edit2d-customize.md)
