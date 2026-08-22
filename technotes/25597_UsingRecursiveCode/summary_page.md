# Tech Note 02-56: Using Recursive Code

**Author:** Not specified in source document
**Published:** December 31, 2002 | **Product/Version:** 4D v6.8 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=25597
**Download:** https://kb.4d.com/DLTN/TN/2002/Windows/TN_2002_56-61_(DEC)/02-56_Using_Recursive_Code.exe

## Overview
A Tech Note discussing recursive coding patterns in 4D, with particular attention to the harder-to-detect indirect recursion pattern and why it should generally be avoided.

## Key Points
- Defines direct recursion (a method calling itself) and indirect recursion (method A calls B which eventually calls back to A).
- Warns that indirect recursion is often unintentional and hard to trace/maintain.
- Recommends avoiding this programming style due to maintainability difficulties.

## Featured Technology
- Recursive methods
- Code maintainability

## Historical Context
General programming guidance applicable to classic 4D's method-based (non-object-oriented) programming style of the era.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Still Relevant

The software-engineering guidance in this note — that unintentional indirect recursion is hard to trace and should be avoided — is a timeless principle that remains just as valid in modern 4D (including its later object-oriented class-based code) as it was in 2002.
