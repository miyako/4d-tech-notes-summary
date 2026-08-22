# Tech Note 01-28: Creating a 6.0-style Pop-up in 6.7 using Layered Objects

**Author:** Not specified in source document
**Published:** June 30, 2001 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=15347
**Download:** https://kb.4d.com/ftp://ftp.4d.com/aci_technical_notes/2001/windows/tn_2001_26-30_(jun)/01-28_popups_6.0_in_6.7.exe

## Overview
A form-object workaround that restores 4D v6.0's pop-up/drop-down click-only object-method behavior in v6.5+. This Tech Note addresses a subtle behavior change introduced in 4D v6.5: unlike v6.0, pop-up menus and drop-down lists now run their object method as soon as the user browses the menu, not only when an item is actually selected.

## Key Points
- For developers who had built logic assuming the old "select-to-fire" behavior, this could break existing forms migrated from v6.0.
- The note's solution is to layer additional form objects (an approach common in binary Design Mode form editing of the era) so that the object method only executes meaningful code when a true selection occurs, effectively emulating the original v6.0 semantics.
- It is a small, surgical technique aimed squarely at cross-version compatibility during the v6.0-to-6.5/6.7 migration window many 4D shops were navigating in 2001.
- The featured technology is entirely classic-language form object manipulation: pop-up/drop-down objects, their object method trigger, and layered/overlapping form objects as a UI trick.

## Featured Technology
- Pop-up menus / Drop-down lists (form objects)
- Layered objects
- Object method (form event handling)

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Obsolete

This note documents a narrow compatibility workaround for a form-object behavior change between 4D v6.0 and v6.5 (pop-up/drop-down menus firing their object method on browse, not just on selection), implemented by layering objects on a binary Design Mode form. The specific trick is tied to the old pop-up/drop-down object types and binary form editor of that era, and the underlying v6.0-vs-v6.5 behavior distinction it addresses has been irrelevant for two decades. It is preserved mainly as a historical illustration of how form-object workarounds were built before richer event models and Project Mode existed.

**Related updates since:**
- 4D's form object model and event system have been significantly extended since (including list box-based dropdowns and richer On Load/On Data Change events), reducing the need for layered-object workarounds
- Project Mode (4D v17+) replaced binary Design Mode structures with text-based form files, changing how forms are authored and versioned

