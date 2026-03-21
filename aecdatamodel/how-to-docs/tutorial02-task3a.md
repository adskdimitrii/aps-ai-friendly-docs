# Get Element Instances of a Particular Type

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/tutorial02/task3a/

---

# Get Element Instances of a Particular Type

In this guide, you will learn how to retrieve all instances of a particular type from a Design at Tip. Additionally, you can request select properties like Area, Volume, etc. of these instances and their type to be returned.
Let us try to retrieve all basic wall instances of the type `Foundation - 24\" Concrete` from the Snowdon Towers Sample Architecture.rvt.

By the end of this guide, you will be able to:

- Fetch Instance Elements of a Type using `referencedBy (name: "Type")` relationship and `propertyFilter` to define the Category `Walls` & Type `Foundation - 24\" Concrete`.
- Return only the properties that you need. For example: Area, Volume, Element Context, Element Name.
- Use advance operators like contains, and, etc.

You will use the following query in this guide:

| Type | Operation | Description |
| --- | --- | --- |
| Query | [elementsByElementGroup](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elementsByElementGroup/) | Retrieves element from given elementGroup, using additional RSQL filters. |

## [Step 1: Request for a list of elements in an ElementGroup](#step-1-request-for-a-list-of-elements-in-an-elementgroup)

The [elementsByElementGroup](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elementsByElementGroup/) query returns an [Elements](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/elements/) object.

1. In [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/), the query is populated by default in the **Query Pane**. You can also edit or update the query as per your requirement and run it.

> **Query**
>
>
>
>
> > ```
> > query ($elementGroupId: ID!, $propertyFilter: String!) {
> > elementsByElementGroup(
> > elementGroupId: $elementGroupId
> > filter: { query: $propertyFilter }
> > pagination: {limit: 5}
> > ) {
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
> > }
> > }
> > referencedBy(name: "Type") {
> > pagination {
> > cursor
> > }
> > results {
> > id
> > name
> > alternativeIdentifiers {
> > externalElementId
> > }
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
> 1. In the Query Variables Pane, replace the value of the `elementGroupId` variable with the elementGroup ID that you used in [Navigate to Elementgroups](https://aps.autodesk.com/en/docs/aecdatamodel/v1/tutorials/tutorial-01/nav-elements/) of previous tutorial.
> 2. In the Query Variables Pane, replace the value of the [``](#id2)propertyFilter [``](#id4)with the property filter of your choice.
> **Note**: To know about the list of supported metadata filtering options, refer [Advanced Filtering Capabilities](https://aps.autodesk.com/en/docs/aecdatamodel/v1/developers_guide/filtering/advanced-filtering/) page.
>
>
>
>
> > ```
> > {
> > "elementGroupId": "YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVB",
> > "propertyFilter": "'property.name.category'=contains=Walls and 'property.name.Element Context'==Type and 'property.name.Element Name'=contains='Foundation - 24'"
> > }
> >
> > ```

2. Click **Play**. The list of elements with its tip ID and name will appear in the response.

> The response should be similar to the following code-block:
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
> > "pagination": {
> > "cursor": null
> > },
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEyYTFiNQ",
> > "name": "Foundation - 24\" Concrete",
> > "properties": {
> > "results": [
> > {
> > "name": "Description",
> > "value": null
> > },
> > {
> > "name": "Manufacturer",
> > "value": null
> > },
> > {
> > "name": "Model",
> > "value": null
> > },
> > {
> > "name": "Type Comments",
> > "value": null
> > },
> > {
> > "name": "URL",
> > "value": null
> > },
> > {
> > "name": "Absorptance",
> > "value": 0.7
> > },
> > {
> > "name": "Heat Transfer Coefficient (U)",
> > "value": 0.30218381255198806
> > },
> > {
> > "name": "Roughness",
> > "value": 3
> > },
> > {
> > "name": "Thermal Mass",
> > "value": 921166.5599999999
> > },
> > {
> > "name": "Thermal Resistance (R)",
> > "value": 0.582791586998088
> > },
> > {
> > "name": "Coarse Scale Fill Color",
> > "value": 0
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Cost",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "9bd3aa6c-2785-4080-985d-83d6cac9401d-0012a1b5"
> > },
> > {
> > "name": "Fire Rating",
> > "value": "4 HR"
> > },
> > {
> > "name": "Function",
> > "value": "Foundation"
> > },
> > {
> > "name": "Export Type to IFC",
> > "value": "Default"
> > },
> > {
> > "name": "Export Type to IFC As",
> > "value": null
> > },
> > {
> > "name": "Type IFC Predefined Type",
> > "value": null
> > },
> > {
> > "name": "Type IfcGUID",
> > "value": "2Rqwfi9uL0W9XTWzRAs_6e"
> > },
> > {
> > "name": "Keynote",
> > "value": null
> > },
> > {
> > "name": "Revit Category Type Id",
> > "value": "Walls"
> > },
> > {
> > "name": "Family Name",
> > "value": "Foundation - 24\" Concrete"
> > },
> > {
> > "name": "Element Name",
> > "value": "Foundation - 24\" Concrete"
> > },
> > {
> > "name": "Element Context",
> > "value": "Type"
> > },
> > {
> > "name": "Assembly Code",
> > "value": "A1010200"
> > },
> > {
> > "name": "Assembly Description",
> > "value": "Foundation Walls"
> > },
> > {
> > "name": "Width",
> > "value": 0.6096
> > },
> > {
> > "name": "Type Mark",
> > "value": "C04"
> > },
> > {
> > "name": "Wrapping at Ends",
> > "value": "None"
> > },
> > {
> > "name": "Wrapping at Inserts",
> > "value": "Do not wrap"
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1221045"
> > }
> > ]
> > },
> > "referencedBy": {
> > "pagination": {
> > "cursor": null
> > },
> > "results": [
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzk3NDY1",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "50f92000-82f8-4258-b6a8-bb42c01b00a0-00097465"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 14.389100000000056
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "50f92000-82f8-4258-b6a8-bb42c01b00a0-00097465"
> > },
> > {
> > "name": "Area",
> > "value": 50.7037695600002
> > },
> > {
> > "name": "Volume",
> > "value": 30.909017923776116
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
> > "value": "1G_I00WlX2MBQekqB04dJ5"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": 3.5052000000000003
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "619621"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzk3NDY2",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "50f92000-82f8-4258-b6a8-bb42c01b00a0-00097466"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 3.162299999999996
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "50f92000-82f8-4258-b6a8-bb42c01b00a0-00097466"
> > },
> > {
> > "name": "Area",
> > "value": 10.550301479999995
> > },
> > {
> > "name": "Volume",
> > "value": 6.431463782207994
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
> > "value": "1G_I00WlX2MBQekqB04dJ6"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": 3.5052000000000003
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "619622"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzk3NDY3",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "50f92000-82f8-4258-b6a8-bb42c01b00a0-00097467"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 21.015009407150227
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "50f92000-82f8-4258-b6a8-bb42c01b00a0-00097467"
> > },
> > {
> > "name": "Area",
> > "value": 114.5973418770376
> > },
> > {
> > "name": "Volume",
> > "value": 68.69976110255986
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
> > "value": "1G_I00WlX2MBQekqB04dJ7"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": 5.3086
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "619623"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzk3NjBk",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "50f92000-82f8-4258-b6a8-bb42c01b00a0-0009760d"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 18.516599999999997
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "50f92000-82f8-4258-b6a8-bb42c01b00a0-0009760d"
> > },
> > {
> > "name": "Area",
> > "value": 42.779189806685366
> > },
> > {
> > "name": "Volume",
> > "value": 24.885678424383006
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
> > "value": "1G_I00WlX2MBQekqB04dQj"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": 3.5052000000000003
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "620045"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzk3NjBl",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "50f92000-82f8-4258-b6a8-bb42c01b00a0-0009760e"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 0.688334025144647
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "50f92000-82f8-4258-b6a8-bb42c01b00a0-0009760e"
> > },
> > {
> > "name": "Area",
> > "value": 5.522060309977901
> > },
> > {
> > "name": "Volume",
> > "value": 3.366247964962528
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
> > "value": "1G_I00WlX2MBQekqB04dQk"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": 4.2545
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "620046"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzk3NjBm",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "50f92000-82f8-4258-b6a8-bb42c01b00a0-0009760f"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 6.959599999999995
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "50f92000-82f8-4258-b6a8-bb42c01b00a0-0009760f"
> > },
> > {
> > "name": "Area",
> > "value": 28.312846599999972
> > },
> > {
> > "name": "Volume",
> > "value": 17.259511287359985
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
> > "value": "1G_I00WlX2MBQekqB04dQl"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": 4.2545
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "620047"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzk3NjEw",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "50f92000-82f8-4258-b6a8-bb42c01b00a0-00097610"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 9.110132736414313
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "50f92000-82f8-4258-b6a8-bb42c01b00a0-00097610"
> > },
> > {
> > "name": "Area",
> > "value": 42.54464127343791
> > },
> > {
> > "name": "Volume",
> > "value": 25.870041820730258
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
> > "value": "1G_I00WlX2MBQekqB04dQm"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": -0.508
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 4.8006
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "620048"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2E1ZGJj",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "717ca888-caa1-4d79-a802-1815f215117a-000a5dbc"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 24.744186068650656
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "717ca888-caa1-4d79-a802-1815f215117a-000a5dbc"
> > },
> > {
> > "name": "Area",
> > "value": 103.2902726290742
> > },
> > {
> > "name": "Volume",
> > "value": 62.45983083152432
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
> > "value": "1nVAY8og5DUQW261No7qp6"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": 4.2545
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "679356"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2E3ZDhk",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "ba8abc87-1993-4a27-9c7e-28f6d5ef2e36-000a7d8d"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 9.44880000000004
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "ba8abc87-1993-4a27-9c7e-28f6d5ef2e36-000a7d8d"
> > },
> > {
> > "name": "Area",
> > "value": 38.68756554362559
> > },
> > {
> > "name": "Volume",
> > "value": 23.385969951459128
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
> > "value": "2wYho76PDA9vn_AFRLvLEx"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": 4.2545
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "687501"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2E3ZTBh",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "ba8abc87-1993-4a27-9c7e-28f6d5ef2e36-000a7e0a"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 11.32652046598141
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "ba8abc87-1993-4a27-9c7e-28f6d5ef2e36-000a7e0a"
> > },
> > {
> > "name": "Area",
> > "value": 48.27367622366221
> > },
> > {
> > "name": "Volume",
> > "value": 29.375820134206812
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
> > "value": "2wYho76PDA9vn_AFRLvL0y"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": 4.2545
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "687626"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2FhNDY0",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "8b2fcbb6-3350-4536-a114-8d91a78c59b4-000aa464"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 7.25169999999995
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "8b2fcbb6-3350-4536-a114-8d91a78c59b4-000aa464"
> > },
> > {
> > "name": "Area",
> > "value": 25.685755079999822
> > },
> > {
> > "name": "Volume",
> > "value": 15.658036296767891
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
> > "value": "2BByksCr15Dg4KZP6dXltG"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": 3.5052000000000003
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "697444"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2FhNDhk",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "8b2fcbb6-3350-4536-a114-8d91a78c59b4-000aa48d"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 15.430499999999984
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "8b2fcbb6-3350-4536-a114-8d91a78c59b4-000aa48d"
> > },
> > {
> > "name": "Area",
> > "value": 52.27925027999992
> > },
> > {
> > "name": "Volume",
> > "value": 31.386274775711957
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
> > "value": "2BByksCr15Dg4KZP6dXlqv"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": 3.5052000000000003
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "697485"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2I4ZmNl",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "5ec49cf7-f328-41e6-8f02-263b961f3b28-000b8fce"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 9.07033402514468
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "5ec49cf7-f328-41e6-8f02-263b961f3b28-000b8fce"
> > },
> > {
> > "name": "Area",
> > "value": 25.3814803232309
> > },
> > {
> > "name": "Volume",
> > "value": 15.472550405041552
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
> > "value": "1Un9ptyoX1vey29ZkM5BJc"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": -0.6096
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 2.8956000000000004
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "757710"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2I5MDM0",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "5ec49cf7-f328-41e6-8f02-263b961f3b28-000b9034"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 9.070334025152942
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "5ec49cf7-f328-41e6-8f02-263b961f3b28-000b9034"
> > },
> > {
> > "name": "Area",
> > "value": 25.38148032323287
> > },
> > {
> > "name": "Volume",
> > "value": 15.472550405042778
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
> > "value": "1Un9ptyoX1vey29ZkM5AiS"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": -0.6096
> > },
> > {
> > "name": "Unconnected Height",
> > "value": 2.8956000000000004
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "757812"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2NmZDg1",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "487309ac-3af1-4fab-a7bb-9b30a3910b36-000cfd85"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 6.270019527898146
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "487309ac-3af1-4fab-a7bb-9b30a3910b36-000cfd85"
> > },
> > {
> > "name": "Area",
> > "value": 31.310036735424237
> > },
> > {
> > "name": "Volume",
> > "value": 19.019273381248762
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
> > "value": "18SmciEl5FgwUxcp2ZdVQp"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": 5.3086
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "851333"
> > }
> > ]
> > }
> > },
> > {
> > "id": "YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2ZmYzFi",
> > "name": "Foundation - 24\" Concrete",
> > "alternativeIdentifiers": {
> > "externalElementId": "c40d2a77-58c6-4479-8315-653c702baee6-000ffc1b"
> > },
> > "properties": {
> > "results": [
> > {
> > "name": "Comments",
> > "value": null
> > },
> > {
> > "name": "Length",
> > "value": 2.933699999999996
> > },
> > {
> > "name": "Design Option",
> > "value": "Main Model"
> > },
> > {
> > "name": "Mark",
> > "value": null
> > },
> > {
> > "name": "External ID",
> > "value": "c40d2a77-58c6-4479-8315-653c702baee6-000ffc1b"
> > },
> > {
> > "name": "Area",
> > "value": 10.86046214999999
> > },
> > {
> > "name": "Volume",
> > "value": 6.620537726639986
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
> > "value": "343IftMCP4UOCLPJnm95Bz"
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
> > "value": "Foundation - 24\" Concrete"
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
> > "value": -0.1524
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
> > "value": false
> > },
> > {
> > "name": "Structural Usage",
> > "value": 0
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
> > "value": 4.2545
> > },
> > {
> > "name": "Revit Element ID",
> > "value": "1047579"
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
> After working through the steps mentioned above, you should see a screen similar to the following image:
>
>
>
>
> > 
