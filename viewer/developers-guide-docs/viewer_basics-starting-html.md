# Getting Started

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/viewer_basics/starting-html/

---

# Getting Started

## [Before You Begin](#before-you-begin)

Before you can create a viewer application, there are a few things you need to do.

1. Create an Autodesk Platform Services (APS) account.
2. Register an app.
3. Get the Client ID and Secret.
4. Provision access in other products.

For more information, see the APS [Getting Started](https://tutorials.autodesk.io) tutorial.

### Add Viewer to an HTML Page

The `<script>` tag in the following HTML snippet loads the bundled Viewer SDK at runtime and creates an instance of the Viewer that covers the entire HTML page.

```
<head>
    <meta name="viewport" content="width=device-width, minimum-scale=1.0, initial-scale=1, user-scalable=no" />
    <meta charset="utf-8">

    <link rel="stylesheet" href="https://developer.api.autodesk.com/modelderivative/v2/viewers/7.*/style.min.css" type="text/css">
    <script src="https://developer.api.autodesk.com/modelderivative/v2/viewers/7.*/viewer3D.min.js"></script>

    <style>
        body {
            margin: 0;
        }
        #forgeViewer {
            width: 100%;
            height: 100%;
            margin: 0;
            background-color: #F0F8FF;
        }
    </style>
</head>
<body>

    <div id="forgeViewer"></div>

</body>

```

Show More

The `div` identifier `forgeViewer` will initialize a Viewer instance. To learn how to initialize a viewer instance, see Part 2: [Initialize Viewer](https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/viewer_basics/initialization/).

**Note:** The Viewer has a hard dependency on three.js R71.

#### Bundle Size

We recommend including the `<script>` tag to load the Viewer JavaScript library as late as possible. This allows browsers to render all static HTML content first.

#### Viewer Versions

The `<script>` tag specifies the location of the Viewer’s JavaScript code, as well as the version of the library to download. In the example HTML above, the specified version is `7.*`, which pulls the latest minor version available for the major version 7 release.

For example, if versions `7.0`, `7.1` and `7.2` are available, then requesting Viewer version `7.*` retrieves version `7.2`.

Likewise, the specified version can include the minor or patch numbers, too. The following URLs are all valid:

```
<!-- Fetch exactly version 7.0.0 -->
<script src="https://developer.api.autodesk.com/modelderivative/v2/viewers/7.0.0/viewer3D.min.js"></script>

<!-- Fetch latest patch version for 7.0 -->
<script src="https://developer.api.autodesk.com/modelderivative/v2/viewers/7.0.*/viewer3D.min.js"></script>

<!-- Also fetch latest patch version for 7.0 -->
<script src="https://developer.api.autodesk.com/modelderivative/v2/viewers/7.0/viewer3D.min.js"></script>

<!-- Fetch latest minor version for 7.0 -->
<script src="https://developer.api.autodesk.com/modelderivative/v2/viewers/7.*/viewer3D.min.js"></script>

```

Show More

#### LMV_VIEWER_VERSION

You can validate the fetched viewer version with the help of the [global variable LMV_VIEWER_VERSION](https://aps.autodesk.com/en/docs/viewer/v7/reference/properties/LMV_VIEWER_VERSION/).

### Initialize Viewer

Initialization is a 3 step process:

1. Enable automatic region routing.
    Automatic region routing enables the Viewer to automatically determine where a model is stored based on its URN. Prior to version 7.109.1, you needed to explicitly specify the region via Initializer options. This is no longer required.

2. Initialize the page using function `Autodesk.Viewing.Initializer()`.

3. Create a Viewer instance and verify that WebGL support is available.

#### Example

```
var viewer;
var options = {
    env: 'AutodeskProduction2', // Use 'AutodeskProduction' for SVF
    api: 'streamingV2', // Use 'derivativeV2' for SVF
    getAccessToken: function(onTokenReady) {
        var token = 'YOUR_ACCESS_TOKEN';
        var timeInSeconds = 3600; // Use value provided by APS Authentication (OAuth) API
        onTokenReady(token, timeInSeconds);
    }
};

Autodesk.Viewing.FeatureFlags.set(‘DS_ENDPOINTS’, true); // Enable automatic region routing

Autodesk.Viewing.Initializer(options, function() {

    var htmlDiv = document.getElementById('forgeViewer');
    viewer = new Autodesk.Viewing.GuiViewer3D(htmlDiv);
    var startedCode = viewer.start();
    if (startedCode > 0) {
        console.error('Failed to create a Viewer: WebGL not supported.');
        return;
    }

    console.log('Initialization complete, loading a model next...');

});

```

Show More

#### Initializing the Viewer for SVF and SVF2 Support

You enable SVF or SVF2 support by passing the `env` and `api` parameters when initializing the Viewer. The value you use for `env` and `api` specifies an SVF derivative or an SVF2 derivative. The following table lists the values to use:

| Parameter | SVF | SVF2 |
| --- | --- | --- |
| env | AutodeskProduction | AutodeskProduction2 |
| api | derivativeV2 | streamingV2 |

#### Initializer

The Initializer function needs to be run just once. It makes sure that all subsystems are running before proceeding.
Refer to the Parameters listed under the [Initializer Method](https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/#initializer-options-callback) for details of the values supported for `options`.

#### Create Viewer instance

Once the Initializer callback is invoked, we proceed to create a new instance of the Viewer.

```
var htmlDiv = document.getElementById('forgeViewer');
viewer = new Autodesk.Viewing.GuiViewer3D(htmlDiv, {});

```

You have to invoke the method `viewer.start()` just once. From there, validate that the browser supports WebGL before moving on to [Load a Model](https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/viewer_basics/load_a_model/).

#### Destroy Viewer instance

When the Viewer is no longer needed on the page, uninitialize and claim back memory using:

```
viewer.finish();
viewer = null;
Autodesk.Viewing.shutdown();

```

### Load a Model

Loading a model is a 2 step process.

1. Fetch a Manifest JSON from [Model Derivative API](../../model-derivative/http-docs/http-urn-manifest-GET.md).
2. Instruct the Viewer to load one of the models referenced by the Manifest JSON.

Before you load a model, you must use the [POST job](../../model-derivative/http-docs/http-job-POST.md) endpoint of the [Model Derivative](https://aps.autodesk.com/en/docs/model-derivative/v2/) API to kick off a translation job, which translates the model into the SVF format. The translation job produces a JSON file known as a Manifest. The manifest provides details of the resources (e.g., model geometry, thumbnails, camera views) that were produced by the [translation job](../../model-derivative/http-docs/http-job-POST.md).

See the [Prepare a File for the Viewer](https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/prep-file4viewer/) tutorial in the Model Derivative API documentation for more information.

In order to use the [Model Derivative](https://aps.autodesk.com/en/docs/model-derivative/v2/) API you must have an `ACCESS_TOKEN`. Use the APS [Authentication](https://aps.autodesk.com/en/docs/oauth/v2/reference/http/) API to obtain an access token. The Viewer supports both 2-legged and 3-legged tokens.

#### Step 1: Fetch Manifest

A manifest is a JSON document containing the result of a translation job. As this process takes place, the content in the JSON document is updated to reflect the progress of the translation job. Once the translation process is complete, the JSON document will contain references to all available derivatives, some of which are models that can be loaded into the Viewer.

The Viewer library provides a static method for fetching a manifest for a specified URN string value.

```
var documentId = 'urn:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bXktYnVja2V0L215LWF3ZXNvbWUtZm9yZ2UtZmlsZS5ydnQ';
Autodesk.Viewing.Document.load(documentId, onDocumentLoadSuccess, onDocumentLoadFailure);

function onDocumentLoadSuccess(viewerDocument) {
    // viewerDocument is an instance of Autodesk.Viewing.Document
}

function onDocumentLoadFailure() {
    console.error('Failed fetching Forge manifest');
}

```

Show More

**Notes:**
> - The `documentId` is a string value of the URN of the model that was translated.
> - The URN must be encoded as an *unpadded Base64 string*. See the [Prepare a File for the Viewer](https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/prep-file4viewer/) tutorial in the Model Derivative API documentation for more information on Base64 encoding.
> - The value assigned to `documentId` must be prefixed with the string `urn:`
> - If you want to reuse the code snippet shown above, replace the value of `documentId` with the URN from your own translation jobs.
> - In some cases you may need to determine if the URN is from EMEA or US. Start by base64 decoding the URN, then check if it contains `urn:adsk.wipemea:xxx` (for EMEA) or `urn:adsk.wipprod:xxx` (for US).

After successfully fetching the manifest, the callback `onDocumentLoadSuccess` gets invoked. The callback receives the argument `viewerDocument`, which is an instance of [Autodesk.Viewing.Document](../reference-docs/Viewing-Document.md).

#### Step 2: Load Model in Manifest

The snippets below assume that a `viewer` instance is available.

You have the option to load the default model or to choose from the list of all models in the manifest.

To load the default model in the manifest:

```
var defaultModel = viewerDocument.getRoot().getDefaultGeometry();
viewer.loadDocumentNode(viewerDocument, defaultModel);

```

To choose a different model, retrieve the list of all models and use custom code to determine which one to load.

```
var viewables = viewerDocument.getRoot().search({'type':'geometry'});
viewer.loadDocumentNode(viewerDocument, viewables[0]);

```

#### Putting it all together

At this point, developers should have code that looks like this:

```
var documentId = 'urn:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bXktYnVja2V0L215LWF3ZXNvbWUtZm9yZ2UtZmlsZS5ydnQ';
Autodesk.Viewing.Document.load(documentId, onDocumentLoadSuccess, onDocumentLoadFailure);

function onDocumentLoadSuccess(viewerDocument) {
    var defaultModel = viewerDocument.getRoot().getDefaultGeometry();
    viewer.loadDocumentNode(viewerDocument, defaultModel);
}

function onDocumentLoadFailure() {
    console.error('Failed fetching Forge manifest');
}

```

Show More
