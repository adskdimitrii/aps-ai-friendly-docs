# geometryDataByElement

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/geometrydatabyelement/

---

Queries

# geometryDataByElement

[](#)

Retrieves geometry data for given element.

**Template for Query:**

```
query GetGeometryDataByElement($elementId: ID!) {
  geometryDataByElement(elementId: $elementId) {
    # GeometryDataByElement Fields
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

| elementId*   [ID!](scalars.md) `non-null` | Element to retrieve Geometry Data from. |
| --- | --- |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [GeometryDataResponse](objects-geometrydataresponse.md) | Represents the response for geometry data requests, including geometry data for elements and download information. |
