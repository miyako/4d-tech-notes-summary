# Tech Note 22-24: Overview of Logging and Configuration File

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** December 28, 2022 | **Product/Version:** 4D v19 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79082
**Download:** https://kb.4d.com/DLTN/TN/2022/22-24_LogConfiguration.pdf

## Proposition
Enabling 4D's diagnostic logs traditionally required code or UI changes that are impractical in compiled or multi-site deployments. This note documents the logConfig.json feature (4D v19 R3+) that lets an administrator load a single JSON file to control every logging subsystem at once, and pairs it with external OS-level tools for a complete troubleshooting toolkit.

## Key Points
- **logConfig.json follows a documented JSON Schema** covering forceLoggingConfiguration, requestLogs, debugLogs, diagnosticLogs, httpDebugLogs, POP3Logs, SMTPLogs, IMAPLogs, and ORDALogs.
- **forceLoggingConfiguration overrides code/UI settings** when true, which is useful for enforcing consistent logging policy across multiple 4D Server sites by distributing one file.
- **debugLogs.commandList supports positive/negative command number filters** (e.g. 277=QUERY, 341=QUERY SELECTION) to include or exclude specific commands from the debug log.
- **Loaded via 4D Server's Maintenance tab**, applying immediately without a server restart.
- **httpDebugLogs.level is equivalent to WEB SET OPTION(Web debug log; level)**, letting administrators capture only headers, body, or both for HTTP debugging.
- **External tools fill gaps 4D logging doesn't cover**: ProcDump (Windows) and native crash logs under /Library/Logs/DiagnosticReports (macOS) capture full process state at crash time.
- **The Info Reports component** gathers periodic 4D Server statistics (users, processes, memory) via a scheduled worker/stored procedure for longer-term trend analysis.
- **A per-scenario log matrix** (crashing on Windows/macOS, hanging, network instability) tells developers exactly which combination of logs and tools to enable.

## Featured Technology
- logConfig.json schema
- SET DATABASE PARAMETER
- ProcDump (Windows)
- macOS DiagnosticReports crash logs
- Info Reports component
- requestLogs / debugLogs / diagnosticLogs / httpDebugLogs / ORDALogs

## Best Practices Highlighted
1. Distribute the same logConfig.json to every 4D Server site so their logging configuration stays consistent, rather than relying on manually replicated code/UI settings.
2. Combine 4D's own logs with OS-native crash capture (ProcDump / DiagnosticReports) since 4D logs alone don't always explain a hard crash.
3. Use the commandList filter in debugLogs to scope debug logs to only the commands relevant to the problem being investigated, keeping log volume manageable.

## Context / Positioning
Published under 4D v19 R (late 2022), this note reflects 4D's ongoing investment in making 4D Server operable and diagnosable at scale — a priority as more customers run headless, multi-site server deployments. It packages a genuinely new administrative capability (config-file-driven logging) alongside longstanding external tooling recommendations from 4D's technical support playbook.

## Historical Commentary
**Status:** current

The logConfig.json mechanism described here is a durable, still-current feature of 4D Server administration; there has been no successor mechanism, and JSON-driven configuration remains squarely in line with 4D's broader move toward JSON/object-based configuration everywhere (settings files, ORDA, ROLES, ORDALogs, etc.). The specific per-scenario recommendations (ProcDump, macOS crash logs, Info Reports) also remain standard 4D technical-support practice as of this writing.
