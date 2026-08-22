# Tech Note 07-22: Building Applications with 4D 2004: Automatic Client Upgrade

**Author:** Josh Fletcher, Technical Support Engineer, 4D Inc.
**Published:** June 6, 2007 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=46638
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_22-25_(JUN)/07-22_Auto_Client_Upgrade.pdf

## Overview
This note explains the automatic client upgrade feature introduced in 4D 2004, which lets a merged 4D Server force a full client-software upgrade (a new 4D Client image, not just method/form/resource updates) onto connecting clients, distinguishing "update" (long supported) from "upgrade" (new in 2004).

## Key Points
- Defines key terms: compiled (.4DC) apps, merged/double-clickable client-server apps, per-user Client Cache location (Windows and Mac OS paths given), Install Image, Install Client, and Upgrade Client.
- Enabled/disabled via the Build Application XML key `<BuildCSUpgradeable>`; version behavior tuned via `<CurrentVers>`, `<RangeVersMin>`, and `<RangeVersMax>` (the latter two only settable via a custom build project file, not the Build Application dialog).
- Flowcharts show: a version mismatch (or out-of-range version) triggers a prompt to upgrade; a 4D-version mismatch always blocks connection regardless of the current-version check.
- Upgrade process: merged client quits → a platform script deletes the old client → extracts the upgrade client from "archive.win"/"archive.mac" in an "Upgrade4DClient" folder → relaunches; the local client cache is preserved throughout.
- Cross-platform build note: a Windows machine can build a Mac *upgrade* client but not a Mac *install* client, and vice versa.
- Customization options: (1) modify the install image — any files added to the 4D Client/Server/single-user folder are automatically included in the merged build; (2) modify the platform upgrade scripts (`upgclnt.bat` on Windows, `Upgclnt.sh` on Mac OS) — explicitly flagged as undocumented and subject to change, with suggested uses like launching a full installer or showing release notes.

## Featured Technology
- 4D Build Application XML keys (BuildCSUpgradeable, CurrentVers, RangeVersMin/Max)
- Merged 4D Client/Server applications (.4DC compiled structures)
- Platform-specific upgrade install scripts

## Historical Context
Published June 2007, this note describes 4D 2004-era client/server deployment mechanics — merged double-clickable applications built via the classic Build Application dialog/XML keys — from just before 4D v11 introduced 4D's first native SQL engine later that same year. It predates Project Mode (2018) and any web-based client deployment model.

## Historical Commentary
**Status:** Historical interest only

The general concept of automatically forcing client software upgrades in a client/server deployment remains conceptually relevant to any distributed application today, but the concrete mechanism described — merged .4DC client applications, Build Application XML keys, and batch/shell upgrade scripts — is specific to 4D's pre-Project-Mode deployment model of that era. 4D's build and deployment tooling has evolved considerably since, and many modern deployments favor other distribution approaches, making this note primarily useful as a historical reference rather than a current how-to.
