# Tech Note 23-17: Replacing Interprocess Variables

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** September 29, 2023 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79295
**Download:** https://kb.4d.com/DLTN/TN/2023/23-17_ReplaceIPVars.zip

## Proposition
Interprocess variables ("<>" prefixed) are deprecated in 4D because they are not thread-safe, which blocks any method using them from running preemptively — an increasingly important limitation as 4D pushes toward scalable, multi-threaded execution. This note explains why, and provides a menu of thread-safe alternatives along with a systematic migration process.

## Key Points
- **Three variable scopes reviewed:** Local ("$var", method-scoped), process ("var", process-scoped), and interprocess ("<>var", database-wide) variables are demonstrated step-by-step in the debugger to build intuition before discussing replacements.
- **Why interprocess variables are deprecated:** Their global, unsynchronized cross-process accessibility makes them inherently not thread-safe, disqualifying any method touching them from preemptive execution.
- **4D Custom Constants via XLIFF:** Static values can be defined in an XML XLIFF resource file (`<group>`/`<trans-unit>` elements with typed `d4:value` attributes) to appear as named constants in the Explorer window, ideal for replacing static-constant use cases.
- **Shared objects/collections:** `New shared object`/`New shared collection` create thread-safe, reference-passed (pointer-like) items usable across processes; writes require a `Use(...)...End use` block that acts as a mutex, blocking concurrent writers until released.
- **Storage object:** A special, always-available shared object automatically initialized at app startup, acting as a persistent catalog for shared items so they don't need to be explicitly passed as process parameters; items are added/removed via `OB REMOVE` inside `Use...End use`.
- **On-disk files:** For deployment- or user-specific settings, storing values in XML/JSON/text files (mirroring 4D's own `directory.json`/AppData/Application Support usage) avoids recompilation and supports per-site configuration.
- **4D Tables as settings stores:** A single-record table (optionally hidden from REST and, via an underscore-prefixed name, from ORDA auto-completion) offers a modular, no-extra-file alternative for storing configurable values.
- **Migration workflow:** Identify interprocess variables via generated `Compiler_Variables_Inter`/`Compiler_Arrays_Inter` compiler methods or a "Find in design" search for "<>"; determine each variable's actual use (static/dynamic constant vs. data sharing) via reference lookups or regex analysis of exported method text; then replace incrementally, prioritizing frequently executed methods, with backups before automated replacements.

## Featured Technology
- **4D Custom Constants (XLIFF):** XML-based mechanism for defining named, typed constants visible in the Explorer window.
- **New shared object / New shared collection:** Thread-safe, reference-passed object/collection types for cross-process data sharing.
- **Use...End use:** Mutex-like locking construct required to write to shared objects/collections/Storage.
- **Storage object:** Built-in, always-alive shared object acting as a global catalog for shared items.
- **Find in design / METHOD GET CODE:** Tools for locating interprocess variable usages and extracting method source as text for regex-based analysis.

## Best Practices Highlighted
1. Classify each interprocess variable's use (static constant, dynamic constant, or shared data) before choosing a replacement, since the right alternative differs by use case.
2. Always back up the database before performing automated find/replace operations on variable names, to avoid partial-match corruption (e.g., "colorCodeKha" matching inside "colorCodeKhaki").
3. Prioritize replacing interprocess variables in frequently executed, performance-critical methods first rather than attempting a full migration all at once.
4. Use the `Use...End use` locking pattern consistently whenever writing to shared objects/collections or the Storage object to preserve thread safety.

## Context / Positioning
This note is part of 4D's broader modernization push toward ORDA, object notation, and multi-threaded/preemptive execution, treating the elimination of legacy interprocess variables as a prerequisite for applications to benefit from improved scalability and performance in v20-era 4D.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
