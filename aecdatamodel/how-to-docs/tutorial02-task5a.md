# Get Project Elements with Specific Properties

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/tutorial02/task5a/

---

# Get Project Elements with Specific Properties

In this guide, you will learn how to retrieve elements in a project based on specific properties using the AEC Data Model Explorer. You will retrieve elements that match certain criteria, such as walls with a length rating greater than 10.

By the end of this guide, you will be able to:

- Fetch wall elements with a length greater than 10 from all elementGroups in a project and information like id and properties.
- Understand the options and fields in the documentation on the elements query, elements object, and Properties object.

You will use the following query in this guide:

| Type | Operation | Description |
| --- | --- | --- |
| Query | [elementsByProject](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elementsbyproject/) | Retrieves element in the given project, using additional RSQL filters if provided. |

## [Step 1: Request Elements Matching the Specified Classification Filter](#step-1-request-elements-matching-the-specified-classification-filter)

The [elementsByProject](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elementsbyproject/) query returns [Elements](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/elements/) object, which contains an array of Elements objects.

For this exercise, we request all elements instances with
:   - Elements id, name field, and properties.
    - Name and value fields in the properties object.

1. In [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/), the query is populated by default in the **Query Pane**. You can also edit or update the query as per your requirement and run it.

> **Query**
>
>
>
>
> > ```
> > query GetElementsInProject($projectId: ID!, $propertyFilter: String!) {
> > elementsByProject(projectId: $projectId, filter: {query: $propertyFilter}) {
> > pagination {
> > cursor
> > }
> > results {
> > id
> > name
> > properties(
> > includeReferencesProperties: "Type"
> > filter: {names: ["Family Name", "Element Name", "Element Context", "Fire Rating"]}
> > ) {
> > results {
> > name
> > value
> > displayValue
> > definition {
> > units{
> > name
> > }
> > }
> > }
> > }
> > }
> > }
> > }
> >
> > ```
> > Show More
> **Query Variables**
>
>
>
>
> > - In the Query Variables Pane, replace the value of the `projectId` variable with the project ID that you used in [Navigate to Elementgroups](https://aps.autodesk.com/en/docs/aecdatamodel/v1/tutorials/tutorial-01/nav-elements/).
> > - In the Query Variables Pane, replace the value of the `propertyFilter` with the property filter of your choice.
> > **Note**: To know the list of supported metadata filtering options, refer to the [Advanced Filtering Capabilities](https://aps.autodesk.com/en/docs/aecdatamodel/v1/developers_guide/filtering/advanced-filtering/) page.
> >
> >
> >
> >
> > ```
> > {
> > "projectId": "urn:adsk.workspace:prod.project:39208068-e548-4d9e-b8a7-e000fdf2a9b4",
> > "propertyFilter": "'property.name.Family Name'=='Basic Wall' and property.name.Length > 10 and 'property.name.Element Context'==Instance"
> > }
> >
> > ```

2. Click **Play**. The list of elements available within that elementGroup of property ‘family’ and value ‘“Basic Wall” is displayed in the response. The response should be similar to the following code-block:

> **Note**: The following code is a subset data of complete response, hence do not use this as reference.
>
> **Response**
>
>
>
>
> > ```
> > {
> > "data": {
> > "elementsByProject": {
> > "pagination": {
> > "cursor": "YWRjdXJzfjB-NTB-NTA"
> > },
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ340VFVtRnF0WFJVVy1CS09Gb1cyd3FRXzE4NTI4MQ",
> > "name": "Generic - 200mm",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 200mm",
> > "displayValue": "Generic - 200mm",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ340VFVtRnF0WFJVVy1CS09Gb1cyd3FRXzE4NTI4Mg",
> > "name": "Generic - 200mm",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 200mm",
> > "displayValue": "Generic - 200mm",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ340VFVtRnF0WFJVVy1CS09Gb1cyd3FRXzE4NTI4Mw",
> > "name": "Generic - 200mm",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 200mm",
> > "displayValue": "Generic - 200mm",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ340VFVtRnF0WFJVVy1CS09Gb1cyd3FRXzE4NTI4NA",
> > "name": "Generic - 200mm",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 200mm",
> > "displayValue": "Generic - 200mm",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzExNjJiYw",
> > "name": "Retaining - 12\" Concrete",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Retaining - 12\" Concrete",
> > "displayValue": "Retaining - 12\" Concrete",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzExNjJiZA",
> > "name": "Retaining - 12\" Concrete",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Retaining - 12\" Concrete",
> > "displayValue": "Retaining - 12\" Concrete",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNGM2Nw",
> > "name": "Foundation - 24\" Concrete",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Foundation - 24\" Concrete",
> > "displayValue": "Foundation - 24\" Concrete",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": "4 HR",
> > "displayValue": "4 HR",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNTYzNQ",
> > "name": "Foundation - 24\" Concrete",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Foundation - 24\" Concrete",
> > "displayValue": "Foundation - 24\" Concrete",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": "4 HR",
> > "displayValue": "4 HR",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNTYzNg",
> > "name": "Foundation - 24\" Concrete",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Foundation - 24\" Concrete",
> > "displayValue": "Foundation - 24\" Concrete",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": "4 HR",
> > "displayValue": "4 HR",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNTcxMg",
> > "name": "Foundation - 24\" Concrete",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Foundation - 24\" Concrete",
> > "displayValue": "Foundation - 24\" Concrete",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": "4 HR",
> > "displayValue": "4 HR",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNTcxMw",
> > "name": "Foundation - 24\" Concrete",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Foundation - 24\" Concrete",
> > "displayValue": "Foundation - 24\" Concrete",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": "4 HR",
> > "displayValue": "4 HR",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNTcxNA",
> > "name": "Foundation - 24\" Concrete",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Foundation - 24\" Concrete",
> > "displayValue": "Foundation - 24\" Concrete",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": "4 HR",
> > "displayValue": "4 HR",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNTcxNQ",
> > "name": "Foundation - 24\" Concrete",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Foundation - 24\" Concrete",
> > "displayValue": "Foundation - 24\" Concrete",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": "4 HR",
> > "displayValue": "4 HR",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNTcxNw",
> > "name": "Foundation - 24\" Concrete",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Foundation - 24\" Concrete",
> > "displayValue": "Foundation - 24\" Concrete",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": "4 HR",
> > "displayValue": "4 HR",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35fR1IzdHpORlI3LV9tclFBOGR4TWN3XzE4NGNkMg",
> > "name": "Proposed Partition 4\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Proposed Partition 4\"",
> > "displayValue": "Proposed Partition 4\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEwNTc3ZQ",
> > "name": "Block 39 - L2 Entablature",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Block 39 - L2 Entablature",
> > "displayValue": "Block 39 - L2 Entablature",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEwNTg3Yg",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEwNTkwZA",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEwNjk1Zg",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEwNjk4OQ",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmI5Zg",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmJiNQ",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmJjNQ",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmMwMQ",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmMxOA",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmMyYQ",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmM0Nw",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmM2YQ",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmM4Yg",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmZmNQ",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEzMDBlZg",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEzMDFiYw",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEzMDRmNA",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDI5",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDJh",
> > "name": "Generic - 6\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 6\"",
> > "displayValue": "Generic - 6\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDJi",
> > "name": "Generic - 6\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 6\"",
> > "displayValue": "Generic - 6\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDJj",
> > "name": "Block 43",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Block 43",
> > "displayValue": "Block 43",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDJk",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDJl",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDJm",
> > "name": "Generic - 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 12\"",
> > "displayValue": "Generic - 12\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDMx",
> > "name": "Block 37",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Block 37",
> > "displayValue": "Block 37",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDMy",
> > "name": "Block 37",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Block 37",
> > "displayValue": "Block 37",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDM2",
> > "name": "Generic - 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 10\"",
> > "displayValue": "Generic - 10\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDQx",
> > "name": "Generic - 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 10\"",
> > "displayValue": "Generic - 10\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDQ0",
> > "name": "Generic - 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 10\"",
> > "displayValue": "Generic - 10\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDQ3",
> > "name": "Generic - 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 10\"",
> > "displayValue": "Generic - 10\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDRh",
> > "name": "Generic - 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 10\"",
> > "displayValue": "Generic - 10\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDRk",
> > "name": "Generic - 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 10\"",
> > "displayValue": "Generic - 10\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDUw",
> > "name": "Generic - 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 10\"",
> > "displayValue": "Generic - 10\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDc3",
> > "name": "Generic - 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Element Name",
> > "value": "Generic - 10\"",
> > "displayValue": "Generic - 10\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "displayValue": null,
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > }
> > ]
> > }
> > }
> > }
> >
> > ```
> > Show More

After working through the steps mentioned above, your Explorer should look similar to the following image:
> 
