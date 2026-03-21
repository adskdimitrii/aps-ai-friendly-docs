# Get Projects

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/tutorial01/getprojects/

---

# Get Projects

In this guide, you will learn how to retrieve a list of all projects available within the hubs you have access to.

By the end of this guide, you will be able to:

- Fetch project information like project ID and name of the project.
- Understand the options and fields in the documentation on the [projects](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/projects/) query, [Projects](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/projects/) object, and [Project](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/project/) object.

You will use the following query in this guide:

| Type | Operation | Description |
| --- | --- | --- |
| Query | [projects](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/projects/) | Retrieves all projects within a specified hub. |

## [Step 1: Request for a list of Projects within a Hub](#step-1-request-for-a-list-of-projects-within-a-hub)

The [projects](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/projects/) query returns a [Projects](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/projects/) object. The Projects object contains an array of [Project](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/project/) objects. In this exercise, we query for the `project id` and `project name` fields.
> 1. In the [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/), the query is populated by default in the **Query Pane**. You can also edit or update the query as per your requirement and run it.
>
>
>
> > **Query**
> >
> >
> >
> >
> > ```
> > query GetProjects($hubId: ID!) {
> > projects(hubId: $hubId) {
> > pagination {
> > cursor
> > }
> > results {
> > id
> > name
> > alternativeIdentifiers{
> > dataManagementAPIProjectId
> > }
> > }
> > }
> > }
> >
> > ```
> > Show More
>
> 2. In the Query Variables Pane, enter the value of the `hubId` obtained from [Get Hubs](https://aps.autodesk.com/en/docs/aecdatamodel/v1/tutorials/tutorial-01/gethubs/) topic.
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
> > "hubId": "urn:adsk.ace:prod.scope:dccde3e3-c20c-40d3-a27c-7ac53b051b6e"
> > }
> >
> > ```
>
> 3. Click **Play**. The list of projects available within that hub is displayed in the response. Note down the ExternalIDs and Project IDs of one of the projects. You will need these IDs for the remaining tasks. In this tutorial, we will use the ID of the project named “AEC DM Bootcamp Project”. The response should be similar to the following code-block:
>
>
>
> > **Response**
> >
> >
> >
> >
> > ```
> > {
> > "data": {
> > "projects": {
> > "pagination": {
> > "cursor": null
> > },
> > "results": [
> > {
> > "id": "urn:adsk.workspace:prod.project:39208068-e548-4d9e-b8a7-e000fdf2a9b4",
> > "name": "AEC DM Bootcamp Project",
> > "alternativeIdentifiers": {
> > "dataManagementAPIProjectId": "b.ddcecd34-68b7-41af-ad65-2ce571186c6c"
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
