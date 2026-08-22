# Tech Note: Optimizing Record Selections - Part 1 — Under the Hood of the 4D Data File

**Author:** Not specified in source document
**Published:** May 1, 1997 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11760
**Download:** Not available (no working download link archived for this page)

## Overview

Part 1 of a two-part Tech Note explaining how a 4D data file is organized on disk and in memory, providing the technical foundation for optimizing record selection handling discussed further in Part 2.

## Key Points

- Explains 4D data file disk space usage and in-memory representation.
- States its guidance applies across Mac and Windows, single-user 4D and 4D Client/Server, and 4D versions 3 and 6 alike.
- Serves as the architectural foundation for Part 2's discussion of current record, current selection, and named selections.
- Targets developers dealing with growing data volumes and increasing 4D Client/Web connection counts.

## Featured Technology

- 4D data file internals (disk and memory organization)
- 4D v3/v6 data file compatibility
- 4D Client/Server scalability considerations

## Historical Context

Describes the classic binary 4D data file format (spanning 4D v3 through v6), which has since been superseded by 4D's modern structure file format; the note's stated cross-version applicability (v3 and v6 alike) reflects how stable that binary architecture was during the mid-1990s before later architectural changes.

## Historical Commentary
**Status:** Superseded

This note explains the internal organization of the classic 4D binary data file on disk and in memory as background for optimizing record selections in large, multi-user deployments; the specific binary .4DB/.4DC data file architecture it describes has been long superseded by 4D's modern structure file format, though the general goal of understanding storage internals to optimize performance at scale remains a relevant engineering principle.
