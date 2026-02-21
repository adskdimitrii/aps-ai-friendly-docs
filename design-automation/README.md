# APS Design Automation Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Activities API (13 files)

Full CRUD operations for managing Design Automation activities, including versioning and alias management. Activities define the actions that engines can perform on input files.

- [List Activities](http-docs/http-activities-GET.md) | [Create Activity](http-docs/http-activities-POST.md) | [Get Activity](http-docs/http-activities-id-GET.md) | [Delete Activity](http-docs/http-activities-id-DELETE.md)
- Aliases: [List](http-docs/http-activities-id-aliases-GET.md) | [Create](http-docs/http-activities-id-aliases-POST.md) | [Get](http-docs/http-activities-id-aliases-aliasId-GET.md) | [Update](http-docs/http-activities-id-aliases-aliasId-PATCH.md) | [Delete](http-docs/http-activities-id-aliases-aliasId-DELETE.md)
- Versions: [List](http-docs/http-activities-id-versions-GET.md) | [Create](http-docs/http-activities-id-versions-POST.md) | [Get](http-docs/http-activities-id-versions-version-GET.md) | [Delete](http-docs/http-activities-id-versions-version-DELETE.md)

### AppBundles API (13 files)

Full CRUD for custom application bundles (plugins) uploaded to Design Automation, with the same alias and versioning structure as Activities.

- [List AppBundles](http-docs/http-appbundles-GET.md) | [Create AppBundle](http-docs/http-appbundles-POST.md) | [Get AppBundle](http-docs/http-appbundles-id-GET.md) | [Delete AppBundle](http-docs/http-appbundles-id-DELETE.md)
- Aliases: [List](http-docs/http-appbundles-id-aliases-GET.md) | [Create](http-docs/http-appbundles-id-aliases-POST.md) | [Get](http-docs/http-appbundles-id-aliases-aliasId-GET.md) | [Update](http-docs/http-appbundles-id-aliases-aliasId-PATCH.md) | [Delete](http-docs/http-appbundles-id-aliases-aliasId-DELETE.md)
- Versions: [List](http-docs/http-appbundles-id-versions-GET.md) | [Create](http-docs/http-appbundles-id-versions-POST.md) | [Get](http-docs/http-appbundles-id-versions-version-GET.md) | [Delete](http-docs/http-appbundles-id-versions-version-DELETE.md)

### WorkItems API (7 files)

Endpoints for submitting and monitoring jobs. WorkItems tie an Activity to specific inputs/outputs and execute the processing.

- [Submit WorkItem](http-docs/http-workitems-POST.md) | [Get WorkItem Status](http-docs/http-workitems-id-GET.md) | [Delete WorkItem](http-docs/http-workitems-id-DELETE.md)
- [Batch Submit](http-docs/http-workitems-batch-POST.md) | [Combine WorkItems](http-docs/http-workitems-combine-POST.md)
- [List by Start Time](http-docs/http-workitems-startAfterTime-GET.md) | [Check Status](http-docs/http-workitems-status-POST.md)

### Engines, Health & Service Configuration (6 files)

Engine discovery, health checks, service limits, nicknames, and shared resources.

- Engines: [List Engines](http-docs/http-engines-GET.md) | [Get Engine](http-docs/http-engines-id-GET.md) | [Engine Health](http-docs/http-health-engine-GET.md)
- Nicknames (ForgeApps): [Get](http-docs/http-forgeapps-id-GET.md) | [Set](http-docs/http-forgeapps-id-PATCH.md) | [Delete](http-docs/http-forgeapps-id-DELETE.md)
- [Service Limits - Get](http-docs/http-servicelimits-owner-GET.md) | [Service Limits - Set](http-docs/http-servicelimits-owner-PUT.md) | [List Shares](http-docs/http-shares-GET.md)

### AutoCAD Tutorial (7 files)

Step-by-step guide for running a Design Automation workflow with the AutoCAD engine: authentication, nickname creation, AppBundle upload, Activity publishing, cloud storage prep, WorkItem submission, and downloading results.

- [About This Tutorial](how-to-docs/autocad-about_this_tutorial.md) | [Authenticate](how-to-docs/autocad-task1-authenticate.md) | [Upload AppBundle](how-to-docs/autocad-task3-upload-appbundle.md) | [Post WorkItem](how-to-docs/autocad-task6-post-workitem.md) | [Download Results](how-to-docs/autocad-task7-download-results.md) (+2 more)

### Revit Tutorial (8 files)

End-to-end guide for converting an existing Revit add-in to run on Design Automation, including Forge app creation, AppBundle/Activity publishing, and job execution.

- [About This Tutorial](how-to-docs/revit-about_this_tutorial.md) | [Convert Add-in](how-to-docs/revit-step1-convert-addin.md) | [Publish AppBundle](how-to-docs/revit-step4-publish-appbundle.md) | [Post WorkItem](how-to-docs/revit-step7-post-workitem.md) | [Download Results](how-to-docs/revit-step8-download-results.md) (+3 more)

### Inventor Tutorial (7 files)

Complete walkthrough for the Inventor engine covering the standard workflow: authenticate, set nickname, upload AppBundle, publish Activity, prepare storage, submit WorkItem, and retrieve results.

- [About This Tutorial](how-to-docs/inventor-about-this-tutorial.md) | [Authenticate](how-to-docs/inventor-task1-authenticate.md) | [Upload AppBundle](how-to-docs/inventor-task3-upload-appbundle.md) | [Post WorkItem](how-to-docs/inventor-task6-post-workitem.md) | [Download Results](how-to-docs/inventor-task7-download-results.md) (+2 more)

### 3ds Max Tutorial (6 files)

Tutorial for running Design Automation jobs with the 3ds Max engine. Unlike other tutorials, this one creates an Activity directly (no AppBundle upload step).

- [About This Tutorial](how-to-docs/3dsmax-about_tutorial.md) | [Authenticate](how-to-docs/3dsmax-task1-authenticate.md) | [Create Activity](how-to-docs/3dsmax-task3-create-activity.md) | [Submit WorkItem](how-to-docs/3dsmax-task5-submit-workitem.md) | [Download Results](how-to-docs/3dsmax-task6-download-results.md) (+1 more)

### Fusion Tutorial (6 files)

Guide for the Fusion engine workflow, ending with opening results directly in Fusion rather than downloading files.

- [About This Tutorial](how-to-docs/fusion-about-this-tutorial.md) | [Authenticate](how-to-docs/fusion-task1-authenticate.md) | [Upload AppBundle](how-to-docs/fusion-task3-upload-appbundle.md) | [Post WorkItem](how-to-docs/fusion-task5-post-workitem.md) | [Open Result in Fusion](how-to-docs/fusion-task6-open-result-in-fusion.md) (+1 more)

### Common How-To (1 file)

- [Using On-Demand Inputs](how-to-docs/common-using-on-demand-inputs.md) — How to use on-demand (callback) inputs with WorkItems.
<!-- GENERATED:CONTENT_SUMMARY:END -->
