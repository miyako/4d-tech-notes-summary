# Tech Note 18-08: Server Process Activity Component

**Author:** Kristopher Merolla, Technical Services Engineer, 4D Inc.
**Published:** May 14, 2018 | **Product/Version:** 4D v16 R4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78017
**Download:** https://kb.4d.com/DLTN/TN/2018/18-08_ServerProcessActivity.zip

## Proposition
Builds a custom server-monitoring component around the `Get process activity` command (new in v16 R4), giving developers a filterable, graphable, loggable window into 4D Server sessions and processes beyond what native monitoring tools expose.

## Key Points
- **Get process activity command:** returns Sessions and Processes objects covering connected user sessions and their associated running processes, including internal processes not visible to PROCESS PROPERTIES.
- **Existing tools vs. component:** explicitly compares 4D's built-in Process Manager to the custom component, justifying the custom build for tailored dashboards.
- **Processes_Display form:** an interactive listbox-based UI with Init_Form/Update_Form driving live refresh.
- **Filtering and sorting:** Manage_Lists, Filter_Listbox, and Manage_Arrows methods let users narrow down and sort visible sessions/processes.
- **CPU graphing:** Sort_Two_Arrays_And_Graph and Graph_CPU_Top_5 visualize the top 5 CPU-consuming processes.
- **Dual-format logging:** Set_Log_Location, Log_Manager, and Data_Logger methods write both JSON and plain-text logs, with sample outputs of each shown.
- **Drop-in and startup-launchable:** designed to be added to any database (v16 R6+) and started automatically on server boot.

## Featured Technology
- `Get process activity` command
- Form objects / listboxes
- Workers (background execution)
- JSON and TEXT logging (`Create document`, `Append document`)

## Best Practices Highlighted
1. Use `Get process activity` rather than polling PROCESS PROPERTIES when internal server processes must also be visible.
2. Separate display/filtering logic (listbox methods) from data-collection and logging logic for maintainability.
3. Support multiple log output formats (JSON for machine consumption, text for humans) from the same logging pipeline.

## Context / Positioning
Published in the v16 R4/R6 era, this note showcases a relatively new (at the time) server-introspection command layered on top of classic form/listbox UI techniques, worker-based background execution, and manual JSON/text log writing — all typical of 4D's pre-Project-Mode, pre-ORDA development style circa 2017-2018.

## Historical Commentary
**Status:** Still relevant

`Get process activity` remains part of the 4D language and is still the recommended way to build custom server-monitoring dashboards that need visibility into internal processes; the technique demonstrated here is directly usable today. Workers and preemptive processing, also referenced in the note, remain current 4D concepts as well.

What is dated is mostly the surrounding implementation style: classic listbox-driven forms, manual array sorting for graphing, and hand-rolled JSON/text logging routines reflect 2017-era 4D coding conventions rather than the class-based, more declarative patterns favored in modern 4D projects. Additionally, 4D's own built-in server administration and monitoring tools have continued to improve in subsequent releases, which may reduce (though not eliminate) the need for a fully custom component like this one for some use cases.
