# Task 1 - Query Work In Progress Data

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/revit_sync/query_sync_data/

---

# Task 1 - Query Work In Progress Data

In this tutorial you will learn how to query version data for your Revit Models, and what that data means and how it can be used.

The steps include:

1. Listing the `versionHistory` of the model to obtain version numbers.
2. Understanding what each `versionNumber` and `wipVersionNumber` means.
3. Using the `versionFilter` to retrieve data for a specific version.
4. Getting differences between a chosen version type and the latest version.

## [Step 1: Get Complete Version History of a Revit Model](#step-1-get-complete-version-history-of-a-revit-model)

The following steps demonstrate how you can list the versionHistory and alternativeIdentifiers of a Model.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> ```
> query elementGroupAtTip($elementGroupId: ID!) {
> elementGroupAtTip(elementGroupId: $elementGroupId) {
> id
> name
> alternativeIdentifiers{
> fileUrn
> fileVersionUrn
> }
> versionHistory {
> id
> versions {
> results {
> versionNumber
> wipVersionNumber
> createdOn
> elementGroup{
> alternativeIdentifiers{
> fileVersionUrn
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
> "elementGroupId": "{{YOUR_ELEMENT_GROUP_ID}}"
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
> "elementGroupAtTip": {
> "id": "YWVjZH5Hc2V2NElwWkp3TVpoYXdiWUk0Rjk5X0wyQ34zMmE1ZWIxYi1iY2M0LTVlMWYtOTczMS1jYzk1ZGI1OWRkYjA",
> "name": "Residence Sample.rvt",
> "alternativeIdentifiers": {
> "fileUrn": "urn:adsk.wipstg:dm.lineage:bGT_Z5ukSlu2VV0ij0Lgqw",
> "fileVersionUrn": "urn:adsk.wipstg:fs.file:vf.bGT_Z5ukSlu2VV0ij0Lgqw?version=6"
> },
> "versionHistory": {
> "id": "YWVjZH5Hc2V2NElwWkp3TVpoYXdiWUk0Rjk5X0wyQ34zMmE1ZWIxYi1iY2M0LTVlMWYtOTczMS1jYzk1ZGI1OWRkYjA",
> "versions": {
> "results": [
> {
> "versionNumber": null,
> "wipVersionNumber": 9,
> "createdOn": "2026-01-29T09:05:24.834Z",
> "elementGroup": {
> "alternativeIdentifiers": {
> "fileVersionUrn": "urn:adsk.wipstg:fs.file:vf.bGT_Z5ukSlu2VV0ij0Lgqw?version=6"
> }
> }
> },
> {
> "versionNumber": 6,
> "wipVersionNumber": 8,
> "createdOn": "2026-01-13T10:56:54.233Z",
> "elementGroup": {
> "alternativeIdentifiers": {
> "fileVersionUrn": "urn:adsk.wipstg:fs.file:vf.bGT_Z5ukSlu2VV0ij0Lgqw?version=6"
> }
> }
> },
> {
> "versionNumber": null,
> "wipVersionNumber": 7,
> "createdOn": "2026-01-13T10:56:46.467Z",
> "elementGroup": {
> "alternativeIdentifiers": {
> "fileVersionUrn": "urn:adsk.wipstg:fs.file:vf.bGT_Z5ukSlu2VV0ij0Lgqw?version=5"
> }
> }
> },
> {
> "versionNumber": null,
> "wipVersionNumber": 6,
> "createdOn": "2026-01-13T10:56:42.189Z",
> "elementGroup": {
> "alternativeIdentifiers": {
> "fileVersionUrn": "urn:adsk.wipstg:fs.file:vf.bGT_Z5ukSlu2VV0ij0Lgqw?version=5"
> }
> }
> },
> {
> "versionNumber": 5,
> "wipVersionNumber": 5,
> "createdOn": "2026-01-13T10:56:33.397Z",
> "elementGroup": {
> "alternativeIdentifiers": {
> "fileVersionUrn": "urn:adsk.wipstg:fs.file:vf.bGT_Z5ukSlu2VV0ij0Lgqw?version=5"
> }
> }
> }
> ]
> }
> }
> }
> }
>
> ```
> Show More

Additional entries in `results` use the same shape and are omitted here.

From the above response in the version history, you can see `versionNumber` and `wipVersionNumber`.

Note

**versionNumber** is the published (lineage) version of the model, while **wipVersionNumber** is the Work In Progress version. **fileVersionUrn** always corresponds to the last published version of the model. The **Work In Progress** version refers to the **Revit cloud work sharing sync to central** version in Revit.

Using this query you can see the latest Work In Progress version by looking at the latest wipVersionNumber and the latest PUBLISHED version by looking at the latest versionNumber.

## [Step 2: Using the VersionFilter to Get ElementGroup at a Particular Work In Progress Version](#step-2-using-the-versionfilter-to-get-elementgroup-at-a-particular-work-in-progress-version)

The following steps demonstrate how you can use the [versionFilterInput](../reference-docs/inputs-versionfilterinput.md) to get the elementGroup corresponding to a particular Work In Progress version (wipVersionNumber).

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> ```
> query elementGroupByVersionNumber($elementGroupId: ID!, $versionNumber: Int!, $versionFilter: VersionFilterInput) {
> elementGroupByVersionNumber(elementGroupId: $elementGroupId, versionNumber: $versionNumber, versionFilter: $versionFilter) {
> id
> name
> alternativeIdentifiers{
> fileVersionUrn
> }
> version{
> versionNumber
> wipVersionNumber
> createdOn
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
> "elementGroupId": "{{YOUR_ELEMENT_GROUP_ID}}",
> "versionNumber": 8,
> "versionFilter": {
> "versionType": "WIP"
> }
> }
>
> ```

The `versionType` value is WIP in this case to define that we are querying for a Work In Progress version. The versionNumber should be whatever version you are interested in.

3. Click **Play**. The response should be similar to the following code-block:

> **Response**
>
>
>
>
> ```
> {
> "data": {
> "elementGroupByVersionNumber": {
> "id": "YWVjZH5Hc2V2NElwWkp3TVpoYXdiWUk0Rjk5X0wyQ34zMmE1ZWIxYi1iY2M0LTVlMWYtOTczMS1jYzk1ZGI1OWRkYjA",
> "name": "Residence Sample.rvt",
> "alternativeIdentifiers": {
> "fileVersionUrn": "urn:adsk.wipstg:fs.file:vf.bGT_Z5ukSlu2VV0ij0Lgqw?version=6"
> },
> "version": {
> "versionNumber": 6,
> "wipVersionNumber": 8,
> "createdOn": "2026-01-13T10:56:54.233Z"
> }
> }
> }
> }
>
> ```
> Show More
> In the above we get the elementGroup at wipVersionNumber 8 which is what is defined by the filter.

## [Step 3: Using the VersionFilter to Get ElementGroup at a Particular PUBLISHED Version](#step-3-using-the-versionfilter-to-get-elementgroup-at-a-particular-published-version)

The following steps demonstrate how you can use the [versionFilterInput](../reference-docs/inputs-versionfilterinput.md) to get the elementGroup corresponding to a particular **published** version (`versionNumber`).

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> ```
> query elementGroupByVersionNumber($elementGroupId: ID!, $versionNumber: Int!, $versionFilter: VersionFilterInput) {
> elementGroupByVersionNumber(elementGroupId: $elementGroupId, versionNumber: $versionNumber, versionFilter: $versionFilter) {
> id
> name
> alternativeIdentifiers{
> fileVersionUrn
> }
> version{
> versionNumber
> wipVersionNumber
> createdOn
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
> "elementGroupId": "{{YOUR_ELEMENT_GROUP_ID}}",
> "versionNumber": 3,
> "versionFilter": {
> "versionType": "PUBLISHED"
> }
> }
>
> ```

The `versionType` value is PUBLISHED in this case to define that we are querying for a PUBLISHED version. The versionNumber should be whatever version you are interested in.

3. Click **Play**. The response should be similar to the following code-block:

> **Response**
>
>
>
>
> ```
> {
> "data": {
> "elementGroupByVersionNumber": {
> "id": "YWVjZH5Hc2V2NElwWkp3TVpoYXdiWUk0Rjk5X0wyQ34zMmE1ZWIxYi1iY2M0LTVlMWYtOTczMS1jYzk1ZGI1OWRkYjA",
> "name": "Residence Sample.rvt",
> "alternativeIdentifiers": {
> "fileVersionUrn": "urn:adsk.wipstg:fs.file:vf.bGT_Z5ukSlu2VV0ij0Lgqw?version=3"
> },
> "version": {
> "versionNumber": 3,
> "wipVersionNumber": 4,
> "createdOn": "2026-01-13T10:56:17.420Z"
> }
> }
> }
> }
>
> ```
> Show More
> In the above we get the elementGroup at versionNumber 3 which is what is defined by the filter.

Note

The `versionFilter` can be used in the same way for all version-based queries and subqueries:

- [elementGroupByVersionNumber](../reference-docs/queries-elementgroupbyversionnumber.md)
- [elementsByElementGroupAtVersion](../reference-docs/queries-elementsbyelementgroupatversion.md)
- [diffElementGroupByVersionWithLatest](../reference-docs/queries-diffelementgroupbyversionwithlatest.md)
- [diffElementByVersionWithLatest](../reference-docs/queries-diffelementbyversionwithlatest.md)
- [elementGroupVersionHistory](../reference-docs/objects-elementgroupversionhistory.md) (`versionByNumber`)

## [Step 4: Get differences between a particular version and the latest](#step-4-get-differences-between-a-particular-version-and-the-latest)

The following steps demonstrate how you can use the [versionFilterInput](../reference-docs/inputs-versionfilterinput.md) and the [diffElementGroupByVersionWithLatest](../reference-docs/queries-diffelementgroupbyversionwithlatest.md) query to get the changes between an elementGroup at a particular versionType and the latest version.

1. Enter the following query in the Query Pane of the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/).

> **Query**
>
>
>
>
> ```
> query diffElementGroupByVersionWithLatest($elementGroupId: ID!, $startVersion: Int, $changeFilter: [DifferenceType], $pagination: PaginationInput, $versionFilter: VersionFilterInput) {
> diffElementGroupByVersionWithLatest(elementGroupId: $elementGroupId, startVersion: $startVersion, changeFilter:$changeFilter, pagination: $pagination, versionFilter: $versionFilter) {
> result{
> type
> element{
> id
> name
> }
> differences{
> pagination{
> cursor
> pageSize
> }
> results{
> type
> oldItem{
> name
> value
> }
> item{
> name
> value
> }
> }
> }
> }
> pagination{
> pageSize
> cursor
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
> "elementGroupId": "{{YOUR_ELEMENT_GROUP_ID}}",
> "startVersion": 8,
> "changeFilter": ["REMOVAL", "ADDITION", "MODIFICATION"],
> "pagination": {
> "limit": 100
> },
> "versionFilter": {
> "versionType": "WIP"
> }
> }
>
> ```
> Show More

The `versionType` value is WIP in this case, so `startVersion` is interpreted as a Work In Progress version. You can use `PUBLISHED` instead to interpret `startVersion` as a published version.
For this example, the differences are between that Work In Progress version and the latest version.

3. Click **Play**. The response should be similar to the following code-block:

> **Response**
>
>
>
>
> ```
> {
> "data": {
> "diffElementGroupByVersionWithLatest": {
> "result": [
> {
> "type": "MODIFICATION",
> "element": {
> "id": "YWVjZX5Hc2V2NElwWkp3TVpoYXdiWUk0Rjk5X0wyQ34yOTJjYTA5ZS0wZTA5LTUwMjYtYmRhYS02NDc3N2ZkZmVjM2I",
> "name": "Window Types (El Cabrillo)"
> },
> "differences": {
> "pagination": {
> "cursor": null,
> "pageSize": 2
> },
> "results": [
> {
> "type": "ADDITION",
> "oldItem": null,
> "item": {
> "name": "Edited by",
> "value": ""
> }
> },
> {
> "type": "ADDITION",
> "oldItem": null,
> "item": {
> "name": "Workset",
> "value": 701
> }
> }
> ]
> }
> },
> {
> "type": "ADDITION",
> "element": {
> "id": "YWVjZX5Hc2V2NElwWkp3TVpoYXdiWUk0Rjk5X0wyQ34xMDNmZjc2My0yMzQzLTU0YzMtOGMxMy03ZGIyZTliOTNlNTU",
> "name": ""
> },
> "differences": {
> "pagination": null,
> "results": null
> }
> },
> {
> "type": "MODIFICATION",
> "element": {
> "id": "YWVjZX5Hc2V2NElwWkp3TVpoYXdiWUk0Rjk5X0wyQ34yODhlMWQ1My1iMDBlLTU3NDItOTgyMi01ODdkMzFmNzM4NzU",
> "name": "1/2\""
> },
> "differences": {
> "pagination": {
> "cursor": null,
> "pageSize": 3
> },
> "results": [
> {
> "type": "ADDITION",
> "oldItem": null,
> "item": {
> "name": "Workset",
> "value": 517
> }
> },
> {
> "type": "REMOVAL",
> "oldItem": {
> "name": "Width",
> "value": 0.012700000000000001
> },
> "item": null
> },
> {
> "type": "ADDITION",
> "oldItem": null,
> "item": {
> "name": "Edited by",
> "value": ""
> }
> }
> ]
> }
> }
> ],
> "pagination": {
> "pageSize": 100,
> "cursor": null
> }
> }
> }
> }
>
> ```
> Show More

For more detail on the Diff API, see the [diffElementGroupByVersionWithLatest](../reference-docs/queries-diffelementgroupbyversionwithlatest.md) query reference.
