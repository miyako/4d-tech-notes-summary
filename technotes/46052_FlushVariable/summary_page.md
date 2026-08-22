# Tech Note 001: The Flush Variable

**Author:** Samir Arora (revised by Scott Knaster; edited by John Doe)
**Published:** March 1987 (revised August 1987; republished April 1, 2007) | **Product/Version:** 4D v1.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=46052
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_13-16_(APR)/07-13_Flush_Variable.pdf

## Overview
This is a nostalgia reprint of the very first 4D Technical Note ever published, republished on April 1, 2007 with a foreword from then-4D Inc. president/CEO Brendan Coveney celebrating 4D entering its 21st year of publishing Tech Notes (and noting over a thousand had been published by that point). The original 1987 note describes the classic Macintosh "Flush" system variable used to trade crash-safety for a meaningful performance boost during bulk record operations.

## Key Points
- On classic Macintosh systems, 4th DIMENSION normally forced the File Manager to flush its disk write buffer to disk after every record create/modify, maximizing data reliability at the cost of speed.
- The system variable `Flush` (default value 1) could be set to 0 to disable this per-record flush, letting the OS flush only when its buffer filled — claimed to yield a 2–3x speed improvement, especially useful when importing large record sets.
- Explicitly lists the affected routines: `ADD RECORD`, `SAVE RECORD`, `DELETE RECORD`, `MODIFY SELECTION`, `APPLY TO SELECTION`, `DELETE SELECTION`, `DELETE DOCUMENT`, `IMPORT SYLK`/`TEXT`/`DIF`, `SAVE LINKED RECORD`, `SAVE OLD LINKED RECORD`, `SAVE VARIABLE`.
- Provides a sample procedure setting `Flush:=0` before a `RECEIVE RECORD`/`SAVE RECORD` import loop, then restoring `Flush:=1` immediately afterward.
- Explicit warning: using `Flush:=0` increases the risk of data loss on crash/power failure, so it should be used only for special bulk operations and reset to 1 as soon as possible.
- Even in its 2007 republication, the note is explicitly flagged (by 4D's own CEO) as inapplicable to current 4D versions — included purely "for the nostalgia."

## Featured Technology
- Classic Macintosh File Manager disk buffering
- The `Flush` system variable
- Bulk record import/save workflow (`RECEIVE RECORD` / `SAVE RECORD`)

## Historical Context
As the very first 4D Technical Note (originally from March 1987), this document is a window into 4D's earliest days, when the product ran on classic Mac OS and relied directly on the Macintosh File Manager's buffering behavior. That storage architecture bears no resemblance to modern 4D's journaled, transactional storage engine, and the `Flush` variable itself no longer exists in any current 4D version. The note's value today is purely historical/anecdotal, illustrating both the two-decade-plus lineage of 4D's developer documentation and how fundamentally the platform's underlying engine has been rebuilt since 1987.

## Historical Commentary
**Status:** Historical interest only

This 1987-era classic Mac OS buffering technique has no current-day equivalent or relevance to modern 4D development; its value is purely as a historical artifact marking the origin of 4D's Tech Note series.
