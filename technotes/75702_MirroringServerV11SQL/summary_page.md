# Tech Note 09-16: Mirroring with 4D Server v11 SQL

**Author:** Atanas Atanassov, Technical Services Team Member, 4D Inc.
**Published:** April 23, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75702
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_13-17_(APR)/09-16_Mirroring.zip

## Proposition
This note introduces a component-based log-file mirroring solution for 4D Server v11 SQL, continuously replicating data changes from a principal server to a mirror server for high availability, so that critical always-on deployments (hospitals, police/fire) never need to put the operational database into read-only mode for backups.

## Key Points
- **Mirroring model:** the principal server segments its log file at intervals and sends each segment to the mirror, which integrates it — the principal never runs a backup itself and stays read-write at all times.
- **Backups run safely on the mirror instead**, with 4D automatically locking the mirror during log integration or its own backup to prevent desynchronization (these two operations are mutually exclusive).
- **Only data changes are mirrored** — structural changes to the database are not, making mirroring unsuitable for databases still under active structural development.
- **SOAP-based entry points:** the mirroring component publishes project methods as SOAP web services (requiring the 4D Web Services Server Expansion License), using the "Offered as a web service"/"Published in WSDL" method properties and RPC/DOC publication modes.
- **Setup covers:** installing the component and host database methods, and configuring Mirrors, Scheduling, Error Handling, and Backup preference tabs.

## Featured Technology
- 4D Server database mirroring (log-file-based replication)
- SOAP web services (used for mirror configuration/entry points)
- 4D component architecture (shared component methods)
- 4D log file segmentation and integration

## Best Practices Highlighted
1. Reserve mirroring for stable, already-deployed databases rather than ones still undergoing active structural changes, since structure changes aren't mirrored.
2. Perform backups on the mirror server rather than the principal, to keep the operational database continuously available.
3. Schedule and monitor mirroring via the dedicated preferences tabs (Scheduling, Error Handling) rather than relying on ad hoc manual processes.

## Context / Positioning
Published to address genuine high-availability needs for always-on 4D deployments, this note gave developers a documented path to database mirroring using the web-services infrastructure (SOAP) that was the standard 4D integration mechanism at the time.

## Historical Commentary
**Status:** Partially Superseded

This note introduced 4D v11 SQL's log-file-based database mirroring component, letting a mirror server stay continuously synchronized with a principal server for high availability without blocking the operational database for backups — a genuinely important capability for always-on deployments. The high-availability mirroring concept itself remains valid, and 4D has continued to develop native mirroring/replication capabilities in subsequent versions.

However, the specific SOAP-based component and entry-point mechanism shown here reflects 4D's pre-REST web services era and would today more likely be built on 4D's newer, more integrated replication features or a REST-based control layer rather than hand-rolled SOAP web services.
