# Tech Note 98-18: Building a User-Definable Report/Function Interface

**Author:** Not specified
**Published:** December 1, 1998 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11821

## Overview
This Tech Note describes a data-driven approach to report and function management, storing report/method metadata in data tables and presenting them via access-controlled drop-down lists.

## Key Points
- Addresses the scalability problem of managing many reports via direct menu calls.
- Stores report names and associated method names in the application data file.
- Populates drop-down lists dynamically from stored metadata.
- Integrates password-group-based access control for per-user report visibility.
- Works for both report dialogs and function access from detail forms.
- Enables end-user customization of available reports/functions.

## Featured Technology
- 4D v6.0
- Dynamic method dispatch
- Password group access control
- Data-driven UI patterns
- Drop-down list population

## Historical Context
**Status:** Historical interest only

The data-driven, metadata-based approach to UI construction described here remains a valid design pattern. However, modern 4D would implement this using ORDA for data access, collections for UI population, and more granular permission systems beyond classic password groups. The full archive/PDF for this note could not be recovered (NO_DOWNLOAD_LINK_TEASER_ONLY).
