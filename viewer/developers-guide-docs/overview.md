# About the Viewer SDK

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/overview/

---

# About the Viewer SDK

![../../../_images/viewer_illustration.png](../../../_images/viewer_illustration.png)

**The Autodesk Platform Services Viewer SDK lets you create applications to view, share, and interact with design models on your own website from a wide variety of products.** The Viewer can display files from [AutoCAD](http://www.autodesk.com/products/autocad/overview), [Fusion 360](http://www.autodesk.com/products/fusion-360/overview), [Revit](http://www.autodesk.com/products/revit-family/overview), and many more. This JavaScript library enables developers to create applications that combine 2D and 3D visualization with business-oriented data.

The Viewer SDK provides an extension framework that allows developers to:

- Customize the Viewerâs appearance, controls, and behavior.
- Customize the content and location of the Viewer toolbar.
- Write custom extensions to further customize the user experience.

## [Common Uses](#common-uses)

Common applications that use this SDK include, but are not limited to:

- Project dashboards
- Digital twin
- Display planning and timelines
- Aggregate and coordinate model changes
- Generate 2D and 3D markups

## [Try it out](#try-it-out)

You can interact with the viewer in the following example. Click the drop-down in the Viewer window to choose different 2D and 3D models.

[https://codepen.io/autodesk-platform-services/embed/MWqmXxG?default-tab=result&amp;theme-id=light](https://codepen.io/autodesk-platform-services/embed/MWqmXxG?default-tab=result&amp;theme-id=light)

**Tip**: To experiment with customizing the Viewer, copy the following snippet and then click EDIT ON CODEPEN at upper right in the example. When CodePen opens, paste the snippet to the end of the original code in the **JS** tab. This snippet isolates all objects that contain the word âconcreteâ in their metadata.

```
viewer.addEventListener(Autodesk.Viewing.GEOMETRY_LOADED_EVENT, function () {
 viewer.search('concrete', function (ids) {
     viewer.isolate(ids);
 });
});

```

## [Next Steps](#next-steps)

Before you can display a model in the viewer, it must be translated into the SVF or SVF2 format. There are two ways to do this:

- If the file is in a BIM 360 or ACC workspace, the SVF/SVF2 file is automatically generated.
- Upload the model to the Object Storage Service (OSS). After uploading you can call the Model Derivative APIâs [POST Start Translation Job](https://aps.autodesk.com/en/docs/model-derivative/v2/reference/http/jobs/job-POST/) operation to perform the translation.

For more information, see the Model Derivative tutorial [Prepare a File for the Viewer](https://aps.autodesk.com/en/docs/model-derivative/v2/).

**Authentication (OAuth)** is required to use Model Derivative. The Model Derivative tutorial guides you through the process of obtaining an access token. You can also refer to the [Authentication Documentation](https://aps.autodesk.com/en/docs/oauth/v2/).

Note

- The Autodesk Viewer SDK JavaScript must be delivered from an Autodesk hosted URL.
- Before you begin, it is advisable to review the content in the Viewer Essentials and Advanced Options sections.

## [Terms of Service](#terms-of-service)

**APS Viewer SDK** is subject to [Autodesk Platform Services Terms of Service.](https://www.autodesk.com/company/legal-notices-trademarks/terms-of-service-autodesk360-web-services/forge-platform-web-services-api-terms-of-service)
