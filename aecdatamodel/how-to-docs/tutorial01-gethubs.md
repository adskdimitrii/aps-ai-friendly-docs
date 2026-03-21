# Get Hubs

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/tutorial01/gethubs/

---

# Get Hubs

In this guide, you will learn how to retrieve a list of all the hubs you have access to.

By the end of this guide, you will be able to:

- Send a query using AEC Data Model Explorer.
- Understand the fields in the [hubs](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/hubs/) query, [Hubs](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/hubs/) object, and [Hub](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/hub/) objects.

You will use the following query in this guide:

| Type | Operation | Description |
| --- | --- | --- |
| Query | [hubs](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/hubs/) | Retrieves all hubs accessible to you. |

## [Step 1: Request a list of Hubs](#step-1-request-a-list-of-hubs)

The [hubs](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/hubs/) query returns a [Hubs](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/hubs/) object. The Hubs object contains an array of [Hub](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/hub/) objects. While the Hub object has many fields, for this exercise, we will be requesting the `id` and the `name` fields only.
> 1. In [AEC Data Model Explorer](https://aecdatamodel-explorer.autodesk.io/), the query is populated by default in the **Query Pane**. You can also edit or update the query as per your requirement and run it.
>
>
>
> > **Query**
> >
> >
> >
> >
> > > ```
> > > query GetHubs {
> > > hubs {
> > > pagination {
> > > cursor
> > > }
> > > results {
> > > name
> > > id
> > > }
> > > }
> > > }
> > >
> > > ```
> > > Show More
>
> 2. Click **Play**. A list of hubs that you have access to is displayed in the response section. It should be similar to the following code-block:
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
> > "hubs": {
> > "pagination": {
> > "cursor": null
> > },
> > "results": [
> > {
> > "name": "AEC DM Developer Advocacy Support",
> > "id": "urn:adsk.ace:prod.scope:dccde3e3-c20c-40d3-a27c-7ac53b051b6e"
> > },
> > {
> > "name": "Developer Advocacy Support",
> > "id": "urn:adsk.ace:prod.scope:c0c44a35-fc67-4a8d-8967-f2d975bc03ec"
> > }
> > ]
> > }
> > }
> > }
> >
> > ```
> > Show More
>
> Note down the ID of the hubs that you wish to use. You will need this ID for the remaining guides.
>
> After working through the steps mentioned above, you should see a screen similar to the following image:
>
> 
