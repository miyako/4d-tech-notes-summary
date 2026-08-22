# Tech Note 07-41: Macros in 4D v11 SQL

**Author:** Robert Molina, Technical Support Engineer, 4D Inc.
**Published:** October 31, 2007 | **Product/Version:** 4D Developer v11 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=47934
**Download:** https://kb.4d.com/DLTN/TN/2007/MacOS/TN_2007_39-42_(OCT)/07-41_4D_v11_SQL_Macros.pdf

## Overview
This note documents the evolution of 4D's method-editor macro feature (originally introduced in 4D 2003) as it stands in 4D v11 SQL, focused on macro storage/conversion mechanics and new full XML standard conformity.

## Key Points
- Macro history: 4D 2003 introduced text-insertion macros; 4D 2004 added the ability to call 4D methods from macros; 4D v11 SQL adds XML conformity, removes the need for blobs on macro text over 32,000 characters, and adds event-triggered macros.
- Conversion logic on first open: if a "Macros v2" folder exists, it's used as-is; if only an older "Macros" folder or Macros.xml exists, 4D v11 SQL creates "Macros v2" and copies content in; if none exist, 4D creates "Macros v2" with a generated default Macros.xml.
- New macro files get standard XML declaration + DOCTYPE lines prepended (encoding "windows-1252" on Windows, "x-mac-roman" on Mac when converting; UTF-8 recommended going forward), making macros fully W3C XML-conformant for the first time.
- New attributes were added to the `<macro>` XML element (detailed later in the source document).
- Aimed at developers maintaining custom macro libraries through the 4D v11 SQL upgrade.

## Featured Technology
- 4D Macros (method editor automation)
- "Macros v2" folder / Macros.xml conversion mechanism
- W3C XML standard conformity for macro definitions
- New `<macro>` element attributes

## Historical Context
Published in October 2007 as part of the wave of Technical Notes accompanying 4D v11 SQL, this note documents a largely internal tooling change to the classic 4D method editor's macro system, at a time when 4D development still occurred exclusively in binary Design Mode, long before Project Mode (2018) or any modern code-editor tooling.

## Historical Commentary
**Status:** Superseded

4D's method/code editor and associated productivity tooling have been substantially modernized in the many versions released since 2007, and the specific "Macros v2" folder/XML conversion mechanics described here are tied to that era's editor implementation. The note is chiefly of historical interest today, illustrating how 4D handled developer tooling migrations during major version transitions.
