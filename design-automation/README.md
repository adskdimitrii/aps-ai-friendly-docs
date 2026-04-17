# APS Design Automation Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Activities API
HTTP reference (13 files) covering full CRUD for Design Automation activities, aliases, and versions: [list](http-docs/http-activities-GET.md), [create](http-docs/http-activities-POST.md), [get](http-docs/http-activities-id-GET.md), [delete](http-docs/http-activities-id-DELETE.md); alias management ([list](http-docs/http-activities-id-aliases-GET.md), [create](http-docs/http-activities-id-aliases-POST.md), [get](http-docs/http-activities-id-aliases-aliasId-GET.md), [update](http-docs/http-activities-id-aliases-aliasId-PATCH.md), [delete](http-docs/http-activities-id-aliases-aliasId-DELETE.md)); version management ([list](http-docs/http-activities-id-versions-GET.md), [create](http-docs/http-activities-id-versions-POST.md), [get](http-docs/http-activities-id-versions-version-GET.md), [delete](http-docs/http-activities-id-versions-version-DELETE.md)).

### AppBundles API
HTTP reference (13 files) for uploading and managing application bundles — mirrors the Activities structure: [list](http-docs/http-appbundles-GET.md), [create](http-docs/http-appbundles-POST.md), [get](http-docs/http-appbundles-id-GET.md), [delete](http-docs/http-appbundles-id-DELETE.md); alias management ([list](http-docs/http-appbundles-id-aliases-GET.md), [create](http-docs/http-appbundles-id-aliases-POST.md), [get](http-docs/http-appbundles-id-aliases-aliasId-GET.md), [update](http-docs/http-appbundles-id-aliases-aliasId-PATCH.md), [delete](http-docs/http-appbundles-id-aliases-aliasId-DELETE.md)); version management ([list](http-docs/http-appbundles-id-versions-GET.md), [create](http-docs/http-appbundles-id-versions-POST.md), [get](http-docs/http-appbundles-id-versions-version-GET.md), [delete](http-docs/http-appbundles-id-versions-version-DELETE.md)).

### Work Items API
HTTP reference (7 files) for submitting and monitoring Design Automation jobs: [submit](http-docs/http-workitems-POST.md), [batch submit](http-docs/http-workitems-batch-POST.md), [combine](http-docs/http-workitems-combine-POST.md), [get status](http-docs/http-workitems-id-GET.md), [delete](http-docs/http-workitems-id-DELETE.md), [query by start time](http-docs/http-workitems-startAfterTime-GET.md), [post status callback](http-docs/http-workitems-status-POST.md).

### Engines, ForgeApps & Service Configuration
HTTP reference (9 files) for engine discovery, app registration, health checks, service limits, and shared items.

- [List Engines](http-docs/http-engines-GET.md), [Get Engine](http-docs/http-engines-id-GET.md)
- [Get ForgeApp](http-docs/http-forgeapps-id-GET.md), [Update ForgeApp](http-docs/http-forgeapps-id-PATCH.md), [Delete ForgeApp](http-docs/http-forgeapps-id-DELETE.md)
- [Engine Health Check](http-docs/http-health-engine-GET.md)
- [Get Service Limits](http-docs/http-servicelimits-owner-GET.md), [Update Service Limits](http-docs/http-servicelimits-owner-PUT.md)
- [List Shares](http-docs/http-shares-GET.md)

### Application Tutorials
Step-by-step how-to tutorials (40 files total) for five Autodesk engines. Each tutorial covers: authenticate → create nickname → upload AppBundle → publish Activity → prepare cloud storage → post Work Item → download results.

**3ds Max** (7 files): [About](how-to-docs/3dsmax-about_tutorial.md) | [Authenticate](how-to-docs/3dsmax-task1-authenticate.md) | [Create Nickname](how-to-docs/3dsmax-task2-create-nickname.md) | [Create Activity](how-to-docs/3dsmax-task3-create-activity.md) | [Manage Cloud Storage](how-to-docs/3dsmax-task4-manage-cloud-storage.md) | [Submit Work Item](how-to-docs/3dsmax-task5-submit-workitem.md) | [Download Results](how-to-docs/3dsmax-task6-download-results.md)

**AutoCAD** (8 files): [About](how-to-docs/autocad-about_this_tutorial.md) | [Authenticate](how-to-docs/autocad-task1-authenticate.md) | [Create Nickname](how-to-docs/autocad-task2-create-nickname.md) | [Upload AppBundle](how-to-docs/autocad-task3-upload-appbundle.md) | [Publish Activity](how-to-docs/autocad-task4-publish-activity.md) | [Prepare Cloud Storage](how-to-docs/autocad-task5-prepare_cloud_storage.md) | [Post Work Item](how-to-docs/autocad-task6-post-workitem.md) | [Download Results](how-to-docs/autocad-task7-download-results.md)

**Fusion 360** (7 files): [About](how-to-docs/fusion-about-this-tutorial.md) | [Authenticate](how-to-docs/fusion-task1-authenticate.md) | [Create Nickname](how-to-docs/fusion-task2-create-nickname.md) | [Upload AppBundle](how-to-docs/fusion-task3-upload-appbundle.md) | [Publish Activity](how-to-docs/fusion-task4-publish-activity.md) | [Post Work Item](how-to-docs/fusion-task5-post-workitem.md) | [Open Result in Fusion](how-to-docs/fusion-task6-open-result-in-fusion.md)

**Inventor** (8 files): [About](how-to-docs/inventor-about-this-tutorial.md) | [Authenticate](how-to-docs/inventor-task1-authenticate.md) | [Create Nickname](how-to-docs/inventor-task2-create-nickname.md) | [Upload AppBundle](how-to-docs/inventor-task3-upload-appbundle.md) | [Publish Activity](how-to-docs/inventor-task4-publish-activity.md) | [Prepare Cloud Storage](how-to-docs/inventor-task5-prepare_cloud_storage.md) | [Post Work Item](how-to-docs/inventor-task6-post-workitem.md) | [Download Results](how-to-docs/inventor-task7-download-results.md)

**Revit** (9 files — includes an extra step for converting an existing add-in): [About](how-to-docs/revit-about_this_tutorial.md) | [Convert Add-in](how-to-docs/revit-step1-convert-addin.md) | [Create Forge App](how-to-docs/revit-step2-create-forge-app.md) | [Create Nickname](how-to-docs/revit-step3-create-nickname.md) | [Publish AppBundle](how-to-docs/revit-step4-publish-appbundle.md) | [Publish Activity](how-to-docs/revit-step5-publish-activity.md) | [Prepare Cloud Storage](how-to-docs/revit-step6-prepare-cloud-storage.md) | [Post Work Item](how-to-docs/revit-step7-post-workitem.md) | [Download Results](how-to-docs/revit-step8-download-results.md)

### Common Guides
Shared reference (1 file) applicable across all engines.

- [Using On-Demand Inputs](how-to-docs/common-using-on-demand-inputs.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
