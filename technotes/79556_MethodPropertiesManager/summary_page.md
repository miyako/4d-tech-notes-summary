# Tech Note 24-12: Method Properties Manager

**Author:** Elliott Jensen, Technical Services Engineer, 4D Inc.
**Published:** October 23, 2024 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79556
**Download:** https://kb.4d.com/DLTN/TN/2024/24-12_MethodPropertiesManager.zip

## Proposition
Viewing or editing 4D method properties (like preemptive-capable or web-published status) normally requires selecting methods one at a time via the Explorer or Code Editor, and 4D's existing batch-attribute tool only works cleanly if method names follow a strict naming convention. This component lets developers filter, multi-select, and bulk-edit method properties directly, regardless of naming scheme.

## Key Points
- **Ten method properties, two limited native entry points:** Properties are accessible via right-click "Edit Properties" in the Explorer or a button in the Code Editor, but both require per-method selection.
- **Batch setting of attributes has naming-convention limits:** 4D's native batch tool matches a string prefix/pattern (e.g., "Web@") against method names — ineffective for methods without a consistent naming scheme or with multiple unrelated properties.
- **Filterable method list UI:** The component's left pane lists methods along with a live count matching the current property filter; double-clicking opens the method in the code editor.
- **Multi-select via Shift-click:** Developers can select multiple methods from the filtered list to apply changes to all of them at once.
- **Boolean toggle via Apply/Remove:** Most properties are boolean and are set/cleared using dedicated Apply and Remove buttons on the selected methods.
- **Three-state preemptive property:** Unlike other boolean properties, "preemptive" supports "capable," "incapable," and "indifferent" states, handled specially in the UI.
- **Implementation via hidden method header:** Every .4dm method file begins with a hidden `//%attributes = {}` line (visible only in external editors like VS Code) that the component reads/writes using METHOD GET ATTRIBUTE / METHOD SET ATTRIBUTE.
- **Simple local install:** Requires running locally in interpreted mode; the .4dbase is dropped into a Components folder and launched via the "open_property_manager" method.

## Featured Technology
- **METHOD GET ATTRIBUTE** — command to read a method's stored properties programmatically.
- **METHOD SET ATTRIBUTE** — command to write/update a method's stored properties programmatically.
- **.4dm attribute header** — the hidden `//%attributes = {}` metadata line 4D stores at the top of each method file.
- **Properties Manager Component** — the packaged .4dbase component providing the filter/multi-select/bulk-edit UI.

## Best Practices Highlighted
1. Use the component's filter view to audit all methods sharing a given property (e.g., all preemptive-capable methods) before making sweeping changes.
2. Prefer multi-select bulk editing over one-by-one property edits when refactoring large codebases without consistent naming conventions.

## Context / Positioning
This note reflects 4D's continued attention to developer tooling and productivity around code maintenance — complementing other contemporaneous notes on technical-debt evaluation and structure introspection — by making a previously tedious, per-method task (property auditing/editing) scale to large, real-world codebases via a lightweight, locally installed component.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
