# APS Model Derivative Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### HTTP API Reference — Translation Jobs

Submit translation jobs and check supported formats.

- [POST /job](http-docs/http-job-POST.md) — initiate a translation/derivative job
- [GET /formats](http-docs/http-formats-GET.md) — list supported input/output formats
- [POST /urn/references](http-docs/http-urn-references-POST.md) — set references for files with external dependencies

### HTTP API Reference — Manifest & Derivatives

Retrieve, download, and manage derivative outputs and manifests (5 files).

- [GET /urn/manifest](http-docs/http-urn-manifest-GET.md)
- [DELETE /urn/manifest](http-docs/http-urn-manifest-DELETE.md)
- [GET /urn/manifest/:derivativeUrn](http-docs/http-urn-manifest-derivativeurn-GET.md)
- [HEAD /urn/manifest/:derivativeUrn](http-docs/http-urn-manifest-derivativeurn-HEAD.md)
- [GET /urn/manifest/:derivativeUrn/signedcookies](http-docs/http-urn-manifest-derivativeUrn-signedcookies-GET.md)

### HTTP API Reference — Metadata & Properties

Query model structure, geometry metadata, and object properties (4 files).

- [GET /urn/metadata](http-docs/http-urn-metadata-GET.md)
- [GET /urn/metadata/:guid](http-docs/http-urn-metadata-guid-GET.md)
- [GET /urn/metadata/:guid/properties](http-docs/http-urn-metadata-guid-properties-GET.md)
- [POST /urn/metadata/:guid/properties/query](http-docs/http-urn-metadata-guid-properties-query-POST.md)

### HTTP API Reference — Thumbnails

- [GET /urn/thumbnail](http-docs/http-urn-thumbnail-GET.md) — retrieve a thumbnail image for a translated model

### Tutorial: Prepare a File for the Viewer (5 files)

End-to-end walkthrough uploading a source file to OSS, translating it, and displaying it in the viewer.

- [About](how-to-docs/prep-file4viewer-about-this-tutorial.md)
- [Task 1 — Authenticate](how-to-docs/prep-file4viewer-task1-authenticate.md)
- [Task 2 — Upload to OSS](how-to-docs/prep-file4viewer-task2-upload_source_file_to_oss.md)
- [Task 3 — Translate](how-to-docs/prep-file4viewer-task3-translate-source-file.md)
- [Task 4 — Display Model](how-to-docs/prep-file4viewer-task4-display_model.md)

### Tutorial: Prepare Room Info for the Viewer (5 files)

Similar flow focused on extracting and displaying room information.

- [About](how-to-docs/prep-roominfo4viewer-about-this-tutorial.md)
- [Task 3 — Translate](how-to-docs/prep-roominfo4viewer-task3-translate-source-file.md)
- [Task 4 — Display Model](how-to-docs/prep-roominfo4viewer-task4-display_model.md) + 2 more task files

### Tutorial: Translate a File with Cross-References (5 files)

Covers handling files that reference external assets, with STL download as output.

- [About](how-to-docs/translate-source-file-containing-xref-about-this-tutorial.md)
- [Task 3 — Translate](how-to-docs/translate-source-file-containing-xref-task3-translate-source-file.md)
- [Task 4 — Download STL](how-to-docs/translate-source-file-containing-xref-task4-download-stl-file.md) + 2 more task files

### Tutorial: Translate to OBJ (5 files)

Upload a source file, translate to OBJ format, and download the result.

- [About](how-to-docs/translate-to-obj-about-this-tutorial.md)
- [Task 4 — Download OBJ](how-to-docs/translate-to-obj-task4-download-obj-file.md) + 3 more task files

### Tutorial: Translate ZIP to STL (5 files)

Package a model as a ZIP, translate it, and download an STL derivative.

- [About](how-to-docs/translate-zip-to-stl-about-this-tutorial.md)
- [Task 4 — Download STL](how-to-docs/translate-zip-to-stl-task4-download-stl-file.md) + 3 more task files

### Tutorial: Extract Geometry from a Source File (6 files)

Five-task tutorial covering upload, translation, metadata extraction, and geometry extraction.

- [About](how-to-docs/xtract-geometry-from-source-file-about-this-tutorial.md)
- [Task 4 — Extract Metadata](how-to-docs/xtract-geometry-from-source-file-task4-extract_metadata.md)
- [Task 5 — Extract Geometry](how-to-docs/xtract-geometry-from-source-file-task5-extract_geometry.md) + 3 more task files

### Tutorial: Extract Metadata (5 files)

Focused walkthrough on pulling model metadata after translation.

- [About](how-to-docs/xtract-metadata-about-this-tutorial.md)
- [Task 4 — Extract Metadata](how-to-docs/xtract-metadata-task4-extract_metadata.md) + 3 more task files
<!-- GENERATED:CONTENT_SUMMARY:END -->
