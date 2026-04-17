# Task 2 - Add a Custom Cost Property to Door Instance Elements

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/extend_element_data/custom_property_elements/

---

# Task 2 - Add a Custom Cost Property to Door Instance Elements

In this tutorial, you will learn how to add a custom cost property to elements inside an elementGroup that are instances of a door.

The steps include:

1. Retrieving all door instances within an elementGroup.
2. Selecting specific elements to extend with the custom cost property.
3. Creating an ExtensionElementGroup to manage the extended elements.
4. Adding the custom property to the elements.
5. Updating and removing properties as needed.

## [Step 1: Get Door Instance Elements](#step-1-get-door-instance-elements)

The following steps demonstrate how you can get all instances of elements which are of type door.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> > ```
> > query elementsByElementGroup($elementGroupId: ID!, $filter: ElementFilterInput) {
> > elementsByElementGroup(elementGroupId: $elementGroupId, filter: $filter) {
> > pagination {
> > pageSize
> > cursor
> > }
> > results {
> > id
> > name
> > }
> > }
> > }
> >
> > ```
> > Show More
> >
> > 2. In the query variable pane enter the following values.
> **Query Variables**
>
>
>
>
> > ```
> > {
> > "elementGroupId": "{{YOUR_ELEMENT_GROUP_ID}}",
> > "filter": {
> > "query": "property.name.category==Doors"
> > }
> > }
> >
> > ```

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
> "pagination": {
> "pageSize": 50,
> "cursor": "Y3Vyc341MH41MA"
> },
> "results": [
> {
> "id": "YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ352ZUZGYzFyWFQ0cUhESmJSMkUwMnpnXzEwMWQ3Mw",
> "name": "36\" x 84\""
> },
> {
> "id": "YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ352ZUZGYzFyWFQ0cUhESmJSMkUwMnpnXzEwMzY4ZQ",
> "name": "Store Front Double Door"
> },
> {
> "id": "YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ352ZUZGYzFyWFQ0cUhESmJSMkUwMnpnXzEwMzcxMA",
> "name": "Store Front Double Door"
> },
> ...
> {
> "id": "YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ352ZUZGYzFyWFQ0cUhESmJSMkUwMnpnXzFmNjJlYw",
> "name": "Store Front Double Door"
> }
> ]
> }
> }
> }
>
> ```
> Show More

You should pick any two elementIds which will be used in the Steps and Tasks that follow.

## [Step 2: Create Extension Element Group](#step-2-create-extension-element-group)

The following steps demonstrate how you can create an Extension Element Group which corresponds to a Model Element Group by using the createExtensionElementGroup mutation.

This will be required as this is where the extension elements will be created to add properties on.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> ```
> mutation createExtensionElementGroup($elementGroupId: ID!, $name: String) {
> createExtensionElementGroup(elementGroupId: $elementGroupId, name: $name) {
> id
> name
> createdOn
> }
> }
>
> ```

2. In the query variable pane enter the following values.

> **Query Variables**
>
>
>
>
> ```
> {
> "elementGroupId": "{{YOUR_ELEMENT_GROUP_ID}}",
> "name": "Door Cost Extension Group"
> }
>
> ```

The `name` value is optional, but recommended so the extension element group is easy to identify later.

3. Click **Play**. The response should be similar to the following code-block:

> **Response**
>
>
>
>
> ```
> {
> "data": {
> "createExtensionElementGroup": {
> "id": "YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ340NWExYjI4ZS1kZmM2LTQwZWYtOWE4MS05NjdiMjlmOWQ5OTA",
> "name": "Door Cost Extension Group",
> "createdOn": "2025-07-14T20:57:50.000Z"
> }
> }
> }
>
> ```
> Show More

## [Step 3: Verify Extension ElementGroup Creation](#step-3-verify-extension-elementgroup-creation)

The following steps demonstrate how you can get all the Extension Groups associated with the model elementGroup. This can be used to verify the creation of the Extension ElementGroup in the previous step.

You can confirm the creation with the associatedElementGroupsByGroup Query.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> ```
> query ($elementGroupIds: [ID!]!, $pagination: PaginationInput) {
> associatedElementGroupsByGroup(elementGroupIds: $elementGroupIds, pagination: $pagination) {
> results {
> id
> components {
> results {
> ... on ExtensionComponent {
> elementGroup {
> id
> }
> }
> }
> }
> }
> }
> }
>
> ```
> Show More

2. In the query variable pane enter the following values.

> **Query Variables**
>
>
>
>
> ```
> {
> "elementGroupIds": ["{{YOUR_ELEMENT_GROUP_ID}}"]
> }
>
> ```

3. Click **Play**. The response should be similar to the following code-block:

> **Response**
>
>
>
>
> ```
> {
> "data": {
> "associatedElementGroupsByGroup": {
> "results": [
> {
> "id": "YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ340NWExYjI4ZS1kZmM2LTQwZWYtOWE4MS05NjdiMjlmOWQ5OTA",
> "components": {
> "results": [
> {
> "elementGroup": {
> "id": "YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35LNlNrcGdOY1MzSzM3eE1Ea05ZMzBR"
> }
> },
> {},
> {}
> ]
> }
> }
> ]
> }
> }
> }
>
> ```
> Show More

## [Step 4: Add Custom Properties to Extension Elements](#step-4-add-custom-properties-to-extension-elements)

The following steps demonstrate how you can add Extension properties to Elements. These properties are added to extension elements, which are associated with the model element Ids provided. These extension elements are created in the Extension ElementGroup created in Step 2 which is associated with the model Element Group.

In this step we will add a custom cost property created from Task 1 to extension elements by using the addExtensionPropertiesToElements mutation.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> ```
> mutation addExtensionPropertiesToElements($input: AddExtensionPropertiesInput!) {
> addExtensionPropertiesToElements(input: $input) {
> elements {
> id
> name
> properties {
> results {
> name
> value
> }
> }
> }
> }
> }
>
> ```
> Show More

2. In the query variable pane enter the following values.

> **Query Variables**
>
>
>
>
> ```
> {
> "input": {
> "targets": [
> {
> "elementIds": ["{{YOUR_ELEMENT_ID_1}}", "{{YOUR_ELEMENT_ID_2}}"],
> "extensionGroupId": "{{YOUR_EXTENSION_ELEMENT_GROUP_ID}}"
> }
> ],
> "properties": [
> {
> "definitionId": "{{YOUR_CUSTOM_COST_PROPERTY_ID}}",
> "value": "8000.0"
> }
> ]
> }
> }
>
> ```
> Show More

The elementIds can be gotten from step 1. The extensionGroupId is the id of the extension ElementGroup created in Step 2. The definitionId is of the Custom Cost Property created in Task 1.

3. Click **Play**. The response should be similar to the following code-block:

> ```
> {
> "data": {
> "addExtensionPropertiesToElements": {
> "elements": [
> {
> "id": "YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35kNzlkYWRmNC1jZTQxLTQ1MDctYjJjNS04ZDNmOTIzMDAyZDU",
> "name": "",
> "properties": {
> "results": [
> {
> "name": "Cost",
> "value": 8000.0
> }
> ]
> }
> },
> {
> "id": "YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35mMTYxOTU4Mi1lYWQ5LTQ5ZGEtODY0My02YTZjNTJjY2Q3ODg",
> "name": "",
> "properties": {
> "results": [
> {
> "name": "Cost",
> "value": 8000.0
> }
> ]
> }
> }
> ]
> }
> }
> }
>
> ```
> Show More

## [Step 5: Verify Extension Element Creation](#step-5-verify-extension-element-creation)

The following steps demonstrate how you can get all the Extension Elements associated with the model element Ids provided. This can be used to verify the creation of the Extension Elements corresponding to the model elements used in the previous step and that the relevant cost property has been added.

You can confirm the creation and property addition with the following associatedElementsByElements Query.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> ```
> query ($elementIds: [ID!]!, $pagination: PaginationInput) {
> associatedElementsByElements(elementIds: $elementIds, pagination: $pagination) {
> results {
> id
> components {
> results {
> ... on ExtensionComponent {
> element {
> id
> }
> }
> }
> }
> elementGroup {
> id
> }
> properties {
> results {
> name
> value
> }
> }
> }
> }
> }
>
> ```
> Show More

2. In the query variable pane enter the following values.

> **Query Variables**
>
>
>
>
> ```
> {
> "elementIds": ["{{YOUR_ELEMENT_ID_1}}", "{{YOUR_ELEMENT_ID_2}}"]
> }
>
> ```

The element Ids are the same as the previous step which were gotten from Step 1.

3. Click **Play**. The response should be similar to the following code-block:

The above response shows the ids of the extension elements created in the extensionGroup provided, which can also be seen in the elementGroup field for each element in the response. The response also shows the original model element each extension element is associated with, and the Custom Cost property present on each extension element which was just added.
