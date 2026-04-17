# APS AEC Data Model Friendly Docs

Documentation for the AEC Data Model API (GraphQL-based API for accessing BIM element data from Autodesk Construction Cloud projects).

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Getting Started

Prerequisite setup and orientation for the AEC Data Model API.

- [Before You Begin](how-to-docs/before_you_begin.md)

### Tutorial 1: Hubs, Projects & Element Navigation (4 files)

Step-by-step introduction to discovering hubs and projects, browsing folders, and querying elements by category.

- [Get Hubs](how-to-docs/tutorial01-gethubs.md)
- [Get Projects](how-to-docs/tutorial01-getprojects.md)
- [Elements by Category](how-to-docs/tutorial01-elementsbycategory.md)
- [Navigate Elements](how-to-docs/tutorial01-nav-elements.md)

### Tutorial 2: Advanced Queries (7 files)

Multi-part series covering distinct value queries, filtering strategies, and pagination patterns.

- [Distinct Values Query](how-to-docs/tutorial02-distinctvaluesquery.md)
- Tasks: [1a](how-to-docs/tutorial02-task1a.md) · [2a](how-to-docs/tutorial02-task2a.md) · [3a](how-to-docs/tutorial02-task3a.md) · [4a](how-to-docs/tutorial02-task4a.md) · [5a](how-to-docs/tutorial02-task5a.md) · [6a](how-to-docs/tutorial02-task6a.md)

### Extend Element Data — Custom Properties (7 files)

How-to guides for adding, updating, and removing custom properties on elements, including cost properties, category binding filters, and property definition lifecycle management.

- [Create Property Definition](how-to-docs/extend_element_data-create_property_definition.md)
- [Custom Property Elements](how-to-docs/extend_element_data-custom_property_elements.md)
- [Category Binding Filter Workflow](how-to-docs/extend_element_data-category_binding_filter_workflow.md)
- [Update Cost Property](how-to-docs/extend_element_data-update_cost_property.md)
- [Remove Cost Property](how-to-docs/extend_element_data-remove_cost_property.md)
- [Retrieve All Elements](how-to-docs/extend_element_data-retrieve_all_elements.md)
- [Additional Information](how-to-docs/extend_element_data-additional_information.md)

### Geometry (2 files)

Guides for querying and filtering model elements by geometric properties and axis origin.

- [Filter Elements by Origin](how-to-docs/geometry-filter-elements-by-origin.md)
- [Get Axis Origin Elements](how-to-docs/geometry-get-axis-origin-elements.md)

### Diff API (1 file)

Tutorial for comparing element and element group versions using the Diff API.

- [Diff API Tutorial](how-to-docs/diff_api-diff_api_tutorial.md)

### Revit Sync (1 file)

Guide for querying model synchronization data from Revit.

- [Query Sync Data](how-to-docs/revit_sync-query_sync_data.md)

### GraphQL API Reference — Queries (~39 files)

Full reference for all available GraphQL queries, covering element retrieval, element groups, folder/hub/project traversal, geometry data, property definitions, distinct value aggregation, and version diff queries.

Representative entries:
- [Elements by Element Group](reference-docs/queries-elementsbyelementgroup.md)
- [Elements by Project](reference-docs/queries-elementsbyproject.md)
- [Element Groups by Folder](reference-docs/queries-elementgroupsbyfolder.md)
- [Geometry Data by Element](reference-docs/queries-geometrydatabyelement.md)
- [Diff Element by Version with Latest](reference-docs/queries-diffelementbyversionwithlatest.md)
- [Property Definition Collections by Hub](reference-docs/queries-propertydefinitioncollectionsbyhub.md)
- [Distinct Property Values in Element Group by ID](reference-docs/queries-distinctpropertyvaluesinelementgroupbyid.md)
- 32 additional query reference files

### GraphQL API Reference — Object Types (~68 files)

Reference for all GraphQL return types, including elements, element groups, geometry primitives, property definitions, hubs, projects, folders, diff results, and pagination wrappers.

Representative entries:
- [Element](reference-docs/objects-element.md) · [Elements](reference-docs/objects-elements.md) · [ElementGroup](reference-docs/objects-elementgroup.md) · [ElementGroupVersion](reference-docs/objects-elementgroupversion.md)
- [GeometryDataOutput](reference-docs/objects-geometrydataoutput.md) · [GeometryPiece](reference-docs/objects-geometrypiece.md) · [GeometryInstance](reference-docs/objects-geometryinstance.md)
- [PropertyDefinition](reference-docs/objects-propertydefinition.md) · [PropertyDefinitionCollection](reference-docs/objects-propertydefinitioncollection.md)
- [Hub](reference-docs/objects-hub.md) · [Project](reference-docs/objects-project.md) · [Folder](reference-docs/objects-folder.md)
- ~58 additional object type reference files

### GraphQL API Reference — Input Types (~30 files)

Reference for all input types used in query arguments and mutations, covering element/group/geometry/property filters, extensibility inputs, pagination, and version filtering.

Representative entries:
- [ElementFilterInput](reference-docs/inputs-elementfilterinput.md)
- [ElementGroupFilterInput](reference-docs/inputs-elementgroupfilterinput.md)
- [GeometryComponentsFilterInput](reference-docs/inputs-geometrycomponentsfilterinput.md)
- [PropertyDefinitionFilterInput](reference-docs/inputs-propertydefinitionfilterinput.md)
- [PaginationInput](reference-docs/inputs-paginationinput.md)
- 25 additional input type reference files

### GraphQL Endpoint & Scalars

Reference for the GraphQL endpoint configuration and all custom scalar type definitions.

- [GraphQL Endpoint](reference-docs/graphqlendpoint.md)
- [Scalars](reference-docs/scalars.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
