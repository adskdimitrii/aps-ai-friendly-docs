# Translate a Revit File, Generating Room and Space Information

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/prep-roominfo4viewer/about-this-tutorial/

---

# Translate a Revit File, Generating Room and Space Information

## [About this walkthrough](#about-this-walkthrough)

This walkthrough demonstrates how to generate master views while translating a Revit File to SVF2. A master view is a model view (Viewable) that is generated for each phase of the Revit model. It contains all the elements, including room elements, present in the source model for that phase. When you load an SVF2 that has been translated with master views enabled, you get the ability work at the room level in the Viewer.

In this walkthrough, you translate an MEP (Mechanical Electrical and Plumbing) file that contains space and zone information to SVF2. Thereafter you display the translated SVF2 file in the viewer and display room information. The walkthrough restricts itself to show you how to translate the file. It does not teach you how to display the file in the viewer. Instead, it points you to a web page that uses the Viewer SDK to display the Viewables that were generated, including the Viewable generated for the master view.

## [Postman Collection for this walkthrough](#postman-collection-for-this-walkthrough)

We also provide a [Postman](https://www.getpostman.com/) Collection containing the HTTP requests used in this walkthrough. On the Postman Collection, requests are grouped by task. The group has the same name as the corresponding task in this walkthrough.

![../../../../_images/tutorial_07_forge_postman_menu_01.png](../../../../_images/tutorial_07_forge_postman_menu_01.png)

Similarly, requests are named such that you can easily match a Step in this walkthrough with the corresponding HTTP request in the Postman Collection.

![../../../../_images/tutorial_07_forge_postman_menu_02.png](../../../../_images/tutorial_07_forge_postman_menu_02.png)

The Postman Collection is hosted in a [GitHub repository](https://github.com/autodesk-platform-services/aps-tutorial-postman/tree/master/ModelDerivative_07), and is accompanied by a set of instructions.
