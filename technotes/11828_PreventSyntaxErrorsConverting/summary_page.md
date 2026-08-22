# Tech Note 99-02: Preventing Syntax Errors in 4D Expressions When Converting

**Author:** Not specified
**Published:** March 1, 1999 | **Product/Version:** 4D v6.0.6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11828

## Overview
This Tech Note explains how to prevent syntax errors when converting databases from 4D v3 to v6, specifically addressing 4D expressions embedded in plug-in areas that cannot be versioned during conversion.

## Key Points
- Converting v3 databases to v6 can produce syntax errors when 4D expressions are embedded in plug-in areas.
- 4D cannot determine which version was used when creating expressions in plug-in areas.
- A resource-based solution prevents these conversion errors.
- Uses 4D Write as the primary example, but applies to all 4D plug-ins.
- Requires 4D version 6.0.6 or later.

## Featured Technology
- 4D v6.0.6
- Database conversion (v3 to v6)
- 4D Write plug-in
- Resource-based compatibility fixes

## Historical Context
**Status:** Obsolete

The v3-to-v6 database conversion path is no longer relevant as these versions are decades old. Modern 4D has completely different mechanisms for embedded expressions, and 4D Write has been replaced by 4D Write Pro with an entirely new document model. The full archive/PDF for this note could not be recovered (NO_DOWNLOAD_LINK_TEASER_ONLY).
