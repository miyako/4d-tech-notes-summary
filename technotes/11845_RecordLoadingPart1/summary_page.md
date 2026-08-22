# Tech Note: Record Loading in 4th Dimension - Part 1

**Author:** Not specified in source document
**Published:** August 1, 1999 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11845
**Download:** Not available

## Overview
Part 1 of a series on how 4D v6.5 loads records internally, with implications for performance when dealing with large BLOB-containing records over networks.

## Key Points
- BLOB fields make individual records potentially very large
- Record loading behavior in v6.5 has performance implications developers should understand
- Network traffic optimization is especially important over WANs
- Part 1 of a multi-part series

## Featured Technology
- 4D v6.5
- Record Loading
- BLOBs
- Network Optimization
- Memory Management

## Historical Context
**Status:** Historical Interest Only

This note covers record loading internals in 4D v6.5, knowledge that was critical when BLOB fields were newly introduced and network bandwidth was limited. Modern 4D with ORDA handles entity loading with automatic lazy loading and optimized network transfer, making the specific v6.5 mechanics obsolete while the general principle of understanding data loading for performance remains valid.

### Related Updates
- ORDA entity loading replaced procedural record loading patterns
- Automatic lazy loading of BLOB and object fields in modern 4D

**Note:** The full PDF/archive for this Tech Note could not be recovered — the original download link was either missing or pointed to an obsolete format (e.g., a Windows self-extracting .exe installer). The summary above is based solely on the on-page teaser text preserved from kb.4d.com.
