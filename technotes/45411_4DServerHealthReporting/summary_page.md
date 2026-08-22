# Tech Note 07-05: 4D Server Health – Automatic Reporting

**Author:** Thomas Maul, General Manager, 4D Germany
**Published:** February 7, 2007 | **Product/Version:** 4D Server v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=45411
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_05-09_(FEB)/07-05_4D_Server_Health.zip

## Overview
This Tech Note shows how to build an automatic "health" reporting system for 4D Server using a sample database that generates daily status reports, delivered either by email (via the 4D Internet Commands plug-in) or as a live web page, so administrators can proactively spot problems and monitor server state over time.

## Key Points
- **Server Overview section:** 4D version, last start time, OS/service pack, last reboot, physical/virtual memory, and backup status.
- **Critical errors section:** flags clients or the server that didn't quit cleanly (no Quit command call) within the last 48 hours, plus per-computer crash history, helping distinguish a client-specific problem from a server-wide one.
- **Hard disk usage:** total/free space per disk with day/month/year historical deltas.
- **Table usage:** record counts and used-space ratio per table, useful for detecting large deletions and the need to compact data.
- **Process usage:** CPU time and memory per running process on the server machine, to gauge what else is competing for resources.
- **Database segment usage:** size of each database segment with historical growth deltas.
- **Installation:** copy six project methods via 4D Insider, one choice list, and a [ServerHealth] history table; requires 4D Internet Commands 2004.5+ for emailing; hook logging calls into On Startup/On Exit and On Server Startup/On Server Shutdown methods; run a nightly background process to generate and send/serve the report.
- **Alternative access:** the report can be served live over the 4D Web Server via a 4Daction URL instead of (or in addition to) email.

## Featured Technology
- 4D Server
- 4D Internet Commands plug-in (SMTP email)
- On Server Startup/Shutdown and On Startup/Exit database methods
- 4Daction web publishing
- 4D Insider (cross-database method copying)

## Historical Context
Published in February 2007 for 4D Server 2004, this note predates 4D v11's SQL engine and reflects an era when server health monitoring had to be hand-built entirely from application-level code and third-party plug-ins, with no dedicated APM tooling for 4D.

## Historical Commentary
**Status:** Superseded

The specific building blocks used here — the 4D Internet Commands plug-in for email, 4Daction-based web publishing, and 4D Insider for copying methods between databases — have all been superseded by native 4D language commands (SMTP/HTTP client commands) and later component/web-server architectures. The underlying idea of automated proactive server health reporting, however, remains a sound and still-relevant administrative practice, even if implemented differently in modern 4D applications.
