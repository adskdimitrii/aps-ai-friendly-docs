# Task 1 â Convert Revit Add-in to an Automation API Compatible Add-in

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/revit/step1-convert-addin/

---

# Task 1 â Convert Revit Add-in to an Automation API Compatible Add-in

This task converts an add-in that runs on Revit to an add-in that runs on the Automation Service.

Prerequisites for this task are:
> - [Visual Studio 2017 or Visual Studio 2019](https://visualstudio.microsoft.com/downloads/)
> - Revit 2018, Revit 2019, Revit 2020, Revit 2021, Revit 2022, Revit 2023 or Revit 2024: This is required to compile the changes into the add-in.
> - Basic knowledge of C#

By the end of this task you will know how to convert a regular Revit add-in to one that runs on the Automation Service.

## [Step 1 - Clone Git repository](#step-1-clone-git-repository)

Clone the [Git Repository for the DeleteWalls Sample](https://github.com/autodesk-platform-services/aps-auto-delete-walls), go to the folder named *Desktop_Version*, and open *DeleteWalls.sln* in Visual Studio.

The DeleteWalls Sample Git repository contains the source code for an add-in named DeleteWalls. DeleteWalls reads a *.rvt* file and produces another *.rvt* file with all the walls deleted.

The repository contains two folders for two different versions of DeleteWalls. The folder named *Desktop_Version* contains a C# project that produces a typical Revit add-in that runs only on Revit.
It does not run on the Automation Service. The folder named *Design-Automation_Version* contains the same project, modified to run on the Automation Service.
The objective of this task is to start with the C# project in *Desktop_Version* and end up with the project in *Design-Automation_Version*.

## [Step 2 - Repair references](#step-2-repair-references)

The C# project you cloned may expect to find *RevitAPI.dll* in a location that is different to where it resides on your computer. To eliminate the risk of a broken reference:

1. Find *RevitAPI.dll* in your Revit install location and note its location.
2. In Visual Studio, remove the reference to *RevitAPI.dll*.
3. Add a reference to *RevitAPI.dll*, pointing to the location you noted down earlier.

## [Step 3 - Add a package reference to the DesignAutomationBridge DLL](#step-3-add-a-package-reference-to-the-designautomationbridge-dll)

Autodesk provides a library that contains the functionality an add-in needs to interface with the Revit Automation Service.
This library is known as the Automation Service Bridge (formerly known as the Design Automation Bridge) and is distributed as a NuGet package at <https://www.nuget.org/packages/Autodesk.Forge.DesignAutomation.Revit>.

1. In Visual Studio, remove the reference to *RevitAPIUI.dll*.
2. Insert a package reference to the Automation Service Bridge (formerly known as the Design Automation Bridge) corresponding to the Revit version you want to run.

> Please refer [Microsoft Documentation](https://docs.microsoft.com/en-us/nuget/quickstart/install-and-use-a-package-in-visual-studio) for instructions.
>
>
> [|](#id1)**Tip:** When inserting the package reference using Visual Studio, search for `Autodesk.Forge.DesignAutomation.Revit` with the **Include prerelease** option selected.

## [Step 4 - Remove references to user interface elements](#step-4-remove-references-to-user-interface-elements)

Since there is no UI interaction on the Automation Service, you must remove all references to UI elements.

In the *.cs* file that implements your add-in (*DeleteWalls.cs* in this case):

1. Remove the `using` directive to the `Autodesk.Revit.UI` namespace and insert a `using` directive to the `DesignAutomationFramework` namespace in its place.

> ```
> using Autodesk.Revit.ApplicationServices;
> using Autodesk.Revit.DB;
> using DesignAutomationFramework;
>
> ```

2. In the file *DeleteWalls.addin*, change `AddIn Type` from `command` to `DBApplication`

> ```
> <?xml version="1.0" encoding="utf-8"?>
> <RevitAddIns>
> <AddIn Type="DBApplication">
> <Name>DeleteWalls</Name>
> <Assembly>.\DeleteWalls.dll</Assembly>
> <AddInId>d7fe1983-8f10-4983-98e2-c3cc332fc978</AddInId>
> <FullClassName>DeleteWalls.DeleteWallsApp</FullClassName>
> <Description>"Deletes Walls"</Description>
> <VendorId>Autodesk</VendorId>
> <VendorDescription>
> </VendorDescription>
> </AddIn>
> </RevitAddIns>
>
> ```
>
>
> Show More

**Notes:**
> Whenever you are converting a Revit add-in in general, make sure that you:
>
> - Remove references to `RevitAPIUI` or any code in the `Autodesk.Revit.UI` namespace. These functions are not available on the Automation Service and hence cannot be called.
> - Remove references to `WPF`, `Windows Forms`, or any other UI-based libraries.

## [Step 5 - Convert IExternalApplication or IExternalCommand to IExternalDBApplication](#step-5-convert-iexternalapplication-or-iexternalcommand-to-iexternaldbapplication)

Since there is no UI interaction on the Automation Service, you canât use the Revit UI to initiate commands.
In order to initiate commands with the Automation Service, you must implement `OnStartup` and `OnShutdown` in your add-in.
These functions receive a `ControlledApplication` instead of a `UIControlledApplication`. The functions return an `ExternalDBApplicationResult` object:

For this task, in `DeleteWalls.cs`, implement `OnStartup` and `OnShutdown` as shown in the following code block.

```
using Autodesk.Revit.ApplicationServices;
using Autodesk.Revit.DB;
using DesignAutomationFramework;
namespace DeleteWalls
{
   [Autodesk.Revit.Attributes.Regeneration(Autodesk.Revit.Attributes.RegenerationOption.Manual)]
   [Autodesk.Revit.Attributes.Transaction(Autodesk.Revit.Attributes.TransactionMode.Manual)]
   public class DeleteWallsApp : IExternalDBApplication
   {
      public ExternalDBApplicationResult OnStartup(Autodesk.Revit.ApplicationServices.ControlledApplication app)
      {
         return ExternalDBApplicationResult.Succeeded;
      }

      public ExternalDBApplicationResult OnShutdown(Autodesk.Revit.ApplicationServices.ControlledApplication app)
      {
         return ExternalDBApplicationResult.Succeeded;
      }

```

Show More

## [Step 6 - Add an event handler for DesignAutomationReady](#step-6-add-an-event-handler-for-designautomationready)

`DesignAutomationBridge` defines the event `DesignAutomationReadyEvent`. The Revit engine raises the `DesignAutomationReadyEvent` when itâs ready to run your add-in. The event handler is the entry point to your code.

1. Set the success/failure argument to `DesignAutomationReadyEventArgs.Succeeded` so that the Automation Service knows your code succeeded.

> ```
> public class DeleteWallsApp : IExternalDBApplication
> {
> public ExternalDBApplicationResult OnStartup(Autodesk.Revit.ApplicationServices.ControlledApplication app)
> {
> DesignAutomationBridge.DesignAutomationReadyEvent += HandleDesignAutomationReadyEvent;
> return ExternalDBApplicationResult.Succeeded;
> }
> public void HandleDesignAutomationReadyEvent(object sender, DesignAutomationReadyEventArgs e)
> {
> e.Succeeded = true;
> DeleteAllWalls(e.DesignAutomationData);
> }
>
> ```
>
>
> Show More

2. Modify `DeleteAllWalls` to accept `DesignAutomationData`.

> ```
> public static void DeleteAllWalls(DesignAutomationData data)
> {
> if (data == null) throw new ArgumentNullException(nameof(data));
>
> Application rvtApp = data.RevitApp;
> if (rvtApp == null) throw new InvalidDataException(nameof(rvtApp));
>
> string modelPath = data.FilePath;
> if (String.IsNullOrWhiteSpace(modelPath)) throw new InvalidDataException(nameof(modelPath));
>
> Document doc = data.RevitDoc;
> if (doc == null) throw new InvalidOperationException("Could not open document.");
>
> using (Transaction transaction = new Transaction(doc))
> {
> FilteredElementCollector col = new FilteredElementCollector(doc).OfClass(typeof(Wall));
> transaction.Start("Delete All Walls");
> doc.Delete(col.ToElementIds());
> transaction.Commit();
> }
>
> ModelPath path = ModelPathUtils.ConvertUserVisiblePathToModelPath("result.rvt");
> doc.SaveAs(path, new SaveAsOptions());
> }
>
> ```
>
>
> Show More

3. Delete the method `Execute`, which previously called `DeleteAllWalls`. This is no longer necessary.

During the execution of your add-in, all files you load from the disk or write to the disk must go into the Windows current working directory. In the Automation Service, write access is limited to the current working directory and its children.

## [Step 7 - Handle failures encountered by Revit](#step-7-handle-failures-encountered-by-revit)

When an add-in runs on Revit, the add-in uses the UI to communicate warnings and errors. Since there is no UI interaction on the Automation Service, you must use an alternate strategy to handle failures.

For this walkthrough, you will use the default error handler. You donât need to add any code to enable the default error handler because it comes by default with the Automation Service Bridge (formerly known as the Design Automation Bridge).
The default error handler suppresses warnings and resolves errors automatically by applying the default options. If resolution of an error fails, it rolls back the failed action.

For more information refer [Handling Revit Failures](/en/docs/design-automation/v3/tutorials/handling-failures) .

## [Step 8 - Build the add-in](#step-8-build-the-add-in)

- In Visual Studio, rebuild *DeleteWalls.dll*.

You should now have an Automation API compatible Revit add-in.

## [Additional notes](#additional-notes)
> - Use the [debug tool](https://github.com/autodesk-platform-services/aps-automation-csharp-revit.local.debug.tool) on GitHub to test an add-in designed for the Automation API locally. The [Readme file](https://github.com/autodesk-platform-services/aps-automation-csharp-revit.local.debug.tool/blob/master/README.md) in the GitHub repository provides instructions on how to test the add-in. You can also follow a [video tutorial](https://youtu.be/i0LJ9JOpKMQ) on how to use this tool on YouTube.
> - Your application cannot use the network or write to any files outside of the current working directory (or a child folder of the working directory). Restrictions for Revit on the Automation Service can be found [here](/en/docs/design-automation/v3/developers_guide/restrictions).
> - If step 8 fails, you can download an Automation API compatible version of *DeleteWalls.dll* from [here](https://github.com/autodesk-platform-services/aps-tutorial-postman/tree/master/DA4Revit/walkthrough_data) and continue with task 2.
