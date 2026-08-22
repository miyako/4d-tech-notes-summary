# Tech Note 18-21: Power your ORDA queries with query options

**Author:** Xiang Liu, Technical Services Team Member, 4D Inc.
**Published:** December 28, 2018 | **Product/Version:** 4D v17 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78175
**Download:** https://kb.4d.com/DLTN/TN/2018/18-21_ORDAPowerfulQueries.zip

## Proposition
`dataClass.query()`'s query-string syntax was new and somewhat unfamiliar to 4D developers used to classic `QUERY`/`QUERY BY ATTRIBUTE`. This note goes beyond the official documentation to explain the syntax in depth and share hands-on best practices — including some undocumented options — for building accurate, high-performance ORDA queries.

## Key Points
- **Query string anatomy:** `attributePath comparator value {logicalOperator attributePath comparator value}` — attributePath uses dot notation for related classes (e.g. `company.name`), comparators include `=`, `==`, `===`, `#`, `!=`, `<`, `>`, `<=`, `>=`, `%`, `IS`, `IS NOT`, `IN`, `NOT`.
- **vs. QUERY/QUERY BY ATTRIBUTE:** `query()` builds multi-condition, multi-relation-level searches into one readable string, replacing several chained classic commands.
- **Dot-notation relation traversal:** paths like `department.city.name` make deep many-to-one relation queries far more readable than nested classic `QUERY` calls.
- **Multi-value search via IN + collections:** e.g. `ds.People.query("firstName in :1", New collection("Kim";"John"))` replaces manual OR chains.
- **NOT comparator gotcha:** `NOT` reverses an entire parenthesized compound condition — the note derives the logically-equivalent rewritten query (flipping each comparator/operator) to help developers avoid subtle logic mistakes.
- **EXCEPT operator:** documented for excluding matches in joined queries (per table of contents; a further logic-refinement tool alongside NOT).
- **IN with collections to narrow scope, and correct Null-value querying:** dedicated techniques for two common pain points.
- **Ordering results and querySettings:** covers result ordering plus `querySettings` options such as `queryPath` and `queryPlan` for introspecting how a query executes.

## Featured Technology
- `dataClass.query()` and `entitySelection`
- ORDA query-string syntax (attributePath, comparator, value, logicalOperator)
- `NOT` and `EXCEPT` logical operators
- Collections as multi-value `IN` parameters
- `querySettings` (`queryPath`, `queryPlan`)

## Best Practices Highlighted
1. Prefer `query()`'s single-string, dot-notation syntax over chained `QUERY`/`QUERY BY ATTRIBUTE` calls for multi-level relational searches.
2. Carefully reason through `NOT` on compound conditions — rewrite manually to verify the logic before trusting the compact form.
3. Use `IN` with a collection parameter rather than repeated OR clauses when matching multiple possible values.
4. Inspect `queryPath`/`queryPlan` via `querySettings` to understand and optimize how a complex query executes.

## Context / Positioning
Published as ORDA rapidly matured through 4D v17's R-releases, this note reflects the Technical Services team's practice of publishing field-tested, sometimes ahead-of-documentation guidance to help early ORDA adopters avoid common pitfalls in the still-evolving `query()` syntax.

## Historical Commentary
**Status:** Still relevant

`dataClass.query()` and its query-string syntax remain the standard, current way to query ORDA data classes in 4D today; nothing in this note has been deprecated. Options the author flagged as "not currently documented" (like some NOT/EXCEPT behaviors) have generally since been folded into 4D's official ORDA documentation as the feature matured, but the underlying mechanics described here are unchanged.

This is a good example of a 4D Tech Note whose technical content has aged very well — ORDA querying is arguably more central to 4D development in 2026 than it was in 2018, and the comparator/logical-operator semantics, dot-notation attribute paths, and IN/collection usage described here are still exactly how a 4D developer would write ORDA queries today. The main caveat is to double-check current documentation for any newly added comparators or querySettings options introduced in the years since.
