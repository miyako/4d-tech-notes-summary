# Tech Note: Inside the Runtime Explorer (TN 00-15)

**Author:** Jean-Yves Fock-Hoon, ACI Technical Support
**Published:** March 1, 2000 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11949
**Download:** https://kb.4d.com/DLTN/TN/2000/MacOS/TN_2000_11-15_(MAR)/00-15_Runtime_Explorer.hqx

## Overview
This Tech Note covers a deep dive into the classic Runtime Explorer debugging window (Watch, Process, Break, and Catch pages) and how to interpret its memory cache statistics.

## Key Points
- It describes the window's four pages — Watch, Process, Break, and Catch — with detailed focus on the Watch page, which surfaces the list of variables and inter-process variables for a selected process, all running processes application-wide, current record/selection counts per table, existing local semaphores, visible sets, visible named selections, and general application information such as memory load and free memory.
- A substantial portion of the note is devoted to explaining the memory cache statistics displayed on the Watch page in detail: the overall cache fill ratio (e.g., "2258Kb/4096Kb (55%)"), the Global hit ratio (how often 4D satisfies operations from cache rather than disk), and per-category breakdowns for Records, Index pages, and Transaction data, each with worked numeric examples showing how to interpret the reported percentages and derive absolute KB figures.
- The featured technology is 4D's classic in-memory cache architecture and the Runtime Explorer's introspection into it, including 4D's automatic cache-flush behavior (writing cached data to disk every 20 minutes, per Database Properties settings, or whenever cache occupancy exceeds 80%).
- This kind of note was invaluable to developers doing performance tuning and troubleshooting, since correctly interpreting cache hit ratios and memory usage let them decide whether increasing the cache size, adjusting indexing, or restructuring transactions would meaningfully improve application responsiveness.
- As a deep technical explainer of internal engine behavior rather than a simple how-to, this note remains a good illustration of the level of engine transparency 4D exposed to developers even in this comparatively early version, well before more modern profiling and debugging tools existed.

## Featured Technology
- Runtime Explorer
- Memory cache statistics
- Processes/Watch/Break/Catch debugging pages
- Sets and named selections

## Historical Context
This note is a detailed technical explanation of the classic Runtime Explorer debugging tool's Watch page and cache-statistics reporting, giving developers a way to inspect variables, processes, sets, named selections, and memory cache efficiency inside the Design Environment. The Runtime Explorer as a distinct named tool from this era has been superseded by 4D's substantially evolved and expanded modern debugger and execution-monitoring tools, but the underlying diagnostic concepts (watching variables/processes, understanding cache hit ratios, inspecting sets and selections) remain conceptually similar to what 4D's current debugging and performance tools expose, even if the exact window and shortcut (CTRL+Shift+F9) described here no longer match the current interface. Related updates since: 4D's debugging tools have been substantially rebuilt and expanded since this era, including the modern 4D Debugger and execution/profiling tools that supersede the classic Runtime Explorer window described here; The specific memory-cache statistics model and exact keyboard shortcut described are tied to 4D v6.5-era internals and may not directly match current 4D versions.
