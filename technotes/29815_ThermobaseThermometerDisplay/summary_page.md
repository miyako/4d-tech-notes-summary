# Tech Note: Thermobase

- **Asset ID:** 29815
- **Tech Note #:** 03-41
- **Published:** September 30, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon
- **Page URL:** https://kb.4d.com/assetid=29815
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_40-43_(SEP)/03-41_Thermobase.hqx

## Overview

Jean-Yves Fock-Hoon, QA Manager at 4D, Inc., explains why a thermometer (progress bar) placed in the same window as a long-running task never updates — because the busy process can't service window redraws — and presents the standard workaround: spin up a separate, always-idle process to own and redraw the progress dialog, updating it from the working process via global variables and CALL PROCESS. Two example methods (M_TEST1, M_TEST2) demonstrate single and multiple simultaneous thermometers using both a native Thermometer form object and a picture-based alternative.

## Key Points

- Explains why a thermometer object in the same process as a long task won't redraw: a busy process only services window updates when it idles for an interface event
- Standard fix is a dedicated display process created just to own the thermometer dialog; the busy process pushes progress via a global variable rather than driving the UI itself
- Compares two update strategies: an On Timer event redrawing every 60 ticks (simple but wasteful) versus the working process explicitly calling CALL PROCESS to trigger an On Outside call event in the display process (the recommended approach)
- M_Thermo_Create's system parameter selects among four combinations: native Thermometer object vs. a scaling picture (for custom artwork), each paired with the On Timer or On Outside call update mechanism
- The thermometer form object must be explicitly set non-enterable, since it is user-editable by default and could otherwise be dragged by the user during the task
- M_ThermoMulti_* extends the pattern to a single resizable dialog showing up to 5 simultaneous progress bars, using synchronized interprocess arrays (message + value per slot, -1 marking a free slot) so concurrent tasks share one window instead of one each
- Warns that SET PROCESS VARIABLE / CALL PROCESS against an arbitrary or stale process number is dangerous, and developers must be careful to target the correct process

## Featured Technology

- Dedicated display process for a progress dialog
- Interprocess/global variables updated cross-process
- CALL PROCESS / SET PROCESS VARIABLE / VARIABLE TO VARIABLE
- On Timer vs. On Outside call update strategies
- 4D Thermometer form object and picture-based alternative
- Multi-thermometer single-dialog management

## Historical Commentary

**Status:** Still Relevant

The fundamental constraint this note addresses — a busy 4D process cannot redraw its own UI — is still true in current 4D, so the core pattern of a dedicated display process communicating via shared/interprocess variables and CALL PROCESS remains a legitimate technique today. Modern 4D has since added richer tools for cross-process communication (shared objects/collections, worker processes) that can simplify some of the plumbing shown here, but the specific problem and general architecture of this note have not been superseded by a single built-in 'just works' progress bar API.

**References to newer/updated information:**
- 4D has since added shared objects/collections and worker-process patterns that can simplify cross-process data sharing compared to the raw interprocess-variable approach shown here
- The core technique — a dedicated display process updated via CALL PROCESS because a busy process cannot redraw its own UI — remains valid and in use in current 4D applications
