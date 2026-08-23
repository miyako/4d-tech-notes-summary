# Tech Note: The Blob Analyzer

- **Asset ID:** 12151
- **Tech Note #:** 01-10
- **Published:** February 28, 2001
- **Product / Version:** 4D 6.5
- **Platform:** Mac & Win
- **Author:** Gilles Mellot
- **Page URL:** https://kb.4d.com/assetid=12151
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_06-10_(FEB)/01-10_The_Blob_Analyzer.hqx

## Overview

Gilles Mellot of 4D S.A. provides a self-contained BLOB-inspection utility — a single Wood_Blob method plus form — that any 4D v6.5+ structure can drop in to view the contents of BLOB fields in hexadecimal, decimal, and binary, addressing 4D's lack of native BLOB display on forms.

## Key Points

- At On Load, the form scans every table and field with Count tables/Count fields/Field/Type(...)=Is BLOB to dynamically build a hierarchical pop-up menu (Blob_Choice) listing only the BLOB fields present in the host structure.
- The Ascii_txt/Hexa_txt display variables are populated via BLOB to text(Field(◊Table;◊field)->;Text without length;$offset;720), reading the BLOB in fixed 720-byte pages, with next/previous/first/last-segment buttons enabled or disabled based on position.
- Custom F_Dec2Base/F_Base2Dec/F_Ascii2Hexa submethods (dispatched through the same Wood_Blob method via a Case of on $1) implement base conversion between decimal, hexadecimal, and other bases without relying on built-in commands.
- An On Timer event continuously recomputes hex/decimal/binary values (vH/vD/vB) from the user's current highlighted selection in the hex text area via GET HIGHLIGHT, refreshing the display live as the selection changes.
- A Find dialog (triggered via the On Outside Call form event and ◊message="Find") searches the hex or ASCII text for a user-supplied value and highlights it with HIGHLIGHT TEXT and Position.
- A Goto dialog lets the user jump directly to a byte offset by computing the containing 720-byte page and highlighting the corresponding hex character range; a Print button uses OUTPUT FORM/PRINT RECORD to print the current view.

## Featured Technology

- BLOB fields and BLOB to text conversion
- Development-time BLOB inspection utility (Wood_Blob)
- Decimal/hexadecimal/binary base conversion
- Hierarchical pop-up menu for field selection
- On Timer form event for live hex/ASCII highlighting

## Historical Commentary

**Status:** Superseded

Written by Gilles Mellot of 4D S.A., this note addresses a real development-time gap of the era: 4D could not natively display the contents of a BLOB field on a form, a problem for developers using BLOBs to store non-4D data types. The utility it provides — a single reusable Wood_Blob method and form that lets a developer page through a BLOB field's contents in hex/ASCII/binary, search for byte sequences, and convert between number bases — has been superseded by 4D's expanded native debugger and variable-inspection tooling, and much of the raw-BLOB-as-generic-storage pattern itself has been supplemented by native JSON/object/collection handling for structured data.

**References to newer/updated information:**
- 4D's debugger and variable-inspection tools have since gained the ability to inspect BLOB and other complex variable contents natively, closing the gap this utility addressed
- Structured data that once had to be packed into BLOBs is now more commonly represented using native JSON, objects, and collections in current 4D versions
