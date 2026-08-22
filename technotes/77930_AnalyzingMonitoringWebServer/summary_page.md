# Tech Note 18-01: Analyzing and Monitoring 4D Web Server

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** January 18, 2018 | **Product/Version:** 4D v16 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77930
**Download:** https://kb.4d.com/DLTN/TN/2018/18-01_4DWebServerInfo.zip

## Proposition
Introduces `WEB Get server info`, a new v16 R5 command that returns comprehensive 4D Web Server metrics as a single object, and demonstrates building a custom monitoring dashboard and logging system around it.

## Key Points
- **New command, one-line retrieval:** `WEB Get server info` obtains current 4D Web Server metrics and settings in a single call using 4D's object type variables.
- **Web server fundamentals covered:** settings and starting/stopping the 4D Web Server are documented as background context.
- **Technical properties documented:** the note enumerates the metrics/information available via the command in detail.
- **Sample monitoring database:** demonstrates polling the command to build a live-status monitoring interface.
- **Logging subsystem:** stores historical web server metrics for later analysis, including generating metric lists and comparing changes between log entries or selections of logs.
- **Complex system, simplified access:** frames the 4D Web Server as feature-rich (from settings to runtime metrics) and positions this single command as dramatically simplifying access to that complexity.

## Featured Technology
- `WEB Get server info` command
- 4D Web Server settings and lifecycle (start/stop)
- 4D object type variables
- Custom logging/graphing of historical metrics

## Best Practices Highlighted
1. Use `WEB Get server info` rather than piecing together web server state from multiple older commands/sources.
2. Combine live monitoring with historical logging to support both real-time health checks and trend analysis.
3. Compare metrics across log entries (rather than only viewing the latest snapshot) to detect gradual issues.

## Context / Positioning
Published right after v16 R5 introduced this command, the note reflects 4D's mid-2010s classic web server (pre-REST-server, pre-ORDA) architecture, where the built-in 4D Web Server handled HTTP requests directly rather than via a dedicated ORDA-based REST layer. It's an operations-facing note aimed at administrators/developers running production 4D web deployments.

## Historical Commentary
**Status:** Still relevant

`WEB Get server info` remains part of the current 4D language and continues to be a valid, supported way to retrieve 4D Web Server metrics, so this note's central technique is still directly usable today. The overall monitoring-and-logging pattern it demonstrates (poll a metrics command, log results, graph trends) also remains sound practice.

The broader context has shifted somewhat: 4D later introduced a REST server built on ORDA, adding a different (and increasingly more emphasized) web-facing surface alongside the classic 4D Web Server that this note doesn't address, and 4D's built-in server administration tools have continued to improve since 2018. Still, for classic 4D Web Server deployments, this note's guidance remains accurate.
