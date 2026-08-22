# Tech Note 13-12: Converting Relations to Subtable Fields

**Author:** Milan Adamov, International Technical Support Team Member, 4D SAS.
**Published:** November 5, 2013 | **Product/Version:** 4D v13.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76895
**Download:** https://kb.4d.com/DLTN/TN/2013/13-12_RelationToSubtableField.zip

## Proposition
This note provides an automated code-migration technique for legacy 4D version-2004-era databases whose relations pointed to subtable fields — a pattern that 4D v11 SQL's structure conversion silently drops — restoring equivalent behavior via bulk method-code rewriting.

## Key Points
- In 4D version 2004 or earlier, subtables could have relations (`RELATE ONE` chains) to fields in another table.
- Converting such a structure to 4D v11 SQL+ turns subtables into standard tables (adding a link field) but **drops the relation itself**, silently breaking dependent code.
- The note translates the old `RELATE ONE`/`RELATE ONE` pattern into its logical equivalent (`QUERY` + `QUERY SUBRECORDS`) to make the lost behavior explicit.
- Migration steps: export relation metadata (table/field pairs) from the pre-conversion structure to a tab-delimited file; read it into 4D arrays post-conversion.
- A loop walks every project method, using `Replace string` to substitute the old subtable-relation code with the v11+ equivalent (`QUERY` using `Get subrecord key`, followed by the original `QUERY SELECTION`).
- Rewritten method bodies are committed programmatically with `METHOD SET CODE`, avoiding manual method-by-method, line-by-line edits.
- Notes that subtables were discouraged for a long time, yet many developers kept creating them, making this a necessary tool for real-world v13 migrations.

## Featured Technology
- Legacy 4D subtables (pre-4D v11 SQL structures)
- `RELATE ONE`-based relations to subtable fields
- Automated code migration via `METHOD SET CODE` and `Replace string`
- `QUERY` / `QUERY SUBRECORDS` / `Get subrecord key` as subtable-relation replacements

## Best Practices Highlighted
1. Always audit and export legacy relation metadata before converting an old 4D-2004-era structure forward.
2. Automate bulk method-code migrations with `METHOD SET CODE` rather than manual method-by-method edits when a codebase is large.
3. Explicitly translate implicit relation-based behavior into equivalent explicit `QUERY`-based code so nothing is silently lost during conversion.

## Context/Positioning
Published for 4D v13.3, this note served the practical, unglamorous but necessary need of helping longstanding 4D customers safely bring very old (2004-era or earlier) database structures forward without losing subtable-relation functionality.

## Historical Commentary
**Status:** Obsolete

This note is doubly legacy even for its own era: it exists solely to help migrate database structures created in 4D version 2004 or earlier, which used subtables with relations that 4D v11 SQL's new structure model could not represent. Subtables themselves were a deprecated 4D concept fully removed from the product line years ago, and the classic `RELATE ONE`/`QUERY`-based relation patterns this note's converter manipulates have since been superseded by ORDA's entity-based, dot-notation relational access (4D v16 R5/R6, 2017). Any database still needing this specific conversion would have had to complete it (or be re-platformed) long before ORDA and Project Mode arrived, making the entire migration scenario obsolete today.
