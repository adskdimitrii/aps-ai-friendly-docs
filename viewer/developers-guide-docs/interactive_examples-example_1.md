# Controlling Viewer State

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/interactive_examples/example_1/

---

# Controlling Viewer State

This example adds a button named **Toggle Explode** to the UI. The button toggles between an explode value of 0 and a second preset explode value. This example uses a 50% explode value (0.5) for the second value.

This is accomplished by adding a click event listener to the new `explodeButton`, which calls `viewer.explode()`. The click event lets you switch between the specified explode values.

[https://codepen.io/autodesk-platform-services/embed/QWJaazd?default-tab=js%2Cresult&amp;theme-id=light](https://codepen.io/autodesk-platform-services/embed/QWJaazd?default-tab=js%2Cresult&amp;theme-id=light)

**Tip** Open the example in CodePen and try different explode scale values.
