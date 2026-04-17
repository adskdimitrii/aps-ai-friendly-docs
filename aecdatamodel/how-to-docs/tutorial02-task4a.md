# Get Element Instances in a Category by Version

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/tutorial02/task4a/

---

# Get Element Instances in a Category by Version

In this guide, you will learn how to retrieve all instances of a particular category from an elementGroup at a specific version. Also, you can request only those instances that match your filter criteria.

Let’s try to retrieve all instances of the category `Walls` from the second version of the model **Snowdon Towers Sample Architecture.rvt**.

By the end of this guide, you will be able to:

- Fetch Instance Elements of a category `Walls` from a specific version of the elementGroup and define the property filter with `versionNumber`.
- Use advanced operators like `greater than`, `less than`, `and`, and `or`.

You will use the following queries in this guide:

| Type | Operation | Description |
| --- | --- | --- |
| Query | [ElementsByElementGroup](../reference-docs/queries-elementsbyelementgroup.md) | Retrieves elementGroups in the given project, using additional RSQL filters if provided. |

## [Step 1: Request elements matching the specified classification filter](#step-1-request-elements-matching-the-specified-classification-filter)

The [ElementsByElementGroup](../reference-docs/queries-elementsbyelementgroup.md) query returns [Elements](../reference-docs/objects-elements.md) object, which contains an array of Elements objects.

For this exercise, we request all elements instances that contain:
:   - Elements id, name field, and properties.
    - Name and value fields in the properties object.

1. In [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/), the query is populated by default in the **Query Pane**. You can also edit or update the query as per your requirement and run it.

> **Query**
>
>
>
>
> > ```
> > query GetWallsElementsByElementGroupIdAtVersion($elementGroupId: ID!, $versionNumber: Int!, $propertyFilter: String!) {
> > elementsByElementGroupAtVersion(elementGroupId: $elementGroupId, versionNumber: $versionNumber, filter: { query: $propertyFilter}, pagination : { limit : 5 }) {
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
> > displayValue
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
> > - In the Query Variables Pane, replace the value of the `elementGroupId` variable with the elementGroup ID that you used in [Navigate to Elementgroups](https://aps.autodesk.com/en/docs/aecdatamodel/v1/tutorials/tutorial-01/nav-elements/).
> >
> > - In the Query Variables Pane, replace the value of the `property filter` with the property filter of your choice. For ease of understanding, here we have added the filter based on property name and category as `Walls`.
> > **Note**: To know the list of supported metadata filtering options, refer [Advanced Filtering Capabilities](https://aps.autodesk.com/en/docs/aecdatamodel/v1/developers_guide/filtering/advanced-filtering/) page.
> >
> >
> >
> >
> > ```
> > {
> > "elementGroupId" : "YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVB",
> > "versionNumber": 1,
> > "propertyFilter": "property.name.category==Walls and 'property.name.Element Context'==Instance"
> > }
> >
> > ```

2. Click **Play**. The list of elements available within that elementGroup of property ‘family’ and category ‘“Walls” is displayed in the response. The response should be similar to the following code-block:

> **Response**
>
>
>
>
> > ```
> > {
> > "data": {
> > "elementsByElementGroupAtVersion": {
> > "pagination": {
> > "cursor": "Y3Vyc341fjU"
> > },
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTc5NQ",
> > "name": "_Not Defined",
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Angle",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Offset",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Length",
> > "value": 1.0668000000000002,
> > "displayValue": "1.0668000000000002"
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "displayValue": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-00101795",
> > "displayValue": "049439b4-5467-47c4-a72e-459e7fd736c2-00101795"
> > },
> > {
> > "name": "Area",
> > "value": 2.4928982400006445,
> > "displayValue": "2.4928982400006445"
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
> > "value": "04b3cqL6T7nASkHPv$no5N",
> > "displayValue": "04b3cqL6T7nASkHPv$no5N"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "displayValue": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Curtain Wall",
> > "displayValue": "Curtain Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "_Not Defined",
> > "displayValue": "_Not Defined"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "displayValue": "Beginning"
> > },
> > {
> > "name": "Justification",
> > "value": "Beginning",
> > "displayValue": "Beginning"
> > },
> > {
> > "name": "Number",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Number",
> > "value": 4,
> > "displayValue": "4"
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0.8128000000000001,
> > "displayValue": "0.8128000000000001"
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "displayValue": "Vertical"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Top Offset",
> > "value": -2.3368,
> > "displayValue": "-2.3368"
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 2.3368000000006037,
> > "displayValue": "2.3368000000006037"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054613",
> > "displayValue": "1054613"
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
> > "displayValue": null
> > },
> > {
> > "name": "Length",
> > "value": 1.4383160862420683,
> > "displayValue": "1.4383160862420683"
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "displayValue": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001017a5",
> > "displayValue": "049439b4-5467-47c4-a72e-459e7fd736c2-001017a5"
> > },
> > {
> > "name": "Area",
> > "value": 3.2317665212142757,
> > "displayValue": "3.2317665212142757"
> > },
> > {
> > "name": "Volume",
> > "value": 0.9860739215865809,
> > "displayValue": "0.9860739215865809"
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
> > "value": "04b3cqL6T7nASkHPv$no5d",
> > "displayValue": "04b3cqL6T7nASkHPv$no5d"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "displayValue": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "displayValue": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "displayValue": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.9398000000000002,
> > "displayValue": "-0.9398000000000002"
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.546600000000602,
> > "displayValue": "4.546600000000602"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054629",
> > "displayValue": "1054629"
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
> > "displayValue": null
> > },
> > {
> > "name": "Length",
> > "value": 1.6460776368749865,
> > "displayValue": "1.6460776368749865"
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "displayValue": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001017a6",
> > "displayValue": "049439b4-5467-47c4-a72e-459e7fd736c2-001017a6"
> > },
> > {
> > "name": "Area",
> > "value": 1.376465981556736,
> > "displayValue": "1.376465981556736"
> > },
> > {
> > "name": "Volume",
> > "value": 0.687905392562603,
> > "displayValue": "0.687905392562603"
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
> > "value": "04b3cqL6T7nASkHPv$no5a",
> > "displayValue": "04b3cqL6T7nASkHPv$no5a"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "displayValue": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Parapet)",
> > "displayValue": "Solar Wall (Parapet)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Base Offset",
> > "value": -0.9398000000000002,
> > "displayValue": "-0.9398000000000002"
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "displayValue": "Tapered"
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "displayValue": "3"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "displayValue": "0.17453292519943278"
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6387870964698155,
> > "displayValue": "0.6387870964698155"
> > },
> > {
> > "name": "Top Width",
> > "value": 0.47307500000000025,
> > "displayValue": "0.47307500000000025"
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 0.9397999999999986,
> > "displayValue": "0.9397999999999986"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054630",
> > "displayValue": "1054630"
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
> > "displayValue": null
> > },
> > {
> > "name": "Length",
> > "value": 1.0626540981910537,
> > "displayValue": "1.0626540981910537"
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "displayValue": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001017a7",
> > "displayValue": "049439b4-5467-47c4-a72e-459e7fd736c2-001017a7"
> > },
> > {
> > "name": "Area",
> > "value": 3.768650122285474,
> > "displayValue": "3.768650122285474"
> > },
> > {
> > "name": "Volume",
> > "value": 1.1019842226549768,
> > "displayValue": "1.1019842226549768"
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
> > "value": "04b3cqL6T7nASkHPv$no5b",
> > "displayValue": "04b3cqL6T7nASkHPv$no5b"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "displayValue": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud",
> > "displayValue": "Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Base Offset",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Vertical",
> > "displayValue": "Vertical"
> > },
> > {
> > "name": "Location Line",
> > "value": 2,
> > "displayValue": "2"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Top Offset",
> > "value": -0.9398000000000002,
> > "displayValue": "-0.9398000000000002"
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.546600000000602,
> > "displayValue": "4.546600000000602"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054631",
> > "displayValue": "1054631"
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
> > "displayValue": null
> > },
> > {
> > "name": "Length",
> > "value": 1.2009675475581287,
> > "displayValue": "1.2009675475581287"
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model",
> > "displayValue": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null,
> > "displayValue": null
> > },
> > {
> > "name": "External ID",
> > "value": "049439b4-5467-47c4-a72e-459e7fd736c2-001017a8",
> > "displayValue": "049439b4-5467-47c4-a72e-459e7fd736c2-001017a8"
> > },
> > {
> > "name": "Area",
> > "value": 0.901755704546776,
> > "displayValue": "0.901755704546776"
> > },
> > {
> > "name": "Volume",
> > "value": 0.43464459760001195,
> > "displayValue": "0.43464459760001195"
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
> > "value": "04b3cqL6T7nASkHPv$no5g",
> > "displayValue": "04b3cqL6T7nASkHPv$no5g"
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls",
> > "displayValue": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Basic Wall",
> > "displayValue": "Basic Wall"
> > },
> > {
> > "name": "Element Name",
> > "value": "Solar Wall (Parapet)",
> > "displayValue": "Solar Wall (Parapet)"
> > },
> > {
> > "name": "Element Context",
> > "value": "Instance",
> > "displayValue": "Instance"
> > },
> > {
> > "name": "Related to Mass",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Room Bounding",
> > "value": true,
> > "displayValue": "true"
> > },
> > {
> > "name": "Base Offset",
> > "value": -0.9398000000000002,
> > "displayValue": "-0.9398000000000002"
> > },
> > {
> > "name": "Base Extension Distance",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Base is Attached",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Cross-Section",
> > "value": "Tapered",
> > "displayValue": "Tapered"
> > },
> > {
> > "name": "Location Line",
> > "value": 3,
> > "displayValue": "3"
> > },
> > {
> > "name": "Structural",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Exterior Angle",
> > "value": 0.17453292519943278,
> > "displayValue": "0.17453292519943278"
> > },
> > {
> > "name": "Interior Angle",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Enable Angle Overrides",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Bottom Width",
> > "value": 0.6387870964698155,
> > "displayValue": "0.6387870964698155"
> > },
> > {
> > "name": "Top Width",
> > "value": 0.47307500000000025,
> > "displayValue": "0.47307500000000025"
> > },
> > {
> > "name": "Top Extension Distance",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Top is Attached",
> > "value": false,
> > "displayValue": "false"
> > },
> > {
> > "name": "Top Offset",
> > "value": 0,
> > "displayValue": "0"
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 0.9397999999999986,
> > "displayValue": "0.9397999999999986"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1054632",
> > "displayValue": "1054632"
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
