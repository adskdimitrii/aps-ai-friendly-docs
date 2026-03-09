# About this Walkthrough

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/autocad/about_this_tutorial/

---

# About this Walkthrough

This walkthrough guides you through the process of loading an AutoCAD CRX plug-in and running a custom command on a drawing file using the Automation API.
It doesnât teach you how to create an AutoCAD plug-in. We assume you already know how to create plug-ins or are able to obtain the required AutoCAD plug-ins.
The [additional notes section in Task 3](autocad-task3-upload-appbundle.md#additional-notes) provides links to resources that can teach you how to create AutoCAD plug-ins.

This walkthrough uses [cURL](https://curl.haxx.se/) to send HTTP requests to APS. cURL is able to clearly show request and response information. It, however, is not the best tool to demonstrate a workflow by sending a series of HTTP requests to APS.
So, we have created a Postman Collection so that you donât have to use cURL to try out the walkthrough.

## [Postman walkthrough](#postman-walkthrough)

[Postman](https://www.getpostman.com/) is a popular tool that provides an easy-to-use interface to send HTTP requests. The Postman Collection at <https://github.com/autodesk-platform-services/aps-tutorial-postman/tree/master/DA4ACAD> collates all the HTTP requests used in this walkthrough as a single workflow. If you are familiar with Postman, you can import this Postman Collection and use Postman to send requests to APS.

On the Postman Collection, requests are grouped by task. The group has the same name as the corresponding task in the cURL walkthrough.



Similarly, requests on Postman are named such that they have the same name as the corresponding step in the cURL walkthrough.



Download the Postman installer from [here.](https://www.getpostman.com/downloads/)

Get installation instructions from [here.](https://learning.getpostman.com/docs/postman/launching_postman/installation_and_updates/)
