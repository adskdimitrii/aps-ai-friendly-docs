# Querying Model Properties

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/interactive_examples/example_3/

---

# Querying Model Properties

This example illustrates how to query a model using a property name and then isolate the corresponding element while automatically zooming in to that element. To test it out:

1. From the drop-down on the top-left, select **01_rac_basic_sample_project.rvt**.
2. In the text box next to the drop-down, enter *Single-Flush [422466]*.
3. Click **Search**. The specified door will display clearly, with all other elements suppressed.

The script first captures the name of the property from the text box. After that, it queries the modelâs properties to obtain the node ID of the element. It then uses this ID to isolate the element and zoom in on it.

[https://codepen.io/autodesk-platform-services/embed/QWJQjyV?default-tab=js%2Cresult&amp;theme-id=light](https://codepen.io/autodesk-platform-services/embed/QWJQjyV?default-tab=js%2Cresult&amp;theme-id=light)
