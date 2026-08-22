# Tech Note 20-01: A Technique to Rebuild a Data File

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** January 29, 2020 | **Product/Version:** 4D v18 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78397
**Download:** https://kb.4d.com/DLTN/TN/2020/20-01_DataFileReconstruction.zip

## Proposition
Rather than restoring from backup or performing risky low-level repairs, this note shows how to rebuild a clean, compacted datafile from an existing one by repurposing 4D Server's mirroring/journal infrastructure — refreshing every record into a fresh log file, then replaying that log into a brand-new empty datafile.

## Key Points
- **`New log file`**: creates a fresh, empty journal file to capture a full data snapshot as a sequence of update events.
- **Forcing a full record snapshot**: looping `ALL RECORDS`/`NEXT RECORD` and re-saving each record generates Create/Update events in the journal for every record of a selected table.
- **Picture/Blob caveat**: these field types are only journaled when specifically modified, so affected fields must be explicitly reassigned (detected via `GET FIELD PROPERTIES`) to ensure they're captured.
- **`CREATE DATA FILE`**: spins up a brand-new empty datafile and restarts the database against it.
- **`INTEGRATE MIRROR LOG FILE`** (auto-repair mode): replays the journal into the new empty datafile, requiring 4D Server.
- **Sample component UI**: table selection, "Automatically Rebuild" (auto-restart and integrate on startup), and "Separate Journals For Each Table" (parallelizable per-table journals) options.

## Featured Technology
- 4D Server mirroring / journal (log) files
- `New log file`, `INTEGRATE MIRROR LOG FILE`, `CREATE DATA FILE`
- `GET FIELD PROPERTIES`, `GET TABLE TITLES`

## Best Practices Highlighted
1. Explicitly reassign Picture/Blob fields during the log-generation pass to work around the known journal-capture limitation for these types.
2. Use "Separate Journals For Each Table" only when preemptive multi-core processing per table is acceptable, since combined single-journal generation is faster overall but sequential.
3. Verify tables have zero records post-`CREATE DATA FILE` before integrating logs, to confirm a clean starting point.

## Context / Positioning
This note showcases advanced, creative reuse of 4D Server's mirroring feature for a purpose (datafile reconstruction/compaction) beyond its primary intended use (live backup redundancy), reflecting the kind of expert-level technique 4D's technical support team shared to help large production deployments maintain data file health without full backup restores.

## Historical Commentary
**Status:** Still relevant

The commands this technique relies on — `New log file`, `INTEGRATE MIRROR LOG FILE`, `CREATE DATA FILE` — remain part of current 4D Server with no deprecation, so the approach is technically still usable today. It remains a fairly advanced/niche maintenance technique requiring 4D Server and careful understanding of mirroring semantics (and the ongoing Picture/Blob journaling caveat, if it still applies in current versions, should be re-verified against current documentation). For most teams, standard backup/restore and 4D's structure verification tools remain the primary recommended path to data file health, with this technique serving as a supplementary option for corruption recovery or compaction when a suitable backup isn't available.
