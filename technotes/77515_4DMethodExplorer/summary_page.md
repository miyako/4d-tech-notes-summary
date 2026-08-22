# Tech Note 16-03: 4D Method Explorer

**Author:** Timothy Aaron Penner, Technical Services Engineer, 4D Inc.
**Published:** April 20, 2016 | **Product/Version:** 4D v15.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77515
**Download:** https://kb.4d.com/DLTN/TN/2016/16-03_4DMethodExplorer.zip

## Proposition
This note builds a custom Method Explorer for classic (Design Mode) 4D databases, using the Design Object Access command suite to enable on-the-fly fuzzy filtering, sorting, previewing, and direct execution of project methods from a searchable list window.

## Key Points
- **Design Object Access suite (since v13):** provides programmatic read/write access to method contents and metadata, the foundation for this tool.
- **On-the-fly filtering:** the explorer narrows the method list as the user types any substring of a method's name.
- **Sorting options:** methods can be sorted by modification date/time or alphabetically by name.
- **Method preview and execution:** users can preview source code and run a method directly from the explorer window.
- **Code Object Explorer:** extends the same introspection approach to other design objects beyond project methods.
- **Small utility examples:** counting methods, counting total lines of code, and computing total code size using the same commands.

## Featured Technology
- Design Object Access command suite (4D v13+)
- Custom list/search UI in classic 4D forms
- Method introspection and execution

## Best Practices Highlighted
1. Use Design Object Access commands for introspection rather than manually maintaining method inventories.
2. Provide fuzzy/substring filtering rather than requiring exact method names for large codebases.

## Context / Positioning
This Tech Note was published in 2016, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Partially Superseded

This custom Method Explorer solves a real problem specific to binary/Design-Mode 4D databases, where there is no ordinary file system to browse methods in; once a database migrates to Project Mode (v17+), methods become plain text files in normal folders, so developers can use standard code editors, IDE fuzzy finders, or OS search to locate methods, largely superseding the need for this specific tool, though the Design Object Access commands themselves remain valid and useful for other introspection tasks.
