# Tech Note 03-51: Free Form Object Storage

**Author:** Not specified in source document
**Published:** November 30, 2003 | **Product/Version:** 4D v2003 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=30595
**Download:** https://kb.4d.com/DLTN/TN/2003/Windows/TN_2003_48-51_(NOV)/03-51_FreeFormObjectStorage.exe

## Overview
A design-pattern Tech Note proposing an alternative to rigid, one-field-per-setting table schemas for storing unstructured or free-form application data such as user preferences.

## Key Points
- Identifies the common but inflexible pattern of one dedicated field per preference/setting in a database.
- Proposes an alternative approach to storing "unstructured" data without hard-coding a field per data item.
- Framed as a general-purpose data storage technique applicable beyond just preferences.

## Featured Technology
- Unstructured/generic data storage
- Text/BLOB serialization

## Historical Context
Written in the pre-JSON, pre-object-field era of classic 4D (no native object/collection data type existed yet), so flexible/free-form storage required custom serialization techniques; only the short teaser text for this note could be recovered here.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Superseded

The specific serialization technique this note likely used (probably text- or BLOB-based encoding, given 4D had no object/JSON field type in 2003) has been made largely unnecessary by 4D's later native Object/Collection data type and built-in JSON support, which now provide a natural, structured way to store free-form data. The core design motivation — avoiding rigid one-field-per-setting schemas for flexible data — remains highly relevant and is now solved more elegantly with modern 4D object fields.
