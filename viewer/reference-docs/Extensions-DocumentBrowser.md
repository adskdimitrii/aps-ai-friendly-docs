# DocumentBrowser

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/DocumentBrowser/

---

Autodesk.Viewing.Extensions

# DocumentBrowser

Adds a toolbar button that opens a Panel displaying all models and views available from the loaded Document. The panel allows navigating to any model referenced by the Document.

The extension id is: `Autodesk.DocumentBrowser`

## [new DocumentBrowser()](#new-documentbrowser)

### Examples

```
viewer.loadExtension('Autodesk.DocumentBrowser')

```

---

# Methods

## [loadNextModel(viewerConfig, loadOptions)](#loadnextmodel-viewerconfig-loadoptions)

Unloads the current model and then loads the next model in the Document. It may reload the same model if the Document contains only 1 model.

### Parameters

| viewerConfig   object |  |
| --- | --- |
| loadOptions   object |  |

## [loadPrevModel(viewerConfig, loadOptions)](#loadprevmodel-viewerconfig-loadoptions)

Unloads the current model and then loads the previous model in the Document. It may reload the same model if the Document contains only 1 model.

### Parameters

| viewerConfig   object |  |
| --- | --- |
| loadOptions   object |  |
