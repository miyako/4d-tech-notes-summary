# Tech Note 01-55: Index Control Panel

**Author:** Not specified in source
**Published:** December 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=19054
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_54-57_(DEC)/01-55_Index_Control_Panel.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> There are times indexed fields may need to have their indexes turned off and on for rebuilding a particular field's index or for other reasons. If the database is compiled, the access to the design environment is not available and it is time consuming to re-index the uncompiled version and recompile it. This technical note explores a means of turning indexes off and on programmatically.

## Key Points

Based on the available teaser text, this note is: a technique for programmatically enabling and disabling field indexes on a compiled database.

## Featured Technology

- SET INDEX / index management commands
- Compiled database maintenance

## Historical Context

Published December 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Still relevant**

This note addresses a practical pain point of the compiled-database era: needing to toggle field indexes on and off without access to the Design environment, since a compiled database could not be re-indexed or recompiled quickly. The technique of programmatically enabling/disabling indexes via the classic language remains valid in current 4D versions, though modern deployments increasingly manage index/data maintenance through 4D Server's administrative tools rather than hand-rolled control panels.

**What has changed since:**

- 4D's classic indexing commands remain part of the current language largely unchanged
- 4D Server/4D Mobile administration tools now provide more built-in maintenance tooling than existed in 2001
