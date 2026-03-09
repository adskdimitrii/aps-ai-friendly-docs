# Extract Geometry from a Source File

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/xtract-geometry-from-source-file/about-this-tutorial/

---

# Extract Geometry from a Source File

## [About this walkthrough](#about-this-walkthrough)

This walkthrough demonstrates how to extract 3D geometry from a source file, and save that geometry to an OBJ file.

To extract geometry, you must know the object ID of each geometry to extract. To obtain the object ID you need to identify the model view (Viewable) the geometry resides on. To identify the Viewable (by its ID), you must first translate the source design to SVF2. The tasks in this walkthrough guide you through each stage of this workflow.

**Notes:**
:   1. You can only extract 3D geometry.
    2. You can extract geometry only to the OBJ format.

## [Postman Collection for this walkthrough](#postman-collection-for-this-walkthrough)

We also provide a [Postman](https://www.getpostman.com/) Collection containing the HTTP requests used in this walkthrough. On the Postman Collection, requests are grouped by task. The group has the same name as the corresponding task in this walkthrough.



Similarly, requests are named such that you can easily match a Step in this walkthrough to the corresponding HTTP request in the Postman Collection.



The Postman Collection is hosted in a [GitHub repository](https://github.com/autodesk-platform-services/aps-tutorial-postman/tree/master/ModelDerivative_06). It also contains a set of instructions on how to run the collection.
