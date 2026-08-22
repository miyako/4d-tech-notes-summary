# Tech Note 23-10: Programmatic Implementation of Conditional Formatting in 4D View Pro

**Author:** Shayanna Gatchalian, Technical Services Engineer, 4D Inc.
**Published:** May 22, 2023 | **Product/Version:** 4D View Pro v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79197
**Download:** https://kb.4d.com/DLTN/TN/2023/23-10_ConditionalFormatting.zip

## Proposition
4D View Pro has no dedicated commands for conditional formatting even though the underlying SpreadJS engine fully supports it, leaving developers limited to manual, per-sheet configuration through the ribbon UI. This note shows how to implement conditional formatting programmatically by manipulating the View Pro object directly, unlocking reuse across sheets/workbooks and custom UI scenarios.

## Key Points
- **What conditional formatting is:** dynamic cell styling applied only when a rule's condition is met (e.g., highlighting values below a threshold), distinct from static overall cell styling.
- **Manual limitation:** rules applied via the View Pro ribbon (Styles > Conditional Formats) are tied to a single sheet and can't be reused across sheets or saved outside the VP object.
- **Programmatic benefits:** the same rule(s) can be applied across multiple pages/workbooks, saved externally (variable, record, JSON) for reuse, and driven by custom UI when the ribbon is disabled.
- **VP object structure:** `VP Export to object` surfaces the whole document as a 4D object with `version`, `dateCreation`, `dateModified`, `meta`, and `SpreadJS` properties; `conditionalFormats` lives under `SpreadJS.sheets.<sheet>` and only appears once a rule exists.
- **Rule anatomy:** each rule has a condition ("if"), an optional style, and cell range(s); SpreadJS defines 14 rule types (Cell Value, Formula, Icon Set, Data Bar, Top 10, Duplicate, Unique, etc.) each with its own enumeration constant and required properties.
- **Precedence rules:** overall order in the `rules` collection determines general precedence (last added = highest); for overlapping ranges, an explicit `priority` property on each rule object resolves conflicts.
- **Round-tripping:** after building/modifying the rules collection, `VP Import from object` re-applies it to the live View Pro area; changes remain volatile until the underlying file is saved to disk.
- **Sample database:** demonstrates 16 rule-type implementations, a rule-priority reordering list box, live JSON inspection of the selected rule and full VP object, and a "Create Your Own Rule" skeleton for practice.

## Featured Technology
- **4D View Pro** — the spreadsheet component (built on SpreadJS) whose object model is manipulated for this technique.
- **VP Export to object / VP Import from object** — round-trip commands that expose and reapply the entire View Pro document as a 4D object.
- **SpreadJS conditionalFormats** — the underlying JS library's rule-type enumerations, condition/style/range model, and priority property that 4D's object mirrors.
- **ORDA** — used conceptually to manipulate the object structure and cell ranges programmatically.

## Best Practices Highlighted
1. Study the SpreadJS `ConditionalFormats`/`RuleType` API documentation directly since 4D exposes the same structure with no additional abstraction.
2. Save reusable rule objects outside the View Pro document (JSON, database record) when the same formatting needs to apply across multiple workbooks with the same structure.
3. Always persist the file to disk after `VP Import from object`, since in-memory changes to the VP object are otherwise volatile.

## Context / Positioning
This note reflects 4D View Pro's continued reliance on its SpreadJS foundation and 4D's broader ORDA-object-model strategy: rather than adding new dedicated 4D commands for every SpreadJS feature, 4D empowers developers to manipulate the underlying object structure directly, extending View Pro's capabilities without waiting for native command coverage.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
