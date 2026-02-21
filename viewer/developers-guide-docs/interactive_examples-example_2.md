# Handle Viewer Events

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/interactive_examples/example_2/

---

# Handle Viewer Events

This example implements an event listener for the `SELECTION_CHANGED_EVENT`.

Selecting an object calls the specified inline function, which asynchronously retrieves the ID of the selected object and displays it in an alert box with the message: **The user has selected objects with IDs**. The message is followed by the retrieved object ID.

[https://codepen.io/autodesk-platform-services/embed/QWJaaGj?default-tab=js%2Cresult&amp;theme-id=light](https://codepen.io/autodesk-platform-services/embed/QWJaaGj?default-tab=js%2Cresult&amp;theme-id=light)

**Tip** Open the example in CodePen and change the message text.
