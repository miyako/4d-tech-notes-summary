# Tech Note: Filtering Out Illegal Characters

**Author:** Not specified
**Published:** November 1, 1999 | **Product/Version:** 4D | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11860

## Overview
This Tech Note provides a tool for detecting and removing illegal characters from indexed Alpha fields in 4D databases, preventing problems with queries, sorts, and indexes.

## Key Points
- Users can inadvertently enter control characters, high ASCII characters, or other illegal characters into Alpha/Text fields
- Some appear as blank spaces, others are invisible
- Can cause queries and sorts to malfunction and indexes to become corrupted
- Provides a purging tool for indexed Alpha fields
- Recommends data entry filters as prevention (example filter pattern provided)

## Featured Technology
- Data entry filters for character validation
- Alpha/Text field sanitization
- Index repair/maintenance

## Historical Context
**Status:** Superseded

The full PDF could not be recovered (error: NO_DOWNLOAD_LINK_TEASER_ONLY). The specific character encoding issues described here (high ASCII, control characters corrupting indexes) reflect the pre-Unicode era of 4D. Modern 4D uses Unicode throughout, which eliminates many of these problems. The 4D indexing engine has been rewritten multiple times with improved robustness. However, the general principle of input validation and data sanitization remains universally important in software development.
