# elementAtTip

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/elementattip/

---

Queries

# elementAtTip

[](#)

Retrieves element using given ID.

**Template for Query:**

```
query GetElementAtTip($elementId: ID!) {
  elementAtTip(elementId: $elementId) {
    # ElementAtTip Fields
  }
}

```

**Template for Query Variables:**

```
{
  "elementId" : "<SOME-ID-TYPE-SCALAR-VALUE>"
}

```

## [Arguments](#arguments)

| elementId*   [ID!](scalars.md) `non-null` | Element to retrieve. |
| --- | --- |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [Element](objects-element.md) | Represents an element type. |

## [Examples](#examples)

### Example 1

Retrieves an element at tip by element ID along with its properties.

**Query:**

```
query GetElementAtTip($elementId: ID!, $propertiesPagination: PaginationInput) {
  elementAtTip(elementId: $elementId) {
    id
    name
    properties(pagination: $propertiesPagination) {
      results {
        name
        value
      }
    }
  }
}

```

Show More

**Query Variables:**

```
{
  "elementId": "YWVjZX5FMnRqOFJFOXRsSlRQNU9WVzBiaDZ4X0wyQ35QV0hqdllJalM3NmNWbURQTXJFMXZRXzEwMDAwMA",
  "propertiesPagination": {
    "limit": 5
  }
}

```

**Response:**

```
{
  "data": {
    "elementAtTip": {
      "id": "YWVjZX5FMnRqOFJFOXRsSlRQNU9WVzBiaDZ4X0wyQ35QV0hqdllJalM3NmNWbURQTXJFMXZRXzEwMDAwMA",
      "name": "2.5\" x 5\" rectangular (Orange)",
      "properties": {
        "pagination": {
          "pageSize": 5,
          "cursor": "Y3Vyc341fjU"
        },
        "results": [
          {
            "name": "Length",
            "value": 1.2192
          },
          {
            "name": "Design Option",
            "value": "Main Model"
          },
          {
            "name": "Area",
            "value": 0.24032209999999998
          },
          {
            "name": "Volume",
            "value": 0.0098322384
          },
          {
            "name": "Export to IFC",
            "value": "By Type"
          }
        ]
      }
    }
  }
}

```

Show More
