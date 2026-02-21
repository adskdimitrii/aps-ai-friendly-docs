# cloneHTMLElementsToWrapperElement

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/globals/Functions/cloneHTMLElementsToWrapperElement/

---

Functions

# cloneHTMLElementsToWrapperElement

Helper method to create a wrapper HTML element that contains all HTML elements specified. CSS styles are preserved. The wrapper element is sized to match the viewerâs canvas size, and the elements are positioned relative to the viewerâs canvas. This is useful for capturing HTML elements in a screenshot using html2canvas.

## [Parameters](#parameters)

| elementsToClone*   Array | Array of HTML elements to clone and capture |
| --- | --- |
| viewerImpl*   Viewer3DImpl | Viewer instance to get the original canvas size and bounding rect |

* Required

## [Returns](#returns)

| type | description |
| --- | --- |
| HTMLElement | Returns a wrapper element containing the cloned HTML elements, styled and positioned correctly. |
