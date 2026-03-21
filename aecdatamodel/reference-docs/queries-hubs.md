# hubs

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/hubs/

---

Queries

# hubs

[](#)

Retrieves all hubs that match the specified criteria.

A Hub is a container of projects, shared resources, and users with a common context.

**Template for Query:**

```
query GetHubs($filter: HubFilterInput, $pagination: PaginationInput) {
  hubs(filter: $filter, pagination: $pagination) {
    # Hubs Fields
  }
}

```

**Template for Query Variables:**

```
{
  "filter" : "<SOME-HUBFILTER-INPUT-TYPE-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| filter   [HubFilterInput](inputs-hubfilterinput.md) | Specifies how to filter a list of hubs. You can filter by name. |
| --- | --- |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [Hubs](objects-hubs.md) | Contains a list of hubs returned in response to a query. A hub is a container of projects, shared resources, and users with a common context. |

## [Examples](#examples)

### Example 1

Retrieves all hubs you have access to.

**Query:**

```
query GetHubs {
  hubs {
    results {
      id
      name
    }
  }
}

```

Show More

**Query Variables:**

```
{
}

```

**Response:**

```
{
  "data": {
    "hubs": {
      "results": [
        {
          "name": "Revit Nexus",
          "id": "b.e4fbd315-2dc5-4026-8ca3-80f09d24ff42"
        },
        {
          "name": "Golden Gate",
          "id": "b.5c07c84c-bbd9-476e-8712-547f74c5b76b"
        }
      ]
    }
  }
}

```

Show More
