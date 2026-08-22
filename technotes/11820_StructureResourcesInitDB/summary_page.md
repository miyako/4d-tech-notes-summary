# Tech Note: Using Structure Resources for Initializing a Database

**Author:** Not specified
**Published:** February 1, 1999 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11820

## Overview
This Tech Note demonstrates how to use resources stored in the 4D structure file to initialize default records in new data files and embed serial numbers or identifying information for simple copy protection.

## Key Points
- Uses resources in the structure file to create missing default records in new data files.
- Demonstrates embedding serial numbers or user information in the structure.
- Information persists into every new data file created by the user.
- Can serve as a simple copy protection mechanism.
- Leverages 4D's resource access commands for practical deployment needs.

## Featured Technology
- 4D v6.0
- Resource management (structure file resources)
- Database initialization
- Simple copy protection via embedded data

## Historical Context
**Status:** Obsolete

The resource fork-based approach described here is entirely obsolete. Modern 4D does not use resource forks for data storage, and database initialization is handled through the On Startup database method and other mechanisms. Copy protection and licensing are managed through 4D's built-in license management system. The full archive/PDF for this note could not be recovered (NO_DOWNLOAD_LINK_TEASER_ONLY).
