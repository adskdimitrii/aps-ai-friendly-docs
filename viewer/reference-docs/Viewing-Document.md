# Document

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/Document/

---

Autodesk.Viewing

# Document

## [new Document(dataJSON, path, acmsession)](#new-document-datajson-path-acmsession)

Allows the client to load the model data from the cloud, it gives access to the root and provides a method for finding elements by id.

Typically, you load the document from APS, parse it for the required content (for example, 3d geometries), then pass this on to the viewer to display. You can also get some information about the document, such as the number of views it contains and its thumbnail image.

### Parameters

| dataJSON*   object | JSON data representing the document. |
| --- | --- |
| path*   string | Path/URL where dataJSON was fetched from. |
| acmsession   string | ACM session ID. |

* Required

# Methods

## [load(documentId, onSuccessCallback, onErrorCallback, options)](#load-documentid-onsuccesscallback-onerrorcallback-options)

Static method to load the translationâs manifest data from an APS endpoint.

### Parameters

| documentId*   string | The URN of the file. |
| --- | --- |
| onSuccessCallback*   Autodesk.Viewing.Document~loadSuccessCallback | A function that is called when load succeeds. |
| onErrorCallback*   Autodesk.Viewing.Document~loadErrorCallback | A function that is called when load fails. |
| options   object | An optional object that allows configuring manually the manifest request attributes - such as headers, endpoint etc. |

* Required

### Examples

```
Autodesk.Viewing.Document.load(
   MY_URN,
   function onSuccessCallback(doc){
       var bubbleRoot = doc.getRoot();
       console.log(bubbleRoot);
       // proceed to load a viewable into the Viewer...
   },
   function onErrorCallback(errCode, errMsg){
       console.error('Failed to load manifest [' + errCode + '] ' + errMsg);
   }
)

```

Show More

---

## [getRoot()](#getroot)

Returns a BubbleNode instance, encapsulating the current document manifest JSON.

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.BubbleNode](Viewing-BubbleNode.md) |  |
