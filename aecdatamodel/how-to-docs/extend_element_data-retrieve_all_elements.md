# Task 4: Retrieve All Elements which are Doors, Based on the Custom Cost Property on Their Extensions.

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/extend_element_data/retrieve_all_elements/

---

# Task 4: Retrieve All Elements which are Doors, Based on the Custom Cost Property on Their Extensions.

In this tutorial you learn how to filter model elements in an ElementGroup using the properties present on them and the properties present on their associated extension elements together.

In the previous task you updated an existing property on an extension element. Now you will learn to use the compound filter to filter elements based on properties present on them and their associated extension elements. The purpose of this is to more accurately show the filtering using properties across model and extension elements, by having different values of the cost property on the extension elements.

## [Step 1: Retrieve All elements which are Doors, which have the Custom Cost Property Above 10000.0 on Their Extensions](#step-1-retrieve-all-elements-which-are-doors-which-have-the-custom-cost-property-above-10000-0-on-their-extensions)

The following steps demonstrate how you can filter elements based on properties on them and their associated extension elements. For this case, we want to filter all elements in a model elementGroup which are doors, and have a cost property on their associated extensions with a value greater than 10000.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> ```
> query elementsByExtensibility($elementGroupId: ID!, $filter: ElementFilterInput) {
> elementsByElementGroup(elementGroupId: $elementGroupId, filter: $filter) {
> results {
> id
> name
> }
> }
> }
>
> ```
> Show More

2. In the query variable pane enter the following values:

> **Query Variables**
>
>
>
>
> ```
> {
> "elementGroupId": "{{YOUR_ELEMENT_GROUP_ID}}",
> "filter": {
> "query": "property.name.category==Doors",
> "extensibilityFilter": {
> "extensionElementGroups": ["{{YOUR_EXTENSION_ELEMENT_GROUP_ID}}"],
> "query": "'property.name.Cost' > 10000.0"
> }
> }
> }
>
> ```
> Show More

The ElementGroupId is the model ElementGroup ID you have been using for all the tasks. The Extension ElementGroup ID is the ID of the ExtensionGroup created in Task 2 Step 2.

3. Click **Play**. The response should be similar to the following code-block:

> **Response**
>
>
>
>
> ```
> {
> "data": {
> "elementsByElementGroup": {
> "results": [
> {
> "id": "YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ352ZUZGYzFyWFQ0cUhESmJSMkUwMnpnXzEwMWQ3Mw",
> "name": "36\" x 84\""
> }
> ]
> }
> }
> }
>
> ```
> Show More

You should get back one element, which should be the model element whose ID we used to update the cost property on its extension in the previous task.
