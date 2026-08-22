# Tech Note 11-16: The 4D v12 Rich Text Area Component

**Author:** Tom Fitch, Technical Services Team Member, 4D Inc.
**Published:** May 20, 2011 | **Product/Version:** 4D v12.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76338
**Download:** https://kb.4d.com/DLTN/TN/2011/11-16_RichTextArea.zip

## Proposition
This Tech Note introduces 4D v12's native rich text support and documents the Rich Text Area component — a sub-form-based rich text editor that gives end users a polished interface for creating and editing styled text saved back to Text/Alpha variables and fields.

## Key Points
- **Native v12 rich text feature:** styled text can now be applied to Text/Alpha form objects and to list box cells.
- **Rich Text Area component:** a sub-form providing a richer, dedicated editing UI beyond plain contextual-menu-driven field styling.
- **Installation:** covers install steps on both Mac OS X and Windows, removing source code post-install, and verifying installation.
- **Form integration:** step-by-step instructions for adding Rich Text Areas to application forms.
- **End-user interaction:** contrasts plain rich-text-enabled fields/variables against the fuller Rich Text Area experience, plus text manipulation capabilities.
- **Data flow:** explains populating and saving text to/from the Rich Text Area, with a sample database demonstrating the whole workflow.

## Featured Technology
- 4D v12 native rich text support (Text/Alpha fields and variables, list box cells)
- Rich Text Area component (sub-form-based rich text editor)
- Component installation and form integration workflow

## Context / Positioning
Published in mid-2011 as 4D v12.1 matured its newly introduced rich text feature, this note gave developers a ready-made, polished UI component so they wouldn't have to build their own rich text editing experience from scratch.

## Historical Commentary
**Status:** Partially Superseded

4D's native rich text support for Text/Alpha fields introduced in v12 is still present in current 4D, but the specific sub-form-based Rich Text Area component described here has been superseded by 4D Write Pro, which provides a far more capable, standards-aligned word-processing area for end-user text editing.

New development needing rich text editing UI would use 4D Write Pro rather than installing and wiring up this legacy component, though the component itself may still technically function in older, unmigrated projects.
