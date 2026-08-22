# Tech Note 06-12: OCI Mapper Debug 2004-1

**Author:** Josh Fletcher, Technical Support Engineer, 4D Inc.
**Published:** March 24, 2006 | **Product/Version:** 4D Oracle (4D 2004 + 4D for OCI) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=42333
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_09-13_(MAR)/06-12_OCI_Mapper_Debug.zip

## Overview
This note introduces a debug-enabled variant of the OCI Mapper component — a 4D-language framework that emulates the high-level commands of the discontinued 4D Oracle plug-in on top of the lower-level 4D for OCI plug-in. It is the second of a two-part release; the debug logging code was split out from the main OCI Mapper (documented separately in TN 06-06) because the added instrumentation made the core methods harder to read.

## Key Points
- Adds 26 new "OCIM_DBG_" methods to log OCI Mapper method calls and 4D for OCI function calls to a plain-text log file.
- Log entries include process ID, a "stack level" (artificial indentation for readability, not the real 4D call stack), and OCI constants rendered as readable strings instead of integers.
- Only integer and string parameters are natively logged; other types show as "<n/a>" unless the parameter-formatting method is extended.
- A background log-monitor process caps log file size (default 500KB) and rotates/archives old logs (default 6 kept), using semaphores for safe multi-process access.
- Logging of OCI Mapper calls and raw OCI calls can be toggled independently.
- Developers can call the same logging primitives from their own custom methods and OCI calls, making it a general-purpose debugging harness.
- Requires 4D 2004 and the 4D for OCI plug-in; installed/updated via 4D Insider, and the non-debug OCI Mapper must first be uninstalled before installing this debug version.

## Featured Technology
- 4D for OCI plug-in
- OCI Mapper component (open-source 4D component)
- Oracle Call Interface (OCI)
- 4D Insider (component installation tooling)
- Text-file based logging/debugging harness pattern

## Historical Context
Published in 2006, this note documents tooling for an Oracle connectivity stack (4D Oracle → OCI Mapper → 4D for OCI) that existed entirely before 4D's own native SQL engine arrived in 4D v11 (2007) and long before ORDA. The debug logging technique — text logging with process IDs and indentation-based call depth — is a generic, still-recognizable debugging pattern, but the specific OCI Mapper component, 4D for OCI plug-in, and 4D Insider-based component installation workflow it depends on are all long retired from current 4D products, making this note relevant only to historical archaeology of legacy 4D-Oracle integrations.

## Status
**Obsolete** — describes a discontinued plug-in ecosystem and component-based debugging tool with no equivalent in current 4D releases.
