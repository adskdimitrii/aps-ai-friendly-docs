# PDFExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/PDFExtension/

---

Autodesk.Viewing.Extensions

# PDFExtension

Registers a FileLoader to enhance `viewer.loadModel()` to allow loading of PDF files. The viewer will render a single page at a time.

The extension id is: `Autodesk.PDF`

## [new PDFExtension()](#new-pdfextension)

### Examples

```
// Create Viewer instance and load PDF file on page 1

```

Autodesk.Viewing.Initializer(options, function() {
:   var viewer = new Autodesk.Viewing.Viewer3D(div,config3d);
    viewer.start();
    viewer.loadExtension(‘Autodesk.PDF’).then(function() {
    > // URL parameter page will override value passed to loadModel
    > viewer.loadModel(‘path/to/file.pdf’, { page: 1 });

    });

});

---
