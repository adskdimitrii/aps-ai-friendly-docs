# projects

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/projects/

---

Queries

# projects

[](#)

Retrieves all projects that match the specified filter criteria from a specified hub.

**Template for Query:**

```
query GetProjects($hubId: ID!, $filter: ProjectFilterInput, $pagination: PaginationInput) {
  projects(hubId: $hubId, filter: $filter, pagination: $pagination) {
    # Projects Fields
  }
}

```

**Template for Query Variables:**

```
{
  "hubId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "filter" : "<SOME-PROJECTFILTER-INPUT-TYPE-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| hubId*   [ID!](scalars.md) `non-null` | The ID of the hub that contains the projects. |
| --- | --- |
| filter   [ProjectFilterInput](inputs-projectfilterinput.md) | Specifies how to filter a list of projects. You can filter by name. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [Projects](objects-projects.md) | Contains a list of projects returned in response to a query. |

## [Examples](#examples)

### Example 1

Retrieves all projects under a hub by hub ID.

**Query:**

```
query GetProjects($hubId: String!) {
  projects(hubId: $hubId) {
    results {
      name
      id
      hub {
        id
        name
      }
    }
  }
}

```

Show More

**Query Variables:**

```
{
  "hubId": "b.5c07c84c-bbd9-476e-8712-547f74c5b76b"
}

```

**Response:**

```
{
  "data": {
    "projects": {
      "results": [
        {
          "id": "YWltcHJvan5iLmU0ZmJkMzE1LTJkYzUtNDAyNi04Y2EzLTgwZjA5ZDI0ZmY0Mn5iLjdhZGJmOWZkLWRlYmItNDI5Yy1iZmU1LTMyYTNjMjJjMDY5NQ",
          "name": "AEC Design AIM STG",
          "hub": {
            "id": "b.e4fbd315-2dc5-4026-8ca3-80f09d24ff42",
            "name": "Revit Nexus"
          }
        },
        {
          "id": "YWltcHJvan5iLmU0ZmJkMzE1LTJkYzUtNDAyNi04Y2EzLTgwZjA5ZDI0ZmY0Mn5iLjgxY2U0YjkyLWIxNTYtNDE5ZS04MjM1LTNiNzY5M2FhMGY0MA",
          "name": "Extractor-AIM",
          "hub": {
            "id": "b.e4fbd315-2dc5-4026-8ca3-80f09d24ff42",
            "name": "Revit Nexus"
          }
        }
      ]
    }
  }
}

```

Show More
