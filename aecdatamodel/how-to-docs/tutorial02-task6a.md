# Get Elements by using Instances or Reference

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/tutorial02/task6a/

---

# Get Elements by using Instances or Reference

In this guide, you will learn how to retrieve all elements from all elementGroups within a project. You will also learn how to filter elements based on their materials, by element instances, or by using reference types to fetch specific results that match your criteria.

By the end of this guide, you will be able to:

- Fetch elements and information like id and properties.
- Understand the options and fields in the documentation on the elements query, elements object, Properties object, and references relationship.
- Learn to List all instances of concrete material elements in a elementGroup.
- Learn to List all instances of concrete material elements using instances.
- Learn to List all instances of concrete material elements by using reference parameter.

You will use the following query in this guide:

| Type | Operation | Description |
| --- | --- | --- |
| Query | [ElementsByElementGroup](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elementsByElementGroup/) | Retrieves element in the given elementGroup using additional RSQL filters if provided. |

## [Step 1: List all Elements Having Concrete Material in a ElementGroup](#step-1-list-all-elements-having-concrete-material-in-a-elementgroup)

First, list all concrete material elements under a elementGroup. This is done by fetching elements of category ‘Materials’ having an ‘Element Name’ property matching the string ‘Concrete’.

The [Elements](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elements/) query returns [Elements](../reference-docs/objects-elements.md) object, which contains an array of Elements objects.

For this exercise, we request all elements instances with
- Elements id, name field, and properties.
- Classification object.
- Name and value fields in the properties object.

1. In [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/), the query is populated by default in the **Query Pane**. You can also edit or update the query as per your requirement and run it.

> **Query**
>
>
>
>
> > ```
> > query GetConcreteMaterials($elementGroupId: ID!, $propertyFilter: String!) {
> > elementsByElementGroup(
> > elementGroupId: $elementGroupId
> > filter: {query: $propertyFilter}
> > pagination: {limit: 20}
> > ) {
> > results {
> > id
> > name
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
> > - In the Query Variables Pane, replace the value of the elementGroupId variable with the elementGroupId that you used in [Navigate to ElementGroups](https://aps.autodesk.com/en/docs/aecdatamodel/v1/tutorials/tutorial-01/nav-elements/) of previous tutorial.
> > - In the Query Variables Pane, replace the value of the property filter with the property filter of your choice. For ease of understanding, here we have filtered based on property name from the category of windows.
> > **Note**: For information on the supported metadata filtering options, refer to the [Advanced Filtering Capabilities](https://aps.autodesk.com/en/docs/aecdatamodel/v1/developers_guide/filtering/advanced-filtering/) page.
> >
> >
> >
> >
> > ```
> > {
> > "elementGroupId": "YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVB",
> > "propertyFilter": "property.name.category==Materials and 'property.name.Element Name'=contains='Concrete'"
> > }
> >
> > ```

2. Click **Play**. The list of elements available within that elementGroup of property ‘family’ and value ‘“Basic Wall” is displayed in the response. The response should be similar to the following code-block:

> **Response**
>
>
>
>
> > ```
> > {
> > "data": {
> > "elementsByElementGroup": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzE1Nzc0Mw",
> > "name": "Concrete, Precast Smooth, Light Grey"
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzFmYjFhNA",
> > "name": "Concrete, Polished"
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzQ5ZmI",
> > "name": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzQ5ZmM",
> > "name": "Concrete, Precast"
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzQ5ZmU",
> > "name": "Concrete Masonry Units"
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzVlOGE",
> > "name": "Concrete, Lightweight"
> > }
> > ]
> > }
> > }
> > }
> >
> > ```
> > Show More

After working through the steps mentioned above, you should see a screen similar to the following image:
> **Note**: In some elementGroups, element instances may directly refer to material elements. In these cases, we use a query similar to [step 2](https://aps.autodesk.com/en/docs/aecdatamodel/v1/tutorials/tutorial-02/task6a/#step-2-list-the-instance-of-elements-referencing-the-concrete-material-directly). However, in other elementGroups, material elements are referenced by Type elements. In such cases, we use a query similar to [step 3](https://aps.autodesk.com/en/docs/aecdatamodel/v1/tutorials/tutorial-02/task6a/#step-3-list-the-instance-of-elements-which-references-concrete-material-through-a-type-for-every-type-element), where we list the Type that references the material.

## [Step 2: List Element Instances Having Concrete Material](#step-2-list-element-instances-having-concrete-material)

List the elements Instance having different types of concrete material. For this example, we will use the ‘Concrete, Precast’ and ‘Concrete, Precast Smooth, Light Grey’ ids.

1. In [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/), the query is populated by default in the **Query Pane**. You can also edit or update the query as per your requirement and run it.

> **Query**
>
>
>
>
> > ```
> > query GetInstancesOfConcreteMaterial($elementGroupId: ID!, $propertyFilter: String!) {
> > elementsByElementGroup(elementGroupId: $elementGroupId, filter: { query: $propertyFilter}, pagination : { limit : 20 }) {
> > results {
> > id
> > name
> > properties {
> > results {
> > name
> > value
> > }
> > }
> > references{
> > results{
> > name
> > displayValue
> > value{
> > properties{
> > results{
> > name
> > value
> > displayValue
> > }
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
> > - In the Query Variables Pane, replace the value of the `elementGroupId` variable with the elementGroup ID that you used in [Navigate to ElementGroups](https://aps.autodesk.com/en/docs/aecdatamodel/v1/tutorials/tutorial-01/nav-elements/) of previous tutorial.
> > - In the Query Variables Pane, replace the value of the `property filter` with the property filter of your choice. For ease of understanding, here we have filtered based on property filter as reference.structural Material.
> > **Note**: For information on the supported metadata filtering options, refer to the [Advanced Filtering Capabilities](https://aps.autodesk.com/en/docs/aecdatamodel/v1/developers_guide/filtering/advanced-filtering/) page.
> >
> >
> >
> >
> > ```
> > {
> > "elementGroupId" : "YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3",
> > "propertyFilter" : "('reference.Structural Material'==YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzJkNjE3 or 'reference.Structural Material'==YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzJlZA) and 'property.name.Element Context'==Instance"
> > }
> >
> > ```

2. Click **Play**. The list of elements available for the elementGroup property is retrieved. The response should be similar to the following code-block:

> **Note**: In this query result, you might see blank responses because the system could not find matching elements for the specified filters. However, it is important to note that this does not apply to all cases, and the responses may differ for other queries based on the availability of elements.
>
> **Response**
>
>
>
>
> > ```
> > {
> > "data": {
> > "elementsByElementGroup": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzkzZjc1",
> > "name": "CC24x24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Column Location Mark",
> > "value": "D-3"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093f75"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Volume",
> > "value": 1.3120138920959115
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqQ9"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular-Column"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Column Style",
> > "value": 0
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606069"
> > }
> > ]
> > },
> > "references": {
> > "results": [
> > {
> > "name": "Rebar Cover - Top Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Other Faces",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Bottom Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family and Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Base Level",
> > "displayValue": "Top of Footing",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27",
> > "displayValue": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSZ9",
> > "displayValue": "1CEMWRTvz6HwQKgNsRJSZ9"
> > },
> > {
> > "name": "Elevation",
> > "value": -5.3340000000000005,
> > "displayValue": "-5.3340000000000005"
> > },
> > {
> > "name": "Building Story",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "772903",
> > "displayValue": "772903"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Top Level",
> > "displayValue": "L1_35_Low",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "L1_35_Low",
> > "displayValue": "L1_35_Low"
> > },
> > {
> > "name": "External ID",
> > "value": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e93",
> > "displayValue": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e93"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3eRW_mgkzCZQysdnuCHXVn",
> > "displayValue": "3eRW_mgkzCZQysdnuCHXVn"
> > },
> > {
> > "name": "Elevation",
> > "value": -1.8034000000002377,
> > "displayValue": "-1.8034000000002377"
> > },
> > {
> > "name": "Building Story",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "L1_35_Low",
> > "displayValue": "L1_35_Low"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "618131",
> > "displayValue": "618131"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Phase Created",
> > "displayValue": "New Construction",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "External ID",
> > "value": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000",
> > "displayValue": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000"
> > },
> > {
> > "name": "Family Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "0",
> > "displayValue": "0"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Structural Material",
> > "displayValue": "Concrete, Cast-in-Place gray",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": "Cast-in-place concrete",
> > "displayValue": "Cast-in-place concrete"
> > },
> > {
> > "name": "Comments",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Manufacturer",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Model",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "URL",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Cost",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Mark",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "External ID",
> > "value": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed",
> > "displayValue": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1krdmuBkzDbgRKCWsf465_",
> > "displayValue": "1krdmuBkzDbgRKCWsf465_"
> > },
> > {
> > "name": "Keynote",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Color",
> > "value": 9673370,
> > "displayValue": "9673370"
> > },
> > {
> > "name": "Glow",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Shininess",
> > "value": 64,
> > "displayValue": "64"
> > },
> > {
> > "name": "Smoothness",
> > "value": 50,
> > "displayValue": "50"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Behavior",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Class",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Concrete compression",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Lightweight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear strength modification",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Subclass",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Material Type",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Unit weight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "749",
> > "displayValue": "749"
> > }
> > ]
> > }
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzkzZmQz",
> > "name": "CC24x24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Column Location Mark",
> > "value": "D-5"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093fd3"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Volume",
> > "value": 1.5904628835839993
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqOl"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular-Column"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Column Style",
> > "value": 0
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606163"
> > }
> > ]
> > },
> > "references": {
> > "results": [
> > {
> > "name": "Rebar Cover - Top Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Other Faces",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Bottom Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family and Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Base Level",
> > "displayValue": "Top of Footing",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27",
> > "displayValue": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSZ9",
> > "displayValue": "1CEMWRTvz6HwQKgNsRJSZ9"
> > },
> > {
> > "name": "Elevation",
> > "value": -5.3340000000000005,
> > "displayValue": "-5.3340000000000005"
> > },
> > {
> > "name": "Building Story",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "772903",
> > "displayValue": "772903"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Phase Created",
> > "displayValue": "New Construction",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "External ID",
> > "value": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000",
> > "displayValue": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000"
> > },
> > {
> > "name": "Family Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "0",
> > "displayValue": "0"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Structural Material",
> > "displayValue": "Concrete, Cast-in-Place gray",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": "Cast-in-place concrete",
> > "displayValue": "Cast-in-place concrete"
> > },
> > {
> > "name": "Comments",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Manufacturer",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Model",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "URL",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Cost",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Mark",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "External ID",
> > "value": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed",
> > "displayValue": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1krdmuBkzDbgRKCWsf465_",
> > "displayValue": "1krdmuBkzDbgRKCWsf465_"
> > },
> > {
> > "name": "Keynote",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Color",
> > "value": 9673370,
> > "displayValue": "9673370"
> > },
> > {
> > "name": "Glow",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Shininess",
> > "value": 64,
> > "displayValue": "64"
> > },
> > {
> > "name": "Smoothness",
> > "value": 50,
> > "displayValue": "50"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Behavior",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Class",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Concrete compression",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Lightweight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear strength modification",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Subclass",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Material Type",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Unit weight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "749",
> > "displayValue": "749"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Top Level",
> > "displayValue": "L1_37_Med",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "External ID",
> > "value": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54",
> > "displayValue": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3eRW_mgkzCZQysdnuCHXSs",
> > "displayValue": "3eRW_mgkzCZQysdnuCHXSs"
> > },
> > {
> > "name": "Elevation",
> > "value": -1.0541000000000016,
> > "displayValue": "-1.0541000000000016"
> > },
> > {
> > "name": "Building Story",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "618068",
> > "displayValue": "618068"
> > }
> > ]
> > }
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MDNj",
> > "name": "CC24x24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Column Location Mark",
> > "value": "D-7"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-0009403c"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Volume",
> > "value": 1.5904628835839993
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpd0"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular-Column"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Column Style",
> > "value": 0
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606268"
> > }
> > ]
> > },
> > "references": {
> > "results": [
> > {
> > "name": "Rebar Cover - Top Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Other Faces",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Bottom Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family and Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Base Level",
> > "displayValue": "Top of Footing",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27",
> > "displayValue": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSZ9",
> > "displayValue": "1CEMWRTvz6HwQKgNsRJSZ9"
> > },
> > {
> > "name": "Elevation",
> > "value": -5.3340000000000005,
> > "displayValue": "-5.3340000000000005"
> > },
> > {
> > "name": "Building Story",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "772903",
> > "displayValue": "772903"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Phase Created",
> > "displayValue": "New Construction",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "External ID",
> > "value": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000",
> > "displayValue": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000"
> > },
> > {
> > "name": "Family Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "0",
> > "displayValue": "0"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Structural Material",
> > "displayValue": "Concrete, Cast-in-Place gray",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": "Cast-in-place concrete",
> > "displayValue": "Cast-in-place concrete"
> > },
> > {
> > "name": "Comments",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Manufacturer",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Model",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "URL",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Cost",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Mark",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "External ID",
> > "value": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed",
> > "displayValue": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1krdmuBkzDbgRKCWsf465_",
> > "displayValue": "1krdmuBkzDbgRKCWsf465_"
> > },
> > {
> > "name": "Keynote",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Color",
> > "value": 9673370,
> > "displayValue": "9673370"
> > },
> > {
> > "name": "Glow",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Shininess",
> > "value": 64,
> > "displayValue": "64"
> > },
> > {
> > "name": "Smoothness",
> > "value": 50,
> > "displayValue": "50"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Behavior",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Class",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Concrete compression",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Lightweight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear strength modification",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Subclass",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Material Type",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Unit weight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "749",
> > "displayValue": "749"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Top Level",
> > "displayValue": "L1_37_Med",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "External ID",
> > "value": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54",
> > "displayValue": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3eRW_mgkzCZQysdnuCHXSs",
> > "displayValue": "3eRW_mgkzCZQysdnuCHXSs"
> > },
> > {
> > "name": "Elevation",
> > "value": -1.0541000000000016,
> > "displayValue": "-1.0541000000000016"
> > },
> > {
> > "name": "Building Story",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "618068",
> > "displayValue": "618068"
> > }
> > ]
> > }
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MDdi",
> > "name": "CC24x24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Column Location Mark",
> > "value": "D-8"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-0009407b"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Volume",
> > "value": 1.9821792614399987
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpc7"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular-Column"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Column Style",
> > "value": 0
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606331"
> > }
> > ]
> > },
> > "references": {
> > "results": [
> > {
> > "name": "Rebar Cover - Top Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Other Faces",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Bottom Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family and Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Base Level",
> > "displayValue": "Top of Footing",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27",
> > "displayValue": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSZ9",
> > "displayValue": "1CEMWRTvz6HwQKgNsRJSZ9"
> > },
> > {
> > "name": "Elevation",
> > "value": -5.3340000000000005,
> > "displayValue": "-5.3340000000000005"
> > },
> > {
> > "name": "Building Story",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "772903",
> > "displayValue": "772903"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Phase Created",
> > "displayValue": "New Construction",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "External ID",
> > "value": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000",
> > "displayValue": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000"
> > },
> > {
> > "name": "Family Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "0",
> > "displayValue": "0"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Structural Material",
> > "displayValue": "Concrete, Cast-in-Place gray",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": "Cast-in-place concrete",
> > "displayValue": "Cast-in-place concrete"
> > },
> > {
> > "name": "Comments",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Manufacturer",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Model",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "URL",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Cost",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Mark",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "External ID",
> > "value": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed",
> > "displayValue": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1krdmuBkzDbgRKCWsf465_",
> > "displayValue": "1krdmuBkzDbgRKCWsf465_"
> > },
> > {
> > "name": "Keynote",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Color",
> > "value": 9673370,
> > "displayValue": "9673370"
> > },
> > {
> > "name": "Glow",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Shininess",
> > "value": 64,
> > "displayValue": "64"
> > },
> > {
> > "name": "Smoothness",
> > "value": 50,
> > "displayValue": "50"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Behavior",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Class",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Concrete compression",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Lightweight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear strength modification",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Subclass",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Material Type",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Unit weight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "749",
> > "displayValue": "749"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Top Level",
> > "displayValue": "L1_43_High",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "L1_43_High",
> > "displayValue": "L1_43_High"
> > },
> > {
> > "name": "External ID",
> > "value": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000149",
> > "displayValue": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000149"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "12f1l24kT8d9RBml7$P4Yu",
> > "displayValue": "12f1l24kT8d9RBml7$P4Yu"
> > },
> > {
> > "name": "Elevation",
> > "value": -1.7102397031084183e-15,
> > "displayValue": "-1.7102397031084183E-15"
> > },
> > {
> > "name": "Building Story",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "L1_43_High",
> > "displayValue": "L1_43_High"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "329",
> > "displayValue": "329"
> > }
> > ]
> > }
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MDk2",
> > "name": "CC24x24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Column Location Mark",
> > "value": "B.1-7"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00094096"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Volume",
> > "value": 1.4960733949439982
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpbg"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular-Column"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Column Style",
> > "value": 0
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606358"
> > }
> > ]
> > },
> > "references": {
> > "results": [
> > {
> > "name": "Rebar Cover - Other Faces",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Bottom Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family and Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Base Level",
> > "displayValue": "Top of Footing",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27",
> > "displayValue": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSZ9",
> > "displayValue": "1CEMWRTvz6HwQKgNsRJSZ9"
> > },
> > {
> > "name": "Elevation",
> > "value": -5.3340000000000005,
> > "displayValue": "-5.3340000000000005"
> > },
> > {
> > "name": "Building Story",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "772903",
> > "displayValue": "772903"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Phase Created",
> > "displayValue": "New Construction",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "External ID",
> > "value": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000",
> > "displayValue": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000"
> > },
> > {
> > "name": "Family Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "0",
> > "displayValue": "0"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Structural Material",
> > "displayValue": "Concrete, Cast-in-Place gray",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": "Cast-in-place concrete",
> > "displayValue": "Cast-in-place concrete"
> > },
> > {
> > "name": "Comments",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Manufacturer",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Model",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "URL",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Cost",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Mark",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "External ID",
> > "value": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed",
> > "displayValue": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1krdmuBkzDbgRKCWsf465_",
> > "displayValue": "1krdmuBkzDbgRKCWsf465_"
> > },
> > {
> > "name": "Keynote",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Color",
> > "value": 9673370,
> > "displayValue": "9673370"
> > },
> > {
> > "name": "Glow",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Shininess",
> > "value": 64,
> > "displayValue": "64"
> > },
> > {
> > "name": "Smoothness",
> > "value": 50,
> > "displayValue": "50"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Behavior",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Class",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Concrete compression",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Lightweight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear strength modification",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Subclass",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Material Type",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Unit weight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "749",
> > "displayValue": "749"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Top Level",
> > "displayValue": "L1_37_Med",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "External ID",
> > "value": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54",
> > "displayValue": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3eRW_mgkzCZQysdnuCHXSs",
> > "displayValue": "3eRW_mgkzCZQysdnuCHXSs"
> > },
> > {
> > "name": "Elevation",
> > "value": -1.0541000000000016,
> > "displayValue": "-1.0541000000000016"
> > },
> > {
> > "name": "Building Story",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "618068",
> > "displayValue": "618068"
> > }
> > ]
> > }
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MTY0",
> > "name": "CC24x24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Column Location Mark",
> > "value": "B.1-6"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00094164"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Volume",
> > "value": 1.496073394944
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpYO"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular-Column"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Column Style",
> > "value": 0
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606564"
> > }
> > ]
> > },
> > "references": {
> > "results": [
> > {
> > "name": "Rebar Cover - Other Faces",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Bottom Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family and Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Base Level",
> > "displayValue": "Top of Footing",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27",
> > "displayValue": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSZ9",
> > "displayValue": "1CEMWRTvz6HwQKgNsRJSZ9"
> > },
> > {
> > "name": "Elevation",
> > "value": -5.3340000000000005,
> > "displayValue": "-5.3340000000000005"
> > },
> > {
> > "name": "Building Story",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "772903",
> > "displayValue": "772903"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Phase Created",
> > "displayValue": "New Construction",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "External ID",
> > "value": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000",
> > "displayValue": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000"
> > },
> > {
> > "name": "Family Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "0",
> > "displayValue": "0"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Structural Material",
> > "displayValue": "Concrete, Cast-in-Place gray",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": "Cast-in-place concrete",
> > "displayValue": "Cast-in-place concrete"
> > },
> > {
> > "name": "Comments",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Manufacturer",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Model",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "URL",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Cost",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Mark",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "External ID",
> > "value": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed",
> > "displayValue": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1krdmuBkzDbgRKCWsf465_",
> > "displayValue": "1krdmuBkzDbgRKCWsf465_"
> > },
> > {
> > "name": "Keynote",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Color",
> > "value": 9673370,
> > "displayValue": "9673370"
> > },
> > {
> > "name": "Glow",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Shininess",
> > "value": 64,
> > "displayValue": "64"
> > },
> > {
> > "name": "Smoothness",
> > "value": 50,
> > "displayValue": "50"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Behavior",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Class",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Concrete compression",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Lightweight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear strength modification",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Subclass",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Material Type",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Unit weight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "749",
> > "displayValue": "749"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Top Level",
> > "displayValue": "L1_37_Med",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "External ID",
> > "value": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54",
> > "displayValue": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3eRW_mgkzCZQysdnuCHXSs",
> > "displayValue": "3eRW_mgkzCZQysdnuCHXSs"
> > },
> > {
> > "name": "Elevation",
> > "value": -1.0541000000000016,
> > "displayValue": "-1.0541000000000016"
> > },
> > {
> > "name": "Building Story",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "618068",
> > "displayValue": "618068"
> > }
> > ]
> > }
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MTZl",
> > "name": "CC24x24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Column Location Mark",
> > "value": "B.1-5"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-0009416e"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Volume",
> > "value": 1.4960733949440004
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpYI"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular-Column"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Column Style",
> > "value": 0
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606574"
> > }
> > ]
> > },
> > "references": {
> > "results": [
> > {
> > "name": "Rebar Cover - Other Faces",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Bottom Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family and Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Base Level",
> > "displayValue": "Top of Footing",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27",
> > "displayValue": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSZ9",
> > "displayValue": "1CEMWRTvz6HwQKgNsRJSZ9"
> > },
> > {
> > "name": "Elevation",
> > "value": -5.3340000000000005,
> > "displayValue": "-5.3340000000000005"
> > },
> > {
> > "name": "Building Story",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "772903",
> > "displayValue": "772903"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Phase Created",
> > "displayValue": "New Construction",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "External ID",
> > "value": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000",
> > "displayValue": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000"
> > },
> > {
> > "name": "Family Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "0",
> > "displayValue": "0"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Structural Material",
> > "displayValue": "Concrete, Cast-in-Place gray",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": "Cast-in-place concrete",
> > "displayValue": "Cast-in-place concrete"
> > },
> > {
> > "name": "Comments",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Manufacturer",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Model",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "URL",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Cost",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Mark",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "External ID",
> > "value": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed",
> > "displayValue": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1krdmuBkzDbgRKCWsf465_",
> > "displayValue": "1krdmuBkzDbgRKCWsf465_"
> > },
> > {
> > "name": "Keynote",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Color",
> > "value": 9673370,
> > "displayValue": "9673370"
> > },
> > {
> > "name": "Glow",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Shininess",
> > "value": 64,
> > "displayValue": "64"
> > },
> > {
> > "name": "Smoothness",
> > "value": 50,
> > "displayValue": "50"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Behavior",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Class",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Concrete compression",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Lightweight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear strength modification",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Subclass",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Material Type",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Unit weight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "749",
> > "displayValue": "749"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Top Level",
> > "displayValue": "L1_37_Med",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "External ID",
> > "value": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54",
> > "displayValue": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3eRW_mgkzCZQysdnuCHXSs",
> > "displayValue": "3eRW_mgkzCZQysdnuCHXSs"
> > },
> > {
> > "name": "Elevation",
> > "value": -1.0541000000000016,
> > "displayValue": "-1.0541000000000016"
> > },
> > {
> > "name": "Building Story",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "618068",
> > "displayValue": "618068"
> > }
> > ]
> > }
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MTc4",
> > "name": "CC24x24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Column Location Mark",
> > "value": "B.1-4"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00094178"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Volume",
> > "value": 1.5904628835839996
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpY4"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular-Column"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Column Style",
> > "value": 0
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606584"
> > }
> > ]
> > },
> > "references": {
> > "results": [
> > {
> > "name": "Rebar Cover - Top Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Other Faces",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Bottom Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family and Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Base Level",
> > "displayValue": "Top of Footing",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27",
> > "displayValue": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSZ9",
> > "displayValue": "1CEMWRTvz6HwQKgNsRJSZ9"
> > },
> > {
> > "name": "Elevation",
> > "value": -5.3340000000000005,
> > "displayValue": "-5.3340000000000005"
> > },
> > {
> > "name": "Building Story",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "772903",
> > "displayValue": "772903"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Phase Created",
> > "displayValue": "New Construction",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "External ID",
> > "value": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000",
> > "displayValue": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000"
> > },
> > {
> > "name": "Family Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "0",
> > "displayValue": "0"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Structural Material",
> > "displayValue": "Concrete, Cast-in-Place gray",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": "Cast-in-place concrete",
> > "displayValue": "Cast-in-place concrete"
> > },
> > {
> > "name": "Comments",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Manufacturer",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Model",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "URL",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Cost",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Mark",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "External ID",
> > "value": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed",
> > "displayValue": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1krdmuBkzDbgRKCWsf465_",
> > "displayValue": "1krdmuBkzDbgRKCWsf465_"
> > },
> > {
> > "name": "Keynote",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Color",
> > "value": 9673370,
> > "displayValue": "9673370"
> > },
> > {
> > "name": "Glow",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Shininess",
> > "value": 64,
> > "displayValue": "64"
> > },
> > {
> > "name": "Smoothness",
> > "value": 50,
> > "displayValue": "50"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Behavior",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Class",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Concrete compression",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Lightweight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear strength modification",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Subclass",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Material Type",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Unit weight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "749",
> > "displayValue": "749"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Top Level",
> > "displayValue": "L1_37_Med",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "External ID",
> > "value": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54",
> > "displayValue": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3eRW_mgkzCZQysdnuCHXSs",
> > "displayValue": "3eRW_mgkzCZQysdnuCHXSs"
> > },
> > {
> > "name": "Elevation",
> > "value": -1.0541000000000016,
> > "displayValue": "-1.0541000000000016"
> > },
> > {
> > "name": "Building Story",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "618068",
> > "displayValue": "618068"
> > }
> > ]
> > }
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MTg0",
> > "name": "CC24x24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Column Location Mark",
> > "value": "B.1-3"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00094184"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Volume",
> > "value": 1.2176244034559116
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpXu"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular-Column"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Estimated Reinforcement Volume",
> > "value": 0.011713645468105686
> > },
> > {
> > "name": "Column Style",
> > "value": 0
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606596"
> > }
> > ]
> > },
> > "references": {
> > "results": [
> > {
> > "name": "Rebar Cover - Other Faces",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Bottom Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family and Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Base Level",
> > "displayValue": "Top of Footing",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27",
> > "displayValue": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSZ9",
> > "displayValue": "1CEMWRTvz6HwQKgNsRJSZ9"
> > },
> > {
> > "name": "Elevation",
> > "value": -5.3340000000000005,
> > "displayValue": "-5.3340000000000005"
> > },
> > {
> > "name": "Building Story",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "772903",
> > "displayValue": "772903"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Top Level",
> > "displayValue": "L1_35_Low",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "L1_35_Low",
> > "displayValue": "L1_35_Low"
> > },
> > {
> > "name": "External ID",
> > "value": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e93",
> > "displayValue": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e93"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3eRW_mgkzCZQysdnuCHXVn",
> > "displayValue": "3eRW_mgkzCZQysdnuCHXVn"
> > },
> > {
> > "name": "Elevation",
> > "value": -1.8034000000002377,
> > "displayValue": "-1.8034000000002377"
> > },
> > {
> > "name": "Building Story",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "L1_35_Low",
> > "displayValue": "L1_35_Low"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "618131",
> > "displayValue": "618131"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Phase Created",
> > "displayValue": "New Construction",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "External ID",
> > "value": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000",
> > "displayValue": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000"
> > },
> > {
> > "name": "Family Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "0",
> > "displayValue": "0"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Structural Material",
> > "displayValue": "Concrete, Cast-in-Place gray",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": "Cast-in-place concrete",
> > "displayValue": "Cast-in-place concrete"
> > },
> > {
> > "name": "Comments",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Manufacturer",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Model",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "URL",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Cost",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Mark",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "External ID",
> > "value": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed",
> > "displayValue": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1krdmuBkzDbgRKCWsf465_",
> > "displayValue": "1krdmuBkzDbgRKCWsf465_"
> > },
> > {
> > "name": "Keynote",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Color",
> > "value": 9673370,
> > "displayValue": "9673370"
> > },
> > {
> > "name": "Glow",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Shininess",
> > "value": 64,
> > "displayValue": "64"
> > },
> > {
> > "name": "Smoothness",
> > "value": 50,
> > "displayValue": "50"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Behavior",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Class",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Concrete compression",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Lightweight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear strength modification",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Subclass",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Material Type",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Unit weight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "749",
> > "displayValue": "749"
> > }
> > ]
> > }
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MThl",
> > "name": "CC24x24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Column Location Mark",
> > "value": "B.1-2"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-0009418e"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Volume",
> > "value": 1.2176244034559116
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpXo"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular-Column"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Column Style",
> > "value": 0
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606606"
> > }
> > ]
> > },
> > "references": {
> > "results": [
> > {
> > "name": "Rebar Cover - Other Faces",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Bottom Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family and Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Base Level",
> > "displayValue": "Top of Footing",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27",
> > "displayValue": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSZ9",
> > "displayValue": "1CEMWRTvz6HwQKgNsRJSZ9"
> > },
> > {
> > "name": "Elevation",
> > "value": -5.3340000000000005,
> > "displayValue": "-5.3340000000000005"
> > },
> > {
> > "name": "Building Story",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "772903",
> > "displayValue": "772903"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Top Level",
> > "displayValue": "L1_35_Low",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "L1_35_Low",
> > "displayValue": "L1_35_Low"
> > },
> > {
> > "name": "External ID",
> > "value": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e93",
> > "displayValue": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e93"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3eRW_mgkzCZQysdnuCHXVn",
> > "displayValue": "3eRW_mgkzCZQysdnuCHXVn"
> > },
> > {
> > "name": "Elevation",
> > "value": -1.8034000000002377,
> > "displayValue": "-1.8034000000002377"
> > },
> > {
> > "name": "Building Story",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "L1_35_Low",
> > "displayValue": "L1_35_Low"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "618131",
> > "displayValue": "618131"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Phase Created",
> > "displayValue": "New Construction",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "External ID",
> > "value": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000",
> > "displayValue": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000"
> > },
> > {
> > "name": "Family Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "0",
> > "displayValue": "0"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Structural Material",
> > "displayValue": "Concrete, Cast-in-Place gray",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": "Cast-in-place concrete",
> > "displayValue": "Cast-in-place concrete"
> > },
> > {
> > "name": "Comments",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Manufacturer",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Model",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "URL",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Cost",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Mark",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "External ID",
> > "value": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed",
> > "displayValue": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1krdmuBkzDbgRKCWsf465_",
> > "displayValue": "1krdmuBkzDbgRKCWsf465_"
> > },
> > {
> > "name": "Keynote",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Color",
> > "value": 9673370,
> > "displayValue": "9673370"
> > },
> > {
> > "name": "Glow",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Shininess",
> > "value": 64,
> > "displayValue": "64"
> > },
> > {
> > "name": "Smoothness",
> > "value": 50,
> > "displayValue": "50"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Behavior",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Class",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Concrete compression",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Lightweight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear strength modification",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Subclass",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Material Type",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Unit weight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "749",
> > "displayValue": "749"
> > }
> > ]
> > }
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0NGUw",
> > "name": "CC24x24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Column Location Mark",
> > "value": "D-2"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000944e0"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Volume",
> > "value": 1.3120138920959117
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpqS"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular-Column"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Column Style",
> > "value": 0
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "607456"
> > }
> > ]
> > },
> > "references": {
> > "results": [
> > {
> > "name": "Rebar Cover - Top Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Other Faces",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Bottom Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family and Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Base Level",
> > "displayValue": "Top of Footing",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27",
> > "displayValue": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSZ9",
> > "displayValue": "1CEMWRTvz6HwQKgNsRJSZ9"
> > },
> > {
> > "name": "Elevation",
> > "value": -5.3340000000000005,
> > "displayValue": "-5.3340000000000005"
> > },
> > {
> > "name": "Building Story",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "772903",
> > "displayValue": "772903"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Top Level",
> > "displayValue": "L1_35_Low",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "L1_35_Low",
> > "displayValue": "L1_35_Low"
> > },
> > {
> > "name": "External ID",
> > "value": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e93",
> > "displayValue": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e93"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3eRW_mgkzCZQysdnuCHXVn",
> > "displayValue": "3eRW_mgkzCZQysdnuCHXVn"
> > },
> > {
> > "name": "Elevation",
> > "value": -1.8034000000002377,
> > "displayValue": "-1.8034000000002377"
> > },
> > {
> > "name": "Building Story",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "L1_35_Low",
> > "displayValue": "L1_35_Low"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "618131",
> > "displayValue": "618131"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Phase Created",
> > "displayValue": "New Construction",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "External ID",
> > "value": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000",
> > "displayValue": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000"
> > },
> > {
> > "name": "Family Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "0",
> > "displayValue": "0"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Structural Material",
> > "displayValue": "Concrete, Cast-in-Place gray",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": "Cast-in-place concrete",
> > "displayValue": "Cast-in-place concrete"
> > },
> > {
> > "name": "Comments",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Manufacturer",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Model",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "URL",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Cost",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Mark",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "External ID",
> > "value": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed",
> > "displayValue": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1krdmuBkzDbgRKCWsf465_",
> > "displayValue": "1krdmuBkzDbgRKCWsf465_"
> > },
> > {
> > "name": "Keynote",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Color",
> > "value": 9673370,
> > "displayValue": "9673370"
> > },
> > {
> > "name": "Glow",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Shininess",
> > "value": 64,
> > "displayValue": "64"
> > },
> > {
> > "name": "Smoothness",
> > "value": 50,
> > "displayValue": "50"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns",
> > "displayValue": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Behavior",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Class",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Concrete compression",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Lightweight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear strength modification",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Subclass",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Material Type",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Unit weight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "749",
> > "displayValue": "749"
> > }
> > ]
> > }
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2FkYzMy",
> > "name": "CC24x24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Column Location Mark",
> > "value": "A-7"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "24af0ac3-050b-400d-b912-53533aa10f7f-000adc32"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Volume",
> > "value": 1.5904628835839993
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0ahmh31Gj03RaIKrCwgzDD"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular-Column"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Column Style",
> > "value": 0
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "711730"
> > }
> > ]
> > },
> > "references": {
> > "results": [
> > {
> > "name": "Rebar Cover - Top Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Other Faces",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Bottom Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family and Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Base Level",
> > "displayValue": "Top of Footing",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27",
> > "displayValue": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSZ9",
> > "displayValue": "1CEMWRTvz6HwQKgNsRJSZ9"
> > },
> > {
> > "name": "Elevation",
> > "value": -5.3340000000000005,
> > "displayValue": "-5.3340000000000005"
> > },
> > {
> > "name": "Building Story",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "772903",
> > "displayValue": "772903"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Phase Created",
> > "displayValue": "New Construction",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "External ID",
> > "value": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000",
> > "displayValue": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000"
> > },
> > {
> > "name": "Family Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "0",
> > "displayValue": "0"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Structural Material",
> > "displayValue": "Concrete, Cast-in-Place gray",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": "Cast-in-place concrete",
> > "displayValue": "Cast-in-place concrete"
> > },
> > {
> > "name": "Comments",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Manufacturer",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Model",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "URL",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Cost",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Mark",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "External ID",
> > "value": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed",
> > "displayValue": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1krdmuBkzDbgRKCWsf465_",
> > "displayValue": "1krdmuBkzDbgRKCWsf465_"
> > },
> > {
> > "name": "Keynote",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Color",
> > "value": 9673370,
> > "displayValue": "9673370"
> > },
> > {
> > "name": "Glow",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Shininess",
> > "value": 64,
> > "displayValue": "64"
> > },
> > {
> > "name": "Smoothness",
> > "value": 50,
> > "displayValue": "50"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Behavior",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Class",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Concrete compression",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Lightweight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear strength modification",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Subclass",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Material Type",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Unit weight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "749",
> > "displayValue": "749"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Top Level",
> > "displayValue": "L1_37_Med",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "External ID",
> > "value": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54",
> > "displayValue": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3eRW_mgkzCZQysdnuCHXSs",
> > "displayValue": "3eRW_mgkzCZQysdnuCHXSs"
> > },
> > {
> > "name": "Elevation",
> > "value": -1.0541000000000016,
> > "displayValue": "-1.0541000000000016"
> > },
> > {
> > "name": "Building Story",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "618068",
> > "displayValue": "618068"
> > }
> > ]
> > }
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2FkYzMz",
> > "name": "CC24x24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Column Location Mark",
> > "value": "A-6"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "24af0ac3-050b-400d-b912-53533aa10f7f-000adc33"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Volume",
> > "value": 1.5904628835839993
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0ahmh31Gj03RaIKrCwgzDC"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Structural Columns"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular-Column"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Column Style",
> > "value": 0
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "711731"
> > }
> > ]
> > },
> > "references": {
> > "results": [
> > {
> > "name": "Rebar Cover - Top Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Other Faces",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Rebar Cover - Bottom Face",
> > "displayValue": "Interior (framing, columns)",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Length",
> > "value": 0.0381,
> > "displayValue": "0.0381"
> > },
> > {
> > "name": "Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "External ID",
> > "value": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d",
> > "displayValue": "fa6c9949-ac90-4820-8a83-f8f4a449c3fd-00030c3d"
> > },
> > {
> > "name": "Family Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Name",
> > "value": "Interior (framing, columns)",
> > "displayValue": "Interior (framing, columns)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "199741",
> > "displayValue": "199741"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Family and Type",
> > "displayValue": "CC24x24",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6",
> > "displayValue": "e37453ab-55ac-464e-96ef-b2d748a679fc-00093ee6"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "displayValue": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hqSQ",
> > "displayValue": "3ZT5EhLQn6JfRlijT8hqSQ"
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "OmniClass Number",
> > "value": "23.25.30.11.14.11",
> > "displayValue": "23.25.30.11.14.11"
> > },
> > {
> > "name": "OmniClass Title",
> > "value": "Columns",
> > "displayValue": "Columns"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Name",
> > "value": "CC24x24",
> > "displayValue": "CC24x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "displayValue": "Type"
> > },
> > {
> > "name": "Code Name",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Section Name Key",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Section Shape",
> > "value": "NotDefined",
> > "displayValue": "NotDefined"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B10",
> > "displayValue": "B10"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Superstructure",
> > "displayValue": "Superstructure"
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "h",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "b",
> > "value": 0.6096,
> > "displayValue": "0.6096"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "605926",
> > "displayValue": "605926"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Base Level",
> > "displayValue": "Top of Footing",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27",
> > "displayValue": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcb27"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSZ9",
> > "displayValue": "1CEMWRTvz6HwQKgNsRJSZ9"
> > },
> > {
> > "name": "Elevation",
> > "value": -5.3340000000000005,
> > "displayValue": "-5.3340000000000005"
> > },
> > {
> > "name": "Building Story",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "Top of Footing",
> > "displayValue": "Top of Footing"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "772903",
> > "displayValue": "772903"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Phase Created",
> > "displayValue": "New Construction",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "External ID",
> > "value": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000",
> > "displayValue": "42a41bc2-12e7-489c-96cb-c2f1ff6449f1-00000000"
> > },
> > {
> > "name": "Family Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Name",
> > "value": "New Construction",
> > "displayValue": "New Construction"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "0",
> > "displayValue": "0"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Structural Material",
> > "displayValue": "Concrete, Cast-in-Place gray",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": "Cast-in-place concrete",
> > "displayValue": "Cast-in-place concrete"
> > },
> > {
> > "name": "Comments",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Manufacturer",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Model",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "URL",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Cost",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Mark",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "External ID",
> > "value": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed",
> > "displayValue": "6ed67c38-2eef-4d96-a6d4-320da9106393-000002ed"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1krdmuBkzDbgRKCWsf465_",
> > "displayValue": "1krdmuBkzDbgRKCWsf465_"
> > },
> > {
> > "name": "Keynote",
> > "value": "",
> > "displayValue": ""
> > },
> > {
> > "name": "Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Color",
> > "value": 9673370,
> > "displayValue": "9673370"
> > },
> > {
> > "name": "Glow",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Shininess",
> > "value": 64,
> > "displayValue": "64"
> > },
> > {
> > "name": "Smoothness",
> > "value": 50,
> > "displayValue": "50"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete, Cast-in-Place gray",
> > "displayValue": "Concrete, Cast-in-Place gray"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Behavior",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Class",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Concrete compression",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Thermal expansion coefficient Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Lightweight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Poisson ratio Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Shear strength modification",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Subclass",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Material Type",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Unit weight",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus X",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Y",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Young modulus Z",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "749",
> > "displayValue": "749"
> > }
> > ]
> > }
> > }
> > },
> > {
> > "name": "Top Level",
> > "displayValue": "L1_37_Med",
> > "value": {
> > "properties": {
> > "results": [
> > {
> > "name": "Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "External ID",
> > "value": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54",
> > "displayValue": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00096e54"
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "displayValue": "By Type"
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3eRW_mgkzCZQysdnuCHXSs",
> > "displayValue": "3eRW_mgkzCZQysdnuCHXSs"
> > },
> > {
> > "name": "Elevation",
> > "value": -1.0541000000000016,
> > "displayValue": "-1.0541000000000016"
> > },
> > {
> > "name": "Building Story",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Computation Height",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Levels",
> > "displayValue": "Levels"
> > },
> > {
> > "name": "Family Name",
> > "value": "Level",
> > "displayValue": "Level"
> > },
> > {
> > "name": "Element Name",
> > "value": "L1_37_Med",
> > "displayValue": "L1_37_Med"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "618068",
> > "displayValue": "618068"
> > }
> > ]
> > }
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

After working through the steps mentioned above, you should see a screen similar to the following image:
|
> 

## [Step 3: List Elements having Concrete material by using Reference type](#step-3-list-elements-having-concrete-material-by-using-reference-type)

In some cases, the material elements are referenced by Type elements which are in turn referenced by Instance elements. In such case, we would use a query like the following where we list the Type elements referencing the material elements and, for each Type element, list the Instance element referencing it through ‘Type’:

1. In [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/), the query is populated by default in the **Query Pane**. You can also edit or update the query as per your requirement and run it.

> **Query**
>
>
>
>
> > ```
> > query GetInstancesOfConcreteMaterial($elementGroupId: ID!, $propertyFilter: String!) {
> > elementsByElementGroup(
> > elementGroupId: $elementGroupId
> > filter: {query: $propertyFilter}
> > pagination: {limit: 20}
> > ) {
> > results {
> > id
> > name
> > referencedBy(name: "Type") {
> > results {
> > id
> > name
> > properties {
> > results {
> > name
> > value
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
> > - In the Query Variables Pane, replace the value of the `elementGroupId` variable with the `elementGroupId` that you used in [Navigate to Elementgroups](https://aps.autodesk.com/en/docs/aecdatamodel/v1/tutorials/tutorial-01/nav-elements/) of previous tutorial.
> > - In the Query Variables Pane, replace the value of the property filter with the property filter of your choice. For ease of understanding, here we have filtered based on property filter as reference.structural Material.
> > **Note**: For information on the supported metadata filtering options, refer to the [Advanced Filtering Capabilities](https://aps.autodesk.com/en/docs/aecdatamodel/v1/developers_guide/filtering/advanced-filtering/) page.
> >
> >
> >
> >
> > ```
> > {
> > "elementGroupId" : "YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3",
> > "propertyFilter" : "('reference.Structural Material'==YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzJkNjE3 or 'reference.Structural Material'==YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzJlZA) and 'property.name.Element Context'==Type"
> > }
> >
> > ```

2. Click **Play**. The list of element available within that elementGroup of property. The response should be similar to the following code-block:

> **Response**
>
>
>
>
> > ```
> > {
> > "data": {
> > "elementsByElementGroup": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzExMTY",
> > "name": "Concrete 10",
> > "referencedBy": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2EzOTY3",
> > "name": "Concrete 10",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "a4ced9fb-9d2b-4959-b471-ee8544159d58-000a3967"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.25400000000000006
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 377.8558571900037
> > },
> > {
> > "name": "Perimeter",
> > "value": 87.83320000000037
> > },
> > {
> > "name": "Volume",
> > "value": 95.97538772626088
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2apjdxdIj9MRHnxeL47wG$"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 10"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -2.0574000000002375
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.8034000000002377
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "670055"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2EzYTc3",
> > "name": "Concrete 10",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "a4ced9fb-9d2b-4959-b471-ee8544159d58-000a3a77"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.25400000000000006
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 579.6070665900065
> > },
> > {
> > "name": "Perimeter",
> > "value": 111.48060000000027
> > },
> > {
> > "name": "Volume",
> > "value": 147.22019491386166
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2apjdxdIj9MRHnxeL47wSl"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 10"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -1.3081000000000016
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.0541000000000016
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "670327"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2EzYWQ1",
> > "name": "Concrete 10",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "dfa78100-f32f-45a6-9fb4-dddc93e3a134-000a3ad5"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.25400000000000006
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 159.02722248620609
> > },
> > {
> > "name": "Perimeter",
> > "value": 67.48077305895656
> > },
> > {
> > "name": "Volume",
> > "value": 40.39291451149635
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3Vfu40yoz5ff_qtToJwPlX"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 10"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -0.2540000000000018
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.7102397031084183e-15
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "670421"
> > }
> > ]
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzExMTc",
> > "name": "NW Concrete on Metal Deck",
> > "referencedBy": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk3Yzk4",
> > "name": "NW Concrete on Metal Deck",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e86e0fb0-aaef-4c8d-af36-9f1e0c4f7962-00097c98"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.1524
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 83.54402646000003
> > },
> > {
> > "name": "Perimeter",
> > "value": 45.44059999999998
> > },
> > {
> > "name": "Volume",
> > "value": 12.73210963250401
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3eRW_mgkzCZQysdnuCHWNw"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "NW Concrete on Metal Deck"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": 1.5240000000000942
> > },
> > {
> > "name": "Elevation at Top",
> > "value": 1.676400000000094
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "621720"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2EyNjll",
> > "name": "NW Concrete on Metal Deck",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "bdb1b609-ac6e-4ba6-b32d-4a65ac0ef4ab-000a269e"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.1524
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 156.9454008283928
> > },
> > {
> > "name": "Perimeter",
> > "value": 73.44554848844768
> > },
> > {
> > "name": "Volume",
> > "value": 23.91847908624706
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2ziRO9h6vBfhCjIcMi1D8r"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "NW Concrete on Metal Deck"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": 5.587999999999168
> > },
> > {
> > "name": "Elevation at Top",
> > "value": 5.740399999999168
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "665246"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2EzYjY2",
> > "name": "NW Concrete on Metal Deck",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "8a104ef3-17e6-4cd7-a331-ca6ba63448e2-000a3b3a"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.1524
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 101.15270091999926
> > },
> > {
> > "name": "Perimeter",
> > "value": 50.31739999999991
> > },
> > {
> > "name": "Volume",
> > "value": 15.415671620207888
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2A44xp5_PCrwCnockcFdFO"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "NW Concrete on Metal Deck"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": 5.587999999999168
> > },
> > {
> > "name": "Elevation at Top",
> > "value": 5.740399999999168
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "670566"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E3ZWRm",
> > "name": "NW Concrete on Metal Deck",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e62ae598-d012-4038-9417-14692b034bf4-000a7edf"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.1524
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 397.4920679175058
> > },
> > {
> > "name": "Perimeter",
> > "value": 116.01450000000018
> > },
> > {
> > "name": "Volume",
> > "value": 60.57779115062786
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3cAkMOq190E9GN56ah2JKh"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "NW Concrete on Metal Deck"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": 2.311399999999166
> > },
> > {
> > "name": "Elevation at Top",
> > "value": 2.463799999999166
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "687839"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E4MDk5",
> > "name": "NW Concrete on Metal Deck",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "20dabff6-6a34-4506-9139-9613345ec958-000a8099"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.1524
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 618.1691264625672
> > },
> > {
> > "name": "Perimeter",
> > "value": 169.05566528766133
> > },
> > {
> > "name": "Volume",
> > "value": 94.208983798801
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0Wsh$sQZH51f4vbXCqL4d1"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "NW Concrete on Metal Deck"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": 5.587999999999168
> > },
> > {
> > "name": "Elevation at Top",
> > "value": 5.740399999999168
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "688281"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2IxNjk2",
> > "name": "NW Concrete on Metal Deck",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "8dd067d9-b76c-4be9-a85d-5da21e046ea3-000b1696"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.1524
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 655.9258566727385
> > },
> > {
> > "name": "Perimeter",
> > "value": 192.42163189482068
> > },
> > {
> > "name": "Volume",
> > "value": 99.96310055692537
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2Dq6VPjsnBwQXTNQ8U3tWr"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "NW Concrete on Metal Deck"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": 17.77999999999917
> > },
> > {
> > "name": "Elevation at Top",
> > "value": 17.93239999999917
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "726678"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2IxOGFj",
> > "name": "NW Concrete on Metal Deck",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "8dd067d9-b76c-4be9-a85d-5da21e046ea3-000b18ac"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.1524
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": -1.3589000000000002
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 74.7014634999999
> > },
> > {
> > "name": "Perimeter",
> > "value": 34.92499999999998
> > },
> > {
> > "name": "Volume",
> > "value": 11.384503037399986
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2Dq6VPjsnBwQXTNQ8U3tOF"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "NW Concrete on Metal Deck"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": 16.268700000000003
> > },
> > {
> > "name": "Elevation at Top",
> > "value": 16.421100000000003
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "727212"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JkM2Vj",
> > "name": "NW Concrete on Metal Deck",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "3704f37d-d681-4884-bc9d-ae7e6c625ca9-000bd3ec"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.1524
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": -0.7112000000000002
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 36.13347612000043
> > },
> > {
> > "name": "Perimeter",
> > "value": 24.61260000000018
> > },
> > {
> > "name": "Volume",
> > "value": 5.506741760688065
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0t1FDzre58XBoThdviQOz5"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "NW Concrete on Metal Deck"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": 13.00479999999917
> > },
> > {
> > "name": "Elevation at Top",
> > "value": 13.157199999999168
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "775148"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2MxODY3",
> > "name": "NW Concrete on Metal Deck",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "54ce3320-0d0c-4217-b277-cd230cc4e4cb-000c1867"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.1524
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 714.4506154811202
> > },
> > {
> > "name": "Perimeter",
> > "value": 146.15292287127002
> > },
> > {
> > "name": "Volume",
> > "value": 108.8822737993227
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1KpZCW3Gn25x9tpICCoFoi"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "NW Concrete on Metal Deck"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": 9.651999999999168
> > },
> > {
> > "name": "Elevation at Top",
> > "value": 9.804399999999168
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "792679"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2MxODlj",
> > "name": "NW Concrete on Metal Deck",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "54ce3320-0d0c-4217-b277-cd230cc4e4cb-000c189c"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.1524
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 618.4246098225672
> > },
> > {
> > "name": "Perimeter",
> > "value": 169.1572652876613
> > },
> > {
> > "name": "Volume",
> > "value": 94.247919462865
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1KpZCW3Gn25x9tpICCoFnN"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "NW Concrete on Metal Deck"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": 13.71599999999917
> > },
> > {
> > "name": "Elevation at Top",
> > "value": 13.86839999999917
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "792732"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2MyN2M4",
> > "name": "NW Concrete on Metal Deck",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "54ce3320-0d0c-4217-b277-cd230cc4e4cb-000c27c8"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.1524
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 248.4977684597502
> > },
> > {
> > "name": "Perimeter",
> > "value": 88.98159761909731
> > },
> > {
> > "name": "Volume",
> > "value": 37.871059913265924
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1KpZCW3Gn25x9tpICCoCC3"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "NW Concrete on Metal Deck"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": 9.651999999999168
> > },
> > {
> > "name": "Elevation at Top",
> > "value": 9.804399999999168
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "796616"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2MyYWM4",
> > "name": "NW Concrete on Metal Deck",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "54ce3320-0d0c-4217-b277-cd230cc4e4cb-000c2ac8"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.1524
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 238.4340885565714
> > },
> > {
> > "name": "Perimeter",
> > "value": 84.77364374762976
> > },
> > {
> > "name": "Volume",
> > "value": 36.337355096021476
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1KpZCW3Gn25x9tpICCoCu3"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Floor"
> > },
> > {
> > "name": "Element Name",
> > "value": "NW Concrete on Metal Deck"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": 13.71599999999917
> > },
> > {
> > "name": "Elevation at Top",
> > "value": 13.86839999999917
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "797384"
> > }
> > ]
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzFmNDdk",
> > "name": "Bearing Footing - 36\"x18\"",
> > "referencedBy": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2EzZDBj",
> > "name": "Bearing Footing - 36\"x18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Eccentricity",
> > "value": 0
> > },
> > {
> > "name": "Length",
> > "value": 18.669000000000008
> > },
> > {
> > "name": "Width",
> > "value": 0.9144000000000001
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "8a104ef3-17e6-4cd7-a331-ca6ba63448e2-000a3d0c"
> > },
> > {
> > "name": "Volume",
> > "value": 7.9959695564160045
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2A44xp5_PCrwCnockcFdNk"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Wall Foundation"
> > },
> > {
> > "name": "Element Name",
> > "value": "Bearing Footing - 36\"x18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.791200000000001
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3340000000000005
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "670988"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2EzZDE5",
> > "name": "Bearing Footing - 36\"x18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Eccentricity",
> > "value": 0
> > },
> > {
> > "name": "Length",
> > "value": 10.058400000000002
> > },
> > {
> > "name": "Width",
> > "value": 0.9144000000000001
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "8a104ef3-17e6-4cd7-a331-ca6ba63448e2-000a3d19"
> > },
> > {
> > "name": "Volume",
> > "value": 3.9502000995840008
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2A44xp5_PCrwCnockcFdNx"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Wall Foundation"
> > },
> > {
> > "name": "Element Name",
> > "value": "Bearing Footing - 36\"x18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.791200000000001
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3340000000000005
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "671001"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2EzZDI1",
> > "name": "Bearing Footing - 36\"x18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Eccentricity",
> > "value": 0
> > },
> > {
> > "name": "Length",
> > "value": 19.464461598735145
> > },
> > {
> > "name": "Width",
> > "value": 0.9144000000000001
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "8a104ef3-17e6-4cd7-a331-ca6ba63448e2-000a3d25"
> > },
> > {
> > "name": "Volume",
> > "value": 7.896303433440501
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2A44xp5_PCrwCnockcFdN7"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Wall Foundation"
> > },
> > {
> > "name": "Element Name",
> > "value": "Bearing Footing - 36\"x18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.791200000000001
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3340000000000005
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "671013"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2EzZDJl",
> > "name": "Bearing Footing - 36\"x18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Eccentricity",
> > "value": 0
> > },
> > {
> > "name": "Length",
> > "value": 9.496553359763839
> > },
> > {
> > "name": "Width",
> > "value": 0.9144000000000001
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "8a104ef3-17e6-4cd7-a331-ca6ba63448e2-000a3d2e"
> > },
> > {
> > "name": "Volume",
> > "value": 4.025525020913802
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2A44xp5_PCrwCnockcFdNC"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Wall Foundation"
> > },
> > {
> > "name": "Element Name",
> > "value": "Bearing Footing - 36\"x18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.791200000000001
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3340000000000005
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "671022"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2EzZDM3",
> > "name": "Bearing Footing - 36\"x18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Eccentricity",
> > "value": 0
> > },
> > {
> > "name": "Length",
> > "value": 21.664245226147976
> > },
> > {
> > "name": "Width",
> > "value": 0.9144000000000001
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "8a104ef3-17e6-4cd7-a331-ca6ba63448e2-000a3d37"
> > },
> > {
> > "name": "Volume",
> > "value": 8.78815541895969
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2A44xp5_PCrwCnockcFdNL"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Wall Foundation"
> > },
> > {
> > "name": "Element Name",
> > "value": "Bearing Footing - 36\"x18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.791200000000001
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3340000000000005
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "671031"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2EzZDQz",
> > "name": "Bearing Footing - 36\"x18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Eccentricity",
> > "value": 0
> > },
> > {
> > "name": "Length",
> > "value": 7.549263384998224
> > },
> > {
> > "name": "Width",
> > "value": 0.9144000000000001
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "8a104ef3-17e6-4cd7-a331-ca6ba63448e2-000a3d43"
> > },
> > {
> > "name": "Volume",
> > "value": 2.6905576913770344
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2A44xp5_PCrwCnockcFdMX"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Wall Foundation"
> > },
> > {
> > "name": "Element Name",
> > "value": "Bearing Footing - 36\"x18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.791200000000001
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3340000000000005
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "671043"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2EzZDY3",
> > "name": "Bearing Footing - 36\"x18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Eccentricity",
> > "value": 0
> > },
> > {
> > "name": "Length",
> > "value": 14.770100000000241
> > },
> > {
> > "name": "Width",
> > "value": 0.9144000000000001
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "8a104ef3-17e6-4cd7-a331-ca6ba63448e2-000a3d67"
> > },
> > {
> > "name": "Volume",
> > "value": 5.728852026144099
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2A44xp5_PCrwCnockcFdM5"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Wall Foundation"
> > },
> > {
> > "name": "Element Name",
> > "value": "Bearing Footing - 36\"x18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.791200000000001
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3340000000000005
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "671079"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E1MzE5",
> > "name": "Bearing Footing - 36\"x18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Eccentricity",
> > "value": 0
> > },
> > {
> > "name": "Length",
> > "value": 24.879300000000004
> > },
> > {
> > "name": "Width",
> > "value": 0.9144000000000001
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "0b0a2419-9317-4b98-9c16-1b23aa188460-000a5319"
> > },
> > {
> > "name": "Volume",
> > "value": 9.764002665504002
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0B2YGPanTBc9mM6oEg4jTv"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Wall Foundation"
> > },
> > {
> > "name": "Element Name",
> > "value": "Bearing Footing - 36\"x18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.791200000000001
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3340000000000005
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "676633"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E1NTVm",
> > "name": "Bearing Footing - 36\"x18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Eccentricity",
> > "value": 0
> > },
> > {
> > "name": "Length",
> > "value": 15.354299999999972
> > },
> > {
> > "name": "Width",
> > "value": 0.9144000000000001
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "0c51dbea-26e1-44bb-b62d-61ced65e7691-000a555f"
> > },
> > {
> > "name": "Volume",
> > "value": 6.03679773283199
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0CKTlg9k54kxOjOSxML2FE"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Wall Foundation"
> > },
> > {
> > "name": "Element Name",
> > "value": "Bearing Footing - 36\"x18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.791200000000001
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3340000000000005
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "677215"
> > }
> > ]
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzIzNmM0",
> > "name": "FNDN-6",
> > "referencedBy": {
> > "results": []
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzIzNzAw",
> > "name": "FNDN-12",
> > "referencedBy": {
> > "results": []
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzIzNzAx",
> > "name": "FNDN-8",
> > "referencedBy": {
> > "results": []
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzIzNzAy",
> > "name": "FNDN-10",
> > "referencedBy": {
> > "results": []
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzI4ZDNk",
> > "name": "CB24x30",
> > "referencedBy": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmE1",
> > "name": "CB24x30",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942a5"
> > },
> > {
> > "name": "Volume",
> > "value": 1.9310516217599893
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpjP"
> > },
> > {
> > "name": "Length",
> > "value": 6.692900000000244
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB24x30"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_35_Low"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -2.5654000000002393
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.8034000000002393
> > },
> > {
> > "name": "Cut Length",
> > "value": 6.235700000000001
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606885"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmE5",
> > "name": "CB24x30",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942a9"
> > },
> > {
> > "name": "Volume",
> > "value": 2.170958238720059
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpjL"
> > },
> > {
> > "name": "Length",
> > "value": 7.772400000000245
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB24x30"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_35_Low"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Start Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -2.5654000000002393
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.8034000000002393
> > },
> > {
> > "name": "Cut Length",
> > "value": 7.010400000000229
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606889"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmFi",
> > "name": "CB24x30",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942ab"
> > },
> > {
> > "name": "Volume",
> > "value": 0.4719474432000058
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpjN"
> > },
> > {
> > "name": "Length",
> > "value": 1.80339999999998
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB24x30"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_35_Low"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Start Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -2.5654000000002393
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.8034000000002393
> > },
> > {
> > "name": "Cut Length",
> > "value": 1.523999999999998
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606891"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmFk",
> > "name": "CB24x30",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942ad"
> > },
> > {
> > "name": "Volume",
> > "value": 1.9310516217600204
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpjH"
> > },
> > {
> > "name": "Length",
> > "value": 6.692900000000243
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB24x30"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Estimated Reinforcement Volume",
> > "value": 0.029204478256080555
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_35_Low"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -2.5654000000002393
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.8034000000002393
> > },
> > {
> > "name": "Cut Length",
> > "value": 6.235700000000001
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606893"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmFm",
> > "name": "CB24x30",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942af"
> > },
> > {
> > "name": "Volume",
> > "value": 2.1709582387200927
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpjJ"
> > },
> > {
> > "name": "Length",
> > "value": 7.6200000000002275
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB24x30"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Estimated Reinforcement Volume",
> > "value": 0.017650103616342186
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_35_Low"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Start Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -2.5654000000002393
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.8034000000002393
> > },
> > {
> > "name": "Cut Length",
> > "value": 7.010400000000228
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606895"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmI1",
> > "name": "CB24x30",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942b5"
> > },
> > {
> > "name": "Volume",
> > "value": 1.9310516217600142
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpj9"
> > },
> > {
> > "name": "Length",
> > "value": 6.845299999999999
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB24x30"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_37_Med"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -1.8161000000000032
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.0541000000000031
> > },
> > {
> > "name": "Cut Length",
> > "value": 6.235700000000002
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606901"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmI3",
> > "name": "CB24x30",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942b7"
> > },
> > {
> > "name": "Volume",
> > "value": 2.1709582387200883
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpjB"
> > },
> > {
> > "name": "Length",
> > "value": 7.620000000000225
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB24x30"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_37_Med"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Start Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -1.8161000000000032
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.0541000000000031
> > },
> > {
> > "name": "Cut Length",
> > "value": 7.010400000000229
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606903"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmI4",
> > "name": "CB24x30",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942b8"
> > },
> > {
> > "name": "Volume",
> > "value": 1.9389174124800226
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpj4"
> > },
> > {
> > "name": "Length",
> > "value": 6.870700000000017
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB24x30"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_37_Med"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Start Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -1.8161000000000032
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.0541000000000031
> > },
> > {
> > "name": "Cut Length",
> > "value": 6.261100000000019
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606904"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmI5",
> > "name": "CB24x30",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942b9"
> > },
> > {
> > "name": "Volume",
> > "value": 1.9585818892799847
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpj5"
> > },
> > {
> > "name": "Length",
> > "value": 7.5437999999999965
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB24x30"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_37_Med"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -1.8161000000000032
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.0541000000000031
> > },
> > {
> > "name": "Cut Length",
> > "value": 6.934200000000001
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606905"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmJj",
> > "name": "CB24x30",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942bc"
> > },
> > {
> > "name": "Volume",
> > "value": 2.1709582387200497
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpj0"
> > },
> > {
> > "name": "Length",
> > "value": 7.467600000000227
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB24x30"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_37_Med"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Start Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -1.8161000000000032
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.0541000000000031
> > },
> > {
> > "name": "Cut Length",
> > "value": 7.010400000000234
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606908"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmJk",
> > "name": "CB24x30",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942bd"
> > },
> > {
> > "name": "Volume",
> > "value": 1.2073988755199978
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpj1"
> > },
> > {
> > "name": "Length",
> > "value": 4.3306999999999976
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB24x30"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_37_Med"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -1.8161000000000032
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.0541000000000031
> > },
> > {
> > "name": "Cut Length",
> > "value": 3.8988999999999985
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606909"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmJl",
> > "name": "CB24x30",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942be"
> > },
> > {
> > "name": "Volume",
> > "value": 1.958581889279987
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpj2"
> > },
> > {
> > "name": "Length",
> > "value": 7.499960438660746
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB24x30"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_37_Med"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -1.8161000000000032
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.0541000000000031
> > },
> > {
> > "name": "Cut Length",
> > "value": 6.934200000000003
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606910"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmMw",
> > "name": "CB24x30",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942c0"
> > },
> > {
> > "name": "Volume",
> > "value": 2.1709582387200532
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpiy"
> > },
> > {
> > "name": "Length",
> > "value": 7.620000000000224
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB24x30"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_37_Med"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Start Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -1.8161000000000032
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.0541000000000031
> > },
> > {
> > "name": "Cut Length",
> > "value": 7.010400000000223
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606912"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmMx",
> > "name": "CB24x30",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942c1"
> > },
> > {
> > "name": "Volume",
> > "value": 1.938917412479981
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpiz"
> > },
> > {
> > "name": "Length",
> > "value": 6.823656153385574
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB24x30"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_37_Med"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Start Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -1.8161000000000032
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.0541000000000031
> > },
> > {
> > "name": "Cut Length",
> > "value": 6.261100000000019
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606913"
> > }
> > ]
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzJkNjE0",
> > "name": "Retaining Footing - 24\" x 12\" x 12\"",
> > "referencedBy": {
> > "results": []
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzJlYQ",
> > "name": "Foundation Concrete 12\"",
> > "referencedBy": {
> > "results": []
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzJlYg",
> > "name": "Concrete 12\"",
> > "referencedBy": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhlZTVh",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.5146000000000166
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008ee5a"
> > },
> > {
> > "name": "Area",
> > "value": 65.91277140000146
> > },
> > {
> > "name": "Volume",
> > "value": 20.090212722720445
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC1hI"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 28.575000000000475
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "585306"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmMWNm",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 1.9557999999999853
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f1cf"
> > },
> > {
> > "name": "Area",
> > "value": 34.99218808000055
> > },
> > {
> > "name": "Volume",
> > "value": 10.605838917312166
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC0L7"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 23.393400000000714
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "586191"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmMjMz",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 3.3147000000000344
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f233"
> > },
> > {
> > "name": "Area",
> > "value": 70.41179466000294
> > },
> > {
> > "name": "Volume",
> > "value": 21.435361258224884
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC0Qx"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 23.393400000000714
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "586291"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmMmQ5",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.857500000000009
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f2d9"
> > },
> > {
> > "name": "Area",
> > "value": 82.37886750000163
> > },
> > {
> > "name": "Volume",
> > "value": 25.034353802160474
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC0PH"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 28.575000000000475
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "586457"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmMzRh",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 3.314700000000035
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f34a"
> > },
> > {
> > "name": "Area",
> > "value": 41.209272420002286
> > },
> > {
> > "name": "Volume",
> > "value": 12.560586233616677
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC0V2"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": -1.8033999999999994
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 23.39340000000047
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "586570"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmMzk4",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 7.327900000000009
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f398"
> > },
> > {
> > "name": "Area",
> > "value": 171.42449586000367
> > },
> > {
> > "name": "Volume",
> > "value": 52.21656008280114
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC0SG"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": -1.8034000000000017
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 23.393400000000476
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "586648"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmNDMx",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 7.327899999999999
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f431"
> > },
> > {
> > "name": "Area",
> > "value": 164.46273559000352
> > },
> > {
> > "name": "Volume",
> > "value": 49.387743159801055
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC02v"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": -1.0541
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 22.64410000000047
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "586801"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmNDMy",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.8575000000000004
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f432"
> > },
> > {
> > "name": "Area",
> > "value": 35.274606870001385
> > },
> > {
> > "name": "Volume",
> > "value": 10.751700173976419
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC02w"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": -1.0541000000000018
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 22.644100000000478
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "586802"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmNDMz",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 7.3279
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f433"
> > },
> > {
> > "name": "Area",
> > "value": 164.80596071000343
> > },
> > {
> > "name": "Volume",
> > "value": 49.42510566572102
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC02x"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": -1.0541
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 22.64410000000047
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "586803"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmNTE4",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 6.8580000000000005
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f518"
> > },
> > {
> > "name": "Area",
> > "value": 38.20637519999999
> > },
> > {
> > "name": "Volume",
> > "value": 11.645303160959996
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC06G"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 4
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.333999999999999
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "587032"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmNTE5",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.933699999999998
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f519"
> > },
> > {
> > "name": "Area",
> > "value": 16.054806599999985
> > },
> > {
> > "name": "Volume",
> > "value": 4.893505051679995
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC06H"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 4
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.333999999999999
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "587033"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmNjM1",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.8575000000000004
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f635"
> > },
> > {
> > "name": "Area",
> > "value": 58.319722070001134
> > },
> > {
> > "name": "Volume",
> > "value": 16.172606493432287
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC0Az"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 22.644100000000478
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "587317"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmNmRm",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 7.251699999999998
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f6df"
> > },
> > {
> > "name": "Area",
> > "value": 33.20332068999998
> > },
> > {
> > "name": "Volume",
> > "value": 10.120372146311986
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC09N"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": -1.0541
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.279899999999999
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "587487"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzkxOTg1",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.857499999999998
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2cb1b462-f180-4310-a157-58a1e14d3eb8-00091985"
> > },
> > {
> > "name": "Area",
> > "value": 55.984081580001735
> > },
> > {
> > "name": "Volume",
> > "value": 17.063948065584526
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0iiRHYyO134A5NMA7XH2Sz"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 21.590000000000472
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "596357"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzkxOTg2",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.8574999999999986
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2cb1b462-f180-4310-a157-58a1e14d3eb8-00091986"
> > },
> > {
> > "name": "Area",
> > "value": 50.33860900000104
> > },
> > {
> > "name": "Volume",
> > "value": 15.343208023200313
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0iiRHYyO134A5NMA7XH2S_"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 21.590000000000472
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "596358"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzkxOWZm",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 6.8580000000000005
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2cb1b462-f180-4310-a157-58a1e14d3eb8-000919ff"
> > },
> > {
> > "name": "Area",
> > "value": 141.48358800000312
> > },
> > {
> > "name": "Volume",
> > "value": 43.12419762240094
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0iiRHYyO134A5NMA7XH2T7"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 21.590000000000472
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "596479"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzkxYTAw",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 6.857999999999998
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2cb1b462-f180-4310-a157-58a1e14d3eb8-00091a00"
> > },
> > {
> > "name": "Area",
> > "value": 148.06422000000325
> > },
> > {
> > "name": "Volume",
> > "value": 45.12997425600099
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0iiRHYyO134A5NMA7XH2Iu"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 21.590000000000472
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "596480"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E1MGUy",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.0319999999999854
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "0b0a2419-9317-4b98-9c16-1b23aa188460-000a50e2"
> > },
> > {
> > "name": "Area",
> > "value": 6.2606326399994705
> > },
> > {
> > "name": "Volume",
> > "value": 1.9082408286718384
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0B2YGPanTBc9mM6oEg4jI2"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.181599999999764
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "676066"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2MzYzJi",
> > "name": "Concrete 12\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.933699999999998
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "a4e0d7bb-e129-4834-9aa3-04a969f3b7e3-000c3c2b"
> > },
> > {
> > "name": "Area",
> > "value": 13.61610179999999
> > },
> > {
> > "name": "Volume",
> > "value": 4.1501878286399965
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2auDUxuIb8D9gZ1Abf$ul8"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 12\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 4
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.333999999999999
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "801835"
> > }
> > ]
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzkyOWNj",
> > "name": "Concrete 30\"",
> > "referencedBy": {
> > "results": []
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzlmNzU",
> > "name": "Concrete 10\"",
> > "referencedBy": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhlZDcw",
> > "name": "Concrete 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.819400000000005
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008ed70"
> > },
> > {
> > "name": "Area",
> > "value": 72.49146792000235
> > },
> > {
> > "name": "Volume",
> > "value": 18.269609912320657
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC1du"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 10\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 23.393400000000714
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "585072"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhlZGQ2",
> > "name": "Concrete 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.5146000000000175
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008edd6"
> > },
> > {
> > "name": "Area",
> > "value": 58.579882840002185
> > },
> > {
> > "name": "Volume",
> > "value": 14.174482618720464
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC1bU"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 10\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 23.393400000000714
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "585174"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhlZTI3",
> > "name": "Concrete 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.9210000000000034
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008ee27"
> > },
> > {
> > "name": "Area",
> > "value": 11.740621679999267
> > },
> > {
> > "name": "Volume",
> > "value": 2.9821179067198096
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC1gl"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 10\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.181599999999764
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "585255"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmMTQz",
> > "name": "Concrete 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.7939999999999
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f143"
> > },
> > {
> > "name": "Area",
> > "value": 69.01921679999917
> > },
> > {
> > "name": "Volume",
> > "value": 17.53088106719976
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC0NB"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 10\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 22.644100000000478
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "586051"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmMTQ0",
> > "name": "Concrete 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.5146000000000166
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f144"
> > },
> > {
> > "name": "Area",
> > "value": 56.94085386000159
> > },
> > {
> > "name": "Volume",
> > "value": 14.462976880440408
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC0NC"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 10\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 22.644100000000478
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "586052"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmMTQ1",
> > "name": "Concrete 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.7939999999999006
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f145"
> > },
> > {
> > "name": "Area",
> > "value": 46.42893939999868
> > },
> > {
> > "name": "Volume",
> > "value": 11.792950607599652
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC0ND"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 10\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 22.644100000000478
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "586053"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmMTQ2",
> > "name": "Concrete 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.5146000000000166
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f146"
> > },
> > {
> > "name": "Area",
> > "value": 51.18925246000148
> > },
> > {
> > "name": "Volume",
> > "value": 13.002070124840367
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC0NE"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 10\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 22.644100000000478
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "586054"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E4YzZk",
> > "name": "Concrete 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.61620000000001
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "7a1e6691-5fd6-4bac-8787-4c90364f0d84-000a8c6d"
> > },
> > {
> > "name": "Area",
> > "value": 14.913841140000054
> > },
> > {
> > "name": "Volume",
> > "value": 3.7881156495600115
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1w7cQHNzPBh8U7J90sHO7f"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 10\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 4
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.9309
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "691309"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E4YzZl",
> > "name": "Concrete 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.8955999999999054
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "7a1e6691-5fd6-4bac-8787-4c90364f0d84-000a8c6e"
> > },
> > {
> > "name": "Area",
> > "value": 17.724480679999445
> > },
> > {
> > "name": "Volume",
> > "value": 4.502018092719853
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1w7cQHNzPBh8U7J90sHO7g"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 10\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 4
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.9309
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "691310"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2I5NmI3",
> > "name": "Concrete 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.9210000000000034
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "bcffb50b-5a04-494e-b53c-8d7db89adae1-000b96b7"
> > },
> > {
> > "name": "Area",
> > "value": 13.161263999999417
> > },
> > {
> > "name": "Volume",
> > "value": 3.342961055999861
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2y$xKBMWH9JhKyZNsuaKnM"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 10\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.181599999999764
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "759479"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2MyMWI1",
> > "name": "Concrete 10\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.819400000000005
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "54ce3320-0d0c-4217-b277-cd230cc4e4cb-000c21b5"
> > },
> > {
> > "name": "Area",
> > "value": 54.24311732000153
> > },
> > {
> > "name": "Volume",
> > "value": 13.250416079760145
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1KpZCW3Gn25x9tpICCoCL_"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 10\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 23.393400000000714
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "795061"
> > }
> > ]
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzlmOWU",
> > "name": "Concrete 8\"",
> > "referencedBy": {
> > "results": []
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0MDRk",
> > "name": "30x30x25'",
> > "referencedBy": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0MDVk",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "8a104ef3-17e6-4cd7-a331-ca6ba63448e2-000a405d"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2A44xp5_PCrwCnockcFWY$"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Estimated Reinforcement Volume",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "671837"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NTFl",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a451e"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhro3"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673054"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NTFm",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a451f"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhro2"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673055"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NTIw",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a4520"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhroz"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673056"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NTIx",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a4521"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 2.1657342585967855e-15
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhroy"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999887
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673057"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NTIy",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a4522"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhro$"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673058"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NTIz",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a4523"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhro_"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673059"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NTI0",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a4524"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhrov"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673060"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NTI1",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a4525"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhrou"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673061"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NTI2",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a4526"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhrox"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673062"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NTI3",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a4527"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhrow"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673063"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NTI4",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a4528"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 3.0226383129071885e-18
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhror"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673064"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NTJh",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a452a"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 1.0828671292983927e-15
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhrot"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673066"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NTJi",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a452b"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhros"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673067"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NTJj",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a452c"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhron"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673068"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NWFl",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a45ae"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhrmp"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673198"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0NWI2",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "2632a2eb-c20e-40b7-8fc4-4ed71ba5199d-000a45b6"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0cCgBhmWv0ju$4JjSRhrmh"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "673206"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2YTA5",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6a09"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0.07619999999989388
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEnp"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.334999999999892
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.7149999999998915
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "682505"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JjZjA0",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcf04"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 2.1657342585967855e-15
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSpg"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999887
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "773892"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JjZjBm",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "4c39681b-779f-4647-a694-a97d9b4603ee-000bcf0f"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 2.1657342585967855e-15
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1CEMWRTvz6HwQKgNsRJSpX"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999887
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "773903"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmY2Jj",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e0ca0049-da9c-4b7d-acb9-c4ffd7416a1c-000bfcbc"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3WoW19sfnBVQovnF$NIfQW"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "785596"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2MzNDc2",
> > "name": "30x30x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "5da02e07-8605-4434-9834-37808478436f-000c3476"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Te2u7XWL4D9WqDu24T7SP"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "30x30x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999888
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "799862"
> > }
> > ]
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0ZTVk",
> > "name": "FNDN-36",
> > "referencedBy": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2MmVk",
> > "name": "FNDN-36",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 4.1910000000000105
> > },
> > {
> > "name": "Width",
> > "value": 4.4703999999999064
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "9bb7de5c-5395-4e8d-83ae-c451a0c42cf3-000a62ed"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.9144000000000001
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 18.735446399999642
> > },
> > {
> > "name": "Perimeter",
> > "value": 17.32279999999983
> > },
> > {
> > "name": "Volume",
> > "value": 17.131692188159676
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2RjzvSKvLEZOEkn56WpauU"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Foundation Slab"
> > },
> > {
> > "name": "Element Name",
> > "value": "FNDN-36"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -7.899400000000003
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -6.985000000000002
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "680685"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2MzE0",
> > "name": "FNDN-36",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 9.004300000000017
> > },
> > {
> > "name": "Width",
> > "value": 7.835899999999965
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "9bb7de5c-5395-4e8d-83ae-c451a0c42cf3-000a6314"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.9144000000000001
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 55.521340569999694
> > },
> > {
> > "name": "Perimeter",
> > "value": 33.68039999999993
> > },
> > {
> > "name": "Volume",
> > "value": 50.76871381720772
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2RjzvSKvLEZOEkn56Wpa$d"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Foundation Slab"
> > },
> > {
> > "name": "Element Name",
> > "value": "FNDN-36"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -7.899400000000003
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -6.985000000000002
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "680724"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmNzBi",
> > "name": "FNDN-36",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 4.5339
> > },
> > {
> > "name": "Width",
> > "value": 9.004300000000002
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "f91478b8-6352-4c8c-b922-df750a8f322d-000bf70b"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.9144000000000001
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 40.824595769999995
> > },
> > {
> > "name": "Perimeter",
> > "value": 27.076399999999996
> > },
> > {
> > "name": "Volume",
> > "value": 37.33001037208799
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3v57YuOr9CZBaYttKAXCKc"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Foundation Slab"
> > },
> > {
> > "name": "Element Name",
> > "value": "FNDN-36"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -6.248400000000001
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3340000000000005
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "784139"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmNzNk",
> > "name": "FNDN-36",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 4.5339
> > },
> > {
> > "name": "Width",
> > "value": 8.382000000000007
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "f91478b8-6352-4c8c-b922-df750a8f322d-000bf73d"
> > },
> > {
> > "name": "Thickness",
> > "value": 0.9144000000000001
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Area",
> > "value": 38.0031498
> > },
> > {
> > "name": "Perimeter",
> > "value": 25.8318
> > },
> > {
> > "name": "Volume",
> > "value": 34.75008017712
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3v57YuOr9CZBaYttKAXCKG"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Foundation Slab"
> > },
> > {
> > "name": "Element Name",
> > "value": "FNDN-36"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Slope",
> > "value": null
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -6.248400000000001
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3340000000000005
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "784189"
> > }
> > ]
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0ZmNk",
> > "name": "Concrete 18\"",
> > "referencedBy": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmNTFh",
> > "name": "Concrete 18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 10.033000000000243
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f51a"
> > },
> > {
> > "name": "Area",
> > "value": 47.98459000378657
> > },
> > {
> > "name": "Volume",
> > "value": 21.91197441304352
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC06I"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 4
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.333999999999999
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "587034"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3XzhmNmUx",
> > "name": "Concrete 18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 7.2517000000000005
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "63f8d234-f38c-4508-90c8-59b76e38f488-0008f6e1"
> > },
> > {
> > "name": "Area",
> > "value": 33.31944948999998
> > },
> > {
> > "name": "Volume",
> > "value": 15.215954277708
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Z_D8qyun52938MRTkC09f"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": -1.0541
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.279899999999999
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "587489"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E0Zjg4",
> > "name": "Concrete 18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 3.1622999999999397
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "0b0a2419-9317-4b98-9c16-1b23aa188460-000a4f88"
> > },
> > {
> > "name": "Area",
> > "value": 15.596097839998976
> > },
> > {
> > "name": "Volume",
> > "value": 7.130535932447531
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0B2YGPanTBc9mM6oEg4ile"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.181599999999764
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "675720"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E1M2Zk",
> > "name": "Concrete 18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.5146000000000166
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "0c51dbea-26e1-44bb-b62d-61ced65e7691-000a53fd"
> > },
> > {
> > "name": "Area",
> > "value": 14.345777759999429
> > },
> > {
> > "name": "Volume",
> > "value": 6.558889591871739
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "0CKTlg9k54kxOjOSxML2Li"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.181599999999764
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "676861"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E3Nzcy",
> > "name": "Concrete 18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.9337000000000004
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "4ea3c6f3-8f70-427d-891c-9095033ac8eb-000a7772"
> > },
> > {
> > "name": "Area",
> > "value": 7.851113329999943
> > },
> > {
> > "name": "Volume",
> > "value": 3.5895290144759553
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1EeyRpZt12VOaSa9K3CB_P"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.2799
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "685938"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E4YzZj",
> > "name": "Concrete 18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.8955999999999062
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "7a1e6691-5fd6-4bac-8787-4c90364f0d84-000a8c6c"
> > },
> > {
> > "name": "Area",
> > "value": 13.570940599999366
> > },
> > {
> > "name": "Volume",
> > "value": 6.060427879119723
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1w7cQHNzPBh8U7J90sHO7e"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 4
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.9309
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "691308"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E4YzZm",
> > "name": "Concrete 18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 2.61620000000001
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "7a1e6691-5fd6-4bac-8787-4c90364f0d84-000a8c6f"
> > },
> > {
> > "name": "Area",
> > "value": 16.06738722000005
> > },
> > {
> > "name": "Volume",
> > "value": 7.216223890104007
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1w7cQHNzPBh8U7J90sHO7h"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": 0
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 4
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": 0
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.9309
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "691311"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2U0N2Yy",
> > "name": "Concrete 18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 3.431311253883248
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "54d0215b-3923-47b8-beb3-55f8d5cea386-000e47f2"
> > },
> > {
> > "name": "Area",
> > "value": 15.796759268170508
> > },
> > {
> > "name": "Volume",
> > "value": 9.112804250131353
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Kq25REID7kBwpLVZLmEHq"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": -5.461000000000093
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0.052359877559829834
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": true
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6981395244758577
> > },
> > {
> > "name": "Top Width",
> > "value": 0.45720000000000005
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.8636000000000001
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.597400000000093
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "935922"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2U0N2Yz",
> > "name": "Concrete 18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Center Mark Visible",
> > "value": true
> > },
> > {
> > "name": "Length",
> > "value": 14.961835012721474
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "54d0215b-3923-47b8-beb3-55f8d5cea386-000e47f3"
> > },
> > {
> > "name": "Area",
> > "value": 70.43639325438677
> > },
> > {
> > "name": "Volume",
> > "value": 39.46669429675495
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Kq25REID7kBwpLVZLmEHr"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": -5.461000000000093
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0.052359877559829834
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": true
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6981395244758577
> > },
> > {
> > "name": "Top Width",
> > "value": 0.45720000000000005
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.8636000000000001
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.597400000000093
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "935923"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2U0N2Y0",
> > "name": "Concrete 18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Center Mark Visible",
> > "value": true
> > },
> > {
> > "name": "Length",
> > "value": 7.280415698942867
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "54d0215b-3923-47b8-beb3-55f8d5cea386-000e47f4"
> > },
> > {
> > "name": "Area",
> > "value": 36.52750365067555
> > },
> > {
> > "name": "Volume",
> > "value": 19.668609073178775
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Kq25REID7kBwpLVZLmEHo"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": -5.461000000000093
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0.052359877559829834
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": true
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6981395244758577
> > },
> > {
> > "name": "Top Width",
> > "value": 0.45720000000000005
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.8636000000000001
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.597400000000093
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "935924"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2U0N2Y1",
> > "name": "Concrete 18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 15.238042863510803
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "54d0215b-3923-47b8-beb3-55f8d5cea386-000e47f5"
> > },
> > {
> > "name": "Area",
> > "value": 70.70271728347457
> > },
> > {
> > "name": "Volume",
> > "value": 40.75416129671253
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Kq25REID7kBwpLVZLmEHp"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": -5.461000000000093
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0.052359877559829834
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": true
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6981395244758577
> > },
> > {
> > "name": "Top Width",
> > "value": 0.45720000000000005
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.8636000000000001
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.597400000000093
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "935925"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2U0N2Y2",
> > "name": "Concrete 18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 12.5646005405664
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "54d0215b-3923-47b8-beb3-55f8d5cea386-000e47f6"
> > },
> > {
> > "name": "Area",
> > "value": 58.42491922540825
> > },
> > {
> > "name": "Volume",
> > "value": 33.65545783498836
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Kq25REID7kBwpLVZLmEHm"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": -5.461000000000093
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0.052359877559829834
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": true
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6981395244758577
> > },
> > {
> > "name": "Top Width",
> > "value": 0.45720000000000005
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.8636000000000001
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.597400000000093
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "935926"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2U0YjNh",
> > "name": "Concrete 18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 12.894761641529549
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "54d0215b-3923-47b8-beb3-55f8d5cea386-000e4b3a"
> > },
> > {
> > "name": "Area",
> > "value": 38.335897145217935
> > },
> > {
> > "name": "Volume",
> > "value": 20.56639335613854
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Kq25REID7kBwpLVZLmEYy"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": -5.461000000000093
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0.052359877559829834
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": true
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6169389112547095
> > },
> > {
> > "name": "Top Width",
> > "value": 0.45720000000000005
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": -2.4130000000000003
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 3.048000000000093
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "936762"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2U0YjNi",
> > "name": "Concrete 18\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Length",
> > "value": 13.129803964473885
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "54d0215b-3923-47b8-beb3-55f8d5cea386-000e4b3b"
> > },
> > {
> > "name": "Area",
> > "value": 39.04908672102197
> > },
> > {
> > "name": "Volume",
> > "value": 20.95112160533243
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "1Kq25REID7kBwpLVZLmEYz"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Concrete 18\""
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false
> > },
> > {
> > "name": "Room Bounding",
> > "value": true
> > },
> > {
> > "name": "Base Offset",
> > "value": -5.461000000000093
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Base is Attached",
> > "value": false
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered"
> > },
> > {
> > "name": "Location Line",
> > "value": 2
> > },
> > {
> > "name": "Structural",
> > "value": true
> > },
> > {
> > "name": "Structural Usage",
> > "value": 1
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0.052359877559829834
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": true
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6169389112547181
> > },
> > {
> > "name": "Top Width",
> > "value": 0.45720000000000005
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0
> > },
> > {
> > "name": "Top is Attached",
> > "value": false
> > },
> > {
> > "name": "Top Offset",
> > "value": -2.4130000000000003
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 3.048000000000093
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "936763"
> > }
> > ]
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2OTVh",
> > "name": "24x24x25'",
> > "referencedBy": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2Yjli",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6b9b"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0.07619999999989388
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEtX"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Estimated Reinforcement Volume",
> > "value": 0.05394776452162999
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.334999999999892
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.7149999999998915
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "682907"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2YzU0",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6c54"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0.07619999999989388
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEek"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.334999999999892
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.7149999999998915
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683092"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDFh",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d1a"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0.07619999999989388
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjW"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.334999999999892
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.7149999999998915
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683290"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDFj",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d1c"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0.07619999999989388
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjc"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.334999999999892
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.7149999999998915
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683292"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDFl",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d1e"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0.07619999999989388
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEja"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.334999999999868
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.714999999999867
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683294"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDIw",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d20"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0.07619999999989388
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjQ"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.334999999999868
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.714999999999867
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683296"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDIy",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d22"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0.07619999999989388
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjO"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.334999999999868
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.714999999999867
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683298"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDI0",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d24"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0.07619999999989388
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjU"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.334999999999868
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.714999999999867
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683300"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDI2",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d26"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0.07619999999989388
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjS"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.334999999999868
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.714999999999867
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683302"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDI4",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d28"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0.07619999999989388
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjI"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.334999999999892
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.7149999999998915
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683304"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmNzZj",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "f91478b8-6352-4c8c-b922-df750a8f322d-000bf76c"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3v57YuOr9CZBaYttKAXCL1"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "784236"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmNzc3",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "f91478b8-6352-4c8c-b922-df750a8f322d-000bf777"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3v57YuOr9CZBaYttKAXCLQ"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "784247"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmODEy",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "f91478b8-6352-4c8c-b922-df750a8f322d-000bf812"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3v57YuOr9CZBaYttKAXCe$"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "784402"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmODEz",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "f91478b8-6352-4c8c-b922-df750a8f322d-000bf813"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3v57YuOr9CZBaYttKAXCe_"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "784403"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmODdl",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "f91478b8-6352-4c8c-b922-df750a8f322d-000bf87e"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3v57YuOr9CZBaYttKAXCfJ"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "784510"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmODdm",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "f91478b8-6352-4c8c-b922-df750a8f322d-000bf87f"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3v57YuOr9CZBaYttKAXCfI"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "784511"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmODgw",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "f91478b8-6352-4c8c-b922-df750a8f322d-000bf880"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3v57YuOr9CZBaYttKAXCgj"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "784512"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmOWVk",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "f91478b8-6352-4c8c-b922-df750a8f322d-000bf9ed"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3v57YuOr9CZBaYttKAXCl0"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "784877"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmYWI4",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e0ca0049-da9c-4b7d-acb9-c4ffd7416a1c-000bfab8"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3WoW19sfnBVQovnF$NIf2a"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "785080"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmYWI5",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e0ca0049-da9c-4b7d-acb9-c4ffd7416a1c-000bfab9"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3WoW19sfnBVQovnF$NIf2b"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "785081"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmYWJh",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e0ca0049-da9c-4b7d-acb9-c4ffd7416a1c-000bfaba"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3WoW19sfnBVQovnF$NIf2c"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "785082"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmYzI1",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e0ca0049-da9c-4b7d-acb9-c4ffd7416a1c-000bfc25"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3WoW19sfnBVQovnF$NIfOv"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "785445"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmYzI2",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e0ca0049-da9c-4b7d-acb9-c4ffd7416a1c-000bfc26"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3WoW19sfnBVQovnF$NIfOw"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "785446"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmYzRm",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e0ca0049-da9c-4b7d-acb9-c4ffd7416a1c-000bfc4f"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3WoW19sfnBVQovnF$NIfPJ"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "785487"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmYzUw",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e0ca0049-da9c-4b7d-acb9-c4ffd7416a1c-000bfc50"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3WoW19sfnBVQovnF$NIfPC"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "785488"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2JmZTJi",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e0ca0049-da9c-4b7d-acb9-c4ffd7416a1c-000bfe2b"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3WoW19sfnBVQovnF$NIfGt"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Top of Footing"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.411199999999889
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.791199999999889
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "785963"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2MzM2Nl",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "cd5bcf49-3342-49ff-b18f-a0db3b53a86a-000c33ce"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0.07619999999989388
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3DMyz9Cq99$x6FeDixNvka"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.334999999999892
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.7149999999998915
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "799694"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2MzM2Qw",
> > "name": "24x24x25'",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "cd5bcf49-3342-49ff-b18f-a0db3b53a86a-000c33d0"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": 0.07619999999989388
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3DMyz9Cq99$x6FeDixNvkw"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Round"
> > },
> > {
> > "name": "Element Name",
> > "value": "24x24x25'"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -13.334999999999892
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.7149999999998915
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "799696"
> > }
> > ]
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2OThm",
> > "name": "36x36x24 Pile_24",
> > "referencedBy": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2Yjlh",
> > "name": "36x36x24 Pile_24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6b9a"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": -0.17779999999989463
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEtW"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Pile_Cap_Rectangle"
> > },
> > {
> > "name": "Element Name",
> > "value": "36x36x24 Pile_24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Estimated Reinforcement Volume",
> > "value": 0.0036053123875875353
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.943599999999895
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.334000000000001
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "682906"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2YzUz",
> > "name": "36x36x24 Pile_24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6c53"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": -0.17779999999989463
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEef"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Pile_Cap_Rectangle"
> > },
> > {
> > "name": "Element Name",
> > "value": "36x36x24 Pile_24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.943599999999895
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.334000000000001
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683091"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDE5",
> > "name": "36x36x24 Pile_24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d19"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": -0.17779999999989463
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjZ"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Pile_Cap_Rectangle"
> > },
> > {
> > "name": "Element Name",
> > "value": "36x36x24 Pile_24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.943599999999895
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.334000000000001
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683289"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDFi",
> > "name": "36x36x24 Pile_24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d1b"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": -0.17779999999989463
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjX"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Pile_Cap_Rectangle"
> > },
> > {
> > "name": "Element Name",
> > "value": "36x36x24 Pile_24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.943599999999895
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.334000000000001
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683291"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDFk",
> > "name": "36x36x24 Pile_24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d1d"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": -0.1777999999998697
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjd"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Pile_Cap_Rectangle"
> > },
> > {
> > "name": "Element Name",
> > "value": "36x36x24 Pile_24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.94359999999987
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3339999999999765
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683293"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDFm",
> > "name": "36x36x24 Pile_24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d1f"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": -0.1777999999998697
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjb"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Pile_Cap_Rectangle"
> > },
> > {
> > "name": "Element Name",
> > "value": "36x36x24 Pile_24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.94359999999987
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3339999999999765
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683295"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDIx",
> > "name": "36x36x24 Pile_24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d21"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": -0.1777999999998697
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjR"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Pile_Cap_Rectangle"
> > },
> > {
> > "name": "Element Name",
> > "value": "36x36x24 Pile_24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.94359999999987
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3339999999999765
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683297"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDIz",
> > "name": "36x36x24 Pile_24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d23"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": -0.1777999999998697
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjP"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Pile_Cap_Rectangle"
> > },
> > {
> > "name": "Element Name",
> > "value": "36x36x24 Pile_24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.94359999999987
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3339999999999765
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683299"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDI1",
> > "name": "36x36x24 Pile_24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d25"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": -0.1777999999998697
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjV"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Pile_Cap_Rectangle"
> > },
> > {
> > "name": "Element Name",
> > "value": "36x36x24 Pile_24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.94359999999987
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.3339999999999765
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683301"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E2ZDI3",
> > "name": "36x36x24 Pile_24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "965746f8-0e0c-475e-9d21-93aadfae867a-000a6d27"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": -0.17779999999989463
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "2MLqRu3Wn7NfqXawhVfEjT"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Pile_Cap_Rectangle"
> > },
> > {
> > "name": "Element Name",
> > "value": "36x36x24 Pile_24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.943599999999895
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.334000000000001
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "683303"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2MzM2Nk",
> > "name": "36x36x24 Pile_24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "cd5bcf49-3342-49ff-b18f-a0db3b53a86a-000c33cd"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": -0.17779999999989463
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3DMyz9Cq99$x6FeDixNvkd"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Pile_Cap_Rectangle"
> > },
> > {
> > "name": "Element Name",
> > "value": "36x36x24 Pile_24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.943599999999895
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.334000000000001
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "799693"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2MzM2Nm",
> > "name": "36x36x24 Pile_24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "cd5bcf49-3342-49ff-b18f-a0db3b53a86a-000c33cf"
> > },
> > {
> > "name": "Height Offset From Level",
> > "value": -0.17779999999989463
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3DMyz9Cq99$x6FeDixNvkb"
> > },
> > {
> > "name": "Host",
> > "value": "Level : Parking"
> > },
> > {
> > "name": "Moves With Grids",
> > "value": true
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "SFD_Pile_Cap_Rectangle"
> > },
> > {
> > "name": "Element Name",
> > "value": "36x36x24 Pile_24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -5.943599999999895
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -5.334000000000001
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "799695"
> > }
> > ]
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3X2E4M2I2",
> > "name": "CB18x24",
> > "referencedBy": {
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3Xzk0MmIw",
> > "name": "CB18x24",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Has Association",
> > "value": false
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "e37453ab-55ac-464e-96ef-b2d748a679fc-000942b0"
> > },
> > {
> > "name": "Volume",
> > "value": 1.0179316415519988
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type"
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "IfcGUID",
> > "value": "3ZT5EhLQn6JfRlijT8hpjC"
> > },
> > {
> > "name": "Length",
> > "value": 6.718299999999995
> > },
> > {
> > "name": "Structural Usage",
> > "value": 3
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Concrete-Rectangular Beam"
> > },
> > {
> > "name": "Element Name",
> > "value": "CB18x24"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance"
> > },
> > {
> > "name": "Work Plane",
> > "value": "Level : L1_35_Low"
> > },
> > {
> > "name": "Start Level Offset",
> > "value": 0
> > },
> > {
> > "name": "End Level Offset",
> > "value": 0
> > },
> > {
> > "name": "Orientation",
> > "value": "Normal"
> > },
> > {
> > "name": "Start Attachment Type",
> > "value": "End Elevation"
> > },
> > {
> > "name": "Cross-Section Rotation",
> > "value": 0
> > },
> > {
> > "name": "Elevation at Bottom",
> > "value": -2.413000000000239
> > },
> > {
> > "name": "Elevation at Top",
> > "value": -1.8034000000002393
> > },
> > {
> > "name": "Cut Length",
> > "value": 6.261100000000018
> > },
> > {
> > "name": "y Justification",
> > "value": "Origin"
> > },
> > {
> > "name": "y Offset Value",
> > "value": 0
> > },
> > {
> > "name": "yz Justification",
> > "value": "Uniform"
> > },
> > {
> > "name": "z Justification",
> > "value": "Top"
> > },
> > {
> > "name": "z Offset Value",
> > "value": 0
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "606896"
> > }
> > ]
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

After working through the steps mentioned above, you should see a screen similar to the following image:
> 
