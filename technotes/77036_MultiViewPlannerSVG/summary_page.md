# Tech Note 14-07: Build a Multi-View Planner with SVG

**Author:** Herve LE MARCHAND, 4D Developer
**Published:** May 5, 2014 | **Product/Version:** 4D v13.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77036
**Download:** https://kb.4d.com/DLTN/TN/2014/14-07_MultiViewPlannerWithSVG.zip

## Proposition
This note demonstrates how to build a fully interactive, Gantt-chart-style multi-view scheduling planner by directly manipulating a large SVG document through the 4D SVG Component and native 4D language, applying MVC architecture and solving real interactivity problems like collision detection and zoom.

## Key Points
- Interactive SVG editing became practical from 4D v12 onward, since individual element attributes can be changed without rebuilding the entire XML tree (here, ~3000 lines).
- SVG objects are addressed via a unique ID (`SVG_SET_ID`), then manipulated using a CRUD-like mapping onto SVG Component commands: create/delete via `SVG_SET_VISIBILITY`, retrieve via `SVG GET ATTRIBUTE`, update via `SVG SET ATTRIBUTE`.
- The planner's form and methods are structured with an MVC pattern, covering On Load, On Timer, and On Outside Call events.
- Simple collision management prevents scheduled items from improperly overlapping.
- Covering management resolves visual stacking so overlapping items remain accessible/visible.
- A zoomable viewport with an optimally positioned viewbox keeps the planner legible "at all scales."
- SVG gradients are used for visual polish, and keyboard shortcuts are wired up for schedule navigation/editing.

## Featured Technology
- 4D SVG Component (`SVG_SET_ID`, `SVG GET/SET ATTRIBUTE`, `SVG_SET_VISIBILITY`)
- MVC pattern applied to 4D forms/methods
- SVG viewport/viewbox zoom and gradient rendering

## Best Practices Highlighted
1. Address individual SVG elements by unique ID rather than regenerating the whole document on each change.
2. Separate model, view, and controller responsibilities across form events and methods for maintainability.
3. Solve visual overlap (collision/covering) explicitly rather than leaving it to incidental SVG stacking order.

## Context/Positioning
Published as a deep, expert-level technique showcase for 4D v13.5, this note demonstrated how far a developer could push the SVG Component to build genuinely rich, interactive scheduling UI without leaving the native 4D language.

## Historical Commentary
**Status:** Partially superseded

Building a CRUD-style interactive Gantt planner by directly manipulating a large SVG document was an impressively deep technique for its era, and the 4D SVG Component and its commands still function in current 4D. However, developers building rich interactive scheduling/planning UIs today more commonly host a modern JavaScript scheduling/charting library inside a Web Area, or use Qodly Studio's component model, both of which offer far easier styling and richer interactivity than hand-rolled SVG attribute manipulation. The note's MVC architectural discipline for organizing 4D forms and methods remains sound generic advice independent of the rendering technology chosen.
