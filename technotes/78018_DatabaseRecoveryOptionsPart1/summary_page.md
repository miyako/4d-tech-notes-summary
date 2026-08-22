# Tech Note 18-09: 4D Database Recovery Options – Part I

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** May 14, 2018 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78018
**Download:** https://kb.4d.com/DLTN/TN/2018/18-09_DatabaseRecoveryOptionsP1.pdf

## Proposition
Provides a general-purpose overview of 4D's disaster-recovery toolkit — the Maintenance and Security Center, the backup system, restores/rollbacks, and mirroring — as the first of a two-part series aimed at minimizing downtime when a 4D database is damaged.

## Key Points
- **Structure vs. data file:** a classic 4D database is composed of a structure file (.4DB format) and a separate data file, each of which can be independently damaged.
- **MSC Verify:** checks database integrity to detect corruption before it causes bigger problems.
- **MSC Repair:** attempts to fix a damaged data file when corruption is detected, serving as the first response to moderate damage.
- **Backup system fundamentals:** covers preparing/scheduling backups as the foundation for any recovery strategy.
- **Restore and rollback:** restoring from a backup recovers from severe damage, while rollback specifically allows undoing unwanted data changes.
- **Mirroring for high availability:** setting up a mirror server involves identifying the mirror, generating logs, sharing logs with the mirror, and integrating them continuously.
- **Chained/multiple mirrors:** mirrors can be layered (a mirror for a mirror) or multiplied for organizations needing near-zero downtime, such as a hospital database.

## Featured Technology
- Maintenance and Security Center (MSC)
- 4D backup system and log files
- Restore / Rollback
- Mirroring (mirror server setup and log integration)
- .4DB / data file structure

## Best Practices Highlighted
1. Run MSC Verify regularly to catch corruption early, before a full Repair or restore becomes necessary.
2. Maintain a robust, scheduled backup strategy as the baseline safety net for any 4D deployment.
3. For mission-critical systems (e.g., healthcare), consider mirroring — potentially with chained/multiple mirrors — to achieve continuous uptime.

## Context / Positioning
Published in 2018 but targeting 4D v16, this note reflects the classic "binary structure file" era of 4D database administration, prior to Project Mode's text-based .4DProject format (introduced starting v17 and refined afterward). It is a foundational operations/DBA-oriented note rather than a developer-facing feature note, aimed at consultants and system administrators responsible for keeping 4D deployments running.

## Historical Commentary
**Status:** Still relevant

The fundamental disaster-recovery building blocks described here — MSC Verify/Repair, backups, restores/rollbacks, and mirroring for high availability — remain part of 4D Server's data-protection architecture today, so the conceptual guidance in this note is still broadly sound. Mirroring in particular continues to be 4D's primary mechanism for continuous availability and disaster recovery.

That said, the note is written entirely in terms of the classic binary structure file (.4DB) model; 4D's later Project Mode (text-based .4DProject, Git-friendly) changes how structure files are versioned and recovered from source control, a scenario this note does not address at all since it predates that transition. The MSC interface and some mirroring setup details have also been refined in subsequent 4D releases, so an administrator should cross-check current documentation for exact steps, but the strategic framework (verify → repair → backup/restore → mirror) remains the right mental model.
