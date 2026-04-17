# Task 1 - Retrieve Differences of an Element Group

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/diff_api/diff_api_tutorial/

---

# Task 1 - Retrieve Differences of an Element Group

In this tutorial, you will learn how to use the Diff API to query the changes between a specified version and the latest version of an ElementGroup.

The Diff API allows you to retrieve the differences from a version against the latest of an ElementGroup and its elements. You can also paginate through the property differences of a particular element.

## [Step 1 - Retrieve Element Differences of an ElementGroup By Version From the Latest](#step-1-retrieve-element-differences-of-an-elementgroup-by-version-from-the-latest)

The following steps demonstrate how you can run the [diffElementGroupByVersionWithLatest](../reference-docs/queries-diffelementgroupbyversionwithlatest.md) query to get the changes in an ElementGroup after a particular version.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> > ```
> > query diffElementGroupByVersionWithLatest($elementGroupId: ID!, $startVersion: Int, $changeFilter:[DifferenceType] $pagination: PaginationInput) {
> > diffElementGroupByVersionWithLatest(elementGroupId: $elementGroupId, startVersion: $startVersion, changeFilter:$changeFilter, pagination: $pagination) {
> > pagination{
> > pageSize
> > cursor
> > }
> > result{
> > type
> > element{
> > id
> > name
> > }
> > differences {
> > pagination{
> > cursor
> > pageSize
> > }
> > results{
> > type
> > oldItem{
> > name
> > value
> > }
> > item{
> > name
> > value
> > }
> > }
> > }
> >
> > }
> >
> > }
> > }
> >
> > ```
> > Show More

2. In the query variable pane enter the following values, replacing the placeholders for elementGroupId and startVersion.
    The elementGroupId will be the id of the particular elementGroup you are interested in, and the startVersion will be the version of that elementGroup that you want to see the changes after against the latest.
> **Query Variables**
>
>
>
>
> > ```
> > {
> > "elementGroupId": "{{YOUR_ELEMENT_GROUP_ID}}",
> > "startVersion" : {{YOUR_START_VERSION}},
> > "changeFilter": ["REMOVAL", "ADDITION", "MODIFICATION"],
> > "pagination": {
> > "limit": 100
> > }
> > }
> >
> > ```
> > Show More
> The change filter can also be adjusted to query what kind of changes you are interested in for elements. The supported types of changes are: REMOVAL, ADDITION and MODIFICATION.
>
> **Supported Change Filter Types**
>
> | Type | Filtered Change |
> | --- | --- |
> | ADDITION | Shows elements that have been added |
> | MODIFICATION | Shows elements that have been modified |
> | REMOVAL | Shows elements that have been removed |
> Note: Not specifying a changeFilter, will retrieve all the element differences.

3. Click **Play**. The response should be similar to the following code-block:

> **Response**
>
>
>
>
> > ```
> > {
> > "data": {
> > "diffElementGroupByVersionWithLatest": {
> > "pagination": {
> > "pageSize": 73,
> > "cursor": null
> > },
> > "result": [
> > {
> > "type": "MODIFICATION",
> > "element": {
> > "id": "YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35jNG5FNXNFRlRrbVB5ODM0cnlOTFN3XzIwOTEyYg",
> > "name": "Concrete Slab 6\""
> > },
> > "differences": {
> > "pagination": {
> > "cursor": null,
> > "pageSize": 3
> > },
> > "results": [
> > {
> > "type": "MODIFICATION",
> > "oldItem": {
> > "name": "Volume",
> > "value": 178.76503887821477
> > },
> > "item": {
> > "name": "Volume",
> > "value": 187.54936329898482
> > }
> > },
> > {
> > "type": "MODIFICATION",
> > "oldItem": {
> > "name": "Perimeter",
> > "value": 189.64061013477095
> > },
> > "item": {
> > "name": "Perimeter",
> > "value": 207.41600094799753
> > }
> > },
> > {
> > "type": "MODIFICATION",
> > "oldItem": {
> > "name": "Area",
> > "value": 1172.998942770438
> > },
> > "item": {
> > "name": "Area",
> > "value": 1230.6388667912388
> > }
> > }
> > ]
> > }
> > },
> > {
> > "type": "ADDITION",
> > "element": {
> > "id": "YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35jNG5FNXNFRlRrbVB5ODM0cnlOTFN3XzI4NzkxOQ",
> > "name": ""
> > },
> > "differences": {
> > "pagination": null,
> > "results": null
> > }
> > },
> > {
> > "type": "REMOVAL",
> > "element": {
> > "id": "YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35jNG5FNXNFRlRrbVB5ODM0cnlOTFN3XzIwZGRkYg",
> > "name": "Model Lines"
> > },
> > "differences": {
> > "pagination": null,
> > "results": null
> > }
> > }
> > ]
> > }
> > }
> > }
> >
> > ```
> > Show More

## [Step 2 - Retrieve and Paginate Property Differences of an Element By Version From the Latest](#step-2-retrieve-and-paginate-property-differences-of-an-element-by-version-from-the-latest)

The following steps demonstrate how you can run the [diffElementByVersionWithLatest](../reference-docs/queries-diffelementbyversionwithlatest.md) query to retrieve and paginate through the property differences of a particular element you are interested in.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> > ```
> > query diffElementByVersionWithLatest($elementId: ID!, $startElementGroupVersion: Int, $pagination: PaginationInput) {
> > diffElementByVersionWithLatest(elementId: $elementId, startElementGroupVersion: $startElementGroupVersion) {
> > type
> > element{
> > id
> > name
> > }
> > differences(pagination: $pagination) {
> > pagination{
> > cursor
> > pageSize
> > }
> > results{
> > type
> > oldItem{
> > name
> > value
> > }
> > item{
> > name
> > value
> > }
> > }
> > }
> >
> > }
> > }
> >
> > ```
> > Show More

2. In the query variable pane enter the following values, replacing the placeholders for elementId and startElementGroupVersion.
    The elementId can be retrieved from Step 1 for the particular element whose property differences you are interested in, the startElementGroupVersion will be the same as the startVersion in Step 1.
> **Query Variables**
>
>
>
>
> > ```
> > {
> > "elementId": "{{YOUR_ELEMENT_ID}}",
> > "startElementGroupVersion" : {{YOUR_START_VERSION}},
> > "pagination": {
> > "limit":  3
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
> > "diffElementByVersionWithLatest": {
> > "type": "MODIFICATION",
> > "element": {
> > "id": "YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35jNG5FNXNFRlRrbVB5ODM0cnlOTFN3XzI2MTEwMA",
> > "name": "Commercial/Retail 76"
> > },
> > "differences": {
> > "pagination": {
> > "cursor": "Y3Vyc34zfjM",
> > "pageSize": 3
> > },
> > "results": [
> > {
> > "type": "MODIFICATION",
> > "oldItem": {
> > "name": "Room Name",
> > "value": "Commercial/Retail"
> > },
> > "item": {
> > "name": "Room Name",
> > "value": "Unoccupied"
> > }
> > },
> > {
> > "type": "MODIFICATION",
> > "oldItem": {
> > "name": "Room Number",
> > "value": "108"
> > },
> > "item": {
> > "name": "Room Number",
> > "value": "Unoccupied"
> > }
> > },
> > {
> > "type": "MODIFICATION",
> > "oldItem": {
> > "name": "Area",
> > "value": 213.99606898281348
> > },
> > "item": {
> > "name": "Area",
> > "value": null
> > }
> > }
> > ]
> > }
> > }
> > }
> > }
> >
> > ```
> > Show More
> The cursor provided can then be used to paginate through the property differences in subsequent queries.
