# Tech Note 05-44: Optimizing Searches with Hashes

**Author:** David Adams
**Published:** December 22, 2005 | **Product/Version:** 4D (2004 era) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=41108
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_40-46_(DEC)/05-44_Optimizing_Searches.zip

## Overview
4th Dimension's engine could not natively perform case-sensitive string searches, full text-field searches, or any search on BLOBs, pictures, or documents. This note explains hashing — reducing a value to a single longint — as a technique to make these searches practical and fast, built on the companion HashTools component (TN 05-43).

## Key Points
- Explains how hashing works, when to use it, and how to select among algorithms.
- Documents and benchmarks nine hashing algorithms: AP, BKDR, DJB, ELF, JS, PJW, RS, SDBM, and the simple SumBytes.
- A demonstration database includes Hashing Tests, Hashing Speed Tests, Hashing Search Speed Tests, and Hashing Collision Tests screens across several sample data sets.
- Recommends AP, BKDR, RS, and SDBM as functionally equivalent choices for most projects based on test results.
- Documents `HashTools_FindByHash`, which does an indexed pre-filter search on a stored hash field before confirming exact matches — a major speed win for text/BLOB/picture searches, best maintained via triggers.
- Notes that QUERY BY FORMULA is much slower, especially under 4D Server, motivating the hash-based approach.

## Featured Technology
- HashTools component
- Nine hashing algorithms (AP, BKDR, DJB, ELF, JS, PJW, RS, SDBM, SumBytes)
- Hash-optimized indexed search (`HashTools_FindByHash`)
- Case-sensitive / BLOB / picture / document searching

## Historical Context
This is a genuinely clever workaround for a real 4th Dimension 2004-era engine limitation, and the general "pre-filter with a cheap hash, then confirm exact match" pattern remains a timeless database optimization technique used well beyond 4D. However, 4D's subsequent SQL engine (from v11 SQL, 2007 onward) and continued query/indexing improvements have reduced how often developers need to hand-build this kind of workaround for ordinary case-sensitive or full-text search needs today.
