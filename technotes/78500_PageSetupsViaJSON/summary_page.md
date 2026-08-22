# Tech Note 20-10: Saving and Loading Page Setups via JSON

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** June 29, 2020 | **Product/Version:** 4D v18 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78500
**Download:** https://kb.4d.com/DLTN/TN/2020/20-10_Page_Setups_via_JSON.zip

## Proposition
`GET PRINT OPTION` normally only works from inside a form's own method, which is inconvenient for bulk print-setting management. This note shows how to combine the deprecated `_O_PAGE SETUP` command with `GET`/`SET PRINT OPTION` and JSON serialization to save and reload every form's page setup from a project method, menu item, or batch job.

## Key Points
- **`_O_PAGE SETUP(table; formName)`**: deprecated command that lets a project method retrieve a named form's print context without opening the form.
- **`GET PRINT OPTION` / `SET PRINT OPTION`**: read/write individual print settings (paper, orientation, scale, copies, destination, double-sided, spooler name, page range, legacy printing layer).
- **JSON persistence**: settings are packed into an object keyed by print-option constant and serialized with `JSON Stringify`/`TEXT TO DOCUMENT`, stored under `Get 4D folder(Current resources folder)+"pageSetups"`.
- **`saveAllFormPageSetups` / `savePageSetupDefinition`**: iterate `FORM GET NAMES` (project forms) and `GET TABLE TITLES` (table forms) to export one JSON file per form.
- **`loadPageSetup`**: reverses the process with `JSON Parse` and `SET PRINT OPTION`, returning a success flag usable before calling `Print form`.
- **JSON over BLOB**: unlike `Print settings to BLOB`, JSON files are human-readable and editable in any text editor, easing troubleshooting and version control.

## Featured Technology
- `_O_PAGE SETUP` (deprecated 4D command)
- `GET PRINT OPTION` / `SET PRINT OPTION`
- `JSON Stringify` / `JSON Parse`
- `FORM GET NAMES`, `GET TABLE TITLES`, `Print form`

## Best Practices Highlighted
1. Store exported print settings in a dedicated Resources subfolder for portability across environments.
2. Use JSON rather than BLOB storage for anything that may need manual inspection or editing.
3. Check the return code of `loadPageSetup` before printing, mirroring the OK-variable convention.

## Context / Positioning
This note is a workaround/utility note rather than a showcase of new features — it leans on a command already marked deprecated to solve a real gap in 4D's classic form-printing API. It reflects the pragmatic, "make classic tools scriptable" mindset common in tech notes from this era, before 4D's printing/reporting story shifted more heavily toward 4D Write Pro/View Pro document-based output.

## Historical Commentary
**Status:** Partially superseded

`_O_PAGE SETUP` was already deprecated when this note was written and remains so today with no direct 1:1 replacement for retrieving a form's print settings outside its own context — so the note documents a legacy workaround for a legacy command. `GET PRINT OPTION`/`SET PRINT OPTION` and classic form printing are still supported in current 4D versions, so the JSON-persistence technique itself remains technically functional. However, 4D's centre of gravity for document generation and printing has moved toward 4D Write Pro and 4D View Pro (which have their own modern export/print pipelines and JSON-based document models), and toward PDF-focused commands, so a developer starting fresh today would more likely build printing around those rather than classic form page setups. Developers still maintaining older classic-form-based applications may find this technique directly useful.
