# Tech Note: Handling a Large Number of Records

- **Asset ID:** 19052
- **Tech Note #:** 01-51
- **Published:** November 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Thomas Maul, 4D Germany
- **Page URL:** https://kb.4d.com/assetid=19052
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_51-56_(NOV)/01-51_Large_Number_of_Records.hqx

## Overview

Thomas Maul of 4D Germany addresses the practical performance and scale limits of very large 4D tables (up to and around the 16-million-record ceiling), using a factory sensor-logging scenario to demonstrate combined index keys, timestamp arithmetic, record-volume reduction via aggregation/archiving, and a Boolean-set-based query cache for fast word searches.

## Key Points

- Illustrates the core problem with a factory example: two halls x five assembly lines x ten sensors x one reading/second = 8.6 million records/day, where a naive five-indexed-field schema forces 4D to run several sequential `QUERY` lines and intersect large intermediate selections each time.
- The "combined key" technique uses a Trigger on `On Saving New/Existing Record Event` to compute a single string key (e.g. `"003-02-01"` via `GenerateCombinedIndex_Sensor`) from Sensor ID, Assembly Line, and Production Hall, replacing three separate queries with one: `QUERY([Measured Values];[Measured Values]Sensor Key=$key)`, and even supports wildcard partial matches like `"001@"`.
- A second combined key, `GenerateTimeStamp`, converts Date+Time into a single Longint (`($thedate-!01.01.80!)*86400 + $thetime`) so date/time-range queries collapse from multiple Date/Time comparisons into one or two `TimeStamp` comparisons, cutting query time from minutes to seconds.
- To reduce total record volume, the note proposes aggregating raw per-second sensor readings into per-minute (or longer) arrays, storing them compressed in a Blob field along with precomputed average/min/max, trading detail-on-demand for a large reduction in stored records (e.g. from 1 day's worth to 2 months' or ~2 years' worth of storage).
- Archiving strategy: export older detailed data to disk with `Blob to Document` or `Send Variable`, keeping only summary/aggregated data live in the database, and reload detail data transparently (e.g. in an `On Load` check) only when a user specifically needs it.
- A "clustered index" / query-cache technique for full-text-style search builds one Boolean Set per unique word (`CREATE EMPTY SET`, `BOOLEAN ARRAY FROM SET`, `COMPRESS BLOB`) so that querying for a word becomes a fast `Use Set` operation, and querying for two words is a simple set intersection; real numbers cited are 21,000 archived messages, 69,500 unique words, and ~70,000 stored sets.
- Closing guidance: the same set-caching idea can cache entire web search URLs (not just individual words) for a short time window to reduce redundant server work from repeated or "Back button" searches.

## Featured Technology

- Combined/composite index key technique
- Triggers (On Saving New/Existing Record Event)
- Timestamp-as-Longint calculation for date/time range queries
- Blob/array-based data compression and archiving
- Clustered index via Boolean sets (BOOLEAN ARRAY FROM SET / CREATE SET FROM ARRAY)
- COMPRESS BLOB / EXPAND BLOB for set and data storage

## Historical Commentary

**Status:** Partially superseded

Thomas Maul, writing from 4D Germany, tackles a real scaling problem in classic 4D: multi-field queries against tables approaching the 16-million-record limit become slow because each additional QUERY performs its own indexed search and set intersection. His solution -- combining multiple fields into a single computed 'combined key' field maintained by a trigger, plus a timestamp-as-Longint technique for efficient date/time range queries, and a Boolean-set-based 'clustered index'/query cache for full-text-style search -- are clever manual workarounds for limitations that were inherent to 4D's classic single-field-index query engine of that era. Modern 4D includes vastly larger capacity (64-bit record limits far beyond 16 million), a more capable query optimizer, and native full-text/keyword search options, so most of these specific manual workarounds are no longer necessary for typical applications, though the combined-key and denormalization principles remain conceptually useful patterns for extreme-scale scenarios.

References to newer/updated information:
- 4D's per-table record limit has been raised far beyond the 16-million-record ceiling described in this note, reducing the urgency of the 'reducing records' techniques shown
- 4D's query optimizer and indexing engine have improved substantially since 2001, reducing (though not eliminating) the need for hand-built combined-key fields for multi-criteria queries
- 4D now offers native full-text search-style capabilities that reduce the need for the hand-rolled Boolean-set 'clustered index' query-cache technique shown for word-based searching
