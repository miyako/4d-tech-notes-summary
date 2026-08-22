# Tech Note 24-03: 4D_Info_Report Tips and Support Cases

**Author:** Thomas SCHLUMBERGER, Technical Services Engineer, 4D SAS.
**Published:** February 29, 2024 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79390
**Download:** https://kb.4d.com/DLTN/TN/2024/24-03_4DInfoReportsTips.zip

## Proposition
4D Server's behavior depends on many environmental factors, making it important to gather deployment context efficiently when communicating with 4D technical support. This note documents how to deploy and drive the 4D_Info_Report component to capture historical, human-readable Server snapshots, and shows through real support cases how those reports are used to diagnose crashes, freezes, and memory leaks.

## Key Points
- **Component basics:** 4D_Info_Report creates human-readable reports of a computer's context, 4D version, settings, and Server load, and can run continuously as a stored procedure (default every 5 minutes) for historical tracking.
- **Progressive integration levels:** From "no code" (calling shared `aa4D_M_`/`aa4D_NP_` methods directly from a remote client) to "low code" snippets in "On Server startup" to full host methods like `aa4D_M_Host_Change_Local_Folder` and `aa4D_M_Host_Attention_Reported`.
- **Component-presence guard pattern:** All examples check `COMPONENT LIST`/`Find in array($at_Components; "4D_Info_Report@")` before calling any shared method, avoiding hard dependency errors.
- **Report retrieval and comparison from remote:** `aa4D_NP_Report_Export_Display` opens a dialog to display the last report, launch a Compare dialog, manage the stored procedure, or enable live updates; retrieval is capped at 6000 reports and throttled to protect Server performance.
- **Stand-alone folder analysis is faster:** Unzipped report folders contain `Array_profiler.json` (per-session computer/app summary) and `Attention_report.txt` (permanent and contextual warnings), analyzable offline on any platform/version.
- **Attention categories:** Permanent Attentions (deprecated OS, low RAM, single-core CPU, disabled/misconfigured backup) versus contextual Attentions (cache-saturated temp files, slow report creation, backup errors, unexpected Server windows, active log type).
- **Graph dialog for pattern spotting:** Three polygon types — counted values, memory in MB/GB, and a pink "Attention" severity polygon — help visually identify problem periods across a report history.
- **Export/import as CompareBlob:** Parsing a large report folder can be slow; exporting the parsed result as a compressed "CompareBlob" file dramatically speeds up future analysis of the same folder.

## Featured Technology
- **4D_Info_Report component (v4.65/4.70):** Third-party/TAOW-distributed component providing the reporting and analysis engine.
- **Stored procedure scheduling:** `aa4D_NP_Schedule_Reports_Server` for periodic report generation on 4D Server.
- **Array_profiler.json / Attention_report.txt:** Structured and human-readable output files summarizing computer/app state and raised warnings.
- **Compare and Graph dialogs:** Built-in UI for comparing report sets and visualizing trends/attention levels over time.
- **ADJUST TABLE/INDEX/BLOBS CACHE PRIORITY, ORDA:** Mitigations recommended for cache-saturation issues surfaced by the reports.

## Best Practices Highlighted
1. Always guard component calls with a `COMPONENT LIST`/`Find in array` presence check before invoking shared methods.
2. Use stand-alone folder parsing (rather than remote retrieval) for faster, more thorough report analysis, and export parsed results as a CompareBlob to speed up repeat analysis.
3. Avoid leaving Administration, License Manager, MSC, or Runtime Explorer windows open on 4D Server, since these degrade performance and are flagged as Attentions.
4. Perform load testing (100+ concurrent users) before production deployment rather than relying on stand-alone testing alone.

## Context / Positioning
This note sits within 4D's ecosystem of Professional Services/support tooling, reflecting the platform's emphasis on operational observability for 4D Server deployments. It reinforces broader 4D v20-era themes of cache and performance tuning (ORDA, cache priority adjustments) and shows how community/TAOW-distributed components extend the core product for enterprise support workflows.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
