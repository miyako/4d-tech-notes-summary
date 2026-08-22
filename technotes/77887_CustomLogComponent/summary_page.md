# Tech Note 17-21: Custom Log Component

**Author:** Add Komoncharoensiri – Director of Technical Services, 4D Inc.
**Published:** November 16, 2017 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77887
**Download:** https://kb.4d.com/DLTN/TN/2017/17-21_CustomLogsR2.zip

## Proposition
This Tech Note provides a reusable custom logging component (`customLogs`) for 4D v16 databases, offering simple text and JSON log file formats. It uses the new CALL WORKER command and preemptive-process design to safely serialize concurrent writes without semaphores or flag variables.

## Key Points
- **Two log formats:** simple sequentially-numbered text logs and structured JSON logs, sharing a common naming convention (`log_YYYYMMDD_ssss`).
- **Automatic rotation:** log files are capped at a default 10 MB and rotated automatically into new files.
- **Storage location:** logs are written to a `Logs` folder next to the host structure file.
- **Concurrency safety:** uses `CALL WORKER` to funnel all log writes through a single dedicated worker process, avoiding race conditions.
- **Modernized vs. older techniques:** replaces pre-v16 patterns that relied on semaphores/flag variables to coordinate log writes across processes.
- **General purpose:** designed to be dropped into any v16 database needing custom log messages beyond 4D's built-in logging options.

## Featured Technology
- CALL WORKER command
- Preemptive process programming
- Custom component architecture
- JSON and delimited text file formats

## Best Practices Highlighted
1. Serialize all writes to a shared log file through a single worker process rather than using semaphores.
2. Rotate log files at a defined size threshold to keep individual files manageable.
3. Store logs in a predictable, discoverable location (Logs folder near the structure file).

## Context / Positioning
Published in late 2017 under classic 4D v16 (pre-Project Mode, pre-ORDA maturity), this note reflects the "classic 4D" era where components were built from regular 4D methods rather than classes, and CALL WORKER/preemptive processes were still a relatively new concurrency tool introduced around v15-v16.

## Historical Commentary
**Status:** Still relevant

The underlying problem — safely serializing writes to a shared log file from multiple concurrent processes — is timeless, and the CALL WORKER-based solution shown here remains a valid, still-used technique in current 4D versions. What has dated is the implementation style: a modern equivalent would likely encapsulate the logger as a 4D class (possibly a shared singleton) introduced in later Project Mode-era 4D rather than as a loose method-based component, but the conceptual approach requires no correction.
