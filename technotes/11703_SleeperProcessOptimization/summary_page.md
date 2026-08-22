# Tech Note 96-23: Optimizing Process Management Using a Sleeper Process

**Author:** Forrest Swilling
**Published:** May 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11703
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_22-26_(MAY)/96-23_Sleeper_Process.exe

## Overview
This Tech Note describes a simple but powerful technique — using a paused "sleeper" process — to handle routine procedural tasks more efficiently in 4th Dimension, improving both modelessness (letting the user work across multiple tasks freely) and reducing the memory/performance overhead of constantly launching new processes.

## Key Points
- **Modelessness vs. overhead:** 4D's multi-process design is ideal for modeless interaction, but every new process requires memory for process variables plus a current selection per file — a cost magnified under 4D Server due to network communication.
- **The technique:** Launch a process and immediately pause it; when work is needed, resume it, hand it an action to run, then let it pause itself again when done.
- **Three procedures:**
  - `LaunchSleeper` — launches the sleeper process and stores its process ID.
  - `Sleeper` — loops forever: hides and pauses itself, and upon resume executes whatever is stored in the shared variable `àSleepAction`.
  - `WakeUpSleeper($1)` — sets `àSleepAction` to the requested action and resumes the sleeper.
- **Why PAUSE PROCESS, not CALL PROCESS:** avoids requiring a layout to sustain the process and uses fewer processor cycles.
- **Global process requirement:** the sleeper must be a global process since it typically needs access to record data shared across the application.
- **Extension ideas:** queue multiple actions via an interprocess array for batch work, add task prioritization, spin off additional sleeper processes under load, and log usage statistics to tune the ideal number of paused processes.

## Featured Technology
- 4D process management commands: `New process`, `PAUSE PROCESS`, `RESUME PROCESS`, `EXECUTE`
- 4D Server multi-user/network process overhead considerations

## Historical Context
Written in the 4D v3.x era (pre-V6, pre-Events/Methods terminology), this note addresses a real constraint of 1990s hardware and networked 4D Server deployments: process creation was comparatively expensive in memory and time. The specific commands used (`New process`, `PAUSE PROCESS`, `RESUME PROCESS`) remain part of the 4D language today, so the mechanics still technically work. However, on modern hardware the overhead this note targets is largely negligible, and later 4D versions introduced structured alternatives such as Worker processes (`CALL WORKER`) for managing background/reusable execution contexts, making a hand-rolled sleeper process pattern more of a historical curiosity than a necessary optimization for most contemporary applications.
