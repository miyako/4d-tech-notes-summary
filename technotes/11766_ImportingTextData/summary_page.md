# Tech Note: Importing Data from Text Documents

**Author:** Not specified in source document
**Published:** July 1, 1997 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11766
**Download:** Not available (no working download link archived for this page)

## Overview

This Tech Note explains the available approaches in 4D v6 for importing data delivered as text documents from other programs and platforms, and how to choose among them based on data format and integration needs.

## Key Points

- Three import approaches, in increasing order of difficulty: the User mode Import Manager, form-based import via the IMPORT TEXT command, and lower-level import via RECEIVE PACKET.
- Two basic input file types: fixed-length (fixed-format) and delimited.
- Method choice depends on the nature of the imported data and how it must integrate with existing database data.

## Featured Technology

- Import Manager (User mode)
- IMPORT TEXT command
- RECEIVE PACKET command
- Fixed-length vs. delimited text file formats

## Historical Context

Text-based data import/export was a core interoperability mechanism in the pre-XML, pre-JSON, pre-ODBC-ubiquity era of 4D v6 (1997), when moving data between disparate systems and platforms commonly meant exchanging flat text files rather than using modern structured APIs.

## Historical Commentary
**Status:** Superseded

This note covers foundational, still-conceptually-relevant text import mechanics (fixed-length vs. delimited files, choosing an import method based on data shape) that remain applicable in spirit to modern 4D, even though the specific tools named (the classic Import Manager UI and low-level RECEIVE PACKET-based import) have been superseded by newer, more flexible import commands and connectors in current 4D versions.
