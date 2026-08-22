# Tech Note 12-01: Converting Subtables to Standard Tables

**Author:** Darrell Draper, Technical Services Team Member, 4D Inc.
**Published:** January 6, 2012 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76460
**Download:** https://kb.4d.com/DLTN/TN/2012/12-01_ConvertingSubtables.zip

## Proposition
This Tech Note guides developers through migrating legacy 4D 2004-era subtables to standard related tables, urging proactive migration before deprecated subtable commands are eventually removed from 4D entirely.

## Key Points
- Subtables have not been supported since 4D v11 SQL; older databases get them auto-converted to standard tables with a special compatibility relation on upgrade.
- The compatibility relation and its commands are deprecated: no further bug fixes/improvements, unlike actively developed standard table commands.
- Presents one concrete migration process (acknowledging alternatives exist), covering structure changes, form updates, and fixing queries/commands that relied on subtable relationships.
- Emphasizes minimal end-user impact and flexibility — the guide can be adapted depending on whether a database is still on v2004-era structures or already upgraded to v12.
- Frames migration as strategically important, not just a cleanup task, since deprecated features will eventually be removed.

## Featured Technology
- Subtables (legacy pre-2004 4D feature, deprecated)
- Auto-generated compatibility relation for converted subtables
- Standard table relations
- Structure/form/query migration techniques

## Best Practices Highlighted
1. Migrate away from deprecated features proactively rather than waiting for forced removal.
2. Treat migration guides as adaptable frameworks, adjusting steps to the specific legacy structure encountered.
3. Prioritize minimizing end-user impact when restructuring underlying data relationships.

## Context/Positioning
Published in early 2012 for 4D v12, this note addressed a long-tail migration need for databases whose lineage traced back to 4D 2004 or earlier, helping developers finish a transition 4D had begun years prior with the v11 SQL subtable-to-standard-table conversion.

## Historical Commentary
This note documents the tail end of a migration that was already necessary over a decade ago; any database still requiring this specific subtable conversion would need to have completed it long before modern 4D versions, making the note's direct applicability essentially obsolete today. More broadly, the standard-table relational techniques this note migrates developers toward have themselves been substantially supplemented by ORDA's entity-based data access model, which is now the recommended approach for modeling and querying related data in current 4D applications.

**Status:** Obsolete
