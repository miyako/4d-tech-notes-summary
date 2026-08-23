# Tech Note: Recovering a Damaged Data File

- **Asset ID:** 36397
- **Tech Note #:** 05-09
- **Published:** March 6, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Thang Nguyen
- **Page URL:** https://kb.4d.com/assetid=36397
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_12-16_(APR)/05-09_Recovering_Damaged_Data_File.hqx

## Overview

Thang Nguyen (4D Technical Support Engineer) presents an escalating set of techniques for diagnosing and recovering a corrupted 4D data file: 4D Tools' Check/Repair options, Recover by Tags for rebuilding a new data file from record header tags, manual re-indexing by stripping and rebuilding a structure file's indexes, a record-by-record 'massaging' diagnostic method, and text/XML export as the final fallback.

## Key Points

- 4D Tools' Maintain tab offers Check All (thorough, recommended for regular maintenance), Check Records (specific tables), and Check Indexes (specific indexes) to detect corruption.
- 4D Tools' Repair tab offers matching Repair All, Repair Records, and Repair Indexes options, letting you scope repair to just the damaged part of a large database for speed.
- Recover by Tags builds a brand-new data file from the tags (a record's 'resume' stored in its header) rather than repairing in place, used when the address table itself is too damaged for Quick Repair; requires ample free disk space and matching data-file segment configuration.
- Manual re-indexing procedure: duplicate the structure file, remove all relations, drop all indexes per table, relaunch the duplicate structure against the original data file to strip indexing, then relaunch the true original structure file to force a clean re-index.
- Provides the full 'Massaging' method source (by Hugo Fournier) that loops Count tables/Count fields/ALL RECORDS, buffering and re-saving each field per its type (Alpha, Text, Integer, LongInt, Boolean, Date, Time, Picture, Real, BLOB; Subtable skipped), logging each successfully loaded record to a 'Record Logs' document to help isolate which record crashes the app.
- As a last resort for severe corruption, recommends 4D's built-in Export to tab-delimited text or XML (not SEND RECORD/RECEIVE RECORD, which re-imports corruption verbatim) since export coerces every field value to text, discarding corruption that a whole-record binary copy would carry over.
- Explicitly recommends always backing up first and trying 4D Backup + log-file integration before resorting to any of these more invasive recovery techniques.

## Featured Technology

- 4D Tools Check All / Check Records / Check Indexes
- 4D Tools Repair All / Repair Records / Repair Indexes
- 4D Tools Recover by Tags
- Manual re-indexing via structure-file duplication
- "Massaging" record-by-record load/resave diagnostic method (by Hugo Fournier)
- Export to tab-delimited text / XML as a last-resort recovery path

## Historical Commentary

**Status:** Still Relevant

Thang Nguyen, a 4D Technical Support Engineer, lays out an escalating toolkit for recovering a corrupted classic 4D data file — 4D Tools' Check/Repair options, Recover by Tags (rebuilding the address table from record header tags when it's itself damaged), manual re-indexing by stripping and rebuilding indexes, a record-by-record 'massaging' load/resave diagnostic method credited to Hugo Fournier, and exporting to text/XML as a last resort. This remains a genuinely useful reference for anyone still operating a classic 4D data file/structure-file pair, since 4D Tools and its Check/Repair/Recover-by-Tags workflow are still the standard recovery mechanism in 4D today, though 4D strongly recommends backup+log-file integration as the first line of defense (as the note itself states) and modern 4D also offers newer built-in backup/verification tooling that reduces how often these manual techniques are needed.

References to newer/updated information:

- 4D Tools' Check/Repair/Recover by Tags workflow remains the standard classic recovery mechanism in current 4D
- 4D's backup and transaction-log integration have continued to evolve in later versions, and remain the first-recommended recovery path ahead of the manual techniques in this note, consistent with the note's own guidance
