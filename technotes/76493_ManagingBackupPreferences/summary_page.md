# Tech Note 12-04: Managing Backup Preferences and Files

**Author:** Charles "Charlie" Vass, Technical Services Team Member, 4D Inc.
**Published:** February 28, 2012 | **Product/Version:** 4D v12.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76493
**Download:** https://kb.4d.com/DLTN/TN/2012/12-04_ManageBackPrefs.zip

## Proposition
This Tech Note addresses the often-overlooked problem of managing the Backup.XML preference file when deploying distributed/merged 4D applications, providing both manual techniques and a BKP_Manager component to create, preserve, or configure backup preferences independent of the native Backup Preferences dialog.

## Key Points
- 4D creates/maintains the Backup.XML file relative to the structure file location, which becomes problematic when deploying merged applications with separately located data files.
- Copying an entire "Preferences" folder during deployment risks pulling in unwanted build artifacts (e.g., the XML project file).
- Presents three approaches: copy/restore an existing Backup.XML, programmatically build a new Backup.XML, and an alternative "Backup.XML2" concept.
- The BKP_Manager component automates the most sophisticated of these tasks and is demonstrated with a full demo database (separate Data/Structure folders).
- Covers client/server interaction, an Advance Settings configuration dialog, and processing logic for applying chosen backup settings.
- Written to be compiler-friendly, allowing optional inclusion of the component without hard dependencies.

## Featured Technology
- Backup.XML preference file management
- BKP_Manager component
- Merged/distributed 4D application deployment
- Client/server backup preference handling

## Best Practices Highlighted
1. Test and explicitly manage backup preferences as part of the deployment process, not as an afterthought.
2. Avoid blindly copying the entire Preferences folder during deployment; selectively manage only the needed files.
3. Design components to be optionally includable in a compiler-friendly way so host applications aren't forced into a hard dependency.

## Context/Positioning
Published in 2012 for 4D v12.3, this note filled a real gap in deployment documentation around an easily overlooked but customer-impacting aspect of distributing merged 4D applications: correct backup configuration.

## Historical Commentary
The core problem this note solves — managing backup configuration separately from the native dialog for distributed applications — remains a legitimate and largely unchanged concern in current 4D development, since 4D's Backup.XML mechanism has not been fundamentally restructured. The technique is therefore still directly usable, though many modern deployments now supplement or replace native backup preference management with infrastructure-level strategies such as cloud storage snapshots or managed database backup services.

**Status:** Still relevant
