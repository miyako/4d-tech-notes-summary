# Tech Note 06-03: Recording Information sent Between 4D Client and 4D Server

**Author:** Jean-Yves Fock-Hoon, QA Manager, 4D, Inc.
**Published:** January 20, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=41472
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_01-04_(JAN)/06-03_Info_bw_Client_Server.zip

## Overview
This note introduces 4D Server's request log recording feature (new database parameter selector ID 28 in 4D 2004), explains the structure of the resulting text log file, and provides a demonstration database that imports, aggregates, and visualizes this data to help developers diagnose and reduce Client/Server network traffic.

## Key Points
- Enabled/disabled via `SET DATABASE PARAMETER` with selector 28; a positive value both starts logging and names the log file, which auto-rotates at 10MB.
- Log columns explained: time, PID (internal process ID), UID (internal connection user ID), CID (connection ID), request ID, bytes in/out, duration (ms), and an optional request name.
- Frames the practical use case: since network latency/request volume often limits Client/Server performance, developers can monitor exactly what commands generate what server traffic.
- The bundled Demonstration database provides a "Request Log File" dialog to Record/Clear/View logs, importing raw text logs into a `[Requests]` table (avoiding loading tens of MB into arrays directly).
- **Raw Data** tab: a paginated listbox using named selections to preserve sort order across large data sets.
- **Mnemonics** tab: per-request-type statistics (call counts, average/sum duration and bytes) computed via the Quick Report editor and an XML export/import round trip.
- **Processes** tab: similar aggregation per connection/process ID to spot problematic processes.
- **Graphs** tab: five 4D Chart visualizations — bytes per request, bytes over time, durations over time, % share per request type, and duration per request type.
- Closes with a full Appendix 1 listing every internal 4D Server request ID and its mnemonic/description.

## Featured Technology
- `SET DATABASE PARAMETER` ID 28 (4D Server Log Recording)
- 4D Server request log file format
- Quick Report-driven XML statistics generation
- 4D Chart (bar/line/pie graphs)
- Named selections for paginated large-data listbox display

## Historical Context
Published in January 2006 for 4D 2004, this is the foundational companion to TN 06-04's deeper request-by-request performance analysis, predating 4D's native SQL engine (v11, 2007) and reflecting an era when performance diagnostics were built entirely from general-purpose 4D tools (Quick Report, 4D Chart) rather than any dedicated profiler. The need to monitor and optimize Client/Server network traffic remains a valid concern in modern 4D Client/Server deployments, though the specific visualization stack (4D Chart, Quick-Report-to-XML statistics) is dated relative to more current 4D reporting and monitoring capabilities.

## Status
**Still relevant** — the request-logging concept and Client/Server performance-monitoring motivation persist, though the demonstrated visualization tooling is dated.
