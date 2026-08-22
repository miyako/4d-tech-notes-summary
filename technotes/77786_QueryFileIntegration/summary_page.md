# Tech Note 17-09: Query file integration in 4D

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** May 19, 2017 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77786
**Download:** https://kb.4d.com/DLTN/TN/2017/17-09_QueryFileIntegration.zip

## Proposition
This Tech Note documents the JSON schema of 4D's classic Query Editor export files (available since v14) and builds a custom component to parse, display, and execute those saved queries programmatically using PROCESS 4D TAGS, without needing to open the Query Editor UI.

## Key Points
- **v14 JSON export:** the Query Editor can export saved queries in a readable, structured JSON format.
- **Detailed schema breakdown:** covers table/field numbers, criteria, line operators, and type-specific box configurations (text, number, date, time, boolean, blob, picture).
- **PROCESS 4D TAGS:** used to reconstruct and execute query commands from the parsed JSON.
- **Custom components:** OF_Execute_Query, OF_Display_Readable_Query, and OF_Display_4D_Code_Query for running, human-readably displaying, or code-displaying a query.
- **Demo database:** shows loading query files into a list box tab, adding new queries, and modifying/re-executing existing ones.
- **Motivation:** removes the need to reopen the Query Editor UI just to reuse or inspect a saved query.

## Featured Technology
- Classic Query Editor JSON export format
- PROCESS 4D TAGS command
- Custom 4D components (OF_Execute_Query family)
- List box-based query management UI

## Best Practices Highlighted
1. Parse and validate query file JSON structure before attempting to execute it programmatically.
2. Separate query execution, human-readable display, and code-display concerns into distinct components.
3. Guard against running a stale or malformed query file without user review.

## Context / Positioning
Published in 2017 for classic 4D v16, this note is deeply tied to the pre-ORDA Query Editor and PROCESS 4D TAGS mechanism, reflecting a data-access approach common before ORDA's dataclass query methods became the modern standard.

## Historical Commentary
**Status:** Partially superseded

The classic Query Editor and its JSON export format still exist in current 4D for backward compatibility, so this note's schema documentation remains technically accurate. However, ORDA's query()/queryByFormula() methods on dataclasses and entity selections have become the preferred, more modern way to build and execute dynamic queries in code, making the PROCESS 4D TAGS-based reconstruction technique shown here a legacy pattern that most new development would no longer choose.
