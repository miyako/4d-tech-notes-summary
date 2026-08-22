# Tech Note 10-18: Dynamic Object Printing

**Author:** Tom Fitch, Technical Services Team Member, 4D Inc.
**Published:** June 16, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76118
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_17-20_(JUN)/10-18_Dynamic_Object_Printing.zip

## Proposition
This note demonstrates a "revolutionary" (for its era) printing technique in 4D v12 that lets developers drive an entire complex print job — such as a full company catalog — from a single, minimal printing form, by reassigning object values/properties and repositioning objects programmatically at print time via the new Print object command.

## Key Points
- **Builds on** the companion Tech Note "Printing in 4D v12" (asset #76089), going deeper into object-level print control.
- **Print object command** allows printing any form object individually, at its existing position or an explicit position/size passed as parameters.
- **One object, many roles:** the same handful of form objects are reused repeatedly within a job, each time reassigned a different value and role (e.g. catalog cover text, then genre page headers).
- **Object property management:** value assignment, positioning, and other properties are all set programmatically immediately before each `Print object` call.
- **Sample database** demonstrates generating an entire company catalog (cover + genre pages) from data, using this reuse pattern.
- **Granular control** surpasses the older, form-area-based Print form approach used in prior 4D versions.

## Featured Technology
- Print object command
- OPEN PRINTING FORM / OPEN PRINTING JOB / CLOSE PRINTING JOB
- Dynamic reuse of a single form object for multiple print roles
- Programmatic object property assignment at print time (position, size, value)

## Best Practices Highlighted
1. Design print forms around a minimal, reusable set of generic objects rather than one object per possible printed element.
2. Set object properties (value, position) immediately before each `Print object` call to control exactly what is rendered.
3. Separate structural print-job control (`OPEN PRINTING JOB`/`FORM`, `CLOSE PRINTING JOB`) from the per-object rendering logic.

## Context / Positioning
Published as a deep-dive follow-up shortly after 4D v12's new object-based printing commands debuted, aimed at developers who needed to generate large, dynamically laid-out documents like catalogs without a form per layout.

## Historical Commentary
**Status:** Still Relevant

This note showcased 4D v12's then-new object-level printing model (`OPEN PRINTING FORM` plus `Print object`), which let developers reuse a handful of form objects to render arbitrarily complex, data-driven documents like catalogs — a genuinely powerful and still-functional classic-language technique that continues to work in current 4D versions.

For new development, however, 4D now recommends 4D Write Pro (introduced v16) for rich document generation, and 4D View Pro (introduced v17-18) for complex tabular reports, since these offer higher-level, more maintainable document composition than object-by-object print-form manipulation.
