# Tech Note 05-32: Server Processes

**Published:** October 3, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=39582
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_30-33_(SEP)/05-32_Server_Process.exe

## Overview
**Note:** this entry's content_source is `teaser_only` — the full PDF/example archive could not be recovered in this environment, so the following is based solely on the short on-page teaser text.

Per the teaser, this is the third Tech Note in an ongoing series building features into a shared example database, and this installment demonstrates setting up, managing, and running processes that are initiated from a 4D Client but that actually execute on the 4D Server.

## Key Points (from teaser)
- Third entry in a continuing example-database series.
- Demonstrates client-initiated, server-executed process management.
- Notes that, due to 4D's underlying architecture plus a small amount of conditional (If-statement) logic, the same mechanism can also run under a 4D Client or a Single User version of 4D if needed.
- No further detail on the specific commands or code structure used is available from the recovered teaser text.

## Featured Technology
- 4D Client/Server architecture
- Server-side process management
- Cross-mode compatibility (4D Client, 4D Server, single-user 4D)

## Historical Context
The full archive for this Tech Note could not be recovered (old-format download not accessible in this environment), so this summary is limited to the general pattern described in the teaser. The idea of delegating work from a client to the server remains conceptually valid, but 4D has since introduced dedicated worker-process language commands for managing background/server-side execution more directly than the manual client/server orchestration this note likely demonstrates.
