# distinctPropertyValuesInElementGroupByName

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/distinctpropertyvaluesinelementgroupbyname/

---

Queries

# distinctPropertyValuesInElementGroupByName

[](#)

Retrieves distinct values in an ElementGroup given a property name.

**Template for Query:**

```
query GetDistinctPropertyValuesInElementGroupByName($elementGroupId: ID!, $name: String!, $filter: ElementFilterInput, $pagination: PaginationInput) {
  distinctPropertyValuesInElementGroupByName(elementGroupId: $elementGroupId, name: $name, filter: $filter, pagination: $pagination) {
    # DistinctPropertyValuesInElementGroupByName Fields
  }
}

```

**Template for Query Variables:**

```
{
  "elementGroupId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "name" : "<SOME-STRING-TYPE-SCALAR-VALUE>",
  "filter" : "<SOME-ELEMENTFILTER-INPUT-TYPE-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| elementGroupId*   [ID!](scalars.md) `non-null` | ElementGroup to retrieve distinct values from. |
| --- | --- |
| name*   [String!](scalars.md) `non-null` | name of the property to retrieve the distinct values of. |
| filter   [ElementFilterInput](inputs-elementfilterinput.md) | RSQL filter to use for searching elements. |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [DistinctPropertyValuesCollection](objects-distinctpropertyvaluescollection.md) | A collection of distinct properties matching the name given. |

## [Examples](#examples)

### Example 1

Retrieves all distinct structural materials used in walls

**Query:**

```
query ($elementGroupId: ID!, $name: String!, $filter: ElementFilterInput, $pagination: PaginationInput) {
  distinctPropertyValuesInElementGroupByName(elementGroupId: $elementGroupId, name: $name, filter: $filter, pagination: $pagination) {
    results {
      definition {
        id
      }
      values(limit: 5) {
        value
        count
      }
    }
  }
}

```

Show More

**Query Variables:**

```
{
  "elementGroupId": "YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35GZGhKOWZxZFJSR2QxTXAwNU1RWkVR",
  "name": "Structural Material",
  "filter": {
    "query": "property.name.category==Walls"
  }
}

```

**Response:**

```
{
  "data": {
    "distinctPropertyValuesInElementGroupByName": {
      "results": [
        {
          "definition": {
            "id": "autodesk.revit.parameter:structuralMaterialParam-5.0.0"
          },
          "values": [
            {
              "value": "Concrete Masonry Units",
              "count": 4
            },
            {
              "value": "Metal Stud Layer",
              "count": 21
            },
            {
              "value": "Metal Furring",
              "count": 5
            },
            {
              "value": "Concrete, Cast-in-Place gray",
              "count": 5
            }
          ]
        }
      ]
    }
  },
}

```

Show More
