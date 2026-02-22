# APS Model Derivative Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Viewer Preparation Tutorials

Step-by-step guides for uploading source files to OSS, translating them, and displaying models in the APS Viewer. Two tutorial series, each covering authentication, upload, translation, and display steps (9 files total).

- [About: Prepare File for Viewer](how-to-docs/prep-file4viewer-about-this-tutorial.md)
- [Task 3: Translate Source File](how-to-docs/prep-file4viewer-task3-translate-source-file.md)
- [Task 4: Display Model](how-to-docs/prep-file4viewer-task4-display_model.md)
- [About: Prepare Room Info for Viewer](how-to-docs/prep-roominfo4viewer-about-this-tutorial.md)
- [Task 4: Display Model (Room Info)](how-to-docs/prep-roominfo4viewer-task4-display_model.md)
- Plus 4 additional task files across both series.

### Format Translation Tutorials

Tutorials covering translation of files to specific output formats (OBJ, STL) and handling files with external references (xrefs). Each series walks through authentication, OSS upload, translation job submission, and download (13 files total).

- [About: Translate to OBJ](how-to-docs/translate-to-obj-about-this-tutorial.md)
- [Task 4: Download OBJ File](how-to-docs/translate-to-obj-task4-download-obj-file.md)
- [About: Translate ZIP to STL](how-to-docs/translate-zip-to-stl-about-this-tutorial.md)
- [Task 4: Download STL File](how-to-docs/translate-zip-to-stl-task4-download-stl-file.md)
- [About: Translate File with Xrefs](how-to-docs/translate-source-file-containing-xref-about-this-tutorial.md)
- [Task 4: Download STL File (Xref)](how-to-docs/translate-source-file-containing-xref-task4-download-stl-file.md)
- Plus 7 additional task files across the three series.

### Data Extraction Tutorials

End-to-end tutorials for extracting structured data (metadata, geometry) from translated source files. Covers geometry extraction in 5 tasks and metadata extraction in 4 tasks (14 files total).

- [About: Extract Geometry from Source File](how-to-docs/xtract-geometry-from-source-file-about-this-tutorial.md)
- [Task 4: Extract Metadata](how-to-docs/xtract-geometry-from-source-file-task4-extract_metadata.md)
- [Task 5: Extract Geometry](how-to-docs/xtract-geometry-from-source-file-task5-extract_geometry.md)
- [About: Extract Metadata](how-to-docs/xtract-metadata-about-this-tutorial.md)
- [Task 4: Extract Metadata](how-to-docs/xtract-metadata-task4-extract_metadata.md)
- Plus 9 additional task files across both series.

### Translation & Job Submission API

HTTP reference for submitting translation jobs, querying supported output formats, and setting references for files with external dependencies (3 files).

- [POST /job](http-docs/http-job-POST.md) — Submit a translation job
- [GET /formats](http-docs/http-formats-GET.md) — List supported output formats
- [POST /{urn}/references](http-docs/http-urn-references-POST.md) — Set references for xref-based files

### Manifest & Derivatives API

HTTP reference for retrieving, deleting, and downloading translation manifests and derivative files, including signed cookie access for streaming (6 files).

- [GET /{urn}/manifest](http-docs/http-urn-manifest-GET.md) — Retrieve translation manifest
- [DELETE /{urn}/manifest](http-docs/http-urn-manifest-DELETE.md) — Delete manifest and derivatives
- [GET /{urn}/manifest/{derivativeUrn}](http-docs/http-urn-manifest-derivativeurn-GET.md) — Download a specific derivative
- [HEAD /{urn}/manifest/{derivativeUrn}](http-docs/http-urn-manifest-derivativeurn-HEAD.md) — Check derivative existence
- [GET /{urn}/manifest/{derivativeUrn}/signedcookies](http-docs/http-urn-manifest-derivativeUrn-signedcookies-GET.md) — Get signed cookies for derivative access

### Metadata & Thumbnail API

HTTP reference for querying model metadata, object hierarchies, properties, and fetching model thumbnails (5 files).

- [GET /{urn}/metadata](http-docs/http-urn-metadata-GET.md) — List model views (GUIDs)
- [GET /{urn}/metadata/{guid}](http-docs/http-urn-metadata-guid-GET.md) — Get object tree for a view
- [GET /{urn}/metadata/{guid}/properties](http-docs/http-urn-metadata-guid-properties-GET.md) — Get object properties
- [POST /{urn}/metadata/{guid}/properties:query](http-docs/http-urn-metadata-guid-properties-query-POST.md) — Query properties with filters
- [GET /{urn}/thumbnail](http-docs/http-urn-thumbnail-GET.md) — Retrieve model thumbnail
<!-- GENERATED:CONTENT_SUMMARY:END -->
