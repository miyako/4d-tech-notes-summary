# Tech Note 15-19: Improving Program Quality with Custom Error Logging

**Author:** David Adams (3rd Party Tech Note)
**Published:** October 27, 2015 | **Product/Version:** 4D v14.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77396
**Download:** https://kb.4d.com/DLTN/TN/2015/15-19_ErrorLogging.zip

## Proposition
Programmers often "look for their keys under the streetlight" — debugging the easy-to-see area instead of the actual problem. This note proposes a disciplined error-handling architecture (Define / Catch / Record / Analyze) that captures rich, structured error context proactively so real problems are easier to find later, whether during development or in production.

## Key Points
- **Four-part architecture:** Define errors statically as data → Catch them at precondition checks, execution failures, or via `ON ERR CALL` → Record with contextual detail → Analyze later via search/summarize.
- **Errors as data, not code:** recommends storing error definitions as records/JSON rather than scattering ad hoc alerts, enabling severity, source, and grouping metadata per error.
- **Named errors over numeric codes:** strongly argues for descriptive, hierarchical error names (e.g. `Account_MergeFromAccountDoesNotExist`) that are self-documenting in logs versus opaque numbers.
- **Why not 4D constants:** explains practical reasons (31-char label limit, poor portability across modules) for using a custom data structure instead of the 4D language's built-in constants.
- **Three sources of errors:** failed precondition checks, mid-execution errors, and unexpected exceptions trapped with `ON ERR CALL` / `GET LAST ERROR STACK`.
- **Design trade-offs:** explicit guidance on what to log, where to store logs, and balancing "not enough detail" against "log file bloat."
- **Sample implementation:** extends the SQLLookup demo database from TN 15-09 into a working error-logging example.
- **Scaling paths suggested:** automatic emailed integrity reports, exporting logs to an external SQL database, or feeding a cloud log-analytics platform for larger deployments.

## Featured Technology
- `ON ERR CALL`
- `GET LAST ERROR STACK`
- Custom error-definition data structures (tables/JSON)
- SQL / cloud log analytics integration (conceptual)

## Best Practices Highlighted
1. Treat error definitions as structured, named data rather than embedding numeric codes or ad hoc text throughout code.
2. Design the recording layer to log "just enough" detail per error, tuned to its severity.
3. Route error logs to searchable storage (SQL/log analytics) once volume grows beyond what flat text files can handle.
4. Review accumulated error logs proactively before each release, not just react to production incidents.

## Context / Positioning
Published in the classic Design Mode era (v14.x, 2015) as a third-party contributed note, this is architectural/methodological guidance rather than a walkthrough of a specific 4D feature, so it sits somewhat outside the usual "new command in vX" format of contemporaneous notes and predates 4D's later class-based and Project Mode tooling.

## Historical Commentary
**Status:** Still relevant

Unlike many notes from this era tied to soon-to-be-superseded APIs (classic DOM XML, 4D Mobile/Wakanda, 4D Write classic), this note's substance is architectural discipline — define errors as data, catch consistently, record with context, analyze systematically — which remains sound advice in any modern 4D codebase, including those using Project Mode, classes, and ORDA. The specific mechanics (`ON ERR CALL`, `GET LAST ERROR STACK`) are unchanged in current 4D, though today's class-based object model could implement the same "error as data" idea more cleanly via a dedicated Error class rather than plain records/constants.
