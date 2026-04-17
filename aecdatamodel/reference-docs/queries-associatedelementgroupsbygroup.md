# associatedElementGroupsByGroup

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/associatedelementgroupsbygroup/

---

Queries

# associatedElementGroupsByGroup

[](#)

Returns the associated element group

**Template for Query:**

```
query GetAssociatedElementGroupsByGroup($elementGroupIds: [ID!]!, $pagination: PaginationInput) {
  associatedElementGroupsByGroup(elementGroupIds: $elementGroupIds, pagination: $pagination) {
    # AssociatedElementGroupsByGroup Fields
  }
}

```

**Template for Query Variables:**

```
{
  "elementGroupIds" : "<SOME-[ID!]-TYPE-SCALAR-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| elementGroupIds*   [[ID!]!](undefined/id!) `non-null` | target ElementGroup that we want the associated elementGroups of. |
| --- | --- |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [ElementGroups](objects-elementgroups.md) | Contains a list of ElementGroups returned in response to a query. |

## [Examples](#examples)
