# Get Distinct Values of Properties

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/tutorial02/distinctvaluesquery/

---

# Get Distinct Values of Properties

This page describes how to use the following queries to retrieve distinct values of properties in the AEC Data Model API. These queries enable you to find and retrieve all distinct values of a given property within an element group, either by property definition ID or property name.
> - **distinctPropertyValuesInElementGroupById**
> - **distinctPropertyValuesInElementGroupByName**

Both queries accept an element filter for more advanced queries.

## [Step 1: Retrieve distinct values by ID](#step-1-retrieve-distinct-values-by-id)

The following example returns the distinct values of a given property filtered by IDs.

**Query**
> ```
> query ($elementGroupId: ID!, $propertyDefinitionId: ID!, $filter: ElementFilterInput) {
> distinctPropertyValuesInElementGroupById(elementGroupId: $elementGroupId, propertyDefinitionId: $propertyDefinitionId, filter: $filter) {
> values(limit: 200) {
> value,
> count
> }
> }
> }
>
> ```
>
>
> Show More

**Variables**
> **Get all categories in an element group (by ID)**
>
>
>
>
> > ```
> > {
> > "elementGroupId": "YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35GZGhKOWZxZFJSR2QxTXAwNU1RWkVR",
> > "propertyDefinitionId": "autodesk.revit.parameter:parameter.category-2.0.0"
> > }
> >
> > ```

**Response**
> ```
> "values": [
> {
> "value": "Curtain Wall Mullions",
> "count": 2372
> },
> {
> "value": "Analytical Nodes",
> "count": 1410
> }
> ]
>
> ```
>
>
> Show More

**IMPORTANT:** The count represents the number of unique assets that have this specific property value. For example, if a property value is only found once on a certain type asset, but that type asset is referenced by multiple instance assets, the count returned will be 1.

(OR)

## [Retrieve distinct values by Name](#retrieve-distinct-values-by-name)

The following example returns the distinct values of a given property filtered by name.

When querying for distinct values **by Name**. multiple properties can have the same name so the response contains the distinct values of all properties matching that name:

**Query**
> ```
> query ($elementGroupId: ID!, $name: String!, $filter: ElementFilterInput, $pagination: PaginationInput) {
> distinctPropertyValuesInElementGroupByName(elementGroupId: $elementGroupId, name: $name, filter: $filter, pagination: $pagination) {
> pagination {
> cursor
> }
> results {
> definition {
> id
> }
> values(limit: 200) {
> value
> count
> }
> }
> }
> }
>
> ```
>
>
> Show More

**Variables**

**Get all categories in an element group (by name)**
> ```
> {
> "elementGroupId": "YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35GZGhKOWZxZFJSR2QxTXAwNU1RWkVR",
> "name": "Length"
> }
>
> ```

**Response**
> ```
> "results": [
> {
> "definition": {
> "id": "autodesk.revit.parameter:structuralFoundationLength-2.0.0",
> },
> "values": [
> {
> "value": "1.93546015625",
> "count": 5
> },
> {
> "value": "1.0947796875000002",
> "count": 1
> }
> ]
> },
> {
> "definition": {
> "id": "autodesk.revit.parameter:continuousrailEndExtensionLengthParam-2.0.0",
> },
> "values": [
> {
> "value": "3.0463569792873577",
> "count": 1
> }
> ]
> }
> }
>
> ```
>
>
> Show More

If too many properties match the specified name, the result will be paginated.

**IMPORTANT:** The count represents the number of unique assets that have this specific property value. For example, if a property value is only found once on a certain type asset, but that type asset is referenced by multiple instance assets, the count returned will be 1.

### Vairable examples: Filtering by Categories and Materials

Besides retrieving distinct values of properties by IDs and names, you can also retrieve by specific categories, families, structural materials used in categories, etc. Refer to the following variable examples to see how to provide the filter values for each of those options.

**A few more variable examples:**

- **Get all family names in an element group for a given category (Doors, in this example)**

> ```
> {
> "elementGroupId": "YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35GZGhKOWZxZFJSR2QxTXAwNU1RWkVR",
> "name": "Family Name",
> "filter": {
> "query": "property.name.category==Doors"
> }
> }
>
> ```

- **Get all types for a given family (Single, in this example)**

> ```
> {
> "elementGroupId": "YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35GZGhKOWZxZFJSR2QxTXAwNU1RWkVR",
> "name": "Type",
> "filter": {
> "query": "'property.name.Family Name'=='Single'"
> }
> }
>
> ```

- **Get all distinct structural materials used in walls**

> ```
> {
> "elementGroupId": "YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35GZGhKOWZxZFJSR2QxTXAwNU1RWkVR",
> "name": "Structural Material",
> "filter": {
> "query": "property.name.category==Walls"
> }
> }
>
> ```

- **Get all the door widths that are less than 0.9 meters**

> ```
> {
> "elementGroupId": "YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35GZGhKOWZxZFJSR2QxTXAwNU1RWkVR",
> "name": "Width",
> "filter": {
> "query" : "property.name.category==Doors",
> "properties" {
> "name": "Width",
> "valueWithComparator": {
> "value": "0.9",
> "comparator": "LESS_THAN"
> }
> }
> }
> }
>
> ```
> Show More
