# Drawing Edit2d Shapes Manually

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/advanced_options/edit2d-manual/

---

# Drawing Edit2d Shapes Manually

With Edit2D loaded in your application, you can begin adding shapes to PDF files and sheets. This tutorial demonstrates how to draw and change shapes using JavaScript, giving you a view into the mechanisms that make up the Edit2D extension. Google Chrome is required to complete this tutorial.

This tutorial covers:
- Drawing polygons and polylines
- Adding and removing shape styles
- Drawing Bezier and ellipse arcs
- Converting your Edit2D shapes to and from SVG

Before you do this tutorial, you should complete the [Setting Up Edit2D](advanced_options-edit2d-setup.md) tutorial. Tutorials for using and customizing Edit2D are linked at the end of this tutorial.

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

Setting up the Edit2D playground gives you quick access to some Edit2D functions. However, because the functions are mechanisms for testing, they should not be used in a production code or environment. They are used in this tutorial to demonstrate how the Edit2D extension works after being loaded in your application.

## [Step 2: Check Sheet Coordinates](#step-2-check-sheet-coordinates)

The following steps contain code snippets that let you draw shapes, lines, and arcs. You need to change the coordinates in these snippets so that the items are within visible range of your sheet. By default, Edit2D uses the same coordinate system as the underlying sheet. To find out the visible area for a sheet, you can check the bounding box of the model:

```
var box = NOP_Viewer.model.getBoundingBox();

```

You can now check x/y values with `box.min` and `box.max`.

## [Step 3: Draw Polygons and Polylines](#step-3-draw-polygons-and-polylines)

Let’s start by drawing a polygon. Enter the following snippet to add a triangle to your sheet. Remember to adjust the coordinates so that the triangle is visible on your PDF or sheet.

```
// Create simple triangle
var poly = new Autodesk.Edit2D.Polygon([
    {x: 53, y: 24},
    {x: 62, y: 24},
    {x: 57, y: 34}
]);

// Show it
layer.addShape(poly);

```

Show More

You can create polylines using similar code:

```
//Create polyline
var polyline = new Autodesk.Edit2D.Polyline([
    {x: 54, y: 30},
    {x: 54, y: 35},
    {x: 62, y: 35},
    {x: 62, y: 30}
]);

// Show it
layer.addShape(polyline);

```

Show More

## [Step 4: Add Shape Styles](#step-4-add-shape-styles)

All Edit2D shapes have a `style` that configures their appearance. Let’s modify the style of the polygon we created.

```
// Configure shape style
var style = poly.style;
style.fillColor = 'rgb(255,0,0)';
style.fillAlpha = 0.3;
style.lineWidth = 1.0;
style.lineStyle = 11;

// show changes
layer.update();

```

Show More

Notice that you must use `layer.update()` to show the changes. This is because an edit layer knows the shape it is showing, but the shape does not know which edit layer is using it. If a shape you are modifying is already displayed, as in this example, you must update the layer.

## [Step 5: Undo Changes](#step-5-undo-changes)

### 5.1 Remove Shapes

You can remove a single shape using `layer.removeShape(poly)` or clear the entire layer using `layer.clear()`.

### 5.2 Use Undo/Redo

For simplicity, we manipulated the layer directly in our examples. If you are using the Edit2D tools in your application, they track the undo/redo history. Mixing this with manual modifications may cause inconsistencies between the undo history and the actual layer state.

To make sure your manual changes are tracked in the undo/redo history, wrap your modifications into an action.

If you are using Edit2D’s default toolset, the `Edit2DContext` provides shortcuts for tracking your manual changes.

```
edit2d.defaultContext.clearLayer();
edit2d.defaultContext.addShape(poly);
edit2d.defaultContext.removeShape(poly);

```

More generally, you can perform an action by calling run on the undoStack. Here is an example for adding multiple shapes in this way:

```
const action = new Actions.AddShapes(this.layer, shapes);
this.undoStack.run(action);

```

## [Step 6: Draw Bezier Arcs](#step-6-draw-bezier-arcs)

Polygons and polylines can contain only straight line segments. To create shapes that are fully or partially smooth, you can use *path* shapes. Path shapes allow you to change straight line segments to Bezier arcs.

This example demonstrates how to create a polypath:

```
// Create simple PolygonPath
var path = new Autodesk.Edit2D.PolygonPath([
    {x: 53, y: 24}, // a
    {x: 62, y: 24}, // b
    {x: 57, y: 34}  // c
]);

// Change segment (a,b) from line to arc
path.setBezierArc(
    0,              // segment index (= index of its start vertex)
    54.72, 20.54,   // control point to define start tangent
    60.53, 20.34    // control point to define end tangent
);

// Show it
layer.addShape(path);

```

Show More

The arc segment is specified by 4 control points P0, P1, P2, P3;

- P0 and P3 define the start and end point. These points are specified in advance by the start and end positions of the edge’s vertex.
- P1 and P2 are points that control the start and end tangents of the arc.

As previously noted, you need `layer.update()` for shapes that are already visible to show the changes from calling `setBezierArc(..)`.

Creating a polyline path is similar to creating a polygon path.

```
// Create simple PolylinePath
var path = new Autodesk.Edit2D.PolylinePath([
    {x: 53, y: 24}, // a
    {x: 62, y: 24}, // b
    {x: 57, y: 34}, // c
    {x: 53, y: 24}, // d = a (repeated to close the triangle)
]);

// Change segment (a,b) from line to arc
path.setBezierArc(0, 54.72, 20.54, 60.53, 20.34);

// Show it
layer.addShape(path);

```

Show More

Notice that the polyline path requires 4 vertices while the polylgon path only needed 3. This is because the closing segment from c to a is added automatically when using the polygon path. To create the same closed shape with a polyline path, you need to repeat *vertex a* at the end. Be aware that the number of valid segment indices for polygons is `vertexCount-1` and `vertexCount-2` for polylines.

## [Step 7: Draw Ellipse Arcs](#step-7-draw-ellipse-arcs)

The following example shows how to specify an ellipse arc. All ellipse parameters are 1:1 matching with those in SVG standard.

```
// Create simple PolygonPath
var path = new Autodesk.Edit2D.PolygonPath([
    {x: 53, y: 24}, // a
    {x: 62, y: 24}, // b
    {x: 57, y: 34}  // c
]);

// Change segment 0 into ellipse arc
var params = new Autodesk.Edit2D.EllipseArcParams();

// ellipse radii along ellipse x/y-axis
params.rx = 4;
params.ry = 6;

// ccw rotation of x/y-axes in degrees.
// rotation 0 means ellipse-x-axis = (1,0)
params.rotation = 0;

// whether to use shorter or longer path around ellipse.
params.largeArcFlag = false;

// Whether to go counterclockwise (true) or clockwise (false) from startAngle.
params.sweepFlag = true;

path.setEllipseArc(0, params);

layer.addShape(path);

```

Show More

## [Step 8: About Edit2D Shapes and SVG Shapes](#step-8-about-edit2d-shapes-and-svg-shapes)

You can convert SVG shapes to Edit2D shapes or convert Edit2D shapes to SVG shapes.

### 8.1 Import and Convert SVG Shapes

The following example shows how to import a single SVG shape and convert it to an Edit2D shape.

```
// Create Edit2D shape from SVG string
const svgString = '<path d="M 12.79,21.51 H 18.70 V 18.56 H 12.79 Z"/>';
const shape2    = Autodesk.Edit2D.Shape.fromSVG(svgString);

```

### 8.2 Export and Convert Edit2D Shapes

You can also export Edit2D shapes as SVG shapes.

```
// Get SVG string representation from a shape
shape.toSVG();

```

In the following example, we convert the full content of an Edit2D layer to an SVG and show the result in a pop up window.

```
function showSvgPopup() {

    // window size
    const width = 400;
    const height = 400;

    // define pixel-scope as box2
    const pixelBox = new THREE.Box2();
    pixelBox.min.set(0, 0);
    pixelBox.max.set(width, height);

    // convert layer to svg element
    const svg = Autodesk.Edit2D.Svg.createSvgElement(
        layer.shapes,
        { dstBox: pixelBox } // rescale to fit pixelBox [0,400]^2
    );

    // show in popup window
    const w = window.open('', '', `width=${width},height=${height}`);
    w.document.body.appendChild(svg);
    w.document.close();
    };

    showSvgPopup();

```

Show More

When you export from Edit2D, you can add style attributes.

```
shape.toSVG({exportStyle: true});

```

**Example output**: <path d=”M 12.79,21.51 H 18.7 V 18.56 H 12.79 Z” stroke=”rgb(0,0,128)” fill=”rgb(0,0,128)” stroke-width=”3” fill-opacity=”0.2”/>

You can also serialize Edit2D’s layer content 1:1 into an xml file and download it.

```
function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

function downloadLayerAsSvg() {

    // define pixel-scope as box2
    var pixelBox = new THREE.Box2();
    pixelBox.min.set(0, 0);
    pixelBox.max.set(400, 400);

    // get layer content as svg dom element
    var svgElem = Autodesk.Edit2D.Svg.createSvgElement(layer.shapes, {dstBox: pixelBox});

    // Serialize to string and download
    var serializer = new XMLSerializer();
    var xmlText = serializer.serializeToString(svg);

    download('test.svg', xmlText);
};

```

Show More

## [What’s Next?](#what-s-next)

Now that you’ve learned how to draw shapes manually, check out these other Edit2D tutorials:

- [Using the Edit2D Toolset](advanced_options-edit2d-use.md)
- [Customizing Edit2D](advanced_options-edit2d-customize.md)
