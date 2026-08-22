# Tech Note 96-14: Converting Arrays to HTML Tables

**Author:** David Adams and Forrest Swilling
**Published:** March 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11667
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_11-15_(MAR)/96-14_Arrays_to_Table.exe

## Overview
This Tech Note documents a 4D procedure, `ArraysToTable`, that converts a series of parallel 4D arrays into a formatted HTML table, using the table tags proposed in the draft HTML 3.0 specification and extended by Netscape Navigator (also supported by Spry Mosaic at the time). It is aimed at 4D developers who want to programmatically publish database content as web tables without hand-typing error-prone HTML.

## Key Points
- A worked example builds an HTML table of 4D user group meeting info from a `[UserGroups]` file, using `SELECTION TO ARRAY` to populate parallel `Name`/`City`/`State`/`Meeting` arrays (with array element `{0}` reserved for the column title).
- `ArraysToTable` accepts: table caption, border size, cell spacing, cell padding, and per-column horizontal alignment (`L`/`R`/`C`), vertical alignment (`T`/`M`/`B`/`A`), and no-wrap (`N`) codes as short strings — one character per content array/column.
- The procedure takes a **variable number of pointer parameters** (`$8...$n`), one pointer per content array, so the same routine works for tables of any width.
- Helper routines `PadChars`, `HAlign`, `VAlign`, and `Wrappage` pad short alignment-code strings to the right length and expand abbreviated codes into full HTML attribute values (e.g. `L` → `LEFT`).
- Sensible Netscape-matching defaults are built in: border 2, cell spacing 2, cell padding 1, left horizontal align, top vertical align, wrap enabled.
- The generated HTML is written to disk via `Create document`/`SEND PACKET`/`CLOSE DOCUMENT`, i.e., a static HTML file rather than a dynamically served page.

## Featured Technology
- 4D procedural language: arrays, pointers, variable parameter counts
- HTML table generation (`<TABLE>`, `<TR>`, `<TH>`, `<TD>` with `ALIGN`/`VALIGN`/`NOWRAP`)
- Netscape Navigator's extended HTML 3.0 draft table tags; also compatible with Spry Mosaic

## Historical Context
Published in March 1996 as one of several 4D "Internet" Tech Notes that month (alongside TN 96-11 through 96-13), this note reflects a time when the Web's HTML table standard was still in draft form and browser vendors like Netscape were extending it ahead of formal standardization. The technique — manually building HTML strings from arrays inside 4D procedures — was a practical necessity before 4D had a built-in web server or templating tools, and long before ORDA/REST-based data publishing existed. Global procedures like `ArraysToTable` would later be renamed Project Methods starting with 4D v6 (1997). While the specific Netscape table tag dialect described here has since been fully absorbed into standard HTML/CSS, the general pattern of generating markup programmatically from structured data remains a recognizable technique, even though it is normally replaced today by templating engines, REST/JSON APIs, and client-side rendering.

