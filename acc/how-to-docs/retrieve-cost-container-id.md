# Retrieve a Cost Container ID (deprecated)

Source: https://aps.autodesk.com/en/docs/acc/tutorials/cost/retrieve-cost-container-id/

---

# Retrieve a Cost Container ID (deprecated)

- The workflow described in this tutorial is deprecated and will not be supported after July 30, 2026.

- You need to use the project ID instead of the container ID. To obtain the project ID, use GET projects .

This tutorial demonstrates how to retrieve a BIM 360 cost management container ID for a BIM 360 project. Each BIM 360 project is assigned with a cost container that stores all the cost data for the project. The cost container ID is used to call the BIM 360 cost endpoints. To retrieve the ID, you need to call several Data Management endpoints.

## Before You Begin

- Register an app

- Acquire a 3-legged OAuth token or a 2-legged OAuth token with user impersonation with the data:read scope.

- Verify that you have access to the relevant BIM 360 account and BIM 360 project.

## Step 1: Find the Hub ID

You must first call GET hubs to find the account ID for your BIM 360 account.

Note that the BIM 360 account ID corresponds to a Data Management hub ID. To convert an account ID into a hub ID you need to add a âb.â prefix. For example, an account ID of c8b0c73d-3ae9 translates to a hub ID of b.c8b0c73d-3ae9 .

In this example, assume that the project for which you want the container is part of the âJohnâs Accountâ hub.

### Request

### Response

## Step 2: Find the Container ID for the Project

Use the BIM 360 hub ID that you retrieved in the previous step ( b.cGVyc29uYWw6cGUyOWNjZjMy ) to call GET hubs/:hub_id/projects , and retrieve a list of all the projects in the hub to which the user has access. In this example, we have added a filter to return only details of a specific project âDemo Project.â

### Request

### Response

The response payload includes the container ID ( data.relationships.cost.data.id ). Youâll use this ID in Cost API calls for this project.
