# distinctPropertyValuesInElementGroupById

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/distinctpropertyvaluesinelementgroupbyid/

---

Queries

# distinctPropertyValuesInElementGroupById

[](#)

Retrieves distinct values in an ElementGroup given a property definition ID.

**Template for Query:**

```
query GetDistinctPropertyValuesInElementGroupById($elementGroupId: ID!, $propertyDefinitionId: ID!, $filter: ElementFilterInput) {
  distinctPropertyValuesInElementGroupById(elementGroupId: $elementGroupId, propertyDefinitionId: $propertyDefinitionId, filter: $filter) {
    # DistinctPropertyValuesInElementGroupById Fields
  }
}

```

**Template for Query Variables:**

```
{
  "elementGroupId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "propertyDefinitionId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "filter" : "<SOME-ELEMENTFILTER-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| elementGroupId*   [ID!](scalars.md) `non-null` | ElementGroup to retrieve distinct values from. |
| --- | --- |
| propertyDefinitionId*   [ID!](scalars.md) `non-null` | definition id of the property to retrieve the distinct values of. |
| filter   [ElementFilterInput](inputs-elementfilterinput.md) | RSQL filter to use for searching elements. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [DistinctPropertyValues](objects-distinctpropertyvalues.md) | Contains a list of DistinctPropertyValue returned in response to a query. |

## [Examples](#examples)

### Example 1

Retrieves all family of doors in an element group

**Query:**

```
query ($elementGroupId: ID!, $propertyDefinitionId: ID!, $filter: ElementFilterInput) {
  distinctPropertyValuesInElementGroupById(elementGroupId: $elementGroupId, propertyDefinitionId: $propertyDefinitionId, filter: $filter) {
    definition {
      id
    }
    values(limit: 200) {
      value,
      count
    }
  }
}

```

Show More

**Query Variables:**

```
{
  "elementGroupId": "YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35GZGhKOWZxZFJSR2QxTXAwNU1RWkVR",
  "propertyDefinitionId": "autodesk.revit.parameter:parameter.elemFamilyName-2.0.0",
  "filter": {
    "query": "property.name.category==Doors"
  }
}

```

**Response:**

```
{
  "data": {
    "distinctPropertyValuesInElementGroupById": {
      "definition": {
        "id": "autodesk.revit.parameter:parameter.elemFamilyName-2.0.0"
      },
      "values": [
        {
          "value": "Door-Passage-Single-Flush",
          "count": 105
        },
        {
          "value": "Door-Passage-Single-Two_Lite",
          "count": 13
        },
        {
          "value": "Door-Opening",
          "count": 9
        },
        {
          "value": "Door-Curtain-Wall-Double-Storefront",
          "count": 6
        },
        {
          "value": "36\" x 84\"",
          "count": 5
        }
      ]
    }
  }
}

```

Show More
