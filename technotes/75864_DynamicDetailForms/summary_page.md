# Tech Note 09-31: Dynamic Detail Forms

**Author:** Tom Fitch, Technical Services Team Member, 4D Inc.
**Published:** August 6, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75864
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_31-35_(AUG)/09-31_Dynamic_Detail_Forms.zip

## Proposition
This Tech Note provides a component and technique for generating record detail/entry forms "on the fly" from table metadata — necessary for 4D v11 SQL applications that let users create their own custom tables — by rendering an auto-built HTML form inside a 4D Web Area and exchanging data with JavaScript.

## Key Points
- Targets the problem of giving end-users a usable input form for tables they created themselves at runtime (enabled by 4D v11 SQL's ability to alter structure via SQL).
- The component reads table/field metadata via 4D commands, then dynamically builds an HTML form (with a `ddf.css` stylesheet) using `4DVAR`/`4DSCRIPT` tags, displayed in a 4D Web Area.
- Two usage modes: the turnkey `DDF_runForm(->[Table])` call for an out-of-the-box window, or eight shared methods (`DDF_onload`, `DDF_cleanup`, `DDF_firstRecord`, `DDF_previousRecord`, `DDF_nextRecord`, `DDF_lastRecord`, `DDF_deleteRecord`, `DDF_saveRecord`) for custom forms.
- Field values are read out of the HTML/JavaScript layer into 4D method code using `WA EXECUTE JAVASCRIPT FUNCTION`, which invokes a named JS function inside the Web Area and returns its result as text.
- Field-type-aware validation and saving logic (shown in detail for Picture fields via `READ PICTURE FILE`) checks each field's value before calling `SAVE RECORD`; invalid values trigger an Alert and abort the save.
- On load, the component checks record-lock status and disables Save/Delete buttons if the record is locked by another process.

## Featured Technology
- 4D v11 SQL Web Area
- `WA EXECUTE JAVASCRIPT FUNCTION` command
- HTML forms with `4DVAR` / `4DSCRIPT` tags
- Dynamically generated HTML detail forms from table/field metadata
- Component-based shared methods (`DDF_onload`, `DDF_saveRecord`, etc.)

## Best Practices Highlighted
1. Separate a turnkey "just works" entry point (`DDF_runForm`) from lower-level shared methods for developers who need a fully custom UI.
2. Check record-lock status on load and disable destructive actions (Save/Delete) rather than letting a save silently fail or conflict.
3. Validate each field's input value before committing any changes, aborting the whole save if any field fails validation.

## Context/Positioning
Published as a companion to 4D's other Web Area technical notes of the era (e.g. "Mashups with 4D v11 SQL Web Area," "Collapsible Lists with Web Area"), showcasing what the Web Area + `WA EXECUTE JAVASCRIPT FUNCTION` combination made possible for building dynamic, metadata-driven UI in 4D v11 SQL.

## Historical Commentary
**Status:** Obsolete

This note builds dynamic record-entry forms by generating raw HTML/CSS/JavaScript on the fly and rendering it inside a classic 4D Web Area, using `WA EXECUTE JAVASCRIPT FUNCTION` to shuttle field values between JavaScript and 4D method code — a workaround necessitated by the lack of any native dynamic-form or metadata-driven UI layer in 4D v11.

That whole approach is functionally obsolete today: ORDA (4D v16 R5+, 2017) provides native dataclass/attribute introspection instead of manual `Field()`/`Table()` pointer walking, and 4D's form technology has matured well beyond needing to host a hand-authored HTML mini-application inside a Web Area to achieve dynamic, metadata-driven data entry.
