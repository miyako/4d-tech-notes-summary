# Tech Note 13-06: Data Reconstruction

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** May 22, 2013 | **Product/Version:** 4D v13.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76828
**Download:** https://kb.4d.com/DLTN/TN/2013/13-06_DataReconstruction.zip

## Proposition
This Tech Note presents a single-method approach, UTIL_TransferData, for rebuilding a 4D data file by loading the existing data as an external file and using embedded SQL to systematically copy every table's data into a brand-new, blank internal data file, producing a perfectly defragmented and clean result.

## Key Points
- Explains why rebuilding a data file helps with fragmentation and guarantees clean data/indexes.
- Provides the UTIL_TransferData method with full source code for transferring data table-by-table via SQL.
- Recommends disabling all triggers and startup/shutdown database method code before running the transfer to avoid interference.
- Details preparation steps: locating source data, making a structure copy, and starting 4D with a blank data file.
- Walks through the process of actually transferring the data end-to-end.

## Featured Technology
- 4D SQL (embedded)
- External data file
- UTIL_TransferData method
- Structure copy / blank data file
- Triggers and startup/shutdown method disabling

## Best Practices Highlighted
1. Disable triggers and startup/exit code during bulk data operations to prevent unintended side effects.
2. Work against a structure copy with a blank data file rather than modifying the live production data file in place.
3. Use SQL for bulk table-to-table transfer instead of manual record-by-record scanning for performance and clarity.

## Context/Positioning
Published for 4D v13.2 as practical DBA-style guidance for developers maintaining large, long-lived 4D data files that could become fragmented over years of use, before more automated maintenance tooling existed.

## Historical Commentary
**Status:** Still Relevant

The core problem (data file fragmentation/corruption requiring reconstruction) and the SQL-based table-copy technique remain valid and usable in current 4D versions, since embedded SQL is still fully supported for classic-language projects. That said, developers working in ORDA/entity-based projects today would more likely perform equivalent bulk data operations through entity selections and dataclass methods, and 4D has also introduced improved built-in data file verification/repair tooling over the years that can reduce the need for a fully manual rebuild.
