# Tech Note 96-36: New Entry Points in 4th Dimension 3.5.3

**Author:** ACI and ACI US Engineering
**Published:** August 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11715
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_33-36_(AUG)/96-36_New_Entry_Points.exe

## Overview
This is a plugin/external-package developer reference documenting three new C-level entry points added to 4D's external package API in version 3.5.3, none of which were yet documented in the standard Ext4D.h header shipped on the Partner CD at the time.

## Key Points
- **kEX_SUBSELECTION_TO_ARRAY (166):** bulk-copies field values or record numbers from a range of a file's current selection into one or more 4D arrays in a single call, using an `ArFldCouple` struct array to map fields to array names; supports following Many-to-One relations, and is optimized for 4D Server (arrays built server-side, then sent whole to the client).
- **kEX_SET_HOOK (168):** lets a plugin register Sequential Operation Progress and Printing Progress hook functions as part of its own bundled, platform-specific resources — eliminating the earlier requirement to manually place Mac HOOK resources or Windows DLLs outside 4D Server's automatic Mac4DX/Win4DX distribution mechanism.
- **kEX_4DPX_ATTRIBUTES (169):** allows one external package to introspect another installed package's entry point address, code type (68K/PowerPC/Intel), private data handle, resource file reference, and name — enabling calls between plugins, with a crash-risk warning if the target hasn't yet been initialized.
- All three entry points use 4D's `ParameterBlock`-based calling convention and are documented across 68K, PowerPC, and Windows/Intel builds.

## Featured Technology
- 4D's original external package (plugin) API and Ext4D.h header
- ParameterBlock-based C calling convention
- 4D Server's Mac4DX/Win4DX automatic component distribution mechanism

## Historical Context
This note is a deep, low-level plugin-development reference tied to 4D's original external package architecture, which predates the modern 4D Plugin SDK by multiple major generations. The explicit handling of 68K-based Macintosh code (versus PowerPC and Windows/Intel) reflects an era before Apple's transition away from 68K and, much later, PowerPC entirely. While the underlying needs — bulk field-to-array data extraction, custom progress UI, and inter-plugin communication — remain conceptually relevant, the specific struct layouts, entry point numbers, and distribution mechanisms described are obsolete; modern 4D exposes equivalent bulk-extraction functionality directly in the language (e.g. `SELECTION TO ARRAY` and related commands) rather than requiring a custom plugin entry point.
