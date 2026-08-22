# Tech Note 01-02: Manipulating Selections with Sets

**Author:** Not specified in source document
**Published:** January 31, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=12153
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_01-05_(JAN)/01-02_Manipulate_Using_Sets.exe

## Overview
A discussion of the performance advantages of Sets for storing, loading, relating, and clearing record selections instead of repeatedly re-querying. This Tech Note discusses querying — one of the most fundamental operations in any 4D database — and the reality that query execution time grows with the total number of records in a table, directly affecting how long end users have to wait for results.

## Key Points
- Since fast response times are a high priority for database users, the note highlights 4D's ability to create Sets, relate them to the current selection, and store, load, and clear them as needed, rather than re-running expensive queries whenever a previously computed selection needs to be reused.
- It walks through the practical advantages of this approach and demonstrates concrete techniques for manipulating record selections via Sets.
- The featured technology is therefore Sets as a performance optimization tool for selection management, aimed at developers looking to reduce redundant querying and improve responsiveness in data-heavy 4D applications.

## Featured Technology
- Sets
- Query performance optimization
- Record selection management

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Partially_superseded

This note explains how Sets let developers store, relate, load, and clear record selections without repeatedly paying the cost of a full table query, framed around the observation that query time scales with table size and that users expect fast results. Sets remain a core, unchanged part of 4D's classic language today and this performance rationale is still valid, though modern applications increasingly also have ORDA entity selections available as an alternative, object-oriented way to manage and persist selection state.

**Related updates since:**
- Sets remain fully supported in current 4D versions with the same core behavior described here
- ORDA entity selections (2018+) offer an additional, more modern mechanism for managing and persisting record selections in newer 4D applications

