# Tech Note 11-30: Partial Data File Verification

**Author:** Jesse Pina, Technical Services Team Member, 4D Inc.
**Published:** December 21, 2011 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76458
**Download:** https://kb.4d.com/DLTN/TN/2011/11-30_PartialDataVerification.zip

## Proposition
This Tech Note explains and demonstrates the VERIFY CURRENT DATA FILE command (introduced in 4D v11 SQL), showing how developers can programmatically verify — and partially repair — a database's data and index files, including targeted partial verification via a callback method.

## Key Points
- 4D v11 SQL incorporated 4D Tools functionality into 4D/4D Server's Maintenance and Security Center (MSC), including graphical verify/repair/compaction tools.
- Two new commands support programmatic verification: VERIFY CURRENT DATA FILE (currently open database) and VERIFY DATA FILE (a data file not currently open, suited to offline maintenance).
- Documents the full VERIFY CURRENT DATA FILE syntax, including optional parameters for restricting scope to specific objects, tables, and fields.
- Explains partial verification — checking only selected objects rather than the whole database — enabled via a callback method.
- Details the callback method's parameters, return value, and provides multiple worked examples plus reasons to use it.
- Demonstration database includes both a "Verify" and a "Rebuild" walkthrough.

## Featured Technology
- VERIFY CURRENT DATA FILE / VERIFY DATA FILE
- Callback method for verification progress and results
- Maintenance and Security Center (MSC)
- Partial verification and partial repair/rebuild

## Best Practices Highlighted
1. Prefer VERIFY CURRENT DATA FILE for convenient, programmatic, partial verification of a live database; use VERIFY DATA FILE for offline maintenance scenarios.
2. Use the callback method to build custom reporting/automation around verification results rather than relying solely on the graphical MSC tools.
3. Scope verification to specific tables/fields when a full-database check is unnecessary, to save time on large databases.

## Context/Positioning
Published in late 2011 for 4D v12, this note extended earlier documentation on 4D v11 SQL's incorporation of 4D Tools, giving developers programmatic control over database maintenance tasks previously only available through graphical tools.

## Historical Commentary
Database integrity verification is a timeless operational need, and VERIFY CURRENT DATA FILE / VERIFY DATA FILE remain part of current 4D versions, functioning essentially as documented here, so this technique is still directly applicable to production 4D applications today. The commands and callback pattern have not been superseded by ORDA or Project mode changes, since data file integrity is an infrastructure-level concern orthogonal to those architectural shifts.

**Status:** Still relevant
