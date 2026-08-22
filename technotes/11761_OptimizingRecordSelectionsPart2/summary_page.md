# Tech Note: Optimizing Record Selections - Part 2 — Under the Hood of the 4D Data File

**Author:** Not specified in source document
**Published:** May 1, 1997 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11761
**Download:** Not available (no working download link archived for this page)

## Overview

Part 2 of a two-part Tech Note on optimizing record selection handling in 4D as data files and concurrent user counts grow, focusing on the runtime concepts of current record, current selection, and named selections.

## Key Points

- Builds on Part 1's coverage of 4D data file disk/memory organization.
- Explains current record, current selection, and named selections as the key concepts developers manipulate at runtime.
- Discusses optimization principles relevant to large data files and high concurrent user/connection counts.
- Framed for 4D Client/Web-connected deployments where scalability was a growing concern.

## Featured Technology

- 4D data file internals
- Current record / current selection
- Named selections
- Record set-based optimization

## Historical Context

Written for the classic 4D v3/v6-era binary data file architecture, well before 4D's modern structure file format and ORDA entity selections existed; however, the fundamental idea of manipulating record subsets as sets/selections for performance remains a core, still-relevant 4D concept today.

## Historical Commentary
**Status:** Still relevant

This note explains the core 4D concepts of current record, current selection, and named selections and how they affect performance with large data files and many concurrent users; these set-based selection concepts remain fully current in modern 4D (including ORDA-based entity selections), even though the specific v3/v6-era binary data file internals discussed as context have been long superseded by the modern structure file format.
