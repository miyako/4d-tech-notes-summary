# Tech Note 17-04: Label Wizard 64-bit in 4D

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** February 16, 2017 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77727
**Download:** https://kb.4d.com/DLTN/TN/2017/17-04_LabelWizard64bit.zip

## Proposition
4D's Label Wizard was redesigned for the 64-bit product line with a new, more intuitive UI and additional automation capabilities. This tech note tours the redesigned interface, its backward-compatibility rules with legacy 32-bit ".4lb" label files, and the new options for deploying, generating, and printing labels programmatically and offscreen.

## Key Points
- **Backward compatibility:** Mac-created 32-bit ".4lb" files open in the new wizard on both platforms (with minor dimensional differences); Windows-created 32-bit files cannot be opened at all.
- **Contextual click menus:** new right-click/contextual options are available on the editor canvas, on generic objects, on field objects, and on level objects.
- **Simplified menu and print preview:** the redesigned UI trims the menu structure and adds a print preview capability.
- **Offscreen label creation:** label files (and the underlying `Label.json`) can be generated and populated entirely via code, without opening the Label Wizard UI.
- **Programmatic object creation:** field objects and other object types can be added to a label file via a method, not just interactively.
- **JSON-based access control:** a settings file in JSON format restricts which forms/methods a given table's users can access within the wizard, and can be modified programmatically.
- **Offscreen printing:** labels can be printed unattended, suitable for batch/automated document workflows.

## Featured Technology
- Label Wizard (64-bit)
- `.4lb` legacy label file format
- 4D DOM commands (XML manipulation of legacy labels)
- JSON label/settings files
- Offscreen (headless) label generation and printing

## Best Practices Highlighted
1. Test legacy `.4lb` imports carefully — Windows-origin files require regeneration, not just an open/save round-trip.
2. Use the JSON settings file to restrict end-user access to forms/methods rather than relying on UI-level restrictions alone.

## Context / Positioning
Published in February 2017 for 4D v16, this note reflects the broader 32-bit-to-64-bit transition 4D underwent in that era, well before Project Mode (v17, 2018) and ORDA. The Label Wizard itself is a long-standing, print-focused 4D tool that predates and sits somewhat apart from the ORDA/Write Pro modernization wave, making this note primarily about UI/tooling continuity rather than data-access paradigm shifts.

## Historical Commentary
**Status:** Still relevant

The 64-bit Label Wizard and its JSON-driven, code-accessible label generation remain part of current 4D, so the programmatic techniques described here — generating labels offscreen, manipulating `Label.json`, restricting form/method access — are still largely applicable today.

That said, for teams building more visually complex or dynamic output, 4D Write Pro (introduced around v15–16 and matured over subsequent releases) has become the more common choice for rich document generation, leaving the Label Wizard mostly for its original niche: simple, repetitive label layouts like shipping or price tags. This note is a solid, durable reference for that narrower use case rather than a general document-generation solution.
