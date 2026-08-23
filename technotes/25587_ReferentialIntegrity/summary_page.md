# Tech Note: Referential Integrity

- **Asset ID:** 25587
- **Tech Note #:** 02-46
- **Published:** October 31, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Roland Lannuzel
- **Page URL:** https://kb.4d.com/assetid=25587
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_46-50_(OCT)/02-46_Referential_Integrity.hqx

## Overview

Roland Lannuzel explains that 4D only enforces Unique, Mandatory, and relational-deletion constraints at the moment data is created or modified -- not retroactively against existing data, such as records inserted before a field was marked Unique -- and provides four generic, structure-introspecting maintenance methods to audit an entire database for such problems. Each method loops through every table and field using `Count tables`/`Count fields` and property-introspection commands, only acting on fields that have the relevant property set, and logs any violations found into a shared text variable (`◊4D_Log`) rather than raising errors directly, so the methods can be run periodically as maintenance utilities. The Unique-field check offers both a brute-force per-record query approach and a faster `DISTINCT VALUES`-based optimization; the N-to-1 relation ('orphan record') check uses `RELATE MANY SELECTION` combined with `CREATE SET`/`DIFFERENCE` to efficiently isolate unmatched child records instead of checking record by record; and the index-verification method sorts a table both ascending and descending on an indexed field and walks the selection checking that ordering is respected in both directions.

## Key Points

- Establishes the scope: 4D enforces Unique/Mandatory/relational constraints only when data is created or modified, so pre-existing data (e.g. records added before a field became Unique) is never automatically checked -- these four methods exist to audit already-existing data.
- Unique-field check (`_CheckUniqueValues`): loops over every table/field via `Count tables`/`Count fields`/`GET FIELD PROPERTIES`, and for each field with the Unique attribute, queries the table for each record's value (using `SET QUERY DESTINATION(Into variable;...)` to avoid disturbing the current selection) and logs an error whenever more than one match is found; also describes a faster alternative using `DISTINCT VALUES` compared against total record count when the table size permits.
- Mandatory-field check (`_CheckMandatoryFields`): for each field flagged Mandatory via `GET FIELD ENTRY PROPERTIES`, queries for the type-appropriate null value (0, empty string, `!00/00/00!`, etc.) and logs any records found, since a null in a Mandatory field indicates existing data that predates the constraint.
- N-to-1 orphan check (`_CheckLinks`): for every relation discovered via `GET RELATION PROPERTIES`, creates a set of all N-side records, uses `RELATE MANY SELECTION` on the 1-side key field to get the set of N-side records that *do* have a match, then computes `DIFFERENCE` between the two sets to isolate orphans -- far faster than checking record by record -- and reports the offending key values via `DISTINCT VALUES` on the orphan set.
- Index verification (`_CheckIndexes`): for each Indexed field, sorts the table ascending then descending via `ORDER BY` and walks the resulting selection checking that each record's value correctly compares to the previous one in both directions (special-cased for Boolean fields using `Num()` since True/False aren't directly comparable), logging 'Index is corrupted' if any comparison fails; notes the check only detects a corrupted index with certainty, it can't fully prove an index is *not* corrupted.
- Suggests two optimizations applicable across the methods -- loading a full selection into an array when memory allows, or processing it in blocks via `SELECTION RANGE TO ARRAY` -- and recommends running these methods periodically as part of routine database maintenance.

## Featured Technology

- SET QUERY DESTINATION (Into current selection / Into variable)
- DISTINCT VALUES for fast uniqueness checks
- GET FIELD PROPERTIES / GET FIELD ENTRY PROPERTIES / GET RELATION PROPERTIES
- RELATE MANY SELECTION + sets (CREATE SET / DIFFERENCE) for orphan detection
- ORDER BY-based index verification
- Structure introspection via Count tables / Count fields / Table() / Field()

## Historical Commentary

**Status:** still_relevant

Roland Lannuzel (4D S.A.) provides four self-contained, structure-introspecting maintenance methods that check data consistency issues 4D's built-in constraints don't catch on already-existing data: duplicate values in Unique fields, null values in Mandatory fields, orphaned N-side records missing their matching 1-side record (an N-to-1 relation check), and index corruption. Each method loops over `Count tables`/`Count fields` and uses field-property introspection commands, with clever set-based (`CREATE SET`/`DIFFERENCE` combined with `RELATE MANY SELECTION`) and array-based (`DISTINCT VALUES`) optimizations rather than brute-force record-by-record loops. The fundamental referential-integrity concepts and the classic structure-level relations/constraints described here remain fully valid and supported in current 4D; ORDA (introduced in 4D v17+) has since added an additional, more modern object-based way to define and navigate these same relationships, but it complements rather than replaces the classic mechanisms this note relies on.

References to newer/updated information:
- ORDA (introduced in 4D v17+) provides an additional, object-based way to define and navigate relations and referential constraints, alongside the classic structure-level relations and field properties (Unique, Mandatory, Indexed) described in this note
- The specific commands used here -- SET QUERY DESTINATION, DISTINCT VALUES, RELATE MANY SELECTION, GET FIELD PROPERTIES, CREATE SET/DIFFERENCE -- all remain part of current 4D
