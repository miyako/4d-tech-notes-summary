# Tech Note 14-19: 4D Log Analyzer v1.0 Preview

**Author:** Vanessa Talbot, 4D Program Team Member, 4D SAS
**Published:** December 29, 2014 | **Product/Version:** 4D v14 R4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77198
**Download:** https://kb.4d.com/DLTN/TN/2014/14-19_4DLogAnalyzer.zip

## Proposition
This note introduces a preview of the 4D Log Analyzer, a companion tool built to make sense of 4D's new, more compact but no-longer-human-readable v14 debug log format, by importing raw log files as "projects" and rendering execution-time breakdowns for methods and commands across stored procedures, triggers, and processes via dedicated Activity, Top Ten, and Operations views.

## Key Points
- **New compact log format since v14** is machine-efficient but no longer directly human-readable, motivating a dedicated analysis tool.
- **Two ways to enable logging:** via the 4D Server Administration window's Maintenance tab, or programmatically with `SET DATABASE PARAMETER(34; 2+4)` (bit 2 = call parameters, bit 3 = new tabbed format).
- **Project-based workflow:** imported logs are organized into named "projects" inside the analyzer for later review.
- **Activity tab** visualizes time spent across processes/methods over the session.
- **Top Ten tab** surfaces the most expensive methods/commands at a glance.
- **Operations tab** breaks down individual logged operations in more granular detail.
- **Explicitly labeled v1.0 preview**, signaling further features/refinement were expected in later releases.

## Featured Technology
- 4D debug/request log format (v14+)
- SET DATABASE PARAMETER(34, ...)
- 4D Log Analyzer tool (projects, activity/top-ten/operations views)

## Context / Positioning
From December 2014, targeting 4D v14 R4, this note documents brand-new (at the time) logging infrastructure in the classic Design Mode era, well before ORDA, Project Mode, or 4D's later expanded observability features existed.

## Historical Commentary
**Status:** Partially Superseded

As an early "v1.0 preview" tool, this note is a snapshot of a still-evolving feature; the log-enabling command and admin-window controls it describes remain functionally present in modern 4D, but the specific analyzer tool previewed here has been superseded by later iterations of 4D's log analysis tooling.

The underlying need it addresses — turning opaque debug logs into actionable performance insight — is timeless, but developers today should look to current-generation 4D diagnostic/log tooling rather than this 2014 preview build for day-to-day work.
