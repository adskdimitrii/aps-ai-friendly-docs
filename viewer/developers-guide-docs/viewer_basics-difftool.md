# Using DiffTool to Compare Models

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/viewer_basics/difftool/

---

# Using DiffTool to Compare Models

The DiffTool extension provides UI controls for comparing 2D and 3D models.

## [Examples](#examples)

```
viewer.loadExtension('Autodesk.DiffTool')

```

### Usage

Using the DiffTool, you can compare the differences between models in Viewer SDK. The DiffTool shows three kinds of changes to the primary model:

- Added: Shows objects that have been added to the primary model.
- Removed: Shows objects that have been removed from the primary model.
- Modified: Shows objects that have been changed in the primary model

There are three modification types:

- Geometry: The geometry data has been modified.
- Transformation: The geometry transformation has been modified.
- Attribute: One or more properties of the geometry has been modified.

### Configuring DiffTool LMV extension

A list of all configuration options for the DiffTool LMV extension:

| primaryModels*   Autodesk.Viewing.Model | An array of loaded âAutodesk.Viewing.Modelâ instances that are compared by the DiffTool. |
| --- | --- |
| diffModels*   Autodesk.Viewing.Model | An array of other loaded Autodesk.Viewing.Model instances that participate in the diff operation as the previous state. Length must match primaryModels to define pairs of models to be compared. |
| versionA*   string | Version identifier for the primary models, such as â2â, âVersion 2â, or â02/26/2018â. Note that you must provide a localized string if you are using something other than numbers or dates. |
| versionB*   string | Version identifier of the diff models, usually a previous version |
| mimeType*   string | âapplication/vnd.autodesk.revitâ: Revitâapplication/vnd.autodesk.r360â: Revitâapplication/vnd.autodesk.fusion360â: For Fusion 360âapplication/vnd.autodesk.f3dâ: For Fusion 360âapplication/vnd.autodesk.inventor.assemblyâ: For Inventor (IAM)âapplication/vnd.autodesk.navisworksâ[`](#id1): For Navisworks (NWD)âapplication/vnd.autodesk.cadâ: For IFCâapplication/vnd.autodesk.dxfâ: For DXFâapplication/vnd.autodesk.autocad.dwgâ: For DWG |
| propertyFilter   {Object.<string,Array<string>} | An object representing a category and properties key-value pair to ignore for diff computation. Example: {âDimensionsâ:[âAreaâ,âLengthâ], âMechanical - Flowâ:[âFlowâ]} |

* Required

#### Using LMV initialization options

## [Examples](#id3)

```
var config = {
    availableDiffModes: ['overlay', 'sidebyside'],
    diffModels: A,
    primaryModels: B,
    mimeType: 'application/vnd.autodesk.revit',
    diffMode: 'overlay',
    versionA: 'A',
    versionB: 'B',
    propertyFilter: { "Category1": [ "Property1", "Property2" ] }
};

viewer.loadExtension("Autodesk.DiffTool", config);

```

Show More
