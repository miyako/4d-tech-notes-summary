# Tech Note 16-20: Pivot Tables and Pivot Charts in 4D

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** November 8, 2016 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77677
**Download:** https://kb.4d.com/DLTN/TN/2016/16-20_PivotTablesAndCharts.zip

## Proposition
A pivot table summarizes large flat datasets into aggregated, easy-to-read views, and a pivot chart provides a matching visual representation. This tech note introduces 4D v16 64-bit's native pivot table/chart objects, explains the concept using a familiar Excel comparison, and shows how to design and expose the feature to end users in a 4D application.

## Key Points
- **Core concept:** pivot tables add a third "value/aggregation" axis on top of the traditional row/column flat-table view, surfacing patterns not visible in raw record lists.
- **Excel analogy:** the note walks through a familiar Excel pivot table example (clothing sales data) before mapping the same idea onto 4D.
- **Pivot charts:** generated from the same underlying configuration as a pivot table, making trends (e.g., regional/gender sales performance) visually obvious.
- **Design-time editor:** the Pivot Table/Chart Design Editor lets developers define available fields, categories, and default aggregations.
- **Runtime end-user interface:** users can interactively pick rows, columns, filters, and value aggregations to build their own pivot views.
- **Output design:** covers rendering flow from user selections through to the final table/chart output.
- **Sample database:** demonstrates the feature with both pre-built tables and a newly added custom table.

## Featured Technology
- 4D v16 64-bit native pivot table object
- 4D v16 64-bit native pivot chart object
- Pivot Table/Chart Design Editor

## Best Practices Highlighted
1. Expose pivot configuration to end users rather than hard-coding fixed report layouts, to reduce developer support burden for ad hoc reporting requests.
2. Pair pivot tables with pivot charts using the same configuration so users can toggle between numeric and visual views of the same summary.

## Context / Positioning
Published November 2016 for 4D v16 64-bit, this note documents a genuinely native, still-current 4D feature rather than a since-discontinued subsystem, distinguishing it from many of its 4D Mobile/Wakanda-era peers. It reflects the classic Design Mode era of 4D (pre-Project Mode, pre-ORDA) but describes UI/reporting functionality largely orthogonal to those later architectural shifts.

## Historical Commentary
**Status:** Still relevant

4D's native pivot table and pivot chart objects introduced around v16 have remained part of the product line in subsequent releases, and the design/runtime workflow described here is still broadly applicable to current 4D versions.

Since 2016, 4D has continued to refine listbox and charting capabilities, and teams building richer document-style reports increasingly also use 4D Write Pro for combined narrative-plus-data output, or export summarized data to dedicated BI tools for more advanced analytics. But for the straightforward end-user pivot use case this note describes, the guidance remains a solid, largely current reference.
