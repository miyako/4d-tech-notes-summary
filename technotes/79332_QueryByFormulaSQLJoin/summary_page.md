# Tech Note 23-19: QUERY BY FORMULA use SQL Join

**Author:** Abdelhafid Elhour, PS 4D and PS Web/mobile manager, 4D Morocco
**Published:** November 28, 2023 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79332
**Download:** https://kb.4d.com/DLTN/TN/2023/23-19_QueryByFormula_SQLJoin.pdf

## Proposition
Since v11, `QUERY BY FORMULA` gained the ability to use indexes and resolve ambiguous multi-table relationships, but this behavior is gated behind the "QUERY BY FORMULA use SQL Join" compatibility property for older databases. This note shows how to safely enable that property — auditing and adapting the small amount of code that would otherwise change behavior — to unlock more efficient, index-based, single-request joined queries.

## Key Points
- **Disambiguating multi-path relationships:** When two tables are connected through more than one relationship path (e.g., Flight→Line→Airport for both departure and arrival), plain `QUERY` with link syntax can't resolve which path to use, but `QUERY BY FORMULA` can by explicitly stating the join equalities.
- **Formula syntax combines criteria, relations, and conjunctions:** A single formula like `([Airport]IATA_AirportCode="SFO") & ([Flight]UUID_Line=[Line]UUID) & ([Line]UUID_Airport_To=[Airport]UUID)` expresses the search filter and the join paths in one expression joined by `&`.
- **Property default varies by database age:** The property is enabled by default (and not user-modifiable) for databases created from v11.2 onward; older/converted databases must opt in explicitly via Database Properties > Compatibility.
- **Four usage patterns when auditing existing code:** pure 4D-function formulas, 4D-method expressions, and simple field comparisons all behave identically before/after enabling the property; only the fourth pattern — a field used as a static current-record value inside an equality — changes meaning once the property is active.
- **Fix pattern for the risky case:** Extract the field's current value into a local variable (e.g., `$uuid:=[Hotel_Chain]UUID`) before the query so the formula's equality is unambiguously a value comparison, not a join.
- **Verification tools:** `DESCRIBE QUERY EXECUTION(True)` combined with `Get last query plan` (structure) and `Get last query path` (execution stats: records found and timing per join step) let developers confirm exactly how a formula query is being resolved.
- **SET DATABASE PARAMETER selector 49:** Exists to programmatically toggle the behavior, but the note explicitly recommends against relying on it in code — do the actual code migration instead.
- **Client-server efficiency gain:** Replacing a `QUERY`/`RELATE MANY SELECTION` chain with a single `QUERY BY FORMULA` join reduces three client-server round trips (and three sets of modified current selections/records) to just one.

## Featured Technology
- **QUERY BY FORMULA / QUERY SELECTION BY FORMULA:** Core commands whose join-resolution behavior is affected by the compatibility property.
- **QUERY BY FORMULA use SQL Join (compatibility property):** The Database Properties > Compatibility toggle that is the subject of the migration.
- **DESCRIBE QUERY EXECUTION / Get last query plan / Get last query path:** Introspection tools for verifying query execution plans and results.
- **SET DATABASE PARAMETER (selector 49):** Programmatic control over the same behavior, discouraged for production use.

## Best Practices Highlighted
1. Audit all `QUERY BY FORMULA`/`QUERY SELECTION BY FORMULA` usages with the development search tool (including wildcards) before enabling the compatibility property.
2. Extract any field used as a static comparison value into a local variable ahead of the query, rather than relying on ambiguous field-to-field equality once SQL-style joins are enabled.
3. Use `DESCRIBE QUERY EXECUTION` with `Get last query plan`/`Get last query path` to confirm query behavior empirically rather than assuming correctness.
4. Avoid depending on `SET DATABASE PARAMETER` selector 49 in code; complete the actual migration instead of toggling behavior at runtime.

## Context / Positioning
This note is a practical database-modernization guide aimed at long-lived 4D databases carrying legacy compatibility settings forward through conversions. It complements 4D's broader emphasis on efficient client-server querying and reflects the platform's SQL-adjacent query capabilities as an alternative to ORDA-based relationship traversal for teams still working with classic command-based (non-ORDA) queries.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
