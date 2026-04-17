# Task 6: Manage Properties Using Category Filter

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/extend_element_data/category_binding_filter_workflow/

---

# Task 6: Manage Properties Using Category Filter

In this tutorial, you will learn how to use category filters to add, update, and remove extension properties. The category filter is used to filter model elements, not extension elements.

When to Use Category Filters:

- When you want to apply properties to all elements of a specific category (e.g., all Doors, all Windows)
- When you don’t know the specific element IDs in advance
- When you want operations to apply to elements dynamically based on their category

In the GraphQL input, this workflow uses the `categoryFilter` field on [ExtensionPropertyTarget](../reference-docs/inputs-extensionpropertytarget.md).

**Important**

- Provide exactly one of `elementIds` or `categoryFilter` in each target.
- `extensionGroupId` must point to the extension group associated with the model element group you want to target.
- For add operations, the property must not already exist on the extension elements.
- For update and remove operations, the property must already exist on the extension elements.

Use the custom property created in Task 1 and the extension group created in Task 2.

## [Step 1: Add Properties Using Category Filter](#step-1-add-properties-using-category-filter)

The following steps demonstrate how to run the `addExtensionPropertiesToElements` mutation by selecting model elements with `categoryFilter`. The mutation then adds properties on the extension elements associated with those selected model elements.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> ```
> mutation addExtensionPropertiesToElements($input: AddExtensionPropertiesInput!) {
> addExtensionPropertiesToElements(input: $input) {
> totalResults
> message
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
> "categoryFilter": {
> "names": ["Walls"]
> },
> "extensionGroupId": "{{YOUR_EXTENSION_ELEMENT_GROUP_ID}}"
> }
> ],
> "properties": [
> {
> "definitionId": "{{YOUR_CUSTOM_COST_PROPERTY_ID}}",
> "value": 50.25
> }
> ]
> }
> }
>
> ```
> Show More

3. Click **Play**. The response should be similar to the following code-block:

> **Response**
>
>
>
>
> ```
> {
> "data": {
> "addExtensionPropertiesToElements": {
> "totalResults": 367,
> "message": "The response only includes the first 100 extension elements. The total amount of elements modified is 367. To view all mutated elements, please use the elementsByElementGroup workflow.",
> "elements": [
> {
> "id": "YWVjZX5FQXVVdG1icWJCTkJIdUx4VkNTRkFjX0wyQ340N2U3NzQwMC0xNmRiLTQ2NDktYTdhOC0zYmI3NDk0MDJiY2M",
> "name": "",
> "properties": {
> "results": [
> {
> "name": "Custom Cost Property",
> "value": 50.25
> }
> ]
> }
> },
> {
> "id": "YWVjZX5FQXVVdG1icWJCTkJIdUx4VkNTRkFjX0wyQ35jMGExMTJkOC0wOTU1LTQxODgtYTMwNy01YTk5MzE0YmM1YmI",
> "name": "",
> "properties": {
> "results": [
> {
> "name": "Custom Cost Property",
> "value": 50.25
> }
> ]
> }
> },
> ...
> ]
> }
> }
> }
>
> ```
> Show More
> The response only includes the first 100 elements that are mutated. To query all the elements that were mutated, follow the message in the response above. This is demonstrated in the next step of the tutorial.

## [Step 2: Query all the Modified Elements in your Extension Group](#step-2-query-all-the-modified-elements-in-your-extension-group)

The following steps demonstrate how to run the `elementsByElementGroup` query on the same Extension ElementGroup, to query all the extension elements that were mutated.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> ```
> query elementsByElementGroup($elementGroupId: ID!, $filter: ElementFilterInput, $pagination: PaginationInput) {
> elementsByElementGroup(elementGroupId: $elementGroupId, filter: $filter, pagination: $pagination) {
> pagination {
> pageSize
> cursor
> }
> results {
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
> "elementGroupId": "{{YOUR_EXTENSION_ELEMENT_GROUP_ID}}",
> "filter": {
> "query": "'property.name.Custom Cost Property' == 50.25"
> },
> "pagination": {
> "limit": 100
> }
> }
>
> ```
> Show More
> Where the property name and value in the filter should be the name and value of the property you added.

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
> "pageSize": 100,
> "cursor": "Y3Vyc34xMDB-MTAw"
> },
> "results": [
> {
> "id": "YWVjZX5FQXVVdG1icWJCTkJIdUx4VkNTRkFjX0wyQ34wMTkzNmM0My1lNzdhLTQ1MjEtOGQ4Yy04YzdiMTIyMTIyNzE",
> "name": "",
> "properties": {
> "results": [
> {
> "name": "Custom Cost Property",
> "value": 50.25
> }
> ]
> }
> },
> {
> "id": "YWVjZX5FQXVVdG1icWJCTkJIdUx4VkNTRkFjX0wyQ34wMjVjMmVlNS0wODZlLTRmODctOGYxNS1lNmNjNTNkYmMxZDg",
> "name": "",
> "properties": {
> "results": [
> {
> "name": "Custom Cost Property",
> "value": 50.25
> }
> ]
> }
> },
> ...
> ]
> }
> }
> }
>
> ```
> Show More
    You can then use the cursor from the above response to paginate through all the modified elements in your extension group.

## [Step 3: Update Properties Using Category Filter](#step-3-update-properties-using-category-filter)

The following steps demonstrate how to run the `updateExtensionPropertiesOnElements` mutation on the same category selection of model elements. The mutation then updates properties on extension elements associated with those model elements.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> ```
> mutation updateExtensionPropertiesOnElements($input: UpdateExtensionPropertiesInput!) {
> updateExtensionPropertiesOnElements(input: $input) {
> totalResults
> message
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
> "categoryFilter": {
> "names": ["Walls"]
> },
> "extensionGroupId": "{{YOUR_EXTENSION_ELEMENT_GROUP_ID}}"
> }
> ],
> "properties": [
> {
> "definitionId": "{{YOUR_CUSTOM_COST_PROPERTY_ID}}",
> "value": 100.54
> }
> ]
> }
> }
>
> ```
> Show More

3. Click **Play**. The response should be similar to the following code-block:

> **Response**
>
>
>
>
> ```
> {
> "data": {
> "updateExtensionPropertiesOnElements": {
> "totalResults": 367,
> "message": "The response only includes the first 100 extension elements. The total amount of elements modified is 367. To view all mutated elements, please use the elementsByElementGroup workflow.",
> "elements": [
> {
> "id": "YWVjZX5FQXVVdG1icWJCTkJIdUx4VkNTRkFjX0wyQ34zMmY2MTMxMy1mZWViLTQ1MDYtYjBkNS1iZWQwM2M1YzFiN2I",
> "name": "",
> "properties": {
> "results": [
> {
> "name": "Custom Cost Property",
> "value": 100.54
> }
> ]
> }
> },
> {
> "id": "YWVjZX5FQXVVdG1icWJCTkJIdUx4VkNTRkFjX0wyQ34yMzQ1MmE0Yy05ZTdkLTRmYWUtYmQ1ZC03NDMwZjk2ZDQ2N2Y",
> "name": "",
> "properties": {
> "results": [
> {
> "name": "Custom Cost Property",
> "value": 100.54
> }
> ]
> }
> },
> ...
> ]
> }
> }
> }
>
> ```
> Show More

## [Step 4: Remove Properties Using Category Filter](#step-4-remove-properties-using-category-filter)

The following steps demonstrate how to run the `removeExtensionPropertiesFromElements` mutation by selecting model elements with `categoryFilter`. The mutation then removes properties from extension elements associated with those selected model elements.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> ```
> mutation removeExtensionPropertiesFromElements($input: RemoveExtensionPropertiesInput!) {
> removeExtensionPropertiesFromElements(input: $input) {
> totalResults
> message
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
> "categoryFilter": {
> "names": ["Walls"]
> },
> "extensionGroupId": "{{YOUR_EXTENSION_ELEMENT_GROUP_ID}}"
> }
> ],
> "propertyDefinitionIds": [
> "{{YOUR_CUSTOM_COST_PROPERTY_ID}}"
> ]
> }
> }
>
> ```
> Show More

3. Click **Play**. The response should be similar to the following code-block:

> **Response**
>
>
>
>
> ```
> {
> "data": {
> "removeExtensionPropertiesFromElements": {
> "totalResults": 367,
> "message": "The response only includes the first 100 extension elements. The total amount of elements modified is 367. To view all mutated elements, please use the elementsByElementGroup workflow.",
> "elements": [
> {
> "id": "YWVjZX5FQXVVdG1icWJCTkJIdUx4VkNTRkFjX0wyQ34zMmY2MTMxMy1mZWViLTQ1MDYtYjBkNS1iZWQwM2M1YzFiN2I",
> "name": "",
> "properties": {
> "results": []
> }
> },
> {
> "id": "YWVjZX5FQXVVdG1icWJCTkJIdUx4VkNTRkFjX0wyQ34yMzQ1MmE0Yy05ZTdkLTRmYWUtYmQ1ZC03NDMwZjk2ZDQ2N2Y",
> "name": "",
> "properties": {
> "results": []
> }
> },
> ...
> ]
> }
> }
> }
>
> ```
> Show More
