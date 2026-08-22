# Tech Note 01-04: Data File Log

**Author:** Not specified in source document
**Published:** January 31, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=12157
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_01-05_(JAN)/01-04_Data_File_Log.exe

## Overview
A technique for monitoring the number, size, and fragmentation state of a classic 4D data file's segments, to avoid hitting the old 2GB-per-segment limit. This Tech Note tackles a real operational hazard of the classic 4D data file format: a database's data file could be composed of up to sixty-four segments, each limited to 2GB, and if the first segment filled up before additional segments were created, developers could run into time-consuming problems.

## Key Points
- The difficulty was compounded for remote clients, where it could be hard to know in advance when a client's data was approaching that 2GB ceiling, whether additional segments had already been added, and how fragmented (i.e., what percentage of deleted-but-not-reclaimed records) their data files had become — a state that could itself degrade performance.
- The note's solution is a simple monitoring implementation that tracks the number and size of data segments, as well as the fragmentation level, across all tables in a database.
- Its featured technology is thus classic 4D data-file introspection aimed squarely at proactive database administration, helping teams catch segment/fragmentation issues before they caused outages or slow performance for end users.

## Featured Technology
- 4D classic data file format (segmented, up to sixty-four 2GB segments)
- Data segment/fragmentation monitoring
- 4D Server / remote client administration

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Obsolete

This note addresses a hard architectural limitation of the classic 4D data file format of the era: a database could comprise up to sixty-four segments, each capped at 2GB, and administrators needed tools to monitor segment count, size, and fragmentation (percentage of deleted records) to avoid running into trouble, especially with remote clients whose data growth was harder to observe directly. This entire class of problem is now obsolete: 4D's data engine was re-architected in later versions (starting with 4D v11 SQL, 2007) to remove the old segmented 2GB-per-segment ceiling, so the specific monitoring technique and its underlying motivation no longer apply to modern 4D databases.

**Related updates since:**
- 4D's data file architecture was fundamentally re-engineered starting with 4D v11 SQL (2007), eliminating the legacy sixty-four-segment, 2GB-per-segment structure this note is designed to monitor
- Modern 4D database administration relies on different, built-in tooling for monitoring data file size and fragmentation rather than custom segment-tracking code

