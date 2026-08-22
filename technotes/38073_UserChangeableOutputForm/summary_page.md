# Tech Note 05-25: User Changeable Output Form

**Author:** Not specified in available source
**Published:** July 18, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=38073
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_25-27_(JUL)/05-25_ChangeableOutputForm.exe

## Overview
This Tech Note demonstrates how to let end users dynamically choose which field appears in each output form column, along with header text, data formatting, and alignment, all at runtime.

## Key Points
- Users can pick the field for each column, its header, its Date/Time/Number/Boolean format, and its alignment.
- Settings persist in memory for the running session, even across window close/reopen — but not across sessions (a follow-up note covers that).
- Implemented with four layout variables per column and a single reusable method, designed to be adapted to any database with minimal changes.

## Featured Technology
- Dynamic output/list form column configuration
- Layout variables driving runtime UI customization
- A single generic, reusable configuration method

## Historical Context
**Status:** Superseded

The specific technique of hand-rolling dynamic column configuration with layout variables on a classic Output form has largely been superseded by the modern List Box object, whose programmatic column and data-source APIs (expanded considerably in versions after 2005) make end-user-configurable tabular views far more straightforward to build today. The underlying feature idea — letting users customize their own list view — remains entirely legitimate and common in current 4D applications, just implemented differently. Note: only the on-page teaser paragraph for this note survived in this archive — the full PDF and example database could not be recovered (old download-archive format not accessible in this environment), so this summary is necessarily limited to that teaser text.
