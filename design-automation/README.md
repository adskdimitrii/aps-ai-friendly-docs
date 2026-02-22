# APS Design Automation Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Tutorial Walkthroughs by Application

Step-by-step guides for automating design workflows using Design Automation with five supported Autodesk applications. Each tutorial covers authentication, creating a nickname, uploading an AppBundle, publishing an Activity, managing cloud storage, submitting a WorkItem, and downloading results.

- **3ds Max** (7 files): [About](how-to-docs/3dsmax-about_tutorial.md) · [Authenticate](how-to-docs/3dsmax-task1-authenticate.md) · [Create Nickname](how-to-docs/3dsmax-task2-create-nickname.md) · [Create Activity](how-to-docs/3dsmax-task3-create-activity.md) · [Manage Cloud Storage](how-to-docs/3dsmax-task4-manage-cloud-storage.md) · [Submit WorkItem](how-to-docs/3dsmax-task5-submit-workitem.md) · [Download Results](how-to-docs/3dsmax-task6-download-results.md)
- **AutoCAD** (7 files): [About](how-to-docs/autocad-about_this_tutorial.md) · [Authenticate](how-to-docs/autocad-task1-authenticate.md) · [Upload AppBundle](how-to-docs/autocad-task3-upload-appbundle.md) · [Publish Activity](how-to-docs/autocad-task4-publish-activity.md) · [Post WorkItem](how-to-docs/autocad-task6-post-workitem.md) · [Download Results](how-to-docs/autocad-task7-download-results.md) · + 1 more
- **Fusion** (6 files): [About](how-to-docs/fusion-about-this-tutorial.md) · [Authenticate](how-to-docs/fusion-task1-authenticate.md) · [Upload AppBundle](how-to-docs/fusion-task3-upload-appbundle.md) · [Publish Activity](how-to-docs/fusion-task4-publish-activity.md) · [Post WorkItem](how-to-docs/fusion-task5-post-workitem.md) · [Open Result in Fusion](how-to-docs/fusion-task6-open-result-in-fusion.md)
- **Inventor** (7 files): [About](how-to-docs/inventor-about-this-tutorial.md) · [Authenticate](how-to-docs/inventor-task1-authenticate.md) · [Upload AppBundle](how-to-docs/inventor-task3-upload-appbundle.md) · [Publish Activity](how-to-docs/inventor-task4-publish-activity.md) · [Post WorkItem](how-to-docs/inventor-task6-post-workitem.md) · [Download Results](how-to-docs/inventor-task7-download-results.md) · + 1 more
- **Revit** (9 files): [About](how-to-docs/revit-about_this_tutorial.md) · [Convert Add-in](how-to-docs/revit-step1-convert-addin.md) · [Create Forge App](how-to-docs/revit-step2-create-forge-app.md) · [Publish AppBundle](how-to-docs/revit-step4-publish-appbundle.md) · [Publish Activity](how-to-docs/revit-step5-publish-activity.md) · [Post WorkItem](how-to-docs/revit-step7-post-workitem.md) · [Download Results](how-to-docs/revit-step8-download-results.md) · + 2 more

### Common How-To Guides

Shared concepts applicable across all application tutorials.

- [Using On-Demand Inputs](how-to-docs/common-using-on-demand-inputs.md)

### Activities API

HTTP reference docs for creating and managing Activities — the named, versioned operations that define what an engine should do. Covers full lifecycle including aliases and versioning (13 files).

- [List Activities](http-docs/http-activities-GET.md) · [Create Activity](http-docs/http-activities-POST.md) · [Get Activity](http-docs/http-activities-id-GET.md) · [Delete Activity](http-docs/http-activities-id-DELETE.md)
- Aliases: [List](http-docs/http-activities-id-aliases-GET.md) · [Create](http-docs/http-activities-id-aliases-POST.md) · [Get](http-docs/http-activities-id-aliases-aliasId-GET.md) · [Update](http-docs/http-activities-id-aliases-aliasId-PATCH.md) · [Delete](http-docs/http-activities-id-aliases-aliasId-DELETE.md)
- Versions: [List](http-docs/http-activities-id-versions-GET.md) · [Create](http-docs/http-activities-id-versions-POST.md) · [Get](http-docs/http-activities-id-versions-version-GET.md) · [Delete](http-docs/http-activities-id-versions-version-DELETE.md)

### AppBundles API

HTTP reference docs for uploading and managing AppBundles — packaged plugins or scripts deployed to an engine. Covers full lifecycle including aliases and versioning (13 files).

- [List AppBundles](http-docs/http-appbundles-GET.md) · [Create AppBundle](http-docs/http-appbundles-POST.md) · [Get AppBundle](http-docs/http-appbundles-id-GET.md) · [Delete AppBundle](http-docs/http-appbundles-id-DELETE.md)
- Aliases: [List](http-docs/http-appbundles-id-aliases-GET.md) · [Create](http-docs/http-appbundles-id-aliases-POST.md) · [Get](http-docs/http-appbundles-id-aliases-aliasId-GET.md) · [Update](http-docs/http-appbundles-id-aliases-aliasId-PATCH.md) · [Delete](http-docs/http-appbundles-id-aliases-aliasId-DELETE.md)
- Versions: [List](http-docs/http-appbundles-id-versions-GET.md) · [Create](http-docs/http-appbundles-id-versions-POST.md) · [Get](http-docs/http-appbundles-id-versions-version-GET.md) · [Delete](http-docs/http-appbundles-id-versions-version-DELETE.md)

### WorkItems API

HTTP reference docs for submitting and monitoring WorkItems — the individual job executions that run an Activity against input data (7 files).

- [Submit WorkItem](http-docs/http-workitems-POST.md) · [Batch Submit](http-docs/http-workitems-batch-POST.md) · [Combined Submit](http-docs/http-workitems-combine-POST.md)
- [Get WorkItem Status](http-docs/http-workitems-id-GET.md) · [Cancel WorkItem](http-docs/http-workitems-id-DELETE.md)
- [Get WorkItems by Time](http-docs/http-workitems-startAfterTime-GET.md) · [Check WorkItem Status (POST)](http-docs/http-workitems-status-POST.md)

### Engines, App Registration & Service Administration

HTTP reference docs for discovering available engines, managing the registered Forge app (nickname), monitoring service health, enforcing service limits, and listing shared resources (9 files).

- Engines: [List Engines](http-docs/http-engines-GET.md) · [Get Engine](http-docs/http-engines-id-GET.md) · [Engine Health](http-docs/http-health-engine-GET.md)
- Forge App: [Get App](http-docs/http-forgeapps-id-GET.md) · [Update App (Nickname)](http-docs/http-forgeapps-id-PATCH.md) · [Delete App](http-docs/http-forgeapps-id-DELETE.md)
- Service Limits: [Get Limits](http-docs/http-servicelimits-owner-GET.md) · [Set Limits](http-docs/http-servicelimits-owner-PUT.md)
- Shares: [List Shared Resources](http-docs/http-shares-GET.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
