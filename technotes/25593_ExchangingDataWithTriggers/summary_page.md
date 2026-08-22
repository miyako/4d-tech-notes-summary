# Tech Note 02-52: Exchanging Data with Triggers

**Author:** Not specified in source document
**Published:** November 30, 2002 | **Product/Version:** 4D v6.8.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=25593
**Download:** https://kb.4d.com/DLTN/TN/2002/Windows/TN_2002_51-55_(NOV)/02-52_Exchanging_Data.exe

## Overview
A Tech Note describing a technique for safely exchanging data between database triggers and calling code using a utility record, working consistently across interpreted/compiled and client/server contexts.

## Key Points
- Uses a dedicated utility record to safely pass data between triggers and the code that provokes them.
- Confirmed to work consistently in both interpreted and compiled 4D, and on 4D Server.
- Includes a sample database demonstrating the technique.

## Featured Technology
- Database triggers
- Utility records for inter-context data sharing

## Historical Context
Reflects classic 4D's trigger-based data validation/side-effect model, where reliably passing context data into and out of triggers required careful technique; only the short teaser text for this note could be recovered here.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Still Relevant

4D's trigger mechanism itself remains a supported, still relevant feature in current 4D, so the general utility-record data-sharing pattern described here remains applicable, though modern 4D also offers object/collection-based session or process variables that could provide additional, more structured ways to share such data today.
