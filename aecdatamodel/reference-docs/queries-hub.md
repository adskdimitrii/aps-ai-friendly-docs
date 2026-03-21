# hub

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/hub/

---

Queries

# hub

[](#)

Retrieves an object representing a hub.

A Hub is a container of projects, shared resources, and users with a common context.

**Template for Query:**

```
query GetHub($hubId: ID!) {
  hub(hubId: $hubId) {
    # Hub Fields
  }
}

```

**Template for Query Variables:**

```
{
  "hubId" : "<SOME-ID-TYPE-SCALAR-VALUE>"
}

```

## [Arguments](#arguments)

| hubId*   [ID!](scalars.md) `non-null` | The ID of the hub to return. |
| --- | --- |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [Hub](objects-hub.md) | Represents a hub. A hub is a container of projects, shared resources, and users with a common context. |

## [Examples](#examples)

### Example 1

Retrieves a hub by ID along with its projects.

**Query:**

```
query GetHub($hubId: ID!) {
  hub(hubId: $hubId) {
    id
    name
    projects {
      results {
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
  "hubId": "b.e4fbd315-2dc5-4026-8ca3-80f09d24ff42"
}

```

**Response:**

```
{
  "data": {
    "hub": {
      "id": "b.e4fbd315-2dc5-4026-8ca3-80f09d24ff42",
      "name": "Revit Nexus",
      "projects": {
        "results": [
          {
            "id": "YWltcHJvan5iLmU0ZmJkMzE1LTJkYzUtNDAyNi04Y2EzLTgwZjA5ZDI0ZmY0Mn5iLjdhZGJmOWZkLWRlYmItNDI5Yy1iZmU1LTMyYTNjMjJjMDY5NQ",
            "name": "AEC Design AIM STG"
          },
          {
            "id": "YWltcHJvan5iLmU0ZmJkMzE1LTJkYzUtNDAyNi04Y2EzLTgwZjA5ZDI0ZmY0Mn5iLjgxY2U0YjkyLWIxNTYtNDE5ZS04MjM1LTNiNzY5M2FhMGY0MA",
            "name": "Extractor-AIM"
          }
        ]
      }
    }
  }
}

```

Show More
