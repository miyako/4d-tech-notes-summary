# Tech Note 01-45: A simple styled text area using 4D Write 6.7

**Author:** Not specified in source
**Published:** September 30, 2001 | **Product/Version:** 4D Write v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=18208
**Download:** https://kb.4d.com/ftp://ftp.4d.com/aci_technical_notes/2001/windows/tn_2001_41-45_(sep)/01-45_stylized_text_areas.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> This tech note shows how to can use a 4D Write area on an input form so that it looks like a standard Alpha or Text field. The advantage is that you can use the 4D Write area to accept styled text.

## Key Points

Based on the available teaser text, this note is: a technique for embedding a 4D Write area on a form so it behaves like a plain Alpha/Text field while accepting styled text.

## Featured Technology

- 4D Write (classic plug-in)
- Styled text form areas

## Historical Context

Published September 2001 for 4D Write v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Obsolete**

This note shows how to embed a classic 4D Write area on a form so it visually behaves like a plain Alpha/Text field while still accepting rich styled text. Classic 4D Write (the plug-in-based rich text editor of this era) has since been replaced by 4D Write Pro, an entirely HTML/CSS-based document engine introduced around 4D v14, so the specific plug-in and API this note relies on are obsolete, even though the underlying goal — an inline styled-text input area — is still achievable with modern tooling.

**What has changed since:**

- Classic 4D Write was superseded by 4D Write Pro (introduced circa 4D v14, ~2012), a different HTML-based rich text engine
- 4D Write Pro areas are the modern way to embed styled/rich text editing directly on a 4D form
