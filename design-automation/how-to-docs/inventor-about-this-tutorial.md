# About this Walkthrough

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/inventor/about-this-tutorial/

---

# About this Walkthrough

This walkthrough guides you through the process of loading an Inventor add-in and resizing an Inventor part or assembly. It doesnât teach you how to create Inventor add-ins. Instead, it points you to resources that can teach you how to create them (See [Task 3](inventor-task3-upload-appbundle.md)).

This walkthrough uses [cURL](https://curl.haxx.se/) to send HTTP requests to APS. cURL is able to clearly show request and response information. It, however, is not the best tool to demonstrate a workflow by sending a series of HTTP requests to APS.
We have hence provided a Postman based walkthrough to make it easier for you to send requests to APS.

## [Postman walkthrough](#postman-walkthrough)

[Postman](https://www.getpostman.com/) is a popular tool that provides an easy-to-use interface to send HTTP requests. [The Postman walkthrough](https://github.com/autodesk-platform-services/aps-tutorial-postman/tree/master/DA4Inventor) comes with a collection of pre-populated HTTP requests that you can modify.
This gives you the ability to experiment without having to write a single line of code.

On the Postman Collection, requests are grouped by task. The group has the same name as the corresponding task in the cURL walkthrough on the APS developer portal.

![../../../../_images/aps_portal_2_inventor_postman_menu_01.png](../../../../_images/aps_portal_2_inventor_postman_menu_01.png)

Similarly, requests are named such that they have the same names as the corresponding step in the cURL walkthrough on the APS developer portal.

![../../../../_images/aps_portal_2_inventor_postman_menu_02.png](../../../../_images/aps_portal_2_inventor_postman_menu_02.png)

## [Additional resources for C# programmers](#additional-resources-for-c-programmers)

A video of a demonstration covering content similar to that of this walkthrough is available at <https://www.autodesk.com/autodesk-university/class/Getting-Started-Design-Automation-Inventor-Forge-2019#video>. If you are a C# programmer, we recommend that you watch this video.

After you follow the cURL or Postman walkthrough, and you have been introduced to the WorkItem creation and WorkItem execution workflow, you can look at [this Visual Studio extension](https://marketplace.visualstudio.com/items?itemName=Autodesk.DesignAutomation2).
