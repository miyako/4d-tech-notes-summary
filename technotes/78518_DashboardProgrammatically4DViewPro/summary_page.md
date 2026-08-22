# Tech Note 20-13: Create a Dashboard Programmatically in 4D View Pro

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** July 27, 2020 | **Product/Version:** 4D View Pro v18 R2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78518
**Download:** https://kb.4d.com/DLTN/TN/2020/20-13_DashboardWith4DVP.zip

## Proposition
4D View Pro is usually associated with spreadsheets and formulas, but it can also serve as a live, real-time visual dashboard. This Tech Note shows a mostly programmatic path — loading live data, adding a chart via the underlying SpreadJS JavaScript API, applying VP styling commands, and stripping away interactive spreadsheet chrome — to turn a VP area into a polished dashboard display.

## Key Points
- **Data loading**: `VP SET VALUE`/`VP SET VALUES` push continuously-updated data into the VP area; consolidate large datasets to a few meaningful data points first.
- **Charts via SpreadJS**: since a VP area is a Web Area running GrapeCity's SpreadJS, charts are added with raw JavaScript through `WA Evaluate JavaScript`, calling `sheet.charts.add()` with name, type, position, size, and data range.
- **Performance wrapping**: SpreadJS modifications are wrapped in `suspendPaint()`/`resumePaint()` to avoid unnecessary repainting during chart creation.
- **Native VP styling**: `VP SET DEFAULT STYLE` sets an overall theme; `VP SET CELL STYLE` overrides specific cells (e.g., a different font).
- **Dashboard priming**: exporting the VP area to an object (`VP Export to object`), toggling nested `spreadJS` properties to hide scrollbars/headers/gridlines and set `isProtected:=True`, then reimporting with `VP IMPORT FROM OBJECT`.
- **Disabling scroll**: `VP SET FROZEN PANES` locks the visible row/column range to prevent user scrolling.
- **Persistence**: the primed dashboard configuration can be exported/imported as a `dashboard.json` file, with live data loaded separately at runtime.

## Featured Technology
- VP SET VALUE / VP SET VALUES
- WA Evaluate JavaScript + SpreadJS (GrapeCity) charts API
- VP SET DEFAULT STYLE / VP SET CELL STYLE
- VP Export to object / VP IMPORT FROM OBJECT
- VP SET FROZEN PANES

## Best Practices Highlighted
1. Consolidate raw data into a few dashboard-relevant summary points before loading it into the VP area, rather than dumping full datasets.
2. Wrap SpreadJS chart-creation JavaScript in `suspendPaint()`/`resumePaint()` to avoid unnecessary rendering overhead.
3. Carefully plan cell layout before adding a chart, to avoid covering data ranges the chart needs to reference.
4. Persist the "primed" dashboard configuration separately from live data so the visual layout can be reused across sessions.

## Context / Positioning
This note showcases 4D View Pro's flexibility beyond its primary spreadsheet use case, part of 4D's broader effort during this period to demonstrate 4D View Pro (and its SpreadJS foundation) as capable of building modern, business-intelligence-style visualizations natively within 4D applications, without needing a separate charting/dashboarding product.

## Historical Commentary
**Status:** Still relevant

4D View Pro, built on GrapeCity's SpreadJS, remains 4D's current and actively developed spreadsheet component (the successor to legacy 4D View), so this note's approach is still applicable today. The technique of reaching past 4D's native VP commands into the underlying SpreadJS JavaScript API via `WA Evaluate JavaScript` — necessary here because charting wasn't (at the time) fully exposed as native VP commands — remains a standard and often still-necessary technique for advanced VP customization; developers should check current 4D documentation to see whether more native charting commands have since been added, but the overall "prime the VP area as a dashboard" pattern (hiding chrome, locking panes, exporting/importing the VP object) remains valid and current practice.
