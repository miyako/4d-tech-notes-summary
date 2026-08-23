# Tech Note: Data File Log

- **Asset ID:** 12157
- **Tech Note #:** 01-04
- **Published:** January 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Steve Hussey
- **Page URL:** https://kb.4d.com/assetid=12157
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_01-05_(JAN)/01-04_Data_File_Log.hqx

## Overview

Steve Hussey (CEO, Alto Stratus LLC) tackles a real operational hazard of the era's 4D data files -- a hard limit of sixty-four 2 GB segments, with remote clients at risk of hitting it unexpectedly -- by providing a `LOG_Create` method that writes out a tab-delimited report of every data segment's size and path plus every table's record count, deletion count, and fragmentation percentage.

## Key Points

- A 4D data file could comprise up to sixty-four 2 GB segments; if the first segment reached its 2GB limit before additional segments existed, developers could face difficult-to-fix problems, especially with remote clients whose segment status was hard to monitor.
- `ARRAY TEXT(text_Segments;0)` plus `DATA SEGMENT LIST(text_Segments)` retrieves the full paths of all current data segments, which the method then loops through, getting each one's size with `Get document size` and writing size + path as a tab-delimited row via `SEND PACKET`.
- Per-table statistics come from looping `For ($Table;1;Count tables)`: `Records in table` gives the current record count, `Sequence number` gives the next available record number (so subtracting one and the current record count yields the number of deletions), and the fragmentation percentage is `(Deletions/Records)*100`.
- The output log is a plain tab-delimited text document (opens cleanly in a spreadsheet like Excel), with clearly labeled header rows for "Segment Size"/"Segment Path" and "Table #"/"Table Name"/"Records"/"Deletions"/"Frag%".
- The example database lets users delete a batch of `[Contacts]` records and then regenerate the log to directly observe the resulting change in fragmentation percentage.
- `LOG_Create` is noted as fully structure-independent and portable to any 4D database, but on 4D Server it must be run inside a Stored Procedure rather than on 4D Client, due to how `DATA SEGMENT LIST` behaves; the author suggests scheduling it periodically (e.g. weekly) and emailing the resulting log via 4D Internet Commands to proactively flag segment or fragmentation issues.

## Featured Technology

- DATA SEGMENT LIST command
- Sequence number for tracking deletions
- Records in table / Count tables
- SEND PACKET for streaming a tab-delimited log document
- Data segment size and fragmentation percentage reporting
- 4D Server Stored Procedure execution requirement

## Historical Commentary

**Status:** Obsolete

Steve Hussey's note addresses a real operational pain point of the era's 4D data files -- a maximum of sixty-four 2 GB segments, with remote clients at risk of silently hitting that ceiling -- by providing a LOG_Create method that writes out a tab-delimited log of each data segment's size and path plus each table's record count, deletions, and fragmentation percentage using DATA SEGMENT LIST and Sequence number. Since 4D's newer .4DD data file format removed the 2 GB-per-segment/64-segment ceiling and modern 4D includes built-in structure/data analysis and maintenance tools, the specific problem this note solves -- monitoring an approaching segment limit -- and its manual DATA SEGMENT LIST-based technique are now largely obsolete, though the general idea of periodically auditing fragmentation and file health for remote databases remains a sound practice.

**References to newer/updated information:**
- 4D's data file format was later redesigned (the .4DD format) to remove the legacy 64-segment / 2 GB-per-segment ceiling this note was written to help developers monitor
- Current 4D versions provide built-in tools for structure and data file diagnostics/maintenance, reducing the need for a hand-rolled DATA SEGMENT LIST-based logging method like the one in this note
