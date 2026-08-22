# Tech Note 21-05: Utilizing Info Report Component

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** March 29, 2021 | **Product/Version:** 4D v18 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78676
**Download:** https://kb.4d.com/DLTN/TN/2021/21-05_Uitilizing_InfoReport.pdf

## Proposition
When troubleshooting a slowdown, hang, or crash that develops over time, the first step is usually to set up automated health logging. This note explains installing and using the community-maintained Info Report component to record and graph key database metrics over long periods with minimal performance overhead.

## Key Points
- **Long history:** originated as a method library in 4D v6 (2004), converted into an installable component in v11, and actively maintained since by Thomas Schlumberger via TAOW.
- **Tracked metrics:** user/task/process counts, cache usage vs. max, memory/virtual memory usage, and stack size, logged on a configurable interval (5 minutes by default).
- **Lightweight by design:** unlike the heavier debug log, it can run for extended periods with negligible performance impact.
- **Different setup per deployment:** 4D Standalone/Server uses the built-in `aa4D_NP_Schedule_Reports_Server` scheduler; 4D Remote requires a custom looped wrapper method since the component only ships a single-report method for Remote clients.
- **Log retention control:** `aa4D_NP_Reports_Max_Set_Limit` (Server/Standalone) or a custom method (Remote) caps the number of retained report files.
- **Log locations differ by platform/deployment:** `Folder_Reports` next to the `.4dbase`, or OS-specific AppData/Library cache paths for Remote clients.
- **Graph-based analysis:** `aa4D_NP_Report_Compare_Display` renders collected logs as a graph; a monotonically increasing memory line regardless of user/process count is the signature of a memory leak.
- **"Attention" markers** overlay database setting changes, low disk space, syntax errors, and other events on the same timeline for correlation.

## Featured Technology
- 4D Info Report component (via TAOW)
- `aa4D_NP_*` / `aa4D_M_*` component methods
- Execute on Server attribute (implicit in Remote-vs-Server setup differences)
- `Get database parameter`

## Best Practices Highlighted
1. Match the downloaded component version to your exact 4D version before installing.
2. Disable stored procedures / heavy logging alongside this component when isolating a specific issue.
3. Cap log retention on Remote clients since files aren't auto-pruned there.
4. Use the "Attention" markers to correlate performance anomalies with configuration or environment changes.

## Context / Positioning
This note highlights 4D's ecosystem of community/technical-services-maintained diagnostic tooling distributed outside the core product via TAOW, positioning the Info Report component as the de facto first troubleshooting step recommended by 4D's own support engineers before escalating to heavier tools like full debug logs.

## Historical Commentary
**Status:** Still relevant

The Info Report component continues to be maintained and distributed via TAOW for current 4D versions, and remains a commonly recommended first-step diagnostic tool for long-running performance and memory-leak investigations — nothing native in 4D has subsumed its role. A developer today would follow essentially the same installation and analysis workflow described here, simply grabbing the release matching their current 4D version rather than v18.
