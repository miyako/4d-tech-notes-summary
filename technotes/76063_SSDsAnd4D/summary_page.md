# Tech Note 10-09: SSDs and 4D v11 SQL

**Author:** Josh Fletcher, Technical Services Team Member, 4D Inc.
**Published:** March 26, 2010 | **Product/Version:** 4D v11.6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76063
**Download:** https://kb.4d.com/DLTN/TN/2010/MacOS/TN_2010_07-11_(MAR)/10-09_SSDs_and_4D.pdf

## Proposition
This note examines whether solid-state drives improve 4D performance given how disk-intensive 4D is (data file, structure file, data log, indexes, and the v11 SQL data file cache all depend on storage speed), explaining SSD internals and benchmarking real drives against real 4D workloads.

## Key Points
- 4D relies heavily on disk I/O: the **data file, structure file, data log file, indexes, and data file cache** are all storage-bound.
- Explains **SSD internals**: flash memory cells, the controller, wear-leveling/lifespan features, and performance features.
- Describes **why SSD write performance degrades over time** — every write can effectively become a read-modify-write cycle as free blocks run out (write amplification/fragmentation).
- Provides guidance on **buying the right SSD** and setting expectations for real-world gains.
- **Benchmarks** three drives (Western Digital Raptor HDD, Intel X25-M SSD, OCZ Colossus SSD) across three 4D operations: modifying 500,000 records, 100,000 random GOTO RECORD calls, and sorting 6,000,000 records sequentially.
- Concludes with guidance on when developers should expect the biggest real-world performance benefit from SSD adoption.

## Featured Technology
- SSD architecture (flash cells, controllers, write amplification)
- 4D v11 SQL Data File Cache
- Benchmarking (500,000 record modification, random Goto Record, 6,000,000 record sort)

## Best Practices Highlighted
1. Prioritize fast storage for 4D deployments, since indexes, the cache, and the data/log files are all disk-bound.
2. Understand SSD write-amplification and fragmentation behavior before assuming an SSD will always outperform an HDD.
3. Benchmark storage choices against representative 4D workloads (bulk modification, random access, large sorts) rather than generic disk benchmarks.

## Context / Positioning
Published as SSDs were becoming affordable for mainstream use, this note applied 4D-specific benchmarking to a hot hardware trend, building on the earlier "4D v11 SQL Data File Cache" note (TN 09-43).

## Historical Commentary
**Status:** Obsolete

This note explains early-generation SSD internals (flash cells, controllers, write amplification, fragmentation-related performance degradation) and benchmarks specific 2009-2010 consumer/enterprise drives (Western Digital Raptor, Intel X25-M, OCZ Colossus) against 4D disk-intensive workloads.

The core recommendation — that 4D benefits substantially from fast storage because indexes, the data file, the data log, and the cache are all disk-bound — remains valid today, but the specific hardware, controller behavior, and degradation characteristics described are obsolete: modern SSDs (NVMe, TRIM support, wear-leveling improvements) have moved far beyond the drives and controller generation profiled here, so the benchmark data and buying advice are of historical interest only.
