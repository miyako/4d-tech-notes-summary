# Tech Note 24-09: Evaluation Technical-Debt of the 4D Code

**Author:** Thomas SCHLUMBERGER, Technical Services Engineer, 4D SAS.
**Published:** July 25, 2024 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79481
**Download:** https://kb.4d.com/DLTN/TN/2024/24-09_EvaluationTechnicalDebt.zip

## Proposition
Migrating legacy 4D code to 20 LTS/Rx requires understanding the scope of technical debt in the existing codebase, especially when inherited from another team. The Methods_Statistics component automates parsing a host database's code to surface quantifiable metrics — old declaration patterns, deprecated commands, thread-unsafe variables — that guide refactoring priorities.

## Key Points
- **Zero-code installation:** Drop the provided component into the host database's Components folder and restart; two "no code" shared methods appear automatically, requiring no host code changes.
- **Legacy pattern counting:** ______Struct_Stats_Dialog counts C_xxx-style declarations, interprocess variables/arrays, #DECLARE usage, var declarations, and class functions (including singletons since 20 R5) across all project methods.
- **Deprecated command detection with optional auto-fix:** Checking "Count old deprecated commands" reveals a "Replace old possible code" option that can automatically correct and save affected methods.
- **Timestamped JSON report export:** A "Create result file" button generates a more complete JSON summary than the on-screen alert, titled with a timestamp for easy before/after comparison during migration.
- **Sortable method list with export:** ______Struct_Dialog_List builds a list box of all methods sortable by name, last modification date/time, and code size, useful for spotting recently changed or oversized methods.
- **Export to text + CSV:** Selected methods can be exported as timestamped .txt files (unchanged content) plus a summary CSV for spreadsheet analysis.
- **Server-compatible, headless execution:** Both shared methods can run directly on 4D Server without an interface, though the host database must be in interpreted mode (compiled mode triggers a warning).
- **Double-click navigation:** In the sortable list box, double-clicking a method line opens it directly in the Method editor for immediate inspection.

## Featured Technology
- **Methods_Statistics component** — the packaged .4dbase providing code-statistics parsing and reporting.
- **Shared methods (______Struct_Stats_Dialog / ______Struct_Dialog_List / ______Struct_Export_Code)** — "no code" entry points visible via Run/Method.
- **JSON report export** — timestamped structured summary of code statistics for historical comparison.
- **CSV export** — spreadsheet-friendly summary of exported method selections.

## Best Practices Highlighted
1. Generate and retain timestamped JSON reports at each migration milestone to measure progress in reducing legacy patterns.
2. Prioritize refactoring of interprocess variables/arrays first, since they are incompatible with thread-safe, preemptive execution.
3. Run the component's methods directly on 4D Server for large structures to avoid GUI-dependent workflows.

## Context / Positioning
Published as 4D continues encouraging migration from binary-mode, classic-language codebases toward modern project-mode and class-based patterns, this note provides a concrete measurement tool supporting that transition — complementing other contemporaneous notes (e.g., Method Properties Manager, Structure Info Class) focused on developer tooling for large-scale code modernization and maintenance.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
