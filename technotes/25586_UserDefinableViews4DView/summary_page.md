# Tech Note 02-45: User Definable Views Using 4D View

**Author:** Not specified in source document
**Published:** September 30, 2002 | **Product/Version:** 4D View v6.8 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=25586
**Download:** https://kb.4d.com/ftp://ftp.4d.com/aci_technical_notes/2002/windows/tn_2002_41-45_(sep)/02-45_user_definable_views.exe

## Overview
A Tech Note describing a generic, user-facing "Views" system built on 4D View, letting end users define and save their own custom record display layouts instead of relying on hard-coded output forms.

## Key Points
- Identifies the problem of repetitive, near-duplicate 4D View code across similar forms/tables.
- Builds a generic, reusable "Views" editor and engine on top of 4D View.
- Lets end users define, save, and reuse their own View definitions as a substitute for hard-coded output forms.

## Featured Technology
- 4D View
- Generic form-replacement engine

## Historical Context
4D View was 4D's classic spreadsheet-style area component; this note demonstrates a genuinely sophisticated, reusable architecture pattern built on top of it.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Superseded

4D View itself has been discontinued, making the specific implementation obsolete, but the underlying architectural idea — a generic, user-editable "saved view" system replacing hard-coded output forms — is a genuinely durable design pattern still used today, typically realized via list box form objects with user-configurable columns or web-based grid components with saved view/filter functionality.
