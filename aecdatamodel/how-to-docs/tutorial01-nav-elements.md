# Navigate to ElementGroups within a Project

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/tutorial01/nav-elements/

---

# Navigate to ElementGroups within a Project

In this guide, you will learn how to retrieve a list of ElementGroups within a specific project. ElementGroups are collections of elements that can be used to organize and manage data in Autodesk AEC applications.

By the end of this guide, you will be able to:

- Fetch elementGroup files available in a project.
- Understand the options and fields in the documentation on the `elementGroupsByProject` query, the results, and versions.

You will use the following query in this guide:

| Type | Operation | Description |
| --- | --- | --- |
| Query | [elementGroupsByProject](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elementGroupsByProject/) | Retrieves all elementGroups within a specific project. |

## [Step 1: Request for a list of ElementGroups within a Project](#step-1-request-for-a-list-of-elementgroups-within-a-project)

The [elementGroupsByProject](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elementgroupsbyproject/) query returns [ElementGroups](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/elementgroups/) object. The `ElementGroups` object contains a list of ElementGroups.
> 1. In [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/), the query is populated by default in the **Query Pane**. You can also edit or update the query as per your requirement and run it.
>
>
>
> > **Query**
> >
> >
> >
> >
> > ```
> > query GetElementGroupsByProject($projectId: ID!) {
> > elementGroupsByProject(projectId: $projectId) {
> > pagination {
> > cursor
> > }
> > results{
> > name
> > id
> > alternativeIdentifiers{
> > fileUrn
> > fileVersionUrn
> > }
> > }
> > }
> > }
> >
> > ```
> > Show More
>
> 2. In the Query Variables Pane, enter the value of the `projectId` obtained from [Get Projects](https://aps.autodesk.com/en/docs/aecdatamodel/v1/tutorials/tutorial-01/getprojects/) topic.
>
>
>
> > **Query Variables**
> >
> >
> >
> >
> > ```
> > {
> > "projectId": "urn:adsk.workspace:prod.project:39208068-e548-4d9e-b8a7-e000fdf2a9b4"
> > }
> >
> > ```
>
> 3. Click **Play**. The list of elementGroups available within that project is displayed in the response. Note down the ElementGroup IDs of one of the Revit models (this case .rvt file you want to work with). You will need these IDs for the remaining guides. For this tutorial, we will use the ID of the item named “Snowdon Towers Sample Architectural.rvt”.
>
>
>
> > The response should be similar to the following code-block:
> >
> > **Response**
> >
> >
> >
> >
> > ```
> > {
> > "data": {
> > "elementGroupsByProject": {
> > "pagination": {
> > "cursor": null
> > },
> > "results": [
> > {
> > "name": "Snowdon Towers Sample HVAC.rvt",
> > "id": "YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35uUVpyS1BEUVJVS0VFOWtmWWNHV0VB",
> > "alternativeIdentifiers": {
> > "fileUrn": "urn:adsk.wipprod:dm.lineage:nQZrKPDQRUKEE9kfYcGWEA",
> > "fileVersionUrn": "urn:adsk.wipprod:fs.file:vf.nQZrKPDQRUKEE9kfYcGWEA?version=1"
> > }
> > },
> > {
> > "name": "Snowdon Towers Sample Electrical.rvt",
> > "id": "YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35fR1IzdHpORlI3LV9tclFBOGR4TWN3",
> > "alternativeIdentifiers": {
> > "fileUrn": "urn:adsk.wipprod:dm.lineage:_GR3tzNFR7-_mrQA8dxMcw",
> > "fileVersionUrn": "urn:adsk.wipprod:fs.file:vf._GR3tzNFR7-_mrQA8dxMcw?version=1"
> > }
> > },
> > {
> > "name": "Snowdon Towers Sample Architectural.rvt",
> > "id": "YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVB",
> > "alternativeIdentifiers": {
> > "fileUrn": "urn:adsk.wipprod:dm.lineage:rEdJOCOqR0ekyJBBYlR9EA",
> > "fileVersionUrn": "urn:adsk.wipprod:fs.file:vf.rEdJOCOqR0ekyJBBYlR9EA?version=1"
> > }
> > },
> > {
> > "name": "Snowdon Towers Sample Site.rvt",
> > "id": "YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRR",
> > "alternativeIdentifiers": {
> > "fileUrn": "urn:adsk.wipprod:dm.lineage:LvosTJ57RXefNY1bachQTQ",
> > "fileVersionUrn": "urn:adsk.wipprod:fs.file:vf.LvosTJ57RXefNY1bachQTQ?version=1"
> > }
> > },
> > {
> > "name": "Snowdon Towers Sample Facades.rvt",
> > "id": "YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1n",
> > "alternativeIdentifiers": {
> > "fileUrn": "urn:adsk.wipprod:dm.lineage:fWDufB-ySmq5Fwn6Fj1_-g",
> > "fileVersionUrn": "urn:adsk.wipprod:fs.file:vf.fWDufB-ySmq5Fwn6Fj1_-g?version=1"
> > }
> > },
> > {
> > "name": "Snowdon Towers Sample Structural.rvt",
> > "id": "YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3",
> > "alternativeIdentifiers": {
> > "fileUrn": "urn:adsk.wipprod:dm.lineage:t9M1_BwUTNmYemthQPX4xw",
> > "fileVersionUrn": "urn:adsk.wipprod:fs.file:vf.t9M1_BwUTNmYemthQPX4xw?version=1"
> > }
> > },
> > {
> > "name": "Snowdon Towers Sample Plumbing.rvt",
> > "id": "YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35CR2QwdEpOc1NHNlZWSFFibkZ6cFFR",
> > "alternativeIdentifiers": {
> > "fileUrn": "urn:adsk.wipprod:dm.lineage:BGd0tJNsSG6VVHQbnFzpQQ",
> > "fileVersionUrn": "urn:adsk.wipprod:fs.file:vf.BGd0tJNsSG6VVHQbnFzpQQ?version=1"
> > }
> > },
> > {
> > "name": "areatest.rvt",
> > "id": "YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ340VFVtRnF0WFJVVy1CS09Gb1cyd3FR",
> > "alternativeIdentifiers": {
> > "fileUrn": "urn:adsk.wipprod:dm.lineage:4TUmFqtXRUW-BKOFoW2wqQ",
> > "fileVersionUrn": "urn:adsk.wipprod:fs.file:vf.4TUmFqtXRUW-BKOFoW2wqQ?version=3"
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

## [Step 2: To preview the model](#step-2-to-preview-the-model)
> 1. Enter the fileVersionUrn of the model. For example, refer to the ID urn:adsk.wipprod:fs.file:vf.rEdJOCOqR0ekyJBBYlR9EA?version=1 as mentioned in the Revit model Snowdon Towers Sample Architectural.rvt.
> 2. Click **Viewer** to preview the model.
>
>
>
> > After working through the steps mentioned above, you should see a screen similar to the following image:
> > :   
