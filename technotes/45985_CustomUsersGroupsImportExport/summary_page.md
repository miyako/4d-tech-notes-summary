# Tech Note 07-12: Custom Users and Groups Import/Export

**Author:** Josh Fletcher, Technical Support Engineer, 4D Inc.
**Published:** March 28, 2007 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=45985
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_10-12_(MAR)/07-12_Custom_Users_Groups.zip

## Overview
This note builds a custom Users and Groups import/export module for 4D 2004 that closes a specific gap in the built-in Tool Box import/export feature: it does not preserve per-plug-in access group assignments, requiring tedious manual reconfiguration after every import into a new or updated database.

## Key Points
- 4D 2004's built-in "Groups" page (Tool Box / `EDIT ACCESS`) already preserves user names, passwords, startup methods, groups, group owners, and memberships — but not plug-in access settings.
- Plug-in access lets an administrator restrict which group can use a given licensed/serialized plug-in, important both for security and for managing scarce licenses under 4D Server.
- Core commands used: `USERS TO BLOB` / `BLOB TO USERS` (programmatic, encrypted export/import of the entire user/group access system) and `SET PLUGIN ACCESS` / `Get plugin access` (per-plug-in access group assignment; only works if a plug-in is installed, licensed, and not disabled).
- The example source database ("UG_Source.4DB", ~40 project methods) serializes this data as XML using 4D's DOM commands: the Users/Groups BLOB is Base64-`ENCODE`d into one XML element, while plug-in access settings become a loop-generated set of XML elements keyed by pre-defined XPATH constants.
- Four methods are the conceptual core: `UG_EXPORT_UGToXMLTree`, `UG_EXPORT_PluginAccessToXMLTree`, `UG_IMPORT_XMLTreeToUG`, `UG_IMPORT_XMLTreeToPluginAccess`.
- Design notes: uses a string-based "messaging" system instead of numeric error codes (so the compiler catches typos and code-completion works), plus a documented method-prefix naming convention.
- Acknowledged limitations: the exported Users/Groups BLOB is unreadable as plain XML (Base64-encoded), and plug-in XPATH/ID lists are hard-coded rather than dynamically discovered.
- A demo database ("UG_Demo.4DB") walks through setting a Designer password, restarting, logging in as Administrator, and importing a sample `demo.XML` covering plug-ins like 4D Draw, 4D View, 4D Write, 4D for OCI/ADO/MySQL/PostgreSQL/Sybase, with color-coded (green/orange/red) success/warning/error status messages.

## Featured Technology
- `USERS TO BLOB` / `BLOB TO USERS`
- `SET PLUGIN ACCESS` / `Get plugin access`
- 4D DOM XML commands
- `ENCODE`/`DECODE` (Base64 BLOB serialization)
- Classic 4D Users and Groups access system

## Historical Context
This note targets 4D 2004's classic access/security model and its serialized-plug-in licensing scheme (4D Write, 4D View, 4D Draw, ODBC-based database connectors, etc.), all predating 4D v11's native SQL engine (2007) and ORDA (2018+). `USERS TO BLOB`/`BLOB TO USERS` and the plug-in access commands remain present in current 4D for backward compatibility, but the plug-in licensing landscape they target has evolved substantially, and modern 4D development favors JSON over ad hoc DOM-based XML serialization for data interchange.

## Historical Commentary
**Status:** Superseded

The specific plug-in access commands and DOM-XML approach are dated, but the general need to programmatically export/import a database's security model (users, groups, permissions) between environments remains a standard administrative task in current 4D, now more commonly addressed via JSON and ORDA/REST-based tooling.
