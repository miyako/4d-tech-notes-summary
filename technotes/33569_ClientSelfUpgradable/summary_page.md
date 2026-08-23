# Tech Note: Client Self-Upgradable

- **Asset ID:** 33569
- **Tech Note #:** 04-32
- **Published:** August 12, 2004
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Jonathan Le (Technical Support, 4D, Inc.)
- **Page URL:** https://kb.4d.com/assetid=33569
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_31-35_(JUL)/04-32_ClientSelfUpgradable.hqx

## Overview

Written by Jonathan Le, this note documents a 4D 2004 feature for building fully stand-alone client and server executables from a database -- no longer requiring separately installed 4D Server or 4D Client applications -- and, crucially, for making those client executables able to detect and automatically upgrade themselves over the network when the server has been rebuilt at a newer version. It explains the Build Application tool's dialog (accessed via Design > Build Application), covering the 'Build Client-Server Application' and 'Allow automatic update of client application' checkboxes, the numeric Current version field, and the 4D Server/4D Client Folder (Win and Mac) path fields needed to produce cross-platform upgradeable clients. It documents the relevant BuildApp.xml project-file keys under Preferences4D/BuildApp/CS -- BuildServerApplication, BuildCSUpgradable, CurrentVers, IPAddress, PortNumber, HardLink, RangeVersMin, and RangeVersMax -- and the new BUILD APPLICATION command that can trigger a build programmatically from a specified (or default) project file. A hands-on walkthrough builds a demo database at version 1, then rebuilds the server at version 2 and shows the backed-up version-1 client being prompted to upgrade itself automatically, then demonstrates setting RangeVersMin/RangeVersMax so that clients within an allowed version range can connect without being forced to upgrade.

## Key Points

- The Build Application tool can produce fully stand-alone client and server executables that run independently of any separately installed 4D Client/Server application.
- Checking 'Allow automatic update of client application' and setting a Current version number in the Build Application dialog enables clients to detect a newer server version and upgrade themselves automatically over the network.
- 4D Client Folder Win and 4D Client Folder Mac path fields let a single build produce upgradeable clients for both platforms, provided 'Compile for both platforms' is enabled in the compiler preferences.
- BuildApp.xml (found in Preferences/BuildApp) exposes client/server keys under Preferences4D/BuildApp/CS: BuildServerApplication, BuildCSUpgradable, CurrentVers, IPAddress, PortNumber, HardLink, RangeVersMin, and RangeVersMax.
- The new BUILD APPLICATION command programmatically triggers a build from a given (or default) XML project file, setting the OK variable to reflect build success.
- RangeVersMin/RangeVersMax let a server accept connections from a range of older client versions without forcing an upgrade, while clients below the minimum are required to upgrade first.

## Featured Technology

- Build Application tool (client/server stand-alone build)
- BUILD APPLICATION command
- Client self-upgradeable versioning (CurrentVers, RangeVersMin, RangeVersMax)
- BuildApp.xml project file client/server (CS) XML keys

## Historical Commentary

**Status:** Historical Interest Only

This note documents the 4D 2004-era Build Application workflow for producing stand-alone, self-upgrading Client/Server executables, a genuinely useful deployment convenience at the time since it removed the need to distribute and manually update separate 4D Client installations. The Build Application tool and its BuildApp.xml/BUILD APPLICATION mechanics have evolved substantially since 2004 (structure/data file formats, project architecture, and deployment options have all changed across two decades of 4D releases), so while the general concept of self-updating deployed clients persists, the specific XML keys, tool dialog, and workflow described here no longer match current 4D build tooling and are mainly of historical interest.

**References to newer/updated information:**
- 4D's Build Application tool and its project file format have been substantially revised across many releases since 2004; the specific BuildApp.xml CS keys documented here do not directly map to current build tooling
- 4D has introduced Project mode and newer deployment/versioning mechanisms since this note was written
- The general concept of self-upgrading deployed client applications is still supported by 4D's current build and update tooling, using updated mechanisms rather than the 2004-era keys shown here
