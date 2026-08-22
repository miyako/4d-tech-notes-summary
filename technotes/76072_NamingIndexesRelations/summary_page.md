# Tech Note 10-10: Naming Indexes and Relations in 4D v11 SQL

**Author:** Atanas Atanassov, Technical Services Team Member, 4D Inc.
**Published:** April 2, 2010 | **Product/Version:** 4D v11.6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76072
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_07-11_(MAR)/10-10_Naming_Indexes_and_Relations.pdf

## Proposition
This note recommends that developers apply a disciplined, SQL-style naming convention to indexes and table relations in 4D — rather than relying on 4D's auto-generated UUIDs — so structure objects are easier to find, read, audit, and query via the newly introduced System Tables.

## Key Points
- Common SQL prefix conventions: **Pkc** (primary key, clustered), **Pknc** (primary key, non-clustered), **Ncu** (non-clustered unique), **Nc** (non-clustered).
- The **Structure Editor** provides search and an information bar, but naming discipline makes finding specific indexes/relations far faster in complex structures.
- **System Tables** (new in 4D v11 SQL) let code query index/relation metadata by name — enabling lookups of index types, related tables, and more.
- Naming can support **structure auditing**: e.g., checking for lost indexes after a recovery, or index types that no longer reflect field data.
- No single naming standard is mandated — consistency of whatever convention is chosen matters more than the specific scheme.
- Three worked examples demonstrate applying the naming approach to sample structures.

## Featured Technology
- 4D v11 SQL System Tables
- Index/relation naming conventions (SQL-style prefixes: Pkc, Pknc, Ncu, Nc)
- Structure Editor search tools

## Best Practices Highlighted
1. Give indexes and relations descriptive, SQL-compliant names instead of relying on 4D's auto-generated UUIDs.
2. Pick one naming convention and apply it consistently across the entire structure.
3. Use System Tables queries against named indexes/relations as a structure-auditing technique (e.g., detecting corruption after recovery).

## Context / Positioning
Published as 4D v11 SQL's System Tables matured, extending general database-naming discipline (already common for tables/fields) to indexes and relations to take full advantage of the new metadata-querying capability.

## Historical Commentary
**Status:** Partially Superseded

This note recommends applying disciplined, SQL-style naming conventions to indexes and table relations in 4D's Design-mode Structure Editor, using the newly introduced System Tables to query and audit index/relation metadata. The general principle — descriptive, consistent naming of database structure objects — remains genuinely timeless good practice today.

However, the specific mechanism (the binary-file Design-mode Structure Editor and its UUID-based index/relation naming) is tied to the classic structure model that Project mode (introduced 4D v17, 2018) reorganizes into plain-text, version-controllable files, and ORDA's entity-based data access reduces day-to-day reliance on raw relation/index names for navigating data.
