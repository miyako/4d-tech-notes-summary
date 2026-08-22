# Tech Note 06-06: OCI Mapper 2004.3

**Author:** Josh Fletcher, Technical Support Engineer, 4D, Inc.
**Published:** February 10, 2006 | **Product/Version:** 4D v2004.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=41779
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_05-08_(FEB)/06-06_OCI_Mapper_2004-3.zip

## Overview
This note documents the 2004-3 update to the OCI Mapper, an open-source 4D component that emulates the discontinued 4D Oracle plug-in's high-level commands on top of 4D for OCI, 4D's lower-level Oracle connectivity plug-in introduced with 4D 2004. Its goal is to give 4D Oracle developers a source-code-compatible migration path while also serving as a learning example for 4D for OCI programming in general.

## Key Points
- Architecture: OCI Mapper (framework, developer-owned) sits above 4D for OCI (plug-in, from 4D), which sits above the Oracle Call Interface library (API, from Oracle).
- 4D Oracle offered high-level commands but was discontinued for 4D 2004+; 4D for OCI is low-level but faster and required for continued Oracle development.
- Major fixes in this release: a rewritten `CheckError` method now iterates multiple OCI error records and supports `OD Last Error` properly; `OD Cursor state` and `OD Last Error` reliability bugs from the prior version were fixed.
- Known workaround: `OD GET SERVER LIST` fails to find Oracle Home under Oracle 10g due to a moved registry key; documents the manual registry key fix.
- Documents former 4D Oracle `OD SET OPTIONS` flags (kNoWait, kWithLock, kDistinctLines, kDeferred) that now apply globally rather than per-object.
- Explicit limitations: unreliable with multiple concurrent cursors using independent output parameter sets; no LOB (BLOB/CLOB/RAW) support without custom OCI code; cannot execute objects inside Oracle packages.
- Framed throughout as a "learning tool" and migration bridge, not a finished production solution — developers are encouraged to read and modify the provided source.
- First half of a two-part release; the companion debug-logging edition is covered in TN 06-12.

## Featured Technology
- OCI Mapper component (open-source 4D component)
- 4D for OCI plug-in
- 4D Oracle plug-in (legacy/discontinued)
- OCI error handling, cursor state tracking, `tnsnames.ora`/Oracle Home resolution

## Historical Context
Published in 2006, this note is squarely about a legacy Oracle plug-in transition (4D Oracle → 4D for OCI) that predates 4D's own native SQL engine (introduced in v11, 2007) by over a year, and long predates ORDA and Project Mode. The entire plug-in stack discussed — 4D Oracle, 4D for OCI, and the OCI Mapper component — has since been retired from current 4D product offerings, making this note relevant only as historical documentation for anyone still maintaining or archaeologically studying decades-old 4D-Oracle integrations.

## Status
**Obsolete** — documents a discontinued plug-in generation and a community migration component with no equivalent in current 4D releases.
