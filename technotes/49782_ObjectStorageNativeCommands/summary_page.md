# Object Storage in 4D v11 SQL Using Native Commands

## Overview
4D v11 SQL extended hierarchical list items to support Object-like structures, where a single list item can hold values of mixed types (numeric, string, boolean) — effectively a dictionary attached to each list item. The note demonstrates using the new SET LIST ITEM PARAMETER and GET LIST ITEM PARAMETER commands to store and retrieve these object-style key/value pairs natively, without needing external XML or text serialization.

## Key Points
- Published May 14, 2008 as Technical Note 08-18.
- Targets 4D v11 on Mac & Win.
- Author: Luis Pineiros Technical Services Team Member, 4D Inc..

## Featured Technology
- 4D v11 SQL
- Hierarchical lists
- SET LIST ITEM PARAMETER / GET LIST ITEM PARAMETER commands
- Object-like data storage

## Historical Context
This note captures 4D's early, native attempt at object-like storage on top of the classic hierarchical list structure — years before 4D introduced true JSON/object support (the Object type and OB commands) in later versions. The specific SET/GET LIST ITEM PARAMETER approach is now superseded by native object (OB Get/OB Set) and JSON support built directly into the language.

**Status:** superseded

**Related updates:**
- 4D later added native Object (OB_...) and JSON commands, providing far more ergonomic key/value and nested-object storage than the hierarchical-list workaround shown here
- ORDA (2018+) and native JSON support now handle most of what this technique was working around
