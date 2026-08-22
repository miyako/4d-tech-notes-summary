# Tech Note 16-07: CodeTracker Component

**Author:** Charlie Vass, Technical Services Engineer, 4D Inc.
**Published:** June 23, 2016 | **Product/Version:** 4D v15.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77572
**Download:** https://kb.4d.com/DLTN/TN/2016/16-07_CodeTracker_R2.zip

## Proposition
This note presents CodeTracker, a component that exports a 4D binary-mode database's method source code to text files (with progress tracking, validation, and quit-detection) and can diff two exported snapshots to find differences — effectively a DIY substitute for source control in the Design Mode era.

## Key Points
- **Method Export feature:** walks the whole database and writes method source to disk, with an adaptive progress bar and macro-driven automation.
- **Method Name Validation:** checks exported filenames for filesystem compatibility issues.
- **Design Object Access commands:** relies on METHOD GET PATHS and related commands to enumerate and read method code programmatically.
- **Quit Detection:** safely aborts or resumes long-running exports if the user quits mid-process.
- **History Compare:** displays and finds differences between two exported code snapshots — a built-in diff capability.
- **Solo-developer friendly:** explicitly pitched as useful for individuals, not just teams with formal source-control processes.
- **External database support:** can operate against another (external) database structure, not just the host.

## Featured Technology
- Design Object Access commands (METHOD GET PATHS, etc.)
- 4D binary/Design Mode method storage
- Macros for automation
- Custom diffing logic

## Best Practices Highlighted
1. Validate exported filenames against filesystem restrictions before writing.
2. Provide progress feedback and safe-abort handling for long-running structural exports.
3. Regularly export and diff method code as a lightweight substitute for real version control when none is in place.

## Context / Positioning
This Tech Note was published in 2016, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Obsolete

CodeTracker directly addresses a gap that no longer exists in modern 4D: since Project Mode arrived in v17 (2018), every method is natively stored as an individual text file in a Git-friendly folder structure, so diffing and history tracking are handled by standard tools like git rather than a custom export/compare component. For any project still on legacy Design Mode this note remains a useful stopgap, but for current development the recommended path is migrating to Project Mode and using real source control.
