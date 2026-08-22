# Tech Note 05-22: Clusters: Using Saved Sets Effectively - Part II

**Author:** Not specified in available source
**Published:** June 12, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=37526
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_21-24_(JUN)/05-22_Clusters_Part_II.exe

## Overview
Second in a two-part series, this Tech Note covers how to use pre-built "cluster" saved sets to actually retrieve data efficiently, following Part I's coverage of creating and maintaining those clusters.

## Key Points
- Continues directly from Part I (Tech Note 05-21), which covered cluster creation/maintenance.
- Focuses on data retrieval using the pre-built clusters, the practical performance payoff of the technique.
- Represents a manual, developer-driven performance optimization pattern typical of the classic 4D era.

## Featured Technology
- 4D Saved Sets ("Sets")
- Cluster-based query performance technique
- Classic-language set operations for record retrieval

## Historical Context
**Status:** Superseded

Manual clustering of saved sets was a meaningful performance technique in 2005 given the query and indexing capabilities of 4D at the time, but subsequent versions of 4D have substantially improved the built-in query engine and indexing, narrowing the gap this technique aimed to close. For ORDA-based development, entity selections (introduced around 4D v16 R2/2017) offer lazy-loaded, cursor-like access to large record sets that addresses similar performance goals with a fundamentally different, more modern mechanism. Note: only the on-page teaser paragraph for this note survived in this archive — the full PDF and example database could not be recovered (old download-archive format not accessible in this environment), so this summary is necessarily limited to that teaser text.
