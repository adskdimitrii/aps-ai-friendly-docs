# About this Walkthrough

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/revit/about_this_tutorial/

---

# About this Walkthrough

This walkthrough guides you through the process of executing a Revit add-in on the Automation Service.
It doesnât teach you how to create a Revit add-in. Instead, it limits itself teaching you how to run a Revit add-in on the Automation Service.
For instructions on how to create Revit add-ins, visit the Revit Developer Center .

Revit add-ins are typically designed to interact with the Revit User Interface (UI). However, no user interaction is possible on the Automation Service.
Before you execute an add-in on the Automation Service, you must strip it of all references to the UI.
Task 1 of this walkthrough walks you through converting a Revit add-in to an Automation API ready add-in.
It requires you to modify C# code. If you are not proficient in C#, you can download the Automation API ready add-in DeleteWalls.dll from here , and start from Task 2.

## Postman walkthrough

Postman is a popular tool that provides an easy-to-use interface to send HTTP requests.
The Postman Collection at https://github.com/autodesk-platform-services/aps-tutorial-postman/tree/master/DA4Revit collates all the HTTP requests used in this walkthrough.
If you are familiar with Postman, you can import this Postman Collection and use Postman to send requests instead of cURL.

On the Postman Collection, requests are grouped by task. The group has the same name as the corresponding task in the walkthrough.

Task 1 is performed exclusively on Visual Studio. It does not send any requests to APS. Because Postman deals only with requests, there is no Task 1 in the Postman Collection.

Similarly, requests are named such that they have the same names as the corresponding step within the task.

You can install Postman from here.

You can learn how to install and use Postman from here.
