# Tech Note 98-20: Using 4D's password system in the data file

**Author:** Not specified in source document
**Published:** July 1, 1998 | **Product/Version:** 4D v6.0.x | **Platform:** Mac &amp; Win
**Page:** https://kb.4d.com/assetid=11803
**Download:** Not available

## Proposition
This Tech Note addresses the challenge of preserving 4D's password system (users/groups) when updating client structure files, since this information was stored in the structure rather than the data file.

## Key Points
- 4D's password system (users/groups) was stored in the structure file
- Updating a client's structure file erased their password customizations
- Proposes a method to transfer password data to/from the data file
- Critical for developers distributing application updates to clients

## Featured Technology
- 4D Password System
- Structure File
- Data File
- User/Group Management

## Context / Positioning
The structure/data file architecture was central to 4D deployment. Password system portability was a recurring pain point for developers who needed to ship structure updates without disrupting client user configurations.

## Historical Commentary
**Status:** Obsolete

The problem of passwords being stored in the structure file (lost when updating client structures) was a significant deployment pain point in the v6 era. 4D eventually moved user/group management and addressed structure update workflows in later versions, though the architecture of separating structure and data has remained a core 4D concept.

---
*Note: The full PDF/archive for this Tech Note could not be recovered — the original page has no working download link. This summary is based solely on the on-page teaser paragraph.*
