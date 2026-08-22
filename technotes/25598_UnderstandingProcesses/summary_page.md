# Tech Note 02-57: Understanding Processes in 4th Dimension

**Author:** Not specified in source document
**Published:** December 31, 2002 | **Product/Version:** 4D v | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=25598
**Download:** https://kb.4d.com/DLTN/TN/2002/Windows/TN_2002_56-61_(DEC)/02-57_Understand_Processes.exe

## Overview
A foundational Tech Note explaining 4th Dimension's process model, clarifying the crucial distinction that 4D processes are cooperatively emulated rather than true operating-system threads.

## Key Points
- Clarifies that 4D processes are cooperatively emulated by a single underlying thread, not real OS threads.
- Notes that 4D processes have existed since 4D version 3.0.
- Identifies the main process as the User/Custom menu process (or User Interface/Client Manager/Cache Manager processes on 4D Server).

## Featured Technology
- 4D processes
- Cooperative multitasking model

## Historical Context
Reflects classic 4D's cooperative multitasking process model, a core architectural concept that predates the later preemptive multithreading capabilities introduced in much later 4D versions.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Superseded

This note's core conceptual explanation of 4D's classic cooperative process model remains accurate and useful for understanding legacy 4D code, but current 4D has since introduced true preemptive multithreading (worker processes with genuine OS-level concurrency) in later versions, meaning developers today must also understand a newer, more capable threading model beyond what this note describes.
