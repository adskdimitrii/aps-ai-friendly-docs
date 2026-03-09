# Using Aggregated View to Load a Model

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/advanced_options/aggregated-view/

---

# Using Aggregated View to Load a Model

AggregatedView implements a viewing application based on Viewer3D. The purpose of Aggregated View is to provide functionality around Viewer3D to facilitate implementation of viewer application workflows like switching between different views or toggling models on or off dynamically.

Examples of AggregatedView functionality include:

- React compatibility: You can set an array of nodes from React property and AggregatedView takes care of loading and showing or hiding models as needed.
- LRU-Caching of models: Keep models in memory for fast switches, but unload unused models if memory is critical.
- Extensions: You can specify which extensions to load or load the following defaults: `Autodesk.CrossFadeEffects`, `Autodesk.AEC.LevelsExtension`, `Autodesk.ModelStructure`, `Autodesk.AEC.HyperlinkExtension`, `Autodesk.AEC.Minimap3DExtension`, `Autodesk.AEC.CanvasBookmarkExtension` and `Autodesk.AEC.DropMeExtension`.
- Home camera: All models are considered when calculating the shared home view.
- Application State management: Facilitates some state management. For example,

> * You can set a camera before or after the model is loaded.
> * You can start Walk-mode before or after the BIMWalk extension loaded.
> * You can toggle visibility of a model regardless of loading state of the model.

- GlobalOffsets: Choose globalOffset automatically, but identically for all models to make sure that they are placed consistently.
- View Switches: Allow visibility toggling (hide/show) versus full view switches (switchView(nodes)), the latter including proper reset of camera, UI, and extensions.
- Diff Setups: Use diffOptions to view changes between aggregated views.

For more information, see: [AggregatedView](../reference-docs/Viewing-AggregatedView.md)

# Initialize and load a model with Aggregated View

Loading a model with Aggregated View follows the same steps as the `Autodesk.Viewing.Viewer3D` class. Initialize and load your document from a URN using `Autodesk.Viewing.Initializer` and `Autodesk.Viewing.Document.load`.

```
// AggregatedView instance
var view = new Autodesk.Viewing.AggregatedView();

// Initialize and load a document.
Autodesk.Viewing.Initializer(options, function onInitialized() {
    // Get the Viewer DIV
    var htmlDiv = document.getElementById('forgeViewer');

    // Initialize the AggregatedView view
    view.init(htmlDiv, options).then(function () {
        Autodesk.Viewing.Document.load(documentId, (doc) => {
            // Set the nodes from the doc
            var nodes = doc.getRoot().search({ type: 'geometry' });
            // Load the first bubble node. This assumes that a bubbleNode was successfully found
            view.setNodes(nodes[0]);
        }, (errorCode, errorMsg, messages) => {
            // Do something with the failed document.
            // ...
        });
    });
});

```

Show More

# Loading multiple models

`AggregatedView` makes it easy for you to load multiple models. Use `Autodesk.Viewing.Document.load` to load each document.

```
const bubbleNodes = [];
// docs is an array of loaded documents
docs.forEach((doc) => {
    var nodes = doc.getRoot().search({ type: 'geometry' });
    bubbleNodes.push(nodes[0]);
});
view.setNodes(bubbleNodes);

```

# Switching between views

The `switchView` function resets the extension, tools, and camera before loading the specified bubble nodes.

The following snippet finds all 3D bubble nodes from a loaded document and loads a 3D bubble node. This example also gets the model instance that is loaded.

```
// Get all of the 3D bubble nodes in a loaded document
const nodes3D = doc.docRoot.search({ role: '3d', type: "geometry" });

// The switchView function will load the model
view.switchView(nodes3D[0]);

// Get the model after it is fully loaded
const model = await view.getModelAndWait(nodes3D[0]);

```

Show More

After the first model is loaded, you can switch to other views by using the same method.

```
// Get all of the 2D bubble nodes in a loaded document
const nodes2D = doc.docRoot.search({ role: '2d', type: "geometry" });

// Now lets load two 2D models
// This will reset the UI, the extensions, the tools and the camera before a new node is loaded
view.switchView([nodes2D[0], nodes2D[1]]);

```

The following snippet demonstrates how you can unload a single bubble node.

```
// Unload a model
view.unload(nodes2D[1]);

```

To unload all current models use:

```
// Unload all of the loaded models
view.unloadAll();

```

For an Interactive Example, see [Aggregated View](interactive_examples-example_6.md).
