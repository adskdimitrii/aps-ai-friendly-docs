# Selective Loading Using Queries

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/advanced_options/selective-loading/

---

# Selective Loading Using Queries

Selective Loading uses spatial and property queries to filter the model geometry and load only what you need.
It allows you to provide a better experience interacting with the 3D scene by:
> - Improving the load time
> - Loading only the portion of the model required

Currently, the API focuses on load-time optimizations and only load-time filtering is supported.
Minor, known issues in the progressive rendering and the delay in time-to-first-pixel when using spatial filters will be addressed in future releases.

Example:

![../../../../_images/selective-loading-hyperlink1.png](../../../../_images/selective-loading-hyperlink1.png)

The image on the left shows a model without the loading filters applied.
The middle image shows an axis-aligned box (blue) being used as the spatial filter to define the portion of the model to load.
The image on the right shows the model loaded with the filter load-option passed to [loadDocumentNode](../reference-docs/Viewing-Viewer3D.md#loaddocumentnode-avdocument-manifestnode-options).
The same option can be provided to [viewer.loadModel](../reference-docs/Viewing-Viewer3D.md#loadmodel-url-options-onsuccesscallback-onerrorcallback).

## [Quickstart Example for Load-time Filtering](#quickstart-example-for-load-time-filtering)

To restrict model loading to certain areas or types of geometry, use queries to filter what to load using [loadDocumentNode](../reference-docs/Viewing-Viewer3D.md#loaddocumentnode-avdocument-manifestnode-options) options.
A load-time filter can be set by specifying a spatial and/or a property query using the `filter` load-option.

The following example creates a load-time filter using a `spatial_query`.
It describes a condition for testing an axis-aligned bounding box (`aabbox`) against the given axis-aligned box (`aabox`).
Objects that do not fulfill the condition are not loaded and only the objects in the shaded area are loaded.

```
const viewer = new Autodesk.Viewing.GuiViewer3D(document.getElementById('viewer'));
Autodesk.Viewing.Initializer(options, () => {
    viewer.start();
    Autodesk.Viewing.Document.load(documentID, onDocumentLoadSuccess,
        () => console.error('Failed to fetch the manifest.'));
});

function onDocumentLoadSuccess(viewerDocument) {
    const defaultModel = viewerDocument.getRoot().getDefaultGeometry();
    viewer.loadDocumentNode(viewerDocument, defaultModel, { // ...options
        filter: {
            "spatial_query": {
                "$encloses": [ { "aabox": [ -21.0, 37.0, -4.0, 46.0, 59.0, 21.0 ] } ]
            },
        }
    });
}

```

Show More

## [Try it out](#try-it-out)

You can interact and experiment with the viewer in the following example (the blue box shows the boundary of a simple, spatial query):

[https://codepen.io/autodesk-platform-services/embed/JjmwrWp?default-tab=result&amp;theme-id=light](https://codepen.io/autodesk-platform-services/embed/JjmwrWp?default-tab=result&amp;theme-id=light)

**Tip**: To experiment with the Viewer click EDIT ON CODEPEN at upper right in the example.

## [Spatial Query Language](#spatial-query-language)

*Spatial conditions* are specified using a spatial query language.
A spatial query comprises a *spatial condition* (`<scondition>`).

### `<scondition>`

Spatial conditions are composed of building blocks that determine whether an object should be loaded or not. Usually these are an expression, a primitive, an optional proxy, and in some cases additional parameters:
> - Primitives define what to test objects against. In the example above, all objects are tested against an axis-aligned box.
> - Proxies define how to represent objects when testing them against the primitive. This could be the objectâs axis-aligned bounding box, or a bounding sphere, for example. The proxy part of a condition is optional and defaults to the objectâs bounding box, which is the only proxy that is currently supported.
> - Expressions define how to interpret the proxy-primitive check. For example, an object could pass the condition if its bounding box intersects the given primitive, or it could be required to be fully enclosed.

Conditions can be negated, combined and nested as illustrated below.

| Condition | Description |
| --- | --- |
| `{ "$intersects": [ <sprimitive> ] }` | True, if the primitive intersects with the objectsâs axis-aligned bounding box. |
| `{ "$encloses": [ <sprimitive>, <sproxy>?, epsilon? ] }` | True, if the primitive has a volume and fully encloses the objectsâs axis-aligned bounding box. `sproxy` (optional) defines the type of the bounding box. Defaults to `aabbox` if not provided. `epsilon` (optional) is a scalar that expands each dimension of the primitive. Defaults to 0.0 if not provided. |
| `{ "$extent": [ <threshold> ] }` | True, if the volume of the objectsâs axis-aligned bounding box (world space) passes the threshold. |
| `{ "$not": <scondition> }` | Inverts the given condition. |
| `{ "$or": [ <scondition1>, <scondition2>, ... ] }` | Any of the given conditions must be fulfilled. |
| `{ "$and": [ <scondition1>, <scondition2>, ... ] }` | All of the given conditions must be fulfilled. |

### `<sprimitive>`

Spatial primitives are basic geometries such as points, lines, planes, spheres, and axis-aligned boxes that can be used to create spatial conditions. Currently, only the axis-aligned box is supported.

| Primitive | Specification | Example |
| --- | --- | --- |
| `aabox` | [ min, min, min, max, max, max ] | `{ "aabox": [ -3.3,  1.1,  0.4, -1.8,  3.9,  2.7 ] }` |

### `<sproxy>`

Spatial proxies describe the type of a *simplified geometrical representations of objects* that are used for the evaluation of a spatial condition. Currently, only axis-aligned bounding box is supported and the parameter is not explicitly required.

| Proxy | Description |
| --- | --- |
| `aabbox` | Axis-Aligned Bounding Box |

### Spatial Query Examples

Simple Example:

```
"spatial_query": { "$encloses": [ { "aabox": [ -0.3, -3.3, -4.9, +0.0, -3.2, -2.1 ] } ] }

```

Complex Example:

```
"spatial_query": { "$or": [

        /* two regions of interest where objects should be loaded */
        { "$encloses": [ { "aabox": [ -168.99, -226.19, -739.92, -133.78, -192.75, 978.69 ] } ] },
        { "$encloses": [ { "aabox": [ -389.19, -368.12,  836.04,  382.63,  140.48, 978.69 ] } ] },

        { "$and": [

            /* two regions that should remain empty (not intersecting with the scene objects) */
            { "$not": { "$or": [
                    { "$intersects": [ { "aabox": [  -88.49, -331.87, -536.42, 486.78, 350.62, -314.62 ] } ] },
                    { "$intersects": [ { "aabox": [ -285.78, -170.97,  119.58, -10.78, 353.67,  581.08 ] } ] }
                ] } },

            /* objects should pass a minimal world-space volume */
            { "$extent": 100000.0 } ] }
        ] }

```

Show More

### Immediate Spatial Evaluation

Spatial queries are evaluated per object as soon as all objects and their exact bounding volumes are available.
For large models consisting of lots of individual objects, this can introduce a minor but notable offset to the loading time.
In this case, the spatial evaluation behavior can be changed to immediate evaluation using the `spatial_behavior` filter option.
Here, preliminary, approximate bounding volumes are used for spatial evaluation once an object is known to the loader, likely leading to inaccuracies in filter evaluation:

```
viewer.loadDocumentNode(viewerDocument, defaultModel, { // ...options
    filter: {
        "spatial_behavior": "immediate", // or "exact" (default)
        "spatial_query": { ... },
    }
});

```

## [Property Query Language](#property-query-language)

The property queries use a simplified version of the [ACC Model Property Service Query Language](../../acc/how-to-docs/model-properties-query-ref.md), but with a reduced feature set.
Only `$or`, `$and`, `$not`, `$in`, `$eq`, `$ne`, `$like`, `$isnull`, `$notnull`, and `$coalesce` expressions are currently supported.

### Property Query Examples

Simple Example:

```
"property_query": {
    "$and": [
        { "$notnull": "s.props.p20d8441e" },
        { "$notnull": "s.props.p30db51f9" },
        { "$notnull": "s.props.p13b6b3a0" }
    ] }

```

Complex Example:

```
"property_query": [
    { "s.props.p4735026f": "'VALV'" },
    { "s.props.p4735026f": "'FBLI'" },
    { "s.props.p4735026f": "'TUBI'" },
    { "s.props.p4735026f": "'INST'" },
    { "s.props.p4735026f": "'ELBO'" },
    { "s.props.p4735026f": "'REDU'" },
    { "s.props.p4735026f": "'ATTA'" },
    { "s.props.p4735026f": "'FLAN'" } ]

```

Show More

### How to Get Property Hashes

Currently, property queries rely on property hashes. There are two ways to acquire these, either directly or indirectly.

**Direct Enumeration of Property Hashes**: To obtain the available properties and their hashes, you can enumerate them as soon as the property database is loaded using the following command:

```
const propertyHashes = await model.getPropertyHashes();

```

**Hash Lookup Syntax**: Instead of using the `s.props.p...` syntax, you can utilize a preliminary property lookup syntax to perform implicit property hash lookups:

```
// Match basic walls (by name property) and all objects that have CENTRIFUGE in their LTS description
"property_query": [
    // instead of { "s.props.p153cb174": "'Basic Wall'" },
    { "?name": "'Basic Wall'" }, // note the ? indicating a look-up
    { "?Base Constraint": "'Level 1'" } ]

```

A hash lookup currently requires an exact match of the property name to produce valid query results. If no objects are loaded, consider modifying the property query for better search outcomes.

## [Top-level Filter Condition](#top-level-filter-condition)

When both `spatial_query` and `property_query` are set, an object passes filtering if both conditions are met.
This behavior can be specified in the filter load option by specifying the `root_condition` to be either `and` (default) or `or`:

```
viewer.loadDocumentNode(viewerDocument, defaultModel, { // ...options
    filter: {
        "root_condition": "or", // or "and" (default)
        "spatial_query": { ... },
        "property_query": { ... },
    }
});

```

When `and` is specified, filtering cannot start immediately but needs to wait until all object bounds are known and properties are loaded.
