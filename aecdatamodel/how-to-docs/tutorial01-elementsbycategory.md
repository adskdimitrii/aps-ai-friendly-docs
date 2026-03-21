# Get Elements from a Category

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/tutorial01/elementsbycategory/

---

# Get Elements from a Category

In this guide, you will learn how to retrieve elements from a specific category within an ElementGroup. This is useful for filtering elements based on their classification, such as walls, doors, or windows.

By the end of this guide, you will be able to:

- Fetch elements and information like id and properties.
- Understand the options and fields in the documentation on the elements query, elements, object, and properties object.

You will use the following query in this guide:

| Type | Operation | Description |
| --- | --- | --- |
| Query | [elementsByElementGroup](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elementsbyelementgroup/) | Retrieves element in the given ElementGroup, using additional RSQL filters if provided. |

## [Step 1: Request Elements matching the specified classification filter](#step-1-request-elements-matching-the-specified-classification-filter)

The [Elements](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elements/) query returns an [Elements](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/elements/) object, which contains an array of Element objects.

For this exercise, we request all elements instances with
- Elements id, name field, and properties.
- Name and value fields in the properties object.
> 1. In [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/), the query is populated by default in the **Query Pane**. You can also edit or update the query as per your requirement and run it.
>
>
>
> > **Query**
> >
> >
> >
> >
> > ```
> > query GetElementsFromCategory($elementGroupId: ID!, $propertyFilter: String!) {
> > elementsByElementGroup(elementGroupId: $elementGroupId, filter: {query:$propertyFilter}) {
> > pagination {
> > cursor
> > }
> > results {
> > id
> > name
> > properties {
> > results {
> > name
> > value
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
>
> 2. In the Query Variables Pane, replace the value of the `elementGroupId` obtained in [Navigate to Elementgroups within projects](https://aps.autodesk.com/en/docs/aecdatamodel/v1/tutorials/tutorial-01/nav-elements/) and property filter with the ID of your choice. For ease of understanding, we have used *“property.name.category==Walls”*.
>
>
>
> > **Note**: Refer to the [Advanced Filtering Capabilities](https://aps.autodesk.com/en/docs/aecdatamodel/v1/developers_guide/filtering/advanced-filtering/) page to see the list of supported metadata filtering options.
> >
> > **Query Variables**
> >
> >
> >
> >
> > ```
> > {
> > "elementGroupId":"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVB",
> > "propertyFilter":"property.name.category==Walls"
> > }
> >
> > ```
>
> 3. Click **Play**. The list of elements available within that elementGroup of property with name category and value as “Walls” is displayed in the response.
>
>
>
> > The response should be similar to the following code-block:
> >
> > **Response**
> >
> >
> >
> >
> > ```
> > {
> > "data": {
> > "elementsByElementGroup": {
> > "pagination": {
> > "cursor": "Y3Vyc341MH41MA"
> > },
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMGMzNw",
> > "name": "Generic - 21\"",
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Manufacturer",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Model",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Type Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "URL",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Absorptance",
> > "value": 0.7,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Heat Transfer Coefficient (U)",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Roughness",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Thermal Mass",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Thermal Resistance (R)",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Coarse Scale Fill Color",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cost",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00100c37",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Fire Rating",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Function",
> > "value": "Exterior",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nphr",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Keynote",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Generic - 21\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Generic - 21\"",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Assembly Code",
> > "value": "B2010",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Exterior Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Width",
> > "value": 0.5334000000000001,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Type Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Wrapping at Ends",
> > "value": "None",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Wrapping at Inserts",
> > "value": "Do not wrap",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1051703",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTc5NQ",
> > "name": "_Not Defined",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.0668000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101795",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 2.4928982400006445,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$no5N",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Curtain Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "_Not Defined",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 4,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0.8128000000000001,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": -2.3368,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 2.3368000000006037,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054613",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTdhNQ",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.4383160862420683,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001017a5",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 3.2317665212142757,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 0.9860739215865809,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$no5d",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.546600000000602,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054629",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTdhNg",
> > "name": "Solar Wall (Parapet)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.6460776368749865,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001017a6",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 1.376465981556736,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 0.687905392562603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$no5a",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Parapet)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6387870964698155,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.47307500000000025,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 0.9397999999999986,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054630",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTdhNw",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.0626540981910537,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001017a7",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 3.768650122285474,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 1.1019842226549768,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$no5b",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.546600000000602,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054631",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTdhOA",
> > "name": "Solar Wall (Parapet)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.2009675475581287,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001017a8",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 0.901755704546776,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 0.43464459760001195,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$no5g",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Parapet)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6387870964698155,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.47307500000000025,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 0.9397999999999986,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054632",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTdhYg",
> > "name": "Solar Wall (Multi-Level)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 4.792662500000017,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001017ab",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 23.709836410796086,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 25.039749093710018,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$no5f",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Multi-Level)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 1.5889109726195683,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.6215106256605418,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054635",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTdiNA",
> > "name": "_Not Defined",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.0413999999999752,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001017b4",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 11.109655199999741,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$no5s",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Curtain Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "_Not Defined",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 8,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 1,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0.6096,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.9144000000000001,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 10.668000000000003,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054644",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTdkMw",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 3.0539553128302654,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001017d3",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 15.050292480001643,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 4.814710783207467,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$no4H",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054675",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTdkNA",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.201737499999955,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001017d4",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 8.2226448450007,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 2.497916847167566,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$no4M",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -1.5240000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 14.198600000000607,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054676",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTdlYQ",
> > "name": "Solar Wall (Multi-Level)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 4.792662500000017,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001017ea",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 23.709836410796086,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 24.574663482831845,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$no4e",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Multi-Level)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 1.5889109726195683,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.6215106256605418,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054698",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTdlYg",
> > "name": "_Not Defined",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.0413999999999752,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001017eb",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 11.109655199999716,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$no4f",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Curtain Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "_Not Defined",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 8,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 1,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0.6096,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.9144000000000001,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 10.668000000000003,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054699",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTgwYQ",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 3.0539553128302654,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-0010180a",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 15.050292480001643,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 4.8147098193551665,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nox8",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054730",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTgyNA",
> > "name": "Solar Wall (Multi-Level)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 4.792662500000017,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101824",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 23.70983641079611,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 25.04026236877448,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noxc",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Multi-Level)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 1.5889109726195683,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.6215106256605418,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054756",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTgyNQ",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 3.0539553128302654,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101825",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 15.05029248000164,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 4.81471050400158,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noxd",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054757",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTgyNw",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.201737499999955,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101827",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 8.222644845000717,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 2.4873596547576757,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noxb",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -1.5240000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 14.198600000000607,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054759",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTgyOA",
> > "name": "Solar Wall (Parapet)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.201737499999995,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101828",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 0.9938058641460061,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 0.5440940086951872,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noxg",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Parapet)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6387870964698149,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.4730749999999999,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 0.9397999999999986,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054760",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTgyOQ",
> > "name": "Solar Wall (Parapet)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.201737499999995,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101829",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 0.9938058641460084,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 0.5440940086951884,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noxh",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Parapet)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6387870964698149,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.4730749999999999,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 0.9397999999999986,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054761",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTgyYQ",
> > "name": "Solar Wall (Parapet)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.201737499999995,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-0010182a",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 0.9938058641460122,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 0.4253410526529743,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noxe",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Parapet)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6387870964698149,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.4730749999999999,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 0.9397999999999986,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054762",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTgyYg",
> > "name": "Solar Wall (L5)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 4.792662500000015,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-0010182b",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 23.460893610284835,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 22.830919776663414,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noxf",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (L5)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 1.514294096959028,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.5468937500000003,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054763",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTgzMA",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.5352203527555242,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101830",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 8.290165595627899,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 2.5193765509461903,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noxo",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054768",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTgzMQ",
> > "name": "Solar Panels",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0.7112000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 4.9784000000000015,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101831",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 76.52763732767735,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noxp",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Curtain Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Panels",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 8,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 5,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -1.5240000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Slanted",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle From Vertical",
> > "value": -0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 15.138400000000605,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054769",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMThmNw",
> > "name": "Solar Panels",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0.7112000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 4.9784000000000015,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001018f7",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 76.52763732767735,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nour",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Curtain Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Panels",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 8,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 5,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -1.5240000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Slanted",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle From Vertical",
> > "value": -0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 15.138400000000605,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054967",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTliZA",
> > "name": "Solar Panels",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0.7112000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 4.9784000000000015,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001019bd",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 76.52763732767727,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noz$",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Curtain Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Panels",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 8,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 5,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -1.5240000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Slanted",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle From Vertical",
> > "value": -0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 15.138400000000605,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055165",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWE4Mw",
> > "name": "Solar Panels",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0.4318000000000001,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 4.978399999999997,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101a83",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 26.32242559089769,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$non1",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Curtain Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Panels",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 5,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0.27940000000000004,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Slanted",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle From Vertical",
> > "value": -0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.207000000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055363",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWFkYQ",
> > "name": "Solar Wall (L5)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 3.7766625000000156,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101ada",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 19.88397863451805,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 19.656287535319187,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nomO",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (L5)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 1.5142940969590277,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.5468937500000001,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055450",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWFkYg",
> > "name": "Exterior - 14 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.3324161999416064,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101adb",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 6.689604964360378,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 2.4792586980929507,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nomP",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 14 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055451",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWFkYw",
> > "name": "Solar Panels",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0.40640000000000004,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 3.987799999999999,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101adc",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 20.981947407298946,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nomU",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Curtain Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Panels",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 4,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0.3048,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Slanted",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle From Vertical",
> > "value": -0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.181600000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055452",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWIxYw",
> > "name": "Solar Wall (L5)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 3.8101315193233423,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101b1c",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 18.39138208672618,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 18.275082331560544,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$notU",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (L5)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 1.5142940969590282,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.5468937500000011,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055516",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWIyMQ",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 0.8533228176263074,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101b21",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 10.662678441052247,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 3.286284587451731,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$notZ",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055521",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWIyMg",
> > "name": "Solar Panels",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0.40640000000000004,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 3.9877999999999996,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101b22",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 20.981947407298954,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$notW",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Curtain Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Panels",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 4,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0.3048,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Slanted",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle From Vertical",
> > "value": -0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.181600000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055522",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWI1Yw",
> > "name": "_Not Defined",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 0.9683749999999998,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101b5c",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 2.508382080000551,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nosU",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Curtain Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "_Not Defined",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 4,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0.40640000000000004,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": -2.3368,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 2.7432000000006025,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055580",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWI2Yw",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.2444684806766668,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101b6c",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 2.3052441967445993,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 0.7392341827910742,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nosk",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.546600000000602,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055596",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWI2ZA",
> > "name": "Solar Wall (Parapet)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.244468480676672,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101b6d",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 1.0103447831280445,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 0.5531488221683959,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nosl",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Parapet)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6387870964698156,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.47307499999999997,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 0.9397999999999986,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055597",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWI2ZQ",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.7216829493046037,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101b6e",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 9.074522364724338,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 2.8960993623415128,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nosi",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055598",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWI5NA",
> > "name": "_Not Defined",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 0.9398,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101b94",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 2.196124640000567,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$norM",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Curtain Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "_Not Defined",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 4,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0.8128000000000001,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": -2.3368,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 2.3368000000006037,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055636",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWJhNQ",
> > "name": "Solar Wall (Parapet)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.2191999999995216,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101ba5",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 1.145804159999551,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 0.5420513029917878,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nord",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Parapet)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 0.9397999999999986,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055653",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWJhNg",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 0.4174718075886615,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101ba6",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 1.429162065489934,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 0.35176889004206735,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nora",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.546600000000602,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055654",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWJhNw",
> > "name": "Solar Wall (Parapet)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 0.3156708582215581,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101ba7",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 0.2719908748655249,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 0.08322161076578016,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$norb",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Parapet)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6387870964698156,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.4730750000000001,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 0.9397999999999986,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055655",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWJhOA",
> > "name": "Party - 6 1/8\" (2-hr)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 2.3876,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101ba8",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 6.623422240325789,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 1.647263399665575,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$norg",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Party - 6 1/8\" (2-hr)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.064000000000001,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055656",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWJhYQ",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.4848504443479604,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101baa",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 17.155713741494722,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 5.2254763496888765,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nore",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -1.5240000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 14.198600000000607,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055658",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWJkZQ",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.2874624999999873,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101bde",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 3.034832640000137,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 0.9731949568320408,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noqS",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.546600000000602,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055710",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWJkZg",
> > "name": "Solar Wall (L5)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 3.802062500000016,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101bdf",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 19.88397863451806,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 19.549206767408798,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noqT",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (L5)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 1.514294096959027,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.5468937499999988,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055711",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWJlNA",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.3937636696451252,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101be4",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 5.635357385430516,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 1.4346190142295514,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noqc",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.486400000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055716",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWJlNQ",
> > "name": "Solar Panels",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0.40640000000000004,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 3.987800000000015,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101be5",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 20.981947407299025,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noqd",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Curtain Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Panels",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Number",
> > "value": 4,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0.3048,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Slanted",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Angle From Vertical",
> > "value": -0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.181600000000603,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055717",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWMzZA",
> > "name": "Solar Wall (Parapet)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.3817150783837686,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101c3d",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 1.1655580946171125,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 0.5714564175710436,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$noh$",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Parapet)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -0.9398000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6387870964698155,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.4730750000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 0.9397999999999986,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055805",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWMzZQ",
> > "name": "Solar Wall (Multi-Level)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 4.792662500000022,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101c3e",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 24.22082426447388,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 27.086071162364657,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nohy",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Multi-Level)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -1.5240000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 1.606825793859443,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.6215106256605413,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.588000000000001,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055806",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWM0Nw",
> > "name": "Solar Wall (Multi-Level)",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 4.792662500000017,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101c47",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 16.556006459260587,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 15.534317429211052,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nog5",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Multi-Level)",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Bottom Width",
> > "value": 1.338103475259741,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Width",
> > "value": 0.6215106256605418,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.064000000000001,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055815",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWM1MA",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.8916131434242718,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101c50",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 9.407036751107253,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 3.0087134463831715,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nogI",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": -1.5240000000000002,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 5.588000000000001,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055824",
> > "definition": {
> > "units": null
> > }
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMWM1MQ",
> > "name": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Length",
> > "value": 1.1750202938250813,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101c51",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Area",
> > "value": 3.9290956600414,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Volume",
> > "value": 1.2576606779356483,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC",
> > "value": "By Type",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Export to IFC As",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IFC Predefined Type",
> > "value": null,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "IfcGUID",
> > "value": "04b3cqL6T7nASkHPv$nogJ",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.064000000000001,
> > "definition": {
> > "units": null
> > }
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1055825",
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

After working through the steps mentioned above, you should see a screen similar to the following image:
> 
