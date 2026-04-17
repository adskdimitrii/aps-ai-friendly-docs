# Task 1 - Property Definition Creation

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/extend_element_data/create_property_definition/

---

# Task 1 - Property Definition Creation

In this tutorial, you will learn how to create a property definition using the AEC DM API. Alternatively, you can also complete this process through the ACC admin UI.

To create extension properties, you first need to create a property definition (also known as a parameter). A property definition acts as a template for a property that you can use to create multiple properties. It specifies the property name, data type, and other relevant information.

You will use the following mutations in this task:

## [Step 1: Create Property Definition Collection](#step-1-create-property-definition-collection)

The following steps demonstrate how you can run the [createPropertyDefinitionCollectionInHub](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/mutations/createpropertydefinitioncollectioninhub/) mutation to create a property definition collection.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> > ```
> > mutation createCollection($collectionInput: CreatePropertyDefinitionCollectionInHubInput!) {
> > createPropertyDefinitionCollectionInHub(input: $collectionInput) {
> > propertyDefinitionCollection {
> > id
> > name
> > description
> > }
> > }
> > }
> >
> > ```
> > Show More

2. In the query variable pane enter the following values

> **Query Variables**
>
>
>
>
> > ```
> > {
> > "collectionInput": {
> > "hubId": "{{Your_Hub_Id}}",
> > "title": "Example Collection",
> > "description": "This is an example collection."
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
> > ```
> > {
> > "data": {
> > "createPropertyDefinitionCollectionInHub": {
> > "propertyDefinitionCollection": {
> > "id": "cGRjfjIyZWRmNWI1LWVjZjctNDc1My04MmExLWRkYmE3Nzk1YTY1ZH4yMmVkZjViNS1lY2Y3LTQ3NTMtODJhMS1kZGJhNzc5NWE2NWR-ZTM5N2E5MmUtMDdjNi00MWJlLTgwMTEtNWVkMDc1YmYxOTU5",
> > "name": "Example Collection",
> > "description": "This is an example collection."
> > }
> > }
> > }
> > }
> >
> > ```
> > Show More

## [Step 2: Create Property Definition](#step-2-create-property-definition)

The following steps demonstrate how you can run the [createPropertyDefinitionsInCollection](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/mutations/createpropertydefinitionsincollection/) mutation to create a property definition.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> > ```
> > mutation createPropertyDefinitions($definitionInput: CreatePropertyDefinitionsInCollectionInput!) {
> > createPropertyDefinitionsInCollection(input: $definitionInput) {
> > propertyDefinitions {
> > id
> > name
> > description
> > }
> > }
> > }
> >
> > ```
> > Show More

2. In the query variable pane enter the following values, replacing the placeholders for property definition collection id and property definition specification id.

> **Query Variables**
>
>
>
>
> > ```
> > {
> > "definitionInput": {
> > "propertyDefinitionCollectionId": "{{Your_Property_Definition_Collection_Id}}",
> > "propertyDefinitionsInput": [{
> > "name": "Cost",
> > "specification": "{{property_definition_specification_id}}",
> > "description": "Property used for cost estimates."
> > }]
> > }
> > }
> >
> > ```
> > Show More

**Common Property Definition Specification ids**
> | Type | Property Specification Id |
> | --- | --- |
> | Int64 | autodesk.spec:spec.int64-2.0.0 |
> | Text | autodesk.spec:spec.string-2.0.0 |
> | Length | autodesk.spec.aec:length-2.0.1 |
> | Bool | autodesk.spec:spec.bool-1.0.0 |
> | Cost Per Area | autodesk.spec.aec:costPerArea-2.0.0 |
> | Number/Float64 | autodesk.spec.aec:number-2.0.0 |
> | Area | autodesk.spec.aec:area-2.0.0 |
>
> Following query can be used to find further specification ids for creating extensibility properties:
>
> **Query**
>
>
>
>
> > ```
> > query getSpecifications ($pagination: PaginationInput){
> > propertyDefinitionSpecifications (pagination: $pagination){
> > pagination {
> > cursor
> > }
> > results {
> > id
> > name
> > valueType
> > }
> > }
> > }
> >
> > ```
> >
> >
> > Show More
>
> **Query Variables**
>
>
>
>
> > ```
> > {
> > "pagination": {
> > "limit" : 50
> > }
> > }
> >
> > ```
>
> **Response**
>
>
>
>
> > ```
> > {
> > "data": {
> > "propertyDefinitionSpecifications": {
> > "pagination": {
> > "cursor": "c3BlY0N1cnNvcn4zNTZ-NTB-MA"
> > },
> > "results": [
> > {
> > "id": "autodesk.spec.aec.electrical:apparentPower-2.0.0",
> > "name": "Apparent Power",
> > "valueType": "Float64"
> > },
> > ...
> > ]
> > }
> > }
> > }
> >
> > ```
> >
> >
> > Show More

3. Click **Play**. The response should be similar to the following code-block:

> **Response**
>
>
>
>
> > ```
> > {
> > "data": {
> > "createPropertyDefinitionsInCollection": {
> > "propertyDefinitions": [{
> > "id": "{{Property_Definition_Id}}",
> > "name": "Cost",
> > "description": "Property used for cost estimates."
> > }]
> > }
> > }
> > }
> >
> > ```
> > Show More
