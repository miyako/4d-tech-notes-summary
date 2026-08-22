# Tech Note 11-25: 4D SQL Query Browser

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** August 9, 2011 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76386
**Download:** https://kb.4d.com/DLTN/TN/2011/11-25_4DSQLQueryBrowser.zip

## Proposition
This Tech Note demonstrates how to build a generic SQL client for 4D Server using SQL Pass-through, enabling simultaneous connections to multiple 4D Server (v11.2+) databases from a single application.

## Key Points
- **Prerequisites:** requires 4D Server v11.2+ with SQL Server enabled, a known SQL publishing port (default 19812), a client/unlimited SQL license, and valid SQL credentials.
- **Multi-connection architecture:** the sample opens a new process per SQL Query Browser window, allowing concurrent connections to several 4D Servers.
- **Connection flow:** collects username, password, and server IP, then authenticates via the SQL LOGIN command.
- **Server browsing:** once connected, the tool lets the user browse the target server's schema and data.
- **Query browser UI:** provides an interface for exploring data and issuing SQL queries against the connected server.
- **Dual purpose:** works as both a teaching example of SQL Pass-through mechanics and a directly reusable diagnostic utility.

## Featured Technology
- SQL LOGIN command (SQL Pass-through)
- 4D Server SQL engine (v11+)
- Per-process multi-connection client architecture

## Context / Positioning
Published in mid-2011, shortly after SQL capabilities matured in 4D Server v11/v12, this note gave developers a ready-made diagnostic and exploration tool for a still-new SQL access layer, encouraging adoption of SQL Pass-through as a serious integration option.

## Historical Commentary
**Status:** Still Relevant

SQL Pass-through via SQL LOGIN and 4D's embedded SQL engine remain functional in current 4D, so this sample browser's core mechanism still works as a way to connect to and explore multiple 4D Server databases simultaneously via SQL.

However, for building new client tools that inspect or browse remote 4D data, developers today would more likely reach for 4D's REST/ORDA APIs, which offer JSON-based, HTTP-native browsing without requiring a SQL client license or SQL Server to be separately enabled.
