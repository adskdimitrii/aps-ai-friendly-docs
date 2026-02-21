# DataTable

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/UI/DataTable/

---

Autodesk.Viewing.UI

# DataTable

## [new DataTable(dockingPanel)](#new-datatable-dockingpanel)

UI component in LMV that can be added into the DockingPanels to create custom tables

### Parameters

| dockingPanel*   [Autodesk.Viewing.UI.DockingPanel](/en/docs/viewer/v7/reference/UI/DockingPanel/) | Instance of the Docking Panel |
| --- | --- |

* Required

# Methods

## [setData(rowdata, columndata)](#setdata-rowdata-columndata)

Sets the table data

### Parameters

| rowdata*   Array.<Array.<Array>> | The dataset in array of arrays and represents a set of rows |
| --- | --- |
| columndata*   Array | The dataset in array and represents the column data |

* Required

## [destroyTable()](#destroytable)

Destroys the table instance

## [setSortFunction(sortFunc)](#setsortfunction-sortfunc)

API to set the custom sorting function

### Parameters

| sortFunc*   function | custom sort function for the table dataset |
| --- | --- |

* Required

## [getSortFunction()](#getsortfunction)

API to get the custom sorting function

### Returns

| type | description |
| --- | --- |
| function | custom sort function set by the setSortFunction method |

## [restoreDefaultSortFunction()](#restoredefaultsortfunction)

API to set the default sorting function

## [getGroupByColumn(col)](#getgroupbycolumn-col)

Get the group by given column

### Parameters

| col*   number | column index |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Array.<number> | rowGroups - an array of grouped data, where each group contains numbers that represent the row-indices of the original table dataset. |

## [groupByColumn(col)](#groupbycolumn-col)

Group by given column

### Parameters

| col*   number | column index |
| --- | --- |

* Required

## [getAggregate(type, col)](#getaggregate-type-col)

Get aggregation based on the type for the given column

### Parameters

| type*   string | type of aggregation |
| --- | --- |
| col*   number | column index |

* Required

### Returns

| type | description |
| --- | --- |
| string | the final result of the aggregation |

## [aggregate(type, col)](#aggregate-type-col)

Aggregate based on the type for the given column

### Parameters

| type*   string | type of aggregation |
| --- | --- |
| col*   number | column index |

* Required

## [clearAggregates()](#clearaggregates)

Clears all the aggregations
