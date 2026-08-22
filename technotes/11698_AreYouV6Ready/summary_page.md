# Tech Note 96-42: Are You V6 Ready?

**Author:** David Adams
**Published:** September 1, 1996 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11698
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_41-45_(SEP)/96-42_V6_Ready.exe

## Overview
Published ahead of 4th Dimension version 6's release, this Tech Note is a preparation checklist helping developers understand breaking terminology, compatibility, and behavioral changes coming in v6 before they upgrade their existing v3.x databases and code.

## Key Points
- **Terminology change:** "Files" become **Tables**, and "Layouts" become **Forms** throughout v6's documentation, language, and interface — a foundational naming shift developers had to internalize.
- **EXECUTE statement compatibility:** source text intended for the `EXECUTE` statement should be stored in **STR# resource #8**, so that 4D can apply the correct compatibility handling when compiling/interpreting it under the new v6 compiler/language.
- **Longer identifier names:** table, field, and other object names can now be up to **31 characters**, a substantial increase from the previous 15 (or 11, in some contexts) character limits.
- **New pointer sign syntax:** v6 introduces a new syntax for the pointer sign character used to declare and dereference pointers, requiring review of existing v3.x code that uses pointers.
- **Stored procedure process IDs:** stored procedures now return **negative process IDs**, distinguishing them from regular process IDs — existing code comparing/checking process ID values needed updating.

## Featured Technology
- 4D v6.0 terminology changes (Tables/Forms replacing Files/Layouts)
- EXECUTE statement / STR# resource #8 compatibility mechanism
- 31-character identifier name length limit
- New pointer sign syntax
- Stored procedures returning negative process IDs

## Historical Context
Published in September 1996 as a pre-release readiness guide, this note documents one of the more significant terminology and language shifts in 4D's history — the Files/Layouts-to-Tables/Forms renaming that has since become the permanent, familiar vocabulary of 4D — alongside several compiler and language-level compatibility changes developers needed to plan for before adopting v6.

## Historical Commentary
**Status:** Superseded

The migration this note prepares developers for was a one-time historical milestone completed decades ago; 4D has since progressed through many further major version transitions (v7 through v20 and beyond), each introducing its own compatibility considerations. The v6 terminology change (Tables/Forms) described here has long since simply become standard 4D vocabulary rather than a novel change to adapt to, and 4D's language and compiler have evolved far beyond anything anticipated in this 1996 note, including Project Mode, ORDA, and modern object/collection data types.

