# Task 4 â Publish an Activity

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/autocad/task4-publish-activity/

---

# Task 4 â Publish an Activity

An Activity is an action that can be executed in the Automation Service. You create and post Activities to run specific AppBundles.

By the end of this task, you will know:

- What an Activity is.

- How to create an Activity.

- How to create new versions of an Activity.

- How to reference a specific version of an Activity by an alias.

You will use the following operations to handle Activities for this task:

HTTP Request Description POST /activities Creates a new Activity. POST /activities/{id}/aliases Creates a new alias for this Activity. POST /activities/{id}/versions Creates a new version of the Activity. PATCH /activities/{id}/aliases/{aliasId} Modifies alias details.

## Step 1 - Create a new Activity

To create a new Activity named ListLayersActivity, post this request:

### Request

```
curl - X POST \ https : // developer . api . autodesk . com / da / us - east / v3 / activities \ - H 'Content-Type: application/json' \ - H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \ - d '{ "id": "ListLayersActivity", "commandLine": [ "$(engine.path) \\ accoreconsole.exe /i \" $(args[InputDwg].path) \" /al \" $(appbundles[ListLayers].path) \" /s \" $(settings[script].path) \" " ], "parameters": { "InputDwg": { "zip": false, "ondemand": false, "verb": "get", "description": "Input drawing file", "localName": "Input.dwg" }, "result": { "zip": false, "ondemand": false, "verb": "put", "description": "Results", "required": true, "localName": "layers.txt" } }, "engine": "Autodesk.AutoCAD+24_3", "appbundles": [ "<YOUR_APP_NICKNAME>.ListLayers+my_working_version" ], "settings": { "script": "(command \" LISTLAYERS \" ) \n " }, "description": "Extracts layer names from an input drawing file and saves them to a text file" }''
```

Attribute Description id The name given to your new Activity. commandLine The command run by this Activity. - $(engine.path)\\accoreconsole.exe - The full path to the AutoCAD engine. The version of AutoCAD to be used is defined in the request body as âengineâ: âAutodesk.AutoCAD+24_3 (Autocad 2024). More information about engines can be found in the Additional notes section of the previous step . - $(args[InputDwg].path) - The full path to the folder that the file identified by the parameter InputDwg is downloaded to. - $(appbundles[ListLayers].path) - The full path to where the AppBundle specified under appbundles is unzipped to. - $(settings[script].path) - The full path to the file where the Automation Service saves the value of the setting named script . For more information on command line options for the AccoreConsole see Getting Started with AccoreConsole parameters Defines the inputs and outputs that need to be provided when the Activity is executed. Input parameters are identified by the attribute "verb":"get" . Output parameters are identified by the attribute "verb":"put" . engine The engine on which your Activity runs. The available engine versions are described in the Additional notes section in Task 3 appbundles The fully qualified id of the AppBundle referred to in commandLine . settings Contains the script to be run by the AutoCAD engine, as referred to in commandLine . See AutoCAD documentation on scripts for more information on the syntax of command scripts.

### Response

```
{ "commandLine" : [ "$(engine.path)\\accoreconsole.exe /i \"$(args[InputDwg].path)\" /al \"$(appbundles[ListLayers].path)\" /s \"$(settings[script].path)\"" ], "parameters" : { "InputDwg" : { "verb" : "get" , "description" : "Input drawing file" , "localName" : "Input.dwg" }, "result" : { "verb" : "put" , "description" : "Results" , "required" : true , "localName" : "layers.txt" } }, "id" : "DA4ACADV2.ListLayerActivity" , "engine" : "Autodesk.AutoCAD+24_3" , "appbundles" : [ "<YOUR_APP_NICKNAME>.ListLayers+my_working_version" ], "settings" : { "script" : { "value" : "(command \"LISTLAYERS\")\n" } }, "description" : "Extracts layer names from an input drawing file and saves them to a text file" , "version" : 1 }
```

The response includes:

Attribute Description version The version number for the Activity created by the post request. A post request that creates a new Activity will get version number 1 .

## Step 2 - Create an alias to the Activity

The Automation API does not let you reference an Activity by its id . You must always reference an Activity by an alias.  Note that an alias points to a specific version of an Activity and not the Activity itself.

To create an alias named current_version , which refers to version 1 of the ListLayersActivity :

### Request

```
curl - X POST \ https : // developer . api . autodesk . com / da / us - east / v3 / activities / ListLayersActivity / aliases \ - H 'Content-Type: application/json' \ - H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \ - d '{ "version": 1, "id": "current_version" }'
```

### Response

```
{ "version" : 1 , "id" : "current_version" }
```

## Step 3 - Update an existing Activity

NOTE: This step is optional

The Automation API does not let you overwrite an Activity once you have created it. If you want to modify/update an existing Activity,
you must update it as a new version.
If you try to overwrite an existing Activity, the Automation Service returns a `409 Conflict error.

To create a new version of an Activity:

### Request

```
curl - X POST \ https : // developer . api . autodesk . com / da / us - east / v3 / activities / ListLayersActivity / versions \ - H 'Content-Type: application/json' \ - H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \ - d '{ "id": null, "commandLine": [ "$(engine.path) \\ accoreconsole.exe /i \" $(args[InputDwg].path) \" /al \" $(appbundles[ListLayers].path) \" /s \" $(settings[script].path) \" " ], "parameters": { "InputDwg": { "zip": false, "ondemand": false, "verb": "get", "description": "Input drawing file", "localName": "InputDrawing.dwg" }, "result": { "zip": false, "ondemand": false, "verb": "put", "description": "Results", "required": true, "localName": "layers.txt" } }, "engine": "Autodesk.AutoCAD+22", "appbundles": [ "YOUR_APP_NICKNAME.ListLayers+my_working_version" ], "settings": { "script": "(command \" TEST \" ) \n " }, "description": "Extracts layer names from an input drawing file and saves them to a text file" }'
```

Note: You can omit id from the request body. If you include id in the request body, set it to null . If you donât set it to null , the Automation Service throws an error.

### Response

```
{ "commandLine" : [ "$(engine.path)\\accoreconsole.exe /i \"$(args[InputDwg].path)\" /al \"$(appbundles[ListLayers].path)\" /s \"$(settings[script].path)\"" ], "parameters" : { "InputDwg" : { "verb" : "get" , "description" : "Input drawing file" , "localName" : "$(InputDwg)" }, "result" : { "verb" : "put" , "description" : "Results" , "required" : true , "localName" : "layers.txt" } }, "id" : "YOUR_APP_NICKNAME.ListLayersActivity" , "engine" : "Autodesk.AutoCAD+22" , "appbundles" : [ "YOUR_APP_NICKNAME.ListLayers+my_working_version" ], "settings" : { "script" : { "value" : "(command \"TEST\")\n" } }, "description" : "Extracts layer names from an input drawing file and saves them to a text file" , "version" : 2 }
```

## Step 4 - Assign an existing alias to the updated Activity

NOTE: Perform this step only if you carried out Step 3

Currently, the alias current_version points to version 1 of the Activity.

id alias version ListLayersActivity current_version 1 ListLayersActivity 2

You can reassign the alias current_version to point to version 2 of the Activity.

id alias version ListLayersActivity 1 ListLayersActivity current_version 2

To update the alias, you can either:

- Delete the existing alias and recreate it with the version you want to label.

- Send a PATCH request.

To send a PATCH request:

### Request

```
curl - X PATCH \ https : // developer . api . autodesk . com / da / us - east / v3 / activities / ListLayersActivity / aliases / current_version \ - H 'Content-Type: application/json' \ - H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \ - d '{ "version": 2 }'
```

Notes:

- version - Refers to the version number the alias refers to.
