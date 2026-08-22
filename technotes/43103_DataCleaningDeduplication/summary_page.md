# Tech Note 06-20: Data Cleaning and Deduplication

**Author:** David Adams
**Published:** May 19, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=43103
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_18-21_(MAY)/06-20_Data_Cleaning.zip

## Overview
This note is a methodology-focused guide to cleaning up and deduplicating database records — a problem it frames as universal across all database platforms, not specific to 4D. It builds on the companion FuzzyTools component (see TN 06-19, TN 06-18) to demonstrate practical techniques, but its core content (standardization, blocking, matching, merging, and process improvement) is largely platform-agnostic.

## Key Points
- **Why bother:** duplicate/inconsistent data degrades report accuracy, increases mailing costs, hurts customer service, slows lookups, and complicates external-system reconciliation.
- **The four-stage process:** (1) cleaning/standardization, (2) query-based reduction of the candidate set ("blocking"), (3) fuzzy matching of candidates, (4) human-reviewed merge/combine.
- **Address standardization:** references USPS/UPS free web verification services (callable from 4D via cURL or HTTP GET), commercial vendors (PostCode Anywhere, AddressDoctor, DesertSoft), and warns that rules like USPS Publication 28 are genuinely complex — better to integrate an existing validator than hand-roll one.
- **Blocking:** exhaustive pairwise comparison grows near-exponentially ((n²−n)/2 pairs); practical blocking strategies include matching on a reliable field first (e.g., gender, ZIP code, birthdate proximity) or randomly sampling a percentage of records.
- **Fuzzy matching demo:** uses the FuzzyTools "Show People" sample (500 records, 50 duplicate pairs) to illustrate a weighted rule-based similarity scoring system combining edit distance, Metaphone phonetic codes, and other comparisons, with both positive and negative (disqualifying) scores.
- **Merge discipline:** combining confirmed duplicates should happen inside transactions, with care to avoid orphaning related child records; a user-facing review screen letting people accept, skip, or flag false positives is recommended over forced auto-merging.
- **Process improvement:** run duplicate-checking sweeps nightly, review mistakes with data-entry staff promptly, periodically re-measure duplication rates, and consider probabilistic/frequency-based weighting (rare names are more diagnostic than common ones).
- **Reporting tip:** generate one canonical XML report and use APPLY XSLT TRANSFORMATION to produce multiple output formats instead of writing separate report routines.

## Featured Technology
- FuzzyTools component (phonetic and edit-distance/LCS fuzzy matching)
- WordList word-comparison utilities
- USPS/UPS free address-verification web services (via cURL / 4D Internet Commands)
- APPLY XSLT TRANSFORMATION for multi-format reporting

## Historical Context
Written in 2006 for 4D v2004, well before 4D's SQL engine (v11, 2007), Project Mode, or ORDA existed. The FuzzyTools component it centers on was a third-party/community add-on of that era rather than a built-in 4D feature, and the commercial vendors and free postal web-service URLs cited are 2006-era references that should not be assumed current.

## Historical Commentary
**Status:** Still relevant

The deduplication methodology described — standardize first, reduce the comparison set, fuzzy-match with weighted scoring, and merge under human review — remains sound data-engineering practice today and translates directly to modern SQL-based or ORDA-based 4D applications. What's dated is the specific tooling: the FuzzyTools component itself, the 2006-era commercial address vendors, and the free USPS/UPS web service references, none of which should be assumed to still exist in their described form without independent verification.
