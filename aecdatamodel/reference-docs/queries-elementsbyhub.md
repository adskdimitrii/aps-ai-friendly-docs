# elementsByHub

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/elementsbyhub/

---

Queries

# elementsByHub

[](#)

Retrieves elements from given hub, using additional RSQL filters if provided.

**Template for Query:**

```
query GetElementsByHub($hubId: ID!, $filter: ElementFilterInput, $pagination: PaginationInput) {
  elementsByHub(hubId: $hubId, filter: $filter, pagination: $pagination) {
    # ElementsByHub Fields
  }
}

```

**Template for Query Variables:**

```
{
  "hubId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "filter" : "<SOME-ELEMENTFILTER-INPUT-TYPE-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| hubId*   [ID!](scalars.md) `non-null` | Hub to retrieve elements from. |
| --- | --- |
| filter   [ElementFilterInput](inputs-elementfilterinput.md) | RSQL filter to use for searching elements. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [Elements](objects-elements.md) | Contains a list of Elements returned in response to a query. |

## [Examples](#examples)

### Example 1

Retrieves elements of category ‘Windows’ across elementgroups under a hub by hub ID.

**Query:**

```
query GetElementsByHub($hubId: ID!, $filter: ElementFilterInput, $pagination: PaginationInput) {
  elementsByHub(hubId: $hubId, filter: $filter, pagination: $pagination) {
    pagination {
      pageSize
      cursor
    }
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
  "hubId": "b.e4fbd315-2dc5-4026-8ca3-80f09d24ff42",
  "filter": {
    "query": "property.name.category==Windows and 'property.name.Element Context'==Instance"
  },
  "pagination": {
    "limit": 5
  }
}

```

Show More

**Response:**

```
{
  "data": {
    "elementsByHub": {
      "pagination": {
        "pageSize": 5,
        "cursor": "YWRjdXJzfk5VTEx-QlE9PX41"
      },
      "results": [
        {
          "id": "YWVjZX5FMnRqOFJFOXRsSlRQNU9WVzBiaDZ4X0wyQ35QQllLNWlOb1NsQ283QVpEOVdUM0V3XzEyM2ViN2M",
          "name": "32.10-sparing tbv installaties_1400x600"
        },
        {
          "id": "YWVjZX5FMnRqOFJFOXRsSlRQNU9WVzBiaDZ4X0wyQ35QQllLNWlOb1NsQ283QVpEOVdUM0V3XzEyM2ViN2Q",
          "name": "32.10-sparing tbv installaties_1100x650"
        },
        {
          "id": "YWVjZX5FMnRqOFJFOXRsSlRQNU9WVzBiaDZ4X0wyQ35QQllLNWlOb1NsQ283QVpEOVdUM0V3XzEyM2ViODY",
          "name": "32.10-sparing tbv installaties_500x300"
        },
        {
          "id": "YWVjZX5FMnRqOFJFOXRsSlRQNU9WVzBiaDZ4X0wyQ35QQllLNWlOb1NsQ283QVpEOVdUM0V3XzEyM2ViOGE",
          "name": "32.10-sparing tbv installaties_625x150"
        },
        {
          "id": "YWVjZX5FMnRqOFJFOXRsSlRQNU9WVzBiaDZ4X0wyQ35QQllLNWlOb1NsQ283QVpEOVdUM0V3XzEyM2ViOGM",
          "name": "32.10-sparing tbv installaties_400x150"
        }
      ]
    }
  }
}

```

Show More
