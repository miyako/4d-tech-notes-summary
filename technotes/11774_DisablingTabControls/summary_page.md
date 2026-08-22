# Tech Note: Disabling Tab Controls

**Author:** Not specified
**Published:** September 1, 1997 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11774
**Download:** Not available (no working download link archived — teaser only)

## Overview
This note explains how to enable and disable individual tabs in 4D V6's new tab control active object, which presents information in a multi-page format navigated by clicking tabs, either as a page-navigation tool or to organize content into categories.

## Key Points
- Tab controls are one of the new "active objects" introduced in 4D V6, driven by arrays or lists.
- Individual tabs can be disabled, as shown in the note's example database.
- Use the `Selected list item` command to detect which tab item was clicked, returning the "List" item reference number.
- Pass that reference number to `SET LIST ITEM PROPERTIES` to toggle a tab's "Enterable" property (True/False) and thereby enable or disable it.
- The note's core purpose is teaching this enable/disable technique specifically.

## Featured Technology
- 4D V6 Tab control (active object)
- `Selected list item` command
- `SET LIST ITEM PROPERTIES` command and the list item "Enterable" property

## Historical Context
Published September 1997 shortly after 4D V6 introduced the tab control as a new form object, this note documents a fairly low-level manipulation of list item properties to control tab availability. The archive of the full technical content (example database, exact code) could not be recovered (no working download link exists for the original page). The specific commands referenced (`Selected list item`, `SET LIST ITEM PROPERTIES`) remain part of the current 4D language, so this technique is still largely applicable, though modern 4D form design offers richer built-in tab/page control options that may reduce the need for this manual workaround.
