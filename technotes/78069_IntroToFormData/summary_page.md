# Tech Note 18-10: Introduction to Form Data

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** June 8, 2018 | **Product/Version:** 4D v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78069
**Download:** https://kb.4d.com/DLTN/TN/2018/18-10_FormData.zip

## Proposition
Explains the new v17 "Form Data" feature — a C_Object variable bound to a form instance via the new FORM command — that lets each running instance of a form (dialog or subform) carry its own reference-typed data without relying on process variables.

## Key Points
- **The new FORM command:** returns/accesses the object bound to the current form context.
- **Updated DIALOG command:** now accepts a formData parameter to pass an object into a dialog when it opens.
- **Reference semantics:** because formData is a C_Object, it is passed by reference, so multiple parts of an application sharing the same object see consistent updates.
- **Solves multi-instance dialog problems:** running the same dialog form concurrently in one process no longer requires manual process-variable management to avoid collisions.
- **Two access styles:** formData properties can be accessed either via code or directly through form objects bound to those properties.
- **Passing data into subforms:** formData can flow from a parent form into a subform, enabling parameter passing without global/process variables.
- **Extending table input forms:** adding a single Object field to a table and binding a subform's formData to it lets a table gain unlimited ad hoc structured attributes without schema changes.

## Featured Technology
- FORM command (new in v17)
- formData (C_Object bound to forms)
- DIALOG command (updated parameter)
- Subforms and Object fields

## Best Practices Highlighted
1. Use formData instead of process variables when a form may run multiple concurrent instances in one process.
2. Bind an Object field to a subform's formData to extend a record's input form with flexible, schema-less data.
3. Prefer accessing formData properties through form objects where possible for clarity, falling back to code access when needed.

## Context / Positioning
This note documents a genuinely new v17-era 4D language feature aimed at reducing process-variable complexity in classic Design Mode form code. It sits squarely in the "classic 4D" era — pre-Project Mode, pre-ORDA-maturity — but the feature itself (object-bound form data) was forward-looking for its time and anticipated 4D's later broader embrace of object notation throughout the language.

## Historical Commentary
**Status:** Still relevant

Form Data (the FORM command and the underlying concept of an object bound to a form instance) is still a current, actively used 4D concept today; it solved a real and persistent pain point (juggling process variables across multiple form instances) and its design has not been superseded by anything newer. The technique of extending a table's input form with a single Object field bound to a subform remains valid practice for adding flexible metadata without altering the base structure.

What has aged is mostly cosmetic: the C_Object declaration style shown would today more commonly be written using typed `var` declarations (introduced in v19+), and later 4D code increasingly favors binding ORDA entities directly into forms alongside or instead of a bare formData object. The core mechanism and its rationale, however, remain accurate and useful for developers working in classic (non-ORDA) form contexts.
