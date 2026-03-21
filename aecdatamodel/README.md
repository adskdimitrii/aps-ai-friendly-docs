# APS AEC Data Model Friendly Docs

Documentation for the AEC Data Model API (GraphQL-based API for accessing BIM element data from Autodesk Construction Cloud projects).

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Getting Started
Prerequisites and setup before working with the API. See [Before You Begin](how-to-docs/before_you_begin.md) for onboarding steps and OAuth requirements.

### Tutorial 1: Getting Started (~4 files)
Step-by-step walkthrough for navigating the AEC Data Model from hubs down to elements.
- [Get Hubs](how-to-docs/tutorial01-gethubs.md) — query for available hubs
- [Get Projects](how-to-docs/tutorial01-getprojects.md) — list projects within a hub
- [Navigate to ElementGroups within a Project](how-to-docs/tutorial01-nav-elements.md) — traverse the element group hierarchy
- [Get Elements from a Category](how-to-docs/tutorial01-elementsbycategory.md) — filter elements by category

### Tutorial 2: Advanced Queries (~7 files)
More complex query patterns including filtering, versioning, and property-based searches.
- [Get ElementGroups Based on Metadata](how-to-docs/tutorial02-task1a.md) — filter element groups using metadata properties
- [Get Versions of an ElementGroup](how-to-docs/tutorial02-task2a.md) — access version history
- [Get Element Instances of a Particular Type](how-to-docs/tutorial02-task3a.md)
- [Get Element Instances in a Category by Version](how-to-docs/tutorial02-task4a.md)
- [Get Project Elements with Specific Properties](how-to-docs/tutorial02-task5a.md)
- [Get Elements by Using Instances or Reference](how-to-docs/tutorial02-task6a.md)
- [Get Distinct Values of Properties](how-to-docs/tutorial02-distinctvaluesquery.md)

### Reference: GraphQL Endpoint
- [GraphQL Endpoint](reference-docs/graphqlendpoint.md) — endpoint URL, authentication headers, and request format for the AEC Data Model GraphQL API

### Reference: Queries (~24 files)
All top-level GraphQL queries available in the API.
- **Hubs & Projects**: [hubs](reference-docs/queries-hubs.md), [hub](reference-docs/queries-hub.md), [projects](reference-docs/queries-projects.md), [project](reference-docs/queries-project.md)
- **Folders**: [foldersByProject](reference-docs/queries-foldersbyproject.md), [foldersByFolder](reference-docs/queries-foldersbyfolder.md), [folder](reference-docs/queries-folder.md)
- **ElementGroups**: [elementGroupsByHub](reference-docs/queries-elementgroupsbyhub.md), [elementGroupsByProject](reference-docs/queries-elementgroupsbyproject.md), [elementGroupsByFolder](reference-docs/queries-elementgroupsbyfolder.md), [elementGroupsByFolderAndSubFolders](reference-docs/queries-elementgroupsbyfolderandsubfolders.md), [elementGroupAtTip](reference-docs/queries-elementgroupattip.md), [elementGroupByVersionNumber](reference-docs/queries-elementgroupbyversionnumber.md), [elementGroupExtractionStatus](reference-docs/queries-elementgroupextractionstatus.md), [elementGroupExtractionStatusAtTip](reference-docs/queries-elementgroupextractionstatusattip.md)
- **Elements**: [elementsByHub](reference-docs/queries-elementsbyhub.md), [elementsByProject](reference-docs/queries-elementsbyproject.md), [elementsByFolder](reference-docs/queries-elementsbyfolder.md), [elementsByElementGroup](reference-docs/queries-elementsbyelementgroup.md), [elementsByElementGroupAtVersion](reference-docs/queries-elementsbyelementgroupatversion.md), [elementAtTip](reference-docs/queries-elementattip.md)
- **Properties**: [propertyDefinitionsByElementGroup](reference-docs/queries-propertydefinitionsbyelementgroup.md), [distinctPropertyValuesInElementGroupById](reference-docs/queries-distinctpropertyvaluesinelementgroupbyid.md), [distinctPropertyValuesInElementGroupByName](reference-docs/queries-distinctpropertyvaluesinelementgroupbyname.md)

### Reference: Objects (~30 files)
GraphQL object types returned by the API.
- **Core**: [ElementGroup](reference-docs/objects-elementgroup.md), [ElementGroups](reference-docs/objects-elementgroups.md), [Element](reference-docs/objects-element.md), [Elements](reference-docs/objects-elements.md)
- **Versions**: [ElementGroupVersion](reference-docs/objects-elementgroupversion.md), [ElementGroupVersions](reference-docs/objects-elementgroupversions.md), [ElementGroupVersionHistory](reference-docs/objects-elementgroupversionhistory.md), [ExtractionStatus](reference-docs/objects-extractionstatus.md), [ElementGroupExtractionStatus](reference-docs/objects-elementgroupextractionstatus.md)
- **Identifiers**: [ElementGroupAlternativeIdentifiers](reference-docs/objects-elementgroupalternativeidentifiers.md), [ElementAlternativeIdentifiers](reference-docs/objects-elementalternativeidentifiers.md), [ProjectAlternativeIdentifiers](reference-docs/objects-projectalternativeidentifiers.md)
- **Hub/Project/Folder**: [Hub](reference-docs/objects-hub.md), [Hubs](reference-docs/objects-hubs.md), [Project](reference-docs/objects-project.md), [Projects](reference-docs/objects-projects.md), [Folder](reference-docs/objects-folder.md), [Folders](reference-docs/objects-folders.md), [User](reference-docs/objects-user.md)
- **Properties**: [Property](reference-docs/objects-property.md), [Properties](reference-docs/objects-properties.md), [PropertyDefinition](reference-docs/objects-propertydefinition.md), [PropertyDefinitions](reference-docs/objects-propertydefinitions.md), [PropertyDefinitionCollection](reference-docs/objects-propertydefinitioncollection.md), [ReferenceProperty](reference-docs/objects-referenceproperty.md), [ReferenceProperties](reference-docs/objects-referenceproperties.md), [DistinctPropertyValue](reference-docs/objects-distinctpropertyvalue.md), [DistinctPropertyValues](reference-docs/objects-distinctpropertyvalues.md), [DistinctPropertyValuesCollection](reference-docs/objects-distinctpropertyvaluescollection.md)
- **Other**: [Pagination](reference-docs/objects-pagination.md), [Comparators](reference-docs/objects-comparators.md)

### Reference: Inputs (~13 files)
Input types used as query arguments and filters.
- [ElementFilterInput](reference-docs/inputs-elementfilterinput.md), [ElementGroupFilterInput](reference-docs/inputs-elementgroupfilterinput.md), [ElementGroupVersionFilterInput](reference-docs/inputs-elementgroupversionfilterinput.md), [ElementPropertyFilterInput](reference-docs/inputs-elementpropertyfilterinput.md), [ElementReferenceFilterInput](reference-docs/inputs-elementreferencefilterinput.md)
- [FolderFilterInput](reference-docs/inputs-folderfilterinput.md), [HubFilterInput](reference-docs/inputs-hubfilterinput.md), [ProjectFilterInput](reference-docs/inputs-projectfilterinput.md), [PaginationInput](reference-docs/inputs-paginationinput.md)
- [PropertyFilterInput](reference-docs/inputs-propertyfilterinput.md), [PropertyDefinitionFilterInput](reference-docs/inputs-propertydefinitionfilterinput.md), [ReferencePropertyFilterInput](reference-docs/inputs-referencepropertyfilterinput.md), [ValueComparatorInput](reference-docs/inputs-valuecomparatorinput.md)

### Reference: Scalars
- [Scalars](reference-docs/scalars.md) — custom scalar types used in the API schema
<!-- GENERATED:CONTENT_SUMMARY:END -->
