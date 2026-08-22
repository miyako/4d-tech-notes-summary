# Tech Note 07-11: Printing with 4D View

**Author:** Larry Sharpe
**Published:** March 20, 2007 | **Product/Version:** 4D View (for 4D 2004.5) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=45884
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_10-12_(MAR)/07-11_4D_View_Printing.zip

## Overview
Updating his earlier 2002 Tech Note 02-45 ("User Definable Views Using 4D View"), the author adds straightforward "click-and-print" functionality to a 4D View-based output form, letting users print exactly what is displayed on screen rather than relying on 4D's separate Reports engine.

## Key Points
- Reuses most of the original 2002 sample database's code, with `updated 02/15/07` comments marking every change so readers can find the differences.
- Documents an important intervening 4D View change: column sorting is now handled by a dedicated `PV SORT COLUMN` command instead of being bundled into `PV SET COLUMN HEADER`, allowing sort order/column to change independently of header setup.
- Adds a Print List menu item and Print button, both routed through one `xOutput_Print4DView` method that checks whether Alt (Windows) / Option (Mac) is held to pick between two printing implementations.
- `Views_4DV_Print_UserDefined`: hides the row header, then lets the user interactively configure 4D View's native print options and page setup via `PV EXECUTE COMMAND`, optionally previewing on screen instead of printing to paper (useful for saving paper/ink while testing).
- `Views_4DV_Print_CodeDefined`: a larger (~3 page) method that sets font/size/color for printed rows and columns via a new optional third parameter on the existing `x4DView_Fields` method, and automatically computes Portrait vs. Landscape orientation based on column widths to avoid the alignment problems of multi-page-wide printouts.
- Also shows (commented out) how the same logic could target a PDF document instead of a physical printer or preview page, with platform-specific code for Mac vs. Windows.
- Notes that `PV EXECUTE COMMAND`'s printing-options dialog remembers settings for the life of the process, so code-defined defaults and user-adjustable overrides can be combined.

## Featured Technology
- 4D View plug-in
- `PV PRINT`, `PV EXECUTE COMMAND`, `PV SORT COLUMN`, `PV SET AREA PROPERTY`
- Programmatic page orientation/print-preview logic

## Historical Context
4D View was a companion spreadsheet/grid plug-in for 4D, entirely predating 4D View Pro (introduced in 4D v17, 2018) which uses a completely different, modern spreadsheet API. This note's `PV_*` command family and workflow are specific to the legacy plug-in and are not applicable to current 4D View Pro areas, though the underlying goal — giving end users a simple way to print exactly what they see in a data grid — remains a standard requirement addressed differently in modern tooling.

## Historical Commentary
**Status:** Superseded

The legacy 4D View plug-in's `PV_*` printing commands have no direct equivalent in current 4D, having been fully superseded by 4D View Pro (2018+), which provides its own modern printing and export capabilities.
