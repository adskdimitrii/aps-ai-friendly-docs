# Task 3 â Upload an AppBundle to the Automation Service

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/autocad/task3-upload-appbundle/

---

# Task 3 â Upload an AppBundle to the Automation Service

An AppBundle is a package that contains the files of an AutoCAD plug-in.

By the end of this task you will be able to:

- Put together an AppBundle.

- Upload an AppBundle to the Automation Service.

- Create an alias for the AppBundle.

You will use the following operations to handle AppBundles in this task:

HTTP Request Description POST /appbundles Registers a new AppBundle. POST /appbundles/{id}/aliases Creates a new alias for the AppBundle. POST /appbundles/{id}/versions Creates a new version of the AppBundle. PATCH /appbundles/{id}/aliases/{aliasId} Modify alias details.

## Step 1 - Download the AutoCAD CRX plug-in

You need to download a CRX plug-in called command.dll from the GitHub repository provided below. This plug-in contains a command called LISTLAYERS, which extracts layer names from an input drawing file and stores them in a text file.

- Download command.dll from here Alternatively, you can use the source code provided in this GitHub repository to build the plug-in.

## Step 2 - Build an AppBundle

An AppBundle is a zip file that includes the AutoCAD CRX plug-in, a manifest file called PackageContents.xml, and related files organized in a specific way. It follows a format similar to an Autodesk Exchange Appâs Autoloader. AppBundle allows you to upload the plug-in and its dependencies for execution. The PackageContents.xml file provides runtime instructions to the Automation Service, helping it locate and load the plug-in.

- Create a folder named ListLayers.bundle , and within it, create a folder named Contents .

- Place the file commands.dll (the file you downloaded in the previous step) inside the Contents folder.

- Create a text file named PackageContents.xml with the following content, and save it in the ListLayers.bundle folder.

```
<?xml version="1.0" encoding="utf-8" ?> <ApplicationPackage SchemaVersion= "1.0" Version= "1.0" > <Components> <RuntimeRequirements OS= "Win64" Platform= "AutoCAD" /> <ComponentEntry AppName= "ListLayers" ModuleName= "./Contents/command.dll" AppDescription= "AutoCAD.IO .net test app" LoadOnCommandInvocation= "True" LoadOnAutoCADStartup= "False" > <Commands GroupName= "MyTestCommands" > <Command Global= "LISTLAYERS" Local= "LISTLAYERS" /> </Commands> </ComponentEntry> </Components> </ApplicationPackage>
```

Note : For more information on PackageContents.xml , see PackageContents.xml Format Reference

- Create a zip file named ListLayers.zip from the folder ListLayers.bundle . Note : If you are unable to build the AppBundle, download and use ListLayers.zip for subsequent steps from here The structure of ListLayers.zip should look similar to the following code block. ListLayers.zip
|-- ListLayers.bundle
|   |-- PackageContents.xml
|   |-- Contents
|   |   |-- command.dll

Note : If you are unable to build the AppBundle, download and use ListLayers.zip for subsequent steps from here

The structure of ListLayers.zip should look similar to the following code block.

```
ListLayers.zip
|-- ListLayers.bundle
|   |-- PackageContents.xml
|   |-- Contents
|   |   |-- command.dll
```

## Step 3 - Register the AppBundle

Before you upload the AppBundle to the Automation Service, you must register the AppBundle.

- Register an AppBundle named ListLayers as per the following example. It uses AutoCAD 2020 as the target engine:

### Request

```
curl - X POST \ 'https://developer.api.autodesk.com/da/us-east/v3/appbundles' \ - H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \ - H 'Content-Type: application/json' \ - d '{ "id": "ListLayers", "engine": "Autodesk.AutoCAD+24_3", "description": "List Layers AppBundle based on AutoCAD 2024" }'
```

Attribute Description id The name given to the AppBundle. engine The engine that the AppBundle must be loaded on; AutoCAD 2023 in this case. For more information on engine aliases, see the Additional Notes section at the bottom of this page.

### Response

```
{ "uploadParameters" : { "endpointURL" : "https://dasprod-store.s3.amazonaws.com" , "formData" : { "key" : "apps/DA4ACADV2/ListLayers/1" , "content-type" : "application/octet-stream" , "policy" : "eyJleHBpcmF0aW9uIjoiMjAyMy0wOS..." , "success_action_status" : "200" , "success_action_redirect" : "" , "x-amz-signature" : "c8df469d02b4e618288b6..." , "x-amz-credential" : "ASIATGVJZKM3OFUVUYM2/20230921/us-east-1/s3/aws4_request/" , "x-amz-algorithm" : "AWS4-HMAC-SHA256" , "x-amz-date" : "20230921T060833Z" , "x-amz-server-side-encryption" : "AES256" , "x-amz-security-token" : "IQoJb3JpZ2luX2VjEP7//////////wEaC..." } }, "id" : "DA4ACADV2.ListLayers" , "engine" : "Autodesk.AutoCAD+24_2" , "description" : "List Layers AppBundle based on AutoCAD 2023" , "version" : 1 }
```

Attribute Description endpointURL The URL you must upload the AppBundle zip file to. version The version number of the AppBundle created by the POST request. For new AppBundles, the returned version is always 1 . formData The form data that must accompany the AppBundle when you upload it to endpointURL . formData expires in 3600 seconds.

## Step 4 - Upload the AppBundle

Upload the AppBundle to the signed URL returned by endpointURL in the previous step.

```
curl - X POST \ https : // dasprod - store . s3 . amazonaws . com \ - H 'Cache-Control: no-cache' \ - F 'key="apps/DA4ACADV2/ListLayers/1"' \ - F 'content-type="application/octet-stream"' \ - F 'policy="eyJleHBpcmF0aW9uIjoiMjAyMy0wOS0yMVQwNzowODozMy..."' \ - F 'success_action_status="200"' \ - F 'x-amz-signature="c8df469d02b4e618288b6f9423bf342670312..."' \ - F 'x-amz-credential="ASIATGVJZKM3OFUVUYM2/20230921/us-east-1/s3/aws4_request/"' \ - F 'x-amz-algorithm="AWS4-HMAC-SHA256"' \ - F 'x-amz-date="20230921T060833Z"' \ - F 'x-amz-server-side-encryption="AES256"' \ - F 'x-amz-security-token="IQoJb3JpZ2luX2VjEP7//////////wEaCX...' \ - F 'success_action_redirect=""' \ - F 'file=@"<LOCAL_PATH_TO_FOLDER_CONTAINING_ZIP_FILE>/ListLayers.zip"' ** Note : ** Ensure that all the form - data from the `Register AppBundle <#step-3-register-the-appbundle>` __ response is included in your request .
```

## Step 5 - Create an alias for the AppBundle

When you registered the AppBundle in step 2, it was registered as version 1 of the AppBundle. In this step, you create an alias named my_working_version to reference that version. You can think of the alias as a tag that points to a version of an AppBundle.

```
curl - X POST \ https : // developer . api . autodesk . com / da / us - east / v3 / appbundles / ListLayers / aliases \ - H 'Content-Type: application/json' - H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \ - d '{ "version": 1, "id": "my_working_version" }'
```

Note:

If you make changes to the AppBundle, some time later, you must register it as a new version and then upload it. You can then update the alias to point to the newer version
of the AppBundle. Consequently, endpoints referencing the AppBundle using the alias get access to the updated version of the AppBundle.

## Additional notes

### Notes on Engines

- Each AppBundle POST request specifies an engine on which the application runs. The following table shows the keywords to specify for the available AutoCAD engines.

- The active engine version aliases are:

Engine Description JSON in AppBundle post Autodesk.AutoCAD+24 AutoCAD 2021 âengineâ: âAutodesk.AutoCAD+24â Autodesk.AutoCAD+24_1 AutoCAD 2022 âengineâ: âAutodesk.AutoCAD+24_1â Autodesk.AutoCAD+24_2 AutoCAD 2023 âengineâ: âAutodesk.AutoCAD+24_2â Autodesk.AutoCAD+24_3 AutoCAD 2024 âengineâ: âAutodesk.AutoCAD+24_3â

Notes:

- For the most current list of engines use the operation listed here .

- If there is an error, refer the section on troubleshooting .

### Notes on CRX plug-ins

A CRX plug-in is a module that has been coded against the AcCoreMgd.dll instead of the AcMgd.dll , against which ARX plug-ins are coded. You can think of a CRX plug-in as an ARX plug-in that is designed to run against the core functionality of AutoCAD. To ensure that a CRX plug-in is restricted to core functionality, Visual Studio projects used to build CRX plug-ins are allowed to access only a subset of the libraries that ARX plug-ins can access. If you know how to build ARX plug-ins, you already have the knowledge required to build CRX plug-ins. Use the following links for more information:

- AutoCAD Developer Center Contains instructions on how to create ARX plug-ins.

- The AutoCAD 2013 Core Console A blog Post that provides an overview of the AutoCAD core console and CRX.

- Developing a CRX App A blog post that contains a table that lists the libraries a CRX module can access, as well as the libraries it canât.

- AutoCAD Scripting from the Core (AutoCAD Core Console) An Autodesk University class on writing scripts for the AutoCAD Core Console.
