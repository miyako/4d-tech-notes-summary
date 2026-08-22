# Tech Note 12-08: Practical Subversion with 4D

**Author:** Josh Fletcher, Technical Account Manager, 4D Inc.
**Published:** April 29, 2012 | **Product/Version:** 4D v13.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76559
**Download:** https://kb.4d.com/DLTN/TN/2012/12-08_PracticalSVN4D.zip

## Proposition
This Tech Note presents the CodeExport component, which macro-drives automatic export of every 4D method to UTF-8 text files, solving the historical problem of tracking changes to binary 4D methods with revision control systems like Subversion.

## Key Points
- Revision control has been a fundamentally unsolved problem for classic 4D databases because methods are stored in binary form.
- CodeExport uses 4D v13's Source Toolkit to export every method as UTF-8 text, suitable for committing to a repository.
- Requires zero configuration or startup code in the host database; driven entirely by Method Editor macro events (open/save/create).
- A background stored procedure ("CodeExport Component Process") checks for changes every second and exports as needed, showing a progress bar for longer operations.
- Exported code lands in a "ce_source" folder (organized by method type/table/form); a separate "ce_data" folder holds independent component metadata for upgradeability.
- Provides macros for Start/Stop Monitor, Resolve Error, Full Reset, and optional Startup Install.
- In client/server deployments, the export process runs on the server.
- CodeExport is interpreted-only; not applicable to compiled databases.

## Featured Technology
- CodeExport component
- 4D v13 Source Toolkit
- Method Editor macros
- Stored procedures (client/server)
- Subversion (SVN) workflow

## Best Practices Highlighted
1. Use macro-driven, zero-configuration components to avoid impacting the host database's behavior.
2. Separate exported source (ce_source) from component metadata (ce_data) so the tool itself can be upgraded independently.
3. Guard for slow operations with progress feedback (adaptive progress bar) rather than blocking silently.

## Context/Positioning
Published in 2012 while 4D databases were still exclusively binary Design Mode structures, this note offered a practical stopgap that let development teams adopt standard revision-control workflows years before 4D natively supported text-based project storage.

## Historical Commentary
CodeExport was a clever workaround for a real limitation of the binary Design Mode era, but that limitation itself has been eliminated: 4D's Project Mode, introduced years later, stores methods, forms, and other structure elements natively as plain text files, making any 4D codebase directly diff-able and version-controllable without an export component. As a result, this Tech Note's specific solution is now obsolete for any project built in Project Mode, though it remains a piece of 4D history illustrating a genuine pain point that shaped later product direction.

**Status:** Obsolete
