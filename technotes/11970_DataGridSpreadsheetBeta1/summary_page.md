# Tech Note: The DataGrid Spreadsheet - Beta 1

## Overview
- **Technical Note 00-33**
- **Author:** Sebastian Frey, Sextant Technologies, Inc.
- **Published:** July 1, 2000
- **Product/Version:** 4D Calc v6.5
- **Platform:** Mac & Win
- **Content source:** Full PDF text recovered

## Key Points
This Tech Note is the second in Sebastian Frey's series documenting DataGrid Beta 1, an application built to demonstrate and exercise 4D's new Enterprise Data Module (EDM) framework while also serving as a genuinely useful data-administration tool. The note explains that the visible DataGrid Spreadsheet is not a standalone module in its own right but is instead implemented via a special 'non-module' module called APP, which depends on two other modules: GRD ('grid'), intended as an abstraction over whatever grid/spreadsheet tool is plugged in, and CAL, the concrete implementation backed by the 4D Calc plug-in. It candidly notes that this abstraction was imperfect in the Beta 1 release, since 4D Calc was the only grid tool available at the time, leaving GRD tightly (and mutually) dependent on CAL, with the stated hope that future grid tools could be substituted in more cleanly later. It then introduces the grid 'object' as EDM's core conceptual entity for this part of the application, mirroring the model/query object pattern from the EDM architecture note, with properties stored in arrays and accessed via a defined set of getter/setter-style methods. The featured technology is 4D Calc (one of the 4D Productivity Modules) as wrapped by DataGrid's GRD abstraction layer to power its spreadsheet interface.

## Featured Technology
- DataGrid GRD and CAL modules
- 4D Calc grid abstraction
- Enterprise Data Module (EDM)

## Historical Context
This is the second note in Sextant Technologies' DataGrid series, explaining how the DataGrid application's spreadsheet UI was built atop an abstracted 'grid' concept implemented via the GRD module, which at Beta 1 time was tightly coupled to the 4D Calc plug-in (the CAL module) since 4D Calc was the only grid tool available. DataGrid, 4D Calc, and the broader 4D Productivity Modules line are all long defunct, and modern 4D applications requiring spreadsheet-like grids use entirely different, actively-maintained components, so this note is now historical only.

## What's Changed Since
- DataGrid, the Sextant Technologies application this note documents, and 4D Calc, the underlying grid plug-in it depended on, are both long discontinued
- Modern 4D applications needing spreadsheet-like grid interfaces use current, actively maintained grid/list components rather than the GRD/CAL module architecture described here

