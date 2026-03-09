# Glossary of Terms

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/glossary/

---

# Glossary of Terms

| Term | Definition |
| --- | --- |
| access token | An access token (sometimes just âtokenâ or âbearer tokenâ) is a credential used by an application to access an API.   The Authentication API returns an access token at the end of a successful authentication flow.       The Viewer requires access tokens that have a scope of `viewables:read`.       For more information, see the [Authentication API Basics](https://aps.autodesk.com/en/docs/oauth/v2/overview/basics/) and [Scopes](https://aps.autodesk.com/en/docs/oauth/v2/overview/scopes/) sections. |
| canvas | An HTML element used as a target for rendering the Viewer SDK. |
| dbid | The ID of an object linking it to its metadata in the properties database. The dbid is also needed to call Viewer SDK methods; for example, the function used to hide objects in the model expects a list of dbids as its argument. |
| document | The file for the model you want to load. The doc gives access to the root and provides a method for finding elements by id. To learn more, see [Document](../reference-docs/Viewing-Document.md). |
| extensions | A piece of JavaScript code that is optionally loaded at runtime to extend or modify Viewer SDKâs behavior.       Some extensions are bundled with Viewer SDK, and developers can write their own extensions for specific use cases. |
| fragID | The ID for an individual fragment of a Viewer SDK model. |
| fragment | A part of an object with specific geometry and material; a single object consists of one or more fragments. For example, a door object may consist of a door knob (with brass material) and a door frame (with wood material). |
| geometry node | The smallest selectable element of a model in Viewer SDK (e.g. a door). This is also known as an *object*. |
| ghosting | A feature that makes selected nodes in a model transparent, allowing other nodes to become more prominent. |
| headless | Viewer SDK without UI elements; only the 3D render canvas. |
| highlighting | The act of changing the way an object is drawn to make it standout. The Viewer SDK will highlight objects when they are selected and when the user mouses over them. Theming is another way to highlight objects available to applications. |
| markup | An extension for annotating viewables. |
| manifest | The result of a translation process, a structured collection of resources (e.g., model geometry, thumbnails, camera views) used by Viewer SDK.       Get a manifest using the [GET :urn/manifest](../../model-derivative/http-docs/http-urn-manifest-GET.md) endpoint.       Viewer SDK can only render viewables. |
| measure | An extension for measuring the distance between two points on the surface of a model. |
| orbit | A feature that allows users to move the camera up, down, left & right. |
| overlay | A feature that allows you to add custom geometry to the loaded model. To learn more, see the [Add Custom Geometry](advanced_options-custom-geometry.md) tutorial. |
| profile | A set of preferences and extensions in the Viewer SDK. Developers can create their own custom profiles and there are built-in profiles available in the Viewer SDK to bring the same user experience as Autodesk desktop products like Navisworks and Revit. |
| property database | Metadata associated with a viewable and its parts. The property database may   contain metadata for each geometry node. |
| scene | An environment where one more more models are placed. Models, cameras, and lights can be positioned or transformed in the environmentâs coordinate system. |
| search | A feature for searching the viewableâs metadata, also   called *property database*. |
| section(ing) | An extension for cutting 3D models and seeing inside of them. |
| seed file | The original file that you want to visualize in Viewer SDK. |
| selection | A feature that lets users select nodes in a model. You can use selection to specify which nodes users can select and keep track of the selected nodes. |
| theming | A means to highlight objects by changing their color. |
| viewable | Either a 3D model or a 2D sheet referenced by the manifest. |
| viewcube | A tool available for 3D models that helps users orient the cameraâs position. |
| viewer state | The current view of a model based on the position of the camera systemâs eye. |
