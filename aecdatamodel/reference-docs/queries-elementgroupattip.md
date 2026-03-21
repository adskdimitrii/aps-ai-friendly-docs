# elementGroupAtTip

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/elementgroupattip/

---

Queries

# elementGroupAtTip

[](#)

Retrieves latest elementGroup data based on given ID.

**Template for Query:**

```
query GetElementGroupAtTip($elementGroupId: ID!) {
  elementGroupAtTip(elementGroupId: $elementGroupId) {
    # ElementGroupAtTip Fields
  }
}

```

**Template for Query Variables:**

```
{
  "elementGroupId" : "<SOME-ID-TYPE-SCALAR-VALUE>"
}

```

## [Arguments](#arguments)

| elementGroupId*   [ID!](scalars.md) `non-null` | The ID of the elementGroup. |
| --- | --- |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [ElementGroup](objects-elementgroup.md) | Represents a Revit model. |

## [Examples](#examples)
