# Tech Note 10-14: Printing in 4D v12

**Author:** Tom Fitch, Technical Services Team Member, 4D Inc.
**Published:** April 29, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76089
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_11-14_(APR)/10-14_4Dv12_Print_Objects.zip

## Proposition
This note introduces 4D v12's new printing commands — OPEN PRINTING FORM and Print object — which give developers object-level control over print jobs (mixing multiple forms and printing individual objects at arbitrary positions) rather than being limited to printing whole static form areas, and demonstrates the technique with a sample company newsletter/sales-report wizard.

## Key Points
- **OPEN PRINTING FORM** loads a project form for printing and can be called repeatedly within a single job to draw content from multiple forms; passing an empty string closes the current printing form.
- **On load/On unload form events** fire on the printing form's method as it is opened/closed, allowing setup/teardown logic scoped to the print job.
- **Print object** prints any individual form object, either at its existing position or at explicit posX/posY/width/height parameters, returning a Boolean indicating whether the object printed entirely.
- **Builds on 4D v11 SQL's OPEN PRINTING JOB/CLOSE PRINTING JOB** commands, which scope a sequence of print calls to a single atomic job on a given printer.
- **Object management commands** (e.g. OBJECT GET BEST SIZE, OBJECT GET COORDINATES) can be used within an opened printing form's context.
- **Sample "Demo" wizard database** walks through printing company letters and sales reports combining dynamic data and static objects.

## Featured Technology
- OPEN PRINTING FORM command
- Print object command
- OPEN PRINTING JOB / CLOSE PRINTING JOB (from 4D v11 SQL)
- Project form On load/On unload form events during printing

## Best Practices Highlighted
1. Scope all related print calls within OPEN PRINTING JOB/CLOSE PRINTING JOB to guarantee atomicity against a target printer.
2. Use On load/On unload form events on printing forms to set up and tear down state cleanly around each form's use in a job.
3. Prefer explicit posX/posY/width/height parameters with Print object when composing dynamic layouts that don't match the form's static object positions.

## Context / Positioning
Published at the start of the 4D v12 cycle, this note announced a headline new capability (object-level print control) and served as the foundation for the more advanced follow-up note "Dynamic Object Printing" (asset #76118).

## Historical Commentary
**Status:** Still Relevant

This note introduces the foundational object-level printing commands added in 4D v12 (OPEN PRINTING FORM and Print object), which for the first time let developers mix content from multiple forms and print individual objects at arbitrary coordinates within one job — a substantial upgrade over the older, form-area-only Print form model.

These commands and the technique remain fully functional in current 4D versions and are still a valid, classic-language approach to programmatic printing, though for building complex, richly formatted documents 4D now recommends 4D Write Pro (introduced v16) and 4D View Pro (introduced v17-18 for tabular/report printing) as higher-level, more maintainable alternatives to manual object-by-object print-job assembly.
