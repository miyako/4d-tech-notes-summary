# Tech Note 18-14: 4D Database Recovery Using Backups and Mirroring – Part II

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** July 20, 2018 | **Product/Version:** 4D v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78094
**Download:** https://kb.4d.com/DLTN/TN/2018/18-14_DatabaseRecoveryOptionsP2.pdf

## Proposition
Part I covered backups and general mirror setup at a high level. Part II goes in-depth into how 4D's mirroring feature actually operates (log shipping between principal and mirror servers) and, critically, exactly how to recover a damaged database using a mirror's datafile plus the principal's current log file.

## Key Points
- **Mirror architecture:** two full 4D Server copies on separate physical machines — a principal (active) database and a mirror (standby) database, distinguished by startup logic (e.g., a marker file check).
- **Hot vs. warm standby:** hot standby fully synchronizes every operation immediately; warm standby synchronizes periodically. 4D mirrors are typically configured as warm standby, which the architecture makes low-risk.
- **Log-shipping mechanics:** operations on the principal are continuously logged; `New log file` periodically closes the current log and starts a new one; closed logs are transferred to the mirror.
- **Mirror replication:** the mirror periodically applies received logs to its datafile using `Integrate Mirror Log File`, keeping it a near-real-time replica.
- **Recovery trigger scenario:** an event (e.g., ungraceful shutdown) corrupts the principal's datafile, making it untrustworthy.
- **Recovery process:** use the mirror's (trusted) datafile combined with the principal's intact current log file, integrating the remaining un-shipped operations to reconstruct a fully up-to-date datafile.
- **Manual integration path:** run `Integrate Mirror Log File` on the still-running mirror, then carefully pair the updated datafile with its correctly-renamed log file (`{databaseName}.journal`) before moving both back to the principal machine.
- **Final step:** restart both the production and mirror servers once the datafile/log pair is restored correctly.

## Featured Technology
- 4D mirroring (principal/mirror server architecture)
- `New log file`
- `Integrate Mirror Log File`
- 4D's current log file (`.journal`) / transaction logging system

## Best Practices Highlighted
1. Host principal and mirror servers on physically separate machines to avoid a single hardware failure taking down both copies.
2. Keep log-shipping intervals short enough that the warm-standby mirror stays close to current, minimizing recovery-time log integration.
3. When manually integrating logs, always keep the datafile and its corresponding log file paired and correctly renamed before relocating them, to avoid corrupting the recovery.
4. Restart both production and mirror servers only after confirming the recovered datafile/log pair is correctly in place.

## Context / Positioning
As part of a two-part series, this note reflects 4D's ongoing emphasis on giving developers concrete operational playbooks — not just feature descriptions — for keeping mission-critical 4D databases available, at a time when many customers were running always-on business applications on 4D Server.

## Historical Commentary
**Status:** Still relevant

4D's mirroring architecture — principal/mirror servers, warm-standby log shipping via `New log file` and `Integrate Mirror Log File`, and recovery by pairing a mirror's datafile with the principal's current log — remains fundamentally unchanged and still accurate today. This is a solid, durable operational reference.

4D has since added more built-in tooling and guided configuration for setting up and monitoring mirrors within the Server administration interface, making some of the manual setup described easier to achieve through UI rather than custom startup-logic code, but the underlying recovery mechanics documented here (and the commands referenced) remain valid, and understanding this manual process is still valuable for diagnosing or executing recovery when automated tooling isn't available or sufficient.
