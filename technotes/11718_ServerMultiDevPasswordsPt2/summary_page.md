# Tech Note 96-39: Developing with 4D Server Part 2: Setting Up a Multi-Developer Password System

**Author:** Walt Nelson
**Published:** September 1, 1996 | **Product/Version:** 4D Server v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11718
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_37-41_(SEP)/96-39_Server_Pt_2.exe

## Overview
Part 2 of a three-part series on 4D Server multi-developer workflows, this note explains how to divide a large project into functional modules and configure a Design Mode Users/Groups password system so each module's development team owns only its own files, forms, and procedures.

## Key Points
- **Module division factors:** Universality, Interdependence, Timing/delivery schedule, Availability of resources, and Degree of difficulty/complexity — illustrated with a 5-module split of the Invoices example database.
- **Ownership model:** objects are owned by Groups, not individuals; the top-level Designer belongs to every group by default (full access), except cannot modify Administrator-created passwords/group memberships; the Administrator can Export/Import Users & Groups (a unique privilege) but has no other default design rights beyond compiling.
- **Compile/4D Insider restriction:** only the Designer and Administrator can Compile; only the Designer can open the structure with 4D Insider.
- **Worked example (Payments module):** assigns Group ownership to a File via the File attributes Owner pop-up, verifies a non-member user is denied access at Runtime; repeats the same Owner assignment for a Layout (Form) and a Global Procedure, carefully distinguishing "Owner" (Design-mode modify rights) from "Access" (Runtime usage rights, left open to All Groups in the examples).
- **Workaround for compile/Insider restriction:** periodically distribute "Single-User Copies" of the structure with a special, less-restrictive Designer password so developers can view (but not modify, since it isn't the Master Structure) work outside their module.

## Featured Technology
- 4D password system (Users & Groups, Design mode ownership/access)
- 4D Server / 4D Client multi-developer workflow
- 4D Insider
- 4D Compiler

## Historical Context
**Status:** Superseded

The underlying engineering discipline this note teaches — dividing large projects into ownership-scoped modules to prevent developers from overwriting each other's work — remains a sound and generally applicable practice. However, the specific mechanics are dated: Design Mode is now called that specifically because Project Mode was introduced in v17 (2018) as an alternative, text-based structure format that works naturally with modern source control (Git) branching and merging, largely obviating the binary-structure ownership-lock scheme described here. "Global Procedures" were also later renamed "Methods," and the single-Designer 4D Insider access limitation this note works around is a legacy constraint of binary structure files not shared by modern Project Mode databases.
