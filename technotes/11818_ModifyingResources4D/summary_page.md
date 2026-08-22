# Tech Note 98-16: Modifying Resources with 4th Dimension

**Author:** Not specified
**Published:** November 1, 1998 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11818

## Overview
This Tech Note shows how to programmatically modify STR# resources in 4D structure files using 4D v6 commands, replacing the need for external resource editors like ResEdit or Resorcerer.

## Key Points
- 4D v6 introduced programmatic access to resource files, eliminating the need for external tools.
- Focuses on modifying STR# (string list) resources.
- Includes "FlushKeys V6" sample database for changing flush buffer characters.
- Includes "4D Localizer" sample database for language localization.
- Replaces the workflow of using ResEdit or Resorcerer for resource editing.

## Featured Technology
- 4D v6.0
- Resource management commands
- STR# resource modification
- Database localization
- Classic Mac resource fork architecture

## Historical Context
**Status:** Obsolete

The resource fork-based approach described here is entirely obsolete. Modern macOS no longer uses resource forks for applications, and 4D now uses XLIFF files and built-in localization mechanisms instead of STR# resource manipulation. ResEdit and Resorcerer are discontinued classic Mac OS tools. The full archive/PDF for this note could not be recovered (NO_DOWNLOAD_LINK_TEASER_ONLY).
