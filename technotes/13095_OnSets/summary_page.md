# Tech Note 01-13: On Sets

**Author:** Not specified in source document
**Published:** March 30, 2001 | **Product/Version:** 4D | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=13095
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_11-15_(MAR)/01-13_On_Sets.exe

## Overview
A brief introduction to Sets as a lightweight, memory-efficient way to manipulate record selections. This brief Tech Note introduces Sets as a tool for manipulating record selections more efficiently, in terms of memory usage, than working directly with full selections.

## Key Points
- It frames Sets as particularly valuable when a developer needs to handle selections quickly — for example when working with especially large tables — since a Set can capture and restore selection state without carrying the full overhead of a live selection.
- As one of the more concise entries in this batch, its featured technology is simply the Sets mechanism itself, presented as a quick pointer for developers who may not yet be taking advantage of this classic-language feature for performance-sensitive selection work.

## Featured Technology
- Sets
- Record selection manipulation
- Memory-efficient selection handling

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Still relevant

This short note introduces Sets as a way to manipulate record selections with less memory overhead than working with full selections directly, especially useful when quick handling of large selections is required. Sets remain a fully supported, core part of 4D's classic language today, and the fundamental performance rationale for using them over ad hoc selection manipulation is unchanged, making this brief introduction still directly relevant, even if modern ORDA-based entity selections now offer an additional, newer alternative for similar problems.

**Related updates since:**
- Sets remain part of 4D's current classic language, unchanged in their basic purpose
- ORDA entity selections (introduced 2018) provide a newer, object-oriented alternative for many selection-manipulation use cases alongside classic Sets

