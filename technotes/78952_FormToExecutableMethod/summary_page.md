# Tech Note 22-12: Transform a Utility Form into One Executable Method

**Author:** Add Komoncharoensiri, Director of Technical Services, 4D Inc.
**Published:** June 21, 2022 | **Product/Version:** 4D v19 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78952
**Download:** https://kb.4d.com/DLTN/TN/2022/22-12_FormDef2Method.zip

## Proposition
Sharing a reusable utility form between 4D projects normally means copying several separate pieces (form definition, form method, object methods) and keeping them synchronized. This note's macro-driven technique collapses all of that into a single, shareable, self-contained project method.

## Key Points
- **codeText_fromObject(formDefinition) -> codeText** converts a project form's definition object into evaluable 4D code, usable with Open form window/DIALOG — project forms only.
- **meth_mergeObjectFormMethods(tablePointer; formName) -> codeText** consolidates a form's form method and all its object methods into a single method body.
- **A 'Build a form definition code' macro (Macros v2) automates both steps** — selecting the macro and entering a form name produces a ready-to-run method immediately.
- **Parameterless utility forms (e.g. a timer) convert with zero manual wiring**; forms needing input/output (e.g. a custom request dialog) require manually copying parameter-handling code into the generated method.
- **The bundled demo includes several pre-converted, reusable utility dialogs** — a confirm dialog, a date-range chooser, and a multi-item selector — as ready-to-copy examples.
- **Embedded picture content cannot be converted automatically** and must be manually re-pointed to an external file after conversion.

## Featured Technology
- Project mode macros (Macros v2)
- codeText_fromObject
- meth_mergeObjectFormMethods
- Open form window / DIALOG
- Form definition objects

## Best Practices Highlighted
1. Test the original utility form's behavior thoroughly before converting it, since the conversion process assumes the source form/method logic is already correct.
2. For forms taking input/output parameters, first understand the original form's parameter-handling code before splicing it into the macro-generated method.

## Context / Positioning
Published under 4D v19 R (June 2022), this note is a project-mode-era productivity technique that leans on 4D's newer macro system (Macros v2) to solve a packaging/distribution problem that became more pronounced once project mode's file-per-object structure made 'copy the whole form' less of a single drag-and-drop operation than it was under classic binary structure files.

## Historical Commentary
**Status:** still relevant

This is a niche but still-valid technique for anyone needing to package and share a self-contained utility dialog as a single file; nothing about project-mode forms, macros, or the Open form window/DIALOG commands referenced here has been deprecated. It remains a specialized trick rather than a mainstream workflow, and most teams today would more likely share reusable UI via a proper 4D component or shared project rather than a single consolidated method, but the underlying technique described still works as documented.
