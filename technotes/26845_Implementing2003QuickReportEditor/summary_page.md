# Tech Note: Implementing the 2003 Quick Report Editor

- **Asset ID:** 26845
- **Tech Note #:** 03-10
- **Published:** February 28, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Kent D. Wilbur
- **Page URL:** https://kb.4d.com/assetid=26845
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_06-10_(FEB)/03-10_Implementing_QRE.hqx

## Overview

Kent D. Wilbur, Manager of Information Systems at 4D, Inc., explains how to adapt existing 4D databases to take full advantage of the redesigned Quick Report editor introduced in 4D 2003, which now allows a report to start from any table and follow relations outward, rather than requiring the developer to always begin at the lowest child table (e.g. LineItems) the way the legacy REPORT() command did. Simply swapping in the new QR REPORT command preserves old behavior, but unlocking related-table access, the built-in Quick Report Wizard, and master-table switching requires passing three additional boolean parameters: QR REPORT(pTable->; reportName; True; True; True), enabling cross-table selection, the report Wizard, and searching/redefining the master table respectively. The note then presents a "Special Reports" feature built on top of this: pre-designed Quick Report templates are imported once per originating table via File > Import Report Formats, then re-saved under different master tables (e.g., a report created in Products is reopened, its default table changed, and re-imported under Invoices and Customers), with each variant's BLOB stored in a zFatFile table referenced by a zSpecialReports lookup table keyed by table name and report name — so the same report can be triggered automatically and appropriately regardless of which table the user started from. At print time the selected report's BLOB is written to a temporary document with BLOB TO DOCUMENT (setting Mac creator/type codes "4D06"/"4DSE" so QR REPORT can locate it), and the note flags a subtlety that QR REPORT's built-in dialog turns on AUTOMATIC RELATIONS itself only inside its own On Load handling, so automated (non-dialog) report generation must explicitly call AUTOMATIC RELATIONS(True;True) beforehand.

## Key Points

- 4D 2003's new `QR REPORT` command replaces the legacy `REPORT(table;Char(1))` call, and simply substituting it preserves old single-table behavior, but three additional boolean parameters unlock the new editor's capabilities: `QR REPORT(pTable->;reportName;True;True;True)` enables cross-related-table reporting, the built-in Quick Report Wizard, and the ability to search/redefine the report's master table.
- Unlike the old editor, which forced reports to start at the lowest child table (e.g. LineItems for an Invoices/Products report), the new editor lets a report start at any table (e.g. Invoices) and automatically follow relations — a change that matches how end users actually think about their data.
- A "Special Reports" feature is layered on top: a single report template (e.g. "Category – State") is imported once per table it should run from via File > Import Report Formats, then reopened, its default/master table changed, and re-imported under each additional table, with the resulting BLOBs stored in a `zFatFile` table cross-referenced by a `zSpecialReports` lookup table keyed on process/table name and report name.
- At print time, the `M_SpecialReports` method displays a dialog for the user to pick from the reports available for the current table, looks up the matching BLOB via `zSpecialReports`/`zFatFile`, writes it to disk with `BLOB TO DOCUMENT` (setting Mac creator/type codes `"4D06"`/`"4DSE"` via `SET DOCUMENT CREATOR`/`SET DOCUMENT TYPE` so `QR REPORT` can find it), and then calls `QR REPORT` to launch the editor with that template.
- A key gotcha: `QR REPORT`'s own built-in dialog only turns on `AUTOMATIC RELATIONS(True;True)` inside its own On Load handling, so any automated (dialog-bypassing) report generation must explicitly call `AUTOMATIC RELATIONS(True;True)` beforehand or related-table data will not appear.

## Featured Technology

- QR REPORT command (replacing the legacy REPORT command)
- QR REPORT's related-table/Wizard/master-table boolean parameters
- Report template storage as BLOBs (zSpecialReports / zFatFile tables)
- BLOB TO DOCUMENT + platform-specific creator/type codes for .4qr documents
- AUTOMATIC RELATIONS(True;True) requirement for automated related-table reports
- Per-table "Special Reports" automation pattern across multiple master tables

## Historical Commentary

**Status:** Obsolete

For developers migrating 2002-era databases into 4D 2003, this note is a practical, specific guide to the exact parameter and storage changes needed to benefit from the new Quick Report editor rather than silently keeping the old, more restrictive behavior — a genuinely useful migration note in its time. The QR REPORT command and the general Quick Report engine itself were carried forward and evolved for many years afterward, but 4D's reporting stack has since moved decisively toward the newer 4D Write Pro / Quick Report/Chart replacements and on-the-fly ORDA-based reporting, and the specific BLOB-storage/zFatFile template-sharing pattern shown here is a workaround for limitations (fixed master table per template) that current 4D reporting tools no longer have in the same form.

References to newer/updated information:
- 4D's reporting capabilities have evolved substantially since 2003 (4D Write Pro and later reporting tools), superseding the classic Quick Report editor described here for many modern use cases
- The BLOB-storage workaround for reusing one report template across multiple master tables addressed a limitation of the 2003 Quick Report editor that later 4D versions and reporting tools handle differently
