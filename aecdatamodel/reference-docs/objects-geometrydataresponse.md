# GeometryDataResponse

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/geometrydataresponse/

---

Objects

# GeometryDataResponse

[](#)

Represents the response for geometry data requests, including geometry data for elements and download information.

## [Fields](#fields)

| geometryData   [[GeometryDataOutput]](/en/docs/aecdatamodel/v1/reference/objects/geometrydataoutput) | The geometry data for the requested elements. |
| --- | --- |
| downloadInfo   [[DownloadInfo]](/en/docs/aecdatamodel/v1/reference/objects/downloadinfo) | Information required to download geometry data for the elements from a URL. |

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Query By | [geometryDataByElement](queries-geometrydatabyelement.md) | Retrieves geometry data for given element. |
| Query By | [geometryDataByElements](queries-geometrydatabyelements.md) | Retrieves geometry data for given elements. |
