# GestureDocumentNavigationExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/GestureDocumentNavigationExtension/

---

Autodesk.Viewing.Extensions

# GestureDocumentNavigationExtension

Provide an option to switch sheets and documents, using gestures.

The extension id is: `Autodesk.BIM360.GestureDocumentNavigation`

## [new GestureDocumentNavigationExtension()](#new-gesturedocumentnavigationextension)

### Examples

```
viewer.loadExtension('Autodesk.BIM360.GestureDocumentNavigation')

```

---

# Methods

## [load()](#load)

Load the GestureDocumentNavigation extension.

### Returns

| type | description |
| --- | --- |
| boolean | True if measure extension is loaded successfully. |

## [unload()](#unload)

Unload the measure extension.

### Returns

| type | description |
| --- | --- |
| boolean | True if measure extension is unloaded successfully. |

## [prepareChange(cb)](#preparechange-cb)

Prepare current document before switching sheet / document.

### Parameters

| cb*   function | This callback is called after current document is ready to switch. |
| --- | --- |

* Required

## [changeSheetRequired(guid)](#changesheetrequired-guid)

Change a sheet.

### Parameters

| guid*   number | The guid of the desired sheet. |
| --- | --- |

* Required

## [changeSheetRequired(urn, guid)](#changesheetrequired-urn-guid)

Change a document.

### Parameters

| urn*   number | The urn of the desired document. |
| --- | --- |
| guid*   number | The guid of the desired sheet. |

* Required
