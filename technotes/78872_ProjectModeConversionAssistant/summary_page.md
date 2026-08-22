# Tech Note 22-03: Project Mode Conversion Assistant Component

**Author:** Bryan Yen, Technical Services Engineer, 4D Inc.
**Published:** February 25, 2022 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78872
**Download:** https://kb.4d.com/DLTN/TN/2022/22-03_BinToProjectAssistant.zip

## Proposition
Converting a large legacy binary 4D database to project mode can generate thousands of warning/error messages in a JSON log; this component parses that log into a trackable, filterable UI with direct navigation to problem forms.

## Key Points
- **Conversion log structure**: exporting binary structure to project mode creates a Conversion_*.json file classifying messages as Info, Warning, or Error.
- **Info vs. Warning vs. Error**: Info/Warning are automatic 4D actions to verify; Errors require manual developer fixes (e.g., unsupported form object styles).
- **Component installation**: drop Conversion Manager Component.4dbase into the host's Components folder; launch via the PMCA_ConversionAssistant method.
- **Direct navigation**: double-clicking a message opens the specific form it refers to in Design mode.
- **Progress tracking**: checkbox-based completion tracking, a Show Uncompleted filter, and severity filtering streamline large conversion efforts.
- **Persistent progress**: saves to Conversion_Component_Log.json in Resources (leaving the original conversion log untouched) so work resumes across sessions.

## Featured Technology
- Project mode conversion log (Conversion_*.json)
- 4D component architecture
- Binary-to-project export

## Best Practices Highlighted
1. Always perform a binary-to-project export first to generate the conversion log before using the component.
2. Triage Errors before Warnings, since Errors are the ones that can break application behavior if left unresolved.
3. Use the Show Uncompleted filter to focus on remaining work across long-running, multi-session conversion efforts.

## Context / Positioning
This note is a direct enabler of 4D's strategic push toward project mode as the standard development paradigm (replacing binary Design Mode structures), providing tooling specifically to lower the switching cost for existing customers with large legacy codebases.

## Historical Commentary
**Status:** Still Relevant

The binary-to-project-mode transition itself is now old news — project mode has been 4D's default/recommended mode since v18 and is by far the dominant approach today — but that's exactly why a tool like this remains useful: many organizations are still migrating older applications years later, and this component's core function (parsing the still-stable conversion-log JSON format) should still work on current 4D. This is a support-tooling note whose usefulness is durable specifically because the underlying pain point (legacy binary-to-project conversion) persists for late adopters.
