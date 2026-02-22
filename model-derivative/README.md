# APS Model Derivative Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Tutorial: Preparing Files for the Viewer

Step-by-step guides for uploading source files to OSS, translating them, and displaying the result in the APS Viewer. Covers two variants: standard model viewing and room/space information extraction.

- [About: Prepare File for Viewer](how-to-docs/prep-file4viewer-about-this-tutorial.md) — 5-task tutorial ([Task 1: Auth](how-to-docs/prep-file4viewer-task1-authenticate.md), [Task 2: Upload](how-to-docs/prep-file4viewer-task2-upload_source_file_to_oss.md), [Task 3: Translate](how-to-docs/prep-file4viewer-task3-translate-source-file.md), [Task 4: Display](how-to-docs/prep-file4viewer-task4-display_model.md))
- [About: Prepare Room Info for Viewer](how-to-docs/prep-roominfo4viewer-about-this-tutorial.md) — 4-task tutorial covering the same workflow with room data focus ([Task 3: Translate](how-to-docs/prep-roominfo4viewer-task3-translate-source-file.md), [Task 4: Display](how-to-docs/prep-roominfo4viewer-task4-display_model.md))

### Tutorial: File Translation

End-to-end guides for translating source files into specific output formats, including handling of external references (XREFs) and ZIP packages.

- [About: Translate File with XREFs](how-to-docs/translate-source-file-containing-xref-about-this-tutorial.md) — 4-task tutorial; output is STL ([Task 3: Translate](how-to-docs/translate-source-file-containing-xref-task3-translate-source-file.md), [Task 4: Download STL](how-to-docs/translate-source-file-containing-xref-task4-download-stl-file.md))
- [About: Translate to OBJ](how-to-docs/translate-to-obj-about-this-tutorial.md) — 4-task tutorial for OBJ output ([Task 3: Translate](how-to-docs/translate-to-obj-task3-translate-source-file.md), [Task 4: Download OBJ](how-to-docs/translate-to-obj-task4-download-obj-file.md))
- [About: Translate ZIP to STL](how-to-docs/translate-zip-to-stl-about-this-tutorial.md) — 4-task tutorial for ZIP package → STL ([Task 3: Translate](how-to-docs/translate-zip-to-stl-task3-translate-source-file.md), [Task 4: Download STL](how-to-docs/translate-zip-to-stl-task4-download-stl-file.md))

### Tutorial: Metadata & Geometry Extraction

Guides for extracting structured data (metadata, properties, geometry) from translated source files.

- [About: Extract Metadata](how-to-docs/xtract-metadata-about-this-tutorial.md) — 4-task tutorial ([Task 3: Translate](how-to-docs/xtract-metadata-task3-translate-source-file.md), [Task 4: Extract Metadata](how-to-docs/xtract-metadata-task4-extract_metadata.md))
- [About: Extract Geometry](how-to-docs/xtract-geometry-from-source-file-about-this-tutorial.md) — 5-task tutorial extending metadata extraction to geometry data ([Task 4: Extract Metadata](how-to-docs/xtract-geometry-from-source-file-task4-extract_metadata.md), [Task 5: Extract Geometry](how-to-docs/xtract-geometry-from-source-file-task5-extract_geometry.md))

### API: Translation Jobs & Formats

Endpoints for initiating translation jobs, setting file references, and querying supported output formats.

- [POST /job](http-docs/http-job-POST.md) — Submit a translation job
- [POST /urn/references](http-docs/http-urn-references-POST.md) — Register external file references (XREFs) before translating
- [GET /formats](http-docs/http-formats-GET.md) — List all supported input/output format combinations

### API: Manifest & Derivatives

Endpoints for retrieving, downloading, and deleting the translation manifest and its derivative files.

- [GET /urn/manifest](http-docs/http-urn-manifest-GET.md) — Retrieve the manifest for a translated URN
- [DELETE /urn/manifest](http-docs/http-urn-manifest-DELETE.md) — Delete a manifest and all its derivatives
- [GET /urn/manifest/:derivativeUrn](http-docs/http-urn-manifest-derivativeurn-GET.md) — Download a specific derivative file
- [HEAD /urn/manifest/:derivativeUrn](http-docs/http-urn-manifest-derivativeurn-HEAD.md) — Check derivative file headers
- [GET /urn/manifest/:derivativeUrn/signedcookies](http-docs/http-urn-manifest-derivativeUrn-signedcookies-GET.md) — Obtain signed cookies for large derivative downloads

### API: Metadata & Properties

Endpoints for querying model views, object metadata, and properties from a translated model.

- [GET /urn/metadata](http-docs/http-urn-metadata-GET.md) — List available model views (GUIDs)
- [GET /urn/metadata/:guid](http-docs/http-urn-metadata-guid-GET.md) — Retrieve the object tree for a view
- [GET /urn/metadata/:guid/properties](http-docs/http-urn-metadata-guid-properties-GET.md) — Get all object properties for a view
- [POST /urn/metadata/:guid/properties/query](http-docs/http-urn-metadata-guid-properties-query-POST.md) — Query/filter object properties

### API: Thumbnails

- [GET /urn/thumbnail](http-docs/http-urn-thumbnail-GET.md) — Retrieve a thumbnail image for a translated model
<!-- GENERATED:CONTENT_SUMMARY:END -->
