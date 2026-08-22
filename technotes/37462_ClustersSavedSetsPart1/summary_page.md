# Tech Note 05-21: Clusters: Using Saved Sets Effectively - Part I

**Author:** Not specified in available source
**Published:** June 3, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=37462
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_21-24_(JUN)/05-21_Clusters_Part_I.exe

## Overview
The first of a two-part series, this Tech Note explains how to create and maintain "cluster" saved sets as the foundation of a technique to drastically improve database query performance.

## Key Points
- Introduces Clusters, a technique built on 4D's classic Saved Sets ("Sets") feature.
- Focuses on cluster creation and ongoing maintenance as data changes.
- Sets up for Part II (Tech Note 05-22), which covers actual data retrieval using the clusters.

## Featured Technology
- 4D Saved Sets ("Sets")
- Cluster creation and maintenance technique
- Manual, developer-managed query performance optimization

## Historical Context
**Status:** Superseded

This manual clustering approach was a valuable performance technique in 2005 given the query engine capabilities 4D had at the time, but later improvements to 4D's built-in query engine, indexing, and (for ORDA-based code) lazy-loaded entity selections have reduced how essential this kind of hand-managed technique is for new development. The general strategic idea — precomputing and reusing expensive-to-derive record groupings — remains a valid performance principle in any data-driven application, even if the specific classic-language Sets mechanism described here is no longer the primary tool developers reach for. Note: only the on-page teaser paragraph for this note survived in this archive — the full PDF and example database could not be recovered (old download-archive format not accessible in this environment), so this summary is necessarily limited to that teaser text.
