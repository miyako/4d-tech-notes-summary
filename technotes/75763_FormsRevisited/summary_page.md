# Tech Note 09-20: Forms Revisited

**Author:** Luis Pineiros, Technical Services Team Member, 4D Inc.
**Published:** May 21, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75763
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_18-21_(MAY)/09-20_Forms_Revisited.zip

## Proposition
This note is a broad, practical survey of 4D form design fundamentals and best practices — form types, elements, sizing, inheritance, multi-page layouts, style sheets, resizing, and dynamic show/hide — intended to help developers plan new applications or improve existing ones.

## Key Points
- **Form types covered:** Input/Output forms (and hybrid list+detail combined forms), **Project Forms** (new in 4D v11 SQL — table-independent, ideal for dialogs/components, but no list forms and not usable in label editor or import/export editors), Form Wizard forms (a fast starting point, not meant for direct end-user use), and User Forms (limited end-user customization, no code/variable/field additions).
- **Form elements and properties** are reviewed generally as building blocks for any form.
- **Ideal form sizing** guidance is provided to balance information density against usability.
- **Inherited forms** are recommended to maintain consistency across an application's many forms.
- **Multi-page forms and style sheets** help organize complex interfaces and enforce consistent formatting.
- **Resizing forms and dynamically hiding/showing elements** are covered as techniques to maximize the user experience across different contexts.

## Featured Technology
- 4D classic Form editor (Input/Output/Project/Form Wizard/User Forms)
- Project Forms (introduced in 4D v11 SQL)
- Inherited forms
- Multi-page forms and style sheets
- Dynamic form resizing / element show-hide

## Best Practices Highlighted
1. Use Project Forms instead of dummy tables when you only need a dialog or component interface with no data table attached.
2. Build inherited forms to enforce visual and behavioral consistency rather than duplicating layout across many forms.
3. Use the Form Wizard only as a starting point, not as the final end-user-facing form, to avoid losing 4D v11 SQL's richer form features.

## Context / Positioning
Published as a foundational, evergreen-style reference rather than a single-feature deep dive, this note consolidated form design guidance — including the then-new Project Forms concept — for both new and experienced 4D developers.

## Historical Commentary
**Status:** Still Relevant

This note surveyed 4D's classic Design-mode form types and best practices — including Project Forms, newly introduced in v11 SQL as table-independent forms — along with inherited forms, multi-page forms, style sheets, and dynamic resizing. These classic binary-structure forms remain fully supported and are still how most existing 4D applications are built, so the concepts and guidance here are largely current.

4D has since introduced Project mode (storing forms as JSON text files rather than binary structure objects), making forms version-controllable and diffable — a storage-model change rather than a conceptual one, since the form types, inheritance, and style sheet concepts described here carry over largely unchanged.
