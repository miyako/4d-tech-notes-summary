# Tech Note: Object Libraries

- **Asset ID:** 35535
- **Tech Note #:** 05-02
- **Published:** January 13, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Jonathan Le
- **Page URL:** https://kb.4d.com/assetid=35535
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_01-04_(JAN)/05-02_Object_Libraries.hqx

## Overview

Jonathan Le (Technical Support, 4D, Inc.) introduces Object Libraries -- a new 4D 2004 mechanism for storing reusable form objects, including their properties and object methods, in a shareable external file -- and shows how the new EDIT FORM command lets developers expose "Editable Forms" that end users can customize at runtime using a supplied Object Library.

## Key Points

- Defines an Object Library as an external file (created like a database, via the Design environment's "New" button) whose members are form objects, distinct from 4D Insider libraries because it holds only form objects (with properties and object methods) but works directly with any database, without requiring 4D Insider.
- Shows how objects are dragged/copied between a form and the Object Library's clipboard-like viewer, and how the new EDIT FORM command opens a simplified "User Form Editor" (e.g. `EDIT FORM([Table 1];"Input";"";"Sample Lib.4IL")`) so end users in Custom Menus mode can add/remove Object Library objects to an "Editable" form -- objects containing object methods are invisible in this mode since compiled databases cannot add code at runtime.
- Explains "standalone" vs. "dependent" objects: standalone objects (e.g. Standard Action button libraries) work in any database with no external dependencies, while dependent objects rely on project methods supplied by a Template or Component (illustrated with a `DoSomethingToHighlighted` example).
- Recommends generic coding techniques for objects meant to work on any table/database -- using `Current form table` and `Table name()` instead of hard-coded table pointers like `->[Pets]` -- and shows a commented-out, easily-adapted "Add To Outlook" object example that references field names the developer must uncomment/adjust.
- Highlights bundled Office/iApps Object Libraries: Windows objects for Word/Excel 2003 built on `LAUNCH EXTERNAL PROCESS`, `APPLY XSLT TRANSFORMATION`, and `PROCESS HTML TAGS`; Mac OS X equivalents for Excel 2004, iCal, and Address Book (Word 2004 for Mac lacked XML support at the time).
- Notes the Object Library revision/version mechanic implicitly via the EDIT FORM command's requirement that project methods called by object methods must exist in the calling database, or a runtime error results.

## Featured Technology

- 4D Object Libraries (.4IL files)
- EDIT FORM command with Object Library parameter
- Current form table / Table name (generic, table-independent object methods)
- Standard Action object libraries
- LAUNCH EXTERNAL PROCESS, APPLY XSLT TRANSFORMATION, PROCESS HTML TAGS (used by bundled Office/iApps libraries)

## Historical Commentary

**Status:** Superseded

Jonathan Le's note introduces Object Libraries, a new 4D 2004 mechanism for saving reusable form objects (with their properties and object methods) into a standalone .4IL file that can be shared between databases without the separate 4D Insider tool, and shows how the new EDIT FORM command lets end users customize "Editable Forms" using a supplied Object Library. It also details design patterns for writing generic, database-independent object code using Current form table rather than hard-coded table pointers. This binary Design Mode-era mechanism, along with 4D Insider itself, was superseded by 4D's modern Project Mode (introduced in v17/2018) and component architecture, which offer far more powerful and text-based ways to package and reuse form elements and code across databases.

**References to newer/updated information:**
- 4D Insider is no longer part of the modern 4D product line
- 4D's Project Mode (v17, 2018) and component system now provide filesystem-based, far more capable mechanisms for sharing and reusing forms, objects, and code across databases
- The generic-coding guidance (using Current form table instead of hard-coded table pointers) remains good practice in modern 4D development
