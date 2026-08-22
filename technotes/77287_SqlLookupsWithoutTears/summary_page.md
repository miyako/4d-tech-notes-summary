# Tech Note 15-09: SQL Lookups without Tears

**Author:** David Adams (3rd Party Tech Note)
**Published:** May 8, 2015 | **Product/Version:** 4D v14.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77287
**Download:** https://kb.4d.com/DLTN/TN/2015/15-09_SQLLookup.zip

## Proposition
4D's embedded SQL is a convenient way to look up a single field value without disturbing the current record or selection, but hardcoded SQL text silently breaks when tables or fields are renamed, deleted, or retyped. This note presents a "Named SQL Lookup" framework that declares lookups once, by name, with built-in validation to catch structural drift before deployment.

## Key Points
- **The core problem:** raw SQL SELECT lookups referencing table/field names as literals can break silently after schema changes, with no compile-time warning.
- **Named lookup declarations:** each lookup is declared with a lookup field pointer, result field pointer, and a "magic string" describing expected field-pair types (e.g. `LongFromText`, `BoolFromLong`).
- **Validation tooling:** a review screen lists all declared lookups with their tables, fields, and flags validation errors — such as unsupported result types or since-retyped fields — surfacing problems during development.
- **Visual builder dialog:** a "Named Lookup Builder" UI helps construct lookup declarations without hand-writing magic strings.
- **Custom constants recommended:** suggests using the free 4D Pop tool to generate readable constants instead of raw magic strings, while noting constants are less portable between systems.
- **Design rationale section:** explains stylistic choices like storing lookup definitions in arrays and splitting logic into many small routines.
- **Reused foundation:** the sample database later becomes the base for the related error-logging note, TN 15-19.

## Featured Technology
- 4D embedded SQL (`Begin SQL` / `End SQL`)
- Custom Named SQL Lookup framework (declarations, validation, builder dialog)
- 4D Pop (free custom-constants editor tool)

## Best Practices Highlighted
1. Declare lookups by name with explicit expected field types rather than embedding raw SQL literals scattered through code.
2. Validate lookup declarations against the live database structure before deployment to catch renamed/retyped fields early.
3. Prefer readable custom constants over raw "magic strings" for lookup type declarations, using tooling like 4D Pop to generate them.

## Context / Positioning
This is a classic Design Mode-era (v14.x, 2015) utility/methodology note focused on making 4D's native SQL support safer to use in day-to-day application code, predating ORDA's structurally validated entity/attribute query model and Project Mode's text-based, more refactor-friendly codebase.

## Historical Commentary
**Status:** Still relevant

4D's embedded SQL (`Begin SQL`/`End SQL`) remains a supported feature today, so the named-lookup wrapper technique described here is still directly usable code. That said, ORDA's entity selections and attribute-based queries (introduced starting v16 R5/R6 in 2017) offer many of the same lookup use cases with structural safety built into the platform itself, reducing the need for hand-rolled validation tooling like the one this note builds — a good example of a clever workaround note whose underlying problem the platform later addressed more directly.
