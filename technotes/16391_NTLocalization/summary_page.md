# Tech Note: NT Localization

- **Asset ID:** 16391
- **Tech Note #:** 01-34
- **Published:** July 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon
- **Page URL:** https://kb.4d.com/assetid=16391
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_31-35_(JUL)/01-34_NT_Localization.hqx

## Overview

Jean-Yves Fock-Hoon (QA Manager, 4D, Inc.) explains how 4D of the 6.7 era handled foreign-language ("foreign system") support across Mac OS and Windows NT — noting that 4D under Windows still emulated the Mac Toolbox through Altura's ASINTPPC.DLL, so its behavior largely mirrored the Mac. The note covers scripts, sorting/searching rules, character-set translation, and font/localization strategy for developers deploying 4D outside Roman/Western locales.

## Key Points

- Distinguishes **Roman systems** (French, US, UK, German, etc.) from **Script Manager (non-Roman) systems** — Japanese (`smJapanese`), Arabic (`smArabic`), Cyrillic (`smCyrillic`), East European (`smEastEurRoman`) — each requiring a Primary script plus optional Secondary scripts.
- Sorting/searching is governed by **Customizer Plus**'s Script Manager section: a Comparison mode (4th Dimension / System / Mixed [legacy] / German for v2.2 [legacy] / Turkish) plus a **TRIC resource** supplying the actual sort/search tables; 4D stores a signature in the data file to detect index/rule mismatches and prompt a rebuild.
- Explains that 4D cannot tell *which* Script Manager mode built an index (only that it was Script Manager-built), so indexes built under, e.g., a Korean system won't auto-rebuild when opened under Chinese.
- Cross-platform character translation between Mac and Windows extended-ASCII tables uses a **'MapC' resource**; Roman systems get automatic Mac↔Windows mapping via ASINTPPC.DLL, while foreign systems need explicit MapC tables (created/customized in Customizer Plus) and the `Mac to ISO` / `ISO to Mac` commands — relevant to Web Server character-set configuration too.
- Two kinds of localization: **Language** localization (needed to tokenize 4D methods correctly on a foreign system — required if developing under that system) and **Usage** localization (needed for correct sort/search behavior at runtime); compiling for a foreign system requires enabling "Script-Manager: ON" in the 4D Compiler.
- Font strategy guidance: West-European locales need little more than font availability checks; Central/East European locales (Chicago CE/Geneva CE) require the `FONT` command; Asian markets require `FONT SIZE`/`FONT STYLE` adjustments since bold/enlarged CJK fonts are often illegible; Arabic (right-to-left) layouts require `MOVE OBJECT` repositioning. 4D's built-in **style sheets** are recommended as the best general solution.
- Warns that editing/saving 4D methods under an uncustomized foreign system can corrupt tokenized code, since meta-characters (e.g., the diamond `◊` for inter-process variables) are remapped per locale (e.g., `<>` replaces the diamond under Japanese systems).

## Featured Technology

- 4D Script Manager systems (smRoman, smJapanese, smArabic, smCyrillic, smEastEurRoman)
- TRIC sorting/comparison resources
- Customizer Plus localization editor
- 'MapC' Mac-to-Windows character mapping resource
- Mac to ISO / ISO to Mac commands
- FONT, FONT SIZE, FONT STYLE commands
- 4D style sheets

## Historical Commentary

**Status:** Obsolete

This note documents 4D's pre-Unicode internationalization architecture — Script Manager systems, TRIC sort tables, and MapC character-mapping resources — configured through Customizer Plus, at a time when 4D under Windows still emulated Mac Toolbox behavior for foreign-language support. This entire mechanism became obsolete once 4D introduced native Unicode text handling (around 4D v11 SQL, 2007), which removed the need for platform-specific script managers and character-translation tables for almost all modern development. The note remains a useful historical reference for understanding legacy 4D data files created under Script Manager systems, but its guidance does not apply to current 4D versions.

**References to newer/updated information:**
- 4D introduced native Unicode text support beginning around 4D v11 SQL (~2007), superseding Script Manager/TRIC/MapC-based localization
- Windows NT itself is long obsolete, superseded by many subsequent Windows releases
- 4D's style sheets feature (recommended in this note for font/localization handling) remains part of the product today
