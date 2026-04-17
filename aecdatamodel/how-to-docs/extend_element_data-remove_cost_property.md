# Task 5: Remove Cost property from extension Elements

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/extend_element_data/remove_cost_property/

---

# Task 5: Remove Cost property from extension Elements

In this tutorial you will learn how to remove existing extension properties from extension elements corresponding to model elements.

The purpose of this is to show that you can also remove properties along with add and update (Shown previously).

## [Step 1: Remove Cost property from Extension Elements](#step-1-remove-cost-property-from-extension-elements)

The following steps demonstrate how you can run the removeExtensionPropertiesFromElements mutation to remove existing properties from extension elements corresponding to model elements, in a particular extension elementGroup.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> ```
> mutation removeExtensionPropertiesFromElements($input: RemoveExtensionPropertiesInput!) {
> removeExtensionPropertiesFromElements(input: $input) {
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
> "targets": [{
> "elementIds": ["{{YOUR_ELEMENT_ID_1}}", "{{YOUR_ELEMENT_ID_2}}"],
> "extensionGroupId": "{{YOUR_EXTENSION_ELEMENT_GROUP_ID}}"
> }],
> "propertyDefinitionIds": ["{{YOUR_CUSTOM_COST_PROPERTY_ID}}"]
> }
> }
>
> ```
> Show More

The variables are the same as the ones used in the previous tasks.

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
> "elements": [
> {
> "id": "YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35kNzlkYWRmNC1jZTQxLTQ1MDctYjJjNS04ZDNmOTIzMDAyZDU",
> "name": "",
> "properties": {
> "results": []
> }
> },
> {
> "id": "YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35mMTYxOTU4Mi1lYWQ5LTQ5ZGEtODY0My02YTZjNTJjY2Q3ODg",
> "name": "",
> "properties": {
> "results": []
> }
> }
> ]
> }
> }
> }
>
> ```
> Show More
